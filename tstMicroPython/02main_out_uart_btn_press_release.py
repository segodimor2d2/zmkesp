from machine import Pin, UART
import time

# UART - verifique os pinos corretos para seu ESP32
uart = UART(1, baudrate=115200, tx=17, rx=16)

# Pino do botão
pino_botao = Pin(27, Pin.IN, Pin.PULL_UP)

estado_anterior = 1  # Botão inicialmente não pressionado (puxado para cima)

# Mapeamento do botão para a matriz
ROW = 1
COL = 2

while True:
    estado_atual = pino_botao.value()
    
    if estado_atual != estado_anterior:
        time.sleep_ms(20)
        estado_atual = pino_botao.value()
        
        if estado_atual != estado_anterior:
            if estado_atual == 0:
                print("Botão PRESSIONADO")
                uart.write(bytes([ROW, COL, 0x01]))  # pressionado
            else:
                print("Botão SOLTO")
                uart.write(bytes([ROW, COL, 0x00]))  # solto
            
            estado_anterior = estado_atual
    
    time.sleep_ms(10)
