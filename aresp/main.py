import time
import math
import config
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs
from pots import add_pot_samples, calc_calibrate
from gyro import append_gyro, average_and_slide

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
def calibrate_pots(pots):
    bufferPot = [[] for _ in pots]
    for _ in range(config.POT_CALIBRATION_SAMPLES):
        pval = [pot.read() for pot in pots]
        log("pot sample:", 0, pval)
        add_pot_samples(bufferPot, pval)
        time.sleep_ms(config.POT_CALIBRATION_DELAY_MS)
    log('run...', 0)
    return calc_calibrate(bufferPot)

def check_gyro_axis(axis_index, pos_thresh, neg_thresh, step, event_pos, event_neg, vib, invert=False):
    """Verifica giroscópio em um eixo e atualiza estado."""
    if not event_pos and gyro[axis_index] > pos_thresh:
        step += -1 if invert else 1
        vibrar(vib, 1, step)
        log(f"[GYRO] Eixo {axis_index} POS -> step={step}")
        event_pos = True
    elif event_pos and gyro[axis_index] <= pos_thresh:
        event_pos = False

    if not event_neg and gyro[axis_index] < neg_thresh:
        step += 1 if invert else -1
        vibrar(vib, 1, step)
        log(f"[GYRO] Eixo {axis_index} NEG -> step={step}")
        event_neg = True
    elif event_neg and gyro[axis_index] >= neg_thresh:
        event_neg = False

    return step, event_pos, event_neg

def check_step_wait(event_triggered, step_wait, step, delta, vib):
    """Controle de espera para repetição automática."""
    step_wait = step_wait + 1 if event_triggered else 0
    if step_wait >= config.STEP_WAIT_LIMIT:
        step += delta
        vibrar(vib, 1, step)
        log(f"[STEP_WAIT] step={step} delta={delta}")
        step_wait = 0
    return step_wait, step

def check_pots(pvals, thresh, triggerPot, abclevel, holdclick, wait2Zero, cycle):
    """Verifica potenciômetros e envia eventos."""
    for i, val in enumerate(pvals):
        if not triggerPot[i] and val < thresh[i]:
            send_charPs(abclevel, i, 1)
            log(f"[POT{i+1}] Pressionado | val={val} | abclevel={abclevel}")
            triggerPot[i] = True
            holdclick = True
            wait2Zero = False
            cycle = 0
        elif triggerPot[i] and val >= thresh[i]:
            send_charPs(abclevel, i, 0)
            log(f"[POT{i+1}] Liberado | val={val}")
            triggerPot[i] = False
            holdclick = False
            wait2Zero = True
    return triggerPot, holdclick, wait2Zero, cycle

# -----------------------------
# Função principal
# -----------------------------
def start(i2c=None, mpu=None, pots=None, vib=None):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()
    pot1, pot2, pot3, pot4, pot5 = pots

    # Calibração de pots
    maxCalibratePots = calibrate_pots(pots)
    log("maxCalibratePots:", maxCalibratePots)

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
    triggerPot = [False] * 5
    threshPot = config.THRESH_POT

    # Thresholds giroscópio
    threshP  = config.PORAGORA - (config.PORAGORA * config.THRES_PERCENT)
    threshN  = -config.PORAGORA + (config.PORAGORA * config.THRES_PERCENT)
    threshXP = config.PORAGORA - (config.PORAGORA * config.THRES_PERCENT)
    threshXN = -config.PORAGORA + (config.PORAGORA * config.THRES_PERCENT)

    stepX = stepY = 0
    evntTriggeredXP = evntTriggeredXN = False
    evntTriggeredYP = evntTriggeredYN = False

    wait2Zero = True
    cycle = 0
    stepWaitXP = stepWaitXN = stepWaitYP = stepWaitYN = 0

    gy1, gy2 = config.GY1, config.GY2

    vibrar(vib, 2)

    # Loop principal
    while True:
        gyro, accl = average_and_slide(buffer, mpu)

        # Movimento no eixo X
        stepX, evntTriggeredXP, evntTriggeredXN = check_gyro_axis(
            gy1, threshXP, threshXN, stepX, evntTriggeredXP, evntTriggeredXN, vib
        )

        # Movimento no eixo Y
        stepY, evntTriggeredYP, evntTriggeredYN = check_gyro_axis(
            gy2, threshP, threshN, stepY, evntTriggeredYP, evntTriggeredYN, vib
        )

        # Controle de repetição automática
        stepWaitXP, stepX = check_step_wait(evntTriggeredXP, stepWaitXP, stepX, 1 if gy1 == 0 else -1, vib)
        stepWaitXN, stepX = check_step_wait(evntTriggeredXN, stepWaitXN, stepX, -1 if gy1 == 0 else 1, vib)
        stepWaitYP, stepY = check_step_wait(evntTriggeredYP, stepWaitYP, stepY, -1 if gy1 == 0 else 1, vib)
        stepWaitYN, stepY = check_step_wait(evntTriggeredYN, stepWaitYN, stepY, 1 if gy1 == 0 else -1, vib)

        # Leitura dos potenciômetros
        pval = [pot.read() - maxCalibratePots[i] for i, pot in enumerate([pot1, pot2, pot3, pot4, pot5])]
        log(f"[POT VALS] {pval}")

        # Definição do nível
        if -1 <= stepX <= 1 and -2 <= stepY <= 2:
            abclevel = [stepX + 1, 2 - stepY]
        else:
            abclevel = None

        # Eventos de pots
        triggerPot, holdclick, wait2Zero, cycle = check_pots(
            pval, threshPot, triggerPot, abclevel, holdclick, wait2Zero, cycle
        )

        # Reset se parado
        if wait2Zero:
            cycle += 1
        if cycle == config.CYCLE_RESET_LIMIT:
            stepY = stepX = 0
            vibrar(vib, 2)
            log("[RESET] StepX e StepY resetados")

        if num % config.TCLEAR == 0:
            num = 0
        num += 1
        time.sleep_ms(config.TSLEEP)

# -----------------------------
def run():
    vibrar(init_vibrator(), 4)
    start()
