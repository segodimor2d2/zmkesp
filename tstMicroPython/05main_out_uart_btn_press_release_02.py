from machine import Pin, UART
import time

# Inicializar UART - ajuste os pinos conforme necessário
uart = UART(1, baudrate=115200, tx=17, rx=16)

def enviar_evento(row, col, pressionado):
    """
    Envia um evento de botão via UART.

    Args:
        row (int): número da linha.
        col (int): número da coluna.
        pressionado (bool): True para pressionado, False para solto.
    """
    tipo_evento = 0x01 if pressionado else 0x00
    checksum = tipo_evento ^ row ^ col
    packet = bytes([0xAA, tipo_evento, row, col, checksum])
    print(f"Enviando: {packet}")
    uart.write(packet)

def tocar_tecla(row, col, delay=0.1):
    """
    Simula uma tecla sendo pressionada e depois solta.

    Args:
        row (int): número da linha.
        col (int): número da coluna.
        delay (float): tempo em segundos entre pressionar e soltar.
    """
    enviar_evento(row, col, True)
    time.sleep(delay)
    enviar_evento(row, col, False)

# Lista de botões com pinos e posições na matriz
botoes = [
    {"pin": 25, "row": 0, "col": 1},
    {"pin": 26, "row": 1, "col": 1},
    {"pin": 27, "row": 2, "col": 1},
    {"pin": 32, "row": 0, "col": 2},
    {"pin": 33, "row": 1, "col": 2},
]

# Inicializar botões
for botao in botoes:
    botao["obj"] = Pin(botao["pin"], Pin.IN, Pin.PULL_UP)
    botao["estado_anterior"] = 1  # Estado inicial (não pressionado)

print("Aguardando ZMK...")
time.sleep(2)
print("Pronto para enviar eventos.")

# Loop principal
while True:
    for botao in botoes:
        estado_atual = botao["obj"].value()

        if estado_atual != botao["estado_anterior"]:
            time.sleep_ms(20)  # debounce
            estado_atual = botao["obj"].value()

            if estado_atual != botao["estado_anterior"]:
                row = botao["row"]
                col = botao["col"]
                pressionado = estado_atual == 0
                enviar_evento(row, col, pressionado)

                botao["estado_anterior"] = estado_atual

    time.sleep_ms(10)
