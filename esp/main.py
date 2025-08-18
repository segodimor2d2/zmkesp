import time
import math
import config
import ujson
import os
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs
from pots import load_calibration, save_calibration
from gyro import append_gyro, average_and_slide
from dicctozmk import potsgyrotozmk

# -----------------------------
# CONFIG TOUCH
# -----------------------------
CALIB_SAMPLES   = config.CALIB_SAMPLES
PRESS_OFFSET    = config.PRESS_OFFSET
RELEASE_OFFSET  = config.RELEASE_OFFSET
DEBOUNCE_COUNT  = config.DEBOUNCE_COUNT
INDEX_MAP_POTS  = config.INDEX_MAP_POTS

# ===== VARIÁVEIS GLOBAIS =====
baseline        = []
press_thresh    = []
release_thresh  = []
pot_counter     = []
triggerPot      = []
pval            = []

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

# -----------------------------
# Funções auxiliares
# -----------------------------
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
            print("Calibração carregada do arquivo")
        else:
            print("Calibração inválida/no arquivo, fazendo nova calibração")
            force_new_calib = True
    
    # Se forçado ou se não encontrou calibração válida
    if force_new_calib:
        print("Calibrando... não toque nos sensores.")
        baseline = [0] * num_pots
        press_thresh = [0] * num_pots
        release_thresh = [0] * num_pots
        
        for i in range(num_pots):
            soma = 0
            for _ in range(CALIB_SAMPLES):
                soma += pots[i].read()
                time.sleep_ms(5)
            baseline[i] = soma / CALIB_SAMPLES
            press_thresh[i] = baseline[i] - PRESS_OFFSET
            release_thresh[i] = baseline[i] - RELEASE_OFFSET
        
        # Salva a nova calibração
        save_calibration(baseline, press_thresh, release_thresh)
        print("Nova calibração concluída e salva!")

    # Inicializa variáveis de estado
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots
    pval = [0] * num_pots

    print("Baseline:       ", baseline)
    print("Press thresh:   ", press_thresh)
    print("Release thresh: ", release_thresh)

def check_gyro_axis(axis_index, pos_thresh, neg_thresh, step, event_pos, event_neg, vib, wait2Zero, cycle, invert=False):
    """Verifica giroscópio em um eixo e atualiza estado."""
    if not event_pos and gyro[axis_index] > pos_thresh:
        step += -1 if invert else 1
        vibrar(vib, 1, step)
        log(f"[GYRO] Eixo {axis_index} POS -> step={step}")
        event_pos = True
        wait2Zero = True
        cycle = 0
    elif event_pos and gyro[axis_index] <= pos_thresh:
        event_pos = False

    if not event_neg and gyro[axis_index] < neg_thresh:
        step += 1 if invert else -1
        vibrar(vib, 1, step)
        log(f"[GYRO] Eixo {axis_index} NEG -> step={step}")
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
        log(f"[STEP_WAIT] step={step} delta={delta}")
        step_wait = 0
    return step_wait, step

def check_pots(pots, abclevel, wait2Zero, cycle):
    global pval, triggerPot, pot_counter

    for i, pot in enumerate(pots):
        val = pot.read()
        pval[i] = val
        mapped_i = INDEX_MAP_POTS[i]

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 1, config.THIS_IS))
                log(f"[POT{mapped_i}] Pressionado | val={val} | abclevel={abclevel}", 2)
                triggerPot[i] = True
                pot_counter[i] = 0
                wait2Zero = False
                cycle = 0

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 0, config.THIS_IS))
                log(f"[POT{mapped_i}] Liberado | val={val} | abclevel={abclevel}", 2)
                triggerPot[i] = False
                pot_counter[i] = 0
                wait2Zero = True

        else:
            pot_counter[i] = 0

    return wait2Zero, cycle

# -----------------------------
# Função principal
# -----------------------------
def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()

    if pots is None: pots = init_pots()
    num_pots = len(pots)   # agora detecta sozinho

    # Calibração de pots
    calibrate_pots(pots, force_calib)

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    for _ in range(config.SAMPLES - 1):
        append_gyro(buffer, mpu)
        time.sleep_ms(70)
    global gyro
    gyro, accl = average_and_slide(buffer, mpu)

    # Variáveis de estado
    num = 0
    holdclick = False
    triggerPot = [False] * num_pots

    # Thresholds giroscópio
    threshP  = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    threshN  = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)
    threshXP = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    threshXN = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)

    stepX = stepY = 0
    evntTriggeredXP = evntTriggeredXN = False
    evntTriggeredYP = evntTriggeredYN = False

    wait2Zero = False
    cycle = 0
    stepWaitXP = stepWaitXN = stepWaitYP = stepWaitYN = 0

    gy1, gy2 = config.GY1, config.GY2

    vibrar(vib, 2)

    # Loop principal
    while True:
        gyro, accl = average_and_slide(buffer, mpu)

        # Movimento no eixo X
        stepX, evntTriggeredXP, evntTriggeredXN, wait2Zero, cycle = check_gyro_axis(
            gy1, threshXP, threshXN, stepX, evntTriggeredXP, evntTriggeredXN, vib, wait2Zero, cycle, invert=config.INVERT_X
        )

        # Movimento no eixo Y
        stepY, evntTriggeredYP, evntTriggeredYN, wait2Zero, cycle = check_gyro_axis(
            gy2, threshP, threshN, stepY, evntTriggeredYP, evntTriggeredYN, vib, wait2Zero, cycle, invert=config.INVERT_Y
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
                log("[RESET] StepX e StepY resetados")
                wait2Zero = False
                cycle = 0

        if num % config.TCLEAR == 0:
            num = 0
        num += 1
        time.sleep_ms(config.TSLEEP)

# -----------------------------
# def run():
#     vibrar(init_vibrator(), 4)
#     start()

start()
vibrar(init_vibrator(), 4)
