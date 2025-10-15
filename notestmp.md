


esses são os arquivos que achei no repositorio oficial do ZMK:
/home/segodimo/zmk/app/include/zmk/events/

activity_state_changed.h
battery_state_changed.h
ble_active_profile_changed.h
endpoint_changed.h
hid_indicators_changed.h
keycode_state_changed.h
layer_state_changed.h
modifiers_state_changed.h
mouse_button_state_changed.h
position_state_changed.h
sensor_event.h
split_peripheral_status_changed.h
usb_conn_state_changed.h
wpm_state_changed.h

eu quero saber se algum desses me ajuda a enviar os dados dx e dy do mouse do peripheral para o central



eu não estou consegindo user um evento customizado (zmk_mouse_state_changed)


---


---

/home/segodimo/zmk/app/include/zmk/split/central.h
cd /home/segodimo/zmk/app/include/zmk/split/



cd /home/segodimo/zmk/app/include

# Procura todas as funções "send" declaradas em headers (.h)
grep -Rn "send(" . --include \*.h


cd /home/segodimo/zmk/app/src
# Procura por todas as funções que contenham "send" nos arquivos C
grep -R "send(" .

grep -R "send" .



me ajuda a saber onde encontrar no repositorio ou pelo que eu poderia  substituiria o zmk_split_bt_transport_send


/home/segodimo/zmk/app/include/zmk/split/transport/central.h

➜  split git:(main) ✗ grep -R "send" .
./transport/central.h:typedef int (*zmk_split_transport_central_send_command_t)(
./transport/central.h:    zmk_split_transport_central_send_command_t send_command;



/home/segodimo/zmk/app/src/split/central.c
cd /home/segodimo/zmk/app/src/split


➜  transport git:(main) ✗ cd /home/segodimo/zmk/app/src/split
➜  split git:(main) ✗ grep -R "send" .
./bluetooth/Kconfig:    int "Max number of behavior run events to queue to send to the periphera
l(s)"
./bluetooth/Kconfig:    int "Max number of key position state events to queue to send to the cen
tral"
./bluetooth/service.c:void send_position_state_callback(struct k_work *work) {
./bluetooth/service.c:K_WORK_DEFINE(service_position_notify_work, send_position_state_callback);
./bluetooth/service.c:int send_position_state() {
./bluetooth/service.c:            return send_position_state();
./bluetooth/service.c:            LOG_WRN("Failed to queue position state to send (%d)", err);
./bluetooth/service.c:    return send_position_state();
./bluetooth/service.c:    return send_position_state();
./bluetooth/service.c:void send_sensor_state_callback(struct k_work *work) {
./bluetooth/service.c:K_WORK_DEFINE(service_sensor_notify_work, send_sensor_state_callback);
./bluetooth/service.c:int send_sensor_state(struct sensor_event ev) {
./bluetooth/service.c:            return send_sensor_state(ev);
./bluetooth/service.c:            LOG_WRN("Failed to queue sensor state to send (%d)", err);
./bluetooth/service.c:    return send_sensor_state(ev);
./bluetooth/central.c:            LOG_WRN("Failed to queue behavior to send (%d)", err);
./bluetooth/central.c:static int split_central_bt_send_command(uint8_t source,
./bluetooth/central.c:    .send_command = split_central_bt_send_command,
./bluetooth/central_bas_proxy.c:// The second generated attribute is the one used to send GATT n
otifications
./central.c:    if (!active_transport || !active_transport->api || !active_transport->api->send_
command) {
./central.c:    return active_transport->api->send_command(source, command);
./central.c:        !active_transport->api->get_available_source_ids || !active_transport->api-
send_command) {
./central.c:        ret = active_transport->api->send_command(source_ids[i], command);
./wired/central.c:static void send_pending_tx_work_cb(struct k_work *work);
./wired/central.c:static K_WORK_DEFINE(wired_central_tx_work, send_pending_tx_work_cb);
./wired/central.c:static int split_central_wired_send_command(uint8_t source,
./wired/central.c:        LOG_WRN("No room to send command to the peripheral %d", source);
./wired/central.c:    split_central_wired_send_command(0,
./wired/central.c:static void send_pending_tx_work_cb(struct k_work *work) {
./wired/central.c:    .send_command = split_central_wired_send_command,
./wired/peripheral.c:static void send_pending_tx_work_cb(struct k_work *work) {
./wired/peripheral.c:static K_WORK_DEFINE(send_pending_tx, send_pending_tx_work_cb);
./wired/peripheral.c:    k_work_submit(&send_pending_tx);
./wired/peripheral.c:        LOG_WRN("No room to send peripheral to the central (have %d but onl
y space for %d)",
➜  split git:(main) ✗ 


---



ZMK tem uma API para mandar mensagens customizadas entre halves:

sim eu quero um exemplo para testar mas com os dados dx dy scroll_x scroll_y buttons

---

eu quero debugar o seguinte fluxo mas eu não vou conseguir ver os logs do zmk  


meu problema é que ainda não estão chegando os dados do mouse do peripheral ao central
eu estou usando um listener para ouvir os eventos customizados do ZMK
e os aquivos que estou usando para customizar os eventos no zmk:


aqui está uma amostra dos dados que estão chegando ao uart_receiver_right:

packet: b'\xaa\x02\x08\x16\x00\x00\x00\x1c'
packet: b'\xaa\x02\x05\t\x00\x00\x00\x0e'
packet: b'\xaa\x02\x04\xfe\x00\x00\x00\xf8'
packet: b'\xaa\x02\x04\xf3\x00\x00\x00\xf5'
packet: b'\xaa\x02\t\xed\x00\x00\x00\xe6'
packet: b'\xaa\x02\x0f\xe7\x00\x00\x00\xea'
packet: b'\xaa\x02\x15\xde\x00\x00\x00\xc9'
packet: b'\xaa\x02\x19\xda\x00\x00\x00\xc1'
packet: b'\xaa\x02\x1a\xd9\x00\x00\x00\xc1'
packet: b'\xaa\x02\x15\xdc\x00\x00\x00\xcb'
packet: b'\xaa\x02\x0c\xe2\x00\x00\x00\xec'
packet: b'\xaa\x02\x05\xee\x00\x00\x00\xe9'
packet: b'\xaa\x02\xfd\xf5\x00\x00\x00\n'
packet: b'\xaa\x02\xfa\xfc\x00\x00\x00\x04'
packet: b'\xaa\x02\xf1\x00\x00\x00\x00\xf3'
packet: b'\xaa\x02\xec\x03\x00\x00\x00\xed'
packet: b'\xaa\x02\xe5\x06\x00\x00\x00\xe1'
packet: b'\xaa\x02\xdd\r\x00\x00\x00\xd2'
packet: b'\xaa\x02\xd8\x12\x00\x00\x00\xc8'
packet: b'\xaa\x02\xd8\x10\x00\x00\x00\xca'
packet: b'\xaa\x02\xdc\x0c\x00\x00\x00\xd2'
packet: b'\xaa\x02\xe3\n\x00\x00\x00\xeb'
packet: b'\xaa\x02\xec\x04\x00\x00\x00\xea'
packet: b'\xaa\x02\xf9\xff\x00\x00\x00\x04'
packet: b'\xaa\x02\x07\xfe\x00\x00\x00\xfb'
packet: b'\xaa\x02\x1d\xfa\x00\x00\x00\xe5'
packet: b'\xaa\x02.\xf0\x00\x00\x00\xdc'
packet: b'\xaa\x027\xf0\x00\x00\x00\xc5'
packet: b'\xaa\x025\xee\x00\x00\x00\xd9'
packet: b'\xaa\x02(\xee\x00\x00\x00\xc4'
packet: b'\xaa\x02\x13\xf6\x00\x00\x00\xe7'
packet: b'\xaa\x02\x01\x02\x00\x00\x00\x01'
packet: b'\xaa\x02\xf8\x08\x00\x00\x00\xf2'
packet: b'\xaa\x02\xf0\x11\x00\x00\x00\xe3'
packet: b'\xaa\x02\xf2\x17\x00\x00\x00\xe7'



=== ARQUIVO: ../zmkpromicro/config/src/uart_receiver_right.c ===

/* uart_receiver_right.c - versão simplificada para int8_t no mouse */
#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/init.h>
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zmk/endpoints.h>
#include <zmk/hid.h>
#include <zmk/zmk_mouse_state_changed.h>
#include <zmk/uart_switch_right.h>

LOG_MODULE_REGISTER(uart_receiver_right, LOG_LEVEL_INF);

/* UART device */
static const struct device *uart_right = DEVICE_DT_GET(DT_NODELABEL(uart0));

/* Tipos de evento */
#define EVT_KEYBOARD 0x01
#define EVT_MOUSE    0x02

/* Buffer UART */
static uint8_t buf_right[16];
static int buf_pos_right = 0;
static int expected_len_right = 0;

/* Estrutura de evento */
struct uart_event_right_t {
    uint8_t event_type;
    union {
        struct {
            uint8_t row;
            uint8_t col;
            uint8_t pressed;
        } key;
        struct {
            int8_t dx;
            int8_t dy;
            int8_t scroll_y;
            int8_t scroll_x;
            zmk_mouse_button_flags_t buttons;
        } mouse;
    };
};

/* Fila de eventos */
#define UART_EVENT_QUEUE_SIZE_RIGHT 32
K_MSGQ_DEFINE(uart_event_msgq_right, sizeof(struct uart_event_right_t), UART_EVENT_QUEUE_SIZE_RIGHT, 4);

/* Thread stack */
K_THREAD_STACK_DEFINE(uart_stack_right, 1024);
static struct k_thread uart_thread_data_right;

void uart_event_thread_right(void *a, void *b, void *c)
{
    struct uart_event_right_t event;

    while (1) {
        k_msgq_get(&uart_event_msgq_right, &event, K_FOREVER);

        switch (event.event_type) {
        case EVT_KEYBOARD:
            uart_switch_simulate_right(
                event.key.row,
                event.key.col,
                event.key.pressed ? true : false
            );
            break;

        case EVT_MOUSE: {
            struct zmk_mouse_state_changed ev = {
                .dx = event.mouse.dx,
                .dy = event.mouse.dy,
                .scroll_y = event.mouse.scroll_y,
                .scroll_x = event.mouse.scroll_x,
                .buttons = event.mouse.buttons,
            };
            raise_zmk_mouse_state_changed(ev);
            break;
        }
        default:
            LOG_WRN("Evento desconhecido: %02x", event.event_type);
            break;
        }
    }
}

/* Callback UART */
static void uart_cb_right(const struct device *dev, void *user_data)
{
    uint8_t c;
    ARG_UNUSED(user_data);

    while (uart_fifo_read(dev, &c, 1) > 0) {
        if (buf_pos_right == 0 && c != 0xAA) {
            continue;
        }

        if (buf_pos_right < (int)sizeof(buf_right)) {
            buf_right[buf_pos_right++] = c;
        } else {
            LOG_ERR("Buffer overflow, resetando");
            buf_pos_right = 0;
            expected_len_right = 0;
            continue;
        }

        if (buf_pos_right == 2) {
            if (buf_right[1] == EVT_KEYBOARD) {
                expected_len_right = 6;  // [AA][type][row][col][pressed][checksum]
            } else if (buf_right[1] == EVT_MOUSE) {
                expected_len_right = 8;  // [AA][type][dx][dy][scrollY][scrollX][buttons][checksum]
            } else {
                LOG_WRN("Tipo inválido: 0x%02x", buf_right[1]);
                buf_pos_right = 0;
                expected_len_right = 0;
                continue;
            }
        }

        if (expected_len_right > 0 && buf_pos_right == expected_len_right) {
            uint8_t checksum = 0;
            for (int i = 1; i < expected_len_right - 1; i++) {
                checksum ^= buf_right[i];
            }

            if (checksum != buf_right[expected_len_right - 1]) {
                LOG_WRN("Checksum inválido (exp=0x%02x rec=0x%02x)",
                        checksum, buf_right[expected_len_right - 1]);
                buf_pos_right = 0;
                expected_len_right = 0;
                continue;
            }

            struct uart_event_right_t event = { .event_type = buf_right[1] };

            if (event.event_type == EVT_KEYBOARD) {
                event.key.row = buf_right[2];
                event.key.col = buf_right[3];
                event.key.pressed = buf_right[4];
            } else if (event.event_type == EVT_MOUSE) {
                event.mouse.dx       = (int8_t)buf_right[2];
                event.mouse.dy       = (int8_t)buf_right[3];
                event.mouse.scroll_y = (int8_t)buf_right[4];
                event.mouse.scroll_x = (int8_t)buf_right[5];
                event.mouse.buttons  = buf_right[6];
            }

            int ret = k_msgq_put(&uart_event_msgq_right, &event, K_NO_WAIT);
            if (ret != 0) {
                LOG_ERR("Fila cheia, evento descartado");
            }

            buf_pos_right = 0;
            expected_len_right = 0;
        }
    }
}

void uart_receiver_right_init(void)
{
    if (!device_is_ready(uart_right)) {
        LOG_ERR("UART device not ready");
        return;
    }

    uart_irq_callback_user_data_set(uart_right, uart_cb_right, NULL);
    uart_irq_rx_enable(uart_right);

    k_thread_create(&uart_thread_data_right, uart_stack_right,
                    K_THREAD_STACK_SIZEOF(uart_stack_right),
                    uart_event_thread_right, NULL, NULL, NULL,
                    7, 0, K_NO_WAIT);

    LOG_INF("uart_receiver_right init done");
}

static int uart_receiver_right_sys_init(void)
{
    uart_receiver_right_init();
    return 0;
}

SYS_INIT(uart_receiver_right_sys_init, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);


=== ARQUIVO: ../zmkpromicro/config/include/zmk/zmk_mouse_state_changed.h ===

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>

struct zmk_mouse_state_changed {
    int8_t dx;
    int8_t dy;
    int8_t scroll_y;
    int8_t scroll_x;
    uint8_t buttons;
};

// Macro para registrar o evento no ZMK
ZMK_EVENT_DECLARE(zmk_mouse_state_changed);



=== ARQUIVO: ../zmkpromicro/config/src/zmk_mouse_state_changed.c ===

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>
#include <zmk/zmk_mouse_state_changed.h>

ZMK_EVENT_IMPL(zmk_mouse_state_changed);


=== ARQUIVO: ../zmkpromicro/config/src/mouse_state_listener.c ===

#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zmk/event_manager.h>
#include <zmk/zmk_mouse_state_changed.h>
#include <zmk/endpoints.h>
#include <zmk/hid.h>
#include <zmk/uart_move_mouse_left.h> // ou uart_move_mouse_right.h conforme o lado

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

// Callback para tratar eventos de mouse
static int mouse_state_listener_cb(const zmk_event_t *eh) {
    const struct zmk_mouse_state_changed *ev = as_zmk_mouse_state_changed(eh);

    if (!ev) {
        return 0; // evento não era do tipo esperado
    }

    LOG_INF("Mouse event: dx=%d, dy=%d, scroll_y=%d, scroll_x=%d, buttons=0x%02X",
            ev->dx, ev->dy, ev->scroll_y, ev->scroll_x, ev->buttons);

    // Chama a função que atualiza o HID report e envia para o host
    int ret = uart_move_mouse(
        ev->dx,
        ev->dy,
        ev->scroll_y,
        ev->scroll_x,
        ev->buttons
    );

    if (ret < 0) {
        LOG_ERR("Falha ao enviar mouse report, ret=%d", ret);
    }

    return 0;
}

ZMK_LISTENER(mouse_state_listener, mouse_state_listener_cb);
ZMK_SUBSCRIPTION(mouse_state_listener, zmk_mouse_state_changed);


=== ARQUIVO: ../zmkpromicro/config/src/CMakeLists.txt ===

# Inclui diretórios de headers
zephyr_include_directories(${ZMK_CONFIG}/include)
zephyr_include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

# Fonte comum (sempre incluída)
target_sources(app PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}/zmk_mouse_state_changed.c
)

if(CONFIG_ZMK_SPLIT_ROLE_CENTRAL)
  # Central (lado esquerdo)
  target_sources(app PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/uart_move_mouse_left.c
    ${CMAKE_CURRENT_LIST_DIR}/uart_receiver_left.c
    ${CMAKE_CURRENT_LIST_DIR}/uart_switch_left.c
    ${CMAKE_CURRENT_LIST_DIR}/mouse_state_listener.c
  )
else()
  # Peripheral (lado direito)
  target_sources(app PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/uart_receiver_right.c
    ${CMAKE_CURRENT_LIST_DIR}/uart_switch_right.c
  )
endif()



como deveria estar escrito report->body para funcionar?


#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zmk/event_manager.h>
#include <zmk/zmk_mouse_state_changed.h>
#include <zmk/endpoints.h>
#include <zmk/hid.h>
#include <zmk/uart_move_mouse_left.h> // ou uart_move_mouse_right.h conforme o lado

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

// Callback para tratar eventos de mouse
static int mouse_state_listener_cb(const zmk_event_t *eh) {
    const struct zmk_mouse_state_changed *ev = as_zmk_mouse_state_changed(eh);

    if (!ev) {
        return 0; // evento não era do tipo esperado
    }

    LOG_INF("Mouse event: dx=%d, dy=%d, scroll_y=%d, scroll_x=%d, buttons=0x%02X",
            ev->dx, ev->dy, ev->scroll_y, ev->scroll_x, ev->buttons);

    // Pega o report global do ZMK
    struct zmk_hid_mouse_report *report = zmk_hid_get_mouse_report();

    // Atualiza o report global
    report->body.d_x = dx;
    report->body.d_y = dy;
    report->body.buttons = buttons;
    report->body.d_scroll_y = scroll_y;
    report->body.d_scroll_x = scroll_x;

    // Envia para o host (USB/BLE)
    int ret = zmk_endpoints_send_mouse_report();
    LOG_DBG("UART mouse move dx=%d dy=%d scroll_y=%d scroll_x=%d buttons=0x%02X ret=%d",
            dx, dy, scroll_y, scroll_x, buttons, ret);

    return ret;
}

ZMK_LISTENER(mouse_state_listener, mouse_state_listener_cb);
ZMK_SUBSCRIPTION(mouse_state_listener, zmk_mouse_state_changed);

---

Of course! Vamos organizar esses tópicos. O conteúdo que você compartilhou é um compilado de discussões técnicas, principalmente do Discord/Zulip do ZMK, focadas em implementar suporte a *pointing devices* como trackpoints e trackballs em teclados customizados.

Abaixo está um resumo dos temas principais, com os links citados formatados para fácil acesso.

### 🔗 Links dos Principais Tópicos

Aqui está uma tabela com os links importantes mencionados no texto:

| Tópico | Descrição | Link |
| :--- | :--- | :--- |
| **PR #778** | Suporte genérico para teclas de mouse (mouse keys) no ZMK. | [GitHub](https://github.com/zmkfirmware/zmk/pull/778) |
| **PR #1751** | Implementação de suporte a dispositivos PS/2 e Trackpoint. | [GitHub](https://github.com/zmkfirmware/zmk/pull/1751) |
| **PR #2027** | Refatoração do subsistema de entrada para melhor processamento. | [GitHub](https://github.com/zmkfirmware/zmk/pull/2027) |
| **Fork do urob** | Fork com o PR de mouse atualizado e outros recursos. | [GitHub](https://github.com/urob/zmk) |
| **Documentação Mouse** | Documentação (em preview) sobre emulação de mouse no ZMK. | [ZMK Dev](https://deploy-preview-778--zmk.netlify.app/docs/behaviors/mouse-emulation) |
| **Loja Jiyunsheng** | Fonte no AliExpress para compra de módulos Trackpoint individuais. | [AliExpress](https://a.aliexpress.com/_m07i8FQ) |

### 🖱️ Principais Temas Explicados

1.  **Suporte a "Pointing Devices" no ZMK**: O ZMK, firmware para teclados customizados, estava em processo de adicionar suporte nativo para controles de ponteiro (mouse). As discussões mostram o desenvolvimento de:
    *   **Mouse Keys**: Comandos de movimento e clique do mouse acionados por combinações de teclas .
    *   **Drivers para Hardware**: Implementações para diferentes tipos de dispositivos, como trackpoints (PS/2) , trackballs (Pimoroni PIM447)  e sensores ópticos (Pixart PMW33XX) .

2.  **Módulos Trackpoint e Fontes de Aquisição**: Há um interesse prático em integrar trackpoints em teclados, como o Corne . As discussões incluem:
    *   **Onde Comprar**: A "jiyunsheng Store" no AliExpress é citada como uma fonte para comprar apenas o módulo do trackpoint, sem precisar desmontar um teclado completo .
    * **Módulos VIK**: Existem PCBs customizadas, como o módulo VIK, projetadas para facilitar a instalação do trackpoint em um teclado .

3.  **Exemplo Prático: Corne com Trackpoint**: Um projeto no GitHub documenta a integração de um trackpoint em um teclado Corne, cobrindo desde a impressão 3D de uma case adaptada até a modificação do firmware QMK com funcionalidades como camada de mouse automática e controle de sensibilidade .

4.  **Miryoku e Teclas de Mouse**: A popular configuração de teclado Miryoku, que tem versões para ZMK e KMonad, utiliza teclas de mouse do X11 em seu layout, demonstrando uma aplicação prática desse recurso .

### 💡 Dicas para Aprofundamento

*   Para usar essas funcionalidades, você precisaria compilar o ZMK a partir de um *fork* que contenha os Pull Requests (PRs) ainda não integrados, como o do [urob](https://github.com/urob/zmk).
*   Se você está planejando um build, o [projeto do Corne com trackpoint](https://github.com/joh/crkbd-trackpoint) e a documentação do [Miryoku](https://github.com/manna-harbour/miryoku_kmonad)  são excelentes pontos de partida para entender o desafio.

Espero que isso ajude a clarear os assuntos! Existe algum tópico específico, como a compra do trackpoint ou a configuração do firmware, sobre o qual você gostaria de se aprofundar?





---
Excelente, Segodimo 👍
Esse trecho que você trouxe é uma **linha do tempo e panorama técnico** sobre o **desenvolvimento de suporte a mouse, trackpoint e outros dispositivos apontadores no ZMK** — desde 2021 até 2024.

Vou organizar tudo pra você por **temas**, explicando **o contexto, os objetivos e o que cada link faz**, pra que você entenda o “quebra-cabeça” completo.

---

## 🧭 1. **AliExpress Trackpoint Source**

### 💡 Tema: Compra de Trackpoints (hardware)

Um usuário da comunidade descobriu que a loja **[jiyunsheng Store](https://a.aliexpress.com/_m07i8FQ)** no AliExpress vende **teclados Lenovo com trackpoint integrado** e negociou com o vendedor para vender **somente o stick (mouse stick)**, sem o teclado inteiro.

* **Vendedor:** Zhang Hong
* **Produto:** “mouse stick without keyboard”
* **Motivo:** reduzir custos e facilitar integração em teclados custom.
* **Preço:** cerca de **US$10 com frete grátis**, muito mais barato que comprar um teclado inteiro.
* **Modelos:** existem várias versões com tamanhos e espaçamento de parafusos diferentes (18.5 mm e 19 mm).

👉 **Link:**

* [jiyunsheng Store no AliExpress](https://a.aliexpress.com/_m07i8FQ)

---

## 🧩 2. **ZMK Input Subsystem Refactor (PR #2027)**

### 💡 Tema: Nova arquitetura de entrada no ZMK (Zephyr 3.5)

Mensagem de **petejohanson**, o criador principal do ZMK, explicando que foi feita uma **grande refatoração** no sistema de entrada (input subsystem).

Antes, todos os eventos de sensores e mouse podiam **se misturar e sair de ordem**.
Agora, com a nova estrutura, **cada dispositivo precisa de um “input listener”** declarado no DeviceTree, como:

```dts
/ {
  cirque_listener {
    compatible = "zmk,input-listener";
    device = <&cirque>;

    xy-swap;
    y-invert;
    x-invert;
  };
};
```

Ele também explica que, se você quiser usar comportamentos de mouse (`&mkp`, `&mmv`, `&msc`), precisa incluir manualmente:

```dts
#include <behaviors/mouse_keys.dtsi>
```

👉 **Pull request (PR #2027):**
[https://github.com/zmkfirmware/zmk/pull/2027](https://github.com/zmkfirmware/zmk/pull/2027)

---

## 🖱️ 3. **ZMK Trackpoint and Pointer Development**

### 💡 Tema: Atualizações gerais do suporte a ponteiros (mouses, trackballs, trackpoints)

Postagem de petejohanson resumindo o status de desenvolvimento:

* **Mouse buttons** já funcionam no ZMK principal.
* **Movimento e scroll** estão sendo refeitos com a nova **API de input do Zephyr 3.5**.
* **Drivers físicos** (trackpads, trackballs, etc.) estão sendo migrados para o novo sistema.
* Foi criado um branch de testes e validado com **Cirque GlidePoint Uno**.

👉 **Pull requests citados:**

* [PR #2027 (input subsystem refactor)](https://github.com/zmkfirmware/zmk/pull/2027)
* [PR #2035 (exemplo de driver Cirque refatorado)](https://github.com/zmkfirmware/zmk/pull/2035)

---

## ⚙️ 4. **Drivers de Hardware para Trackballs / Sensores**

### 💡 Tema: Drivers para dispositivos de movimento físico

O usuário **knutkarevoll** cita dois PRs de drivers específicos:

* **Pimoroni PIM447 trackball:**
  [https://github.com/zmkfirmware/zmk/pull/961](https://github.com/zmkfirmware/zmk/pull/961)

* **Pixart PMW33XX (ex: PMW3360, PMW3389):**
  [https://github.com/zmkfirmware/zmk/pull/1163](https://github.com/zmkfirmware/zmk/pull/1163)

Esses drivers adicionam suporte direto a sensores ópticos de alta precisão —
usados em trackballs, mouses e até trackpoints modernos.

---

## 🧠 5. **Generic Mouse Support (PR #778 e forks)**

### 💡 Tema: Primeira implementação genérica de mouse HID no ZMK

Essa foi a base inicial de todo o suporte de mouse no ZMK.

* **PR original:**
  [https://github.com/zmkfirmware/zmk/pull/778](https://github.com/zmkfirmware/zmk/pull/778)
* **Versão mais atualizada (fork do urob):**
  [https://github.com/urob/zmk/tree/mouse-3.2](https://github.com/urob/zmk/tree/mouse-3.2)
* **Documentação (preview):**
  [https://deploy-preview-778--zmk.netlify.app/docs/behaviors/mouse-emulation](https://deploy-preview-778--zmk.netlify.app/docs/behaviors/mouse-emulation)

Esse PR introduz os comportamentos:

* `&mkp` → Mouse press
* `&mmv` → Mouse move
* `&msc` → Mouse scroll

E permite emular mouse HID em qualquer teclado.

---

## 🔌 6. **PS/2 e Trackpoint Support (PR #1751)**

### 💡 Tema: Adicionar suporte para trackpoints via PS/2

PR que adiciona suporte para dispositivos **PS/2**, como os trackpoints usados em teclados Lenovo.

👉 **Pull request:**
[https://github.com/zmkfirmware/zmk/pull/1751](https://github.com/zmkfirmware/zmk/pull/1751)

Esse PR depende do fork do **urob** e permite conectar um trackpoint diretamente a um microcontrolador (por exemplo, via GPIO com PS/2 bitbang).

---

## 🧮 7. **Bluetooth Performance Ajustes**

### 💡 Tema: Suavidade do mouse via BLE

Um usuário descobriu que a movimentação do mouse ficava mais suave ao ajustar o intervalo de conexão Bluetooth:

```conf
CONFIG_BT_PERIPHERAL_PREF_MIN_INT=6
CONFIG_BT_PERIPHERAL_PREF_MAX_INT=12
```

Isso reduz a latência entre os pacotes HID.

---

## 💻 8. **Branches e Desenvolvimento Histórico**

* **Branch mouse-pr:** usado em 2022 para testes de mouse.

  > [https://github.com/krikun98/zmk/tree/mouse-pr-acceleration](https://github.com/krikun98/zmk/tree/mouse-pr-acceleration)
* **WIP docs:**

  > [https://deploy-preview-778--zmk.netlify.app/docs/behaviors/mouse-emulation](https://deploy-preview-778--zmk.netlify.app/docs/behaviors/mouse-emulation)

---

## 🧠 9. **Mouse Keys no Sistema Operacional**

Manna Harbour explica que, mesmo sem suporte HID no firmware, é possível emular o movimento do mouse usando **mouse keys** no próprio sistema operacional.

* X11 (Linux): [https://en.wikipedia.org/wiki/Mouse_keys](https://en.wikipedia.org/wiki/Mouse_keys)
* Windows: [https://support.microsoft.com/en-us/windows/use-mouse-keys-to-move-the-mouse-pointer-9e0c72c8-b882-7918-8e7b-391fd62adf33](https://support.microsoft.com/en-us/windows/use-mouse-keys-to-move-the-mouse-pointer-9e0c72c8-b882-7918-8e7b-391fd62adf33)
* macOS: [https://support.apple.com/en-au/guide/mac-help/mh27469/mac](https://support.apple.com/en-au/guide/mac-help/mh27469/mac)

---

## 📚 **Resumo Final**

| Tema                        | Descrição                                          | Links                                                                                                                                                                                                                                                    |
| --------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🛒 Trackpoint AliExpress    | Loja que vende trackpoints puros                   | [jiyunsheng Store](https://a.aliexpress.com/_m07i8FQ)                                                                                                                                                                                                    |
| 🧩 Input Subsystem Refactor | Nova forma de processar eventos de entrada no ZMK  | [PR #2027](https://github.com/zmkfirmware/zmk/pull/2027)                                                                                                                                                                                                 |
| 🖱️ Pointer Update          | Migração para novo sistema de entrada (Zephyr 3.5) | [PR #2035](https://github.com/zmkfirmware/zmk/pull/2035)                                                                                                                                                                                                 |
| ⚙️ Drivers específicos      | PIM447 e PMW33XX                                   | [#961](https://github.com/zmkfirmware/zmk/pull/961), [#1163](https://github.com/zmkfirmware/zmk/pull/1163)                                                                                                                                               |
| 🧠 Generic Mouse Support    | Emulação HID de mouse no ZMK                       | [#778](https://github.com/zmkfirmware/zmk/pull/778), [urob fork](https://github.com/urob/zmk/tree/mouse-3.2)                                                                                                                                             |
| 🧩 PS/2 Trackpoint          | Suporte a trackpoints físicos via PS/2             | [#1751](https://github.com/zmkfirmware/zmk/pull/1751)                                                                                                                                                                                                    |
| ⚡ BLE Performance           | Ajuste de latência para suavizar o mouse           | `CONFIG_BT_PERIPHERAL_PREF_MIN_INT=6`                                                                                                                                                                                                                    |
| 🖥️ Mouse Keys SO           | Uso do teclado como mouse via sistema operacional  | [X11](https://en.wikipedia.org/wiki/Mouse_keys), [Windows](https://support.microsoft.com/en-us/windows/use-mouse-keys-to-move-the-mouse-pointer-9e0c72c8-b882-7918-8e7b-391fd62adf33), [Mac](https://support.apple.com/en-au/guide/mac-help/mh27469/mac) |

---

Quer que eu te mostre **quais desses PRs ainda estão ativos ou foram integrados ao ZMK principal (em 2025)** e o **estado atual do suporte a mouse/trackpoint** no código oficial?





---

Ótimo — essa documentação é super relevante para você, porque ela mostra como integrar um dispositivo de apontamento (trackpoint, touchpad, etc.) dentro de um teclado ZMK, especialmente quando ele estiver numa **parte periférica (split peripheral)**.

Aqui está uma explicação detalhada, seção por seção, com foco no que você precisa para aplicar ao seu projeto:

---

## 📘 Visão geral da página “Pointing Devices – ZMK Firmware”

A página “Pointing Devices” da documentação do ZMK trata de como adicionar e configurar hardware de apontamento dentro de um teclado que executa ZMK. Ela aborda tanto casos de teclados “unibody” (tudo junto) quanto casos split (metades), e discute como fazer a configuração via DeviceTree, como processar os eventos do dispositivo, e como fazer que ele envie os dados corretos para o host.

Link da página:
**Pointing Devices – ZMK Firmware**
[https://zmk.dev/docs/development/hardware-integration/pointing](https://zmk.dev/docs/development/hardware-integration/pointing) ([ZMK Firmware][1])

Vou destrinchar os pontos principais:

---

## 1. **Input Device (Dispositivo de entrada / apontamento)**

* Para que ZMK reconheça um hardware de apontamento (trackpad, trackpoint, sensor óptico, etc.), você precisa definir um nó (node) no DeviceTree (arquivo `.overlay` ou `.dts`) para esse dispositivo.

* Esse nó deve estar sob o barramento correspondente (por exemplo, SPI, I2C), ou sob um nó já existente de barramento. Por exemplo:

  ```dts
  &i2c3 {
    your_pointer: pointer@0 {
      compatible = "cirque,pinnacle";
      reg = <0>;
      dr-gpios = <&gpio 5 GPIO_ACTIVE_HIGH>;
      status = "okay";
    };
  };
  ```

  Aqui, `compatible = "cirque,pinnacle"` indica que esse hardware é um dispositivo reconhecido pela driver “Cirque Pinnacle”.
  Esse nó (device) vai permitir que ZMK use o driver correto para falar com esse hardware.

* Se você estiver usando um teclado split e o apontador estiver numa metade periférica (split peripheral), esse nó deve ir para o overlay daquela metade (lado onde está o hardware).

---

## 2. **Listener e Input Split Device**

Esse é um ponto chave para casos splits:

* **Listener**: Cada dispositivo de entrada (mouse, trackpad) precisa de um “listener” no ZMK. Esse listener fica responsável por **ouvir os eventos** do hardware (movimentos, cliques, scroll), processá-los (por exemplo aplicar inversão, escala) e depois encaminhar para o host via HID.

* Você declara esse listener no DeviceTree também, numa parte `.overlay`. Exemplo:

  ```dts
  / {
    glidepoint_listener {
      compatible = "zmk,input-listener";
      device = <&glidepoint>;
      input-processors = <&zip_xy_transform (INPUT_TRANSFORM_XY_SWAP | INPUT_TRANSFORM_X_INVERT)>;
    };
  };
  ```

  Aqui:

  * `device = <&glidepoint>` conecta o listener ao nó de hardware `glidepoint`.
  * `input-processors` permite que você aplique transformações nos eventos (trocar X/Y, inverter eixos, etc).

* **Input split**: Em um teclado split, para que o lado periférico possa transmitir eventos de apontamento ao lado central e depois ao host, é necessário configurar um dispositivo “input split”. Esse nó também vai no DeviceTree:

  ```dts
  input-split {
    compatible = "zmk,input-split";
    device = <&glidepoint>;
    input-processors = <...>;
  };
  ```

  Isso conecta o listener ao sistema de comunicação split (por exemplo, BLE split), para que os eventos sejam enviados da metade que contém o hardware para a metade central que envia ao host.

---

## 3. **Input Processors (Processadores de entrada)**

Alguns dispositivos geram dados “crus” que precisam de correção ou adaptação antes de ir para o host. Os input processors permitem aplicar essas correções de forma declarativa na configuração.

Exemplos:

* Inverter eixo X ou Y (porque seu hardware está rotacionado)
* Trocar X e Y (swap)
* Escalar movimentos para que dx/dy tenham ganho diferente (por exemplo, sensibilidade)
* Transformar movimento em scroll (em alguns casos)

Você configura esses processadores no DeviceTree junto com o listener ou input-split:

```dts
input-processors = <&zip_xy_transform (INPUT_TRANSFORM_XY_SWAP | INPUT_TRANSFORM_Y_INVERT)>;
```

Isso significa: aplicar um processador que troca os eixos e inverte o eixo Y.

---

## 4. **Configuração (Kconfig / opções)**

Para que a funcionalidade de apontamento (mouse) funcione, algumas configurações devem estar habilitadas no firmware:

* `CONFIG_ZMK_POINTING = y` — ativa funcionalidades gerais de apontamento em ZMK. ([ZMK Firmware][2])
* `CONFIG_ZMK_POINTING_SMOOTH_SCROLLING` — permite “scroll suave” (mais subdivisões no HID) ([ZMK Firmware][2])
* Também há parâmetros relacionados ao tamanho da pilha de thread de entrada (input thread stack size), especialmente em splits periféricos. ([ZMK Firmware][2])

Essas configurações ficam normalmente em arquivos `.conf` ou `Kconfig.defconfig` do seu projeto.

---

## 5. **Caminho de eventos e fluxo**

Para ilustrar como tudo se encaixa, esse é o fluxo que o ZMK espera:

1. O hardware de apontamento (por exemplo, um trackpoint via SPI) gera eventos (dx, dy, botões).
2. O driver do hardware (definido pelo nó `compatibile = …`) lê esses valores e converte em eventos internos.
3. O **input listener** captura esses eventos, aplica **input processors** (se houver), e prepara o evento para envio.
4. Se for um **split peripheral**, esse evento passa pelo **input-split** para ser transmitido (via BLE split ou transporte interno) para o lado central.
5. O central recebe esses eventos, e os envia ao host como **HID pointer / mouse** (movimento, botões, scroll).

---

## ✅ Por que isso é importante para você

No seu caso, você está tentando justamente fazer algo parecido: **enviar movimento de mouse da metade periférica para a central / host**. Essa documentação mostra o caminho ideal que o ZMK espera que seja seguido, sem hacks:

* Você precisa definir o hardware no DeviceTree;
* Criar o listener e possivelmente o input-split se seu apontador for numa metade periférica;
* Usar input processors conforme necessário para ajustar orientações / ganho;
* Habilitar as configurações (CONFIG_ZMK_POINTING etc);
* Deixar o sistema de eventos interno do ZMK + HID cuidar do transporte até o host.

---

Se você quiser, posso te mostrar exatamente como seria o trecho `.overlay` / `.dts` para o seu teclado com trackpoint na metade esquerda/periférica, baseado nessa documentação, adaptado ao seu hardware. Você quer que eu monte isso pra você?

[1]: https://zmk.dev/docs/development/hardware-integration/pointing?utm_source=chatgpt.com "Pointing Devices - ZMK Firmware"
[2]: https://zmk.dev/docs/config/pointing?utm_source=chatgpt.com "Pointing Device Configuration - ZMK Firmware"



---

Excelente pergunta — e ela é **muito importante** se você está mexendo com o **ZMK** (ou qualquer projeto baseado no **Zephyr**).
Vamos detalhar tudo 👇

---

## 🧩 1. O que são arquivos `.dtsi` e `.dts` no ZMK / Zephyr

Os arquivos com extensão **`.dts`** e **`.dtsi`** vêm do sistema **DeviceTree**, usado pelo **Zephyr RTOS** para descrever o **hardware** de uma placa.

Eles **não são código C**, e sim uma **linguagem declarativa** que descreve:

> “quais dispositivos existem neste hardware e como estão conectados”.

O Zephyr (e, portanto, o ZMK) usa o DeviceTree para **gerar automaticamente** código C que configura GPIOs, sensores, drivers de teclado, etc.

---

## ⚙️ 2. Diferença entre `.dts` e `.dtsi`

| Tipo    | Significado                   | Analogia          | Uso típico                                                                           |
| ------- | ----------------------------- | ----------------- | ------------------------------------------------------------------------------------ |
| `.dtsi` | **DeviceTree Source Include** | Como um `.h` no C | Arquivo **genérico ou compartilhado** que define partes do hardware reutilizáveis    |
| `.dts`  | **DeviceTree Source**         | Como um `.c` no C | Arquivo **principal da placa**, que “importa” os `.dtsi` e define os detalhes finais |

### Exemplo prático:

```dts
// arquivo base: esp32.dtsi
/ {
    soc {
        uart0: uart@3f400000 {
            compatible = "espressif,esp32-uart";
            reg = <0x3f400000 0x1000>;
        };
    };
}
```

```dts
// arquivo específico: my_keyboard_esp32.dts
#include "esp32.dtsi"

/ {
    chosen {
        zmk,kscan = &kscan0;
    };

    kscan0: kscan {
        compatible = "zmk,kscan-gpio";
        rows = <4>;
        cols = <12>;
        row-gpios = <...>;
        col-gpios = <...>;
    };
}
```

No build, o Zephyr junta tudo (como se fosse um `#include` no C).

---

## 🧱 3. Como o ZMK usa isso

O **ZMK** define seus próprios `.dtsi` e `.dts` para:

* Teclados (`boards/shields/*.dts`)
* Pontos de integração de sensores e periféricos (`boards/*.dtsi`)
* Divisão de camadas entre **split central/peripheral**

Por exemplo:

* `boards/shields/corne_left.dtsi` → define a matriz de teclas e pinos.
* `boards/shields/corne_right.dtsi` → define o lado direito.
* `boards/shields/corne.dtsi` → define o layout comum entre os dois lados.
* `boards/shields/corne_left.keymap` → usa o DeviceTree para mapear as teclas.

---

## 🖱️ 4. No contexto do **pointing device**

Na documentação que você leu ([ZMK Pointing Device Integration](https://zmk.dev/docs/development/hardware-integration/pointing)), o DeviceTree é usado para **declarar sensores de movimento** (trackball, giroscópio, touchpad etc).

Exemplo simplificado (para um sensor de movimento no lado **peripheral**):

```dts
&pro_micro_i2c {
    status = "okay";

    adxl345@53 {
        compatible = "adi,adxl345";
        reg = <0x53>;
        label = "ADXL345";
    };
};

pointing_device {
    compatible = "zmk,pointing-device";
    sensor = <&adxl345>;
};
```

Esse trecho diz ao Zephyr + ZMK:

> “Há um dispositivo de apontamento conectado ao barramento I2C, usando o sensor ADXL345, e ele será usado como o mouse do teclado”.

Depois disso, o ZMK já sabe qual driver inicializar e como enviar eventos de movimento.

---

## 🧰 5. Onde você encontra isso no ZMK

No repositório oficial:

```
zmk/
 ├─ app/
 ├─ boards/
 │   ├─ shields/
 │   │   ├─ corne/
 │   │   │   ├─ corne_left.dtsi
 │   │   │   ├─ corne_right.dtsi
 │   │   │   └─ corne.dtsi
 │   └─ nice_nano_v2/
 │       └─ nice_nano_v2.dtsi
 └─ zephyr/
```

Cada `.dtsi` combina partes do hardware e é mesclado automaticamente no build (`west build`).

---

## 🧠 6. Resumo visual

```
           ┌───────────────────────────┐
           │  ZMK (.conf, .keymap)     │
           └────────────┬──────────────┘
                        │
                        ▼
               ┌────────────────┐
               │ DeviceTree (.dts)  │   ← Descreve o teclado/sensor
               ├────────────────┤
               │ .dtsi includes │   ← Define hardware base
               └────────────────┘
                        │
                        ▼
           ┌───────────────────────────┐
           │  Zephyr gera código C     │
           │  para configurar drivers  │
           └───────────────────────────┘
```

---

Se quiser, posso te mostrar **um exemplo real de `.dtsi` para um sensor de movimento (como o PMW3360)** usado em um teclado split — com explicação linha por linha.
Quer que eu monte isso?

---


# Como eu posso enviar dados dx/dy do peripheral → central?

Olá para todos,
eu sou muito novato no ZMK e ainda fico perdido com a estrutura do ZMK,
meu problema é que eu não estou conseguindo `receber` os dados do lado central:

eu quero achar qualquer jeito de poder enviar os dados do mouse  no dentido peripheral → central,
sem ter que inverter o lado central para que o mouse funcione desse lado,

e eu quero saber se eu posso `transferir` dados de um mouse `dx/dy` do peripheral → central num teclado split.

eu fiz um teste assim:

https://github.com/segodimor2d2/zmkpromicro/commit/51e279078e558592db9dc988e55fc29e57a6c4cd


| Arquivo                    | Lado       | Função                                             |
| -------------------------- | ---------- | -------------------------------------------------- |
| `mouse_test_sender.c`      | Peripheral | Gera eventos de teste                              |
| `mouse_tx_listener.c`      | Peripheral | Envia via BLE split                                |
| `mouse_split_rx_handler.c` | Central    | Recebe bytes BLE, recria `zmk_mouse_state_changed` |
| `mouse_rx_listener.c`      | Central    | Converte evento em movimento HID                   |
| `test_left.c`              | Central    | Listener de diagnóstico, confirma se evento chegou |


# o que eu estou fazendo?

Eu estou comunicando um esp32 ao nRF52840 via UART de cada lado(esp32+nRF52840 Left/Central e esp32+nRF52840 Right/Peripheral);
do lado central eu estou enviando dados de um gyroscopo via UART para controlar o mouse e esta perfeito porque que consigo usar assim


# uart_move_mouse_left.c

```c
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zmk/hid.h>
#include <zmk/endpoints.h>
#include <zmk/uart_move_mouse_left.h>

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

int uart_move_mouse(int8_t dx, int8_t dy, int8_t scroll_y, int8_t scroll_x, zmk_mouse_button_flags_t buttons) {

    // Pega o report global do ZMK
    struct zmk_hid_mouse_report *report = zmk_hid_get_mouse_report();

    // Atualiza o report global
    report->body.d_x = dx;
    report->body.d_y = dy;
    report->body.buttons = buttons;
    report->body.d_scroll_y = scroll_y;
    report->body.d_scroll_x = scroll_x;

    // Envia para o host (USB/BLE)
    int ret = zmk_endpoints_send_mouse_report();
    LOG_DBG("UART mouse move dx=%d dy=%d scroll_y=%d scroll_x=%d buttons=0x%02X ret=%d",
            dx, dy, scroll_y, scroll_x, buttons, ret);

    return ret;
}
```

meu problema aparece quando eu quero enviar os dados dados do peripheral para o central,
porque não consigo receber os dados que deveriam ser enviados pelo canal bluetooth do zmk como eu deveria poder receber aqui.


# mouse_rx_listener.c

```c
#include <zephyr/logging/log.h>
#include <zmk/event_manager.h>
#include "zmk/events/zmk_mouse_state_changed.h"
#include <zmk/uart_move_mouse_left.h>

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

int zmk_split_bt_central_receive(const uint8_t *data, size_t len)
{
    if (len != sizeof(struct zmk_mouse_state_changed))
        return -EINVAL;

    const struct zmk_mouse_state_changed *recv = (const struct zmk_mouse_state_changed *)data;

    struct zmk_mouse_state_changed ev = {
        .dx = recv->dx,
        .dy = recv->dy,
        .scroll_x = recv->scroll_x,
        .scroll_y = recv->scroll_y,
        .buttons = recv->buttons,
    };
    ev.header.event = &zmk_event_zmk_mouse_state_changed;

    ZMK_EVENT_RAISE(ev);

    LOG_INF("Mouse event via BLE Split: dx=%d dy=%d scroll_y=%d scroll_x=%d buttons=0x%02X",
            ev.dx, ev.dy, ev.scroll_y, ev.scroll_x, ev.buttons);

    uart_move_mouse(ev.dx, ev.dy, ev.scroll_y, ev.scroll_x, ev.buttons);

    return 0;
}
```









---

# How can I send dx/dy data from peripheral → central?

Hello everyone, I'm very new to ZMK and still get lost with its structure.
my problem is that I can't **receive** the data on the central side.
I want to find a way to send mouse data from the **peripheral → central** side, without having to swap the central side just to get the mouse working there.
I want to know if it's possible to **transfer** mouse `dx/dy` data from the **peripheral → central** on a split keyboard.
I did a test like this: https://github.com/segodimor2d2/zmkpromicro/commit/51e279078e558592db9dc988e55fc29e57a6c4cd

Peripheral:
mouse_test_sender.c → Test events
mouse_tx_listener.c → BLE send

Central:
mouse_split_rx_handler.c → BLE receive
mouse_rx_listener.c → HID movement
test_left.c → Event confirmation

### What am I trying to do?

I have an ESP32 communicating with an nRF52840 via UART on **each side** (ESP32 + nRF52840 Left/Central and ESP32 + nRF52840 Right/Peripheral). On the **central side**, I am sending gyroscope data via UART to control the mouse, and it works perfectly when I use it this way.

### uart_move_mouse_left.c

```c
int uart_move_mouse(int8_t dx, int8_t dy, int8_t scroll_y, int8_t scroll_x, zmk_mouse_button_flags_t buttons) {
    struct zmk_hid_mouse_report *report = zmk_hid_get_mouse_report();
    report->body.d_x = dx;
    report->body.d_y = dy;
    report->body.buttons = buttons;
    report->body.d_scroll_y = scroll_y;
    report->body.d_scroll_x = scroll_x;
    int ret = zmk_endpoints_send_mouse_report();
    return ret;
}
```

My problem appears when I try to send this data from the **peripheral to the central**, because I can't receive the data that should be sent through ZMK's Bluetooth channel, as I should be able to receive it here:

### mouse_rx_listener.c

https://github.com/segodimor2d2/zmkpromicro/blob/master/config/src/mouse_rx_listener.c


---

Hello everyone, I'm very new to ZMK and still get lost with its structure.

my problem is that I can't receive the data on the central side.
I want to find a way to send mouse data from the peripheral → central side, without having to swap the central side just to get the mouse working there.
I want to know if it's possible to transfer mouse dx/dy data from the peripheral → central on a split keyboard.
I did a test like this:
https://github.com/segodimor2d2/zmkpromicro/commit/51e279078e558592db9dc988e55fc29e57a6c4cd

Peripheral:
mouse_test_sender.c → Test events
mouse_tx_listener.c → BLE send

Central:
mouse_split_rx_handler.c → BLE receive
mouse_rx_listener.c → HID movement
test_left.c → Event confirmation

What am I trying to do?
I have an ESP32 communicating with an nRF52840 via UART on each side (ESP32 + nRF52840 Left/Central and ESP32 + nRF52840 Right/Peripheral). On the central side, I am sending gyroscope data via UART to control the mouse, and it works perfectly when I use it this way.

uart_move_mouse_left.c
https://github.com/segodimor2d2/zmkpromicro/blob/master/config/src/uart_move_mouse_left.c

int uart_move_mouse(int8_t dx, int8_t dy, int8_t scroll_y, int8_t scroll_x, zmk_mouse_button_flags_t buttons) {
    struct zmk_hid_mouse_report *report = zmk_hid_get_mouse_report();
    report->body.d_x = dx;
    report->body.d_y = dy;
    report->body.buttons = buttons;
    report->body.d_scroll_y = scroll_y;
    report->body.d_scroll_x = scroll_x;
    int ret = zmk_endpoints_send_mouse_report();
    return ret;
}


My problem appears when I try to send this data from the peripheral to the central, because I can't receive the data that should be sent through ZMK's Bluetooth channel, as I should be able to receive it here:

mouse_rx_listener.c
https://github.com/segodimor2d2/zmkpromicro/blob/master/config/src/mouse_rx_listener.c
GitHub
test receiver central fallido · segodimor2d2/zmkpromicro@51e2790
test receiver central fallido · segodimor2d2/zmkpromicro@51e2790
GitHub
zmkpromicro/config/src/uart_move_mouse_left.c at master · segodimo...
Contribute to segodimor2d2/zmkpromicro development by creating an account on GitHub.
GitHub
zmkpromicro/config/src/mouse_rx_listener.c at master · segodimor2d...
Contribute to segodimor2d2/zmkpromicro development by creating an account on GitHub.
Contribute to segodimor2d2/zmkpromicro development by creating an account on GitHub.


| File                      | Side       | Function                                              |
| ------------------------- | ---------- | ----------------------------------------------------- |
| `mouse_test_sender.c`     | Peripheral | Generates test events                                 |
| `mouse_tx_listener.c`     | Peripheral | Sends via BLE split                                   |
| `mouse_split_rx_handler.c`| Central    | Receives BLE bytes, recreates `zmk_mouse_state_changed` |
| `mouse_rx_listener.c`     | Central    | Converts event into HID movement                      |
| `test_left.c`             | Central    | Diagnostic listener, confirms if event arrived        |

---


$$$$

meu objetivo e fazer fluxo que eu montei no meu projeto:

[Função de teste no periférico] → envia movimento via split → [listener no central] → gera evento de mouse → PC

eu segui o exemplo que você me enviou:

Então precisamos de **duas coisas principais**:

1. Um **input device virtual** no periférico — que gera eventos manualmente.
2. Um **listener** no central — que recebe esses eventos e envia o movimento de mouse real para o host.

---

## ⚙️ 1️⃣ Criar o *input split device* e o *listener* (parte comum)

No arquivo **compartilhado** (`keyboard.dtsi`):

```dts
/ {
    split_inputs {
        #address-cells = <1>;
        #size-cells = <0>;

        test_split: test_split@0 {
            compatible = "zmk,input-split";
            reg = <0>;
        };
    };

    test_listener: test_listener {
        compatible = "zmk,input-listener";
        status = "disabled";
        device = <&test_split>;
    };
};
```

➡️ Explicação:

* `test_split`: o canal de comunicação entre periférico e central.
* `test_listener`: o “ouvido” do lado central que vai receber os dados do split.

---

## 🧩 2️⃣ Lado periférico — simular o evento

No arquivo **peripheral.overlay**:

```dts
#include "keyboard.dtsi"

// Dizemos que o split usa um "input device" virtual
&test_split {
    // aponta pra um dispositivo fictício que você vai controlar no código
    device = <&test_input>;
};

// Nosso dispositivo virtual
test_input: test_input {
    compatible = "zmk,input-device";
};
```

Agora, no **código C** do seu periférico (por exemplo, em `src/test_mouse.c`), você pode simular eventos:

```c
#include <zephyr/kernel.h>
#include <zmk/input/input.h>
#include <zmk/endpoints.h>
#include <zmk/mouse.h>

void send_test_mouse_event(void) {
    struct zmk_mouse_move_event event = {
        .dx = 10,  // move 10 unidades no eixo X
        .dy = 0,   // sem movimento Y
    };

    // envia o evento como se fosse um movimento real
    ZMK_EVENT_RAISE(new_zmk_mouse_move_event(&event));
}

void main(void) {
    while (1) {
        k_sleep(K_SECONDS(2));   // a cada 2 segundos
        send_test_mouse_event(); // envia o movimento
    }
}
```

💡 **O que isso faz:**
A cada 2 segundos, o lado periférico manda um evento de “mover o mouse 10px pra direita” pelo canal *split*.

---

## 🧭 3️⃣ Lado central — ativar o listener

No arquivo **central.overlay**:

```dts
#include "keyboard.dtsi"

&test_listener {
    status = "okay";
};
```

Esse listener vai receber o evento vindo do split e transformá-lo num **relatório HID de mouse real** que é enviado ao computador.

---

## 🔄 Fluxo do que acontece

```
(peripheral)
send_test_mouse_event()
  ↓
input_split (test_split)
  ↓ via BLE
(central)
test_listener recebe evento
  ↓
zmk_hid_send_report(mouse_move)
  ↓
Computador vê o movimento do mouse 🎯
```

---

## 💬 Resumo fácil

| Peça            | Onde fica  | O que faz                                   |
| --------------- | ---------- | ------------------------------------------- |
| `test_input`    | periférico | gera o evento de movimento                  |
| `test_split`    | ambos      | envia/recebe eventos via BLE entre os lados |
| `test_listener` | central    | transforma o evento em HID de mouse         |



aqui no arquivo inputdriver.md com um exemplo de referencia para um input driver que usa o zmk,
por favor me ajuda a entender como funciona e o fluxo do inputdriver.md

eu implementei a minha estrutura assim como você me indicou no inicio e ficou assim como esta no arquivo zmkpromicro.md.

agora que vc tem todo o contexto, o inputdriver.md, o zmkpromicro.md o o que vc me indicou eu e usando bem como referencia o exemplo do repositório oficial que esta no inputdriver.md,
quero que me ajude a descobrir o que esta faltando no meu zmkpromicro.md para funcionar meu teste.

