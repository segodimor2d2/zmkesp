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
        with open(config.CALIB_POTS_FILE, 'w') as f:
            ujson.dump(calib_data, f)
        log("Pots Calibração dos pots salva com sucesso!", 1)
    except Exception as e:
        log(f"Erro ao salvar calibração dos pots: {e}", 0)

def load_calibration():
    try:
        if config.CALIB_POTS_FILE in os.listdir():
            with open(config.CALIB_POTS_FILE, 'r') as f:
                calib_data = ujson.load(f)
            log("Calibração dos pots carregada!", 1)
            return calib_data['baseline'], calib_data['press_thresh'], calib_data['release_thresh']
    except Exception as e:
        log(f"Erro ao carregar calibração dos pots: {e}", 0)
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
            return pots_thresh_on, pots_thresh_off

        else:
            log("Calibração inválida dos pots carregada!", 0)
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
        vibrar(vib, 6)

        return pots_thresh_on, pots_thresh_off


def save_accl_calibration(baselines, thresholds):
    try:
        calib_data = {
            'baselines': baselines,
            'thresholds': thresholds
        }
        with open(config.CALIB_ACCL_FILE, 'w') as f:   # usar outro arquivo
            ujson.dump(calib_data, f)
        log("Calibração do acelerômetro salva com sucesso!", 0)
    except Exception as e:
        log(f"Erro ao salvar calibração do acelerômetro: {e}", 0)


def load_accl_calibration():
    try:
        if config.CALIB_ACCL_FILE in os.listdir():
            with open(config.CALIB_ACCL_FILE, 'r') as f:
                calib_data = ujson.load(f)
            log("Calibração do acelerômetro carregada!", 0)
            return calib_data['baselines'], calib_data['thresholds']
    except Exception as e:
        log(f"Erro ao carregar calibração do acelerômetro: {e}", 0)
    return None, None


def calc_accl_hysteresis(mpu, vib, force_calib=False):

    if not force_calib:
        baselines, thresholds = load_accl_calibration()
        if thresholds is not None:
            return thresholds
        else:
            log("Calibração do acelerômetro inválida/no arquivo, fazendo nova calibração", 0)
            force_calib = True

    if force_calib:
        vibrar(vib, 6)
        log("calc_accel_hysteresis... nao toque nos sensores.", 0)

        # ======== CALIBRAÇÃO ========
        N = config.SAMPLES_ACCL
        samples = {"X": [], "Y": [], "Z": []}

        for _ in range(N):
            vals = mpu.get_values()
            samples["X"].append(vals["AcX"])
            samples["Y"].append(vals["AcY"])
            samples["Z"].append(vals["AcZ"])
            time.sleep_ms(config.TIME_ACCL_SAMPLES)

        # Calcula baseline e ruído de cada eixo
        baselines = {}
        noises = {}
        for axis in ["X", "Y", "Z"]:
            baselines[axis] = sum(samples[axis]) / N
            noises[axis] = max(samples[axis]) - min(samples[axis])

        # Define thresholds com histerese para cada eixo
        thresholds = {}
        for axis in ["X", "Y", "Z"]:
            baseline = baselines[axis]
            noise = noises[axis]
            thresholds[axis] = {
                "on_pos":  baseline + noise * 3,
                "off_pos": baseline + noise * 2,
                "on_neg":  baseline - noise * 3,
                "off_neg": baseline - noise * 2
            }

        save_accl_calibration(baselines, thresholds)
        vibrar(vib, 6)
        return thresholds

