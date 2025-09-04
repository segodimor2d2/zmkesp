from machine import Pin, SoftI2C, TouchPad
import time
import config
from printlogs import log
from mpr121 import MPR121

pinos = config.PINOS
pinos_vib = config.PINOS_VIB
numsamples = config.NUMTSTSAMPLES
tsamples = config.TIMEMS_SAMPLES

def init_i2c(scl_pin=22, sda_pin=21):
    return SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

def init_mpu(i2c):
    # importa aqui para evitar erro se rodar testes sem MPU
    try:
        import mpu6050
        mpu = mpu6050.MPU6050(i2c)
        return mpu
    except Exception as e:
        log("init_mpu erro:", e, 0)
        return None

def init_mpr121(i2c):
    try:
        return MPR121(i2c)
    except Exception as e:
        log("init_mpr121 erro:", e, 0)
        return None

def init_vibrator(pin_no=(pinos_vib)):
    p = Pin(pin_no, Pin.OUT)
    try:
        p.off()
    except Exception:
        pass
    return p


