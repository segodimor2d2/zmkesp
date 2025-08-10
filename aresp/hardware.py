import time
from machine import Pin, SoftI2C, TouchPad
import mpu6050

# Configuração I2C e sensor MPU6050
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
mpuSensor = mpu6050.accel(i2c)

# Motor vibrador
pino_vibracao = Pin(33, Pin.OUT)

# TouchPads
pots = [
    TouchPad(Pin(13)),
    TouchPad(Pin(12)),
    TouchPad(Pin(14)),
    TouchPad(Pin(27)),
    TouchPad(Pin(4))
]
