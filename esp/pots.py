def add_pot_samples(bufferPot, pval):
    """bufferPot: list de listas; pval: lista com leituras atuais"""
    for i, v in enumerate(pval):
        bufferPot[i].append(v)
    return bufferPot

def calc_calibrate(bufferPot):
    """Retorna lista com max por pot (ou 0 se vazio)"""
    maxCalc = []
    for potList in bufferPot:
        maxCalc.append(max(potList) if potList else 0)
    return maxCalc
