import time
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

        self.tap_event = []          # histórico bruto de eventos (inclui abclevel)
        self.active_buttons = set()  # botões atualmente pressionados

def check_pots(pots, abclevel, current_mask, last_mask, state: PotsState):

    """
    Retorna uma lista de eventos desde a última leitura.
    Cada evento é uma tupla: (electrode, "press") ou (electrode, "release")


    current_mask = get_touched_mask()
    changed = current_mask ^ last_mask  # bits que mudaram

    for i in range(electrodes):
        if changed & (1 << i):  # esse eletrodo mudou
            if current_mask & (1 << i):
                local_res_check_pots = [abclevel, i, 1, config.THIS_IS]
                state.wait2Zero = False
                state.cycle = 0
            else:
                local_res_check_pots = [abclevel, i, 0, config.THIS_IS]
                state.wait2Zero = True

    last_mask = current_mask

    # res_check_pots [[M, Y], pot, status, R/L]
    return local_res_check_pots, state

    """


    """
    Verifica os potenciômetros e atualiza o estado.
    Retorna um evento (ou None) + estado atualizado.
    """
    local_res_check_pots = None

    for i, pot in enumerate(pots):
        if i >= state.num_pots:
            log(f"Erro: Índice {i} fora dos limites (max {state.num_pots})", 0)
            continue
        try:
            val = pot.read()
        except Exception as e:
            log(f"Erro ao ler TouchPad no índice {i} pino {config.PINOS[i]} (pot {pot}): {e}", 0)
            continue

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
            local_res_check_pots = [abclevel, mapped_i, 0, config.THIS_IS]
            state.triggerPot[i] = False
            state.pot_counter[i] = 0
            state.wait2Zero = True

        else:
            state.pot_counter[i] = 0

    # res_check_pots [[M, Y], pot, status, R/L]
    return local_res_check_pots, state

def tap_pots_test(abclevel, mapped_i, status, side, state: PotsState):
    """
    Versão de teste sem timeout, só para debug.
    """
    event = [abclevel, mapped_i, status, side]
    state.tap_event.append(event)

    if status == 1:  # pressionado
        state.active_buttons.add(mapped_i)

    elif status == 0:  # solto
        state.active_buttons.discard(mapped_i)
        if not state.active_buttons:
            result = {"tap_go": True, "events": state.tap_event[:]}
            state.tap_event.clear()
            return result, state

    return None, state

def tap_pots(abclevel, mapped_i, status, side, state: PotsState):
    """
    Processa evento de pressionar/soltar e organiza ciclos.
    Ignora release que não teve press.
    Fecha ciclo quando todos os botões ativos já foram liberados.
    """
    now = time.ticks_ms()

    if status == 1:  # press
        state.active_buttons.add(mapped_i)
        state.tap_event.append([abclevel, mapped_i, status, side, now])

    elif status == 0:  # release
        # só processa release se o botão estava ativo
        if mapped_i in state.active_buttons:
            state.tap_event.append([abclevel, mapped_i, status, side, now])
            state.active_buttons.remove(mapped_i)

        # se não sobra nenhum botão ativo → ciclo fechado
        if not state.active_buttons:
            result = {"tap_go": True, "events": state.tap_event}
            state.tap_event = []
            return result, state

    return None, state


def check_timeout(state: PotsState, timeout=1000):
    """
    Força fechamento do ciclo se passar muito tempo sem release.
    Cria release apenas para botões que realmente estavam ativos.
    """
    if not state.active_buttons:
        return None, state

    now = time.ticks_ms()
    oldest = state.tap_event[0][4]
    if time.ticks_diff(now, oldest) > timeout:
        # adiciona release apenas para botões que estavam ativos
        for btn in list(state.active_buttons):
            state.tap_event.append([[0, 0], btn, 0, 1, now])  # release forçado
        state.active_buttons.clear()

        result = {"tap_go": True, "events": state.tap_event}
        state.tap_event = []
        return result, state

    return None, state
