import config
from printlogs import log

def check_pots(pots, abclevel, wait2Zero, cycle, pval, triggerPot, pot_counter, press_thresh, release_thresh):
    local_res_check_pots = None

    for i, pot in enumerate(pots):
        if i >= len(pval):
            log(f"Erro: Índice {i} fora dos limites (max {len(pval)})", 0)
            continue
            
        val = pot.read()
        pval[i] = val
        mapped_i = config.INDEX_MAP_POTS[i]

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= config.DEBOUNCE_COUNT:
                local_res_check_pots = [abclevel, mapped_i, 1, config.THIS_IS]
                triggerPot[i] = True
                pot_counter[i] = 0
                wait2Zero = False
                cycle = 0

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= config.DEBOUNCE_COUNT:
                local_res_check_pots = [abclevel, mapped_i, 0, config.THIS_IS]
                triggerPot[i] = False
                pot_counter[i] = 0
                wait2Zero = True

        else:
            pot_counter[i] = 0

    return local_res_check_pots, wait2Zero, cycle
