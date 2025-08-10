
projeto/
│
├── main.py                 # Ponto de entrada
├── hardware.py              # Inicialização de pinos, I2C e sensores
├── utils.py                 # Funções utilitárias (vibrar, média, etc.)
├── sensors.py               # Lógica de leitura e configuração de sensores
└── actions.py               # Ações executadas pelos sensores


a estrutura do meu progama está assim:

tar -czvf nome-do-arquivo.tar.gz pasta/
tar -czvf use.tar.gz use/


main.py
hardware.py
utils.py
sensors.py
actions.py


mpremote repl
mpremote fs ls
mpremote connect /dev/ttyUSB0 cp main.py :main.py
mpremote connect /dev/ttyUSB0 cp hw.py :hw.py
mpremote connect /dev/ttyUSB0 cp utils.py :utils.py
mpremote connect /dev/ttyUSB0 cp sensors.py :sensors.py
mpremote connect /dev/ttyUSB0 cp actions.py :actions.py
mpremote connect /dev/ttyUSB0 cp mpu6050.py :mpu6050.py


---

mpremote fs ls
mpremote rm nome_do_arquivo.py
mpremote rm hidcodes.py
mpremote rm hardware.py

rshell --port /dev/ttyACM0

ls /pyboard

mpremote fs ls

mpremote repl

mpremote connect /dev/ttyUSB0 cp arquivo_local.py :arquivo_remoto.py

mpremote connect /dev/ttyUSB0 cp main.py :main.py
mpremote connect /dev/ttyUSB0 cp mpu6050.py :mpu6050.py
mpremote connect /dev/ttyUSB0 cp gyro_utils.py :gyro_utils.py

mpremote connect /dev/ttyUSB0 cp pot_utils.py :pot_utils.py
mpremote connect /dev/ttyUSB0 cp input_handler.py :input_handler.py

mpremote connect /dev/ttyUSB0 cp hidcodes.py :hidcodes.py


mpremote connect /dev/ttyUSB0 cp arquivo_local.py :arquivo_remoto.py











---


Perfeito — vou te dar um plano passo‑a‑passo **prático** para modularizar esse código do ESP32 em arquivos menores (fácil de testar a cada mudança) e já te entregar o código pronto para copiar/colar em cada arquivo. Vou manter a lógica original, só que mais limpa, com injeção de dependências para facilitar testes.

### Plano (passos)

1. **`hw.py`** — inicializa hardware (I2C, MPU, vibrator, pots). Teste só esse arquivo primeiro.
2. **`utils.py`** — funções utilitárias: `vibrar`, `send_charPs`.
3. **`pots.py`** — leitura e calibração de TouchPad (buffer + calc).
4. **`gyro.py`** — leitura do MPU e cálculo da média deslizante.
5. **`main.py`** — junta tudo: rotina `start()` (seu loop principal) e `run()`.

Depois de cada passo eu te mostro como testar rapidamente no ESP (mpremote ou REPL).

---

# `hw.py`

```python
# hw.py
from machine import Pin, SoftI2C, TouchPad
import time

def init_i2c(scl_pin=22, sda_pin=21):
    return SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

def init_mpu(i2c):
    # importa aqui para evitar erro se rodar testes sem MPU
    try:
        import mpu6050
        mpu = mpu6050.MPU6050(i2c)
        return mpu
    except Exception as e:
        print("init_mpu erro:", e)
        return None

def init_vibrator(pin_no=33):
    p = Pin(pin_no, Pin.OUT)
    try:
        p.off()
    except Exception:
        pass
    return p


def init_pots(pins=(13,12,14,27,4)):
    return [TouchPad(Pin(p)) for p in pins]

# teste rápido:
if __name__ == "__main__":
    i2c = init_i2c()
    mpu = init_mpu(i2c)
    vib = init_vibrator()
    pots = init_pots()
    print("hw init done, mpu:", bool(mpu), "pots:", [type(p) for p in pots])
```

# `utils.py`

```python
# utils.py
import time

def send_charPs(abckey):
    # placeholder: aqui você conecta ao HID/USB quando for integrar.
    print("send_charPs ->", abckey)

def vibrar(pino_vibracao, n_pulsos, step=None):
    if pino_vibracao is None:
        print("vibrador não inicializado")
        return
    for _ in range(n_pulsos):
        try:
            pino_vibracao.on()
        except Exception:
            # alguns firmwares usam value(1)/value(0)
            try: pino_vibracao.value(1)
            except: pass
        if step == 0:
            time.sleep_ms(200)
        else:
            time.sleep_ms(101)
        try:
            pino_vibracao.off()
        except Exception:
            try: pino_vibracao.value(0)
            except: pass
        time.sleep_ms(70)
```

# `pots.py`

```python
# pots.py

def add_pot_samples(bufferPot, pval):
    """bufferPot: list de listas; pval: lista com leituras atuais"""
    for i, v in enumerate(pval):
        bufferPot[i].append(v)
    return bufferPot

def calc_calibrate(bufferPot):
    """Retorna lista com max por pot (ou 0 se vazio)"""
    maxCalc = []
    for potList in bufferPot:
        maxCalc.append(max(potList) if potList else 0)
    return maxCalc
```

# `gyro.py`

```python
# gyro.py

def append_gyro(buffer, mpuSensor):
    """Adiciona uma leitura ao buffer (6 listas)"""
    if mpuSensor is None:
        # evita crash se MPU não inicializou
        return buffer
    try:
        mpuData = mpuSensor.get_values()
    except Exception as e:
        print("MPU read error:", e)
        return buffer

    keys = ['GyX','GyY','GyZ','AcX','AcY','AcZ']
    for i, k in enumerate(keys):
        buffer[i].append(mpuData.get(k, 0))
    return buffer

def average_and_slide(buffer, mpuSensor):
    """Lê mais um valor, calcula média e remove o mais antigo (sliding window)"""
    append_gyro(buffer, mpuSensor)
    averages = []
    for lst in buffer:
        averages.append(sum(lst)/len(lst) if lst else 0)
    gyro = averages[:3]
    accl = averages[3:6]
    # remove o mais antigo para manter a janela
    for lst in buffer:
        if lst:
            lst.pop(0)
    return gyro, accl
```

# `main.py`

```python
# main.py
import time
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from utils import vibrar, send_charPs
from pots import add_pot_samples, calc_calibrate
from gyro import append_gyro, average_and_slide

def start(tsleep, tclear, samples,
          i2c=None, mpu=None, pots=None, vib=None):
    # inicializa hardware se não passado
    if i2c is None:
        i2c = init_i2c()
    if mpu is None:
        mpu = init_mpu(i2c)
    if vib is None:
        vib = init_vibrator()
    if pots is None:
        pots = init_pots()

    # --- calibracao de pots (40 amostras)
    bufferPot = [[] for _ in pots]
    for _ in range(40):
        pval = [pot.read() for pot in pots]
        print("pot sample:", pval)
        add_pot_samples(bufferPot, pval)
        time.sleep_ms(70)
    maxCalibratePots = calc_calibrate(bufferPot)
    print("maxCalibratePots:", maxCalibratePots)

    # --- prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    for _ in range(samples-1):
        append_gyro(buffer, mpu)
        time.sleep_ms(70)
    gyro, accl = average_and_slide(buffer, mpu)

    # variaveis do loop (copiei sua lógica original, mas mais legível)
    num = 0
    stepX = 0
    stepY = 0
    evntTriggeredXP = evntTriggeredXN = False
    evntTriggeredYP = evntTriggeredYN = False

    triggerPot = [False] * len(pots)
    threshPot = [-120] * len(pots)

    poragora = 14000
    thresPercentX = 0.1
    thresPercentY = 0.1
    limthresholdXP = poragora
    limthresholdXN = -poragora
    limthresholdYP = poragora
    limthresholdYN = -poragora
    threshXP = limthresholdXP - (limthresholdXP * thresPercentX)
    threshXN = limthresholdXN - (limthresholdXN * thresPercentX)
    threshP = limthresholdYP - (limthresholdYP * thresPercentY)
    threshN = limthresholdYN - (limthresholdYN * thresPercentY)

    wait2Zero = True
    cycle = 0
    stepWaitXP = stepWaitXN = stepWaitYP = stepWaitYN = 0

    gy1, gy2 = 0, 1  # eixos (pode inverter se precisar)

    vibrar(vib, 2)

    while True:
        gyro, accl = average_and_slide(buffer, mpu)

        # --- eixo X
        if not evntTriggeredXP and gyro[gy1] > threshXP:
            stepX = stepX + 1 if gy1 == 0 else stepX - 1
            vibrar(vib, 1, stepX)
            evntTriggeredXP = True
            wait2Zero = False
            cycle = 0
        elif evntTriggeredXP and gyro[gy1] <= threshXP:
            evntTriggeredXP = False
            wait2Zero = True

        if not evntTriggeredXN and gyro[gy1] < threshXN:
            stepX = stepX - 1 if gy1 == 0 else stepX + 1
            vibrar(vib, 1, stepX)
            evntTriggeredXN = True
            wait2Zero = False
            cycle = 0
        elif evntTriggeredXN and gyro[gy1] >= threshXN:
            evntTriggeredXN = False
            wait2Zero = True

        # auto-step X
        if evntTriggeredXP:
            stepWaitXP += 1
        else:
            stepWaitXP = 0
        if stepWaitXP >= 5:
            stepX = stepX + 1 if gy1 == 0 else stepX - 1
            stepWaitXP = 0
            vibrar(vib, 1, stepX)

        if evntTriggeredXN:
            stepWaitXN += 1
        else:
            stepWaitXN = 0
        if stepWaitXN >= 5:
            stepX = stepX - 1 if gy1 == 0 else stepX + 1
            stepWaitXN = 0
            vibrar(vib, 1, stepX)

        # --- eixo Y (mesma logica)
        if not evntTriggeredYP and gyro[gy2] > threshP:
            stepY = stepY + 1 if gy2 == 0 else stepY - 1
            vibrar(vib, 1, stepY)
            evntTriggeredYP = True
            wait2Zero = False
            cycle = 0
        elif evntTriggeredYP and gyro[gy2] <= threshP:
            evntTriggeredYP = False
            wait2Zero = True

        if not evntTriggeredYN and gyro[gy2] < threshN:
            stepY = stepY - 1 if gy2 == 0 else stepY + 1
            vibrar(vib, 1, stepY)
            evntTriggeredYN = True
            wait2Zero = False
            cycle = 0
        elif evntTriggeredYN and gyro[gy2] >= threshN:
            evntTriggeredYN = False
            wait2Zero = True

        # auto-step Y
        if evntTriggeredYP:
            stepWaitYP += 1
        else:
            stepWaitYP = 0
        if stepWaitYP >= 5:
            stepY = stepY - 1 if gy1 == 0 else stepY + 1
            stepWaitYP = 0
            vibrar(vib, 1, stepY)

        if evntTriggeredYN:
            stepWaitYN += 1
        else:
            stepWaitYN = 0
        if stepWaitYN >= 5:
            stepY = stepY + 1 if gy1 == 0 else stepY - 1
            stepWaitYN = 0
            vibrar(vib, 1, stepY)

        # --- pots
        pval = [pot.read() for pot in pots]
        # ajusta pelo calibrado
        for i in range(len(pval)):
            pval[i] = pval[i] - maxCalibratePots[i]

        if -1 <= stepX <= 1 and -2 <= stepY <= 2:
            abclevel = [stepX + 1, 2 - stepY]
        else:
            abclevel = None

        for i in range(len(pval)):
            if not triggerPot[i] and pval[i] < threshPot[i]:
                print("evento pot:", i, stepY, stepX, "->", abclevel, cycle)
                send_charPs(abclevel)
                triggerPot[i] = True
                holdclick = True
                wait2Zero = False
                cycle = 0
            elif triggerPot[i] and pval[i] >= threshPot[i]:
                triggerPot[i] = False
                holdclick = False
                wait2Zero = True

        # --- reset para zero se ficar idle
        if wait2Zero:
            cycle += 1
        if cycle >= 20:
            stepY = 0
            stepX = 0
            vibrar(vib, 2)

        if num % tclear == 0:
            num = 0
        num += 1
        time.sleep_ms(tsleep)


def run():
    vibrar(init_vibrator(), 4)
    TSLEEP = 50
    TCLEAR = 10000
    SAMPLES = 5
    start(TSLEEP, TCLEAR, SAMPLES)

if __name__ == "__main__":
    run()
```

---

# Como testar passo‑a‑passo (recomendo)

1. **Copiar** cada arquivo para o ESP (`mpremote cp hw.py :` etc.) ou colar no editor do Thonny.
2. **Passo 1 (hw):** no REPL ou com `mpremote run hw.py` — verifique `init` OK e que não dá exceção ao criar I2C/TouchPad.
3. **Passo 2 (utils):** crie small script `test_utils.py`:

   ```python
   from hw import init_vibrator
   from utils import vibrar
   v = init_vibrator()
   vibrar(v, 1)
   ```

   Rode e veja se vibra.
4. **Passo 3 (pots):** rode um script que use `init_pots()` e leia 10 valores, veja se variação faz sentido.
5. **Passo 4 (gyro):** rode um script que inicialize MPU e chame `append_gyro` e `average_and_slide`, imprima os valores para conferir se o MPU responde.
6. **Passo 5 (main):** rode `main.py` e observe prints — ajuste thresholds se necessário.

---

# Observações / dicas de debug (já que você comentou que *não está vibrando com giro*)

* **Imprima valores do gyro e thresholds** no início do loop para ver se `gyro[gy1]` realmente passa de `threshXP` (uma linha com `print(gyro, threshXP, threshXN)` ajuda muito).
* Confirme `mpuSensor` foi inicializado (se `init_mpu` retornou `None`, tudo falha silenciosamente).
* `TouchPad.read()` retorna valores “grandes” e você faz `pval - maxCalibratePots` — valide com `print` pra checar polaridade.
* Se vibração falha em certas condições, teste `vibrar(vib, 1)` isolado para garantir pino correto e hardware ok.
* Considere **reduzir** `poragora` durante testes (ex.: 2000) para ver facilmente eventos de giro.

---

Se quiser eu já te entrego os pequenos scripts de teste (`test_hw.py`, `test_utils.py`, `test_pots.py`, `test_gyro.py`) prontos, ou posso adaptar os módulos para usar debounce/filtragem diferente, ou ainda transformar o `main.start` em um estado‑machine mais testável. Qual próximo passo prefere: **receber os scripts de teste** ou **eu já aplico alguma otimização extra (ex.: ring buffer, log leve, thresholds configuráveis)**?
