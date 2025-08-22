import time
import config
from hw import init_i2c, init_mpu, init_vibrator, init_pots
from actions import vibrar, send_charPs
from printlogs import log
from dicctozmk import potsgyrotozmk
from calibration import calc_pots_hysteresis
from pots import check_pots, PotsState
from gyro import initial_buffer, average_and_slide, gyro_principal, GyroState


def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()

    # Estado dos potenciômetros
    pots_state = PotsState(len(pots))

    # Calcula thresholds de histerese
    pots_thresh_on, pots_thresh_off = calc_pots_hysteresis(pots, pots_state.num_pots, vib, force_calib)
    print("Thresholds on:", pots_thresh_on)
    print("Thresholds off:", pots_thresh_off)

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    buffer = initial_buffer(buffer, mpu)
    gyro, accl = average_and_slide(buffer, mpu)

    # Estado do giroscópio
    gyro_state = GyroState()

    gy1, gy2 = config.GY1, config.GY2
    vibrar(vib, 2)

    # Loop principal
    num = 0
    while True:
        gyro, accl = average_and_slide(buffer, mpu)

        # Atualiza giroscópio
        gyro_state = gyro_principal(gyro, gy1, gy2, vib, gyro_state)

        # Atualiza potenciômetros
        abclevel = [gyro_state.stepX, gyro_state.stepY]

        res_check_pots, pots_state = check_pots(
            pots, abclevel,
            pots_thresh_on, pots_thresh_off,
            pots_state
        )

        if res_check_pots is not None:
            log(f"potsgyrotozmk {res_check_pots}", 0)
            send_charPs(potsgyrotozmk(*res_check_pots))

        # Reset se parado
        if gyro_state.wait2Zero and gyro_state.cycle < config.CYCLE_RESET_LIMIT:
            gyro_state.cycle += 1
            if gyro_state.cycle == config.CYCLE_RESET_LIMIT:
                gyro_state.stepX = gyro_state.stepY = 0
                vibrar(vib, 2)
                log("[RESET] StepX e StepY resetados", 2)
                gyro_state.wait2Zero = False
                gyro_state.cycle = 0

        # Controle de limpeza de log
        if num % config.TCLEAR == 0:
            num = 0
        num += 1
        time.sleep_ms(config.TSLEEP)


if __name__ == "__main__":
    start(force_calib=False)
    vibrar(init_vibrator(), 4)
