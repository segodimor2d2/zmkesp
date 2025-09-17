import time
import config
from hw import init_i2c, init_mpu, init_mpr121, init_vibrator, init_led
from actions import vibrar, send_charPs, tsttap, piscaled
from printlogs import log
from dicctozmk import potsgyrotozmk
from calibration import calc_pots_hysteresis, calc_accl_hysteresis
from pots import check_pots, tap_pots, tap_pots_test, check_timeout, PotsState
from gyro import initial_buffer, average_and_slide, gyro_principal, accl_principal, GyroState, AcclState


def post_data(url, data):
    import urequests
    try:
        r = urequests.post(url, json=data)  # envia como JSON
        print("Status:", r.status_code)
        print("Resposta:", r.text)
        r.close()
    except Exception as e:
        print("Erro no POST:", e)

def restart(vib, segundos=3):
    vibrar(vib, 1, 2, ready=True)

    import machine
    machine.reset()

def liberar_repl(vib, led, segundos=3):
    vibrar(vib, 1, 2, ready=True)

    import webrepl
    import network

    print("\nBoot...")
    station = network.WLAN(network.STA_IF)
    station.active(True)

    red = config.REDES
    indexid = 0
    for i in red:
        print(f'Connecting to WiFi {i[0]}...')

        try:
            station.disconnect()
            time.sleep_ms(200)
        except:
            pass

        station.connect(i[0], i[1])

        # time.sleep_ms(10000)

        # espera no máximo 5 segundos
        for _ in range(50):
            if station.isconnected():
                break
            time.sleep_ms(100)  # 0.1s
            piscaled(led, 50, 1)

        if station.isconnected():
            print(f'\nConnected to {i[0]} with success.')
            indexid = i
            print(f'Config: {station.ifconfig()}')
            time.sleep_ms(1000)
            piscaled(led, 100, 6)
            break

        else:
            print(f'Falha ao conectar em {i[0]}')
        
    if not station.isconnected():
        print('xxxxxx Error WiFi Connected xxxxxx')
        station.active(False)

    try:
        if webrepl.is_running():
            print("WebREPL já ativo")
            vibrar(vib, 1, 2, ready=True)
        else:
            webrepl.start()

    except AttributeError:
        # fallback se a função não existir
        if getattr(webrepl, "_webrepl", None):
            print("WebREPL já rodando")
        else:
            webrepl.start()

    if station.isconnected():
        # url = "http://192.168.31.127:5050"
        # url = "http://192.168.31.13:5050"
        print("indexid:", indexid)
        url = indexid[2]
        post_data(url,f'config: {station.ifconfig()}')
        piscaled(led, 100, 6)

    print("\n*****************************")

    # print(f"Liberando REPL por {segundos}s...")
    # inicio = time.time()
    # while time.time() - inicio < segundos:
    #     vibrar(vib, 1, 1, ready=True)
    #     time.sleep(1)
    # print("Loop retomado.")

def toggle_ready(ready, vib):
    ready = not ready
    vibrar(vib, 3, 0, ready=True)
    return ready


# --- define triggers fora do start ---
def process_triggers(ativos, gyro_state, triggers, ready, vib):
    for trig in triggers:
        current_state = all(b in ativos for b in trig["buttons"]) and trig["condition"](gyro_state)
        if current_state and not trig["last_state"]:
            # executa a ação, atualizando ready se necessário
            if trig.get("returns_ready", False):
                ready = trig["action"](ready, vib)
            else:
                trig["action"]()
        trig["last_state"] = current_state
    return ready


def start(i2c=None, mpu=None, mpr=None, pots=None, vib=None, led=None, force_calib=False):
    # Inicializa hardware se não passado
    if i2c is None: i2c = init_i2c()
    if mpu is None: mpu = init_mpu(i2c)
    if vib is None: vib = init_vibrator()
    if mpr is None: mpr = init_mpr121(i2c)
    if led is None: led = init_led(2)

    vibrar(vib, 3, 0, ready=True)
    piscaled(led, 100, 2)

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

    # --- triggers ---
    triggers = [
        {
            "buttons": {7, 8},
            "condition": lambda gs: gs.stepY == 0,
            "action": toggle_ready,
            "last_state": False,
            "returns_ready": True  # indica que a função retorna ready
        },
        {
            "buttons": {4, 6, 8},
            "condition": lambda gs: True,
            # "condition": lambda gs: gs.stepY == 3,
            "action": lambda: liberar_repl(vib, led, segundos=20),
            "last_state": False,
            "returns_ready": False
        },
        {
            "buttons": {4, 5, 8},
            "condition": lambda gs: True,
            # "condition": lambda gs: gs.stepY == 3,
            "action": lambda: restart(vib, segundos=20),
            "last_state": False,
            "returns_ready": False
        }
    ]

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
        ativos = {remap[i] for i in range(num_electrodes) if mask & (1 << i) and i in remap}
        # print(f'ativos: {ativos}')

        # --- processa triggers ---
        ready = process_triggers(ativos, gyro_state, triggers, ready, vib)

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
                log(f'tozmk {tozmk}', 0)
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
    vibrar(init_vibrator(), 4, ready=True)
    liberar_repl(init_vibrator(), init_led(2), 3)  # <-- webrepl ativado
    start(force_calib=False)

