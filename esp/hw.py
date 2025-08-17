from machine import Pin, SoftI2C, TouchPad
import time
import config

if config.THIS_IS == 1:
    pinos = config.PINOS_R
    pinos_vib = config.PINOS_VIB_R

if config.THIS_IS == 0:
    pinos = config.PINOS_L
    pinos_vib = config.PINOS_VIB_L

def init_i2c(scl_pin=22, sda_pin=21):
    return SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))

def init_mpu(i2c):
    # importa aqui para evitar erro se rodar testes sem MPU
    try:
        import mpu6050
        mpu = mpu6050.MPU6050(i2c)
        return mpu
    except Exception as e:
        print("init_mpu erro:", e)
        return None

def init_vibrator(pin_no=(pinos_vib)):
    p = Pin(pin_no, Pin.OUT)
    try:
        p.off()
    except Exception:
        pass
    return p

def init_pots(pins=(pinos)):
    return [TouchPad(Pin(p)) for p in pins]

# teste rápido:
if __name__ == "__main__":
    i2c = init_i2c()
    mpu = init_mpu(i2c)
    vib = init_vibrator()
    pots = init_pots()
    print("hw init done, mpu:", bool(mpu), "pots:", [type(p) for p in pots])
