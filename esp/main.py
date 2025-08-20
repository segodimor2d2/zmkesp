import time
import config
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs
from printlogs import log
from dicctozmk import potsgyrotozmk
from pots import init_pot_globals, calibrate_pots, check_pots
from gyro import append_gyro, average_and_slide, check_gyro_axis, check_step_wait

def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()
    
    # Inicializa variáveis globais dos potenciômetros
    init_pot_globals(len(pots))
    
    # Calibração de pots
    calibrate_pots(pots, vib, force_calib)

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    for _ in range(config.SAMPLES - 1):
        append_gyro(buffer, mpu)
        time.sleep_ms(70)
    
    gyro, accl = average_and_slide(buffer, mpu)

    # Variáveis de estado
    num = 0
    stepX = stepY = 0
    evntTriggeredXP = evntTriggeredXN = False
    evntTriggeredYP = evntTriggeredYN = False
    wait2Zero = False
    res_check_pots = None
    cycle = 0
    stepWaitXP = stepWaitXN = stepWaitYP = stepWaitYN = 0

    # Thresholds giroscópio
    threshXP = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    threshXN = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)
    threshYP = config.LIMGYRO - (config.LIMGYRO * config.THRES_PERCENT)
    threshYN = -config.LIMGYRO + (config.LIMGYRO * config.THRES_PERCENT)

    gy1, gy2 = config.GY1, config.GY2

    vibrar(vib, 2)

    # Loop principal
    while True:
        gyro, accl = average_and_slide(buffer, mpu)

        # Movimento no eixo X
        stepX, evntTriggeredXP, evntTriggeredXN, wait2Zero, cycle = check_gyro_axis(
            gyro, gy1, threshXP, threshXN, stepX, evntTriggeredXP, evntTriggeredXN, vib, wait2Zero, cycle, invert=config.INVERT_X
        )

        # Movimento no eixo Y
        stepY, evntTriggeredYP, evntTriggeredYN, wait2Zero, cycle = check_gyro_axis(
            gyro, gy2, threshYP, threshYN, stepY, evntTriggeredYP, evntTriggeredYN, vib, wait2Zero, cycle, invert=config.INVERT_Y
        )

        # Controle de repetição automática
        invX = -1 if config.INVERT_X else 1
        invY = -1 if config.INVERT_Y else 1

        stepWaitXP, stepX = check_step_wait(evntTriggeredXP, stepWaitXP, stepX, invX * (1 if gy1 == 0 else -1), vib)
        stepWaitXN, stepX = check_step_wait(evntTriggeredXN, stepWaitXN, stepX, invX * (-1 if gy1 == 0 else 1), vib)
        stepWaitYP, stepY = check_step_wait(evntTriggeredYP, stepWaitYP, stepY, invY * (-1 if gy1 == 0 else 1), vib)
        stepWaitYN, stepY = check_step_wait(evntTriggeredYN, stepWaitYN, stepY, invY * (1 if gy1 == 0 else -1), vib)

        # Leitura dos potenciômetros
        abclevel = [stepX, stepY]
        res_check_pots, wait2Zero, cycle = check_pots(pots, abclevel, wait2Zero, cycle)

        # Verifica se há resultado antes de processar
        if res_check_pots is not None:
            log(f'potsgyrotozmk {res_check_pots}', 0)
            tozmk = potsgyrotozmk(*res_check_pots)
            # log(f'send_charPs {tozmk}', 0)
            send_charPs(tozmk)

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
    start(force_calib=True)  # Força nova calibração na inicialização
    vibrar(init_vibrator(), 4)
