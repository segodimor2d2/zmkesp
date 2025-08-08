from machine import UART, Pin
import time

# Configuração do UART - deve corresponder ao transmissor
uart = UART(1, baudrate=115200, tx=17, rx=16)

# LED para feedback visual
led = Pin(2, Pin.OUT)

def process_command(cmd):
    """Processa comando no formato [0xAA, pressed, row, column]"""
    if len(cmd) != 4:
        print("Comando inválido:", cmd)
        return
    
    # Verifica o byte de sincronização (0xAA)
    if cmd[0] != 0xAA:
        print("Byte de sincronização inválido:", cmd)
        return
    
    pressed, row, column = cmd[1], cmd[2], cmd[3]
    acao = "Pressionado" if pressed == 0x01 else "Solto"
    print(f"Tecla [{row}, {column}] {acao}")
    
    # Feedback visual (acende o LED quando pressionado)
    led.value(pressed == 0x01)

# Buffer para armazenar bytes recebidos
buffer = bytearray()

print("Aguardando dados UART...")

while True:
    if uart.any():
        # Lê todos os bytes disponíveis
        data = uart.read()
        
        if data:
            buffer.extend(data)
            
            # Processa comandos completos (4 bytes cada)
            while len(buffer) >= 4:
                # Verifica se temos um comando válido começando com 0xAA
                if buffer[0] == 0xAA:
                    # Extrai e remove os 4 primeiros bytes
                    cmd = bytes(buffer[0:4])
                    buffer = buffer[4:]
                    
                    process_command(cmd)
                else:
                    # Descarta bytes inválidos até encontrar 0xAA
                    buffer = buffer[1:]
    
    time.sleep_ms(10)
