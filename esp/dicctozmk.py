from printlogs import log

# --- Mapas de tradução (lado esquerdo e lado direito) ---

## M=Moto, Y=Yave [M,Y]
## pot [gx, gy] status [M,Y]

MAPL = {
    # abclevel, gx, gy: (row, col)

    # --- Gyro (1,0) [P,M,Y](row, col) ---
    (4,  1,  0): (0, 1),  # q
    (3,  1,  0): (0, 2),  # w
    (2,  1,  0): (0, 3),  # e
    (1,  1,  0): (0, 4),  # r
    (0,  1,  0): (0, 5),  # t

    # --- Gyro (0,0) [P,M,Y](row, col) ---
    (4,  0,  0): (1, 1),  # z
    (3,  0,  0): (1, 2),  # x
    (2,  0,  0): (1, 3),  # c
    (1,  0,  0): (1, 4),  # v
    (0,  0,  0): (1, 5),  # b

    # --- Gyro (-1,0) [P,M,Y](row, col) ---
    (4, -1,  0): (2, 1),  # z
    (3, -1,  0): (2, 2),  # x
    (2, -1,  0): (2, 3),  # c
    (1, -1,  0): (2, 4),  # v
    (0, -1,  0): (2, 5),  # b

    (5,  1,  0): (3, 0),  # mo4
    # (5,  0,  0): (3, 0),  # mo4
    # (5, -1,  0): (3, 0),  # mo4

    # (6,  1,  0): (0, 0),  # esc
    (6,  0,  0): (0, 0),  # esc
    (6, -1,  0): (0, 0),  # esc

    # (7,  1,  0): (3, 1),  # space
    (7,  0,  0): (3, 1),  # space
    (7, -1,  0): (3, 1),  # space

    (8,  1,  0): (3, 2),  # mo2
    # (8,  0,  0): (3, 2),  # mo2
    # (8, -1,  0): (3, 2),  # mo2

    # --- Gyro (1,1) [P,M,Y](row, col) ---
    (4,  0,  1): (0, 0),  # esc
    (3,  0,  1): (1, 0),  # shift
    (2,  0,  1): (2, 0),  # ctrl
    (1,  0,  1): (3, 4),  # bspc
}

MAPR = {
    # --- Gyro (1,0) [P,M,Y] ---
    (0,  1,  0): (0, 6),   # y
    (1,  1,  0): (0, 7),   # u
    (2,  1,  0): (0, 8),   # i
    (3,  1,  0): (0, 9),   # o
    (4,  1,  0): (0, 10),  # p

    # --- Gyro (0,0) [P,M,Y] ---
    (0,  0,  0): (1, 6),   # h
    (1,  0,  0): (1, 7),   # j
    (2,  0,  0): (1, 8),   # k
    (3,  0,  0): (1, 9),   # l
    (4,  0,  0): (1, 10),  # c

    # --- Gyro (-1,0) [P,M,Y](row, col) ---
    (0, -1,  0): (2, 6),  # n
    (1, -1,  0): (2, 7),  # m
    (2, -1,  0): (2, 8),  # ,
    (3, -1,  0): (2, 9),  # .
    (4, -1,  0): (2, 10), # ;

    (5,  1,  0): (3, 5),   # mo1
    # (5, -1,  0): (3, 5),   # mo1
    # (5,  0,  0): (3, 5),   # mo1

    (6,  1,  0): (3, 4),   # bspc
    # (6,  0,  0): (3, 4),   # bspc
    (6, -1,  0): (3, 4),   # bspc

    # (7,  1,  0): (3, 6),   # enter
    (7, -1,  0): (3, 6),   # enter
    (7,  0,  0): (3, 6),   # enter

    (8,  1,  0): (3, 7),   # mo3
    # (8, -1,  0): (3, 7),   # mo3
    # (8,  0,  0): (3, 7),   # mo3

    # --- Gyro (1,1) [P,M,Y](row, col) ---
    (4,  0,  1): (0, 0),  # esc
    (3,  0,  1): (1, 0),  # shift
    (2,  0,  1): (2, 0),  # ctrl
    (1,  0,  1): (3, 4),  # bspc

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

