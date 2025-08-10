import time
from utils import calibrar_touchpads
from actions import vibrar, send_charPs

def check_sensor(value, thresh_pos, state, name):
    if value < thresh_pos and not state["trigger"]:
        state["trigger"] = True
        print(f"[{name}] Toque detectado! Valor: {value}")
        if state["action"]:
            state["action"](state)  # Acho que você quis executar a ação aqui
    elif value >= thresh_pos and state["trigger"]:
        state["trigger"] = False
    return state

def start_sensors(pots, mpuSensor, pino_vibracao, tsleep, tclear, samples):
    import actions
    actions.pino_vibracao = pino_vibracao

    print("Calibrando touchpads...")
    maxCalibratePots = calibrar_touchpads(pots)
    thresholds = [m - 100 for m in maxCalibratePots]

    sensors = []
    for i, pot in enumerate(pots):
        sensors.append({
            "name": f"pot{i+1}",
            "read": lambda p=pot: p.read(),
            "thresh_pos": thresholds[i],
            "trigger": False,
            "action": lambda s, i=i: send_charPs(f"Pot {i+1}")  # Corrigido para captura correta do i
        })

    vibrar(pino_vibracao, 2)  # Passando o pino corretamente
    print("Sistema iniciado. Toque para testar...")

    while True:
        for sensor in sensors:
            val = sensor["read"]()
            sensor.update(check_sensor(val, sensor["thresh_pos"], sensor, sensor["name"]))
        time.sleep_ms(tsleep)
