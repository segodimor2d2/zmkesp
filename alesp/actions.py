import time

def send_charPs(abclevel,i,state):
    print(i,abclevel,state)

def vibrar(pino_vibracao, n_pulsos, step=None):
    if pino_vibracao is None:
        print("vibrador não inicializado")
        return
    for _ in range(n_pulsos):
        try:
            pino_vibracao.on()
        except Exception:
            # alguns firmwares usam value(1)/value(0)
            try: pino_vibracao.value(1)
            except: pass
        if step == 0:
            time.sleep_ms(200)
        else:
            time.sleep_ms(101)
        try:
            pino_vibracao.off()
        except Exception:
            try: pino_vibracao.value(0)
            except: pass
        time.sleep_ms(70)

