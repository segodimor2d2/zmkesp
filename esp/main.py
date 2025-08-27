import time
import config
from hw import init_i2c, init_mpu, init_vibrator, init_pots, test_pots
from actions import vibrar, send_charPs
from printlogs import log
from dicctozmk import potsgyrotozmk
from calibration import calc_pots_hysteresis, calc_accl_hysteresis
from pots import check_pots, tap_pots, tap_pots_test, check_timeout, PotsState
from gyro import initial_buffer, average_and_slide, gyro_principal, accl_principal, GyroState, AcclState


def start(i2c=None, mpu=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if pots is None: pots = init_pots()

    # Estado dos potenciômetros
    pots_state = PotsState(len(pots))

    # Estado do giroscópio
    gyro_state = GyroState()
    accl_state = AcclState()

    # Calcula thresholds de histerese
    pots_thresh_on, pots_thresh_off = calc_pots_hysteresis(
        pots, pots_state.num_pots, vib, force_calib
    )
    print("Thresholds on:", pots_thresh_on)
    print("Thresholds off:", pots_thresh_off)

    # # Se quiser calibrar o acelerômetro:
    # acclthresholds = calc_accl_hysteresis(mpu, vib, force_calib)
    # print("\nThresholds Acelerometro", acclthresholds)

    # print("------------------------------------")
    # raise KeyboardInterrupt("Parando programa!")

    # Prepara buffer do gyro
    buffer = [[] for _ in range(6)]
    buffer = initial_buffer(buffer, mpu)
    gyro, accl = average_and_slide(buffer, mpu)

    gy1, gy2 = config.GY1, config.GY2

    # tap_hold = True
    tap_hold = False

    accl_states = [0, 0, 0] # 0 = neutro, 1 = positivo, -1 = negativo
    stable_count = [0, 0, 0]

    # Loop principal
    vibrar(vib, 2)
    num = 0
    while True:
        gyro, accl = average_and_slide(buffer, mpu)
        # x[P] Y[L] Z[V]
        # print(f'x{accl[0]},y{accl[1]},z{accl[2]}')

        # Atualiza acelerômetro
        # accl_state = accl_principal(accl, acclthresholds, accl_state)

        # Atualiza giroscópio
        gyro_state = gyro_principal(gyro, gy1, gy2, vib, gyro_state)

        # Atualiza potenciômetros
        abclevel = [gyro_state.stepX, gyro_state.stepY]

        res_check_pots, pots_state = check_pots( pots, abclevel,
            pots_thresh_on, pots_thresh_off,
            pots_state
        )

        result = None
        if res_check_pots is not None:
            ## pot [gx, gy] status [M,Y]  M=Moto, Y=Yave [M,Y]
            # res_check_pots [[M, Y], pot, status, R/L]
            # log(f'res_check_pots {res_check_pots}', 0)

            # Processa evento vindo do check_pots
            if tap_hold: result, pots_state = tap_pots(*res_check_pots, pots_state)

            result, pots_state = tap_pots_test(*res_check_pots, pots_state)

            if res_check_pots[0][1] == -2:
                # if res_check_pots[1] == 0 and res_check_pots[2] == 1:
                if res_check_pots[1] == 0:
                    start(force_calib=True)
 
        # Se ainda não fechou ciclo, verifica timeout
        if not result and tap_hold:
            result, pots_state = check_timeout(pots_state)

        # Se um ciclo foi fechado → envia eventos
        if result and result["tap_go"]:
            for event in result["events"]:
                print(f'event {event}')
                # tozmk = potsgyrotozmk(*event)
                # log(f'tozmk {tozmk}', 0)
                # log(f'send_charPs {tozmk}', 0)
                # send_charPs(tozmk)
            print()

        # if tap_hold is False:
        #     # Se ainda não fechou ciclo, verifica timeout
        #     if not result: result, pots_state = check_timeout(pots_state)
        #
        #     # Se um ciclo foi fechado → envia eventos
        #     if result and result["tap_go"]:
        #         for event in result["events"]:
        #             print(f'event {event}')
        #             # tozmk = potsgyrotozmk(*event)
        #             # log(f'tozmk {tozmk}', 0)
        #             # log(f'send_charPs {tozmk}', 0)
        #             # send_charPs(tozmk)
        #         print()


        """FIM E LIMPEZA"""
        # Reset se parado
        if gyro_state.wait2Zero and gyro_state.cycle < config.CYCLE_RESET_LIMIT:
            gyro_state.cycle += 1
            if gyro_state.cycle == config.CYCLE_RESET_LIMIT:
                gyro_state.stepX = gyro_state.stepY = 0
                vibrar(vib, 2)
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
