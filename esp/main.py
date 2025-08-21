import time
import config
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs
from printlogs import log
from dicctozmk import potsgyrotozmk
from calibration import calc_pots_hysteresis
from pots import check_pots
from gyro import initial_buffer, average_and_slide, gyro_principal

def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()

    # Inicializa listas locais pots
    num_pots = len(pots)
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots
    pval = [0] * num_pots

    # Calcula thresholds de histerese
    pots_thresh_on, pots_thresh_off = calc_pots_hysteresis(pots, num_pots, vib, force_calib)
    print("Thresholds on:", pots_thresh_on)
    print("Thresholds off:", pots_thresh_off)

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    buffer = initial_buffer(buffer, mpu)
    gyro, accl = average_and_slide(buffer, mpu)

    # Variáveis de estado
    evntTriggeredXP = evntTriggeredXN = evntTriggeredYP = evntTriggeredYN = False
    stepWaitXP = stepWaitXN = stepWaitYP = stepWaitYN = 0
    stepX = stepY = num = cycle = 0
    res_check_pots = None
    wait2Zero = False

    gy1, gy2 = config.GY1, config.GY2

    vibrar(vib, 2)

    # Loop principal
    while True:
        # Lê mais um valor, calcula média e remove o mais antigo (sliding window)
        gyro, accl = average_and_slide(buffer, mpu)

        (
            stepX, stepY,
            evntTriggeredXP, evntTriggeredXN,
            evntTriggeredYP, evntTriggeredYN,
            stepWaitXP, stepWaitXN, stepWaitYP, stepWaitYN,
            wait2Zero, cycle,
        ) = gyro_principal(
            gyro, gy1, gy2,
            stepX, stepY,
            evntTriggeredXP, evntTriggeredXN,
            evntTriggeredYP, evntTriggeredYN,
            stepWaitXP, stepWaitXN, stepWaitYP, stepWaitYN,
            vib, wait2Zero, cycle,
        )

        # Leitura dos potenciômetros
        abclevel = [stepX, stepY]

        (
            res_check_pots, wait2Zero, cycle,
        ) = check_pots(
            pots, abclevel, pval,
            wait2Zero, cycle,
            triggerPot, pot_counter,
            pots_thresh_on, pots_thresh_off,
        )

        # Verifica se há resultado antes de processar
        if res_check_pots is not None:
            log(f"potsgyrotozmk {res_check_pots}", 0)
            tozmk = potsgyrotozmk(*res_check_pots)
            # log(f'send_charPs {tozmk}', 0)
            send_charPs(tozmk)
            pass

        # Reset se parado
        if wait2Zero and cycle < config.CYCLE_RESET_LIMIT:
            cycle += 1
            if cycle == config.CYCLE_RESET_LIMIT:
                stepY = stepX = 0
                vibrar(vib, 2)
                log("[RESET] StepX e StepY resetados", 2)
                wait2Zero = False
                cycle = 0

        if num % config.TCLEAR == 0:
            num = 0
        num += 1
        time.sleep_ms(config.TSLEEP)


if __name__ == "__main__":
    start(force_calib=False)
    vibrar(init_vibrator(), 4)
