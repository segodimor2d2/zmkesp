import os
import ujson
import config

def save_calibration(baseline, press_thresh, release_thresh):
    try:
        calib_data = {
            'baseline': baseline,
            'press_thresh': press_thresh,
            'release_thresh': release_thresh
        }
        with open(config.CALIB_FILE, 'w') as f:
            ujson.dump(calib_data, f)
        print("Calibração salva com sucesso!")
    except Exception as e:
        print("Erro ao salvar calibração:", e)

def load_calibration():
    try:
        if config.CALIB_FILE in os.listdir():
            with open(config.CALIB_FILE, 'r') as f:
                calib_data = ujson.load(f)
            print("Calibração carregada do arquivo")
            return calib_data['baseline'], calib_data['press_thresh'], calib_data['release_thresh']
    except Exception as e:
        print("Erro ao carregar calibração:", e)
    return None, None, None
