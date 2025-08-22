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
