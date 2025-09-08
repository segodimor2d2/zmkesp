from printlogs import log

# --- Mapas de tradução (lado esquerdo e lado direito) ---

## M=Moto, Y=Yave [M,Y]
## pot [gx, gy] status [M,Y]

MAPL = {
    # abclevel, gx, gy: (row, col)

    # --- Gyro (1,0) [P,M,T] ---
    (0,  1,  0): (0, 4),  # r
    (1,  1,  0): (0, 3),  # e
    (2,  1,  0): (0, 2),  # w
    (3,  1,  0): (0, 1),  # q
    (4,  1,  0): (3, 2),  # space

    # --- Gyro (0,0) [P,M,T] ---
    (0,  0,  0): (1, 4),  # f
    (1,  0,  0): (1, 3),  # d
    (2,  0,  0): (1, 2),  # s
    (3,  0,  0): (1, 1),  # a
    (4,  0,  0): (3, 2),  # space

    # --- Gyro (0,0) [P,M,T] ---
    (5, 0,  0): (3, 4),  # mod1

    # --- Gyro (-1,0) [P,M,T] ---
    (0, -1,  0): (2, 4),  # v
    (1, -1,  0): (2, 3),  # c
    (2, -1,  0): (2, 2),  # x
    (3, -1,  0): (2, 1),  # z
    (4, -1,  0): (3, 2),  # space

    # --- Gyro (1,1) [P,M,T] ---
    (4,  1,  1): (3, 2),  # space
    (0,  1,  1): (0, 5),  # t
    (3,  1,  1): (0, 0),  # esc

    # --- Gyro (0,1) [P,M,T] ---
    (4,  0,  1): (3, 2),  # space
    (0,  0,  1): (1, 5),  # g
    (1,  0,  1): (1, 0),  # ctrl
    (2,  0,  1): (2, 0),  # shift
    (3,  0,  1): (0, 0),  # esc

    # --- Gyro (-1,1) [P,M,T] ---
    (4, -1,  1): (3, 2),  # space
    (0, -1,  1): (2, 5),  # b
    (3, -1,  1): (0, 0),  # esc


}

MAPR = {
    # --- Gyro (1,0) [P,M,T] ---
    (0,  1,  0): (0, 7),   # u
    (1,  1,  0): (0, 8),   # i
    (2,  1,  0): (0, 9),   # o
    (3,  1,  0): (0, 10),  # p
    (4,  1,  0): (3, 3),   # enter
    # --- Gyro (1,1) [P,M,T] ---
    (4,  1,  1): (3, 3),   # enter
    (0,  1,  1): (0, 6),   # y
    (3,  1,  1): (0, 11),  # backspace

    # --- Gyro (0,0) [P,M,T] ---
    (0,  0,  0): (1, 7),   # j
    (1,  0,  0): (1, 8),   # k
    (2,  0,  0): (1, 9),   # l
    (3,  0,  0): (1, 10),  # c
    (4,  0,  0): (3, 3),   # enter

    # --- Gyro (0,0) [P,M,T] ---
    (5, 0,  0): (3, 1),  # mod2

    # --- Gyro (-1,0) [P,M,T] ---
    (0, -1,  0): (2, 7),  # m
    (1, -1,  0): (2, 8),  # ,
    (2, -1,  0): (2, 9),  # .
    (3, -1,  0): (2, 10), # ;
    (4, -1,  0): (3, 3),   # enter

    # --- Gyro (1,1) [P,M,T] ---
    (4,  1,  1): (3, 3),   # enter
    (0,  1,  1): (0, 6),   # y
    (3,  1,  1): (0, 11),  # backspace

    # --- Gyro (0,1) [P,M,T] ---
    (4,  0,  1): (3, 3),   # enter
    (0,  0,  1): (1, 6),   # h
    (1,  0,  1): (1, 0),  # ctrl
    (2,  0,  1): (2, 0),  # shift
    (3,  0,  1): (0, 11),  # backspace

    # --- Gyro (-1,1) [P,M,T] ---
    (4,  -1, 1): (3, 3),   # enter
    (0,  -1, 1): (2, 6),   # n
    (3,  -1, 1): (0, 11),  # backspace

}

def potsgyrotozmk(abclevel, mapped_i, status, side):
    """
    Traduz (abclevel, gx, gy, status) -> (row, col, status)
    side: 0 = left, 1 = right
    """
    log(f'{mapped_i}, {abclevel}, {status}, {side}', 4)
    mapping = MAPL if side == 0 else MAPR
    key = (mapped_i, abclevel[0], abclevel[1])
    if key not in mapping:
        return None  # tecla não mapeada
    row, col = mapping[key]
    return row, col, status

