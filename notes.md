

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





---

eu estou rodando ZMK no nRF52840 com dois micros com um teclado split um central e um peripheral
cada um esta recebendo dados via UART de um ESP32
agora eu posso acionar eventos com os switches do nRF52840 ou dados via Uart dede o ESP32.

ao testar com os switches do nRF52840 o peripheral envia tudo certo para o central
mas quando eu tento enviar via UART e o peripheral, o central envia as letras corretas
mas ficam em press e não libera o release

eu estou usando checksum para validar os dados na comunicação UART
e estou enviando um byte inicial assim:

0xAA
checksum = event_type ^ row ^ col

exemplo:

Pronto para enviar eventos UART com checksum.
b'\xaa\x01\x02\x01\x02'
b'\xaa\x00\x02\x01\x03'
b'\xaa\x01\x01\x01\x01'
b'\xaa\x00\x01\x01\x00'
b'\xaa\x01\x00\x01\x00'
b'\xaa\x00\x00\x01\x01'

meu problema é que o switch fica em press e acontece somente do lado do peripheral mas não do lado central, se
eu deligar o o peripheral o centrar continua enviando como se estivece precionando o switch
mas se eu testar o press e o release do lado central via UART funciona tudo certo






me ajude achar o meu problema:

meu problema é que ao enviar via uart diferentes colunas, parece que o uart_switch_simulate sempre envia a coluna 0
porque eu consigo sim mudar de fila ma eu não estou conseguindo mudar de coluna porque sempre envia a coluna 0

checksum = event_type ^ row ^ col
packet = bytes([0xAA, event_type, row, col, checksum])


0xAA
checksum


Pronto para enviar eventos UART com checksum.
b'\xaa\x01\x02\x01\x02'
b'\xaa\x00\x02\x01\x03'
b'\xaa\x01\x01\x01\x01'
b'\xaa\x00\x01\x01\x00'
b'\xaa\x01\x00\x01\x00'
b'\xaa\x00\x00\x01\x01'




Perda de pacotes no UART

Se o peripheral perde o pacote do release, o central nunca vai receber.

Isso pode acontecer se o seu loop de leitura não esvaziar o buffer rápido o suficiente ou se o UART estiver sem checagem de frame completo.



# testes
inverter os nRF52840 (vai acontecer o mesmo)
o checagem esta atrapalhando
loop de leitura não esvaziar o buffer rápido o suficiente



estou com um problema no meu programa, os pinos touch quando tem eu tenho me dedo muito próximo mas sem encostar totalmente do pino,
ele começa a mandar ativado e desativado de um jeito intermitente,
eu gostaria ver sugestões de como mudar isso.

aqui está o código que eu tenho:



---


O que está acontecendo com seus pinos touch é um comportamento normal — o sensor capacitivo detecta variações de campo elétrico e, quando o dedo fica muito próximo, ele entra numa “zona cinza” onde o valor medido oscila acima e abaixo do threshold, causando esse liga/desliga intermitente.

Isso é típico quando não há **histerese** nem **filtro** no código.
Podemos melhorar de algumas formas:

---

### 1. Adicionar **histerese** nos thresholds

Em vez de usar o mesmo valor para “pressionar” e “soltar”, você define dois valores:

```python
PRESS_THRESH = -120   # Pressiona quando abaixo disso
RELEASE_THRESH = -100 # Solta quando acima disso
```

No seu `check_pots()` ficaria algo assim:

```python
if not triggerPot[i] and val < PRESS_THRESH[i]:
    # Pressiona
elif triggerPot[i] and val > RELEASE_THRESH[i]:
    # Solta
```

Assim, pequenas variações na leitura não vão alternar o estado.

---

### 2. Fazer **debounce por tempo**

Mesmo com histerese, ainda pode haver ruído rápido. Então podemos exigir que a leitura fique consistente por alguns ciclos antes de mudar o estado:

```python
# Inicialização
pot_counter = [0] * 5
pot_confirm = 3  # precisa manter 3 leituras estáveis

# No loop:
if not triggerPot[i] and val < PRESS_THRESH[i]:
    pot_counter[i] += 1
    if pot_counter[i] >= pot_confirm:
        triggerPot[i] = True
        pot_counter[i] = 0
elif triggerPot[i] and val > RELEASE_THRESH[i]:
    pot_counter[i] += 1
    if pot_counter[i] >= pot_confirm:
        triggerPot[i] = False
        pot_counter[i] = 0
else:
    pot_counter[i] = 0
```

---

### 3. Aplicar **filtro de média móvel**

Antes de avaliar o valor do sensor, passar as leituras por uma média móvel para suavizar flutuações rápidas:

```python
window_size = 5
history = [[0]*window_size for _ in pots]

for i, pot in enumerate(pots):
    history[i].append(pot.read())
    history[i].pop(0)
    pval[i] = sum(history[i]) / window_size
```

---

💡 **Sugestão para o seu caso:**
Eu usaria **as 3 técnicas juntas**: filtro + histerese + debounce.
Isso vai praticamente eliminar o “flicker” quando o dedo está no limiar de ativação.

---

Se quiser, posso já modificar sua função `check_pots()` para aplicar **histerese e debounce** diretamente no seu código atual, mantendo a compatibilidade com o restante.
Assim, você só ajustaria os thresholds no `config.py`.

















---

Beleza — vou te passar um exemplo que combina **calibração individual**, **histerese** e **debounce** usando a sua função `calc_calibrate()` como ponto de partida.
Assim, cada canal vai ter seus próprios thresholds, e o código vai filtrar os toques “instáveis”.

---

## 1️⃣ Calibração (`calc_calibrate`)

```python
# Quantas amostras para calibrar
CALIB_SAMPLES = 100  

# Quanto abaixo do baseline considera toque
PRESS_OFFSET = 50     
RELEASE_OFFSET = 30   # solta quando volta acima disso

def calc_calibrate():
    global baseline, press_thresh, release_thresh, pot_counter, triggerPot

    num_pots = len(pots)  # 'pots' = lista de objetos de leitura touch
    baseline = [0] * num_pots
    press_thresh = [0] * num_pots
    release_thresh = [0] * num_pots
    pot_counter = [0] * num_pots
    triggerPot = [False] * num_pots

    print("Calibrando... não toque nos sensores.")
    for i in range(num_pots):
        soma = 0
        for _ in range(CALIB_SAMPLES):
            soma += pots[i].read()
        baseline[i] = soma / CALIB_SAMPLES
        press_thresh[i] = baseline[i] - PRESS_OFFSET
        release_thresh[i] = baseline[i] - RELEASE_OFFSET

    print("Baseline:", baseline)
    print("Press thresholds:", press_thresh)
    print("Release thresholds:", release_thresh)
```

---

## 2️⃣ Leitura e detecção (`check_pots`)

```python
# Quantas leituras consecutivas precisa para confirmar
DEBOUNCE_COUNT = 3

def check_pots():
    for i in range(len(pots)):
        val = pots[i].read()

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                triggerPot[i] = True
                pot_counter[i] = 0
                pot_hit(i)  # sua função para evento de toque

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                triggerPot[i] = False
                pot_counter[i] = 0
                pot_release(i)  # sua função para evento de soltar

        else:
            # leitura não consistente, zera contador
            pot_counter[i] = 0
```

---

## 3️⃣ Como funciona

* **`calc_calibrate()`**

  * Mede a média de cada canal separadamente.
  * Calcula thresholds individuais (`press_thresh[i]` e `release_thresh[i]`).
* **`check_pots()`**

  * Aplica histerese (press < press\_thresh, release > release\_thresh).
  * Usa debounce por número de leituras estáveis (`DEBOUNCE_COUNT`).

Isso vai:

* Eliminar flicker no limiar de toque.
* Compensar diferença de sensibilidade entre canais.
* Ser mais estável em ambientes ruidosos.

---

Posso já adaptar isso direto para o **seu** código original mantendo nomes e estruturas que você usa hoje na Maxima, para encaixar sem quebrar nada.
Quer que eu faça essa integração já pronta?










---


Então vamos integrar direto no seu fluxo da Maxima, mantendo os nomes que você já usa.
Vou assumir que:

* Você já tem a lista `pots` com seus objetos de leitura touch.
* `triggerPot` e `pval` já existem no seu código.
* `calc_calibrate()` é chamado na inicialização.
* `check_pots()` é chamado no loop principal.

---

## **Integração sugerida**

```python
# ===== CONFIGURAÇÃO =====
CALIB_SAMPLES   = 100   # Amostras para calibrar cada canal
PRESS_OFFSET    = 50    # Diferença do baseline para considerar pressionado
RELEASE_OFFSET  = 30    # Diferença para considerar liberado
DEBOUNCE_COUNT  = 3     # Leituras consecutivas para confirmar toque

# ===== VARIÁVEIS GLOBAIS =====
baseline        = []
press_thresh    = []
release_thresh  = []
pot_counter     = []
triggerPot      = []
pval            = []

# ===== CALIBRAÇÃO =====
def calc_calibrate():
    global baseline, press_thresh, release_thresh, pot_counter, triggerPot, pval

    num_pots = len(pots)
    baseline        = [0] * num_pots
    press_thresh    = [0] * num_pots
    release_thresh  = [0] * num_pots
    pot_counter     = [0] * num_pots
    triggerPot      = [False] * num_pots
    pval            = [0] * num_pots

    print("Calibrando... não toque nos sensores.")
    for i in range(num_pots):
        soma = 0
        for _ in range(CALIB_SAMPLES):
            soma += pots[i].read()
        baseline[i]       = soma / CALIB_SAMPLES
        press_thresh[i]   = baseline[i] - PRESS_OFFSET
        release_thresh[i] = baseline[i] - RELEASE_OFFSET

    print("Baseline:       ", baseline)
    print("Press thresh:   ", press_thresh)
    print("Release thresh: ", release_thresh)

# ===== LEITURA E DETECÇÃO =====
def check_pots():
    for i in range(len(pots)):
        val = pots[i].read()
        pval[i] = val  # mantém valor atual para uso externo

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                triggerPot[i] = True
                pot_counter[i] = 0
                pot_hit(i)  # chama função de toque

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                triggerPot[i] = False
                pot_counter[i] = 0
                pot_release(i)  # chama função de soltar

        else:
            pot_counter[i] = 0
```

---

## **Onde encaixar no seu código**

1. Substituir a função antiga `calc_calibrate()` por essa versão.
2. Substituir a função antiga `check_pots()` por essa versão.
3. Garantir que `calc_calibrate()` seja chamado **logo após iniciar o sistema**, antes do loop principal.
4. No loop principal, manter `check_pots()` sendo chamado a cada ciclo.

---

💡 Com isso, você vai ter:

* **Calibração individual por canal** (corrige diferenças de sensibilidade).
* **Histerese automática** (não pisca no limiar).
* **Debounce** (filtra ruído rápido).

---

Se quiser, eu posso ainda adicionar **recalibração automática** — por exemplo, se um pino ficar muito tempo sem toque, ele atualiza o baseline sozinho.
Isso deixa o sistema “autoajustável” para mudanças de temperatura e umidade.

Quer que eu já adicione essa recalibração automática também?



---




Entendi — no seu código atual você usa `calibrate_pots()` e `calc_calibrate()`
para gerar **um único valor de baseline por canal**,
mas depois aplica um `config.THRESH_POT` fixo para todos.
A integração que te propus vai trocar isso por **thresholds individuais e histerese**,
mas mantendo sua estrutura de `start()`.

Vou te mostrar como ficaria adaptado para o seu `main`, usando:

* **Baseline por canal**
* **`press_thresh[i]`** e **`release_thresh[i]`** separados
* **Debounce**
* Aproveitando seus `INDEX_MAP_POTS` e chamadas `send_charPs(...)`

---

### 1️⃣ No topo do arquivo (depois dos imports)

```python
# ===== CONFIGS TOUCH =====
CALIB_SAMPLES   = 100   # Amostras por canal
PRESS_OFFSET    = 50    # Quanto abaixo do baseline aciona
RELEASE_OFFSET  = 30    # Quanto abaixo do baseline libera
DEBOUNCE_COUNT  = 3     # Leituras consecutivas para confirmar toque

# ===== VARIÁVEIS GLOBAIS =====
baseline        = []
press_thresh    = []
release_thresh  = []
pot_counter     = []
triggerPot      = []
pval            = []
```

---

### 2️⃣ Nova calibração de pots (substitui `calibrate_pots`)

```python
def calibrate_pots(pots):
    global baseline, press_thresh, release_thresh, pot_counter, triggerPot, pval

    num_pots = len(pots)
    baseline        = [0] * num_pots
    press_thresh    = [0] * num_pots
    release_thresh  = [0] * num_pots
    pot_counter     = [0] * num_pots
    triggerPot      = [False] * num_pots
    pval            = [0] * num_pots

    print("Calibrando... não toque nos sensores.")
    for i in range(num_pots):
        soma = 0
        for _ in range(CALIB_SAMPLES):
            soma += pots[i].read()
            time.sleep_ms(5)
        baseline[i]       = soma / CALIB_SAMPLES
        press_thresh[i]   = baseline[i] - PRESS_OFFSET
        release_thresh[i] = baseline[i] - RELEASE_OFFSET

    print("Baseline:       ", baseline)
    print("Press thresh:   ", press_thresh)
    print("Release thresh: ", release_thresh)
```

---

### 3️⃣ Nova verificação de pots (substitui `check_pots`)

```python
def check_pots(abclevel):
    global pval, triggerPot, pot_counter

    for i, pot in enumerate(pots):
        val = pot.read()
        pval[i] = val
        mapped_i = INDEX_MAP_POTS[i]

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 1, config.THIS_IS))
                log(f"[POT{mapped_i}] Pressionado | val={val} | abclevel={abclevel}", 2)
                triggerPot[i] = True
                pot_counter[i] = 0

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 0, config.THIS_IS))
                log(f"[POT{mapped_i}] Liberado | val={val} | abclevel={abclevel}", 2)
                triggerPot[i] = False
                pot_counter[i] = 0

        else:
            pot_counter[i] = 0
```

---

### 4️⃣ Alterações no `start()`

No início do `start()` troque:

```python
maxCalibratePots = calibrate_pots(pots)
log("maxCalibratePots:", maxCalibratePots)
```

por:

```python
calibrate_pots(pots)
```

E na parte do loop principal, remova esta parte:

```python
pval = [pot.read() - maxCalibratePots[i] for i, pot in enumerate([pot1, pot2, pot3, pot4, pot5])]
log(f"[POT VALS] {pval}", 2)

abclevel = [stepX, stepY]

triggerPot, holdclick, wait2Zero, cycle = check_pots(
    pval, threshPot, triggerPot, abclevel, holdclick, wait2Zero, cycle
)
```

e coloque:

```python
abclevel = [stepX, stepY]
check_pots(abclevel)
```

---

### 5️⃣ Resultado

* Cada canal terá **baseline** e thresholds próprios.
* O disparo só ocorre se o valor ficar **abaixo do press threshold por 3 leituras seguidas**.
* A liberação só ocorre se o valor subir **acima do release threshold**.
* Isso corrige a sensibilidade desigual que você sentia na Maxima.

---

Se quiser, eu também consigo incluir **recalibração automática** no `check_pots()` para quando o sensor ficar muito tempo sem toque, assim ele compensa variações ambientais sem precisar reiniciar.
Quer que eu já coloque isso também?


então 


# Reset se parado
if wait2Zero:
    cycle += 1
if cycle == config.CYCLE_RESET_LIMIT:
    stepY = stepX = 0
    vibrar(vib, 2)
    log("[RESET] StepX e StepY resetados")


wait2Zero e o cycle 



---

Beleza — vou ajustar para:

1. **Passar `pots` como parâmetro** para evitar erro.
2. **Manter a lógica antiga do `wait2Zero` e `cycle`**, igual você usava no `check_pots()` antigo.

Ficaria assim:

```python
def check_pots(pots, abclevel, wait2Zero, cycle):
    global pval, triggerPot, pot_counter

    for i, pot in enumerate(pots):
        val = pot.read()
        pval[i] = val
        mapped_i = INDEX_MAP_POTS[i]

        if not triggerPot[i] and val < press_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 1, config.THIS_IS))
                log(f"[POT{mapped_i}] Pressionado | val={val} | abclevel={abclevel}", 2)
                triggerPot[i] = True
                pot_counter[i] = 0
                wait2Zero = False
                cycle = 0

        elif triggerPot[i] and val > release_thresh[i]:
            pot_counter[i] += 1
            if pot_counter[i] >= DEBOUNCE_COUNT:
                send_charPs(potsgyrotozmk(abclevel, mapped_i, 0, config.THIS_IS))
                log(f"[POT{mapped_i}] Liberado | val={val} | abclevel={abclevel}", 2)
                triggerPot[i] = False
                pot_counter[i] = 0
                wait2Zero = True

        else:
            pot_counter[i] = 0

    return wait2Zero, cycle
```

E no `start()` trocamos esta parte:

```python
# Leitura dos potenciômetros
abclevel = [stepX, stepY]
wait2Zero, cycle = check_pots(pots, abclevel, wait2Zero, cycle)

# Reset se parado
if wait2Zero:
    cycle += 1
if cycle >= config.CYCLE_RESET_LIMIT:
    stepY = stepX = 0
    vibrar(vib, 2)
    log("[RESET] StepX e StepY resetados")
    cycle = 0
```

---

Assim:

* **`pots`** é passado para `check_pots()` (evita o `NameError`).
* **`wait2Zero`** só é `True` quando você solta o último pot.
* **`cycle`** incrementa só quando está parado e reseta `stepX`/`stepY` após o tempo configurado.

Se quiser, já posso também incluir a detecção de inatividade **usando o giroscópio junto com os pots** — aí só reinicia se **não tiver giro + não tiver pot pressionado**. Isso deixaria o reset bem mais preciso. Quer que eu já faça isso também?





---

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   aresp/actions.py
        modified:   aresp/config.py
        modified:   aresp/dicctozmk.py
        modified:   aresp/main.py
        modified:   notes.md
        modified:   print_allfiles_out.txt



