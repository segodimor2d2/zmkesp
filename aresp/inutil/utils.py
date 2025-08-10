import time

def media(valores):
    return sum(valores) / len(valores) if valores else 0

def calibrar_touchpads(pots, amostras=40, delay_ms=70):
    buffers = [[] for _ in pots]
    for _ in range(amostras):
        leituras = [p.read() for p in pots]
        for i, leitura in enumerate(leituras):
            buffers[i].append(leitura)
        time.sleep_ms(delay_ms)

    maximos = [max(b) for b in buffers]
    return maximos
