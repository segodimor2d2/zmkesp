import time
import os
import ujson
import config
from printlogs import log
from actions import vibrar

def save_calibration(baseline, press_thresh, release_thresh):
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

def calibrate_pots(pots, baseline, press_thresh, release_thresh, pot_counter, triggerPot, pval, vib=None, force_new_calib=False):
    num_pots = len(pots)
    
    # Tenta carregar calibração existente apenas se não for forçada
    if not force_new_calib:
        loaded_baseline, loaded_press, loaded_release = load_calibration()
        if loaded_baseline is not None and len(loaded_baseline) == num_pots:
            baseline[:] = loaded_baseline
            press_thresh[:] = loaded_press
            release_thresh[:] = loaded_release
            log("Calibração carregada do arquivo", 0)
        else:
            log("Calibração inválida/no arquivo, fazendo nova calibração", 0)
            force_new_calib = True
    
    if force_new_calib:
        vibrar(vib, 4)
        log("Calibrando... não toque nos sensores.", 0)
        for i in range(num_pots):
            soma = 0
            for _ in range(config.CALIB_SAMPLES):
                soma += pots[i].read()
                time.sleep_ms(5)
            baseline[i] = soma / config.CALIB_SAMPLES
            press_thresh[i] = baseline[i] - config.PRESS_OFFSET
            release_thresh[i] = baseline[i] - config.RELEASE_OFFSET
        
        save_calibration(baseline, press_thresh, release_thresh)
        log("Nova calibração concluída e salva!", 0)
        vibrar(vib, 4)

    # Inicializa variáveis de estado
    for i in range(num_pots):
        pot_counter[i] = 0
        triggerPot[i] = False
        pval[i] = 0

    log("Baseline:       ", baseline, 0)
    log("Press thresh:   ", press_thresh, 0)
    log("Release thresh: ", release_thresh, 0)


def check_pots(pots, abclevel, wait2Zero, cycle, pval, triggerPot, pot_counter, press_thresh, release_thresh):
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
                local_res_check_pots = [abclevel, mapped_i, 1, config.THIS_IS]
                triggerPot[i] = True
                pot_counter[i] = 0
                wait2Zero = False
                cycle = 0

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= config.DEBOUNCE_COUNT:
                local_res_check_pots = [abclevel, mapped_i, 0, config.THIS_IS]
                triggerPot[i] = False
                pot_counter[i] = 0
                wait2Zero = True

        else:
            pot_counter[i] = 0

    return local_res_check_pots, wait2Zero, cycle
