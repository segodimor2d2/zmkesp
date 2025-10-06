=== CONSOLIDAÇÃO DE CÓDIGOS DA PASTA: ../zmkpromicro ===



=== ARQUIVO: ../zmkpromicro/README.md ===

# Recomendação realista
- Se você precisa de código .c adicional como uart_receiver.c, siga esta estrutura:
- Tenha um fork do repositório ZMK
- No seu fork do ZMK, edite CMakeLists.txt para incluir:
- add_subdirectory(${ZMK_CONFIG}/src)
- Mantenha tudo seu (configs e código) no zmk-config/, e só altere o CMakeLists.txt do ZMK uma vez.

## Vá até o final do arquivo zmk/app/CMakeLists.txt e adicione isso 
### Incluir código do zmk-config/src de fora do repositório
add_subdirectory(${ZMK_CONFIG}/src ${CMAKE_CURRENT_BINARY_DIR}/zmk_config_src)


## compilation test
// #error "!!!!VERIFICANDO SE ESTÁ SENDO COMPILADO!!!!"


=== ARQUIVO: ../zmkpromicro/config/include/zmk/uart_move_mouse_right.h ===

#pragma once

#include <zephyr/kernel.h>

int uart_move_mouse_right(int8_t dx, int8_t dy, int8_t scroll_x, int8_t scroll_y, uint32_t buttons);


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


=== ARQUIVO: ../zmkpromicro/config/include/zmk/uart_switch_left.h ===

#ifndef ZMK_UART_SWITCH_H
#define ZMK_UART_SWITCH_H

#include <stdint.h>
#include <stdbool.h>

int uart_switch_simulate_left(uint8_t row, uint8_t col, bool pressed);

#endif


=== ARQUIVO: ../zmkpromicro/config/include/zmk/uart_move_mouse_left.h ===

#pragma once
#include <zephyr/kernel.h>
#include <zmk/hid.h>

// Agora todos os deslocamentos são int8_t
int uart_move_mouse(int8_t dx, int8_t dy,
                    int8_t scroll_y, int8_t scroll_x,
                    zmk_mouse_button_flags_t buttons);


=== ARQUIVO: ../zmkpromicro/config/include/zmk/uart_switch_right.h ===

#ifndef ZMK_UART_SWITCH_H
#define ZMK_UART_SWITCH_H

#include <stdint.h>
#include <stdbool.h>

int uart_switch_simulate_right(uint8_t row, uint8_t col, bool pressed);

#endif


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


=== ARQUIVO: ../zmkpromicro/config/src/zmk_mouse_state_changed.c ===

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>
#include <zmk/zmk_mouse_state_changed.h>

ZMK_EVENT_IMPL(zmk_mouse_state_changed);


=== ARQUIVO: ../zmkpromicro/config/src/uart_switch_left.c ===

#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zmk/keymap.h>
#include <zmk/behavior.h>
#include <zmk/uart_switch_left.h>
#include <zmk/events/position_state_changed.h>  // necessário para raise_zmk_position_state_changed

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

// Número de colunas da matriz lógica (Corne = 12 colunas)
#define MATRIX_COLS 12

// Calcula índice linear a partir de (row, col)
#define ZMK_KEYMAP_POSITION(row, col) ((row) * MATRIX_COLS + (col))

int uart_switch_simulate_left(uint8_t row, uint8_t col, bool pressed) {
    uint32_t position = ZMK_KEYMAP_POSITION(row, col);

    struct zmk_position_state_changed event = {
        .source = ZMK_POSITION_STATE_CHANGE_SOURCE_LOCAL,
        .state = pressed,
        .position = position,
        .timestamp = k_uptime_get(),
    };

    int ret = raise_zmk_position_state_changed(event);
    LOG_DBG("uart_switch LEFT %s at (row=%d, col=%d) => position %d, result: %d",
            pressed ? "press" : "release", row, col, position, ret);

    return ret;
}


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


=== ARQUIVO: ../zmkpromicro/config/src/uart_receiver_left.c ===

/* uart_receiver_left.c - versão simplificada com int8_t */
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/init.h>
#include <zephyr/logging/log.h>
#include <zmk/uart_switch_left.h>
#include <zmk/uart_move_mouse_left.h>

LOG_MODULE_REGISTER(uart_receiver_left, LOG_LEVEL_INF);

/* UART device */
static const struct device *uart_left = DEVICE_DT_GET(DT_NODELABEL(uart0));

/* Tipos de evento */
#define EVT_KEYBOARD 0x01
#define EVT_MOUSE    0x02

/* Buffer UART */
static uint8_t uart_left_buf[16];
static int uart_left_buf_pos = 0;
static int uart_left_expected_len = 0;

/* Estrutura de evento */
struct uart_left_event_t {
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
            uint8_t buttons;
        } mouse;
    };
};

/* Fila de eventos */
#define UART_LEFT_EVENT_QUEUE_SIZE 32
K_MSGQ_DEFINE(uart_left_event_msgq, sizeof(struct uart_left_event_t), UART_LEFT_EVENT_QUEUE_SIZE, 4);

/* Thread stack */
K_THREAD_STACK_DEFINE(uart_left_stack, 1024);
static struct k_thread uart_left_thread_data;

/* Thread de processamento */
void uart_left_event_thread(void *a, void *b, void *c)
{
    struct uart_left_event_t event;

    while (1) {
        k_msgq_get(&uart_left_event_msgq, &event, K_FOREVER);

        switch (event.event_type) {
        case EVT_KEYBOARD:
            uart_switch_simulate_left(
                event.key.row,
                event.key.col,
                event.key.pressed ? true : false
            );
            break;

        case EVT_MOUSE:
            uart_move_mouse(
                event.mouse.dx,
                event.mouse.dy,
                event.mouse.scroll_y,
                event.mouse.scroll_x,
                event.mouse.buttons
            );
            break;

        default:
            LOG_WRN("Evento desconhecido: %02x", event.event_type);
            break;
        }
    }
}

/* Callback UART */
static void uart_left_cb(const struct device *dev, void *user_data)
{
    uint8_t c;
    ARG_UNUSED(user_data);

    while (uart_fifo_read(dev, &c, 1) > 0) {
        if (uart_left_buf_pos == 0 && c != 0xAA) {
            continue; // espera byte inicial
        }

        if (uart_left_buf_pos < (int)sizeof(uart_left_buf)) {
            uart_left_buf[uart_left_buf_pos++] = c;
        } else {
            LOG_ERR("Buffer overflow detectado, resetando");
            uart_left_buf_pos = 0;
            uart_left_expected_len = 0;
            continue;
        }

        /* Define tamanho esperado */
        if (uart_left_buf_pos == 2) {
            if (uart_left_buf[1] == EVT_KEYBOARD) {
                uart_left_expected_len = 6; // [AA][type][row][col][pressed][checksum]
            } else if (uart_left_buf[1] == EVT_MOUSE) {
                uart_left_expected_len = 8; // [AA][type][dx][dy][scrollY][scrollX][buttons][checksum]
            } else {
                LOG_WRN("Tipo inválido recebido: 0x%02x", uart_left_buf[1]);
                uart_left_buf_pos = 0;
                uart_left_expected_len = 0;
                continue;
            }
        }

        /* Pacote completo */
        if (uart_left_expected_len > 0 && uart_left_buf_pos == uart_left_expected_len) {
            /* Checksum */
            uint8_t checksum = 0;
            for (int i = 1; i < uart_left_expected_len - 1; i++) {
                checksum ^= uart_left_buf[i];
            }

            if (checksum != uart_left_buf[uart_left_expected_len - 1]) {
                LOG_WRN("Checksum inválido: esperado 0x%02x recebido 0x%02x",
                        checksum, uart_left_buf[uart_left_expected_len - 1]);
                uart_left_buf_pos = 0;
                uart_left_expected_len = 0;
                continue;
            }

            /* Cria evento */
            struct uart_left_event_t event = { .event_type = uart_left_buf[1] };

            if (event.event_type == EVT_KEYBOARD) {
                event.key.row = uart_left_buf[2];
                event.key.col = uart_left_buf[3];
                event.key.pressed = uart_left_buf[4];
            } else if (event.event_type == EVT_MOUSE) {
                event.mouse.dx       = (int8_t)uart_left_buf[2];
                event.mouse.dy       = (int8_t)uart_left_buf[3];
                event.mouse.scroll_y = (int8_t)uart_left_buf[4];
                event.mouse.scroll_x = (int8_t)uart_left_buf[5];
                event.mouse.buttons  = uart_left_buf[6];
            }

            int ret = k_msgq_put(&uart_left_event_msgq, &event, K_NO_WAIT);
            if (ret != 0) {
                LOG_ERR("Fila cheia, evento descartado");
            }

            uart_left_buf_pos = 0;
            uart_left_expected_len = 0;
        }
    }
}

/* Inicializa receptor UART */
void uart_left_receiver_init(void)
{
    if (!device_is_ready(uart_left)) {
        LOG_ERR("UART device not ready");
        return;
    }

    uart_irq_callback_user_data_set(uart_left, uart_left_cb, NULL);
    uart_irq_rx_enable(uart_left);

    k_thread_create(&uart_left_thread_data, uart_left_stack,
                    K_THREAD_STACK_SIZEOF(uart_left_stack),
                    uart_left_event_thread, NULL, NULL, NULL,
                    7, 0, K_NO_WAIT);

    LOG_INF("uart_receiver_left init done");
}

static int uart_left_receiver_sys_init(void)
{
    uart_left_receiver_init();
    return 0;
}

SYS_INIT(uart_left_receiver_sys_init, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);


=== ARQUIVO: ../zmkpromicro/config/src/uart_switch_right.c ===

#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zmk/keymap.h>
#include <zmk/behavior.h>
#include <zmk/uart_switch_right.h>
#include <zmk/events/position_state_changed.h>  // Inclua o header do evento

// #error "!!!!VERIFICANDO SE ESTÁ SENDO COMPILADO!!!!"
LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

#define MATRIX_COLS 12
#define ZMK_KEYMAP_POSITION(row, col) ((row) * MATRIX_COLS + (col))

// Função que envia evento position_state_changed via split BLE
int uart_switch_simulate_right(uint8_t row, uint8_t col, bool pressed) {
    uint32_t position = ZMK_KEYMAP_POSITION(row, col);

    struct zmk_position_state_changed event = {
        .source = ZMK_POSITION_STATE_CHANGE_SOURCE_LOCAL,
        .state = pressed,
        .position = position,
        .timestamp = k_uptime_get(),
    };

    int ret = raise_zmk_position_state_changed(event);
    LOG_DBG("uart_switch %s at (%d, %d) => position %d, result: %d",
            pressed ? "press" : "release", row, col, position, ret);
    return ret;
}


=== ARQUIVO: ../zmkpromicro/config/src/uart_move_mouse_left.c ===

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
