=== CONSOLIDAÇÃO DE CÓDIGOS DA PASTA: esp ===



=== ARQUIVO: esp/config.py ===

import machine
import ubinascii


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
# CONFIGURAÇÕES DE TOUCH
# ============================================================
CALIB_POTS_FILE = "pots_calib.json"
MAD_MIN = 5 # limites de MAD para evitar thresholds muito colados
MAD_MAX = 50 # limites de MAD para evitar thresholds muito colados
SAMPLES_HYSTERESIS = 100 # amostras para calibrar os pots
TIMEMS_SAMPLES = 70 # tempo para coleta de amostras
K_SENSIBILIDADE = 3 # k: multiplicador para ajustar sensibilidade.
ALPHA_SUAVIZACAO = 0.1 # alpha: fator de suavização para baseline (0.1 = mais rápido para se adaptar).
DEBOUNCE_COUNT  = 2 # Leituras consecutivas para confirmar toque


# ============================================================
# CONFIGURAÇÕES DO GIROSCÓPIO
# ============================================================
SAMPLES = 5       # Amostras para suavisar a curva do giroscópio
LIMGYRO = 14000   # 8000 (sensível) | 20000 (menos sensível)
THRES_PERCENT = 0.1     # 0.05 (5%) | 0.2 (20%)
GY1, GY2 = 1, 0    # Ordem dos eixos: X depois Y

if THIS_IS == 0:
    INVERT_X, INVERT_Y = False, True  # T,M Inverter sentido do eixo
else:
    INVERT_X, INVERT_Y = True, True   # T,M Inverter sentido do eixo


CALIB_ACCL_FILE = "accl_calib.json"
SAMPLES_ACCL = 100
TIME_ACCL_SAMPLES = 70
ACCL_MAD_MAX = 5 # 5
MARGIN_MIN = 2000 # 2000
MARGIN_MAX = 4000 # 4000

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


# ============================================================
# Motor Vib 
# ============================================================
VIBRAR_LIGADO = 150     # 101 default
VIBRAR_DESLIGADO = 70   # 70 default
VIBRAR_LONGO = 250      # 200 para step == 0
VIBRAR_ALERTA = 300     # 300 para step == 1




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


tstpot(row, col, delay=0.1)
tstpot(row, col)

start(force_calib=True)

"""


=== ARQUIVO: esp/actions.py ===

from machine import Pin, UART
import time
from printlogs import log
from config import VIBRAR_LIGADO, VIBRAR_DESLIGADO, VIBRAR_LONGO, VIBRAR_ALERTA

# UART - ajuste TX e RX conforme o seu hardware
uart = UART(1, baudrate=115200, tx=17, rx=16)

def send_charPs(zmkcodes):
    if zmkcodes is not None:
        log('send_charPs', zmkcodes, 4)
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
        log('packet', packet, 5)
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
            try: pino_vibracao.value(1)
            except: pass
        
        # Usando as variáveis de configuração
        if step == 0: time.sleep_ms(VIBRAR_LONGO)
        if step == 1: time.sleep_ms(VIBRAR_ALERTA)
        else: time.sleep_ms(VIBRAR_LIGADO)
        
        try:
            pino_vibracao.off()
        except Exception:
            try: pino_vibracao.value(0)
            except: pass
        
        time.sleep_ms(VIBRAR_DESLIGADO)


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
    pots = [TouchPad(Pin(p)) for p in pins]

    test_pots = [i for i, p in enumerate(pots) if p.read() < 0]
    print('test_pots',test_pots)

    if len(test_pots) > 0:
        log("test_pots erro:", test_pots, 0)
        # sys.exit("encerrando programa.")
        # raise SystemExit
        raise KeyboardInterrupt("Parando programa!")

    return pots



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


=== ARQUIVO: esp/calibration.py ===

import time
import os
import ujson
import config
from printlogs import log
from actions import vibrar

def save_calibration(baseline, press_thresh, release_thresh):
    try:
        calib_data = {
            'baseline': baseline,
            'press_thresh': press_thresh,
            'release_thresh': release_thresh
        }
        with open(config.CALIB_POTS_FILE, 'w') as f:
            ujson.dump(calib_data, f)
        log("Pots Calibração dos pots salva com sucesso!", 1)
    except Exception as e:
        log(f"Erro ao salvar calibração dos pots: {e}", 0)

def load_calibration():
    try:
        if config.CALIB_POTS_FILE in os.listdir():
            with open(config.CALIB_POTS_FILE, 'r') as f:
                calib_data = ujson.load(f)
            log("Calibração dos pots carregada!", 1)
            return calib_data['baseline'], calib_data['press_thresh'], calib_data['release_thresh']
    except Exception as e:
        log(f"Erro ao carregar calibração dos pots: {e}", 0)
    return None, None, None


def calc_pots_hysteresis(pots, num_pots, vib, force_calib=False):

    baseline = [0] * num_pots
    pots_thresh_on = [0] * num_pots
    pots_thresh_off = [0] * num_pots

    if not force_calib:
        loaded_baseline, loaded_press, loaded_release = load_calibration()
        if loaded_baseline is not None and len(loaded_baseline) == num_pots:
            baseline[:] = loaded_baseline
            pots_thresh_on[:] = loaded_press
            pots_thresh_off[:] = loaded_release
            return pots_thresh_on, pots_thresh_off

        else:
            log("Calibração inválida dos pots carregada!", 0)
            force_calib = True

    if force_calib:
        vibrar(vib, 6)
        log("calc_pots_hysteresis... nao toque nos sensores.", 0)

        # k: multiplicador para ajustar sensibilidade.
        k = config.K_SENSIBILIDADE
        # alpha: fator de suavização para baseline (0.1 = mais rápido para se adaptar).
        alpha = config.ALPHA_SUAVIZACAO

        samples_count = config.SAMPLES_HYSTERESIS   # ex: 100

        # inicializa baseline com primeira leitura
        baseline = [pots[i].read() for i in range(num_pots)]
        soma_dev = [0] * num_pots

        for _ in range(samples_count):
            for i in range(num_pots):
                val = pots[i].read()
                # atualiza baseline suavizado (EMA)
                baseline[i] = (1 - alpha) * baseline[i] + alpha * val
                # acumula desvio em relação ao baseline atual
                soma_dev[i] += abs(val - baseline[i])
            time.sleep_ms(config.TIMEMS_SAMPLES)

        # mad = [s / samples_count for s in soma_dev]
        mad = [max(config.MAD_MIN, min(s / samples_count, config.MAD_MAX)) for s in soma_dev]

        pots_thresh_on  = [baseline[i] - k * mad[i] for i in range(num_pots)]
        pots_thresh_off = [baseline[i] - (k/2) * mad[i] for i in range(num_pots)]

        save_calibration(baseline, pots_thresh_on, pots_thresh_off)
        vibrar(vib, 6)

        return pots_thresh_on, pots_thresh_off


def save_accl_calibration(baselines, thresholds):
    try:
        calib_data = {
            'baselines': baselines,
            'thresholds': thresholds
        }
        with open(config.CALIB_ACCL_FILE, 'w') as f:   # usar outro arquivo
            ujson.dump(calib_data, f)
        log("Calibração do acelerômetro salva com sucesso!", 0)
    except Exception as e:
        log(f"Erro ao salvar calibração do acelerômetro: {e}", 0)


def load_accl_calibration():
    try:
        if config.CALIB_ACCL_FILE in os.listdir():
            with open(config.CALIB_ACCL_FILE, 'r') as f:
                calib_data = ujson.load(f)
            log("Calibração do acelerômetro carregada!", 0)
            return calib_data['baselines'], calib_data['thresholds']
    except Exception as e:
        log(f"Erro ao carregar calibração do acelerômetro: {e}", 0)
    return None, None


def calc_accl_hysteresis(mpu, vib, force_calib=False):

    if not force_calib:
        baselines, thresholds = load_accl_calibration()
        if thresholds is not None:
            return thresholds
        else:
            log("Calibração do acelerômetro inválida/no arquivo, fazendo nova calibração", 0)
            force_calib = True

    if force_calib:
        vibrar(vib, 6)
        log("calc_accel_hysteresis... nao toque nos sensores.", 0)

        # ======== CALIBRAÇÃO ========
        N = config.SAMPLES_ACCL

        margin_min = config.MARGIN_MIN # 2000
        margin_max = config.MARGIN_MAX # 4000
        accl_mad_max = config.ACCL_MAD_MAX # 5
        samples = {"X": [], "Y": [], "Z": []}

        for _ in range(N):
            vals = mpu.get_values()
            samples["X"].append(vals["AcX"])
            samples["Y"].append(vals["AcY"])
            samples["Z"].append(vals["AcZ"])
            time.sleep_ms(config.TIME_ACCL_SAMPLES)

        # Calcula baseline e ruído de cada eixo
        baselines = {}
        noises = {}
        for axis in ["X", "Y", "Z"]:
            baselines[axis] = sum(samples[axis]) / N
            noises[axis] = max(samples[axis]) - min(samples[axis])

        # Define thresholds com histerese para cada eixo
        thresholds = {}
        for axis in ["X", "Y", "Z"]:
            baseline = baselines[axis]
            noise = noises[axis]

            margin = int(noise * accl_mad_max)
            margin = max(margin_min, min(margin_max, margin))  # limita a faixa

            thresholds[axis] = {
                "on_pos": baseline + margin,
                "off_pos": baseline + int(margin * 0.8),
                "on_neg": baseline - margin,
                "off_neg": baseline - int(margin * 0.8)
            }

        save_accl_calibration(baselines, thresholds)
        vibrar(vib, 6)
        return thresholds



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
    log(f'{mapped_i}, {abclevel}, {status}, {side}', 4)
    mapping = MAPL if side == 0 else MAPR
    key = (mapped_i, abclevel[0], abclevel[1])
    if key not in mapping:
        return None  # tecla não mapeada
    row, col = mapping[key]
    return row, col, status



=== ARQUIVO: esp/pots.py ===

import config
from printlogs import log

class PotsState:
    def __init__(self, num_pots: int):
        self.num_pots = num_pots
        self.pval = [0] * num_pots
        self.triggerPot = [False] * num_pots
        self.pot_counter = [0] * num_pots
        self.wait2Zero = False
        self.cycle = 0


def check_pots(pots, abclevel, press_thresh, release_thresh, state: PotsState):
    """
    Verifica os potenciômetros e atualiza o estado.
    Retorna um evento (ou None) + estado atualizado.
    """
    local_res_check_pots = None

    for i, pot in enumerate(pots):
        if i >= state.num_pots:
            log(f"Erro: Índice {i} fora dos limites (max {state.num_pots})", 0)
            continue

        val = pot.read()
        state.pval[i] = val
        mapped_i = config.INDEX_MAP_POTS[i]

        # Pressionado
        if not state.triggerPot[i] and val < press_thresh[i]:
            state.pot_counter[i] += 1
            if state.pot_counter[i] >= config.DEBOUNCE_COUNT:
                local_res_check_pots = [abclevel, mapped_i, 1, config.THIS_IS]
                state.triggerPot[i] = True
                state.pot_counter[i] = 0
                state.wait2Zero = False
                state.cycle = 0

        # Solto
        elif state.triggerPot[i] and val > release_thresh[i]:
            state.pot_counter[i] += 1
            if state.pot_counter[i] >= config.DEBOUNCE_COUNT:
                local_res_check_pots = [abclevel, mapped_i, 0, config.THIS_IS]
                state.triggerPot[i] = False
                state.pot_counter[i] = 0
                state.wait2Zero = True

        else:
            state.pot_counter[i] = 0

    return local_res_check_pots, state


=== ARQUIVO: esp/gyro.py ===

import time
import config
from actions import vibrar
from printlogs import log


class GyroState:
    def __init__(self):
        self.stepX = 0
        self.stepY = 0
        self.evXP = False
        self.evXN = False
        self.evYP = False
        self.evYN = False
        self.swXP = 0
        self.swXN = 0
        self.swYP = 0
        self.swYN = 0
        self.wait2Zero = False
        self.cycle = 0


def append_gyro(buffer, mpuSensor):
    """Adiciona uma leitura ao buffer (6 listas)"""
    if mpuSensor is None:
        return buffer
    try:
        mpuData = mpuSensor.get_values()
    except Exception as e:
        log("MPU read error:", e, 0)
        return buffer

    keys = ['GyX', 'GyY', 'GyZ', 'AcX', 'AcY', 'AcZ']
    for i, k in enumerate(keys):
        buffer[i].append(mpuData.get(k, 0))
    return buffer


def initial_buffer(buffer, mpu):
    for _ in range(config.SAMPLES - 1):
        append_gyro(buffer, mpu)
        time.sleep_ms(70)
    return buffer


def average_and_slide(buffer, mpuSensor):
    """Lê mais um valor, calcula média e remove o mais antigo (sliding window)"""
    buffer = append_gyro(buffer, mpuSensor)
    averages = [sum(lst) / len(lst) if lst else 0 for lst in buffer]
    gyro = averages[:3]
    accl = averages[3:6]

    # sliding window: remove o mais antigo
    for lst in buffer:
        if lst:
            lst.pop(0)
    return gyro, accl


def check_gyro_axis(gyro, axis_index, step, event_pos, event_neg, vib, wait2Zero, cycle, invert=False):
    """Verifica giroscópio em um eixo e atualiza estado."""
    pos_thresh = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    neg_thresh = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)

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


def check_accl_axis(gyro, axis_index, step, event_pos, event_neg, vib, wait2Zero, cycle, invert=False):

    # return step, event_pos, event_neg, wait2Zero, cycle
    # return step, event_pos, event_neg, wait2Zero, cycle
    pass


def check_step_wait(event_triggered, step_wait, step, delta, vib):
    """Controle de espera para repetição automática."""
    step_wait = step_wait + 1 if event_triggered else 0
    if step_wait >= config.STEP_WAIT_LIMIT:
        step += delta
        vibrar(vib, 1, step)
        log(f"[STEP_WAIT] step={step} delta={delta}", 2)
        step_wait = 0
    return step_wait, step


def gyro_principal(gyro, gy1, gy2, vib, state: GyroState):
    """Processa movimentos do giroscópio e atualiza estado."""

    # Movimento no eixo X
    state.stepX, state.evXP, state.evXN, state.wait2Zero, state.cycle = check_gyro_axis(
        gyro, gy1, state.stepX,
        state.evXP, state.evXN,
        vib, state.wait2Zero, state.cycle,
        invert=config.INVERT_X
    )

    # Movimento no eixo Y
    state.stepY, state.evYP, state.evYN, state.wait2Zero, state.cycle = check_gyro_axis(
        gyro, gy2, state.stepY,
        state.evYP, state.evYN,
        vib, state.wait2Zero, state.cycle,
        invert=config.INVERT_Y
    )

    # Controle de repetição automática
    invX = -1 if config.INVERT_X else 1
    invY = -1 if config.INVERT_Y else 1

    state.swXP, state.stepX = check_step_wait(state.evXP, state.swXP, state.stepX, invX * (1 if gy1 == 0 else -1), vib)
    state.swXN, state.stepX = check_step_wait(state.evXN, state.swXN, state.stepX, invX * (-1 if gy1 == 0 else 1), vib)
    state.swYP, state.stepY = check_step_wait(state.evYP, state.swYP, state.stepY, invY * (-1 if gy1 == 0 else 1), vib)
    state.swYN, state.stepY = check_step_wait(state.evYN, state.swYN, state.stepY, invY * (1 if gy1 == 0 else -1), vib)

    return state


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
from actions import vibrar, send_charPs
from printlogs import log
from dicctozmk import potsgyrotozmk
from calibration import calc_pots_hysteresis, calc_accl_hysteresis
from pots import check_pots, PotsState
from gyro import initial_buffer, average_and_slide, gyro_principal, GyroState


def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()

    # Estado dos potenciômetros
    pots_state = PotsState(len(pots))

    # Estado do giroscópio
    gyro_state = GyroState()

    # Calcula thresholds de histerese
    pots_thresh_on, pots_thresh_off = calc_pots_hysteresis(pots, pots_state.num_pots, vib, force_calib)
    print("Thresholds on:", pots_thresh_on)
    print("Thresholds off:", pots_thresh_off)

    acclthresholds = calc_accl_hysteresis(mpu, vib, force_calib)
    print("\nThresholds Acelerometro", acclthresholds)

    # print("------------------------------------")
    # raise KeyboardInterrupt("Parando programa!")

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    buffer = initial_buffer(buffer, mpu)
    gyro, accl = average_and_slide(buffer, mpu)

    gy1, gy2 = config.GY1, config.GY2

    accl_states = [0, 0, 0] # 0 = neutro, 1 = positivo, -1 = negativo
    stable_count = [0, 0, 0]

    # Loop principal
    vibrar(vib, 2)
    num = 0
    while True:
        gyro, accl = average_and_slide(buffer, mpu)
        # x[P] Y[L] Z[V]
        # print(f'x{accl[0]},y{accl[1]},z{accl[2]}')

        # Eventos do Acelerometro
        for axis, label in enumerate(["X", "Y", "Z"]):
            a = accl[axis]
            t = acclthresholds[label]
            # print(f"{label}: {a:.2f}, thresholds: {t}, state: {accl_states[axis]}")

            if accl_states[axis] == 0:
                if a > t["on_pos"]:
                    accl_states[axis] = 1
                    stable_count[axis] = 0
                elif a < t["on_neg"]:
                    accl_states[axis] = -1
                    stable_count[axis] = 0

            elif accl_states[axis] == 1:
                if a < t["off_pos"]:
                    accl_states[axis] = 0
                else:
                    stable_count[axis] += 1

            elif accl_states[axis] == -1:
                if a > t["off_neg"]:
                    accl_states[axis] = 0
                else:
                    stable_count[axis] += 1

            # força neutro se parado por muito tempo
            if stable_count[axis] > 50:  
                accl_states[axis] = 0
                stable_count[axis] = 0

        print('accl_states',accl_states,'stable_count',stable_count)
        # print('stable_count',stable_count)





        # Atualiza giroscópio
        gyro_state = gyro_principal(gyro, gy1, gy2, vib, gyro_state)

        # Atualiza potenciômetros
        abclevel = [gyro_state.stepX, gyro_state.stepY]

        res_check_pots, pots_state = check_pots(
            pots, abclevel,
            pots_thresh_on, pots_thresh_off,
            pots_state
        )

        if res_check_pots is not None:
            # log(f'potsgyrotozmk {res_check_pots}', 0)
            tozmk = potsgyrotozmk(*res_check_pots)
            # log(f'send_charPs {tozmk}', 0)
            # send_charPs(tozmk)

        # Reset se parado
        if gyro_state.wait2Zero and gyro_state.cycle < config.CYCLE_RESET_LIMIT:
            gyro_state.cycle += 1
            if gyro_state.cycle == config.CYCLE_RESET_LIMIT:
                gyro_state.stepX = gyro_state.stepY = 0
                vibrar(vib, 2)
                log("[RESET] StepX e StepY resetados", 2)
                gyro_state.wait2Zero = False
                gyro_state.cycle = 0

        # Controle de limpeza de log
        if num % config.TCLEAR == 0:
            num = 0
        num += 1
        time.sleep_ms(config.TSLEEP)


if __name__ == "__main__":
    start(force_calib=False)
    vibrar(init_vibrator(), 4)
