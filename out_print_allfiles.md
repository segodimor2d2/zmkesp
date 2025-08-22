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
CALIB_FILE = "calib.json"
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


=== ARQUIVO: esp/gyro.py ===

import time
import config
from actions import vibrar
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

    keys = ['GyX', 'GyY', 'GyZ', 'AcX', 'AcY', 'AcZ']
    for i, k in enumerate(keys):
        buffer[i].append(mpuData.get(k, 0))
    return buffer


def initial_buffer(buffer, mpu):
    for _ in range(config.SAMPLES - 1):
        append_gyro(buffer, mpu)
        time.sleep_ms(70)
    return buffer   # <-- fora do loop agora


def average_and_slide(buffer, mpuSensor):
    """Lê mais um valor, calcula média e remove o mais antigo (sliding window)"""
    buffer = append_gyro(buffer, mpuSensor)
    averages = []
    for lst in buffer:
        averages.append(sum(lst) / len(lst) if lst else 0)
    gyro = averages[:3]
    accl = averages[3:6]
    # remove o mais antigo para manter a janela
    for lst in buffer:
        if lst:
            lst.pop(0)
    return gyro, accl


def check_gyro_axis(gyro, axis_index,
                    step, event_pos, event_neg, vib, wait2Zero, cycle, invert=False):
    """Verifica giroscópio em um eixo e atualiza estado."""

    # Thresholds giroscópio
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


def check_step_wait(event_triggered, step_wait, step, delta, vib):
    """Controle de espera para repetição automática."""
    step_wait = step_wait + 1 if event_triggered else 0
    if step_wait >= config.STEP_WAIT_LIMIT:
        step += delta
        vibrar(vib, 1, step)
        log(f"[STEP_WAIT] step={step} delta={delta}", 2)
        step_wait = 0
    return step_wait, step


def gyro_principal(
    gyro, gy1, gy2,
    stepX, stepY,
    evntTriggeredXP, evntTriggeredXN,
    evntTriggeredYP, evntTriggeredYN,
    stepWaitXP, stepWaitXN, stepWaitYP, stepWaitYN,
    vib, wait2Zero, cycle
):
    # Movimento no eixo X
    stepX, evntTriggeredXP, evntTriggeredXN, wait2Zero, cycle = check_gyro_axis(
        gyro, gy1, stepX,
        evntTriggeredXP,
        evntTriggeredXN,
        vib, wait2Zero, cycle, invert=config.INVERT_X
    )

    # Movimento no eixo Y
    stepY, evntTriggeredYP, evntTriggeredYN, wait2Zero, cycle = check_gyro_axis(
        gyro, gy2, stepY,
        evntTriggeredYP,
        evntTriggeredYN,
        vib, wait2Zero, cycle, invert=config.INVERT_Y
    )

    # Controle de repetição automática
    invX = -1 if config.INVERT_X else 1
    invY = -1 if config.INVERT_Y else 1

    stepWaitXP, stepX = check_step_wait(evntTriggeredXP, stepWaitXP, stepX, invX * (1 if gy1 == 0 else -1), vib)
    stepWaitXN, stepX = check_step_wait(evntTriggeredXN, stepWaitXN, stepX, invX * (-1 if gy1 == 0 else 1), vib)
    stepWaitYP, stepY = check_step_wait(evntTriggeredYP, stepWaitYP, stepY, invY * (-1 if gy1 == 0 else 1), vib)
    stepWaitYN, stepY = check_step_wait(evntTriggeredYN, stepWaitYN, stepY, invY * (1 if gy1 == 0 else -1), vib)


    return (
        stepX, stepY,
        evntTriggeredXP, evntTriggeredXN,
        evntTriggeredYP, evntTriggeredYN,
        stepWaitXP, stepWaitXN, stepWaitYP, stepWaitYN,
        wait2Zero, cycle
    )

=== ARQUIVO: esp/main.py ===

import time
import config
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs
from printlogs import log
from dicctozmk import potsgyrotozmk
from calibration import calc_pots_hysteresis
from pots import check_pots
from gyro import initial_buffer, average_and_slide, gyro_principal

def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()

    # Inicializa listas locais pots
    num_pots = len(pots)
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots
    pval = [0] * num_pots

    # Calcula thresholds de histerese
    pots_thresh_on, pots_thresh_off = calc_pots_hysteresis(pots, num_pots, vib, force_calib)
    print("Thresholds on:", pots_thresh_on)
    print("Thresholds off:", pots_thresh_off)

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    buffer = initial_buffer(buffer, mpu)
    gyro, accl = average_and_slide(buffer, mpu)

    # Variáveis de estado
    evntTriggeredXP = evntTriggeredXN = evntTriggeredYP = evntTriggeredYN = False
    stepWaitXP = stepWaitXN = stepWaitYP = stepWaitYN = 0
    stepX = stepY = num = cycle = 0
    res_check_pots = None
    wait2Zero = False

    gy1, gy2 = config.GY1, config.GY2

    vibrar(vib, 2)

    # Loop principal
    while True:
        # Lê mais um valor, calcula média e remove o mais antigo (sliding window)
        gyro, accl = average_and_slide(buffer, mpu)

        (
            stepX, stepY,
            evntTriggeredXP, evntTriggeredXN,
            evntTriggeredYP, evntTriggeredYN,
            stepWaitXP, stepWaitXN, stepWaitYP, stepWaitYN,
            wait2Zero, cycle,
        ) = gyro_principal(
            gyro, gy1, gy2,
            stepX, stepY,
            evntTriggeredXP, evntTriggeredXN,
            evntTriggeredYP, evntTriggeredYN,
            stepWaitXP, stepWaitXN, stepWaitYP, stepWaitYN,
            vib, wait2Zero, cycle,
        )

        # Leitura dos potenciômetros
        abclevel = [stepX, stepY]

        (
            res_check_pots, wait2Zero, cycle,
        ) = check_pots(
            pots, abclevel, pval,
            wait2Zero, cycle,
            triggerPot, pot_counter,
            pots_thresh_on, pots_thresh_off,
        )

        # Verifica se há resultado antes de processar
        if res_check_pots is not None:
            log(f"potsgyrotozmk {res_check_pots}", 0)
            tozmk = potsgyrotozmk(*res_check_pots)
            # log(f'send_charPs {tozmk}', 0)
            send_charPs(tozmk)
            pass

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
    start(force_calib=False)
    vibrar(init_vibrator(), 4)
