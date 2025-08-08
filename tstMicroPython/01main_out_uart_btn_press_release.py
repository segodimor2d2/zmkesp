from machine import Pin, UART
import time

# Configuração do UART (ajuste os pinos conforme sua conexão)
# UART 1 - TX: GPIO10 (pino 14), RX: GPIO9 (pino 13) - Verifique os pinos do seu ESP32
uart = UART(1, baudrate=115200, tx=17, rx=16)  # Altere os pinos se necessário

# Configuração do pino do botão
pino_botao = Pin(27, Pin.IN, Pin.PULL_UP)

# Variável para armazenar o estado anterior do botão
estado_anterior = 1  # 1 = não pressionado (pull-up), 0 = pressionado

# Definir o keycode e modificadores (ajuste conforme necessário)
KEYCODE = 0x04  # Exemplo: tecla 'A'
MODIFIERS = 0x02  # Exemplo: Shift

while True:
    estado_atual = pino_botao.value()
    
    # Verifica se o estado mudou
    if estado_atual != estado_anterior:
        # Debounce - espera um pouco para evitar leituras falsas
        time.sleep_ms(20)
        estado_atual = pino_botao.value()  # Lê novamente após o debounce
        
        if estado_atual != estado_anterior:
            if estado_atual == 0:
                print("Botão PRESSIONADO")
                # Envia comando de pressionar via UART
                uart.write(bytes([0x01, KEYCODE, MODIFIERS]))
            else:
                print("Botão SOLTO")
                # Envia comando de soltar via UART
                uart.write(bytes([0x00, KEYCODE, MODIFIERS]))
            
            # Atualiza o estado anterior
            estado_anterior = estado_atual
    
    # Pequena pausa para não sobrecarregar o processador
    time.sleep_ms(10)
