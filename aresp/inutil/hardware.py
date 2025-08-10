from machine import Pin, SoftI2C, TouchPad
import mpu6050

def init_hardware():
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
    mpuSensor = mpu6050.accel(i2c)

    pino_vibracao = Pin(33, Pin.OUT)

    pots = [
        TouchPad(Pin(13)),
        TouchPad(Pin(12)),
        TouchPad(Pin(14)),
        TouchPad(Pin(27)),
        TouchPad(Pin(4)),
    ]
    return pots, mpuSensor, pino_vibracao
