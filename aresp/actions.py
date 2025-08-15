from machine import Pin, UART
import time

# UART - ajuste TX e RX conforme o seu hardware
uart = UART(1, baudrate=115200, tx=17, rx=16)

def send_charPs(zmkcodes):
    if zmkcodes is not None:
        print(zmkcodes)
        row = zmkcodes[0]
        col = zmkcodes[1]

        # Proteção: valores devem estar entre 0 e 255
        if not (0 <= row <= 255 and 0 <= col <= 255):
            print(f"[WARNING] row/col fora do range: row={row}, col={col}")
            return

        if zmkcodes[2] == 0:
            event_type = 0x00
        else:
            event_type = 0x01

        checksum = event_type ^ row ^ col
        packet = bytes([0xAA, event_type, row, col, checksum])
        # print(packet)
        uart.write(packet)

def tstpot(row, col, delay=0.1):
    send_charPs([row, col, True])
    time.sleep(delay)
    send_charPs([row, col, False])

def vibrar(pino_vibracao, n_pulsos, step=None):
    if pino_vibracao is None:
        print("vibrador não inicializado")
        return
    for _ in range(n_pulsos):
        try:
            pino_vibracao.on()
        except Exception:
            # alguns firmwares usam value(1)/value(0)
            try: pino_vibracao.value(1)
            except: pass
        if step == 0:
            time.sleep_ms(200)
        else:
            time.sleep_ms(101)
        try:
            pino_vibracao.off()
        except Exception:
            try: pino_vibracao.value(0)
            except: pass
        time.sleep_ms(70)

