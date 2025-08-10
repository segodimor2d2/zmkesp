from machine import Pin
import time

def vibrar(pino, n_pulsos, step=None):
    if not isinstance(pino, Pin):
        raise TypeError("O parâmetro 'pino' precisa ser um objeto Pin.")
    for _ in range(n_pulsos):
        pino.value(1)  # Ligar
        if step == 0:
            time.sleep_ms(200)
        else:
            time.sleep_ms(101)
        pino.value(0)  # Desligar
        time.sleep_ms(70)

def send_charPs(abckey):
    print(f"TOQUE DETECTADO! Nível: {abckey}")


