import time
from hardware import pino_vibracao, mpuSensor

def vibrar(n_pulsos, step=None):
    for _ in range(n_pulsos):
        pino_vibracao.on()
        time.sleep_ms(200 if step == 0 else 101)
        pino_vibracao.off()
        time.sleep_ms(70)

def getGyro(buffer):
    mpuData = mpuSensor.get_values()
    for i, key in enumerate(['GyX', 'GyY', 'GyZ', 'AcX', 'AcY', 'AcZ']):
        buffer[i].append(mpuData[key])
    return buffer

def media(buffer):
    getGyro(buffer)
    gyro = [sum(buffer[i]) / len(buffer[i]) for i in range(3)]
    accl = [sum(buffer[i]) / len(buffer[i]) for i in range(3, 6)]
    for i in range(6):
        buffer[i].pop(0)
    return gyro, accl

def calcCalibrate(bufferPot):
    return [max(potList) for potList in bufferPot]

def getPots(bufferPot, pval):
    for i in range(5):
        bufferPot[i].append(pval[i])
    return bufferPot
