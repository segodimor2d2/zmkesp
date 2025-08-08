from machine import Pin, UART
import time

# UART - ajuste TX e RX conforme o seu hardware
uart = UART(1, baudrate=115200, tx=17, rx=16)

# Lista de botões e seu mapeamento na matriz (ROW, COL)
botoes = [
    {"pin": 25, "row": 0, "col": 1},
    {"pin": 26, "row": 1, "col": 1},
    {"pin": 27, "row": 2, "col": 1},
    {"pin": 32, "row": 0, "col": 2},
    {"pin": 33, "row": 1, "col": 2},
]

# Inicializar os botões com PULL_UP
for botao in botoes:
    botao["obj"] = Pin(botao["pin"], Pin.IN, Pin.PULL_UP)
    botao["estado_anterior"] = 1  # Botão não pressionado

# Delay para garantir que o ZMK iniciou
print("Aguardando ZMK...")
time.sleep(2)
print("Pronto para enviar eventos UART com checksum.")

while True:
    for botao in botoes:
        estado_atual = botao["obj"].value()

        if estado_atual != botao["estado_anterior"]:
            time.sleep_ms(20)  # debounce
            estado_atual = botao["obj"].value()

            if estado_atual != botao["estado_anterior"]:
                row = botao["row"]
                col = botao["col"]

                if estado_atual == 0:
                    #print(f"Botão {botao['pin']} PRESSIONADO")
                    event_type = 0x01
                else:
                    #print(f"Botão {botao['pin']} SOLTO")
                    event_type = 0x00

                checksum = event_type ^ row ^ col
                packet = bytes([0xAA, event_type, row, col, checksum])
                print(packet)
                uart.write(packet)

                botao["estado_anterior"] = estado_atual

    time.sleep_ms(10)

