from printlogs import log

# --- Mapas de tradução (lado esquerdo e lado direito) ---

## M=Moto, Y=Yave [M,Y]
## pot [gx, gy] status [M,Y]

MAPL = {
    # abclevel, gx, gy: (row, col)

    # --- Gyro (1,0) [P,Y,M](row, col) ---
    (4,  1,  0): (0, 1),  # q
    (3,  1,  0): (0, 2),  # w
    (2,  1,  0): (0, 3),  # e
    (1,  1,  0): (0, 4),  # r
    (0,  1,  0): (0, 5),  # t

    # --- Gyro (0,0) [P,Y,M](row, col) ---
    (4,  0,  0): (1, 1),  # z
    (3,  0,  0): (1, 2),  # x
    (2,  0,  0): (1, 3),  # c
    (1,  0,  0): (1, 4),  # v
    (0,  0,  0): (1, 5),  # b

    # --- Gyro (-1,0) [P,Y,M](row, col) ---
    (4, -1,  0): (2, 1),  # z
    (3, -1,  0): (2, 2),  # x
    (2, -1,  0): (2, 3),  # c
    (1, -1,  0): (2, 4),  # v
    (0, -1,  0): (2, 5),  # b

    # -------------------------------------
    # --- M [P,Y,M] (row, col) ---
    (0,  0,  -1): (3, 10),  # M1 minus 
    (1,  0,  -1): (4, 8),  # M1 mkp LCLK 
    (2,  0,  -1): (4, 9),  # M1 mkp RCLK
    (3,  0,  -1): (4, 10), # M1 mkp MCLK 
    (4,  0,  -1): (3, 5),  # M1 del

    # --- M [P,Y,M] (row, col) ---
    #(0,  0, 1): (3, 6),  # M1 
    # (1,  0, -1): (3, 3),  # M1 mo4
    (2,  0, 1): (3, 2),  # M1 mo3
    (3,  0, 1): (3, 1),  # M1 mo2
    (4,  0, 1): (3, 0),  # M1 mo1

    # ----------- THUMB ------------------
    # --- M [P,Y,M] (row, col) ---

    # (x,  0, 1): (x, x),  # SISTEMA

    # (x,  0, 0): (x, x),  # NORMAL

    # (5,  0, -1): (3, 6),  #
    # (6,  0, -1): (1, 0),  #
    # (7,  0, -1): (3, 4),  #
    # (8,  0, -1): (2, 0),  #

    # --- Y [P,Y,M] (row, col) ---

    (5,  -1,  0): (4, 0),  # Y1 esc
    #(6, -1,  0): (0, 0),  #
    (7,  -1,  0): (4, 3), # Y1 alt
    #(8, -1,  0): (0, 0),  #

    (5,  0,  0): (3, 8),  # Y0 bspc
    #(6,  0,  0): (3, 6),  # Y0 bspc
    (7,  0,  0): (3, 4),  # Y1 space
    #(8,  0,  0): (0, 0),  # 

    (5,  1,  0): (4, 2),  # Y1 ctrl
    #(6,  1,  0): (1, 0),  #
    (7,  1,  0): (4, 1),  # M1 shift
    #(8,  1,  0): (1, 0),  #

    # -------------------------------------

}

MAPR = {

    # --- Gyro (1,0) [P,Y,M](row, col) ---
    (0,  1,  0): (0, 6),   # y
    (1,  1,  0): (0, 7),   # u
    (2,  1,  0): (0, 8),   # i
    (3,  1,  0): (0, 9),   # o
    (4,  1,  0): (0, 10),  # p

    # --- Gyro (0,0) [P,Y,M](row, col) ---
    (0,  0,  0): (1, 6),   # h
    (1,  0,  0): (1, 7),   # j
    (2,  0,  0): (1, 8),   # k
    (3,  0,  0): (1, 9),   # l
    (4,  0,  0): (1, 10),  # c

    # --- Gyro (-1,0) [P,Y,M](row, col) ---
    (0, -1,  0): (2, 6),  # n
    (1, -1,  0): (2, 7),  # m
    (2, -1,  0): (2, 8),  # ,
    (3, -1,  0): (2, 9),  # .
    (4, -1,  0): (2, 10), # ;

    # -------------------------------------
    # --- M [P,Y,M] (row, col) ---
    (0,  0,  -1): (4, 4),  # M1 left
    (1,  0,  -1): (4, 5),  # M1 down
    (2,  0,  -1): (4, 6),  # M1 up
    (3,  0,  -1): (4, 7),  # M1 rigt
    (4,  0,  -1): (3, 6),  # M1 tab

    # --- M [P,Y,M] (row, col) ---
    #(0,  0, 1): (3, 6),  # M1 
    # (1,  0, -1): (3, 3),  # M1 mo4
    (2,  0, 1): (3, 2),  # M1 mo3
    (3,  0, 1): (3, 1),  # M1 mo2
    (4,  0, 1): (3, 0),  # M1 mo1

    # ----------- THUMB ------------------
    # --- M [P,Y,M] (row, col) ---

    # (x,  0, 1): (x, x),  # SISTEMA

    # (x,  0, 0): (x, x),  # NORMAL

    # (5,  0, -1): (3, 6),  #
    # (6,  0, -1): (4, 5),  #
    # (7,  0, -1): (4, 6),  #
    # (8,  0, -1): (4, 6),  #  

    # --- Y [P,Y,M] (row, col) ---

    (5,  -1,  0): (4, 0),  # Y1 esc
    #(6, -1,  0): (0, 0),  #
    (7,  -1,  0): (4, 3), # Y1 alt
    #(8, -1,  0): (0, 0),  #

    (5,  0,  0): (3, 8),  # Y0 bspc
    #(6,  0,  0): (3, 6),  # Y0 bspc
    (7,  0,  0): (3, 3),  # Y0 enter
    #(8,  0,  0): (0, 0),  # 

    (5,  1,  0): (4, 2),  # Y1 ctrl
    #(6,  1,  0): (2, 0),  #
    (7,  1,  0): (4, 1),  # M1 shift
    #(8,  1,  0): (0, 0),  #

    # -------------------------------------
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

# 3 0  &mo 1 
# 3 1  &mo 2 
# 3 2  &mo 3
# 3 3  &kp ENTER 
# 3 4  &kp SPACE 
# 3 5  &kp DELETE
# 3 6  &kp TAB 
# 3 7  &kp KP_DIVIDE 
# 3 8  &kp BSPC 
# 3 9  &kp TAB  
# 3 10 &kp MINUS 
# 3 11 &kp LS(FSLH)
#
# 4 0  kp ESC 
# 4 1  kp LSHFT 
# 4 2  kp LCTRL 
# 4 3  kp LALT
# 4 4  kp LEFT_ARROW 
# 4 5  kp DOWN 
# 4 6  kp UP 
# 4 7  kp RIGHT 
# 4 8  mkp LCLK 
# 4 9  mkp RCLK 
# 4 10 mkp MCLK  
# 4 11 kp GRAVE
