# -----------------------------
# CONFIGURAÇÕES DO SISTEMA
# -----------------------------

# Pinos dos touchpads
THIS_IS = 0 # 0=L, 1=R

# Potenciômetros
## Thresholds individuais
THRESH_POT = [-120] * 5 # -50 (muito sensível) e -200 (pouco sensível)
POT_CALIBRATION_SAMPLES = 40 # 20 (rápido) e 100 (preciso)
POT_CALIBRATION_DELAY_MS = 70 # 0ms e 100ms. 70ms permite leituras estáveis

# Giroscópio
## Limite base para thresholds
PORAGORA = 14000        # 8000 (mais sensível) e 20000 (menos sensível)
# Percentual usado para criar thresholds
THRES_PERCENT = 0.1     # 0.05 (5%) e 0.2 (20%). 0.1 (10%)

# Controle de passos automáticos
STEP_WAIT_LIMIT = 5     # Quantos ciclos esperar antes de repetir passo

# Reset
CYCLE_RESET_LIMIT = 30  # Quantos ciclos parado até resetar stepX/stepY

# Loop principal
TSLEEP = 50             # Delay entre loops (ms)
TCLEAR = 10000          # Intervalo para reset de contador
SAMPLES = 5             # Amostras iniciais do giroscópio

# Inverter sentido do eixo X e/ou Y
INVERT_X = True         # True re(+) ar(-) False o contrario
INVERT_Y = True         # True re(+) ar(-) False o contrario

# Ordem dos eixos do giroscópio
GY1, GY2 = 0, 1         # Eixo X primeiro, depois Y

PINOS_R = 13,12,14,27,4
INDEX_MAP_R = 0,1,2,3,4
PINOS_VIB_R = 33

PINOS_L = 12,13,14,27,4
INDEX_MAP_L = 0,1,2,3,4
PINOS_VIB_L = 32


# -----------------------------
# DEBUG
# -----------------------------
DEBUG = 0
"""
| Você Quer...                  | Configuração        | Comportamento          |
|-------------------------------|---------------------|------------------------|
| Só logs de nível X            | `DEBUG = X`         | Ignora tudo ≠ X        |
| Todos os logs                 | `DEBUG = None`      | Mostra tudo            |
| Logs sem nível                | `DEBUG = -1`        | Mostra só os sem nível |
| Múltiplos níveis (ex: 0,1,2)  | `DEBUG = [0, 1, 2]` | Mostra só esses níveis |
"""


