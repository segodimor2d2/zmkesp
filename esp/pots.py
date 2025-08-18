import os
import ujson
import config
from printlogs import log

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
        log("Erro ao salvar calibração:", e, 0)

def load_calibration():
    try:
        if config.CALIB_FILE in os.listdir():
            with open(config.CALIB_FILE, 'r') as f:
                calib_data = ujson.load(f)
            log("Calibração carregada do arquivo", 1)
            return calib_data['baseline'], calib_data['press_thresh'], calib_data['release_thresh']
    except Exception as e:
        log("Erro ao carregar calibração:", e, 0)
    return None, None, None
