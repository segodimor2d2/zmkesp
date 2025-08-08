


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



/projeto/
│
├── main.py                # Arquivo principal, ponto de entrada
├── config.py              # Configurações e pinos
├── sensores.py            # Funções de leitura do giroscópio e touchpads
├── utils.py               # Funções auxiliares (ex: vibrar, media, calclim, etc)
├── interface.py           # Funções que lidam com os eventos (send_charPs)
└── hidcodes.py            # Já existente: mapeamento de códigos e layout abc
