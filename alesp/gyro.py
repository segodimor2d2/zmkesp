def append_gyro(buffer, mpuSensor):
    """Adiciona uma leitura ao buffer (6 listas)"""
    if mpuSensor is None:
        # evita crash se MPU não inicializou
        return buffer
    try:
        mpuData = mpuSensor.get_values()
    except Exception as e:
        print("MPU read error:", e)
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
