import machine
import ubinascii


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
# CONFIGURAÇÕES DE TOUCH
# ============================================================
CALIB_POTS_FILE = "pots_calib.json"
MAD_MIN = 5 # limites de MAD para evitar thresholds muito colados
MAD_MAX = 50 # limites de MAD para evitar thresholds muito colados
SAMPLES_HYSTERESIS = 100 # amostras para calibrar os pots
TIMEMS_SAMPLES = 70 # tempo para coleta de amostras
K_SENSIBILIDADE = 3 # k: multiplicador para ajustar sensibilidade.
ALPHA_SUAVIZACAO = 0.1 # alpha: fator de suavização para baseline (0.1 = mais rápido para se adaptar).
DEBOUNCE_COUNT  = 2 # Leituras consecutivas para confirmar toque


# ============================================================
# CONFIGURAÇÕES DO GIROSCÓPIO
# ============================================================
SAMPLES = 5       # Amostras para suavisar a curva do giroscópio
LIMGYRO = 14000   # 8000 (sensível) | 20000 (menos sensível)
THRES_PERCENT = 0.1     # 0.05 (5%) | 0.2 (20%)
GY1, GY2 = 1, 0    # Ordem dos eixos: X depois Y

if THIS_IS == 0:
    INVERT_X, INVERT_Y, INVERT_Z = False, True, True  # T,M Inverter sentido do eixo
else:
    INVERT_X, INVERT_Y, INVERT_Z = True, True, True   # T,M Inverter sentido do eixo


CALIB_ACCL_FILE = "accl_calib.json"
SAMPLES_ACCL = 100
TIME_ACCL_SAMPLES = 70
ACCL_MAD_MAX = 5 # 5
MARGIN_MIN = 2000 # 2000
MARGIN_MAX = 4000 # 4000

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


# ============================================================
# Motor Vib 
# ============================================================
VIBRAR_LIGADO = 150     # 101 default
VIBRAR_DESLIGADO = 70   # 70 default
VIBRAR_LONGO = 250      # 200 para step == 0
VIBRAR_ALERTA = 300     # 300 para step == 1




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


tstpot(row, col, delay=0.1)
tstpot(row, col)

start(force_calib=True)

"""
