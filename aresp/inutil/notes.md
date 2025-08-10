
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
mpremote connect /dev/ttyUSB0 cp hardware.py :hardware.py
mpremote connect /dev/ttyUSB0 cp utils.py :utils.py
mpremote connect /dev/ttyUSB0 cp sensors.py :sensors.py
mpremote connect /dev/ttyUSB0 cp actions.py :actions.py
mpremote connect /dev/ttyUSB0 cp mpu6050.py :mpu6050.py


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


eu estou com esse problema:


rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0030,len:4892
ho 0 tail 12 room 4
load:0x40078000,len:14896
load:0x40080400,len:4
load:0x40080404,len:3372
entry 0x400805b0
MicroPython v1.25.0 on 2025-04-15; Generic ESP32 module with ESP32
Type "help()" for more information.
>>> main()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "main.py", line 11, in main
  File "actions.py", line 14, in vibrar
TypeError: unsupported types for __lt__: 'int', 'Pin'
>>> 


main.py:

from hardware import init_hardware
from actions import vibrar
from sensors import start_sensors

def main():
    TSLEEP = 50
    TCLEAR = 10000
    SAMPLES = 5
    
    pots, mpuSensor, pino_vibracao = init_hardware()
    vibrar(pino_vibracao, 4)  # Passa o pino
    start_sensors(pots, mpuSensor, pino_vibracao, TSLEEP, TCLEAR, SAMPLES)


hardware.py:

from machine import Pin, SoftI2C, TouchPad
import mpu6050

def init_hardware():
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
    mpuSensor = mpu6050.accel(i2c)

    pino_vibracao = Pin(33, Pin.OUT)

    pots = [
        TouchPad(Pin(13)),
        TouchPad(Pin(12)),
        TouchPad(Pin(14)),
        TouchPad(Pin(27)),
        TouchPad(Pin(4)),
    ]
    return pots, mpuSensor, pino_vibracao

utils.py:

import time

def media(valores):
    return sum(valores) / len(valores) if valores else 0

def calibrar_touchpads(pots, amostras=40, delay_ms=70):
    buffers = [[] for _ in pots]
    for _ in range(amostras):
        leituras = [p.read() for p in pots]
        for i, leitura in enumerate(leituras):
            buffers[i].append(leitura)
        time.sleep_ms(delay_ms)

    maximos = [max(b) for b in buffers]
    return maximos

sensors.py:

import time
from utils import calibrar_touchpads
from actions import vibrar, send_charPs

def check_sensor(value, thresh_pos, state, name):
    if value < thresh_pos and not state["trigger"]:
        state["trigger"] = True
        print(f"[{name}] Toque detectado! Valor: {value}")
        if state["action"]:
            state 
    elif value >= thresh_pos and state["trigger"]:
        state["trigger"] = False
    return state

def start_sensors(pots, mpuSensor, pino_vibracao, tsleep, tclear, samples):
    import actions
    actions.pino_vibracao = pino_vibracao

    print("Calibrando touchpads...")
    maxCalibratePots = calibrar_touchpads(pots)
    thresholds = [m - 100 for m in maxCalibratePots]

    sensors = []
    for i, pot in enumerate(pots):
        sensors.append({
            "name": f"pot{i+1}",
            "read": lambda p=pot: p.read(),
            "thresh_pos": thresholds[i],
            "trigger": False,
            "action": lambda s: send_charPs(f"Pot {i+1}")
        })

    vibrar(2)
    print("Sistema iniciado. Toque para testar...")

    while True:
        for sensor in sensors:
            val = sensor["read"]()
            sensor.update(check_sensor(val, sensor["thresh_pos"], sensor, sensor["name"]))
        time.sleep_ms(tsleep)


actions.py:


import time

def vibrar(pino, n_pulsos, step=None):
    """Faz o motor vibrar n_pulsos vezes."""
    for _ in range(n_pulsos):
        pino.on()
        if step == 0:
            time.sleep_ms(200)
        else:
            time.sleep_ms(101)
        pino.off()
        time.sleep_ms(70)

def send_charPs(abckey):
    """Exibe ou envia o valor detectado."""
    print(f"TOQUE DETECTADO! Nível: {abckey}")
