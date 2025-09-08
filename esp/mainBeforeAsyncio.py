import time
import config
from hw import init_i2c, init_mpu, init_mpr121, init_vibrator
from actions import vibrar, send_charPs, tstpot
from printlogs import log
from dicctozmk import potsgyrotozmk
from calibration import calc_pots_hysteresis, calc_accl_hysteresis
from pots import check_pots, tap_pots, tap_pots_test, check_timeout, PotsState
from gyro import initial_buffer, average_and_slide, gyro_principal, accl_principal, GyroState, AcclState

def start(i2c=None, mpu=None, mpr=None, pots=None, vib=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if mpr is None: mpr = init_mpr121(i2c)

    vibrar(vib, 3, 0, ready=True)

    remap_list = config.INDEX_MAP_POTS 
    remap = {i: remap_list[i] for i in range(len(remap_list))}

    # Estado dos potenciômetros
    pots_state = PotsState()

    # Estado do giroscópio
    gyro_state = GyroState()
    accl_state = AcclState()

    # # Se quiser calibrar o acelerômetro:
    # acclthresholds = calc_accl_hysteresis(mpu, vib, ready, force_calib)
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

    last_ativos = set()  # mantém o estado anterior
    last_abclevel = [0, 0]  # mantém o último abclevel
    force_release = False

    # Loop principal
    ready = False
    num = 0
    while True:
        gyro, accl = average_and_slide(buffer, mpu)
        # x[P] Y[L] Z[V]
        # print(f'x{accl[0]},y{accl[1]},z{accl[2]}')

        # Atualiza acelerômetro
        # accl_state = accl_principal(accl, acclthresholds, accl_state)

        # Atualiza giroscópio
        gyro_state = gyro_principal(gyro, gy1, gy2, vib, ready, gyro_state)

        # Atualiza potenciômetros
        abclevel = [gyro_state.stepX, gyro_state.stepY]


        mask = mpr.get_touched_mask()
        num_electrodes = mpr.electrodes
        # conjunto dos ativos
        # ativos = {i for i in range(num_electrodes) if mask & (1 << i)} 
        # 3,2,1,0,4,5,6,8,9,10,11
        # L 0,1,2,3,4,5,6,8,9,10,11
        # R 0,1,2,3,6,5,4,8,9,10,11
        ativos = {remap[i] for i in range(num_electrodes) if mask & (1 << i) and i in remap}

        # --- toggle ready fora do loop de eventos ---
        toggle_trigger = (gyro_state.stepY == 0 and 5 in ativos and 6 in ativos)
        if toggle_trigger and not last_toggle_trigger:
            ready = not ready
            vibrar(vib, 3, 0, ready=True)
        last_toggle_trigger = toggle_trigger

        eventos = []  # lista de eventos a enviar

        # --- detecta mudança de abclevel ---
        if abclevel != last_abclevel:
            force_release = True

        # --- se flag ativada, solta tudo ---
        if force_release:
            for i in last_ativos:
                eventos.append([abclevel, i, 0, config.THIS_IS])
            gyro_state.wait2Zero = True
            last_ativos = set()
            force_release = False

        # --- detectar press ---
        novos = ativos - last_ativos
        for i in novos:
            eventos.append([abclevel, i, 1, config.THIS_IS])
            gyro_state.wait2Zero = False
            gyro_state.cycle = 0

        # --- detectar release ---
        liberados = last_ativos - ativos
        for i in liberados:
            eventos.append([abclevel, i, 0, config.THIS_IS])
            gyro_state.wait2Zero = True

        # --- envia todos os eventos ---
        for ev in eventos:
            # ev [[M, Y], pot, status, R/L]
            print(f'evento {ev}, ready={ready}')

            if ready:
                tozmk = potsgyrotozmk(*ev)
                # log(f'tozmk {tozmk}', 0)
                send_charPs(tozmk)

        # atualiza estado
        last_ativos = ativos
        last_abclevel = abclevel[:]

        """FIM E LIMPEZA"""
        # Reset se parado
        if gyro_state.wait2Zero and gyro_state.cycle < config.CYCLE_RESET_LIMIT:
            gyro_state.cycle += 1
            if gyro_state.cycle == config.CYCLE_RESET_LIMIT:
                gyro_state.stepX = gyro_state.stepY = 0
                vibrar(vib, 2, ready=ready)
                gyro_state.wait2Zero = False
                gyro_state.cycle = 0
        
        # Controle de limpeza de log
        if num % config.TCLEAR == 0:
            num = 0
        num += 1

        time.sleep_ms(config.TSLEEP)


if __name__ == "__main__":
    start(force_calib=False)
    vibrar(init_vibrator(), 4, ready=True)
