# -----------------------------
# CONFIGURAÇÕES DO SISTEMA
# -----------------------------

# Giroscópio
PORAGORA = 14000        # Limite base para thresholds
THRES_PERCENT = 0.1     # Percentual usado para criar thresholds

# Potenciômetros
THRESH_POT = [-120] * 5 # Thresholds individuais
POT_CALIBRATION_SAMPLES = 40
POT_CALIBRATION_DELAY_MS = 70

# Controle de passos automáticos
STEP_WAIT_LIMIT = 5     # Quantos ciclos esperar antes de repetir passo

# Reset
CYCLE_RESET_LIMIT = 20  # Quantos ciclos parado até resetar stepX/stepY

# Loop principal
TSLEEP = 50             # Delay entre loops (ms)
TCLEAR = 10000          # Intervalo para reset de contador
SAMPLES = 5             # Amostras iniciais do giroscópio

# Ordem dos eixos do giroscópio
GY1, GY2 = 0, 1         # Eixo X primeiro, depois Y

# -----------------------------
# DEBUG
# -----------------------------
DEBUG = False  # Se False, não imprime nada
