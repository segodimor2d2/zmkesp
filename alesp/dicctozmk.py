

# --- Mapas de tradução (lado esquerdo e lado direito) ---

## M=Moto, Y=Yave [M,Y]
## pot [gx, gy] status [M,Y]

MAPL = {
    # abclevel, gx, gy: (row, col)

    # --- Gyro (1,0) [M,T] ---
    (0,  1,  0): (3, 5),  # space
    (1,  1,  0): (0, 1),  # q
    (2,  1,  0): (0, 2),  # w
    (3,  1,  0): (0, 3),  # e
    (4,  1,  0): (0, 4),  # r

    # --- Gyro (0,0) [M,T] ---
    (0,  0,  0): (3, 5),  # space
    (1,  0,  0): (1, 1),  # a
    (2,  0,  0): (1, 2),  # s
    (3,  0,  0): (1, 3),  # d
    (4,  0,  0): (1, 4),  # f

    # --- Gyro (-1,0) [M,T] ---
    (0, -1,  0): (3, 5),  # space
    (1, -1,  0): (2, 1),  # z
    (2, -1,  0): (2, 2),  # x
    (3, -1,  0): (2, 3),  # c
    (4, -1,  0): (2, 4),  # v

    # --- Gyro (1,1) [M,T] ---
    (0,  1,  1): (3, 5),  # space
    (1,  1,  1): (1, 5),  # t
    (4,  1,  1): (0, 0),  # esc

    # --- Gyro (0,1) [M,T] ---
    (0,  0,  1): (3, 5),  # space
    (1,  0,  1): (1, 5),  # g
    (4,  0,  1): (0, 0),  # esc

    # --- Gyro (-1,1) [M,T] ---
    (0, -1,  1): (3, 5),  # space
    (1, -1,  1): (1, 5),  # b
    (4, -1,  1): (0, 0),  # esc
}

MAPR = {
    # --- Gyro (1,1) [M,T] ---
    (0,  1,  1): (3, 6),   # space
    (1,  1,  1): (1, 6),   # y
    (4,  1,  1): (12, 0),  # backspace

    # --- Gyro (0,1) [M,T] ---
    (0,  1,  0): (3, 6),   # space
    (1,  1,  0): (1, 6),   # h
    (4,  1,  0): (12, 0),  # enter

    # --- Gyro (-1,1) [M,T] ---
    (0,  1, -1): (3, 6),   # space
    (1,  1, -1): (1, 6),   # n
    (4,  1, -1): (12, 0),  # ctrl

    # --- Gyro (1,0) [M,T] ---
    (0,  1,  0): (3, 6),   # space
    (1,  1,  0): (1, 7),   # u
    (2,  1,  0): (1, 8),   # i
    (3,  1,  0): (1, 9),   # o
    (4,  1,  0): (1, 10),   # p

    # --- Gyro (0,0) [M,T] ---
    (0,  0,  0): (3, 6),   # space
    (1,  0,  0): (0, 7),   # j
    (2,  0,  0): (0, 8),   # k
    (3,  0,  0): (0, 9),   # l
    (4,  0,  0): (0, 10),   # c

    # --- Gyro (-1,0) [M,T] ---
    (0, -1,  0): (3, 6),   # space
    (1, -1,  0): (1, 7),  # m
    (2, -1,  0): (1, 8),  # ,
    (3, -1,  0): (1, 9),  # .
    (4, -1,  0): (1, 10),  # ;
}

def potsgyrotozmk(abclevel, mapped_i, status, side):
    """
    Traduz (abclevel, gx, gy, status) -> (row, col, status)
    side: 0 = left, 1 = right
    """
    mapping = MAPL if side == 0 else MAPR
    key = (mapped_i, abclevel[0], abclevel[1])
    if key not in mapping:
        return None  # tecla não mapeada
    row, col = mapping[key]
    return row, col, status

