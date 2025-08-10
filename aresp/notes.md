
projeto/
│
├── main.py                 # Ponto de entrada
├── hardware.py              # Inicialização de pinos, I2C e sensores
├── utils.py                 # Funções utilitárias (vibrar, média, etc.)
├── sensors.py               # Lógica de leitura e configuração de sensores
└── actions.py               # Ações executadas pelos sensores


a estrutura do meu progama está assim:

main.py
hardware.py
utils.py
sensors.py
actions.py

---

mpremote rm nome_do_arquivo.py
mpremote rm hidcodes.py

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

mpremote fs ls
mpremote connect /dev/ttyUSB0 cp main.py :main.py
mpremote connect /dev/ttyUSB0 cp hardware.py :hardware.py
mpremote connect /dev/ttyUSB0 cp utils.py :utils.py
mpremote connect /dev/ttyUSB0 cp sensors.py :sensors.py
mpremote connect /dev/ttyUSB0 cp actions.py :actions.py









---

/projeto/
│
├── main.py                # Arquivo principal, ponto de entrada
├── config.py              # Configurações e pinos
├── sensores.py            # Funções de leitura do giroscópio e touchpads
├── utils.py               # Funções auxiliares (ex: vibrar, media, calclim, etc)
├── interface.py           # Funções que lidam com os eventos (send_charPs)
└── hidcodes.py            # Já existente: mapeamento de códigos e layout abc







┌──────────────────────────────┐
│ run()                         │
│  - vibra 4 vezes              │
│  - define TSLEEP, TCLEAR, etc │
│  - chama start()              │
└─────────────┬────────────────┘
              │
              ▼
┌──────────────────────────────┐
│ start()                       │
│ 1. Calibra TouchPads          │
│    - lê 40x e salva valores   │
│    - pega valor máximo p/ ref │
│                                │
│ 2. Preenche buffer giroscópio │
│    - coleta SAMPLES iniciais  │
│                                │
│ 3. Define thresholds          │
│    - giros (XP, XN, YP, YN)   │
│    - pots (-120 fixo)         │
│                                │
│ 4. Vibra 2 vezes               │
│                                │
│ 5. Cria lista `sensors`       │
│    - gyroX                    │
│    - gyroY                    │
│    - pot1 ... pot5            │
└─────────────┬────────────────┘
              │
              ▼
      ┌─────────────────────┐
      │ LOOP infinito:      │
      └─────────────────────┘
              │
              ▼
┌─────────────────────────────────────────┐
│ 1. Lê stepX e stepY (posições giros)     │
│                                          │
│ 2. Calcula abclevel se dentro do limite  │
│    → [stepX+1, 2-stepY] ou None          │
│                                          │
│ 3. Para cada sensor em `sensors`:        │
│    ├─ lê valor atual (gyro ou pot)       │
│    ├─ chama check_sensor()               │
│    └─ se pot, ajusta action_pos p/ enviar│
│       nível ABC atual                    │
│                                          │
│ 4. Se gyroX e gyroY estão zerados tempo  │
│    suficiente (wait2Zero & cycle=20)     │
│    ├─ zera steps                         │
│    └─ vibra 2 vezes                      │
│                                          │
│ 5. Espera TSLEEP ms                      │
└─────────────────────────────────────────┘



Então vamos modularizar seu código para que ele fique mais organizado, fácil de manter e com menos repetição.
A ideia é separar em **módulos** conforme a responsabilidade:

---

## **Sugestão de Estrutura de Pastas**

```
projeto/
│
├── main.py                 # Ponto de entrada
├── hardware.py              # Inicialização de pinos, I2C e sensores
├── utils.py                 # Funções utilitárias (vibrar, média, etc.)
├── sensors.py               # Lógica de leitura e configuração de sensores
└── actions.py               # Ações executadas pelos sensores
```

---

## **1. hardware.py**

```python
import time
from machine import Pin, SoftI2C, TouchPad
import mpu6050

# Configuração I2C e sensor MPU6050
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpuSensor = mpu6050.accel(i2c)

# Motor vibrador
pino_vibracao = Pin(33, Pin.OUT)

# TouchPads
pots = [
    TouchPad(Pin(13)),
    TouchPad(Pin(12)),
    TouchPad(Pin(14)),
    TouchPad(Pin(27)),
    TouchPad(Pin(4))
]
```

---

## **2. utils.py**

```python
import time
from hardware import pino_vibracao, mpuSensor

def vibrar(n_pulsos, step=None):
    for _ in range(n_pulsos):
        pino_vibracao.on()
        time.sleep_ms(200 if step == 0 else 101)
        pino_vibracao.off()
        time.sleep_ms(70)

def getGyro(buffer):
    mpuData = mpuSensor.get_values()
    for i, key in enumerate(['GyX', 'GyY', 'GyZ', 'AcX', 'AcY', 'AcZ']):
        buffer[i].append(mpuData[key])
    return buffer

def media(buffer):
    getGyro(buffer)
    gyro = [sum(buffer[i]) / len(buffer[i]) for i in range(3)]
    accl = [sum(buffer[i]) / len(buffer[i]) for i in range(3, 6)]
    for i in range(6):
        buffer[i].pop(0)
    return gyro, accl

def calcCalibrate(bufferPot):
    return [max(potList) for potList in bufferPot]

def getPots(bufferPot, pval):
    for i in range(5):
        bufferPot[i].append(pval[i])
    return bufferPot
```

---

## **3. actions.py**

```python
from utils import vibrar

def action_vibrar(step):
    vibrar(1)

def send_charPs(abckey):
    print("send_charPs called with:", abckey)
```

---

## **4. sensors.py**

```python
import time
from hardware import pots
from utils import getPots, calcCalibrate, media, vibrar
from actions import action_vibrar, send_charPs

def check_sensor(value, thresh_pos, thresh_neg, state, holdclick):
    step = state["step"]
    tp = state["trigger_pos"]
    tn = state["trigger_neg"]
    swp = state["stepWait_pos"]
    swn = state["stepWait_neg"]
    wait2Zero = state["wait2Zero"]
    cycle = state["cycle"]

    if not tp and not holdclick and value > thresh_pos:
        step += state["dir_pos"]
        if state["action_pos"]:
            state["action_pos"](step)
        tp = True
        wait2Zero = False
        cycle = 0
    elif tp and value <= thresh_pos:
        tp = False
        wait2Zero = True

    if not tn and not holdclick and value < thresh_neg:
        step += state["dir_neg"]
        if state["action_neg"]:
            state["action_neg"](step)
        tn = True
        wait2Zero = False
        cycle = 0
    elif tn and value >= thresh_neg:
        tn = False
        wait2Zero = True

    if tp:
        swp += 1
    else:
        swp = 0
    if swp >= 5:
        step += state["dir_pos"]
        swp = 0
        if state["action_pos"]:
            state["action_pos"](step)

    if tn:
        swn += 1
    else:
        swn = 0
    if swn >= 5:
        step += state["dir_neg"]
        swn = 0
        if state["action_neg"]:
            state["action_neg"](step)

    state.update(step=step,
                 trigger_pos=tp,
                 trigger_neg=tn,
                 stepWait_pos=swp,
                 stepWait_neg=swn,
                 wait2Zero=wait2Zero,
                 cycle=cycle)
    return state

def start(tsleep, tclear, samples, getGyroFunc):
    bufferPot = [[] for _ in range(5)]
    for _ in range(40):
        pval = [pot.read() for pot in pots]
        getPots(bufferPot, pval)
        time.sleep_ms(70)
    maxCalibratePots = calcCalibrate(bufferPot)

    buffer = [[] for _ in range(6)]
    for _ in range(samples - 1):
        getGyroFunc(buffer)
        time.sleep_ms(70)

    poragora = 14000
    thresPercent = 0.1
    threshXP = poragora - (poragora * thresPercent)
    threshXN = -poragora + (poragora * thresPercent)
    threshYP = poragora - (poragora * thresPercent)
    threshYN = -poragora + (poragora * thresPercent)
    threshPot = [-120] * 5

    vibrar(2)

    sensors = [
        {
            "name": "gyroX",
            "read": lambda: media(buffer)[0][0],
            "thresh_pos": threshXP, "thresh_neg": threshXN,
            "dir_pos": 1, "dir_neg": -1,
            "step": 0, "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": action_vibrar,
            "action_neg": action_vibrar
        },
        {
            "name": "gyroY",
            "read": lambda: media(buffer)[0][1],
            "thresh_pos": threshYP, "thresh_neg": threshYN,
            "dir_pos": 1, "dir_neg": -1,
            "step": 0, "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": action_vibrar,
            "action_neg": action_vibrar
        }
    ]

    for i, pot in enumerate(pots):
        sensors.append({
            "name": f"pot{i+1}",
            "read": (lambda p=pot, m=maxCalibratePots[i]: p.read() - m),
            "thresh_pos": threshPot[i],
            "thresh_neg": -9999,
            "dir_pos": 0, "dir_neg": 0,
            "step": 0,
            "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": lambda _, lvl=None: send_charPs(lvl) if lvl else None,
            "action_neg": None
        })

    while True:
        stepX = sensors[0]["step"]
        stepY = sensors[1]["step"]

        if -1 <= stepX <= 1 and -2 <= stepY <= 2:
            abclevel = [stepX + 1, 2 - stepY]
        else:
            abclevel = None

        for sensor in sensors:
            val = sensor["read"]()
            sensor.update(check_sensor(
                val, sensor["thresh_pos"], sensor["thresh_neg"],
                sensor, holdclick=False
            ))

        if all(s["wait2Zero"] for s in sensors[:2]):
            for s in sensors[:2]:
                s["cycle"] += 1
            if any(s["cycle"] == 20 for s in sensors[:2]):
                sensors[0]["step"] = sensors[1]["step"] = 0
                vibrar(2)

        time.sleep_ms(tsleep)
```

---

## **5. main.py**

```python
from utils import vibrar, getGyro
from sensors import start

def run():
    vibrar(4)
    TSLEEP = 50
    TCLEAR = 10000
    SAMPLES = 5
    start(TSLEEP, TCLEAR, SAMPLES, getGyro)

if __name__ == "__main__":
    run()
```

---

Se quiser, eu posso agora **pegar o seu código original e já te devolver refatorado nesse formato de pastas** para você só colar e rodar no ESP32.
Quer que eu já faça isso agora?













