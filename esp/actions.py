from machine import Pin, UART
import time
from printlogs import log
from config import VIBRAR_LIGADO, VIBRAR_DESLIGADO, VIBRAR_LONGO, VIBRAR_ALERTA

# UART - ajuste TX e RX conforme o seu hardware
uart = UART(1, baudrate=115200, tx=17, rx=16)

# --- estado global do giroscópio ---
_mouse_offset = [0, 0]  # ponto de referência atual (novo centro)

def send_mouse(dx: int, dy: int, scroll_y: int, scroll_x: int, buttons: int):
    # Limita dx/dy/scroll a int8 (-128 a 127)
    for name, val in (("dx", dx), ("dy", dy), ("scroll_y", scroll_y), ("scroll_x", scroll_x)):
        if not (-128 <= val <= 127):
            # log(f"[WARNING] {name} fora do range", val)
            return

    # Limita buttons a 0..255
    if not (0 <= buttons <= 255):
        # log(f"[WARNING] buttons fora do range", buttons)
        return

    dx_byte       = dx & 0xFF
    dy_byte       = dy & 0xFF
    scroll_y_byte = scroll_y & 0xFF
    scroll_x_byte = scroll_x & 0xFF
    buttons_byte  = buttons & 0xFF

    checksum = 0x02 ^ dx_byte ^ dy_byte ^ scroll_y_byte ^ scroll_x_byte ^ buttons_byte

    packet = bytes([
        0xAA,
        0x02,
        dx_byte,
        dy_byte,
        scroll_y_byte,
        scroll_x_byte,
        buttons_byte,
        checksum
    ])

    # print("packet:", packet)
    uart.write(packet)

def reset_mouse_center(gx, gy):
    """Define o novo ponto (0,0) relativo do mouse com base no giroscópio atual."""
    global _mouse_offset
    _mouse_offset = [gx, gy]
    # print(f"[INFO] Mouse center resetado para gx={gx}, gy={gy}")

def gyromouse(gx, gy, scale=360.0, deadzone=200.0):
    """
    scale    : fator de normalização (maior = menos sensível)
    deadzone : zona morta para ignorar pequenas variações (ruído)
    """

    # Compensa o offset
    gx = gx - _mouse_offset[0]
    gy = gy - _mouse_offset[1]

    # Aplica zona morta
    if abs(gx) < deadzone:
        gx = 0
    if abs(gy) < deadzone:
        gy = 0

    # Normaliza e limita
    dx = int(max(-128, min(127, gx / scale)))
    dy = int(max(-128, min(127, gy / scale)))

    # Inverte os sentidos
    dx = -dx
    dy = -dy
    return dx, dy


def testmouse():
    try:
        for i in range(2):
            for _ in range(10):
                send_mouse(10, 0, 0, 0, 0)
                time.sleep(0.05)
            for _ in range(10):
                send_mouse(0, 10, 0, 0, 0)
                time.sleep(0.05)
            for _ in range(10):
                send_mouse(-10, 0, 0, 0, 0)
                time.sleep(0.05)
            for _ in range(10):
                send_mouse(0, -10, 0, 0, 0)
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("Loop de teste interrompido.")

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
        # print('packet', packet)
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
