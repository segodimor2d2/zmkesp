

- terminar a parte da ezquerda
- ajustar os dados certos row/col
- protocolo de envio para nRF52840
- soldas e ajustes novos
- ver a sincornizacao para envio de dados
- pensar no mouse


# ALESP L
mpremote fs ls
mpremote repl
mpremote connect /dev/ttyUSB0 cp alesp/config.py :config.py
mpremote connect /dev/ttyUSB0 cp alesp/main.py :main.py
mpremote connect /dev/ttyUSB0 cp alesp/actions.py :actions.py
mpremote connect /dev/ttyUSB0 cp aresp/dicctozmk.py :dicctozmk.py
mpremote connect /dev/ttyUSB0 cp alesp/hw.py :hw.py
mpremote connect /dev/ttyUSB0 cp alesp/pots.py :pots.py
mpremote connect /dev/ttyUSB0 cp alesp/gyro.py :gyro.py
mpremote connect /dev/ttyUSB0 cp alesp/mpu6050.py :mpu6050.py

# pots
1 0 2 4 3 

(gzar 2) (gz 1) (gzre 0)
(gyar 1) (gy 2) (gyre 3)





# ALESP R
mpremote fs ls
mpremote repl
mpremote connect /dev/ttyUSB0 cp aresp/config.py :config.py
mpremote connect /dev/ttyUSB0 cp aresp/main.py :main.py
mpremote connect /dev/ttyUSB0 cp aresp/actions.py :actions.py
mpremote connect /dev/ttyUSB0 cp aresp/dicctozmk.py :dicctozmk.py
mpremote connect /dev/ttyUSB0 cp aresp/hw.py :hw.py
mpremote connect /dev/ttyUSB0 cp aresp/pots.py :pots.py
mpremote connect /dev/ttyUSB0 cp aresp/gyro.py :gyro.py
mpremote connect /dev/ttyUSB0 cp aresp/mpu6050.py :mpu6050.py

# pots
0 1 2 3 4


GY1, GY2 = 0, 1         # Eixo X primeiro, depois Y
# Eixo x primeiro, depois y
## pot [gx, gy] status [M,T]
1 [0, -1] 1

(gxar 1) (gx 0) (gxre -1)
(gyar 1) (gy 0) (gyre -1)


GY1, GY2 = 1, 0         # Eixo X primeiro, depois Y
# Eixo y primeiro, depois x
## pot [gy, gx] status [T,M]
(gxar 1) (gx 0) (gxre -1)
(gyar 1) (gy 0) (gyre -1)

---



---

mpremote fs ls
mpremote rm nome_do_arquivo.py
mpremote rm hidcodes.py
mpremote rm hardware.py
mpremote rm sensors.py

rshell --port /dev/ttyACM0

ls /pyboard

mpremote fs ls

mpremote repl

mpremote connect /dev/ttyUSB0 cp arquivo_local.py :arquivo_remoto.py

mpremote connect /dev/ttyUSB0 cp main.py :main.py
mpremote connect /dev/ttyUSB0 cp mpu6050.py :mpu6050.py
mpremote connect /dev/ttyUSB0 cp gyro_utils.py :gyro_utils.py

mpremote connect /dev/ttyUSB0 cp pot_utils.py :pot_utils.py
mpremote connect /dev/ttyUSB0 cp input_handler.py :input_handler.py

mpremote connect /dev/ttyUSB0 cp hidcodes.py :hidcodes.py


mpremote connect /dev/ttyUSB0 cp arquivo_local.py :arquivo_remoto.py



Touch
<!-- 0,2,3,4,5,6,7,8 -->
13,12,14,27,33,32,
15,2,4

Lesp
def init_vibrator(pin_no=32):
def init_pots(pins=(33,13,15,04,27)):
27 33

Resp
def init_vibrator(pin_no=33):
def init_pots(pins=(13,12,14,27,4)):




---


## pot [gx, gy] status [M,T]
enviar_evento(row, col, pressionado)

abclevel, [x,y], status em  row, col, status
0 [1,0]  = 3 5 space
1 [1,0]  = 0 1 q
2 [1,0]  = 0 2 w
3 [1,0]  = 0 3 e
4 [1,0]  = 0 4 r
0 [0,0]  = 3 5 space
1 [0,0]  = 1 1 a
2 [0,0]  = 1 2 s
3 [0,0]  = 1 3 d
4 [0,0]  = 1 4 f
0 [-1,0] = 3 5 space
1 [-1,0] = 2 1 z
2 [-1,0] = 2 2 s
3 [-1,0] = 2 3 x
4 [-1,0] = 2 4 c

0 [1,1]  = 3 5 space
1 [1,1]  = 1 5 t
2 [1,1]  = none
3 [1,1]  = none
4 [1,1]  = 0 0 esc
0 [1,0]  = 3 5 space
1 [1,0]  = 1 5 g
2 [1,0]  = none
3 [1,0]  = none
4 [1,0]  = 0 0 esc
0 [1,-1] = 3 5 space
1 [1,-1] = 1 5 v
2 [1,-1] = none
3 [1,-1] = none
4 [1,-1] = 0 0 esc



pot[x,y]   r c
0 [1,1]  = 3 6 space
1 [1,1]  = 1 6 y
2 [1,1]  = none
3 [1,1]  = none
4 [1,1]  = 12 0 backspace

0 [1,0]  = 3 6 space
1 [1,0]  = 1 6 h
2 [1,0]  = none
3 [1,0]  = none
4 [1,0]  = 12 0 enter

0 [1,-1] = 3 6 space
1 [1,-1] = 1 6 n
2 [1,-1] = none
3 [1,-1] = none
4 [1,-1] = 12 0 ctrl

0 [1,0]  = 3 6 space
1 [1,0]  = 8 1 u
2 [1,0]  = 8 2 i
3 [1,0]  = 8 3 o
4 [1,0]  = 8 4 p
0 [0,0]  = 3 6 space
1 [0,0]  = 9 1 j
2 [0,0]  = 9 2 k
3 [0,0]  = 9 3 l
4 [0,0]  = 9 4 c
0 [-1,0] = 3 6 space
1 [-1,0] = 10 1 m
2 [-1,0] = 10 2 ,
3 [-1,0] = 10 3 ,
4 [-1,0] = 10 4 ;

---

numa função de micropython eu tenho os seguintes parâmetros:

abclevel, mapped_i, 1
abclevel, mapped_i, 0

onde abclevel é o pot de 0 a 4
mapped_i é o gyro em x ou y
e 1 e 0 são os estados press e release

abclevel, [x,y], status em  row, col, status

me ajuda a fazer uma função optimizada chamada potsgyrotozmk
para traduzir os parâmetros que irão passar a fila e coluna (row, col)
com o seu status (press=1, release=0) assim:

0,1,0
0,1 0

eu gostaria tirar as [] da entrada e ser for por exempl 0 [1,0] pode ficar como 0,1,0,
eu gostaria de conservar os comentarios para facilitara a leitura,
a função poderia ter como entrada algo assim: 
potsgyrotozmk(0,1,0,0) = 3,5,0

eu preciso de um diccionario para cada lado ezquerdo e direito
tirando o status que o mesmo dos dois lados, os parâmetros que eu quero traduzir são os seguintes:

Lado Esquerdo:

0 [1,0]  = 3 5 # space
1 [1,0]  = 0 1 # q
2 [1,0]  = 0 2 # w
3 [1,0]  = 0 3 # e
4 [1,0]  = 0 4 # r
0 [0,0]  = 3 5 # space
1 [0,0]  = 1 1 # a
2 [0,0]  = 1 2 # s
3 [0,0]  = 1 3 # d
4 [0,0]  = 1 4 # f
0 [-1,0] = 3 5 # space
1 [-1,0] = 2 1 # z
2 [-1,0] = 2 2 # s
3 [-1,0] = 2 3 # x
4 [-1,0] = 2 4 # c
0 [1,1]  = 3 5 # space
1 [1,1]  = 1 5 # t
2 [1,1]  = none
3 [1,1]  = none
4 [1,1]  = 0 0  # esc
0 [1,0]  = 3 5  # space
1 [1,0]  = 1 5  # g
2 [1,0]  = none
3 [1,0]  = none
4 [1,0]  = 0 0  # esc
0 [1,-1] = 3 5  # space
1 [1,-1] = 1 5  # v
2 [1,-1] = none
3 [1,-1] = none
4 [1,-1] = 0 0  # esc


Lado Direito:

0 [1,1]  = 3 6  # space
1 [1,1]  = 1 6  # y
2 [1,1]  = none
3 [1,1]  = none
4 [1,1]  = 12 0 #  backspace
0 [1,0]  = 3 6  # space
1 [1,0]  = 1 6  # h
2 [1,0]  = none
3 [1,0]  = none
4 [1,0]  = 12 0 #  enter
0 [1,-1] = 3 6  # space
1 [1,-1] = 1 6  # n
2 [1,-1] = none
3 [1,-1] = none
4 [1,-1] = 12 0 # ctrl
0 [1,0]  = 3 6  # space
1 [1,0]  = 8 1  # u
2 [1,0]  = 8 2  # i
3 [1,0]  = 8 3  # o
4 [1,0]  = 8 4  # p
0 [0,0]  = 3 6  # space
1 [0,0]  = 9 1  # j
2 [0,0]  = 9 2  # k
3 [0,0]  = 9 3  # l
4 [0,0]  = 9 4  # c
0 [-1,0] = 3 6  # space
1 [-1,0] = 10 1 # m
2 [-1,0] = 10 2 # ,
3 [-1,0] = 10 3 # ,
4 [-1,0] = 10 4 # ;
