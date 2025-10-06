

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


