from machine import UART, Pin
import time

# Configuração do UART - deve corresponder ao transmissor
uart = UART(1, baudrate=115200, tx=17, rx=16)

# LED para feedback visual
led = Pin(2, Pin.OUT)

def process_command(cmd):
    """Processa comando no formato [row, column, pressed]"""
    if len(cmd) != 3:
        print("Comando inválido:", cmd)
        return
    
    row, column, pressed = cmd
    acao = "Pressionado" if pressed == 0x01 else "Solto"
    # print(f"Tecla [{row}, {column}] {acao}")
    print(cmd)
    
    # Feedback visual (acende o LED quando pressionado)
    led.value(pressed == 0x01)

# Buffer para armazenar bytes recebidos
buffer = bytearray()

while True:
    if uart.any():
        # Lê todos os bytes disponíveis
        data = uart.read()
        
        if data:
            buffer.extend(data)
            
            # Processa comandos completos (3 bytes cada)
            while len(buffer) >= 3:
                # Extrai e remove os 3 primeiros bytes
                cmd = bytes(buffer[0:3])
                buffer = buffer[3:]
                
                process_command(cmd)
    
    time.sleep_ms(10)
