import time
from machine import Pin, SoftI2C, TouchPad
import mpu6050

# ==== Inicialização de Hardware ====

# Configura o barramento I2C nos pinos do ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
# Inicializa o sensor MPU6050
mpuSensor = mpu6050.accel(i2c)
# Pino que controla o motor vibrador
pino_vibracao = Pin(33, Pin.OUT)

# Inicialização dos sensores táteis (TouchPads)
pot1 = TouchPad(Pin(13))
pot2 = TouchPad(Pin(12))
pot3 = TouchPad(Pin(14))
pot4 = TouchPad(Pin(27))
pot5 = TouchPad(Pin(4))
# Lista para fácil iteração
pots = [pot1, pot2, pot3, pot4, pot5]

# ==== Funções auxiliares ====

def vibrar(n_pulsos, step=None):
    """Faz o motor vibrar n_pulsos vezes. Pulso mais longo se step==0."""
    for _ in range(n_pulsos):
        pino_vibracao.on()
        if step == 0:
            time.sleep_ms(200)
        else:
            time.sleep_ms(101)
        pino_vibracao.off()
        time.sleep_ms(70)

def getGyro(buffer):
    """Lê dados crus do MPU6050 e armazena no buffer."""
    mpuData = mpuSensor.get_values()
    buffer[0].append(mpuData['GyX'])
    buffer[1].append(mpuData['GyY'])
    buffer[2].append(mpuData['GyZ'])
    buffer[3].append(mpuData['AcX'])
    buffer[4].append(mpuData['AcY'])
    buffer[5].append(mpuData['AcZ'])
    return buffer

def media(buffer):
    """Calcula a média das leituras no buffer e remove a mais antiga."""
    getGyro(buffer)
    # Médias para giroscópio (primeiros 3) e acelerômetro (últimos 3)
    gyro = [sum(buffer[i]) / len(buffer[i]) for i in range(3)]
    accl = [sum(buffer[i]) / len(buffer[i]) for i in range(3, 6)]
    # Remove a leitura mais antiga
    for i in range(6):
        buffer[i].pop(0)
    return gyro, accl

def calcCalibrate(bufferPot):
    """Calcula o valor máximo registrado para cada touchpad."""
    return [max(potList) for potList in bufferPot]

def getPots(bufferPot, pval):
    """Adiciona leitura atual dos touchpads ao buffer."""
    for i in range(5):
        bufferPot[i].append(pval[i])
    return bufferPot

def check_sensor(value, thresh_pos, thresh_neg,
                 state, holdclick):
    """Verifica se o valor do sensor ultrapassa os limites
       e executa ações associadas."""
    step = state["step"]
    tp = state["trigger_pos"]
    tn = state["trigger_neg"]
    swp = state["stepWait_pos"]
    swn = state["stepWait_neg"]
    wait2Zero = state["wait2Zero"]
    cycle = state["cycle"]

    # Evento: valor acima do limiar positivo
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

    # Evento: valor abaixo do limiar negativo
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

    # Incremento repetitivo enquanto mantido no limiar positivo
    if tp:
        swp += 1
    else:
        swp = 0
    if swp >= 5:
        step += state["dir_pos"]
        swp = 0
        if state["action_pos"]:
            state["action_pos"](step)

    # Incremento repetitivo enquanto mantido no limiar negativo
    if tn:
        swn += 1
    else:
        swn = 0
    if swn >= 5:
        step += state["dir_neg"]
        swn = 0
        if state["action_neg"]:
            state["action_neg"](step)

    # Atualiza o estado do sensor
    state.update(step=step,
                 trigger_pos=tp,
                 trigger_neg=tn,
                 stepWait_pos=swp,
                 stepWait_neg=swn,
                 wait2Zero=wait2Zero,
                 cycle=cycle)
    return state

def start(tsleep, tclear, samples):
    """Função principal que calibra, configura e lê sensores em loop."""
    # Calibração inicial dos touchpads
    bufferPot = [[] for _ in range(5)]
    for _ in range(40):
        pval = [pot.read() for pot in pots]
        getPots(bufferPot, pval)
        time.sleep_ms(70)
    maxCalibratePots = calcCalibrate(bufferPot)

    # Coleta inicial de dados do giroscópio
    buffer = [[] for _ in range(6)]
    for _ in range(samples - 1):
        getGyro(buffer)
        time.sleep_ms(70)

    # Definição de limiares
    poragora = 14000
    thresPercent = 0.1
    threshXP = poragora - (poragora * thresPercent)
    threshXN = -poragora + (poragora * thresPercent)
    threshYP = poragora - (poragora * thresPercent)
    threshYN = -poragora + (poragora * thresPercent)
    threshPot = [-120] * 5

    # Vibra para indicar início
    vibrar(2)

    # Lista de sensores monitorados
    sensors = [
        {   # Giroscópio X
            "name": "gyroX",
            "read": lambda: media(buffer)[0][0],
            "thresh_pos": threshXP,
            "thresh_neg": threshXN,
            "dir_pos": 1, "dir_neg": -1,
            "step": 0,
            "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": lambda s: vibrar(1),
            "action_neg": lambda s: vibrar(1)
        },
        {   # Giroscópio Y
            "name": "gyroY",
            "read": lambda: media(buffer)[0][1],
            "thresh_pos": threshYP,
            "thresh_neg": threshYN,
            "dir_pos": 1, "dir_neg": -1,
            "step": 0,
            "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": lambda s: vibrar(1),
            "action_neg": lambda s: vibrar(1)
        }
    ]

    # Adiciona os touchpads à lista de sensores
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

    # Loop principal
    while True:
        stepX = sensors[0]["step"]
        stepY = sensors[1]["step"]

        # Determina nível ABC baseado em stepX/Y
        if -1 <= stepX <= 1 and -2 <= stepY <= 2:
            abclevel = [stepX + 1, 2 - stepY]
        else:
            abclevel = None

        # Processa todos os sensores
        for sensor in sensors:
            val = sensor["read"]()
            if "pot" in sensor["name"]:
                sensor.update(check_sensor(
                    val, sensor["thresh_pos"], sensor["thresh_neg"],
                    sensor, holdclick=False
                ))
                # Ajusta action_pos para enviar nível atual
                if sensor["action_pos"]:
                    sensor["action_pos"] = (
                        lambda lvl=abclevel: lambda s: send_charPs(lvl) if lvl else None
                    )()
            else:
                sensor.update(check_sensor(
                    val, sensor["thresh_pos"], sensor["thresh_neg"],
                    sensor, holdclick=False
                ))

        # Reseta contadores se ambos giros voltarem ao zero por tempo suficiente
        if all(s["wait2Zero"] for s in sensors[:2]):
            for s in sensors[:2]:
                s["cycle"] += 1
            if any(s["cycle"] == 20 for s in sensors[:2]):
                sensors[0]["step"] = sensors[1]["step"] = 0
                vibrar(2)

        time.sleep_ms(tsleep)

def send_charPs(abckey):
    """Envia ou imprime comando baseado no valor abckey."""
    print("send_charPs called with:", abckey)

def run():
    """Inicia o sistema com vibração de sinalização."""
    vibrar(4)
    TSLEEP = 50
    TCLEAR = 10000
    SAMPLES = 5
    start(TSLEEP, TCLEAR, SAMPLES)
