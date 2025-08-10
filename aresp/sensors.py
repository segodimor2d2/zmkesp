import time
from hardware import pots
from utils import getPots, calcCalibrate, media, vibrar
from actions import action_vibrar, send_charPs

def check_sensor(value, thresh_pos, thresh_neg, state, holdclick):
    step = state["step"]
    tp = state["trigger_pos"]
    tn = state["trigger_neg"]
    swp = state["stepWait_pos"]
    swn = state["stepWait_neg"]
    wait2Zero = state["wait2Zero"]
    cycle = state["cycle"]

    if not tp and not holdclick and value > thresh_pos:
        step += state["dir_pos"]
        if state["action_pos"]:
            state["action_pos"](step)
        tp = True
        wait2Zero = False
        cycle = 0
    elif tp and value <= thresh_pos:
        tp = False
        wait2Zero = True

    if not tn and not holdclick and value < thresh_neg:
        step += state["dir_neg"]
        if state["action_neg"]:
            state["action_neg"](step)
        tn = True
        wait2Zero = False
        cycle = 0
    elif tn and value >= thresh_neg:
        tn = False
        wait2Zero = True

    if tp:
        swp += 1
    else:
        swp = 0
    if swp >= 5:
        step += state["dir_pos"]
        swp = 0
        if state["action_pos"]:
            state["action_pos"](step)

    if tn:
        swn += 1
    else:
        swn = 0
    if swn >= 5:
        step += state["dir_neg"]
        swn = 0
        if state["action_neg"]:
            state["action_neg"](step)

    state.update(step=step,
                 trigger_pos=tp,
                 trigger_neg=tn,
                 stepWait_pos=swp,
                 stepWait_neg=swn,
                 wait2Zero=wait2Zero,
                 cycle=cycle)
    return state

def start(tsleep, tclear, samples, getGyroFunc):
    bufferPot = [[] for _ in range(5)]
    for _ in range(40):
        pval = [pot.read() for pot in pots]
        getPots(bufferPot, pval)
        time.sleep_ms(70)
    maxCalibratePots = calcCalibrate(bufferPot)

    buffer = [[] for _ in range(6)]
    for _ in range(samples - 1):
        getGyroFunc(buffer)
        time.sleep_ms(70)

    poragora = 14000
    thresPercent = 0.1
    threshXP = poragora - (poragora * thresPercent)
    threshXN = -poragora + (poragora * thresPercent)
    threshYP = poragora - (poragora * thresPercent)
    threshYN = -poragora + (poragora * thresPercent)
    threshPot = [-120] * 5

    vibrar(2)

    sensors = [
        {
            "name": "gyroX",
            "read": lambda: media(buffer)[0][0],
            "thresh_pos": threshXP, "thresh_neg": threshXN,
            "dir_pos": 1, "dir_neg": -1,
            "step": 0, "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": action_vibrar,
            "action_neg": action_vibrar
        },
        {
            "name": "gyroY",
            "read": lambda: media(buffer)[0][1],
            "thresh_pos": threshYP, "thresh_neg": threshYN,
            "dir_pos": 1, "dir_neg": -1,
            "step": 0, "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": action_vibrar,
            "action_neg": action_vibrar
        }
    ]

    for i, pot in enumerate(pots):
        sensors.append({
            "name": f"pot{i+1}",
            "read": (lambda p=pot, m=maxCalibratePots[i]: p.read() - m),
            "thresh_pos": threshPot[i],
            "thresh_neg": -9999,
            "dir_pos": 0, "dir_neg": 0,
            "step": 0,
            "trigger_pos": False, "trigger_neg": False,
            "stepWait_pos": 0, "stepWait_neg": 0,
            "wait2Zero": True, "cycle": 0,
            "action_pos": lambda _, lvl=None: send_charPs(lvl) if lvl else None,
            "action_neg": None
        })

    while True:
        stepX = sensors[0]["step"]
        stepY = sensors[1]["step"]

        if -1 <= stepX <= 1 and -2 <= stepY <= 2:
            abclevel = [stepX + 1, 2 - stepY]
        else:
            abclevel = None

        for sensor in sensors:
            val = sensor["read"]()
            sensor.update(check_sensor(
                val, sensor["thresh_pos"], sensor["thresh_neg"],
                sensor, holdclick=False
            ))

        if all(s["wait2Zero"] for s in sensors[:2]):
            for s in sensors[:2]:
                s["cycle"] += 1
            if any(s["cycle"] == 20 for s in sensors[:2]):
                sensors[0]["step"] = sensors[1]["step"] = 0
                vibrar(2)

        time.sleep_ms(tsleep)
