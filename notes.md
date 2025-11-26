$$$$


zmk v3.5.0

```bash
cd ~/zmk-ws | term
cd ~/zmkesp/firmwar | term
cd ~/zmk-ws/zmkpromicro | term
cd ~/zmkesp
cd ~/zmkesp | term
cd ~/zmk-ws/zmk/app/src/behaviors/locale/ | term

```

```bash
e /home/segodimo/zmkesp/esp/dicctozmk.py
e /home/segodimo/zmkesp/esp/main.py
e /home/segodimo/zmk-ws/zmkpromicro/config/corne.keymap
e /home/segodimo/zmk-ws/zmk/app/boards/shields/corne/corne.dtsi
cd ~/corne/zmk-config | term
cd ~/corne/out_firmware | term
e ~/corne/zmk-config/config/rec_corne.keymap
e /home/segodimo/corne/zmk-config/config/rec_corne.keymap

e /home/segodimo/00notes_apuntes/010nvimNotes.md
cd ~/14java/proyectos-java/exeptions/09exeptions.md
cd ~/14java/proyectos-java/exeptions | term

# 531 bluetooth
e /home/segodimo/00notes_apuntes/011archlinux.md
```


## rec_corne
[x] - add restart no promicro dos dois lados


## corne
[x] - add restart no promicro dos dois lados
[x] - roadmap do ZMK

<!-- LKJ*#$sdf -->
<!-- 1090 -->

Sophia Dai 
ErgO, a smart ring

# atualizar ou refresh oil
c-f atualizar ou refresh oil

:OilRefresh

# app/CMakeLists.txt

add_subdirectory(${ZMK_CONFIG}/src ${CMAKE_CURRENT_BINARY_DIR}/zmk_config_src)

---
# print_allfiles_path.py

python print_allfiles_path.py /home/segodimo/zmkesp

python print_allfiles_path.py /home/segodimo/zmkpromicro
python ../zmkesp/print_allfiles_path.py /home/segodimo/zmkpromicro

python print_allfiles_path.py /home/segodimo/zmk/app/src/split

python print_allfiles_path.py /home/segodimo/.config/nvim
python print_allfiles_path.py /home/segodimo/zmkbkp/nvim

python print_allfiles_path.py /home/segodimo/zmk/app/include/zmk/events
                                                 app/include/zmk/events/mouse_state_changed.h

python print_allfiles_path.py /home/segodimo/zmkxrepos/cirque-input-module/

no aquivo out_print_allfiles.md estão os eventos do ZMK,
existe alguma função que me ajude a enviar os dados dx e dy do mouse do peripheral para o central?

no aquivo out_print_allfiles.md estão os eventos do ZMK,
eu poderia enviar os dados dx e dy do mouse do peripheral para o central via zmk_sensor_event e conseguir receber esses dados do lado central?

---


- remapear puntos

- modo Hold ou modo Tap
jjk- modo Hold é uma ação similar ao -2 gyro que deixa o Hold liberado

- bug tecla pressionada ao mudar step do gyro
    - um teclado envia todas as teclas no momento que todas estejam soltas

- usar dados do acelerômetro para o mouse
    - o gyro controla a direção
    - valor absoluto do acelerômetro se converte em velocidade do movimento do mouse
jk
- reviçar o pull/down com resistores para os eletrodos
    - 1MΩ 2.2MΩ 3.3MΩ 4.7MΩ 10MΩ 22MΩ
    - isolar os eletrodos do ambiente

- ver se funciona calibrar com valores máximos

- ligar e desligar envio de eventos de kb

- gesto iniciar calibração

- reviçar a questão do buffer porque trava   
- testar tirar o chunks
- ver logs no nRF52840

--- --- ---
- v fechar release quando muda o gyro

--- --- ---




lua require("telescope.builtin").find_files()
lua require("telescope.builtin").find_files()

require('telescope.builtin').registers()
lua require('telescope.builtin').registers()

## copiar
1. selecione o texto "v"
2. pressione '"'
3. pressione letra que va assignar
4. pressione "y" yank

ex. "ay

## colar
<!-- 0. selecione o texto "v" (opcional) -->
1. pressione '"'
2. pressione letra que asignó
3. pressione "p" paste

ex. "ap





---



valor_se_verdadeiro if condicao else valor_se_falso

mpremote fs cp :arquivo_no_esp ./arquivo_no_pc
mpremote fs cp :calib.json ./calib.json



mpremote connect /dev/ttyUSB0 
mpremote connect auto
mpremote repl
mpremote connect list
ls /dev/tty*



# ESP
mpre¿¿¿¿mote fs ls

mpremote repl

mpremote kill
mpremote reset

mpremote exec "raise KeyboardInterrupt"
mpremote exec "import machine; machine.reset()"
mpremote exec "start(force_calib=True)"

mpremote exec "from actions import send_charPs; import time;
send_charPs([2, 0, 1]);
time.sleep(1);
send_charPs([1, 4, 1]);
send_charPs([1, 4, 0]);
send_charPs([2, 0, 0]);
"

s-f
mpremote exec "from actions import send_charPs; import time; send_charPs([2, 0, 1]); time.sleep(1); send_charPs([1, 4, 1]); send_charPs([1, 4, 0]); send_charPs([2, 0, 0]); "
s-r
mpremote exec "from actions import send_charPs; import time; send_charPs([2, 0, 1]); time.sleep(1); send_charPs([0, 4, 1]); send_charPs([0, 4, 0]); send_charPs([2, 0, 0]); "
c-c
mpremote exec "from actions import send_charPs; import time; send_charPs([1, 0, 1]); time.sleep(1); send_charPs([2, 3, 1]); send_charPs([2, 3, 0]); send_charPs([1, 0, 0]); "

mpremote exec "from actions import send_charPs; import time;
send_charPs([3, 2, 1]);
time.sleep(1);
send_charPs([0, 4, 1]);
send_charPs([0, 4, 0]);
time.sleep(0.5);
send_charPs([3, 2, 0]);
"

mo1 3, 1 --- mo2 3, 4


mpremote exec "
tstpot(1, 0, delay=1) #shift
tstpot(1, 2, delay=0.1) #s


tstpot(row, col, delay=1)
tstpot(3, 0, delay=0.1) #lgui
tstpot(3, 1, delay=0.1) #mo1
tstpot(3, 2, delay=0.1) #space 

tstpot(3, 3, delay=0.1) #entrer
tstpot(3, 4, delay=0.1) #mo2
tstpot(3, 5, delay=0.1) #ralt

tstpot(3, 0, delay=1) #lgui


import webrepl_setup

192.168.31.148
Config: ('192.168.31.148', '255.255.255.0', '192.168.31.1', '192.168.31.1')

eu posso enviar um arquivo para um esp 32 usando webrepl?
mpremote
como posso enviar um arquivo para webrepl

WebREPL server started on http://192.168.31.148:8266/

- mpremote exec "raise KeyboardInterrupt"
- mpremote exec "import machine; machine.reset()"
- ter um server para recivir la IP 

$$$$
## RUN
mpremote connect /dev/ttyUSB0
mpremote reset
mpremote kill

mpremote connect /dev/ttyUSB0 fs cp esp/main.py :main.py

mpremote connect /dev/ttyUSB0 fs cp esp/config.py :config.py

mpremote connect /dev/ttyUSB0 fs cp esp/pots.py :pots.py
mpremote connect /dev/ttyUSB0 fs cp esp/gyro.py :gyro.py

mpremote connect /dev/ttyUSB0 fs cp esp/calibration.py :calibration.py
mpremote connect /dev/ttyUSB0 fs cp esp/actions.py :actions.py
mpremote connect /dev/ttyUSB0 fs cp esp/dicctozmk.py :dicctozmk.py

mpremote connect /dev/ttyUSB0 fs cp esp/hw.py :hw.py
mpremote fs ls
mpremote connect /dev/ttyUSB0 fs cp esp/mpr121.py :mpr121.py
mpremote connect /dev/ttyUSB0 fs cp esp/mpu6050.py :mpu6050.py
mpremote connect /dev/ttyUSB0 fs cp esp/printlogs.py :printlogs.py


python webrepl_cli.py main.py 192.168.4.1:/main.py
python webrepl_cli.py main.py 192.168.31.148:8266/main.py




# import webrepl_setup
## python webrepl_cli.py -p 105474 main.py 192.168.31.148:8266:/main.py

---

$$$$
espL
10.50.126.135
192.168.31.148
192.168.197.135
s/192.168.31.148/192.168.31.148/g
python esp/webrepl_cli.py -p 105474 192.168.31.148

python esp/webrepl_cli.py -p 105474 esp/main.py 192.168.31.148:8266:/main.py
python esp/webrepl_cli.py -p 105474 esp/config.py 192.168.31.148:8266:/config.py
python esp/webrepl_cli.py -p 105474 esp/dicctozmk.py 192.168.31.148:8266:/dicctozmk.py

python esp/webrepl_cli.py -p 105474 esp/gyro.py 192.168.31.148:8266:/gyro.py
python esp/webrepl_cli.py -p 105474 esp/actions.py 192.168.31.148:8266:/actions.py
python esp/webrepl_cli.py -p 105474 esp/hw.py 192.168.31.148:8266:/hw.py

espR
192.168.197.44
192.168.31.203
s/192.168.31.203/192.168.31.203/g
python esp/webrepl_cli.py -p 105474 192.168.31.203

python esp/webrepl_cli.py -p 105474 esp/main.py 192.168.31.203:8266:/main.py
python esp/webrepl_cli.py -p 105474 esp/config.py 192.168.31.203:8266:/config.py
python esp/webrepl_cli.py -p 105474 esp/dicctozmk.py 192.168.31.203:8266:/dicctozmk.py

python esp/webrepl_cli.py -p 105474 esp/gyro.py 192.168.31.203:8266:/gyro.py
python esp/webrepl_cli.py -p 105474 esp/actions.py 192.168.31.203:8266:/actions.py
python esp/webrepl_cli.py -p 105474 esp/hw.py 192.168.31.203:8266:/hw.py

$$$$

python serverflask.py


zmk-promicronRF52840

rm -rf build
west build -t pristine

# LEFT
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
<!-- west build -p always -s app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmkpromicro/config -->
cp build/zephyr/zmk.uf2 ../zmkesp/firmwar/corne_left.uf2
<!-- cp build/zephyr/zmk.uf2 ../corne/promicro_out/corne_left-nice_nano_v2-zmk.uf2 -->
sudo mount /dev/sdd /mnt/corne         
sudo cp build/zephyr/zmk.uf2 /mnt/corne

# RIGHT
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_right -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
<!-- west build -p always -s app -b nice_nano_v2 -- -DSHIELD=corne_right -DZMK_CONFIG=/home/segodimo/zmkpromicro/config -->
cp build/zephyr/zmk.uf2 ../zmkesp/firmwar/corne_right.uf2
<!-- cp build/zephyr/zmk.uf2 ../corne/promicro_out/corne_right-nice_nano_v2-zmk.uf2 -->
sudo mount /dev/sdd /mnt/corne         
sudo cp build/zephyr/zmk.uf2 /mnt/corne

# RESET
/home/segodimo/zmkesp/firmwar
sudo cp reset-zmk.uf2 /mnt/corne  




# compilando r e l
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_right -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config

# so para testar -n
west build -n -s zmk/app -d build -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
west build -p always -s zmk/app -d build -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config -DCMAKE_VERBOSE_MAKEFILE=1

west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
west build -p always -s zmk/app -d build -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config

# verbose salva no build.log
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config -DCMAKE_VERBOSE_MAKEFILE=1 | tee build.log

➜  zmk-ws grep -R "CACHED_ZMK_CONFIG" build/         
build/CMakeCache.txt:CACHED_ZMK_CONFIG:STRING=/home/segodimo/zmk-ws/zmkpromicro/config
➜  zmk-ws 




---









Excelente pergunta — esses comandos do **West (ferramenta do Zephyr/ZMK)** parecem muito parecidos, mas há **diferenças sutis e importantes** entre eles.
Vamos destrinchar **cada um** dos parâmetros e o que muda entre os exemplos 👇

---

### 🧩 1️⃣

```bash
west build -p always -s zmk/app -d build -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
```

🔹 **Significado:**

* `-p always` → sempre apaga e recria a pasta de build (build limpa).
* `-s zmk/app` → define o diretório da aplicação (ZMK).
* `-d build` → define a pasta de saída (`build`).
* `-b nice_nano_v2` → define a placa alvo.
* `--` → separa argumentos do CMake.
* `-DSHIELD=corne_left` → define o shield (lado esquerdo do Corne).
* `-DZMK_CONFIG=...` → define o caminho da configuração personalizada.

🔸 **Resumo:**
👉 É um **build completo e limpo**, típico para garantir que não há arquivos residuais.
---------------------------------------------------------------------------------------

### 🧩 2️⃣

```bash
west build -p always -s zmk/app -d build -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config -DCMAKE_VERBOSE_MAKEFILE=1 | grep ZMK_CONFIG
```

🔹 **Diferença principal:**

* Adiciona `-DCMAKE_VERBOSE_MAKEFILE=1` → faz o CMake imprimir **todos os comandos e flags** usados na compilação (modo detalhado).
* Usa `| grep ZMK_CONFIG` → **filtra** a saída, mostrando apenas linhas que contêm `ZMK_CONFIG`.

🔸 **Resumo:**
👉 Mesmo build limpo, mas agora você está **debugando** se o `ZMK_CONFIG` foi realmente passado e reconhecido.
--------------------------------------------------------------------------------------------------------------

### 🧩 3️⃣

```bash
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
```

🔹 **Diferença:**

* **Não especifica `-d build`**, então o `west` usa o **diretório padrão** `build/` dentro da pasta atual.

  * Se você estiver em `/home/segodimo/zmk-ws/`, o output vai para `/home/segodimo/zmk-ws/build`.
  * Mas se estiver dentro de outra pasta, pode gerar um build em outro lugar.

🔸 **Resumo:**
👉 Idêntico ao primeiro, só muda o **local da pasta de build** (implícita em vez de explícita).
-----------------------------------------------------------------------------------------------

### 🧩 4️⃣

```bash
west build -n -s zmk/app -d build -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config
```

🔹 **Diferença:**

* `-n` (ou `--dry-run`) → **não executa a compilação**, apenas **mostra o que seria feito**.

  * Não cria arquivos, apenas exibe os comandos de build.

🔸 **Resumo:**
👉 Serve para **testar configurações ou depurar variáveis CMake** sem realmente compilar.
-----------------------------------------------------------------------------------------

### 🧩 5️⃣

```bash
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config -DCMAKE_VERBOSE_MAKEFILE=1 | tee build.log
```

🔹 **Diferença:**

* `-DCMAKE_VERBOSE_MAKEFILE=1` → modo detalhado (como o 2º).
* `| tee build.log` → salva **toda a saída** (stdout) no arquivo `build.log`, **enquanto ainda mostra na tela**.

🔸 **Resumo:**
👉 É o comando ideal para **depuração completa e registro** da build — útil para compartilhar logs (por exemplo, ao pedir ajuda).

---

### 📋 Comparativo rápido:

|  #  | Flag principal              | O que faz                   | Observações                   |                       |
| :-: | --------------------------- | --------------------------- | ----------------------------- | --------------------- |
|  1  | `-p always -d build`        | Build limpa e completa      | Padrão recomendado            |                       |
|  2  | `-DCMAKE_VERBOSE_MAKEFILE=1 | grep`                       | Build detalhada e filtrada    | Para checar variáveis |
|  3  | Sem `-d`                    | Build no diretório padrão   | Mesmo efeito se em pasta raiz |                       |
|  4  | `-n`                        | Simulação (sem compilar)    | Para testar configs           |                       |
|  5  | `tee build.log`             | Build detalhada e salva log | Para depuração                |                       |

---

Se quiser, posso te mostrar **qual comando é ideal** para cada tipo de tarefa (por exemplo: testar configs, gerar firmware, depurar erro de `ZMK_CONFIG`, etc.). Quer que eu monte essa tabela de “quando usar qual”?












---
# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro

por favor revice todo meu código no arquivo out_print_allfiles.md,
eu estou tentando enviar eventos que estão no uart_move_mouse_right.c do peripheral para o central,
eu não vou poder ler os logs e por isso estou usando led_debug.c para testar,
por favor me ajuda a entender o fluxo e a estrutura do evento para debugar ele,
mantendo compatibilidade com o ZMK 3.5.0 (sem quebrar o split original),

eu não estou vendo o led piscar lado central,
pisca sim no lado peripheral mas gostaria fazer testes com o led para confirmar o fluxo desse lado.

---

por favor revice todo meu código no arquivo out_print_allfiles.md,
eu estou tentando enviar eventos que estão no uart_move_mouse_right.c do peripheral para o central,
eu não vou poder ler os logs e por isso estou usando led_debug.c para testar,
eu não estou vendo o led piscar do lado central mas ja testei o led e funciona sim, só que no split_mouse_central.c nenhum dos testes funcionou.

---


# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro

por favor revice todo meu código no arquivo out_print_allfiles.md,
eu quero adicionar dois botões a mais na quarta linha onde só tem 6 botões,
ficariam oito no total adicionando mais um botão de cada lado, como eu faria isso?

ficaria assom por exemplo:
&kp A  &kp S     &kp D  &kp F           &kp G        &kp H  &kp J         &kp K



por favor revice todo meu código no arquivo out_print_allfiles.md,
eu estou usando a configuração do corne split mas eu quero adicionar dois botões a mais,
eu quero adicionar dois botões a mais no keymap na quarta linha onde só tem 6 botões para que fique com quatro de cada,
eu fiz um test para provar o funcionamento dos botões,
mas ainda eu não consigo usar os dois botões j e k na 4ta linha do keymap,
parece que no uart_switch_left.c e uart_switch_right.c não existe.

a entrada das posições é via serial usando UART a ideia é por um botão de cada lado,
uint32_t position = ZMK_KEYMAP_POSITION(3, 6); // j
uint32_t position = ZMK_KEYMAP_POSITION(3, 7); // k

---



Quando eu tento fazer ZMK_KEYMAP_POSITION(3,6)
Internamente o ZMK faz: posição inválida, evento descartado

como eu faço para que funcione?

---
# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro

por favor revice todo meu código no arquivo out_print_allfiles.md,
ZMK_KEYMAP_POSITION(3,6) e ZMK_KEYMAP_POSITION(3,7) não esta funcionando
o objetivo é poder usar ZMK_KEYMAP_POSITION(3,6) e ZMK_KEYMAP_POSITION(3,7)
tem que manter a compatibilidade com o ZMK 3.5.0



---

# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro

por favor revice todo meu código no arquivo out_print_allfiles.md,
ZMK_KEYMAP_POSITION(3,6) e ZMK_KEYMAP_POSITION(3,7) não esta funcionando
o objetivo é poder usar ZMK_KEYMAP_POSITION(3,6) e ZMK_KEYMAP_POSITION(3,7)
tem que manter a compatibilidade com o ZMK 3.5.0

Problema Principal
Erro de compilação no arquivo keymap.c relacionado à inicialização de arrays no sistema de keymaps do ZMK.

Pontos Chave do Erro
Local do erro: app/src/keymap.c linha 87

Tipo de erro: excess elements in array initializer - excesso de elementos na inicialização do array

Contexto: Ocorre durante o processamento das layers do keymap usando macros do Zephyr




git checkout -b main
git push -u origin main
   
---
















---







eu estou simulando eventos de mouse no test_mouse.c,
meu objetivo é poder enviar esses eventos do peripheral para o central usando a verção do zmk v3.5.0,

ignore os arquivos uart_move_mouse_right.c e uart_receiver_right.c,
por favor revice todo meu código no arquivo out_print_allfiles.md.

---

# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro

por favor revice todo meu código no arquivo out_print_allfiles.md.

repare que a versão do zmk é a v3.5.0,
o código split_mouse_rx.c está conseguindo ouvir cada vez que eu pressiono uma tecla qualquer então ele mando o mouse descer sempre
eu quero entender porque o slpit_mouse_rx.c sempre faz isso.

o meu arquivo uart_move_mouse_right.c esta enviando dx e dx mas esta somente ativando o comportamento de mover o mouse para baixo.
eu quero entender o que enta acontecendo no arquivo uart_move_mouse_right.c.



me ajuda a criar um evento novo mas tem que ser usando a versão do zmk é a v3.5.0,


Crie um novo evento zmk_mouse_split_event, como é feito para sensor_event no ZMK.
Isso exige adicionar um header em app/include/zmk/events/, registrar no CMakeLists.txt, e usar ZMK_EVENT_RAISE()






# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro

por favor revice todo meu código no arquivo out_print_allfiles.md.

a versão que estou trabalhando é a versão do zmk é a v3.5.0,

o código split_mouse_rx.c está conseguindo ouvir cada vez que eu pressiono uma tecla qualquer então ele manda o mouse descer sempre
eu quero entender porque o slpit_mouse_rx.c sempre faz isso.

o meu arquivo uart_move_mouse_right.c esta enviando dx e dx e tem um novo evento zmk_mouse_split_event, mas esta somente ativando o comportamento de mover o mouse para baixo.
eu quero entender o que enta acontecendo no arquivo uart_move_mouse_right.c.

meu objetivo é poder enviar esses eventos do peripheral para o central usando a verção do zmk v3.5.0,



grep -R "struct zmk_event_header" /home/segodimo/zmk/app/include/zmk/ -n


eu gosto muito dos seus trabalhos, parabéns!! meu sonho é ter isso no smartphone



# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro

por favor revice todo meu código no arquivo out_print_allfiles.md,
a versão que estou trabalhando é a versão do zmk v3.5.0,
me ajuda a debugar o fluxo para ver onde não esta funcionando,
me ajuda a validar no repositório do zmk o que estou precisando.
meu objetivo é poder enviar esses eventos do peripheral para o central usando a verção do zmk v3.5.0

---


# python print_allfiles_path.py /home/segodimo/zmkpromicro
python print_allfiles_path.py /home/segodimo/zmkpromicro


por favor revice todo meu código no arquivo out_print_allfiles.md,
a versão que estou trabalhando é a versão do zmk v3.5.0,
eu não vou poder ler os logs e por isso estou usando led_debug.c para testar,
meu objetivo é poder enviar esses eventos que estão no uart_move_mouse_right.c do peripheral para o central usando a versão do zmk v3.5.0
por favor me ajuda a entender o fluxo e a estrutura do evento para debugar ele.


Pôr que eu não estou conseguindo receber os dados no split_mouse_rx.c?
eu deveria serializar ev antes de usar ZMK_EVENT_RAISE(ev)?

é verdade que ZMK_EVENT_RAISE(ev) funciona só funciona localmente?
é verdade que esse listener ZMK_SUBSCRIPTION(split_mouse_rx_listener, zmk_mouse_split_event) só captura eventos locais, não via split?

como eu 
1. Registra o evento localmente no *Event Manager*.
2. Se o *split transport* estiver ativo, o evento é **serializado e enviado via BLE para o lado central**.


a versão que estou trabalhando é a versão do zmk v3.5.0,
me ajuda a validar que no repositório oficial do zmk seguiente
No lado central, o ZMK registra callbacks de recepção via: zmk_split_bt_register_receive_callback(callback);
Toda vez que o periférico envia dados com: zmk_split_bt_transport_send(cmd, data, len);

---

# me ajuda a procurar na documentação do ZMK sobre:

# como usar **a infraestrutura já existente** em `service.c` e `central.c`
# como adicionar **uma nova characteristic BLE** (por exemplo, `split_mouse_data`)
# No periférico: como chamar `bt_gatt_notify()` com teu payload de mouse
# No central: como adicionar callback em `split_central_notify_cb()` pra decodificar o payload


como usar **a infraestrutura já existente** em `service.c` e `central.c`
como adicionar **uma nova characteristic BLE** (por exemplo, `split_mouse_data`)
No periférico: como chamar `bt_gatt_notify()` com teu payload de mouse
No central: como adicionar callback em `split_central_notify_cb()` pra decodificar o payload


* Onde adicionar **uma nova característica BLE** em `service.c`
* Onde interceptar ela no `central.c`
* E como conectar isso ao teu `uart_move_mouse_left()`

mantendo compatibilidade com o ZMK 3.5.0 (sem quebrar o split original)?

---

me ajuda a procurar na documentação do ZMK sobre:


---
quero ter compatibilidade com o ZMK 3.5.0

---
eu quero entender o que é fazer um Device Tree Overlays para Adicionar Characteristics
eu quero saber se eu preciso por no overlay do lado central ou do periférico ou nos dois,
eu quero fazer um teste bem simples para validar que o que fiz no overlay esta funcionado
a versão que estou trabalhando é a versão do zmk v3.5.0,


---




rm -rf build





/home/segodimo/zmk-ws/zmkpromicro/config/src/



eu criei workspaces chamado zmk-ws para o zephyr e o zmk,

esse comando não funciona
west build -n -s zmk/app -d build -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config

não compila o config do meu projeto em zmk-ws/zmkpromicro/config/src/

somente compila se eu adicionar essa linha ao final do zmk-ws/zmk/app/CMakeLists.txt
add_subdirectory(${ZMK_CONFIG}/src ${CMAKE_CURRENT_BINARY_DIR}/zmk_config_src)



ZMK_CONFIG

eu rodei assim:
west build -p always -s zmk/app -b nice_nano_v2 -- -DSHIELD=corne_left -DZMK_CONFIG=/home/segodimo/zmk-ws/zmkpromicro/config -DCMAKE_VERBOSE_MAKEFILE=1 | tee build.log

grep -i "ZMK_CONFIG" build.log
➜  zmk-ws grep -i "ZMK_CONFIG" build.log
➜  zmk-ws

grep -i "ZMK_CONFIG" build.log


west list | grep zmkpromicro || true

➜  zmk-ws west list | grep zmkpromicro || true
zmkpromicro  zmkpromicro                  master                                   git@github.com:segodimor2d2/zmkpromicro


grep -Ei "ZMK Config directory|Adding ZMK config directory|Unable to locate ZMK config|KEYMAP_DIRS|config candidates" build.log || true


➜  zmk-ws grep -Ei "ZMK Config directory|Adding ZMK config directory|Unable to locate ZMK config|KEYMAP_DIRS|config candidates" build.log || 
true
-- ZMK Config directory: /home/segodimo/zmk-ws/zmkpromicro/config
➜  zmk-ws 


---

e /home/segodimo/zmk-ws/zmk/app/boards/shields/corne/corne.dtsi



como eu posso mudar meu código para que,
quando key_ready seja True o mouse_ready seja False,
e quando key_ready seja False o mouse_ready seja True?

como eu posso mudar meu código para que,
quando o mouse_ready seja True key_ready seja False


e quando mouse_ready seja False o mouse_ready seja True?


como eu posso mudar meu código para que,
quando o mouse_ready seja True eu não consiga enviar eventos de teclado?

---

ainda 
estou tendo problemas justo quando abclevel muda mentais um botão esta ativo sem fazer o relese do botão
um exemplo seria quando aperto o botão 'j' o abclevel muda para e solto o 'j' então entra em loop ele só consegue parar quando  
me ajude a fazer um teste para validar o que está acontecendo


esta função parece que não está fazendo nada porque ao mudar o abclevel debreia fazer o release de todos os eventos ativos


como eu consigo fazer para que abclevel não mude se os eventos estiverem ativos ainda?


antig


estou tendo problemas justo quando abclevel muda mentais um botão esta ativo sem fazer o relese do botão,
um exemplo seria quando aperto o botão 'f' o abclevel muda para otro valor e eu solto o 'f',
então o botão entra em loop precisando,
me ajude a fazer um teste para validar o que está acontecendo.
o teste não pode gerar tantos logs então tem que ser um teste otimizado para detectar o problemas



eu estou achando que o problema é que o relese de qualquer botão não é enviado se mudar o abclevel,
eu gostaria de testar na função tozmk = potsgyrotozmk(*ev) se é isso que está causando o problema

será que eu consigo fazer um teste neste codigo para validar o que está acontecendo?
o teste não pode gerar tantos logs então tem que ser um teste otimizado para detectar o problemas

apareceu isso no meomento de precionar o botão e logo teve que precionar de novo para parar de fazer o loop,
que euro saber se o teste tem algum indicio de que algo está errado

no 


estou tendo problemas justo quando abclevel muda mentais um botão esta ativo sem fazer o relese dele mesmo,
um exemplo seria quando aperto o botão 'f' o abclevel muda para otro valor e eu solto o 'f', então o botão entra em loop 
como eu faço para garantir que o botão seja liberado no release quando abclevel mudar?

esse codigo funciona com micropython

```python


    # (5,  1,  0): (0, 0),  # esc
    (5,  0,  0): (0, 0),  # esc
    (5, -1,  0): (0, 0),  # esc

    (6,  1,  0): (3, 0),  # mo4
    # (6,  0,  0): (3, 0),  # mo4
    # (6, -1,  0): (3, 0),  # mo4

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


















    # (5,  1,  0): (3, 4),   # bspc
    (5,  0,  0): (3, 4),   # bspc
    (5, -1,  0): (3, 4),   # bspc

    (6,  1,  0): (3, 5),   # mo1
    # (6, -1,  0): (3, 5),   # mo1
    # (6,  0,  0): (3, 5),   # mo1

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

```

```python



        # --- AÇÃO 1: MOVIMENTO (4) E CLICK ESQUERDO SUSTENIDO (6) ---
        # Se 4 E 6 estiverem ativos, use buttons = 1 (Left Click)
        if mouse_ready and 4 in ativos and 6 in ativos and not key_ready:
            dx, dy = gyromouse(gyro[0], gyro[1])
            if dx != 0 or dy != 0:
                print(f'mouse: dx={dx}, dy={dy}, buttons=1 (LClick Hold)')
                send_mouse(dx, dy, 0, 0, 1)

        # --- AÇÃO 2: MOVIMENTO APENAS (4) ---
        # Se 4 estiver ativo, mas 6 não (o 'elif' garante isso), use buttons = 0
        elif mouse_ready and 4 in ativos and not key_ready:
            dx, dy = gyromouse(gyro[0], gyro[1])
            if dx != 0 or dy != 0:
                # print(f'mouse: dx={dx}, dy={dy}')
                send_mouse(dx, dy, 0, 0, 0)

        # --- AÇÃO 3: CLICK DIREITO (7) ---
        # Se 7 estiver ativo, use buttons = 2 (Right Click). (Corrigindo o valor do seu código antigo)
        elif mouse_ready and 7 in ativos and not key_ready:
            dx, dy = gyromouse(gyro[0], gyro[1])
            if dx != 0 or dy != 0:
                send_mouse(dx, dy, 0, 0, 2)

        # --- AÇÃO 4: CLICK ESQUERDO E DIREITO (2) ---
        # Se 2 estiver ativo, use buttons = 3 (Left + Right Click). (Mantendo a lógica do seu código antigo)
        elif mouse_ready and 2 in ativos and not key_ready:
            dx, dy = gyromouse(gyro[0], gyro[1])
            if dx != 0 or dy != 0:
                send_mouse(dx, dy, 0, 0, 3)









        # --- botão ativa o mouse ---
        if mouse_ready and 4 in ativos and not key_ready:
            dx, dy = gyromouse(gyro[0], gyro[1])
            if dx != 0 or dy != 0:
                # print(f'mouse: dx={dx}, dy={dy}')
                send_mouse(dx, dy, 0, 0, 0) # SEM BOTÃO

        elif mouse_ready and 7 in ativos and not key_ready:
            dx, dy = gyromouse(gyro[0], gyro[1])
            if dx != 0 or dy != 0:
                send_mouse(dx, dy, 0, 0, 1) # BOTÃO DIREITO

        elif mouse_ready and 2 in ativos and not key_ready:
            dx, dy = gyromouse(gyro[0], gyro[1])
            if dx != 0 or dy != 0:
                send_mouse(dx, dy, 0, 0, 2) # BOTÃO ESQUERDO

```




ao ligar tudo começa desativado porque key_ready esta False,
ao ativar com a função toggle_ready eu posso usar os botões porque key_ready é True,
ao ativar com a função toggle_mouse eu posso usar o mouse porque mouse_ready é True,

eu quero que ao ativar ao usar o toggle_mouse o key_ready seja False com mouse_ready True,
e ao usar o toggle_mouse de novo o mouse_ready seja False com key_ready True,
a ideia e intercalar os mouse_ready e o key_ready, cada ver que eu usar a função toggle_mouse,














$$$$


3 0  &mo 1 
3 1  &mo 2 
3 2  &mo 3
3 3  &kp ENTER 
3 4  &kp SPACE 
3 5  &kp DELETE
3 6  &kp TAB 
3 7  &kp KP_DIVIDE 
3 8  &kp BSPC 
3 9  &kp TAB  
3 10 &kp MINUS 
3 11 &kp LS(FSLH)

4 0  kp ESC 
4 1  kp LSHFT 
4 2  kp LCTRL 
4 3  kp LALT
4 4  kp LEFT_ARROW 
4 5  kp DOWN 
4 6  kp UP 
4 7  kp RIGHT 
4 8  mkp LCLK 
4 9  mkp RCLK 
4 10 mkp MCLK  
4 11 kp GRAVE



# [v] 0 mo 1  
# [v] 1 mo 2  
# [v] 2 mo 3 
# [v] 3 mo 4  
# [v] 4 kp SPACE  
# [v] 5 kp ENTER  
# [v] 6 kp BSPC  
# [v] 7 kp LALT  

# [v] 8 kp DELETE  
# [v] 9 kp TAB   
# [v] 10 kp MINUS  
# [v] 11 kp LS(FSLH)

<!-- # [v] 0 &kp KRP_DIVIDE / -->
# [v] 1 &kp RRA(W) ?
# [v] 2 &kp ERXCL !

<!-- &kp LA(PIPE) -->
<!-- &kp RBKT     -->

# [x] 5 &kp LS(LEFT_BRACE) `
# [x] 6 &kp SQT ~

# [x] 7 &kp xxxxx &
# [x] 7 &kp xxxxx "

# BACKSLASH [Backslash] and | [Pipe] RBRC \





&kp RA(UNDERSCORE)


&kp EXCL     
&kp RA(W)    
&kp KP_DIVIDE


### &kp EXCL       /
### &kp RA(W)      ?
### &kp KP_DIVIDE  !

### &kp LEFT_PARENTHESIS   (
### &kp RIGHT_PARENTHESIS  )

### &kp LEFT_BRACKET ´
### &kp RIGHT_BRACKET [
### &kp BACKSLASH ]

### &kp LEFT_BRACE   `
### &kp RIGHT_BRACE  {
### &kp RBRC         {
### &kp LS(RIGHT_BRACKET) {

### &kp NON_US_BSLH \
### &kp NON_US_BACKSLASH \

### &kp DOUBLE_QUOTES  `
### &kp LEFT_BRACE   \
### &kp NUBS         ^

### &kp GRAVE            '
### &kp NON_US_BACKSLASH \
### &kp UNDERSCORE       _

### &kp LBKT      ´
### &kp PIPE      }
### &kp RBKT      [

### &kp DOUBLE_QUOTES  &
### &kp AMPS           ^
### &kp UNDERSCORE     _

### &kp DOUBLE_QUOTES ~
### &kp DQT           ^
### &kp SINGLE_QUOTE  ~

### &kp SQT         ~
### &kp APOSTROPHE  ~
### &kp APOS        ~

### &kp TILDE      "
### &kp NON_US_HASH] 
### &kp TILDE2     _ 
 
### &kp GRAVE            '
### &kp NON_US_BACKSLASH \ 
### &kp UNDERSCORE      _  





# &kp RA(UNDERSCORE) \ !!!

# &kp BACKSLASH      
# &kp LA(BACKSLASH)  
# &kp NON_US_BSLH    

# &kp DOUBLE_QUOTES  
# &kp LEFT_BRACE     
# &kp NUBS           























LA(RBKT)Left Alt + ] [Right Bracket] and } [Right Brace]
LA(RIGHT_BRACKET)Left Alt + ] [Right Bracket] and } [Right Brace]

LA(BACKSLASH)Left Alt + \ [Backslash] and | [Pipe]
LA(PIPE)

LA(SINGLE_QUOTE)Left Alt + ' [Apostrophe] and " [Quote (Double)]
LA(DOUBLE_QUOTES)Left Alt + " [Quote (Double)]




&kp LA(RBKT)           &kp LA(PIPE)








&kp LBKT   &kp KP_DIVIDE  &none  &kp RBKT      &kp LS(LEFT_BRACE)  &none        &kp RA(UNDERSCORE)  &kp MINUS   &kp PLUS   &kp PRCNT  &kp DOUBLE_QUOTES  &kp DELETE
&kp SQT    &kp RA(W)      &none  &kp LA(PIPE)  &kp PIPE            &none        &kp N0              &kp STAR    &kp HASH   &kp DLLR   &kp AMPS        &kp GRAVE
&kp MINUS  &non           &none  &none         &kp RBRC            &none        &kp EQUAL           &kp AT      &kp EXCL   &kp RA(W)  &kp UNDERSCORE  &kp AMPS


&kp KP_DIVIDE 
&kp RA(W)     
&kp EXCL      
&kp RA(UNDERSCORE) 
&kp LBKT 
&kp LS(LEFT_BRACE)  
&kp SQT  





eu quero adicionar esta função para mudar o estado do key_ready usando a função toggle_ready


def switch_ready(key_ready, mouse_ready, vib):
    if key_ready:
        toggle_ready(key_ready, vib)
    # else mouse_ready:
    #     vibrar(vib, 1, 1, key_ready=True)



eu quero ligar inicialmente o teclado e se usar a função de novo quero desligar tudo

def toggle_ready(key_ready, mouse_ready, vib):
    if not key_ready and not mouse_ready:
        key_ready = True
        vibrar(vib, 3, 0, key_ready=True)
        return key_ready, mouse_ready
    elif key_ready or mouse_ready:
        key_ready = False
        mouse_ready = False
        vibrar(vib, 3, 0, key_ready=True)
        return key_ready, mouse_ready



usando zmk v3.5.0 como mudo o teclado para ABNT2 na confuguração?



