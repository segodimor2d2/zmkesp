import machine
import ubinascii


# ============================================================
# PINAGEM (ESQUERDA E DIREITA)
# ============================================================

# L 0G,1I,2C,3A,4M,5G
# L 4G,3I,2C,1A,5M,0G
PINOS_L = 12,13,14,27,4,33
INDEX_MAP_L = 4,3,2,1,5,0
PINOS_VIB_L = 26

# R 0G,1I,2C,3A,4M,5G
# R 0G,5I,1C,2A,4M,3G
PINOS_R = 12,13,14,27,4,33
INDEX_MAP_R = 0,5,1,2,4,3
PINOS_VIB_R = 26

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
# Correção: atribua diretamente a lista/tupla correta
if THIS_IS == 0:
    INDEX_MAP_POTS = list(INDEX_MAP_L)
    PINOS = list(PINOS_R)
    PINOS_VIB = PINOS_VIB_R
else:
    INDEX_MAP_POTS = list(INDEX_MAP_R)
    PINOS = list(PINOS_L)
    PINOS_VIB = PINOS_VIB_L

# ============================================================
# CONFIGURAÇÕES DE TOUCH
# ============================================================
NUMTSTSAMPLES = 2 # amostras test inicial

CALIB_POTS_FILE = "pots_calib.json"
SAMPLES_HYSTERESIS = 60 # amostras para calibrar os pots
TIMEMS_SAMPLES = 70 # tempo ms para coleta de amostras
K_SENSIBILIDADE = 3 # k: multiplicador para ajustar sensibilidade.
ALPHA_SUAVIZACAO = 0.1 # alpha: fator de suavização para baseline (0.1 = mais rápido para se adaptar).
DEBOUNCE_COUNT  = 2 # Leituras consecutivas para confirmar toque
 
# ao tocar os pots o valor diminuie por ex de 320 para 100

# 340-340*0.1 306.0
# 340-340*0.2 272.0
# 340-340*0.3 238.0
# 340-340*0.4 204.0
# 340-340*0.5 170.0
# 340-340*0.6 136.0
# 340-340*0.7 102.1
# 340-340*0.8 68.0
# 340-340*0.9 34.0

MAD_MAX = 0.2 # -80 thresholds  ON 
MAD_MIN = 0.8 # -40 thresholds OFF 



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

# Sensibilidade separada por eixo e sentido
# "X": 1.5 Eixo X vai disparar mais facilmente (thresholds ficam 50% menores).
# "Y": 1.0 Eixo Y fica normal.
# "Z": 0.7 Eixo Z fica menos sensível (precisa de movimento 30% maior).
ACCL_SENS = {
    "X_pos": 1.0,
    "X_neg": 1.0,
    "Y_pos": 1.0,
    "Y_neg": 1.0,
    "Z_pos": 1.0,
    "Z_neg": 1.0
}



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
