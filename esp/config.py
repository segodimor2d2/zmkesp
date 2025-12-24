import machine
import ubinascii


# ============================================================
# PINAGEM (ESQUERDA E DIREITA)
# ============================================================

INDEX_MAP_L = 9,10,11,4,3,2,1,0,5,6,7,8
PINOS_VIB_L = 26

INDEX_MAP_R = 8,7,6,5,0,1,2,3,4,9,10,11
PINOS_VIB_R = 26

# ============================================================
# IDENTIFICAÇÃO DO CHIP / DEFINIÇÃO DO LADO
# ============================================================
chip_id = ubinascii.hexlify(machine.unique_id()).decode()
print("Chip ID:", chip_id)  # Exemplo: '240ac4083456'

# IDs conhecidos dos dois lados
alesp = '78e36d650258'
aresp = 'ece334147530'

# Define se este chip é o lado L (0) ou R (1)
THIS_IS = 0 if chip_id == alesp else 1
print("THIS_IS:", THIS_IS)

# INDEX MAP final (depende do lado detectado)
# Correção: atribua diretamente a lista/tupla correta
if THIS_IS == 0:
    INDEX_MAP_POTS = list(INDEX_MAP_L)
    PINOS_VIB = PINOS_VIB_L
else:
    INDEX_MAP_POTS = list(INDEX_MAP_R)
    PINOS_VIB = PINOS_VIB_R

# ============================================================
# CONFIGURAÇÕES WIFI 
# ============================================================
# red ,xxxx , serverflask
REDES = [
    ["MIR2D2", "3e4r5t6y7u", "http://192.168.31.127:5050"],
    ["wff5", "3e4r5t6y7u", "http://192.0.0.2:5050"],
    # ["wff5", "3e4r5t6y7u", "http://192.168.31.13:5050"],
    ["sego", "3e4r5t6y7u", "http://192.168.31.129:5050"],
]

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
MAD_MAX = 0.2 # -80 thresholds  ON 
MAD_MIN = 0.8 # -40 thresholds OFF 

# ============================================================
# CONFIGURAÇÕES DO GIROSCÓPIO
# ============================================================
SAMPLES = 5       # Amostras para suavisar a curva do giroscópio
LIMGYRO = 14000   # 8000 (sensível) | 20000 (menos sensível)
THRES_PERCENT = 0.1     # 0.05 (5%) | 0.2 (20%)

GY1, GY2 = 1, 0    # Ordem dos eixos: X,Y (T,M=1,0) (M,T=0,1)

if THIS_IS == 0: # Inverter sentido do eixo
    INVERT_X, INVERT_Y, INVERT_Z = True, False, True # T,M 
else:
    INVERT_X, INVERT_Y, INVERT_Z = True, True, True  # T,M

CALIB_ACCL_FILE = "accl_calib.json"
SAMPLES_ACCL = 100
TIME_ACCL_SAMPLES = 70
ACCL_MAD_MAX = 5 # 5
MARGIN_MIN = 2000 # 2000
MARGIN_MAX = 4000 # 4000

# MOUSE SENSITIVITY - fator de normalização (maior = menos sensível)
MOUSESENSX = 260.0
MOUSESENSY = 360.0

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
CYCLE_RESET_LIMIT = 10    # Ciclos parado até resetar stepX/stepY

# ============================================================
# LOOP PRINCIPAL
# ============================================================
TSLEEP  = 50      # Delay entre loops (ms)
TCLEAR  = 15000   # Intervalo para reset de contador

# ============================================================
# Motor Vib / LED
# ============================================================
VIBRAR_DESLIGADO = 90   # 70 default
VIBRAR_LIGADO = 120     # 101 default == 0
VIBRAR_LONGO = 250      # 200 para step == 1
VIBRAR_ALERTA = 300     # 300 para step == 2

LEDREADY = True # Pisca no step do giro

# ============================================================
# DEBUG
# ============================================================
DEBUG = 0

"""
# testando
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
