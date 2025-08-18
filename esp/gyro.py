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

