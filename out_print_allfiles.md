=== CONSOLIDAÇÃO DE CÓDIGOS DA PASTA: esp ===



=== ARQUIVO: esp/config.py ===

import machine
import ubinascii

# ============================================================
# CONFIGURAÇÕES DE TOUCH
# ============================================================
CALIB_FILE = "calib.json"
CALIB_SAMPLES   = 100   # Amostras por canal
PRESS_OFFSET    = 50    # Quanto abaixo do baseline aciona
RELEASE_OFFSET  = 30    # Quanto abaixo do baseline libera
DEBOUNCE_COUNT  = 3     # Leituras consecutivas para confirmar toque


# ============================================================
# CONFIGURAÇÕES DOS POTENCIÔMETROS
# ============================================================
POT_CALIBRATION_SAMPLES   = 40   # 20 (rápido) | 100 (preciso)
POT_CALIBRATION_DELAY_MS  = 70   # Delay entre leituras (ms)


# ============================================================
# CONFIGURAÇÕES DO GIROSCÓPIO
# ============================================================
LIMGYRO       = 14000   # 8000 (sensível) | 20000 (menos sensível)
THRES_PERCENT  = 0.1     # 0.05 (5%) | 0.2 (20%)
GY1, GY2       = 1, 0    # Ordem dos eixos: X depois Y
INVERT_X       = True    # Inverter sentido do eixo X
INVERT_Y       = True    # Inverter sentido do eixo Y


# ============================================================
# CONTROLE DE PASSOS / RESET
# ============================================================
STEP_WAIT_LIMIT   = 5     # Ciclos antes de repetir passo
CYCLE_RESET_LIMIT = 20    # Ciclos parado até resetar stepX/stepY


# ============================================================
# LOOP PRINCIPAL
# ============================================================
TSLEEP  = 50      # Delay entre loops (ms)
TCLEAR  = 10000   # Intervalo para reset de contador
SAMPLES = 5       # Amostras iniciais do giroscópio


# ============================================================
# PINAGEM (ESQUERDA E DIREITA)
# ============================================================
PINOS_R = 13,12,14,27,4,33
INDEX_MAP_R = 0,1,2,3,4,5
PINOS_VIB_R = 26

PINOS_L = 12,13,14,27,4,33
INDEX_MAP_L = 0,1,2,4,3,5
PINOS_VIB_L = 26

# ============================================================
# IDENTIFICAÇÃO DO CHIP / DEFINIÇÃO DO LADO
# ============================================================
chip_id = ubinascii.hexlify(machine.unique_id()).decode()
print("Chip ID:", chip_id)  # Exemplo: '240ac4083456'

# IDs conhecidos dos dois lados
alesp = '083af27f9c38'
aresp = '78e36d170944'

# Define se este chip é o lado L (0) ou R (1)
THIS_IS = 0 if chip_id == alesp else 1
print("THIS_IS:", THIS_IS)

# INDEX MAP final (depende do lado detectado)
INDEX_MAP_POTS = list(INDEX_MAP_L if THIS_IS == 0 else INDEX_MAP_R)


# ============================================================
# DEBUG
# ============================================================
DEBUG = 0
"""
| Você Quer...                  | Configuração        | Comportamento          |
|-------------------------------|---------------------|------------------------|
| Só logs de nível X            | DEBUG = X           | Ignora tudo ≠ X        |
| Todos os logs                 | DEBUG = None        | Mostra tudo            |
| Logs sem nível                | DEBUG = -1          | Mostra só os sem nível |
| Múltiplos níveis (ex: 0,1,2)  | DEBUG = [0, 1, 2]   | Mostra só esses níveis |
"""


=== ARQUIVO: esp/actions.py ===

from machine import Pin, UART
import time
from printlogs import log

# UART - ajuste TX e RX conforme o seu hardware
uart = UART(1, baudrate=115200, tx=17, rx=16)

def send_charPs(zmkcodes):
    if zmkcodes is not None:
        log('send_charPs', zmkcodes, 1)
        row = zmkcodes[0]
        col = zmkcodes[1]

        # Proteção: valores devem estar entre 0 e 255
        if not (0 <= row <= 255 and 0 <= col <= 255):
            log(f"[WARNING] row/col fora do range: row={row}, col={col}", 0)
            return

        if zmkcodes[2] == 0:
            event_type = 0x00
        else:
            event_type = 0x01

        checksum = event_type ^ row ^ col
        packet = bytes([0xAA, event_type, row, col, checksum])
        log('packet', packet, 4)
        uart.write(packet)

def tstpot(row, col, delay=0.1):
    send_charPs([row, col, True])
    time.sleep(delay)
    send_charPs([row, col, False])

def vibrar(pino_vibracao, n_pulsos, step=None):
    if pino_vibracao is None:
        log("vibrador não inicializado", 1)
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



=== ARQUIVO: esp/hw.py ===

from machine import Pin, SoftI2C, TouchPad
import time
import config
from printlogs import log

if config.THIS_IS == 1:
    pinos = config.PINOS_R
    pinos_vib = config.PINOS_VIB_R

if config.THIS_IS == 0:
    pinos = config.PINOS_L
    pinos_vib = config.PINOS_VIB_L

def init_i2c(scl_pin=22, sda_pin=21):
    return SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

def init_mpu(i2c):
    # importa aqui para evitar erro se rodar testes sem MPU
    try:
        import mpu6050
        mpu = mpu6050.MPU6050(i2c)
        return mpu
    except Exception as e:
        log("init_mpu erro:", e, 0)
        return None

def init_vibrator(pin_no=(pinos_vib)):
    p = Pin(pin_no, Pin.OUT)
    try:
        p.off()
    except Exception:
        pass
    return p

def init_pots(pins=(pinos)):
    return [TouchPad(Pin(p)) for p in pins]



=== ARQUIVO: esp/printlogs.py ===

import config
# -----------------------------
# Função de log centralizada
# -----------------------------
def log(*args, **kwargs):
    level = None  # Sem nível por padrão
    if len(args) > 1 and isinstance(args[1], int) and args[1] >= 0:
        level = args[1]
        args = (args[0],) + args[2:]  # Remove o level dos args
    
    debug_level = getattr(config, 'DEBUG', None)
    
    if debug_level is not None and level is not None and level != debug_level:
        return
    
    if debug_level is not None and level is None:
        return
    
    print(*args, **kwargs)


=== ARQUIVO: esp/dicctozmk.py ===

from printlogs import log

# --- Mapas de tradução (lado esquerdo e lado direito) ---

## M=Moto, Y=Yave [M,Y]
## pot [gx, gy] status [M,Y]

MAPL = {
    # abclevel, gx, gy: (row, col)

    # --- Gyro (1,0) [P,M,T] ---
    (0,  1,  0): (3, 2),  # space
    (1,  1,  0): (0, 4),  # r
    (2,  1,  0): (0, 3),  # e
    (3,  1,  0): (0, 2),  # w
    (4,  1,  0): (0, 1),  # q

    # --- Gyro (0,0) [P,M,T] ---
    (0,  0,  0): (3, 2),  # space
    (1,  0,  0): (1, 4),  # f
    (2,  0,  0): (1, 3),  # d
    (3,  0,  0): (1, 2),  # s
    (4,  0,  0): (1, 1),  # a

    # --- Gyro (-1,0) [P,M,T] ---
    (0, -1,  0): (3, 2),  # space
    (1, -1,  0): (2, 4),  # v
    (2, -1,  0): (2, 3),  # c
    (3, -1,  0): (2, 2),  # x
    (4, -1,  0): (2, 1),  # z

    # --- Gyro (1,1) [P,M,T] ---
    (0,  1,  1): (3, 2),  # space
    (1,  1,  1): (0, 5),  # t
    (4,  1,  1): (0, 0),  # esc

    # --- Gyro (0,1) [P,M,T] ---
    (0,  0,  1): (3, 2),  # space
    (1,  0,  1): (1, 5),  # g
    (4,  0,  1): (0, 0),  # esc

    # --- Gyro (-1,1) [P,M,T] ---
    (0, -1,  1): (3, 2),  # space
    (1, -1,  1): (2, 5),  # b
    (4, -1,  1): (0, 0),  # esc

}

MAPR = {
    # --- Gyro (1,0) [P,M,T] ---
    (0,  1,  0): (3, 3),   # enter
    (1,  1,  0): (0, 7),   # u
    (2,  1,  0): (0, 8),   # i
    (3,  1,  0): (0, 9),   # o
    (4,  1,  0): (0, 10),  # p
    # --- Gyro (1,1) [P,M,T] ---
    (0,  1,  1): (3, 3),   # enter
    (1,  1,  1): (0, 6),   # y
    (4,  1,  1): (0, 11),  # backspace

    # --- Gyro (0,0) [P,M,T] ---
    (0,  0,  0): (3, 3),   # enter
    (1,  0,  0): (1, 7),   # j
    (2,  0,  0): (1, 8),   # k
    (3,  0,  0): (1, 9),   # l
    (4,  0,  0): (1, 10),  # c
    # --- Gyro (0,1) [P,M,T] ---
    (0,  0,  1): (3, 3),   # enter
    (1,  0,  1): (1, 6),   # h
    (4,  0,  1): (0, 11),  # backspace

    # --- Gyro (-1,0) [P,M,T] ---
    (0, -1,  0): (3, 3),   # enter
    (1, -1,  0): (2, 7),  # m
    (2, -1,  0): (2, 8),  # ,
    (3, -1,  0): (2, 9),  # .
    (4, -1,  0): (2, 10), # ;
    # --- Gyro (-1,1) [P,M,T] ---
    (0,  -1, 1): (3, 3),   # enter
    (1,  -1, 1): (2, 6),   # n
    (4,  -1, 1): (0, 11),  # backspace

}

def potsgyrotozmk(abclevel, mapped_i, status, side):
    """
    Traduz (abclevel, gx, gy, status) -> (row, col, status)
    side: 0 = left, 1 = right
    """
    log(f'{mapped_i}, {abclevel}, {status}, {side}', 0)
    mapping = MAPL if side == 0 else MAPR
    key = (mapped_i, abclevel[0], abclevel[1])
    if key not in mapping:
        return None  # tecla não mapeada
    row, col = mapping[key]
    return row, col, status



=== ARQUIVO: esp/pots.py ===

import os
import ujson
import config
from printlogs import log

# Variáveis globais
baseline = []
press_thresh = []
release_thresh = []
pot_counter = []
triggerPot = []
pval = []

def init_pot_globals(num_pots):
    global baseline, press_thresh, release_thresh, pot_counter, triggerPot, pval
    baseline = [0] * num_pots
    press_thresh = [0] * num_pots
    release_thresh = [0] * num_pots
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots
    pval = [0] * num_pots

def save_calibration():
    try:
        calib_data = {
            'baseline': baseline,
            'press_thresh': press_thresh,
            'release_thresh': release_thresh
        }
        with open(config.CALIB_FILE, 'w') as f:
            ujson.dump(calib_data, f)
        log("Calibração salva com sucesso!", 1)
    except Exception as e:
        log(f"Erro ao salvar calibração: {e}", 0)

def load_calibration():
    try:
        if config.CALIB_FILE in os.listdir():
            with open(config.CALIB_FILE, 'r') as f:
                calib_data = ujson.load(f)
            log("Calibração carregada do arquivo", 1)
            return calib_data['baseline'], calib_data['press_thresh'], calib_data['release_thresh']
    except Exception as e:
        log(f"Erro ao carregar calibração: {e}", 0)
    return None, None, None


def calibrate_pots(pots, force_new_calib=False):
    global baseline, press_thresh, release_thresh, pot_counter, triggerPot, pval
    
    num_pots = len(pots)
    
    # Tenta carregar calibração existente apenas se não for forçada
    if not force_new_calib:
        loaded_baseline, loaded_press, loaded_release = load_calibration()
        if loaded_baseline is not None and len(loaded_baseline) == num_pots:
            baseline = loaded_baseline
            press_thresh = loaded_press
            release_thresh = loaded_release
            log("Calibração carregada do arquivo", 1)
        else:
            log("Calibração inválida/no arquivo, fazendo nova calibração", 1)
            force_new_calib = True
    
    # Se forçado ou se não encontrou calibração válida
    if force_new_calib:
        log("Calibrando... não toque nos sensores.", 1)
        baseline = [0] * num_pots
        press_thresh = [0] * num_pots
        release_thresh = [0] * num_pots
        
        for i in range(num_pots):
            soma = 0
            for _ in range(config.CALIB_SAMPLES):  # Alterado para config.CALIB_SAMPLES
                soma += pots[i].read()
                time.sleep_ms(5)
            baseline[i] = soma / config.CALIB_SAMPLES  # Alterado para config.CALIB_SAMPLES
            press_thresh[i] = baseline[i] - config.PRESS_OFFSET  # Alterado para config.PRESS_OFFSET
            release_thresh[i] = baseline[i] - config.RELEASE_OFFSET  # Alterado para config.RELEASE_OFFSET
        
        # Salva a nova calibração
        save_calibration()
        log("Nova calibração concluída e salva!", 1)

    # Inicializa variáveis de estado
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots
    pval = [0] * num_pots

    log("Baseline:       ", baseline, 1)
    log("Press thresh:   ", press_thresh, 1)
    log("Release thresh: ", release_thresh, 1)


def check_pots(pots, abclevel, wait2Zero, cycle):
    global pval, triggerPot, pot_counter, press_thresh, release_thresh
    
    for i, pot in enumerate(pots):
        if i >= len(pval):
            log(f"Erro: Índice {i} fora dos limites (max {len(pval)})", 0)
            continue
            
        val = pot.read()
        pval[i] = val
        mapped_i = config.INDEX_MAP_POTS[i]

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= config.DEBOUNCE_COUNT:
                from actions import send_charPs
                from dicctozmk import potsgyrotozmk
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 1, config.THIS_IS))
                log(f"[POT{mapped_i}] Pressionado | val={val} | abclevel={abclevel}", 3)
                triggerPot[i] = True
                pot_counter[i] = 0
                wait2Zero = False
                cycle = 0

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= config.DEBOUNCE_COUNT:
                from actions import send_charPs
                from dicctozmk import potsgyrotozmk
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 0, config.THIS_IS))
                log(f"[POT{mapped_i}] Liberado | val={val} | abclevel={abclevel}", 3)
                triggerPot[i] = False
                pot_counter[i] = 0
                wait2Zero = True

        else:
            pot_counter[i] = 0

    return wait2Zero, cycle


=== ARQUIVO: esp/gyro.py ===

import config
from printlogs import log

def append_gyro(buffer, mpuSensor):
    """Adiciona uma leitura ao buffer (6 listas)"""
    if mpuSensor is None:
        # evita crash se MPU não inicializou
        return buffer
    try:
        mpuData = mpuSensor.get_values()
    except Exception as e:
        log("MPU read error:", e, 0)
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

def check_gyro_axis(gyro, axis_index, pos_thresh, neg_thresh, step, event_pos, event_neg, vib, wait2Zero, cycle, invert=False):
    """Verifica giroscópio em um eixo e atualiza estado."""
    if not event_pos and gyro[axis_index] > pos_thresh:
        step += -1 if invert else 1
        vibrar(vib, 1, step)
        log(f"[GYRO] Eixo {axis_index} POS -> step={step}", 2)
        event_pos = True
        wait2Zero = True
        cycle = 0
    elif event_pos and gyro[axis_index] <= pos_thresh:
        event_pos = False

    if not event_neg and gyro[axis_index] < neg_thresh:
        step += 1 if invert else -1
        vibrar(vib, 1, step)
        log(f"[GYRO] Eixo {axis_index} NEG -> step={step}", 2)
        event_neg = True
        wait2Zero = True
        cycle = 0
    elif event_neg and gyro[axis_index] >= neg_thresh:
        event_neg = False

    return step, event_pos, event_neg, wait2Zero, cycle

def check_step_wait(event_triggered, step_wait, step, delta, vib):
    """Controle de espera para repetição automática."""
    step_wait = step_wait + 1 if event_triggered else 0
    if step_wait >= config.STEP_WAIT_LIMIT:
        step += delta
        vibrar(vib, 1, step)
        log(f"[STEP_WAIT] step={step} delta={delta}", 2)
        step_wait = 0
    return step_wait, step



=== ARQUIVO: esp/mpu6050.py ===

import machine

class MPU6050():
    def __init__(self, i2c, addr=0x68):
        self.iic = i2c
        self.addr = addr
        self.iic.start()
        self.iic.writeto(self.addr, bytearray([107, 0]))
        self.iic.stop()

    def get_raw_values(self):
        self.iic.start()
        a = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        self.iic.stop()
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["AcY"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["AcZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        vals["Tmp"] = self.bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])
        vals["GyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])
        vals["GyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])
        return vals  # returned in range of Int16
        # -32768 to 32767

    def val_test(self):  # ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(0.05)



=== ARQUIVO: esp/main.py ===

import time
import config
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar
from printlogs import log
from pots import init_pot_globals, calibrate_pots, check_pots
from gyro import append_gyro, average_and_slide, check_gyro_axis, check_step_wait

def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()

    if pots is None: pots = init_pots()
    
    # Inicializa variáveis globais dos potenciômetros
    init_pot_globals(len(pots))
    
    # Calibração de pots
    calibrate_pots(pots, force_calib)

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    for _ in range(config.SAMPLES - 1):
        append_gyro(buffer, mpu)
        time.sleep_ms(70)
    
    gyro, accl = average_and_slide(buffer, mpu)

    # Variáveis de estado
    num = 0
    stepX = stepY = 0
    evntTriggeredXP = evntTriggeredXN = False
    evntTriggeredYP = evntTriggeredYN = False
    wait2Zero = False
    cycle = 0
    stepWaitXP = stepWaitXN = stepWaitYP = stepWaitYN = 0

    # Thresholds giroscópio
    threshP  = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    threshN  = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)
    threshXP = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    threshXN = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)

    gy1, gy2 = config.GY1, config.GY2

    vibrar(vib, 2)

    # Loop principal
    while True:
        gyro, accl = average_and_slide(buffer, mpu)

        # Movimento no eixo X
        stepX, evntTriggeredXP, evntTriggeredXN, wait2Zero, cycle = check_gyro_axis(
            gyro, gy1, threshXP, threshXN, stepX, evntTriggeredXP, evntTriggeredXN, vib, wait2Zero, cycle, invert=config.INVERT_X
        )

        # Movimento no eixo Y
        stepY, evntTriggeredYP, evntTriggeredYN, wait2Zero, cycle = check_gyro_axis(
            gyro, gy2, threshP, threshN, stepY, evntTriggeredYP, evntTriggeredYN, vib, wait2Zero, cycle, invert=config.INVERT_Y
        )

        # Controle de repetição automática
        invX = -1 if config.INVERT_X else 1
        invY = -1 if config.INVERT_Y else 1

        stepWaitXP, stepX = check_step_wait(evntTriggeredXP, stepWaitXP, stepX, invX * (1 if gy1 == 0 else -1), vib)
        stepWaitXN, stepX = check_step_wait(evntTriggeredXN, stepWaitXN, stepX, invX * (-1 if gy1 == 0 else 1), vib)
        stepWaitYP, stepY = check_step_wait(evntTriggeredYP, stepWaitYP, stepY, invY * (-1 if gy1 == 0 else 1), vib)
        stepWaitYN, stepY = check_step_wait(evntTriggeredYN, stepWaitYN, stepY, invY * (1 if gy1 == 0 else -1), vib)

        # Leitura dos potenciômetros
        abclevel = [stepX, stepY]
        wait2Zero, cycle = check_pots(pots, abclevel, wait2Zero, cycle)

        # Reset se parado
        if wait2Zero and cycle < config.CYCLE_RESET_LIMIT:
            cycle += 1
            if cycle == config.CYCLE_RESET_LIMIT:
                stepY = stepX = 0
                vibrar(vib, 2)
                log("[RESET] StepX e StepY resetados", 2)
                wait2Zero = False
                cycle = 0

        if num % config.TCLEAR == 0:
            num = 0
        num += 1
        time.sleep_ms(config.TSLEEP)

if __name__ == "__main__":
    start(force_calib=True)  # Força nova calibração na inicialização
    vibrar(init_vibrator(), 4)
