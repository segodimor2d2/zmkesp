import time
import os
import ujson
import config
from printlogs import log

# Variáveis globais
baseline = []
press_thresh = []
release_thresh = []
pot_counter = []
triggerPot = []
pval = []

def init_pot_globals(num_pots):
    global baseline, press_thresh, release_thresh, pot_counter, triggerPot, pval
    baseline = [0] * num_pots
    press_thresh = [0] * num_pots
    release_thresh = [0] * num_pots
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots
    pval = [0] * num_pots

def save_calibration():
    try:
        calib_data = {
            'baseline': baseline,
            'press_thresh': press_thresh,
            'release_thresh': release_thresh
        }
        with open(config.CALIB_FILE, 'w') as f:
            ujson.dump(calib_data, f)
        log("Calibração salva com sucesso!", 1)
    except Exception as e:
        log(f"Erro ao salvar calibração: {e}", 0)

def load_calibration():
    try:
        if config.CALIB_FILE in os.listdir():
            with open(config.CALIB_FILE, 'r') as f:
                calib_data = ujson.load(f)
            log("Calibração carregada do arquivo", 1)
            return calib_data['baseline'], calib_data['press_thresh'], calib_data['release_thresh']
    except Exception as e:
        log(f"Erro ao carregar calibração: {e}", 0)
    return None, None, None


def calibrate_pots(pots, force_new_calib=False):
    global baseline, press_thresh, release_thresh, pot_counter, triggerPot, pval
    
    num_pots = len(pots)
    
    # Tenta carregar calibração existente apenas se não for forçada
    if not force_new_calib:
        loaded_baseline, loaded_press, loaded_release = load_calibration()
        if loaded_baseline is not None and len(loaded_baseline) == num_pots:
            baseline = loaded_baseline
            press_thresh = loaded_press
            release_thresh = loaded_release
            log("Calibração carregada do arquivo", 1)
        else:
            log("Calibração inválida/no arquivo, fazendo nova calibração", 1)
            force_new_calib = True
    
    # Se forçado ou se não encontrou calibração válida
    if force_new_calib:
        log("Calibrando... não toque nos sensores.", 1)
        baseline = [0] * num_pots
        press_thresh = [0] * num_pots
        release_thresh = [0] * num_pots
        
        for i in range(num_pots):
            soma = 0
            for _ in range(config.CALIB_SAMPLES):  # Alterado para config.CALIB_SAMPLES
                soma += pots[i].read()
                time.sleep_ms(5)
            baseline[i] = soma / config.CALIB_SAMPLES  # Alterado para config.CALIB_SAMPLES
            press_thresh[i] = baseline[i] - config.PRESS_OFFSET  # Alterado para config.PRESS_OFFSET
            release_thresh[i] = baseline[i] - config.RELEASE_OFFSET  # Alterado para config.RELEASE_OFFSET
        
        # Salva a nova calibração
        save_calibration()
        log("Nova calibração concluída e salva!", 1)

    # Inicializa variáveis de estado
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots
    pval = [0] * num_pots

    log("Baseline:       ", baseline, 1)
    log("Press thresh:   ", press_thresh, 1)
    log("Release thresh: ", release_thresh, 1)


def check_pots(pots, abclevel, wait2Zero, cycle):
    global pval, triggerPot, pot_counter, press_thresh, release_thresh

    local_res_check_pots = None

    for i, pot in enumerate(pots):
        if i >= len(pval):
            log(f"Erro: Índice {i} fora dos limites (max {len(pval)})", 0)
            continue
            
        val = pot.read()
        pval[i] = val
        mapped_i = config.INDEX_MAP_POTS[i]

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= config.DEBOUNCE_COUNT:
                # send_charPs(potsgyrotozmk(abclevel, mapped_i, 1, config.THIS_IS))
                # log(f"[POT{mapped_i}] Pressionado | val={val} | abclevel={abclevel}", 3)
                local_res_check_pots=[abclevel, mapped_i, 1, config.THIS_IS]
                triggerPot[i] = True
                pot_counter[i] = 0
                wait2Zero = False
                cycle = 0

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= config.DEBOUNCE_COUNT:
                # send_charPs(potsgyrotozmk(abclevel, mapped_i, 0, config.THIS_IS))
                # log(f"[POT{mapped_i}] Liberado | val={val} | abclevel={abclevel}", 3)
                local_res_check_pots=[abclevel, mapped_i, 0, config.THIS_IS]
                triggerPot[i] = False
                pot_counter[i] = 0
                wait2Zero = True

        else:
            pot_counter[i] = 0

    return local_res_check_pots, wait2Zero, cycle
