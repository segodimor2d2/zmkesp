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

class AcclState:
    def __init__(self):
        self.velX = 0
        self.velY = 0
        self.velZ = 0
        self.evXP = False
        self.evXN = False
        self.evYP = False
        self.evYN = False
        self.evZP = False
        self.evZN = False
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

def check_gyro_axis(gyro, axis_index, step, event_pos, event_neg, vib, ready, wait2Zero, cycle, invert=False):
    """Verifica giroscópio em um eixo e atualiza estado."""
    pos_thresh = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    neg_thresh = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)

    if not event_pos and gyro[axis_index] > pos_thresh:
        step += -1 if invert else 1
        vibrar(vib, 1, step, ready=ready)
        event_pos = True
        wait2Zero = True
        cycle = 0
    elif event_pos and gyro[axis_index] <= pos_thresh:
        event_pos = False

    if not event_neg and gyro[axis_index] < neg_thresh:
        step += 1 if invert else -1
        vibrar(vib, 1, step, ready=ready)
        event_neg = True
        wait2Zero = True
        cycle = 0
    elif event_neg and gyro[axis_index] >= neg_thresh:
        event_neg = False

    return step, event_pos, event_neg, wait2Zero, cycle

def check_step_wait(event_triggered, step_wait, step, delta, vib, ready):
    """Controle de espera para repetição automática."""
    step_wait = step_wait + 1 if event_triggered else 0
    if step_wait >= config.STEP_WAIT_LIMIT:
        step += delta
        vibrar(vib, 1, step, ready=ready)
        step_wait = 0
    return step_wait, step

def gyro_principal(gyro, gy1, gy2, vib, ready, state: GyroState):
    """Processa movimentos do giroscópio e atualiza estado."""

    # Movimento no eixo X
    state.stepX, state.evXP, state.evXN, state.wait2Zero, state.cycle = check_gyro_axis(
        gyro, gy1, state.stepX,
        state.evXP, state.evXN,
        vib, ready, state.wait2Zero, state.cycle,
        invert=config.INVERT_X
    )

    # Movimento no eixo Y
    state.stepY, state.evYP, state.evYN, state.wait2Zero, state.cycle = check_gyro_axis(
        gyro, gy2, state.stepY,
        state.evYP, state.evYN,
        vib, ready, state.wait2Zero, state.cycle,
        invert=config.INVERT_Y
    )

    # Controle de repetição automática
    invX = -1 if config.INVERT_X else 1
    invY = -1 if config.INVERT_Y else 1

    state.swXP, state.stepX = check_step_wait(state.evXP, state.swXP, state.stepX, invX * (1 if gy1 == 0 else -1), vib, ready)
    state.swXN, state.stepX = check_step_wait(state.evXN, state.swXN, state.stepX, invX * (-1 if gy1 == 0 else 1), vib, ready)
    state.swYP, state.stepY = check_step_wait(state.evYP, state.swYP, state.stepY, invY * (-1 if gy1 == 0 else 1), vib, ready)
    state.swYN, state.stepY = check_step_wait(state.evYN, state.swYN, state.stepY, invY * (1 if gy1 == 0 else -1), vib, ready)

    return state

def check_accl_axis(accl, axis_index, step, event_pos, event_neg, thresholds, axis_key, invert=False, k=0.01):
    t = thresholds[axis_key]
    a = accl[axis_index]

    # Ajusta thresholds com fator de sensibilidade
    sens = getattr(config, "ACCL_SENS", {}).get(axis_key, 1.0)
    on_pos  = t["on_pos"]  * sens
    off_pos = t["off_pos"] * sens
    on_neg  = t["on_neg"]  * sens
    off_neg = t["off_neg"] * sens

    velocidade = 0  # padrão = parado

    # Movimento positivo
    if not event_pos and a > on_pos:
        event_pos = True
    elif event_pos and a < off_pos:
        event_pos = False

    if event_pos:
        # calcula velocidade proporcional ao quanto passou do off_pos
        velocidade = k * (a - off_pos)
        if invert:
            velocidade = -velocidade

    # Movimento negativo
    if not event_neg and a < on_neg:
        event_neg = True
    elif event_neg and a > off_neg:
        event_neg = False

    if event_neg:
        # calcula velocidade proporcional ao quanto passou do off_neg
        velocidade = k * (a - off_neg)
        if not invert:
            velocidade = -velocidade

    # ===== Reset para zero quando estável =====
    if off_neg < a < off_pos and not event_pos and not event_neg:
        velocidade = 0

    return velocidade, event_pos, event_neg

def accl_principal(accl, thresholds, state: AcclState):
    # Eventos do Acelerômetro
    state.velX, state.evXP, state.evXN = check_accl_axis(
        accl, 0, state.velX, state.evXP, state.evXN,
        thresholds, "X", invert=config.INVERT_X
    )

    state.velY, state.evYP, state.evYN = check_accl_axis(
        accl, 1, state.velY, state.evYP, state.evYN,
        thresholds, "Y", invert=config.INVERT_Y
    )

    state.velZ, state.evZP, state.evZN = check_accl_axis(
        accl, 2, state.velZ, state.evZP, state.evZN,
        thresholds, "Z", invert=config.INVERT_Z
    )

    print("accl_states", state.velX, state.velY, state.velZ)

    return state
