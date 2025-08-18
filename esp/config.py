import machine
import ubinascii

# ============================================================
# CONFIGURAÇÕES DE TOUCH
# ============================================================
CALIB_FILE = "calib.json"
CALIB_SAMPLES   = 100   # Amostras por canal
PRESS_OFFSET    = 50    # Quanto abaixo do baseline aciona
RELEASE_OFFSET  = 30    # Quanto abaixo do baseline libera
DEBOUNCE_COUNT  = 3     # Leituras consecutivas para confirmar toque


# ============================================================
# CONFIGURAÇÕES DOS POTENCIÔMETROS
# ============================================================
POT_CALIBRATION_SAMPLES   = 40   # 20 (rápido) | 100 (preciso)
POT_CALIBRATION_DELAY_MS  = 70   # Delay entre leituras (ms)


# ============================================================
# CONFIGURAÇÕES DO GIROSCÓPIO
# ============================================================
LIMGYRO       = 14000   # 8000 (sensível) | 20000 (menos sensível)
THRES_PERCENT  = 0.1     # 0.05 (5%) | 0.2 (20%)
GY1, GY2       = 1, 0    # Ordem dos eixos: X depois Y
INVERT_X       = True    # Inverter sentido do eixo X
INVERT_Y       = True    # Inverter sentido do eixo Y


# ============================================================
# CONTROLE DE PASSOS / RESET
# ============================================================
STEP_WAIT_LIMIT   = 5     # Ciclos antes de repetir passo
CYCLE_RESET_LIMIT = 20    # Ciclos parado até resetar stepX/stepY


# ============================================================
# LOOP PRINCIPAL
# ============================================================
TSLEEP  = 50      # Delay entre loops (ms)
TCLEAR  = 10000   # Intervalo para reset de contador
SAMPLES = 5       # Amostras iniciais do giroscópio


# ============================================================
# PINAGEM (ESQUERDA E DIREITA)
# ============================================================
PINOS_R = 13,12,14,27,4,33
INDEX_MAP_R = 0,1,2,3,4,5
PINOS_VIB_R = 26

PINOS_L = 12,13,14,27,4,33
INDEX_MAP_L = 0,1,2,4,3,5
PINOS_VIB_L = 26

# ============================================================
# IDENTIFICAÇÃO DO CHIP / DEFINIÇÃO DO LADO
# ============================================================
chip_id = ubinascii.hexlify(machine.unique_id()).decode()
print("Chip ID:", chip_id)  # Exemplo: '240ac4083456'

# IDs conhecidos dos dois lados
alesp = '083af27f9c38'
aresp = '78e36d170944'

# Define se este chip é o lado L (0) ou R (1)
THIS_IS = 0 if chip_id == alesp else 1
print("THIS_IS:", THIS_IS)

# INDEX MAP final (depende do lado detectado)
INDEX_MAP_POTS = list(INDEX_MAP_L if THIS_IS == 0 else INDEX_MAP_R)


# ============================================================
# DEBUG
# ============================================================
DEBUG = 0
"""
| Você Quer...                  | Configuração        | Comportamento          |
|-------------------------------|---------------------|------------------------|
| Só logs de nível X            | DEBUG = X           | Ignora tudo ≠ X        |
| Todos os logs                 | DEBUG = None        | Mostra tudo            |
| Logs sem nível                | DEBUG = -1          | Mostra só os sem nível |
| Múltiplos níveis (ex: 0,1,2)  | DEBUG = [0, 1, 2]   | Mostra só esses níveis |
"""
