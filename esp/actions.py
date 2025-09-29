from machine import Pin, UART
import time
from printlogs import log
from config import VIBRAR_LIGADO, VIBRAR_DESLIGADO, VIBRAR_LONGO, VIBRAR_ALERTA

# UART - ajuste TX e RX conforme o seu hardware
uart = UART(1, baudrate=115200, tx=17, rx=16)

def send_charPs(zmkcodes):
    if zmkcodes is not None:
        log('send_charPs', zmkcodes, 4)
        row = zmkcodes[0]
        col = zmkcodes[1]
        pressed = 1 if zmkcodes[2] else 0

        # Proteção: valores devem estar entre 0 e 255
        if not (0 <= row <= 255 and 0 <= col <= 255):
            log(f"[WARNING] row/col fora do range: row={row}, col={col}", 0)
            return

        checksum = 0
        for b in (0x01, row, col, pressed):
            checksum ^= b

        packet = bytes([0xAA, 0x01, row, col, pressed, checksum])
        # log('packet', packet, 6)
        print('packet', packet)
        uart.write(packet)

def tsttap(row, col, delay=0.1):
    send_charPs([row, col, True])
    time.sleep(delay)
    send_charPs([row, col, False])


def vibrar(pino_vibracao, n_pulsos, step=None, ready=False):
    if pino_vibracao is None:
        log("vibrador não inicializado", 1)
        return
    if ready:
        for _ in range(n_pulsos):
            try:
                pino_vibracao.on()
            except Exception:
                try: pino_vibracao.value(1)
                except: pass
            
            # Usando as variáveis de configuração
            if step == 0: time.sleep_ms(VIBRAR_LIGADO)
            if step == 1: time.sleep_ms(VIBRAR_LONGO)
            if step == 2: time.sleep_ms(VIBRAR_ALERTA)
            else: time.sleep_ms(VIBRAR_DESLIGADO)
            
            try:
                pino_vibracao.off()
            except Exception:
                try: pino_vibracao.value(0)
                except: pass
            
            time.sleep_ms(VIBRAR_DESLIGADO)

def piscaled(pino_led, tms, n_pulsos=2):

    if pino_led is None:
        print("led não inicializado")
        return

    for _ in range(n_pulsos):
        try:
            pino_led.on()
        except Exception:
            try: pino_led.value(1)
            except: pass
        time.sleep_ms(tms)
        try:
            pino_led.off()
        except Exception:
            try: pino_led.value(0)
            except: pass
        time.sleep_ms(tms)

