import config
from printlogs import log


class PotsState:
    def __init__(self, num_pots: int):
        self.num_pots = num_pots
        self.pval = [0] * num_pots
        self.triggerPot = [False] * num_pots
        self.pot_counter = [0] * num_pots
        self.wait2Zero = False
        self.cycle = 0


def check_pots(pots, abclevel, press_thresh, release_thresh, state: PotsState):
    """
    Verifica os potenciômetros e atualiza o estado.
    Retorna um evento (ou None) + estado atualizado.
    """
    local_res_check_pots = None

    for i, pot in enumerate(pots):
        if i >= state.num_pots:
            log(f"Erro: Índice {i} fora dos limites (max {state.num_pots})", 0)
            continue

        val = pot.read()
        state.pval[i] = val
        mapped_i = config.INDEX_MAP_POTS[i]

        # Pressionado
        if not state.triggerPot[i] and val < press_thresh[i]:
            state.pot_counter[i] += 1
            if state.pot_counter[i] >= config.DEBOUNCE_COUNT:
                local_res_check_pots = [abclevel, mapped_i, 1, config.THIS_IS]
                state.triggerPot[i] = True
                state.pot_counter[i] = 0
                state.wait2Zero = False
                state.cycle = 0

        # Solto
        elif state.triggerPot[i] and val > release_thresh[i]:
            state.pot_counter[i] += 1
            if state.pot_counter[i] >= config.DEBOUNCE_COUNT:
                local_res_check_pots = [abclevel, mapped_i, 0, config.THIS_IS]
                state.triggerPot[i] = False
                state.pot_counter[i] = 0
                state.wait2Zero = True

        else:
            state.pot_counter[i] = 0

    return local_res_check_pots, state
