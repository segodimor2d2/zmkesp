

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


---

row, col, status

zmkcodes

---
No **Pro Micro nRF52840** (especialmente nas placas no estilo *nice!nano*, Elite-Pi ou clones), a escolha entre **B+** e **RAW** depende de **como** você quer alimentar e carregar a bateria.

---

## 📌 Diferença entre os pinos:

* **B+**

  * Vai direto para a bateria LiPo/Li-ion (normalmente 3,0 V–4,2 V).
  * Passa pelo circuito de carregamento interno (se a placa tiver carregador).
  * Usado para conectar **diretamente** a bateria, respeitando polaridade.
  * **Se a placa tiver carregador integrado** (muitos clones têm um chip TP4056 ou MCP73831), o conector JST e o pino B+ são equivalentes.

* **RAW**

  * Entrada de tensão não regulada para passar pelo regulador interno (normalmente aceita 5 V, alguns aceitam até \~6 V).
  * **Não** é para conectar diretamente bateria LiPo — vai desperdiçar energia e pode causar descarregamento indesejado, pois passa pelo regulador.

---

## 💡 Em resumo:

* Se for **bateria LiPo recarregável** (3,7 V nominal), **use o pino B+** ou o conector JST da placa.
* Se for alimentar com fonte **maior que 5 V** (USB, pack AA, etc.), use **RAW**.

⚠️ Atenção: Inverter polaridade no **B+** pode queimar a placa. Sempre confira com multímetro antes de ligar.

---

Se quiser, eu posso te mandar um **diagrama de ligação** mostrando a bateria no **B+** e o fluxo de energia para o nRF52840 e para o carregador USB. Isso ajuda a evitar erro na fiação.

---

Se você quer alimentar um **ESP32** a partir do seu **Pro Micro nRF52840**, a escolha do pino depende de **qual tensão você quer fornecer** e de **como as placas estão sendo alimentadas**.

---

## 📌 Opções

1. **Se o ESP32 for rodar em 3,3 V** (a maioria das versões “ESP32-WROOM” e “ESP32-S3” cruas):

   * Pegue o **VCC / 3V3** do Pro Micro nRF52840 (às vezes rotulado como `3V` ou `VCC`).
   * Esse pino é **regulado**, então a tensão vai ser estável mesmo que a bateria esteja variando entre 3,0–4,2 V.

2. **Se o ESP32 tiver regulador onboard** (por exemplo, módulos tipo “ESP32 DevKit” com entrada em `5V`/`VIN`):

   * Você pode alimentar pelo **RAW** do Pro Micro (se ele estiver recebendo >3,7 V da bateria ou USB) **ou** pelo **5V** direto se a placa do Pro Micro estiver no USB.
   * Nesse caso o ESP32 regula para 3,3 V internamente.

---

## ⚠️ Atenções importantes

* O **nRF52840 não consegue fornecer muita corrente** — a linha de 3,3 V dele aguenta normalmente uns **300–500 mA** no máximo.
  O ESP32, especialmente com Wi-Fi ativo, pode puxar picos de **>400 mA**, o que pode causar resets se a bateria/regulador não aguentar.
* Idealmente, **ambos devem ser alimentados da mesma fonte** (ex.: mesma bateria LiPo), cada um com seu regulador, ou usando um regulador único dimensionado para a carga total.
* Sempre conecte **terra (GND)** dos dois para evitar problemas de comunicação.

---

💡 Se você me disser **se o ESP32 é módulo cru ou placa DevKit**, eu posso te indicar exatamente **qual pino** usar no Pro Micro para ligar o VCC dele sem risco.
Você quer que eu já faça esse diagrama de ligação?


