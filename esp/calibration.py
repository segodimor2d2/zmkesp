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


def calc_pots_hysteresis(pots, num_pots, vib, force_calib=False):

    baseline = [0] * num_pots
    pots_thresh_on = [0] * num_pots
    pots_thresh_off = [0] * num_pots

    if not force_calib:
        loaded_baseline, loaded_press, loaded_release = load_calibration()
        if loaded_baseline is not None and len(loaded_baseline) == num_pots:
            baseline[:] = loaded_baseline
            pots_thresh_on[:] = loaded_press
            pots_thresh_off[:] = loaded_release
            log("Calibração carregada do arquivo", 0)

            return pots_thresh_on, pots_thresh_off

        else:
            log("Calibração inválida/no arquivo, fazendo nova calibração", 0)
            force_calib = True

    if force_calib:
        vibrar(vib, 6)
        log("calc_pots_hysteresis... nao toque nos sensores.", 0)

        # k: multiplicador para ajustar sensibilidade.
        k = config.K_SENSIBILIDADE
        # alpha: fator de suavização para baseline (0.1 = mais rápido para se adaptar).
        alpha = config.ALPHA_SUAVIZACAO

        samples_count = config.SAMPLES_HYSTERESIS   # ex: 100

        # inicializa baseline com primeira leitura
        baseline = [pots[i].read() for i in range(num_pots)]
        soma_dev = [0] * num_pots

        for _ in range(samples_count):
            for i in range(num_pots):
                val = pots[i].read()
                # atualiza baseline suavizado (EMA)
                baseline[i] = (1 - alpha) * baseline[i] + alpha * val
                # acumula desvio em relação ao baseline atual
                soma_dev[i] += abs(val - baseline[i])
            time.sleep_ms(config.TIMEMS_SAMPLES)

        # mad = [s / samples_count for s in soma_dev]
        mad = [max(config.MAD_MIN, min(s / samples_count, config.MAD_MAX)) for s in soma_dev]

        pots_thresh_on  = [baseline[i] - k * mad[i] for i in range(num_pots)]
        pots_thresh_off = [baseline[i] - (k/2) * mad[i] for i in range(num_pots)]

        save_calibration(baseline, pots_thresh_on, pots_thresh_off)
        log("Nova calibração concluída e salva!", 0)
        vibrar(vib, 6)

        return pots_thresh_on, pots_thresh_off
