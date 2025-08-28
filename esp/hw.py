from machine import Pin, SoftI2C, TouchPad
import time
import config
from printlogs import log

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

def init_vibrator(pin_no=(pinos_vib)):
    p = Pin(pin_no, Pin.OUT)
    try:
        p.off()
    except Exception:
        pass
    return p

def test_pots():
    touch_pins = [4, 0, 2, 15, 13, 12, 14, 27, 33, 32]  # possíveis pinos touch no ESP32
    erros = []  # lista para guardar pinos problemáticos
    for pin in touch_pins:
        try:
            tp = TouchPad(Pin(pin))
            vals = []
            for _ in range(numsamples):
                vals.append(tp.read())
                time.sleep_ms(tsamples)
            print(f"OK: TouchPad inicializado no pino {pin}, leituras = {vals}")
        except Exception as e:
            print(f"ERRO no pino {pin}: {e}")
            erros.append(pin)

    # Resumo final
    if erros:
        print("Pinos com problema:", ", ".join(str(p) for p in erros))
        print("******************************\n")
    else:
        print("Todos os pinos testados estão funcionando!")
        print("******************************\n")

def init_pots(pins=(pinos)):
    try:
        test_pots()
        pots = [TouchPad(Pin(p)) for p in pins]
        return pots
    except Exception as e:
        # sys.exit("encerrando programa.")
        # raise SystemExit
        # raise KeyboardInterrupt("Parando programa!")
        log("init_mpu erro:", e, 0)
        return None

