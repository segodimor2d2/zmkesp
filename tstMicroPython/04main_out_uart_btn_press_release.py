from machine import Pin, UART
import time

# UART - verifique os pinos corretos para seu ESP32
uart = UART(1, baudrate=115200, tx=17, rx=16)

# Pino do botão
pino_botao = Pin(27, Pin.IN, Pin.PULL_UP)

estado_anterior = 1  # Botão inicialmente não pressionado

# Mapeamento do botão para a matriz (row e col do keymap do ZMK)
ROW = 1
COL = 2

# Delay inicial para garantir que o ZMK já iniciou
print("Aguardando ZMK...")
time.sleep(2)

print("Pronto para enviar eventos UART com checksum.")

while True:
    estado_atual = pino_botao.value()

    if estado_atual != estado_anterior:
        time.sleep_ms(20)  # debounce
        estado_atual = pino_botao.value()

        if estado_atual != estado_anterior:
            if estado_atual == 0:
                print("Botão PRESSIONADO")
                event_type = 0x01  # Press
            else:
                print("Botão SOLTO")
                event_type = 0x00  # Release

            checksum = event_type ^ ROW ^ COL
            packet = bytes([0xAA, event_type, ROW, COL, checksum])
            uart.write(packet)

            estado_anterior = estado_atual

    time.sleep_ms(10)
