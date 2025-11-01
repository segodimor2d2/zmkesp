# ZMK - TRACKING FINGER TO KEYBOARD VIM

![alt text](img_esp3200.png "esp32")

![alt text](img_nrf5284000.png "nrf5284000")

---

# Explicação dos Parâmetros do Arquivo `config.py`

Vou explicar cada parâmetro do arquivo de configuração, seu funcionamento e os valores recomendados:

## Giroscópio
```python
PORAGORA = 14000        # Limite base para thresholds
THRES_PERCENT = 0.1     # Percentual usado para criar thresholds
```

- **PORAGORA**: Valor base para os limiares (thresholds) do giroscópio.
  - Funcionamento: Define a sensibilidade do giroscópio. Valores mais altos exigem movimentos mais bruscos para serem detectados.
  - Valores recomendados: Entre 8000 (mais sensível) e 20000 (menos sensível). 14000 é um bom ponto de partida.

- **THRES_PERCENT**: Percentual de redução dos limiares para criar uma zona morta.
  - Funcionamento: Cria uma pequena margem em torno do limiar para evitar oscilações.
  - Valores recomendados: Entre 0.05 (5%) e 0.2 (20%). 0.1 (10%) é um bom equilíbrio.

## Potenciômetros
```python
THRESH_POT = [-120] * 5 # Thresholds individuais
POT_CALIBRATION_SAMPLES = 40
POT_CALIBRATION_DELAY_MS = 70
```

- **THRESH_POT**: Limiares para detecção de toque nos potenciômetros.
  - Funcionamento: Valores mais negativos exigem mais pressão para ativar.
  - Valores recomendados: Entre -50 (muito sensível) e -200 (pouco sensível). -120 é um bom meio-termo.

- **POT_CALIBRATION_SAMPLES**: Número de amostras para calibração dos potenciômetros.
  - Valores recomendados: Entre 20 (rápido) e 100 (preciso). 40 é um bom compromisso.

- **POT_CALIBRATION_DELAY_MS**: Tempo entre amostras durante a calibração.
  - Valores recomendados: Entre 50ms e 100ms. 70ms permite leituras estáveis.

## Controle de passos automáticos
```python
STEP_WAIT_LIMIT = 5     # Quantos ciclos esperar antes de repetir passo
```

- Funcionamento: Define quantos ciclos o sistema espera antes de repetir automaticamente um movimento.
- Valores recomendados: Entre 3 (rápido) e 10 (lento). 5 é um bom valor intermediário.

## Reset
```python
CYCLE_RESET_LIMIT = 20  # Quantos ciclos parado até resetar stepX/stepY
```

- Funcionamento: Número de ciclos sem movimento para resetar a posição.
- Valores recomendados: Entre 10 (rápido) e 50 (lento). 20 evita resets acidentais.

## Loop principal
```python
TSLEEP = 50             # Delay entre loops (ms)
TCLEAR = 10000          # Intervalo para reset de contador
SAMPLES = 5             # Amostras iniciais do giroscópio
```

- **TSLEEP**: Tempo de espera entre iterações do loop principal.
  - Valores recomendados: Entre 30ms (rápido) e 100ms (lento). 50ms é um bom equilíbrio.

- **TCLEAR**: Intervalo para resetar contadores internos.
  - Valores recomendados: Manter em 10000 (10 segundos) ou similar.

- **SAMPLES**: Número de amostras para média móvel do giroscópio.
  - Valores recomendados: Entre 3 (rápido) e 10 (suave). 5 é um bom valor.

## Ordem dos eixos do giroscópio
```python
GY1, GY2 = 0, 1         # Eixo X primeiro, depois Y
```

- Funcionamento: Define qual eixo do giroscópio controla X (0) e Y (1).
- Valores possíveis: 
  - `0, 1`: Eixo 0 como X, Eixo 1 como Y (padrão)
  - `1, 0`: Inverte os eixos

## DEBUG
```python
DEBUG = 0
```

- Funcionamento: Controla o nível de logs exibidos.
- Valores possíveis:
  - `None`: Mostra todos os logs
  - `-1`: Mostra apenas logs sem nível
  - `N` (número): Mostra apenas logs do nível N
  - `[N1, N2,...]`: Mostra apenas os níveis especificados

## Valores Típicos para Diferentes Cenários

1. **Para maior sensibilidade (movimentos suaves):**
   ```python
   PORAGORA = 8000
   THRES_PERCENT = 0.15
   THRESH_POT = [-80] * 5
   TSLEEP = 40
   ```

2. **Para menor sensibilidade (movimentos mais definidos):**
   ```python
   PORAGORA = 18000
   THRES_PERCENT = 0.08
   THRESH_POT = [-150] * 5
   TSLEEP = 60
   ```

3. **Para uso com crianças ou pessoas com mobilidade reduzida:**
   ```python
   PORAGORA = 6000
   THRES_PERCENT = 0.2
   THRESH_POT = [-50] * 5
   STEP_WAIT_LIMIT = 8
   ```

Recomendo começar com os valores padrão e ajustar gradualmente conforme a necessidade do usuário, testando a sensibilidade e resposta do sistema.

---


# contexto:

##  Estrutura do **módulo “split/bluetooth” oficial** para o transporte BLE para o ZMK 3.5.0:

```
app/src/split/
├── bluetooth/
│   ├── central.c
│   ├── service.c
│   ├── central_bas_proxy.c
│   └── peripheral.c
```

```bash
bt_conn_cb_register(&conn_callbacks);
```

em `central.c` e `peripheral.c`.

👉 Isso é o **registro padrão de callbacks de conexão BLE**, não de transporte split.

### 🔹 O envio BLE ocorre em `service.c`

O envio BLE entre halves (do periférico → central) é feito via
`bt_gatt_notify()` em `service.c`, dentro do módulo `split_svc`.

Cada atributo (`split_svc.attrs[i]`) representa uma *característica BLE* registrada no serviço Split.
Os payloads padrão são estados do teclado (ex: `position_state_changed`, `sensor_event`, etc).

👉 Ou seja, o **periférico envia via GATT notify**, mas **não há API pública genérica** — o transporte é interno ao ZMK.


### 🔹 O recebimento BLE ocorre em `central.c`

o lado **central** usa `bt_gatt_subscribe()` para assinar características BLE e receber notificações do periférico.

Essas notificações disparam callbacks como:

```c
static uint8_t split_central_notify_cb(struct bt_conn *conn,
                                       struct bt_gatt_subscribe_params *params,
                                       const void *data, uint16_t length)
```

Esse é o **callback real** que recebe bytes vindos do periférico.

👉 Esse callback decodifica o `payload` e reconstrói o evento (`position_state_changed`, `sensor_event`, etc).


## 🧭 3️⃣ Conclusão técnica

| Item                                       | Observação                                                              |
| ------------------------------------------ | ----------------------------------------------------------------------- |
| Envio BLE (peripheral)                     | `bt_gatt_notify()` em `app/src/split/bluetooth/service.c`               |
| Recepção BLE (central)                     | `bt_gatt_subscribe()` e callback em `app/src/split/bluetooth/central.c` |

---

## ⚙️ 4️⃣Opções de implementação

1. Usar **a infraestrutura já existente** em `service.c` e `central.c`
   * Adicionar **uma nova characteristic BLE** (por exemplo, `split_mouse_data`)
   * No periférico: chamar `bt_gatt_notify()` com teu payload de mouse
   * No central: adicionar callback em `split_central_notify_cb()` pra decodificar o payload

2. Ou, mais simples: **reutilizar uma característica existente** (como `sensor_event`) e multiplexar teu tipo de evento ali (adicionando um campo “mouse_event”).

---


## 🧩 5️⃣ Caminho ideal pra seguir

me ajuda a fazer uma explicação passo-a-passo mostrando mantendo compatibilidade com o ZMK 3.5.0 sobre:

* Onde adicionar **uma nova característica BLE** em `service.c`
* Onde interceptar ela no `central.c`
* E como conectar isso ao teu `uart_move_mouse_left()`

por favor me ajuda a entender o fluxo e a estrutura do evento para debugar ele.

a versão que estou trabalhando é a versão do zmk v3.5.0,
eu não vou poder ler os logs e por isso estou usando led_debug.c para testar,
meu objetivo é poder enviar esses eventos que estão no uart_move_mouse_right.c do peripheral para o central usando a versão do zmk v3.5.0,

como usar **a infraestrutura já existente** em `service.c` e `central.c`?,
como adicionar **uma nova characteristic BLE** (por exemplo, `split_mouse_data`)?,
No periférico: como chamar `bt_gatt_notify()` com teu payload de mouse?,
No central: como adicionar callback em `split_central_notify_cb()` pra decodificar o payload?,

eu quero achar uma solução feita no zmk-config e não no zmk do repositório,
mantendo compatibilidade com o ZMK 3.5.0 (sem quebrar o split original),

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


