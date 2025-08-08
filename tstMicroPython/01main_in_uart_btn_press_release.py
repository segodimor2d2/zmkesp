from machine import UART, Pin
import time

# Configuração do UART - deve corresponder ao transmissor
uart = UART(1, baudrate=115200, tx=17, rx=16)

# LED para feedback visual
led = Pin(2, Pin.OUT)

# Dicionários para mapear keycodes e modificadores
keycodes = {0x04: "A", 0x05: "B"}
modifiers = {0x00: "", 0x02: "Shift+"}

def process_command(cmd):
    """Processa o comando recebido"""
    if len(cmd) != 3:
        print("Comando inválido:", cmd)
        return
    
    print(cmd)
    estado, keycode, modifier = cmd
    acao = "Pressionado" if estado == 0x01 else "Soltado"
    tecla = keycodes.get(keycode, f"0x{keycode:02x}")
    modificador = modifiers.get(modifier, f"0x{modifier:02x}")
    
    # print(f"Tecla {acao}: {modificador}{tecla}")
    led.value(estado == 0x01)

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
                # Extrai e remove os 3 primeiros bytes sem usar del
                cmd = bytes(buffer[0:3])
                buffer = buffer[3:]  # Isso cria um novo bytearray
                
                process_command(cmd)
    
    time.sleep_ms(10)
