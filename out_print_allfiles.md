# Projeto da pasta: /home/segodimo/zmkpromicro

## arquivo: /home/segodimo/zmkpromicro/README.md

```markdown
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

```


## arquivo: /home/segodimo/zmkpromicro/build.yaml

```text
# This file generates the GitHub Actions matrix.
# For simple board + shield combinations, add them to the top level board and
# shield arrays, for more control, add individual board + shield combinations
# to the `include` property. You can also use the `cmake-args` property to
# pass flags to the build command, `snippet` to add a Zephyr snippet, and
# `artifact-name` to assign a name to distinguish build outputs from each other:
#
# board: [ "nice_nano_v2" ]
# shield: [ "corne_left", "corne_right" ]
# include:
#   - board: bdn9_rev2
#   - board: nice_nano_v2
#     shield: reviung41
#   - board: nice_nano_v2
#     shield: corne_left
#     snippet: studio-rpc-usb-uart
#     cmake-args: -DCONFIG_ZMK_STUDIO=y
#     artifact-name: corne_left_with_studio
#
---
include:
  - board: nice_nano_v2
    shield: corne_left
    snippet: zmk-usb-logging
  - board: nice_nano_v2
    shield: corne_right

```


## arquivo: /home/segodimo/zmkpromicro/config/corne_left.conf

```text
# Mouse enable
CONFIG_ZMK_POINTING=y
CONFIG_ZMK_MOUSE=y
# CONFIG_ZMK_HID_REPORT_TYPE_MOUSE=y

# Para nRF52840 (UARTE é a versão com DMA)
# CONFIG_SERIAL=y
# CONFIG_UART_INTERRUPT_DRIVEN=y
# CONFIG_UART_CONSOLE=n


# CONFIG_ZMK_SPLIT=y
CONFIG_ZMK_SPLIT_ROLE_CENTRAL=y

CONFIG_SERIAL=y
CONFIG_UART_INTERRUPT_DRIVEN=y
# CONFIG_ZMK_KEYBOARD_REPORT=y
# CONFIG_ZMK_MOUSE_REPORT=n

# CONFIG_UART_CONSOLE=y
CONFIG_USB_DEVICE_STACK=y
# CONFIG_USB_CDC_ACM=y
# CONFIG_USB_DEVICE_PRODUCT="ZMK CDC ACM"

# CONFIG_USB_DEVICE_INITIALIZE=y

CONFIG_LOG=y
# CONFIG_ZMK_USB_LOGGING=y
CONFIG_LOG_DEFAULT_LEVEL=3
# CONFIG_LOG_DEFAULT_LEVEL=4  # 4 = INFO
# CONFIG_LOG_MODE_DEFERRED=y
# CONFIG_LOG_BACKEND_UART=y
CONFIG_UART_INTERRUPT_DRIVEN=y
# Ativa o módulo com nível INFO
# CONFIG_UART_RECEIVER_LOG_LEVEL_INF=y

# CONFIG_ZMK_HID=y
# CONFIG_ZMK_HID_MOUSE=y
# CONFIG_ZMK_USB_HID=n      # se estiver usando UART, não precisa USB HID
#
# CONFIG_ZMK_MOUSE_REPORT=y

# CONFIG_LOG=y
# CONFIG_LOG_DEFAULT_LEVEL=3
# CONFIG_LOG_DEFAULT_LEVEL=4  # Debug level
# CONFIG_UART_CONSOLE=n       # se estiver usando USB para console
# CONFIG_STDOUT_CONSOLE=y
# CONFIG_LOG_BACKEND_UART=n   # evita que tente enviar via UART
# CONFIG_LOG_BACKEND_USB=y    # depende da versão do Zephyr/ZMK, em alguns casos o LOG via USB é automático quando CDC ACM está habilitado

# CONFIG_DEBUG=y
# CONFIG_USE_SEGGER_RTT=y
# CONFIG_LOG_BACKEND_RTT=y

# CONFIG_ZMK_EVENT_MANAGER_LOG_LEVEL_DBG=y

CONFIG_ZMK_BLE=y  
# CONFIG_ZMK_SPLIT_BLE=y  

CONFIG_INPUT_MODE_THREAD=y

# CONFIG_INPUT=y
# CONFIG_INPUT_EVENT=y

# Ativa o subsistema de input genérico do Zephyr
CONFIG_INPUT=y

# Ativa o split e o driver zmk,input-split
# CONFIG_ZMK_SPLIT=y
# CONFIG_ZMK_SPLIT_BLE=y
# CONFIG_ZMK_INPUT_SPLIT=y

# (Opcional, mas útil para debug)
# CONFIG_LOG=y
# CONFIG_ZMK_USB_LOGGING=y
# CONFIG_ZMK_BLE=y

```


## arquivo: /home/segodimo/zmkpromicro/config/corne_left.overlay

```text
&pinctrl {
    uart0_default: uart0_default {
        group1 {
            psels = <NRF_PSEL(UART_TX, 0, 6)>,
                    <NRF_PSEL(UART_RX, 0, 8)>;
        };
    };

    uart0_sleep: uart0_sleep {
        group1 {
            psels = <NRF_PSEL(UART_TX, 0, 6)>,
                    <NRF_PSEL(UART_RX, 0, 8)>;
            low-power-enable;
        };
    };
};

&uart0 {
    status = "okay";
    current-speed = <115200>;
    pinctrl-0 = <&uart0_default>;
    pinctrl-1 = <&uart0_sleep>;
    pinctrl-names = "default", "sleep";
};


```


## arquivo: /home/segodimo/zmkpromicro/config/corne_right.conf

```text
# Mouse enable
CONFIG_ZMK_POINTING=y
CONFIG_ZMK_MOUSE=y
# CONFIG_ZMK_HID_REPORT_TYPE_MOUSE=y

# Para nRF52840 (UARTE é a versão com DMA)
# CONFIG_SERIAL=y
# CONFIG_UART_INTERRUPT_DRIVEN=y

# CONFIG_ZMK_SPLIT=y
CONFIG_ZMK_SPLIT_ROLE_CENTRAL=n
# CONFIG_ZMK_SPLIT_BLE_CENTRAL_PERIPHERALS=1
# CONFIG_ZMK_SPLIT_ROLE_PERIPHERAL=y
CONFIG_NRF_STORE_REBOOT_TYPE_GPREGRET=y

# CONFIG_ZMK_BLE=y
CONFIG_ZMK_USB=n

CONFIG_SERIAL=y
CONFIG_UART_INTERRUPT_DRIVEN=y
CONFIG_UART_CONSOLE=n
# CONFIG_ZMK_KEYBOARD_REPORT=y
# CONFIG_ZMK_MOUSE_REPORT=n

# CONFIG_UART_CONSOLE=y
CONFIG_USB_DEVICE_STACK=y
# CONFIG_USB_CDC_ACM=y
# CONFIG_USB_DEVICE_PRODUCT="ZMK CDC ACM"

# CONFIG_USB_DEVICE_INITIALIZE=y

CONFIG_LOG=y
# CONFIG_ZMK_USB_LOGGING=y
CONFIG_LOG_DEFAULT_LEVEL=3
# CONFIG_LOG_DEFAULT_LEVEL=4  # 4 = INFO
# CONFIG_LOG_MODE_DEFERRED=y
# CONFIG_LOG_BACKEND_UART=y
CONFIG_UART_INTERRUPT_DRIVEN=y
# Ativa o módulo com nível INFO
# CONFIG_UART_RECEIVER_LOG_LEVEL_INF=y

# CONFIG_ZMK_HID_MOUSE=y
# CONFIG_ZMK_USB_HID_MOUSE=y
# CONFIG_ZMK_BLE_HID_MOUSE=y



# CONFIG_ZMK_HID=y
# CONFIG_ZMK_HID_MOUSE=y          # mouse HID
# CONFIG_ZMK_SPLIT_ROLE_PERIPHERAL=y
# CONFIG_ZMK_USB_HID=y            # se quiser USB

# CONFIG_ZMK_EVENT_MANAGER_LOG_LEVEL_DBG=y

CONFIG_ZMK_BLE=y  
# CONFIG_ZMK_SPLIT_BLE=y 

CONFIG_INPUT_MODE_THREAD=y

# CONFIG_INPUT=y
# CONFIG_INPUT_EVENT=y

# Ativa o subsistema de input genérico do Zephyr
#
CONFIG_INPUT=y

# Ativa o split e o driver zmk,input-split
CONFIG_ZMK_SPLIT=y
CONFIG_ZMK_SPLIT_BLE=y

# CONFIG_ZMK_INPUT_SPLIT=y

# (Opcional, mas útil para debug)
# CONFIG_LOG=y
# CONFIG_ZMK_USB_LOGGING=y
# CONFIG_ZMK_BLE=y

## Habilitar sistema de sensores
# CONFIG_ZMK_SENSING=y

# Tamanho da fila de eventos de sensor
# CONFIG_ZMK_SENSOR_EVENT_QUEUE_SIZE=16

# Sistema de eventos
# CONFIG_ZMK_EVENT_QUEUE_SIZE=32

```


## arquivo: /home/segodimo/zmkpromicro/config/corne.keymap

```text
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#define ZMK_POINTING_DEFAULT_MOVE_VAL 1200  // 600
#define ZMK_POINTING_DEFAULT_SCRL_VAL 25   // 10

#include <input/processors.dtsi>
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <behaviors.dtsi>
#include <dt-bindings/zmk/bt.h>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/outputs.h>
#include <dt-bindings/zmk/pointing.h>
#include <dt-bindings/zmk/rgb.h>


&mmv_input_listener { input-processors = <&zip_xy_scaler 2 1>; };

&msc_input_listener { input-processors = <&zip_scroll_scaler 2 1>; };

&msc {
    acceleration-exponent = <1>;      // 0
    time-to-max-speed-ms = <500>;       // 300
    delay-ms = <0>;                   // 0
};

&mmv {
    time-to-max-speed-ms = <500>;
    acceleration-exponent = <1>;
    trigger-period-ms = <16>;
};


/ {

    behaviors {
        parenthesis: parenthesis {
            compatible = "zmk,behavior-tap-dance";
            label = "PARENTHESIS";
            #binding-cells = <0>;
            bindings = <&kp LEFT_PARENTHESIS>, <&kp RIGHT_PARENTHESIS>;
        };
        bracket: bracket {
            compatible = "zmk,behavior-tap-dance";
            label = "BRACKET";
            #binding-cells = <0>;
            bindings = <&kp RBKT>, <&kp LA(PIPE)>;
        };
        brace: brace {
            compatible = "zmk,behavior-tap-dance";
            label = "BRACE";
            #binding-cells = <0>;
            bindings = <&kp RBRC>, <&kp PIPE>;
        };
    };

    keymap {
            compatible = "zmk,keymap";

      default_layer {
              bindings = <
&kp ESC    &kp Q  &kp W  &kp E     &kp R  &kp T           &kp Y        &kp U  &kp I         &kp O    &kp P     &kp BSPC
&kp LSHFT  &kp A  &kp S  &kp D     &kp F  &kp G           &kp H        &kp J  &kp K         &kp L    &kp SEMI  &kp ENTER
&kp LCTRL  &kp Z  &kp X  &kp C     &kp V  &kp B           &kp N        &kp M  &kp COMMA     &kp DOT  &kp FSLH  &kp RSHIFT
                  /* &kp Q  &kp LALT  &mo 2  &kp SPACE       &kp ENTER    &mo 1  &kp RSHIFT    &kp W */
                  /* &kp A  &kp S     &kp D  &kp F           &kp G        &kp H  &kp J         &kp K */
                  &kp A  &kp S  &kp D  &kp F  &kp G  &kp H  &kp J  &kp K  &none  &none  &none  &none

                        >;
      };

      lower_layer {
              bindings = <
&kp TAB  &none  &kp NUMBER_9  &kp NUMBER_8    &kp NUMBER_7  &none           &kp HOME        &kp PG_DN       &kp PG_UP     &kp END          &parenthesis  &kp LBKT
&trans   &none  &kp NUMBER_6  &kp NUMBER_5    &kp NUMBER_4  &none           &mmv MOVE_LEFT  &mmv MOVE_DOWN  &mmv MOVE_UP  &mmv MOVE_RIGHT  &bracket      &kp SQT
&trans   &none  &kp NUMBER_3  &kp NUMBER_2    &kp NUMBER_1  &kp NUMBER_0    &kp LEFT        &kp DOWN        &kp UP        &kp RIGHT        &brace        &kp MINUS
                /* &none         &none           &none         &none           &kp RSHIFT      &none           &kp LALT      &none */
                &kp A  &kp S  &kp D  &kp F  &kp G  &kp H  &kp J  &kp K  &none  &none  &none  &none
                        >;
      };

      raise_layer {
              bindings = <
&kp LA(TAB)  &trans  &trans  &trans  &trans  &trans          &kp BSLH   &kp MINUS  &kp PLUS  &kp PRCNT  &kp EXCL       &kp LA(DELETE)
&trans       &trans  &trans  &trans  &trans  &trans          &kp N0     &kp STAR   &kp HASH  &kp DLLR   &kp KP_DIVIDE  &kp GRAVE
&trans       &trans  &trans  &trans  &trans  &trans          &kp EQUAL  &kp AT     &kp EXCL  &kp RA(W)  &kp RA(W)      &kp AMPS
                     /* &trans  &trans  &none   &trans          &kp RET    &trans     &trans    &trans */
                &kp A  &kp S  &kp D  &kp F  &kp G  &kp H  &kp J  &kp K  &none  &none  &none  &none
                        >;
      };

        fn_layer {
            display-name = "FN";
            bindings = <
&none  &none  &none  &none  &none  &none    &kp F7  &kp F8  &kp F9    &kp F10  &none  &none
&none  &none  &none  &none  &none  &none    &kp F4  &kp F5  &kp F6    &kp F11  &none  &none
&none  &none  &none  &none  &none  &none    &kp F1  &kp F2  &kp F3    &kp F12  &none  &none
              /* &none  &none  &none  &none    &none   &none   &kp RALT  &none */
              &kp A  &kp S  &kp D  &kp F  &kp G  &kp H  &kp J  &kp K  &none  &none  &none  &none
            >;
        };

        rec_layer {
            bindings = <
&trans  &trans  &trans  &trans        &trans        &trans        &msc SCRL_LEFT  &msc SCRL_DOWN  &msc SCRL_UP  &msc SCRL_RIGHT  &trans  &trans
&trans  &trans  &trans  &mkp MCLK     &mkp RCLK     &mkp LCLK     &mmv MOVE_LEFT  &mmv MOVE_DOWN  &mmv MOVE_UP  &mmv MOVE_RIGHT  &trans  &kp PG_UP
&none   &trans  &trans  &kp C_VOL_DN  &kp C_VOL_UP  &kp C_MUTE    &kp LEFT_ARROW  &kp DOWN        &kp UP        &kp RIGHT        &trans  &kp PG_DN
                /* &trans  &trans        &trans        &none         &trans          &trans          &trans        &trans */
                &kp A  &kp S  &kp D  &kp F  &kp G  &kp H  &kp J  &kp K  &none  &none  &none  &none
            >;

            label = "REC";
        };



    };
};

```


## arquivo: /home/segodimo/zmkpromicro/config/corne_right.overlay

```text


/* 3️⃣ Configura UART e pinos normalmente */
&pinctrl {
    uart0_default: uart0_default {
        group1 {
            psels = <NRF_PSEL(UART_TX, 0, 6)>,
                    <NRF_PSEL(UART_RX, 0, 8)>;
        };
    };

    uart0_sleep: uart0_sleep {
        group1 {
            psels = <NRF_PSEL(UART_TX, 0, 6)>,
                    <NRF_PSEL(UART_RX, 0, 8)>;
            low-power-enable;
        };
    };
};

&uart0 {
    status = "okay";
    current-speed = <115200>;
    pinctrl-0 = <&uart0_default>;
    pinctrl-1 = <&uart0_sleep>;
    pinctrl-names = "default", "sleep";
};


```


## arquivo: /home/segodimo/zmkpromicro/config/west.yml

```text
manifest:
  defaults:
    revision: v0.2
  remotes:
    - name: zmkfirmware
      url-base: https://github.com/zmkfirmware
    # Additional modules containing boards/shields/custom code can be listed here as well
    # See https://docs.zephyrproject.org/3.2.0/develop/west/manifest.html#projects
  projects:
    - name: zmk
      remote: zmkfirmware
      import: app/west.yml
  self:
    path: config

```


## arquivo: /home/segodimo/zmkpromicro/config/include/zmk/led_debug.h

```c
#pragma once
#include <stdbool.h>
#include <zephyr/kernel.h>

// Inicializa o LED
void led_debug_init(void);

// Pisca o LED um número de vezes
void led_blink_pattern(uint8_t count, uint32_t delay_ms);

// Liga/desliga o LED diretamente
void led_set(bool state);

```


## arquivo: /home/segodimo/zmkpromicro/config/include/zmk/uart_move_mouse_right.h

```c
#pragma once

#include <zephyr/kernel.h>
#include <zmk/hid.h>

int uart_move_mouse_right(
    int8_t dx,
    int8_t dy,
    int8_t scroll_y,
    int8_t scroll_x,
    uint8_t buttons
);

```


## arquivo: /home/segodimo/zmkpromicro/config/include/zmk/split_mouse_service.h

```c
#pragma once

#include <zephyr/types.h>
#include <zephyr/sys/util.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * Envia um payload de mouse via BLE para o central.
 * Tamanho recomendado: 6 bytes.
 */
int split_mouse_notify(const uint8_t *data, uint8_t len);

#ifdef __cplusplus
}
#endif

```


## arquivo: /home/segodimo/zmkpromicro/config/include/zmk/uart_switch_left.h

```c
#ifndef ZMK_UART_SWITCH_H
#define ZMK_UART_SWITCH_H

#include <stdint.h>
#include <stdbool.h>

int uart_switch_simulate_left(uint8_t row, uint8_t col, bool pressed);

#endif

```


## arquivo: /home/segodimo/zmkpromicro/config/include/zmk/uart_move_mouse_left.h

```c
#pragma once

#include <zephyr/kernel.h>
#include <zmk/hid.h>

int uart_move_mouse_left(
    int8_t dx,
    int8_t dy,
    int8_t scroll_y,
    int8_t scroll_x,
    uint8_t buttons
);



```


## arquivo: /home/segodimo/zmkpromicro/config/include/zmk/uart_switch_right.h

```c
#ifndef ZMK_UART_SWITCH_H
#define ZMK_UART_SWITCH_H

#include <stdint.h>
#include <stdbool.h>

int uart_switch_simulate_right(uint8_t row, uint8_t col, bool pressed);

#endif

```


## arquivo: /home/segodimo/zmkpromicro/config/include/zmk/events/mouse_split_event.h

```c
#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>

struct zmk_mouse_split_event {
    zmk_event_t header;
    int8_t dx;
    int8_t dy;
    int8_t scroll_x;
    int8_t scroll_y;
    uint8_t buttons;
};

ZMK_EVENT_DECLARE(zmk_mouse_split_event);

```


## arquivo: /home/segodimo/zmkpromicro/config/src/CMakeLists.txt

```text
# Inclui diretórios de headers
zephyr_include_directories(${ZMK_CONFIG}/include)
zephyr_include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

# # Fonte comum (sempre incluída)
target_sources(app PRIVATE
  ${CMAKE_CURRENT_LIST_DIR}/mouse_split_event.c
  ${CMAKE_CURRENT_LIST_DIR}/led_debug.c
)

if(CONFIG_ZMK_SPLIT_ROLE_CENTRAL)
  # Central (lado esquerdo)
  target_sources(app PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/uart_receiver_left.c
    ${CMAKE_CURRENT_LIST_DIR}/uart_switch_left.c
    ${CMAKE_CURRENT_LIST_DIR}/uart_move_mouse_left.c
    ${CMAKE_CURRENT_LIST_DIR}/split_mouse_central.c
    # ${CMAKE_CURRENT_LIST_DIR}/mouse_listener.c
    # ${CMAKE_CURRENT_LIST_DIR}/test_mouse_l_led.c
    # ${CMAKE_CURRENT_LIST_DIR}/test_mouse_l.c
    # ${CMAKE_CURRENT_LIST_DIR}/mouse_state_listener.
  )
else()
  # Peripheral (lado direito)
  target_sources(app PRIVATE
    ${CMAKE_CURRENT_LIST_DIR}/uart_receiver_right.c
    ${CMAKE_CURRENT_LIST_DIR}/uart_switch_right.c
    ${CMAKE_CURRENT_LIST_DIR}/uart_move_mouse_right.c
    ${CMAKE_CURRENT_LIST_DIR}/split_mouse_service.c
    # ${CMAKE_CURRENT_LIST_DIR}/test_mouse_r.c
    # ${CMAKE_CURRENT_LIST_DIR}/split_mouse_tx.c
  )
endif()

```


## arquivo: /home/segodimo/zmkpromicro/config/src/split_mouse_central.c

```c
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/types.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/gatt.h>
#include <zephyr/bluetooth/conn.h>

// #include <zmk/led_debug.h>
#include <zmk/uart_move_mouse_left.h>

LOG_MODULE_REGISTER(split_mouse_central, CONFIG_ZMK_LOG_LEVEL);

/* UUIDs (iguais ao peripheral, versão 128-bit em uint64_t) */
static struct bt_uuid_128 split_mouse_service_uuid =
    BT_UUID_INIT_128(0xf0debc9a78563412ULL,
                     0x12efcdab90785634ULL);

static struct bt_uuid_128 split_mouse_data_uuid =
    BT_UUID_INIT_128(0x0fedcba987654321ULL,
                     0x21fedcba98765432ULL);

/* Discovery + Subscribe params */
static struct bt_gatt_discover_params discover_params;
static struct bt_gatt_subscribe_params subscribe_params;

/* Callback de notify (recebe payload do peripheral) */
static uint8_t split_mouse_notify_cb(struct bt_conn *conn,
                                     struct bt_gatt_subscribe_params *params,
                                     const void *data, uint16_t len)
{
    if (!data || len < 6) {
        return BT_GATT_ITER_CONTINUE;
    }

    const uint8_t *buf = data;

    /* Nosso tipo de pacote */
    if (buf[0] != 0x02) {
        return BT_GATT_ITER_CONTINUE;
    }

    int8_t dx        = (int8_t)buf[1];
    int8_t dy        = (int8_t)buf[2];
    int8_t scroll_y  = (int8_t)buf[3];
    int8_t scroll_x  = (int8_t)buf[4];
    uint8_t buttons  = buf[5];

    uart_move_mouse_left(dx, dy, scroll_y, scroll_x, buttons);

    // led_blink_pattern(1, 60);

    return BT_GATT_ITER_CONTINUE;
}

/* Descoberta da characteristic via UUID */
static uint8_t split_mouse_discover_func(struct bt_conn *conn,
                                         const struct bt_gatt_attr *attr,
                                         struct bt_gatt_discover_params *params)
{
    if (!attr) {
        // led_blink_pattern(3, 200);
        LOG_WRN("split_mouse: discovery finished (not found)");
        memset(params, 0, sizeof(*params));
        return BT_GATT_ITER_STOP;
    }


    if (!bt_uuid_cmp(params->uuid, &split_mouse_data_uuid.uuid)) {
        LOG_INF("split_mouse: characteristic found, handle=0x%x", attr->handle);

        // led_blink_pattern(2, 60);

        subscribe_params.notify      = split_mouse_notify_cb;
        subscribe_params.value       = BT_GATT_CCC_NOTIFY;
        subscribe_params.value_handle= attr->handle + 1; /* handle do VALUE */
        subscribe_params.ccc_handle  = attr->handle + 2; /* handle do CCC */
        subscribe_params.end_handle  = 0xffff;
        subscribe_params.disc_params = NULL;

        int rc = bt_gatt_subscribe(conn, &subscribe_params);

        // if (rc == 0) {
        //     led_blink_pattern(4, 60);  // subscribe OK
        // } else {
        //     led_blink_pattern(5, 200); // subscribe falhou!
        // }

        LOG_INF("split_mouse: subscribe rc=%d", rc);

        memset(params, 0, sizeof(*params));
        return BT_GATT_ITER_STOP;
    }

    return BT_GATT_ITER_CONTINUE;
}

static void split_mouse_start_discovery(struct bt_conn *conn)
{
    memset(&discover_params, 0, sizeof(discover_params));

    discover_params.uuid         = &split_mouse_data_uuid.uuid;
    discover_params.func         = split_mouse_discover_func;
    discover_params.start_handle = 0x0001;
    discover_params.end_handle   = 0xffff;
    discover_params.type         = BT_GATT_DISCOVER_CHARACTERISTIC;

    bt_gatt_discover(conn, &discover_params);
}

/* ---------- CORREÇÃO REAL: substituir lambda por função C ---------- */

static void split_mouse_connected(struct bt_conn *conn, uint8_t err)
{
    // led_blink_pattern(10, 40); // indica conexão BLE OK
    if (err == 0) {
        split_mouse_start_discovery(conn);
    }
}

/* Registro de callbacks BT */
static struct bt_conn_cb conn_callbacks = {
    .connected = split_mouse_connected,
};

/* Init automático no boot */
static int split_mouse_central_init(void)
{
    bt_conn_cb_register(&conn_callbacks);
    return 0;
}

SYS_INIT(split_mouse_central_init, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);

```


## arquivo: /home/segodimo/zmkpromicro/config/src/uart_move_mouse_right.c

```c
#include <zephyr/input/input.h>
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/device.h>

#include <zmk/uart_move_mouse_right.h>

#include <zmk/event_manager.h>
#include <zmk/events/mouse_split_event.h>

#include <zmk/split_mouse_service.h>
#include <zmk/led_debug.h>

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

int uart_move_mouse_right(int8_t dx,
                          int8_t dy,
                          int8_t scroll_y,
                          int8_t scroll_x,
                          uint8_t buttons) {

    LOG_DBG("uart_move_mouse_right: dx=%d dy=%d scroll_x=%d scroll_y=%d buttons=%d",
            dx, dy, scroll_x, scroll_y, buttons);

    uint8_t payload[6] = {
        0x02,
        (uint8_t)dx,
        (uint8_t)dy,
        (uint8_t)scroll_y,
        (uint8_t)scroll_x,
        buttons
    };

    split_mouse_notify(payload, sizeof(payload));

    // Opcional: indicar sucesso com uma tecla fake (para debug visual)
    // led_blink_pattern(1, 60);

    return 0;
}

```


## arquivo: /home/segodimo/zmkpromicro/config/src/uart_switch_left.c

```c
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

```


## arquivo: /home/segodimo/zmkpromicro/config/src/uart_receiver_right.c

```c
/* uart_receiver_right.c */
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/init.h>
#include <zephyr/logging/log.h>
#include <zmk/uart_switch_right.h>
#include <zmk/uart_move_mouse_right.h>

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
            uint8_t buttons;
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

        case EVT_MOUSE:
            uart_move_mouse_right(
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

```


## arquivo: /home/segodimo/zmkpromicro/config/src/uart_receiver_left.c

```c
/* uart_receiver_left.c */
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
            uart_move_mouse_left(
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

```


## arquivo: /home/segodimo/zmkpromicro/config/src/mouse_split_event.c

```c
#include <zephyr/kernel.h>
#include <zmk/event_manager.h>
#include <zmk/events/mouse_split_event.h>

ZMK_EVENT_IMPL(zmk_mouse_split_event);

```


## arquivo: /home/segodimo/zmkpromicro/config/src/split_mouse_service.c

```c
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/types.h>

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/gatt.h>

#include <zmk/split_mouse_service.h>
// #include <zmk/led_debug.h>

LOG_MODULE_REGISTER(split_mouse_svc, CONFIG_ZMK_LOG_LEVEL);

/*
 * UUID 128-bit custom para o serviço split mouse
 * Você pode alterar, mas mantenha fixo para os dois lados.
 */
#define BT_UUID_SPLIT_MOUSE_SERVICE_VAL \
    BT_UUID_128_ENCODE(0x12,0x34,0x56,0x78,0x90,0xab,0xcd, \
                       0xef,0x12,0x34,0x56,0x78,0x9a,0xbc,0xde,0xf0)

#define BT_UUID_SPLIT_MOUSE_DATA_VAL \
    BT_UUID_128_ENCODE(0x21,0x43,0x65,0x87,0x09,0xba,0xdc, \
                       0xfe,0x21,0x43,0x65,0x87,0xa9,0xcb,0xed,0x0f)

static struct bt_uuid_128 split_mouse_service_uuid =
    BT_UUID_INIT_128(0xf0debc9a78563412ULL,
                     0x12efcdab90785634ULL);

static struct bt_uuid_128 split_mouse_data_uuid =
    BT_UUID_INIT_128(0x0fedcba987654321ULL,
                     0x21fedcba98765432ULL);

/* O valor que vamos enviar (máximo 20 bytes para MTU de BLE) */
static uint8_t split_mouse_value[20];

/* Serviço GATT */
BT_GATT_SERVICE_DEFINE(split_mouse_svc,
    BT_GATT_PRIMARY_SERVICE(&split_mouse_service_uuid),

    /* Characteristic: write + notify */
    BT_GATT_CHARACTERISTIC(&split_mouse_data_uuid.uuid,
                           BT_GATT_CHRC_READ | BT_GATT_CHRC_NOTIFY,
                           BT_GATT_PERM_READ,
                           NULL, NULL, split_mouse_value),

    BT_GATT_CCC(NULL, BT_GATT_PERM_READ | BT_GATT_PERM_WRITE)
);

/* Função chamada pelo uart_move_mouse_right() */
int split_mouse_notify(const uint8_t *data, uint8_t len)
{
    if (len > sizeof(split_mouse_value)) {
        return -EINVAL;
    }

    memcpy(split_mouse_value, data, len);

    /* notify para todos os connections */
    int rc = bt_gatt_notify(NULL, &split_mouse_svc.attrs[2],
                            split_mouse_value, len);

    // if (rc == 0) {
    //     led_blink_pattern(1, 40);
    // }

    return rc;
}

```


## arquivo: /home/segodimo/zmkpromicro/config/src/uart_switch_right.c

```c
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

```


## arquivo: /home/segodimo/zmkpromicro/config/src/led_debug.c

```c
#include <zmk/led_debug.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(led_debug, CONFIG_ZMK_LOG_LEVEL);

// LED interno no P0.13 ou P0.15
#define LED_PORT   DT_NODELABEL(gpio0)
#define LED_PIN    15  // altere para 15 se quiser outro LED

static const struct device *port;

void led_debug_init(void) {
    port = DEVICE_DT_GET(LED_PORT);

    if (!device_is_ready(port)) {
        LOG_ERR("GPIO port not ready");
        return;
    }

    gpio_pin_configure(port, LED_PIN, GPIO_OUTPUT_ACTIVE);
    gpio_pin_set(port, LED_PIN, 0); // começa desligado

    LOG_INF("LED P0.%d initialized", LED_PIN);
}

void led_blink_pattern(uint8_t count, uint32_t delay_ms) {
    if (!port || !device_is_ready(port)) {
        LOG_ERR("LED port not initialized or not ready");
        return;
    }

    for (int i = 0; i < count; i++) {
        gpio_pin_set(port, LED_PIN, 1);
        k_msleep(delay_ms);
        gpio_pin_set(port, LED_PIN, 0);
        k_msleep(delay_ms);
    }
}

void led_set(bool state) {
    if (!port || !device_is_ready(port)) {
        LOG_ERR("LED port not initialized or not ready");
        return;
    }

    gpio_pin_set(port, LED_PIN, state ? 1 : 0);
}

// ✅ Inicialização automática no boot
static int led_debug_init_wrapper(const struct device *unused)
{
    ARG_UNUSED(unused);
    led_debug_init();
    return 0;
}

SYS_INIT(led_debug_init_wrapper, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);

```


## arquivo: /home/segodimo/zmkpromicro/config/src/uart_move_mouse_left.c

```c
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zmk/hid.h>
#include <zmk/endpoints.h>
#include <zmk/uart_move_mouse_left.h>

LOG_MODULE_DECLARE(zmk, CONFIG_ZMK_LOG_LEVEL);

int uart_move_mouse_left(int8_t dx,
                         int8_t dy,
                         int8_t scroll_y,
                         int8_t scroll_x,
                         uint8_t buttons) {

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

    return ret;
}

```


## arquivo: /home/segodimo/zmkpromicro/boards/shields/.gitkeep

```text

```


## arquivo: /home/segodimo/zmkpromicro/.git/index

```text
## arquivo: /home/segodimo/zmkpromicro/.git/index (latin-1)

```text
DIRC      h$P*÷³h$P*÷³ :Û  ¤  è  è   uazYTó.«S;~8V` .github/workflows/build.yml       hÛ#¶íùèhÛ#¶íùè 6>  ¤  è  è  }D
z2Ðùd@fÿñ÷ 	README.md h$P*÷³h$P*÷³ :Þ  ¤  è  è    æâ²ÑÖCK)®wZØÂäS boards/shields/.gitkeep   hí=¹ÓÛhí=¹ þ+ 6÷  ¤  è  è  ÀåºvÿÎÙ wÄV=è¸« 
build.yaml        hÔOúç9hÔOúç9 :  ¤  è  è  Cc¯Ò&¬>£Áu­åËþOÐ?] config/corne.keymap       i ¸¾ìi ¸bá : d  ¤  è  è  6fÏJ6èMÛÕM*; ;)vð5 config/corne_left.conf    iÔÊøGiÔÊøG :}*  ¤  è  è  r ]èæLÄàõ«xG>m
!y¼ config/corne_left.overlay i úª,¥Wi úª,¥W :|  ¤  è  è  îà¡ÌÁÉßîd"	 config/corne_right.conf   icÕÃúûicÕÃúû :}2  ¤  è  è  
4G¨LÈËIjðÿ¨GØð config/corne_right.overlay        i ù¿i ù¿ ¯¡ F\  ¤  è  è  
dV
ÕK<Jû¯
» -config/include/zmk/events/mouse_split_event.h     ißùì~ißùì~ @Å  ¤  è  è  #*p(ù
è[ôd³ÓV config/include/zmk/led_debug.h    iyiy @Ñ  ¤  è  è  7jx=|F$(t¯¿ÏæO (config/include/zmk/split_mouse_service.h  höä+ÎNÙhöä+ÎNÙ @ò  ¤  è  è   ºû+?mÆD-èÇÏë>äbý¡_% )config/include/zmk/uart_move_mouse_left.h hæ¦ó
hæ¦ÀA§ @Ò  ¤  è  è   ¹Ò¹Ò}æù3àù8öðAüLR *config/include/zmk/uart_move_mouse_right.h        hÖ ÌêùhÖ Ì¸' @lÐ  ¤  è  è   ®	KFæä;Û¦Å¬5%T %config/include/zmk/uart_switch_left.h     hÜP3ËýhÜP3Ëý @m  ¤  è  è   ¯zL²öÙËZ¹Þõ
Æ`qØ!Ç &config/include/zmk/uart_switch_right.h    iÔ5«@;iÔ5xbÙ @Ì  ¤  è  è  ¢ûÉlXg-\2M¡ùù© config/src/CMakeLists.txt i×¹"îêi×¹ &Îª @Í  ¤  è  è  ÕÔð=:¨öÒY)²<Á;µ[Î config/src/led_debug.c    i ù¢ô	i ù¢ ^Ëp @¿  ¤  è  è   SýfçïÕpyfÛ¼X config/src/mouse_split_event.c    iü9]âÿiü6È¤Ø @ä  ¤  è  è  (noKéÓí@Ùèê3$½[HÎ  config/src/split_mouse_central.c  i,õÄfi,õ_æý @î  ¤  è  è  wÃ	¼=§À[ýtÅ¡¥hf P  config/src/split_mouse_service.c  i ®ôØ~i ®ô	Z @o  ¤  è  è  '|ñ4ÚªÊ&ýQÂÕ'¼¬O !config/src/uart_move_mouse_left.c i,ø (i,ø ( @é  ¤  è  è  þõ$â8À«Â<ðÀ*¼FJÀè "config/src/uart_move_mouse_right.c        hæE¶#hæØ¾ @Ô  ¤  è  è  þÈ°Lª©ëI¿>Áyù÷l² config/src/uart_receiver_left.c   hèÊ^.r2ÂhèÊ^.r2Â @Ð  ¤  è  è  ±o§g¨é¨`Ja*+©üê!  config/src/uart_receiver_right.c  iü0SÂÁiü0SÂÁ @ç  ¤  è  è   Mi£yöRtçüdY config/src/uart_switch_left.c     i*?i'ÿ ¿ @m~  ¤  è  è  w(óÀU¦¹¨:ëîzÜÎéPD¨µ config/src/uart_switch_right.c    h89«(h89xK$ :  ¤  è  è  ÆÁ4«Øh&ævÁ­õó6  config/west.yml   h v:>h v:> :  ¤  è  è   %Â³V#jÌÜS.Ë	\?¬ zephyr/module.yml TREE  R 29 4
%yË×Qx¾"$ì»*±boards 1 1
UÉ¶gF¤H3{:Üm6ÑÅshields 1 0
ÕdÐ¼=ÙhÅ^7Ìm[^config 24 2
ºÉå¯#QæN¡TM@å>«src 11 0
¤Së©9Öþ§Ê$y$}÷Nâ2include 7 1
ÌãVÚ÷{å£xëCÅ$²B¼zmk 7 1
ê]¸
U¸¹:êk½Ò¸4¶òùevents 1 0
fÈÒÃÿJROâàzephyr 1 0
­ºòµ´-ÔykæqÜ#*H	.github 1 1
¦¼73a!êµÐ¡±[v\C;¹workflows 1 0
OæùE5HÎ/HoE
#åÛûöýWýÃÚö/ÑÚOìªé7
```


## arquivo: /home/segodimo/zmkpromicro/.git/FETCH_HEAD

```text
12561e3c001662dd416a2608a9db27c743cfaaab		branch 'master' of github.com:segodimor2d2/zmkpromicro

```


## arquivo: /home/segodimo/zmkpromicro/.git/COMMIT_EDITMSG

```text
mouse l e r funcionando primeira vez

```


## arquivo: /home/segodimo/zmkpromicro/.git/config

```text
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github.com:segodimor2d2/zmkpromicro.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master

```


## arquivo: /home/segodimo/zmkpromicro/.git/HEAD

```text
ref: refs/heads/master

```


## arquivo: /home/segodimo/zmkpromicro/.git/description

```text
Unnamed repository; edit this file 'description' to name the repository.

```


## arquivo: /home/segodimo/zmkpromicro/.git/ORIG_HEAD

```text
cbc4bd44b390ed77b23d1e464a33cef77f9e421a

```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/357a1485c2cbb82349b0e2725d35b86af8f539

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/357a1485c2cbb82349b0e2725d35b86af8f539 (latin-1)

```text
x+)JMU03µ`040031QpöMÌNõÉ,.)Ö+©(aÈhõáº÷üöLÓOÓ:¾ñUí4ÜìU_Z_TTZ¤ÌpcÖÖ}×DßÎ¾õkùµWÏn°ì@Q^\X¬ãäbÙíÅr.§WNéS¶¯íJYCì]%©Å%ñÅ©y)`UÅl¨ì`øu;È¢É=ìêãå' *GqOpâÂäo/êÎàðùº²ÆñPå`ssRÓJÎ>e¿üçòÐûvQ§ÿ~(
ød7YYQfzHÔ$­¦ÖÖsJ®¬ÚÛ¹°¬h;T]ibQI|n~Y* Ôäïß-Íl3¾þ[z>4ôgÔ|dE©É©e©E0õjuÌÞq
oÉ3×mð¿5ëÓ­7ó°ª9ieÚ5K£¾ºÖñuÿß}`I±&²âòÌäñb¬¾+¿µOj,yþgFãHGÁª^®ñ¹ç@è²+¬^¿«ºsîeË­PÃ«r³¡>DirFb^zj
0D÷-1pf{x§àÁ1Cå"MGÝhÊ``\8õgÉ£µºwÎw¾µÜ^|Ü¾Î <o
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/9a509067f71826a39847a572ad55c3b937343e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/9a509067f71826a39847a572ad55c3b937343e (latin-1)

```text
x+)JMU022g01 Ô²Ô¼bó]¦÷ªTö¦ÚwâªØÿof&&
¥E%ñ¹ùe©@¢´85>'5­D/á·ölûÜc.Su_?ÿÚîIÒßñª8te¦g´\Úy©öÙÏîzãÝÜ?-¾}püã¬¥¸<³$9fÁ<Î.o·g-sÔ[ß^vtò5¦ª!XTÃ¯òÙ4cÎ·§£vÞëüÊ{,¡ðâq ½Ze"
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/d023536032784f712739188177b9189adb830d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/d023536032784f712739188177b9189adb830d (latin-1)

```text
x±NÃ0ó§v
P@,\ûRYuìÈq*Áb¥Ð©m¤x&&!/Æ9´I(Blï¿ÿÿì»Åª^Àu|q2¼ÚV°±éÕåM|§%³¡y
vËíSóVÃ}½±³hÜèTN}V2¼ö'¡ÍKíÐÚ2w^X9GýK@íQl¢(Ú[Ýe3_äJ:yKbÏQ;Û¦uM]þ¾ãßô2ÃÛaVx¹±!¯»O(g¦,ðP#À¡5}·ÜbYL¼À¹äèÇø¬.¸g<ûy¸çÖ»dD@B á(êQÎRKGÏ,ï<ÊLäôK )+ó
ç¨`1$ ujzß ÌÀ ¦!¡8vÐ5PÞr@þç\Ùóã®ÖÍçÃËê{K6ÍÇn¹:Jnc#­õ£¥mI)çÎç¼
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/e46ef1d603ede97db0dfaf4edaf81231c082b1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f6/e46ef1d603ede97db0dfaf4edaf81231c082b1 (latin-1)

```text
xT=oÛ0íì_qvKjÈ¢N2a$(Ê@²v¢!?P»6ßÓ©C§þÿ±eË"ãõdÜ½{÷îÝQåf£Ñã§!ý®f=_,A"EÆsû\N­\.òèÝ²®BCð ZJjcÍBÛ¥æÛ9¬uöíëãø>×Lã/Ã¡Ùî?7ð²YAZ²/=e³ÂoâÊ,ÉA­kelªùÅU²Àh=ðWªà&¢
YMX 0­¯JlÜ§­"Ij¬¢^©óÉ#ëQ}?¡3[©¥<;+¹F§+d£¦}­£¯«ØèbÍÙýÿã(¦øK¦»°½v[çýy­ZêÎÒË
â'HS±dÚu$M,KÊ0x+-Ó:1ÑIï¼é=f.¸¡àÏÎn1t§(w%Î+¥ )ÌX][àhÔW]'Ç CC\d22EGEW©ßÛ±Ä4<Ô:¼yo*ûñvÃVÇ?¯ûåéì×Çßfù¡së»ÆéÆµï4æÜp¯{lAÂ9s3éÛO®YýiÝ	yp¸ü°j¿eÝzÿ½_øèÏè[ô}ÿ¶k¶@3|FÛÆL°<°&Ýitâô¶ÏÀD,ª&F·h3ÑÈÜ»¢6çq·"(ümìP
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c9/eeac788561283234420643582a6c770d4769f1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c9/eeac788561283234420643582a6c770d4769f1 (latin-1)

```text
xAÂ  =ó
> Ù] ÐÄ_àÝeÑ&"
ÒÿÛ/xÃ$·Z¡è0ºÆÈ³A+%ç
ÙÎ^b9Y0blj]>C#{Á%;d½ó;(¸8d'ÊL¨â6^­ë{Ûº¾Å*úügËKm×gËûÄ­^4zg8ÔG0 j·ûßÿK%ßÕÐh·Ò@êUËF,
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c9/a31db7731e44cba994899c76be86d476805ddd

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c9/a31db7731e44cba994899c76be86d476805ddd (latin-1)

```text
x}SËnÛ0ìY_±M@	Ø	zªk­£Fýì¤(z!(i-	¦E¢)E¿¦ÒëR ?«µÜáìîpèéÃÝýÇ»w4Eðù
³¸RÝ5ªÅm<tRBFQF]Zòu·j¶á)P§ß6k¶E,×\#bF1
3¤:?NÅÉ	|Á[lè®4ndYD1¥!éJª
ÁCé8ùÎ^'{ðF/Ï¥;0ÏÇOìçô3÷Ý\õèG\kÈ¸â ×\A-Ì­ÇuÌ¸I 4ÝhæI®1EÅß¥fr
F!+¢k¯àôÙd®UXÌ		¿ðÙ%>jÚðQãÉ
Ü÷¸m+ÐùêB¥ÐëÒ¿$ MJÐIFÿyF!	fNî·%5ÒgîÅÔ\±=ý	Ârpv ¬ê%íàZ^yÙ»ÿqÑ©ÉMóáöf»Vvm©ö¢Óíû§{VI¥!"ësa¢;­+íhKklÔ ¯uP_IGhìflSn[É7C_ÕmÈJÛ>Ð½Øúu±TuªN¢Úy®6ü¶ÜÇ'°R¦Ûc³ÑÅ8<A¹Úí³d9½Ðs
Ô¢C}Q¿ñòÅyw×µ­÷;ç^Ij/_¿.GñóËx>;CpÆïDðRt ñ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/66/cf4a36e84ddbd54d142a3b96203b1f2976f035

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/66/cf4a36e84ddbd54d142a3b96203b1f2976f035 (latin-1)

```text
xU¹nÛ@M­¯X(È¥nTPäJ&,Är)Àn¸°P¤ÂCó7F*©Ò¥åe/ËU¨Ø¹Þ¼y3ÜFÉ>_M¿¿Ã:)2*ö·é¶µ0òn}#Û´i-gý×µí¹ÆÐs½6
Écs!Å­Ãdã^úóÅ·/WÓOpéi\0(Á£J³òw»dÆZ{ß¥t7µU¿IÃ8÷!
nnuæ\{ÅfñhÔ%£V\geaÕäè.uf	^Õkmz|³<¹a·s[ã
}td®89±D[«ä
ôkÏKmLIWhúM?ÙtC¾~ù|
q¸mxº]`e@W@×~Í.»iÙ6ïhª
+ÆÞB$üTEà¢\hÞJÈÛ°Õìkuna
30­=t\Û£T8afôkS9À,CUh{s*Z}H`_þ
¨X\þ9ªèEå{ÎtzâÔ^ÝJmAl@÷q'¤ûFë_"üc¨~c 
ËJ¡Èü8HJO ¦
8¤jf>``Ôh<,<PNâí#:çûíaj[ÜC¤®è@§pp¯ô´à»$Î<-	®0lOÈNÖ­ålT`êæ>ü,ä*ÎéC?ü«ê2âÝùìC *ÝaAïÔáá1ý³ÚÝq;?K2¦ª`t<ÙOy¸KH5¤ÓêÐìÊ'xð·a0¤'
Í½Áð>J-((.H®¯¶^:É	Èr­YS£ÕNIcNÙç¯6>¯OZcjÜMËÁATë%®9ÓHÄ]\eíc¬Ý+$µc³KY±ÍÂ,W{¹0>9Ü«¸|N¯ëAÙH($>H«Møµÿ1©}ÈÈÔ¡¢Ý²×>ÖÝ½kØMÚ.íÃ.Lb?ÀÞÏ üQ­Õ$ßûÚ Ï}¨ÌðÖ
TôþËQ%Â
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/66/16148d8f1ec884d2c310ff4a87524fe2e01603

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/66/16148d8f1ec884d2c310ff4a87524fe2e01603 (latin-1)

```text
x+)JMU01g040031QÈÍ/-N/.ÈÉ,O-KÍ+ÑË`-ÎÒÆ{ÕÛÆ§¾ç÷z^Ý ê
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/98d8c9092d8eaea35cd09ffe203933df16ef59

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/98d8c9092d8eaea35cd09ffe203933df16ef59 (latin-1)

```text
x½ÑNÂ0½æ)NvAla3Q	(	¢^©1wK×d±¬µÝ$h|$Â³í:2Pom,§çïÙwþñú§ÑAÞ[ ]r¹ÌÁåFúç3shDá ×ÂK)Pç_3ãé_*£º=[×Ò~V£)	]ÅÛª=DÝ³\N`<¹­ë}[z·Ú"Ëi!¶Eâ¤dÅ vÂFOO"j:¡)ÝßÙÝô:¾]Ý>âù£¡'¿mÄÈëµ'Vò~g4ÜÊ5¨Q^ó­¨C5¢
<ÿh¨_¯QáoøÖqïXUAÒæñg²ñª;´ó"P15FÑñQ:CÜ¡ÉT³T?Ø"j(¬A{ù¬ÐþÛ½·çgu£"UIú¨}ÙÀNè.k(_	RdÚÓi=Â)
ôÜÆ×¸µ$ÈLÏk¬ç5]Réý
9yìÛ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/098a4b46e6849ce47f3bdba6c59390ac352554

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/098a4b46e6849ce47f3bdba6c59390ac352554 (latin-1)

```text
xmÌ1Â0açü,
EE(.qÑàr´ÍÄDýû¶àø=/|­-¬6ëfë
Yx^Îx/¯5Þ§úXa¥ôÈìéOQ}ç²!Ø'1ìeÙ~­
ÁM¨Æ¹i`ézLüÊ®BGVæyÌ[a(à;ºà
à)%2R¼a«>u=8
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/d1b4ec4696a6fb870d2447b35b6c006955791a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/d1b4ec4696a6fb870d2447b35b6c006955791a (latin-1)

```text
x­MnÛ0»Ö)8iã´@{ Cu
!NlÈNÝhq"¥D¹ùAÔU²ìZE*ºæ<ÎÇo¸UzËÞ}xûþÍ%U¦É4HÏ?Ô	drÆX÷d[$Úª´hÃ³Ç/W/¯/OOçhX_Í.çß¤éüzëåMÏác>O§§+	°]²LMÉBemí<ÿ<r%ÄMV7&svx]³U|mæî±³Ç?-õ¦kõP~R7Á'¬àUb9]ò6ìv¾õjl ].mç9-¢9{1Vd¸b¡âB3´ß4B·g¾­_
7._;4 ð%ý.)+FJ½ÃC^]l­$æî`j20I®°Bã! ´ÇÊ£\à¶Éa«pçÞÁ¨3eî`¯>&#dûqzÑ¾UGâïîÙ£ Å°£mFÖkQÒÿäÍÈ¼ÜE¸¾j(>ýÄQôò?ÐÇ¼°¾?nÎs/®;~èÛo±r¿°ÇBì«OÉ:v*áþ±(øTè8
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/bb5d0444dea1e8036f1c0de72925d9da13aaf5

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/bb5d0444dea1e8036f1c0de72925d9da13aaf5 (latin-1)

```text
x½]OÂ0½æW4»X$Ùb§(	Q`¼k:¨d±¬MÛÂ·§+¤.^Û­=çmÏs>r.rtÓ¹:eQ.âhßBvUTLVìVÜt½dk%*0JÍ¸FèáuöB¦ïÉù¢?ùgp:í^âB4\
ù¬ß¶{÷'ù¡ÞÚ_ ©9còèÏ?B>\lS)¶L¥¬¤9gáC±«±gÕ
oºê;ËJ)VTKÆVPÐ,»¾ÄØÄ7,Åà©;6¬¡È+PÃ_Ò
s±}¿£ENg9ôÂCr¶Ò~.ÅFRSØ{-ÂÃb³#ÖÒEöCpp| wSÃ£;4ßHÿi>þÑx8
8ÍHÍ@Á ¼ Ú¦´?M%:Å5Ñi »ÖEÇÃ6
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/a95f83eb5691faf59af978434c4f188fd07dab

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9e/a95f83eb5691faf59af978434c4f188fd07dab (latin-1)

```text
xSÛÓ0å9_1ZJUÓòvY¤eªí-^,76©Ç|©¶]íÇð-üc7)<893sf&©70MgO
UHÏ8¼<ðf»7PwÇs²}üWÜ(.!©ËR¨2Ã÷ ÎøN<@ýkë*óÔ8RëÇÃ[N(·n ï¸Â@ªhÉÍ/%ðÛìxm¤p$ºnÆ7>MëY­ç9ç×Ë«»<=ÔÕ®×·onäóê-	!ËüS¾]$P9§¼ Øý8?>]Ðþla´ä?BÿZÚ·µ7Þ9­ìHôÔ"pièÕó×ôlPí9ê¼|ÆíÃÙ2uð·¥Ð<ûY/6	SÇ§Ä¾òD²ÞÞPCACªÂ[§kq LÇë/àäÚ5ê­ æÀ%íf2a÷øÝÓí§×èI§ýùCA¬Nnm ØZGì±m,êÉÕNôÔ4\jÈÃÃê¸àZn¾}g¨²6BÈºFQKXMÜÊÛäîêæ}ò]7:¬°n
¡ç 5`}Á­ÅÖé|MÁñBRøB+ilnü'°õT+ÍØH¡*ÒPçðçOgcx>vuwÞ(^$Éw'ÔQè
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a5/38b91baddbcccabb9554e06cd55b92b8f75b65

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a5/38b91baddbcccabb9554e06cd55b92b8f75b65 (latin-1)

```text
x+)JMU047d01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õN¤üÄ¢bÐÛäÓÜxËV[ÝÉm5»(yÔÐÀÀÌÄD!©43'E¯217Ãsõ¢øÛÏ%c\.áp8z¥bLr~^Zf:wV«ó·\¿v#AÜËkDÿÇCT¥dT1¬Ýõië-u¯Tf7t=+¼£¬åÁ	 NÀC
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7a/4bd29132e25820df7214e079f8b19aac0ef709

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7a/4bd29132e25820df7214e079f8b19aac0ef709 (latin-1)

```text
x+)JMU043`040031QHÎ/ÊKÕKÎÏKcL7v¨=év÷c QyøÍÆØ_ÏFQZXÀ ß÷êVÎ~¯V9]ekùWMäEVV¢_ZXÉ¸G+"*­þâaEë
õÌ\µ
ªº<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 æB
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7a/4cb2989cf6d9cb5ab9de89f50dc66071d821c7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7a/4cb2989cf6d9cb5ab9de89f50dc66071d821c7 (latin-1)

```text
xmÌ1Â0açü,
EpE¸hEp9Úæbb"Éþ}ÛÁApü¾Æ«åD³õ,<Î'¼í/^ïÇêPb©ôÀìéOQ}ë²!Ø&1ìeÞí~­	Á¨¹©gi;LüÊ®ÂÈÏN¦yèk¡/à;Úà
à)%2³R¼a«>¹k=¬
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7a/29ccc6dca26eb8edca4d5711f34985a6659546

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7a/29ccc6dca26eb8edca4d5711f34985a6659546 (latin-1)

```text
x+)JMU04¶`040031Q(M,*ÏÍ/K¥Å©z5Âgn[[©ìþçZì}NSÏDV\\YVT=³ËÛíYË'õÖ·<a©jÕEé åU>fÌùvótÔÎ{_y%ÞP< vf=
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cc/11922883acc29c0be2a6bb76c030eb271da666

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cc/11922883acc29c0be2a6bb76c030eb271da666 (latin-1)

```text
x­½nÂ0;û),!Y@Q
UDøQºX&¾«IÚmA<R§>B_¬JPE`¨WßsÏ¹¯WXá~ÿþÎÂ^%ÇKÐß_à(©ÐòøC^1 eU¤ä ìÎþy2&îl:ò½ºÂiW¸ÁxHÜe§!YÌ;$^pèu»§ÈÂ#iÀHÛ
Ò\>Z|2ê Må4Q¢BóÏïiÆý¹ï-ÂÊd¾T
ÒTbmu#ä Ä×v5)çZÌ}/$ÁÌ7qMÖ`à;¦µ]È´¤	¶ÊõZd¢¼kÍÔª RX[¨³%°Ö&6çò(Gyà[ävzã:«Å¥	+áJC²Ö&Ó tÓâò|'gÝ»">ÉóNÐË%äúÿâ|ß¼æ×T\%qkqãOAfþßÕ-¨ñeÌ¬³~ ºÐG[
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cc/8912e356da9d12f77be5a378eb43c524b242bc

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cc/8912e356da9d12f77be5a378eb43c524b242bc (latin-1)

```text
x+)JMU06`01 ªÜlW±l;¸Bwì´z5+{ï¥"&Û>ý öÈ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cc/a2c606e16baf3f767d1db1ec2f49ccca18b3b3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cc/a2c606e16baf3f767d1db1ec2f49ccca18b3b3 (latin-1)

```text
x½ÝNÛ0Çw§8êE5P¢&¶Xé ¨-wãæÆ:´Gâ)öbø8NåtãvQÄöÿó;ÉÌ!Ë²÷oFð½Ø½4¼òÜíÃÃÏ¦4\ÃCIáúd±Û?Ï¦d`äÌÑâW÷wÚ#6T×é$Ú*¬OE5í»[~ééN¦_CgVú·?V0BÙ´~;ùïIdïh¨ÊÕZøü6¢Co¤y§e£²`3QGpømñ\-go1i²º!á`ï8Þ¦òîÚ/ZùÇ½ãÉVnAQ¼øn©à\unðüg@¤ò1QòëW4ü_ø®âß³Ö
m ÐÍ µaÖ¼ª£8/° Yöá]úø%)´ÃÒ5lG
W ó®¹íû=aàt£%5yñ¨ëDo´ÆÐ[zC,
kEëÒ3í&´`ËËáwe¤9(³ãMìxÔZ"ºOðÂ¼ãN2AEày½!vgöAÒÀ£¢ÞÍî¿RøgWóK5ÿ>#çó³ó`{×ø§_ÌN@%Ho*Jjl¡Ü
w,voØmÕÖà'$ý
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/64/05e5143219b2a97a7f5092aa15dff3c68ade3a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/64/05e5143219b2a97a7f5092aa15dff3c68ade3a (latin-1)

```text
xUÛnÓ@åÙ_1R_lH;´P E4¨¹©Ið²ÚÚÓzoZ¯Ó¤(_ÃÀ'ôÇØ];©ÝÔm¬hµ=sf<{rÄà¼;¶_ì±È
2áÃ-&þ7Yd"_üOÆßÃ9sñ	àø¸{<ÂàÁÉpÖÄ9F4¢×È·Ýå¤7L¸>áìÚÛ!!m¦¥1'úm;(÷¦ÊQ®Jx<W,Bt¦ç½ïäó¨?§eìæ3rÖý1èÉx4éM{£¡Éã¸q`©ö¼¬~¦rZÑlÂiÝý½ûÍ,`CB9æjº5RAsa3dáÒÌX$ pý¢ÿ6@>åRf÷nÃ±ghµe´d3æ¦,(×çg$LÄÄlÙV{wÄ+¤R"Nâ@<¶ª_®:ýébÙÃ¼ xËíq"	c!ùE#¼EÖÛ¥yRY¡+à6b2\FrG½|,bU×æ4ÈÊ¦µÙVC·BÙÔ£Â[Ê¾¼·¯òíªmèÐmºÀ¼ÌJ¢25²[ÅÃ¹®øÕIÅ¾È¦É¢0ÎÉõN®QV	¤h<\È8»ÊV~5Nìm©c¯©×bd£Ç
Î{ o.òÌúÃ(Â.Mì÷næÛicµMZq_r¤³|7N=BK!¤Ï"ìw{Ão~=Îkãí3
ºzCsµÎtr1®:R@×; u¾tzÃz7
Çßç´sÑÖã¼U8¿ÂI³@ÔC+YÄÊÈEc¢¥,Í9»ûç1 ¶*Z!äu*¡´Børr<Sièzo| ZK '°"0G
Ø D²HòÏ2çò~E"ÞPÞH¦cÛkÑÔ¼ÏÈôëy·sBNº§½a×ÜâE'ÇÝnJI~È¹Ã~¿ºJF¶üÉëøMªD
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/21/8d64a622bbd5aa1b831af892afe63decbb25c3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/21/8d64a622bbd5aa1b831af892afe63decbb25c3 (latin-1)

```text
xÎÁ
!@QÏT1
h`c´FaÐ]ì_[ðú|nµ;¬ú,L
:*$!Zd)#2çì=gõ¦Y^§Ä)l=°D_('k¬¤ A«É"%Eþh3ÜÚgUÝ"÷ÇÚ÷Jã´áV÷`Ð;k\ÔÖÚj­~õ÷×å©&É¦ñõ¾t¸ÏH´úKÌIÛ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/21/f2abfc1a4a62325b86dd551fe4f9170a904294

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/21/f2abfc1a4a62325b86dd551fe4f9170a904294 (latin-1)

```text
xAJ1E]çu%I®Dæ w®¤¦ú÷É¤=¿}·ÞãYo­N,s $XjØ"³f_²0Ç-1Âs¸Ø¶Y½ûÑïI!qR3YR$æÄ¹,¹\/>é¦¼:ÝçWôÑ÷AoÚ@/w\ûZ[?]ÖÛõöJAR	©øéÑ³÷î ÇßÄÿMw¯
sT£]Çü0Ôß£óN ³ûìK

```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/00/63bdacfdd91f461082b3933c517ec03027a74d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/00/63bdacfdd91f461082b3933c517ec03027a74d (latin-1)

```text
x}RKnÛ0ìZ§xMQ@.(Ë i²­¸B»ð'nF|¶XÓ¤CQí 	ºèA|±¢$[3oÞFB=ÀÅùÅ(r-¸!+UHôæ,>q!|ÝáºØêhZ¢8+®ÛPÈ¾ïðÕ2Â¥U¦.Pÿ.#¿Ù»h&ÚÌjç°ÆMsãXA6»Q%dÒÉ4oót¡7Þ¤òãî8zÜ'Yç2JC
ÏKL y5æJv«%ñ)|Á¢OA öx´4ºÊ=©ÂÒk¸Z§ÑC+vÙHñ9±vÒNÙ¦ÒãäÞÞd8%ñ,³Ä<{.M?'cÌ×È|Ð,¶¹úÌmí÷¤X^³ÍáÝºønm¿WÐ
óJîï)x¬~î_ 7¼4R LAn«ÔTÀj
(kN5|Kûe×JF3¬gcoMtáÜß¿nþÛFn
t[%á¼JÔÝ#UZy7:ÅÞ8ý>MGÃwÿÈ«ñ£eY?áv
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/00/8800e2bbc33c292939f7445fae9e0af845d0ed

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/00/8800e2bbc33c292939f7445fae9e0af845d0ed (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2Óîl¶([zí×Á³ßÔ]ÝoåQPZQYÄ°v×§­¶LÔ½RÝÐõ¬ð²' nTp
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/00/3c21a8b2c5efd6db1583df54aa7df10728f093

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/00/3c21a8b2c5efd6db1583df54aa7df10728f093 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^æ®Ê¨;¼Xô'oÝ5á¦Òü²Ô¢ÄJ®¯Çj§p|:³E÷^Ã¡e~ïç¦l@Q]5ùø,×>¯Vw¾0-Ìpnwµ0£ÿ°_0rÈN[Åóÿò¥¢MÉO& Bf^rNiJ*ÃÙ7F%®'_X­á>-¿ÄWøòâ¢dA U¡<µ{«z]?Gj]yjq^enCÇ±&Í«gÞÈàW{Vvpí×Ï|f  _
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/57/44e948dabdc3d1ee563343a89c41e1bccc6232

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/57/44e948dabdc3d1ee563343a89c41e1bccc6232 (latin-1)

```text
x½UÛNÛ@í3_1Ê¢(&í$ÜZ
HQAÚ¾Y{k¯»ks)åúý±Î®³	Ð"Eª{öìÌÙ39 
ß,<OJ%à~	è©*ý8ÅsVrsö³ØUÑwÆXhÞÁö§ññç½ñÊÙîÉi|ú­~owº6ºÏü¤¯¿ÝÙjáõ+ý9$µ@,¦íÃç?4çòÆ+ä
*s6ø}se«qÃU¬¬hyÅî:õ¤R
óÒÓbjí÷ï74	ó|³R;&lÑwV ¹õehc7ùît¡cqÄÃ0í5$¦ºy5MdV°Ó
ïKÏ òÝÅdÙú}g§Y3x[%ËæÍ
Ø?><wß~Ù÷v¶ ×¢I ÃJHiC*¹Áèµ­
ãM°	
CãL£ñÞÅ\Õ0Á¦óÞ·q¹¦k£ò¬ªdyP0ÅlÄ
ä×¨Ö8¯òË)ëdZ½UH.¥ÆÜq?²«®ªroìKe"¨xqxj¶ae	eÜµ×ñ%ÈªTÒ¼æý°«½ºH¥Ý>\kRËP±)µyi¤³[!å
y)­+°Üßûï0Í«¡oÍpÆJÅouS.Sôß¤$&7j%&§J~¯(&Øñ[â>4RõÓÝ£Íô?&ì6¸[.Á¬¸3>ú
?ë:>ã³ãçLSpÁúÂ`QÑàßI'BXØÃ`aÃ=ö°þ
³íÚ5×çReM+y­áMU÷Óã§³L;P;mGÎ
HPe¹5Éìö×â´¿A&UÁà÷¯æÍº Z[F-qÜ~	D B0j`cf5ô!ìC@BA8]B8pÂ
|ú3«Q QQTíÑÍÁh|ÚkfõÙÁØøt*M''ÝÞãL%
é¸D¹Çó¢*éj¼¶RÜ±IfóÌùÄâòNu-¼c§kk/M×À8ÆÑjÒ-2±UãoñZÐÑìz­ÔtS
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/75/617a825954f31a2eab17531c3b137e3856601f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/75/617a825954f31a2eab17531c3b137e3856601f (latin-1)

```text
x5ÌKÂ aÇ¬â. -j¢FÆ©qÓ@-\èêmM:ûç|Âx»Ãqã¸ÎYn×(máQïÜCÆ±i£|e©âã¤/m¯1ðÔB^ # bq È(Á×N«Hç¦Í Ó]¤ÿK=¯cÝy§ôÐ|¬9½·Íü _9u
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/db/c8ffb1e66f657c3d0d02d78cf57d62cb273b4e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/db/c8ffb1e66f657c3d0d02d78cf57d62cb273b4e (latin-1)

```text
x½ÝnÓ0Ç¹ÎSõ¢bS¢&H hÙ¤Ñ­Ò©íwãmnlì©L<OÁáã8URØ-QÄöÿó;É¥Ê!Ë²Ï&ð»Ä½²XmLað­)-ª²J"|/9Ü­6pûû-8xs²øú~gâN{ã:E{ó©¹áCwëw0?ÃÙüCßþíOq±e­ßNþs¹;ë²µ!¯aÞòFÖS,{iÞÕè¬·AhÒÂ	¼ý¸zÏ®×«ç4Û|!áÕÑi¼OäÝu _µò×G§³½ÜxéÝRY¨;D¿èñüg@¢ê!ÑêMÏ%þßWÜãV[óº¡¢ÔW¾µ6¢1«:±± º{¦¡ ¡aIJ'í°t
;Pd=/ÐÁyÅ·èc~byãhIm^<ê;1­)ÁJ#ÔVóºtE¡L»	-DâÆ2¡rÄ}ydn¼oCGDPQ÷ïI,ì1ît©Rô<owÌíLÁ=XÚ³¤¨¤÷³;¦¯ÞÀÅõò¿Y~^°ËåÅeo7ô§_-Î{&IÞ\ÜºB?úí8êÞ¸%Ú«}z Sù%
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/87/0c019d4484960a7a32d0f9649b4066fff1f79f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/87/0c019d4484960a7a32d0f9649b4066fff1f79f (latin-1)

```text
xQËnÓ@eí¯8Ô]´R/@bY­äJ°±nÆ7aÇcfÆ´ê¢X Øæüc\'"nðÂòãÌy.j³ÀË¯(X
7õ?úï©ÖÎSpckTÿ­e¥¡b¨~WéÁH*­´i¨td})@Ö[¶#u§Wªáf;ßYz-¬sn>º
Æ®Q
­qÚ÷;«
>f×É
wG|¼ WÚ3âÖ|#ÝÈñhÉt£êNÛªªtÝ¢ÒbÄûõìô^ñ4¿Jß>DÎªsAeÔø½ßþ t¦L³Ô+cÂs4wõåáO$àú¨ölæ©!%ÉEØòÝ(Â·ý7ï
z©¢Dös§·{êÚ6zÿÔÊÐÎMôðX¾ÐüåLB
ËH²Ð¿uÿï§÷q6¾NÊø}Q$ù¼|æãâC9IHTÊCþr_Ý>¬Ýê¼l/ÓQ­5'ÏåºMô*ÇùdYd6ïåax§Ù»ôf<¸à7)ß
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ca/3fa7ea09a755df403e5a19cbfdf07550f23e97

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ca/3fa7ea09a755df403e5a19cbfdf07550f23e97 (latin-1)

```text
xSÝnAözâ^t·ÒÖhª¤Û
Ö¨7a÷¡óCiOã·>/æå§ i"	0»gf¾ó¡PC8~õúÍ=.Sá2÷8ÉtmZ¢8Ì?;%¡F#.G5úÿ§^k8EiI6B½[ãCÁ&»ï³)WÛ'*Å8)3Ë,&iÎä³Ã¼²ÉPÓ61÷Ü¦y"ðÖ Ôj`ÐA:ÿñÒ üX¤*CíîEÒéÝ´ãä,n¶ý8$Ð*4»Wç­äkç2ñ[Úñ§¸Õ`/Ã[.:ë~ësÒì¶p|²~í÷_Æ_:^ÒëZ×­îU¨Õ}R%"ý:­Ó/!ôÅ(ð¹ó_ó
qÁ	Ó¬$NkW0°
x;x
SÅ3)³K{X(W%ð÷ è³iáÞRïÖb¬vÕi3éi4¦<I]0qQÑðÎ¡dÄÎÿKäÊ8¦Jæ¢ÙÿÅ¾eÂàÐGÌà.zðcÛ¨M<Á¦D¦¢xe×$¢I¢(aW¬ñÍ LP¤ÚgdmJäXªt¦¨EªEKvkû«ðváÎ¾Ø/KtõºzTÓeï/E´9ÁJrÌ$ãyæ
(gHÑ[&¨¢!ÄÙ;xf"J©Ë«V¢)
Û$RÎ$uÈ_´Roúpç8e*ÿ	 ¡ôä%?&V¬¦CÆ÷Ý·¸@éí,V{JÎ°U}R°TDwãÊ-©'·»S/­ÓêKÇú8"¡Ôà^@0nhRÍ'+Û\ÇWq?\8C§\oD^Ð,û­f¿Õ+ucûsfá'òÊY­VøîÑ-üùhËÆ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9a/039dbcd7aee759d0f05a10885a5dcdf4bab5f1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9a/039dbcd7aee759d0f05a10885a5dcdf4bab5f1 (latin-1)

```text
xT;nÛ@M­SÌ&ägiTÜ¼0X.
ØÍ¶ TDQc¤J*GÐÅ2Câ2J`,æûæÍÕ>ÇãwUS0e>/ÌÈ£©éÇðN'±fÛÆYÊÑäz+<¥Òê!áºÂ¨$ßæPÊéøË·Oð>s¥âpø	9ìÍ¶>ü¨`Q­î¾dÊ¥p»	¥iÃ¥Ì¥÷<º@DiðI9ÙÓ$j8EkÒµÏ#%Ûnç¤sÿÓov'ºîø»²#ÂGîIÐ.Ýá>¥fü^ø\§Êõïzðäñ¯]?OáYæ«Éö¼õÔZE$Ò,i ¦}K)h
¤D8u³@éßó`òµÏºtÞ 8pÑ41ãT
WËÝªx8<¦
XóþW
înµÏ¡õá÷²)Ú*¿ö¦ø«s»RÉ}B4Þq
ÔØØê¶qÑ6IðÈ±DÅÐ~ÐiÕÊl¡©órYµ¾¤¿ÙÅªÎ³ ³FÎ°ñ@36*Äk#ºäûíe03o 0HMß´e¥Sãi\Ü?f@ÀºìEUÖ¾gRÅâLé®¥¥}RÌ~µËá{c`gÊ=DûU¾üµLõù©7y!X)ý$?ÍóËö#îêÌòâ©)kXäuU£<°Ô±AoQ³«Ö×ÝjQ!vI§Ó¡Ý^á9¯
¹¬,i0îe5àÃ¨S>¡ ¤"¹I±¡]½ä)ºKÉÝÞf5èn"=|ÞppÛt|Ë:GçQkhKÝJî>ß1¸Eæ?Ò/Ì
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/85/0cd7751196467fb3042073c492514dfe85c6f5

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/85/0cd7751196467fb3042073c492514dfe85c6f5 (latin-1)

```text
x­VÍn7îyb\vÅúIqZ@HäV°$$½Ôr,1û+K|ì[ôC à7étÈ])ÚÈj
Ta±äçûæ#9£iM¡óü¤ýÃq!^ßa>_©¦LóÂï£ùÏÞ]àBø/&£ðqs*ÅøIÔÄ¦%<å3T»æ+Ãô­4á)9]A75¦:SÌvJ«Þ5Ä(Ài1#@³	ÿñ;te" 6HÞ¶Äüqjo$-v'ïúØËÁÚïI5ýÛð]ô>»WìêrÜô/G¾Ênfq ¾ýàÇÚê§à[càyDî¼Hþ|ø/2\AÎLö»H8cîiÃaIº`®üB¦æpëþì=Û	i17X¾áØ £
ÎÈØ\)ÔtâÊ­X¢cÄÜï´³ÿñÇÚ¤ã,6F»¯§¿unÏ3Ò0±±Ú É
,Éñõ+!Ä²Aë4« J4e¸K"V©pÎS:»LpÃÁ½~ª|­jGÛSëé6ÍÂÎÙÇºwìüêëü}ùyæ9×].Á2ÍÐÑ65¦ååÑþ¸f·+-û
Í12¡#Î+r;f34~°¤A¦ä×ª³¥]S\¶[9¾¾{W'd×¹ÔÀ]yðiÍzc,ákÖ«¢óÝn@;8k6yÍl/ø4iÄrnU!¿C~Çë#j£ÚgªGå©µCÔÞÔ±@úP@ÏzýÑûî`?Üs'7ºöûá^X¸CÂMÆ×Wûñ-ÞìpxÝ_ºýÑ~¸n~8¸óîõ`²îÄÂ}: 5^Äf?Ò©Eþ'Ò½WÛ±ke»ÉQÉ¿¨+rðqIgA­Æ*#T]m5sºJÂ·½g}u7MÉTRq)ïÙí\Æ¾ë([ÕÝçZ¹>nÀ3º¶åTà@ÿYlAÕ*5Ù&ßMj·Zëûí²¹`_ßõºoÙÛÞyÔówØ2)¨(´:/¨Á}IF×AýMZô£Dþà°c
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/85/2579cbd7510178be2290241cecbb08802a7fb1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/85/2579cbd7510178be2290241cecbb08802a7fb1 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg´ëäÓõÊÏ§´ù-ñuè}j·¢ *µ £²aí®O['l¨{¥2»¡ëYáe-N ÃÖTé
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/3b/6a2d3a15c118b6b4d608f5bb4a968ee3483db9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/3b/6a2d3a15c118b6b4d608f5bb4a968ee3483db9 (latin-1)

```text
x½UÍnÛFîÙO1ÐÁHÑ¢HJòOjÀHÄÐäF¬È±½ðËîv7§>@¢çÞ{ïäò
YRòJI Â¹ýfæÛùÛÒ3áäÁÄþûûã_ÿÀS]^ÈËÆ8?<=JÚB©M!Te°5ØØ$iV÷@O#L¦9^FÕ{Ë¿aF7ÕÐ°°²¨,ü
O~?}¼:>bÇéÙÛ>}?>è;õøißy|°¿hôñHZXÍ)ºÏO&ÈçQú6¨ô- K1Sø5ú|Mã«­EÝpÐzúZÜõZ¬1òØ
1ç£(»t	BÞiÍ¶z ýRè|wùîõ¡çpÄ:
sÛ-ù .*QK:"ó¾¬¤ÑgDqdè&ï1ÞUÉ&¯BØç'Ç/ÓÃ§gÇ¯ÒÇÏ_ìÃ` D­Ð®f!'\KJÐrQlM*¦qnÑÀôè7ÅJÕ%¥óÞ/=âfK×yE¥M-¸9*A­Ã¹J
f(oÐlgpÑÔ¥0ÎÈ¼ ©ë²+m±ôÃûâºo2á¸Ú°§
¬®ÐÎÅÎ­n £ûòÖ¿ÝÔF»·¼?ìsÛº5Eé0ÌAZKÑbÊ
Q!¥¶¬5Í©B.
ÊZ;µk2Ü÷õ/çé;Dà2\ÚÈw^ts©sØnVÎA¦Udô-Zª¢xfô
å°@b&ä;âD©úIÇHV(äCIîûåíÂ#¿`¦/ßÀm	O§éùÉ7çLWpÑÎÚ`]Éèû¼(Rl¾D¼>µ-Ö¶0^ÛÂdm;?`aùr}R»ö®Ó®àªí§¯³¸¨$Þ
HÐ¥Iì÷×â¼¿AgM%àÿK4ë¢d{;,Ð4Øðâ'h@4hÑ¨5¢Ý¥Ý8xqqqñhywñâw!	!.í&$1$	Pµ'cðxt£ñé®­¯Æ._N¥ùä¤ûQÉ:x©Ãn:nÐDÈ²jjºo\(îylX]Ý¾÷Ütí`ËÅÒµ 0-tcqh]}}a
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/3b/ad673b4295d46a00d139131fe0546a33436d47

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/3b/ad673b4295d46a00d139131fe0546a33436d47 (latin-1)

```text
x+)JMU030e040031QpöMÌNõÉ,.)Ö+©(aÈ_¬¯Öüõ¯Å-#¶×oæ«E»~{U_Z_TTZ¤ÌðéyóV­ùµ½²Ìñ5¦éY8gÿ¢¼¸$±$YÇ
;c5'äª^e<¤¾4´¡éÊJ%©Å%ñÅ©y)`¦é®»gwÄCWG4lÕÅ°>ýO9³P£¸G%ñ"cú­Áò.NÉÞ25¥+¡ÊÁææ¤¦ ýrÖü\7OÃßÝlúxªwgÖ{?deEé ug#Ný-.¸ÿiöL!cµ¹Û?¤ª+M,*ÏÍ/K pÜàâý»¥ùmÆ×KÏ¾ò¬£(595³,µ¦^­Ù;NáÍ2yæàº
þ·f}ºõfVõ0'Ýyüy¿ÎÝWV¥(¨Íã,NãAÖP\Y3^Õ7sqå·ö	A%ÏÿÌh9jáå{.Û¹Âêõ»ª;ç^¸¬Ø
U^
õ)$J3óÒSSte^4»ebToîõn_O¯¹|væg púZ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f0/dc2f8cdf2326c315c4ee04680c12942730f732

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f0/dc2f8cdf2326c315c4ee04680c12942730f732 (latin-1)

```text
xµÛrÚF´Ï|ÅL=«K3v6²ÃC8©ÃÐ!- A.$ãéôSòc=g/ºã¸Õx,±çì¹ßvg7#/_>ñKã?¤>3}Ç|êÛex`ßü
~üãÀ¾];öÜ6
Ë kÃ7í¯iH\ÜzQÀÈ³Få©íNd1òæ[/·~Ãbw¶ÉoK@>r
È¸ÁvírÀù.sJ÷8Þba»¼sðÛU¹ÖÚ©"hi[ÅEvÇÜÞ®±`~\ýv»¢\kFÈ¨¹4ÜÕ´¢À5øjæRlQé
.èÕ sÝÓéP¿èÆú°Vâ  bOÿ¨÷h·^?®TÀS×íáÃ¢ÍQ Û$¦ç!	B?2Ã*h¢/É	éè»g:íé>®Á«?èè½ö©Þã¼uIl¯½ H®¿Çýj±¹í2¢ÓKýætÐvHsÓlU¦ WëNàÈ!õ4Ï/$NDdäÌ¢¹°É¤õjz¬ A!  z3e53CfQ¹i4#ÏÒ.ÜÂ­<Â!|¿WPb%Û5;ë®í¹ñ$±	ðQ}ï«Ø%é9åµÏY	ð¬Ø6ùYÊNZÏÚ$xÈP-§¶§Ó÷>ÌLb|¡çÒ¹c,0ø$ìïE÷ÇøC_ÛNÊ
A:0)ÄuL?\ë×:u?C.t/ÞÉóÃÊ%½]| ý¼Û×EfÈd_Ë5¨Hß7¯ítm]ã·F^¨x_úÌ°Àµ¹B/éøÝPowèhÜ>»ÌÁqÿVóIÈüb¬h(ÈñPßÔ2BCìÃÜy¶%ª­6/À5|fhD|ÌÔY¯|ç¹S[­@þui;ÔZõTèBÁBã-XXÛKå_äÉ =.F.éù`Þ¢>¢Ç9²C¢¤yôt8·#	ÎVCè'¥ó®eðW°l8´Ò Cr=)Fþ P9"sÃ	XhÕ3pX¥âõí(eRÜ!$ÆCÜ@
(_Âu>¾¬
¬y¢Ö6µ-ÁR¹ÃUË»wäe;Ê$9c!W³ ûÓª~¾º)8lwG:ÄO¹½Õûx7´#rÂlaGü4ì×ª:vgÊ| ­oÉLÛòÈ¯ÍÃMUMÅhV$éá,ÇûÊ=¯ZgãÌ°ð>t­$oÍÚÒYe-LE>O~½ªSBöð^÷¡ivj	j6yÊÌí¹³aÕ8ñ=S#ÚoI3{öÔr}'ÙÛ#&y_v;Êü¡íF²×á
 _øé½!5h2uYwãî]Ï!<ûûS©:r¸'R1è_}8¬UOÅìàÁ8w è,4\Ë«æ¨8- yõìßÿÑ''ä0¯µ²¯gèz)y|d[*Ú«cB
2i·§D¦¨Ó	Ô¹éDV3ø¿
¢Ûiì/¤'-ºK^À-ÇëÖf:±¶Ó¨7êãÏ)8'à'rë`Í8tÂs÷ão'rs#S9	¦Ö4çwÔ8a^0)ârú)5r	^1JRr¹QB2ó-'ÔùÂÀwB\¤[Ì=§±Ö:×ºp`CØþ~ª¢büuÂejÃèPõ¤ÔÄ%¥x#ÔÄE­û´sìæ3¥_ìj(6ëánHqS~Ö«Ù¦¢¤Ã·G{0YÝpwÎ;ÿGÄdìù
¼ù¤Æ)øªÎÒ(¶zÐbnHÚÛ£J
¶Ë9Oeæ 9	
e'ýüAl5m¥xÛ*R»Ù]¨¸jb69áwõÄr»·lÞ­£Ø¬&+0vÄ,ç¼º93qö*n~³U~³Ã2.ÁÃ³Ô¿òjá
<¬£Çúú©Ýçj.ÃbW¦óöÍ©6f¸Å¨=F±ç$þILá%ÏsÉÐ½Ú¢x¹ÄO[j4CÅ[jÃÍL[[y'÷'!'QÒW1®f]éñLù®pTOt¶ÿrÐ¤ñìGaÀIñÔÄIé_÷zÒ1CkÌÚ8< Ôa XÈä¹¯p(|ÒÛL<©ØÊñÈ>8lS{ëå,KVêÄ+Êü/åý»Fx0M¢£¡'àf¬Våä³>qÂ«0Ïeè°¾<©CÆÝvÒ`Ã¢®@~Æ&F7#¦;®È\¦Æä5Ò~ÿ¾×=k»¾FÎýóîM­qôý°;vÇ7Àç_GIç
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f4/31745a6586b782228d5ddc9be401b764d6f29f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f4/31745a6586b782228d5ddc9be401b764d6f29f (latin-1)

```text
x}ÝnÓ0Ç¹ÎS2UrPXÇ¸`ê¨¬¡ª¶SaàÆrÓÖjÇéh¡ÄSðbØq²*-sþçów²HÄÞ\\¾{qÆ³()cÞóõN¶7(3LÎ×ï)«ÏVmýþOO7:n²üÔ¾À5Ûr!OIE®¢µp6¢Ùð.è0¸óìÓ×³é§ñ~ÜPã÷Aèu§Ý»!)D¬T°lQò%ÿ^"hHñ ½\Á/íxú\dz^&àÏï,æBÌ eJò=Ø!³<C0%o¯Á-½}Ï¦&§o³BJ©·TyÆìUµ<]jãh¦¤OË)¬â®¨*Ib>t!ÈuÆüt@?CÂv(¡ÝG³)¹(¸â"ÓÒ³kf&]$²BA¡d)Ði³"ºàH¶WÍ¥_é
]¡¢Ueòø©þcf7¦_yYgjF1v³Ä`>'îT@S) ­ØoÅë[*¡ÓÄHT¥Ìàu0ÞBk?Ø2ÏBqzöì×4Mºó¥m½j·²¡l®þªxbi®IohoxÖéÐL®êµ×?xy¶lèzvßö§ùÕ[·ÓJÃ#âý@Ð*àTZ±¦UÁp««p%&È
<©±¢ªÖ4õ«ë¿ìJZ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f4/e3fac6c0b0407f1349918cee1f87d5ca02f5d4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f4/e3fac6c0b0407f1349918cee1f87d5ca02f5d4 (latin-1)

```text
xÎAnÄ @Ñ®9/ÐÊÁ$`i4ê	ºïÒABDÈý;WèöKOú©·V'X·|Ì¡
! ª1%Ëwn-¢¬(%¸5£fsÈÐ}BI¾¸\8Dè3m¥HK¤²9M$6YkäÏ>à·_~¤)ÜN}ô\[ÿ~4©¯¯ÔÛ¿2;ö´Á'¢y×÷ßÔÿKåTzN¨ûqM8tÔã©C^Ðúuªùy¨MÇ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f1/09f3a539728b5f1e535e7279e3d2180c993324

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f1/09f3a539728b5f1e535e7279e3d2180c993324 (latin-1)

```text
xµÛrÚF´Ï|ÅÆzDL
8fì¸ldÂ@qR¡;BZ`Y"º8?¦ÓOÉõ½èpÜj<ØsöÜo»S×/?ÕØ
"0ñ;ÐÏÑ¡M~!ð+üþOB~»rùÛcX{ÑkÏ'·~2ò¬^yÊ=ÛFÞ|e«Å&¨;ìÛìpñ[	(@Na"p,ð[ºÇõçsîÍëð.Àouæ9+¤·Aîl/~½]R¡
#+bÔ^XÞ 
Û_xd/å@áJoÐ¡ïíëIf§{52Fk{æG³G»ýêI¥î¸n
GDZ
pØ¾F$Ø¨¤#§¤m~ì´=¢sdÀ«?h½ÖÙ¼UEÄW~$»c^äç9lÆ=FÌ#ziÞ
ZÃ6i¬ÍÊÓäÝàúÊ$ð äHzÏf,§¢Æ*<¦ñLÚdÜ|59Ñ  P½²õÙs¨Ë¼,
ÇDD1Ä`Nea¡Ü1ú­k$,Ú¬Ø\÷¸ï)ÄStä&\ÀGoü/r\N¶ïVCæ¤À{²dôg);e=gâ!C½ÙYíÀw]ú °@0ñiE¾Gg®5Ádòg²¿i.îO*ð¾¸ànÆ
a60)ÄuD?\×&½êþ	¹Ðí¼çGKúîªó¶Ínß!=sÎ?K×Õ ì|eþÌØéÚjMÞ65òBÇû"`®µì%ÊxIGof«M¯F­óËGóo6Ê?%ÆF5ùM+²ä.0ÌÏYRU°	|	6ðU#òcª?ìjåÈÚÊlúèô/î2b4«ÐÆ³ÈØÏäAÖ¢ûB¢¹¤!xgBzøÈ"Fs¨dDÉò°-(öÙ"qlG­*Ð4bK§è'Fq%ÈCH«Ú`H®À*ÅÈï
#Çdf¹!ËÑ-£~¦ËâR¢¾gL;CÒdÁxH¨åKºNÓÇ÷¡³u©£è#°°­Å¡³)bmJ°tnpõòîEÔ2ITÎX¨Õ<Èþ¬ªÅCFwØ¢©ÜúÂ}B»Q>¢°?~ö=Sö*ÐÌæL~n­÷jÊÌÍ¨üçx_¹5ìÜrÝ)ÑuÓf±=U!\Ú¡OëA(¥@ç²î¶§5ìÐë>´Ð¶¢æZ$ÐÏ|Ç,ÇÄ÷íDÿ4²ÈgÄ(tQh£dØä	|­[­,:*òGÜUçÃ0¾ðÙ¦÷Ðrªª
'½¼Z$@Æ9y&LJuäpO$f!WÐ¿æphìÉIÂ¹pæBA Ð9Ydy¿W íÙÉëg×ð áøþ8=%GE­µ½Du7A×Ó\a,â#ÛRÑ^R¯q«5ã\2C=¡êMÆª¶Á/øeßN!=eÑ]¢röh9^oÉá¬'cg3Ëªq£?þ£q^ ×vUL²GPhî¾ÿíDn¬U*§ÁÔüç"ÂæF\Î>¥F.ÁÛ¤£BnÄ|+ÈUk|-:!)Ê­ÛÌü@¤á kÀëM	]8£!ìà È UÑ1Cþ:2ÊHå0#T?5q	c)Ùu$õÇ¶VÈ}RÆ9qó¹Ö/q5ëÕ©t7¤¸­>«{ù£¥Ã·§öaòºáîwþÉÙóóxóÉWð;51T¬Qlý ?ä¶·GljºÊ19* rÊNûùØzöÊ*ñ¢°#S¤v)²»P	-ôü¤lr*®ª©åv+¥6oØ¼[G¹YÏY`ìyÎEuSsæ6ã$¶½ùeÁVÅÍz(Ë¹ÒJñ*f0¯÷ê@°s èè§VwT¨¹~H'].Ú·8
B¦r8Ú7ûp>m¸ß±¶;xAâ¤hIáÉ~Y²Å<mùÛ,÷Iâì¥G3Tì¼c¡î!`ÚÚ¨¼MÉ
9É½ñ|43ìÊ'`ª8ð¤{b¢ãÁgj«A&³'Ã³&OzÜ¬þu¯§üP	ÖyÖÔe#BM©
EL·¨Oö¨'[c2àmfoµ¼pUÉÊ¥R¹ÿ¥¼­SÓ¨hè	¸'3öù¼aàp1æ{=ÖWçvÈØ²NnÂí°(¡+¤± «+¦;R®ÈÝ&äk¤õþ}¯{Þuý9ô/ºY$èûaw0ìnÏ¿¬GÌ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f1/77c96b6d37ecb70f289875feba24f49224c229

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f1/77c96b6d37ecb70f289875feba24f49224c229 (latin-1)

```text
x+)JMU0´4`040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ P\ÌÐ+Ê9ëÎÆÜx¹îòJí>ëí¡f§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  øQD
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7e/d9e3eacef233a8098777332f53e141bcf617d0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7e/d9e3eacef233a8098777332f53e141bcf617d0 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgØ¾ì³Â.K¢®ÿùôSgÆÏtªÔÊ"µ»>m°e¢îÊì®gwµ<8V
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7e/513f425e973a43e951c864f84e4b635585d5bc

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7e/513f425e973a43e951c864f84e4b635585d5bc (latin-1)

```text
xUMo@íÙ¿b_RÉU6rñÃÚA±-K¤ä²Âf bpù°þ¨§zê­WþXgÀ%n|ØùzóæÍ°N²5\\]^¼Ã*«
*
×®3·ò~u#=×ví,¦OúëÊ
|OcÐ\¯mKræ¹\Hqç1Ù9¡æ!¤|þõóÕå'8.Ô/Â^åEý3M¶ke¼ïSúÛÆR/Baá0ÎOHÛ·Ì9q@D¾»dÓt4êQ+¾·´Å°æIrt&soêºNM¾YªÜ°»kð
R4D=uüHuàÏ¤ÅnmI_æM,¦eJÃ\
îw­ÀÓ3¬	èèx¦ñ¡e¶[ Ñö=
´Ã³tiâñR>/bÀD87¥KvËÓ/}Ô©ñ`0Û»CÇk1JÃe^²Ì°yæX& õû_=e¼!mý;ªV]iýk¯Wrf2§öÚ.Pesbc@ ê[ÇEÓ$Éw2øYäBó-W¨TU¦QTz)«M\QQ£ñ°ð@3:*Ä«#:åûíaXj]=@¢¾hÃJ§ÆC8¸ôw´Û,-2¼G|a¹]MK'ó¤cPû¸á{¥ TiI§h9à_ÃTyïÏ¦OÄð"µSi¤ êo
|¯vOùGÕÔÂä¡JØEV <0U[ Û kTÙ¶~.ãM@!VfW?Ãc¸e4,6cÀÓ(}¶X  ¸ ¹IÑ¡·¦ÞFrÂr\AÁäÝì´fT ÛMòáÃÆáí5ëL»íx8f½Ä5g¸k¬:ÆÖ½AÒ:v»TTë".Jµ
kÓ]UÂJëø:r=(û*ÃÉÄGy³	?¶ß&M¢zTÔbw®ìÛîÞ-ì.mçîngiL`Pÿ)ã¤ÕjD×>4È³N ÞºÞÑ_ë$þ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7e/141047c584ab72648462af1ea231d2065f873f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7e/141047c584ab72648462af1ea231d2065f873f (latin-1)

```text
x+)JMU022g01 Ô²Ô¼b41Þ~¹-ü÷jòô@ÙÐÀÀÌÄD¡4±¨$>7¿,H§Æç¤¦èe0üÖm{Ìeªîãç_Û=Iú»0^¢ÌôK;/Õ>ûÙ]oü û§Å·|µg$gÀ,ÇÙåíö¬eÎzëÛËN°ÆT5jáU>fÌùvótÔÎ{_y%ÞP< ]c´
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391 (latin-1)

```text
xKÊÉOR0`  	°ð
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/19/bbf96fb46cb126070a2e8f861e554cdfdf3ded

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/19/bbf96fb46cb126070a2e8f861e554cdfdf3ded (latin-1)

```text
x+)JMU017c040031QpöMÌNõÉ,.)Ö+©(að7÷~ì}ù¨½ñÒ¾káéÜBUææ§Æ$¤Æç 5¤æ¥é%3,aê/Ò[>coGJ³´è¦½aP%©Å%ñ`m@uëßì·n¬/gæ½]ñ´`úyi£«ÜPu¥E ue©Åñ9©i%@5ÙÚLn­:Õ7WíïÀCWÕ÷¬ñÇ¡£(3=¤EãBlÛýÞS&\¯×Võ65¼ÚZ¬¥(595³,µfØ¿|Vµ®|=Ãsÿd»?¿çlÂªfAþòô3§½\Ðé%(¯¥½òÏ+Ed
Åå%ÉpãY}3W~kÔXòüÏÆ)Ó±¨^®ñ¹ç@è²+¬^¿«ºsîeË­PåU¹ÙÐÀD@rFb^zj
ÐËÞ
mÛ±ódnöò?úçmý qÆÕ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/19/6f8eeada6cbf4a8534249c8a76ad0fa916910d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/19/6f8eeada6cbf4a8534249c8a76ad0fa916910d (latin-1)

```text
xÅVërÚFíobë´4q±ÁnÓæ2Bj±$lÇ½¸d[cn¢7Nß¨OÑëùÎJ .uÆÉt9ûÝöÛÝo÷°êÆ]U.ï|RÜÎ©me'wQx}«§½gª´[ÚUÞM .Gpâ(ìÎâq4E¨D»íêyÁ{Áhý`Wa}«
þb.÷$õ³~ ^uÿ·cwúñ4|ñôãB7õÃÑõ´øÇð¶xÜMwnèÆâÏÕ»BÃ¡?I1ôÆÃÝA ^«-ä|®C¶^2^BúÁ?Äÿ.2CÅ®_ÍCZ~æGñ%*q}ªXTn ~ShXEàGj6ôUô¾ºúû¯iØóÕÄÄ4ýh=áíDKÖ7e¾×":üæu¬mZÒØüÒ,»Zì¦ð±ZÉïòt'Jðh¢Gß[J¬JxLlVÜ¶©îuNÓsl	2èvUâ!±F:¥ïuÎ#*6ñ%ñqènýÐtMâ)±B¥¦ÎùÊ±(h¹2Jrnh÷ªÖi È>sÜÓX-ÛqYÃ²vri¶Õ»Çmã¢B:!-¢CDÙ¿%¢Æ'fÔTZRmYÙ,·HuX%Qoöu"ª-Á¨v é]«Ù Ë=Á¿EuøºÎ&ñn­E
e`ó¸ÙÔ«©{´º¶°¡x2ÈâçcµÇnÛ0QpÊ,ð´#Ø±h²jR	iSUúÁø÷ ÿÙà6|,i¶ÇX"ûÄ".úÒ×ÄÄo»YU<Óv`òöÄáeâ>ñ (l2§zÖ½Ó:5r^©Æ*ÉæIÀÙp³u9îÓW9¦­ÿb¼-ÔMîT¥^(¨øBAá
ê4Â!è\8-¼ÐÎ"1ìÒ0'b7Æ\âDT^®e+Ä,Üê¼PÊYEE6X86ªÇ89ptÒ9Z8òGÓ¤[fkê¥"|5¾4a&±¶ÿ+õ¼ÉìX=I¾ð¤|Ûå§åñ´_[VäãÃààý§dÇwÄ'ÄÏ?SÊ·OÏ³¼O_WÔé!"ÂW`ÄkâÄ?ËëS^rèÄwÄ÷[÷[²?ÓèW[ú¶}ýmÕÖÇó^¿­r;¬sÓæÅ14mê«ª-¤DDÛ1ñëÛe|R`5m|¡ßp=çÝ6ô'æ<G\òà¦¼Z%Æ*cdkÌÚl´:úq¶N:^¬]9k¬H"TÒ²æ§Ö2µWs¯êH.+´ÓªZÉömÌ®·Wqð¤'$B»ÑÖß#^Ã®rR.{#H¼~«Ó¹ÄÒi»¥Ðöxö¦³ë¯í pE Ö
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/bd/d306100ef595b19bc30d0ef1b441860652a371

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/bd/d306100ef595b19bc30d0ef1b441860652a371 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CE~ç¹DNuõOÅ*¢NM_ÒwSi~YjQNb%C××cµS8>Ù¢{¯ÁáÐ2¿÷sS6 ¨.ÊLÏ¼0ÇtïÔ2U}µ 3]1ïx,jaFÿa¿`å-¶çÿåKEL01 Ì¼äÒTOîÿt.M¶··Úµè£çLï«w­!*¾V´:½CÙsÃ£¢XÓY?¾ZB­+O-.Ñ«ÌÍaè8vÐ¤yõÌüjÏÊ®ýúÏ n$@
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/bd/98fdbc66880ccde252b12867e0f28de496b40d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/bd/98fdbc66880ccde252b12867e0f28de496b40d (latin-1)

```text
x+)JMU022a040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ SÊuöÑÖµ?«Mó_^8çziG'DEqQ2èõÈ)Q²Õ{Ü·tþµ·ëÓÚVZ\¢WÃÐqì Ióê72øÕ\ûõ3 3>aÙ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5b/1a03814b03b4b7f82b606b82f73b954614d595

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5b/1a03814b03b4b7f82b606b82f73b954614d595 (latin-1)

```text
xInÃ0 sÖ+ø¤µEÑôÞ#-ÓËT9¼¾þB¯Ì`¶VL.£õqvíäf.LÖqB$øäY¢[V¢£yp}@Ì1´æÅ®«g"bï$ìB,Åð1nÚáGßÜ>~åªKmúum\·÷¢í(zýd	á
-¢9éù7äÿ¦9¸¸ñ\·:xQèRêS`Wxµ;éGÝx_ÔüÙ&P
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a6/bc3733611621eab5d0a115b15b765c43043bb9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a6/bc3733611621eab5d0a115b15b765c43043bb9 (latin-1)

```text
x+)JMU06c01 òü¢ì´üòbÿg?]M=Îõé{ÈÍÎwåR~zã7 H
\
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/55/c9b61f671246a448331d7b3adc6d8536d119c5

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/55/c9b61f671246a448331d7b3adc6d8536d119c5 (latin-1)

```text
x+)JMU06a01 âÌÔb«)öØÞ1éh9ÛÁÜh±8 0)/
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/f16a042c4ce0cd18f472eb23253d1f16619a93

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/f16a042c4ce0cd18f472eb23253d1f16619a93 (latin-1)

```text
xmOÍJÄ0ö§Ø^"díÉÈ¼´ÒÐ$S©¸+>°/f¶öRÝa`øæû¦öTÃåÕÅÉjHÆbåbãÇáfC·M²ÇÑw·ÿ)OÖºheøÐK|ÇÈ:h,¦-2§±aØ^3ê<xÇzÂ§Rî×ÈÐ¡i1) )amÂ@@urÖðþ;9Á$L-e(=Êl	Þ¦,ùZ3´j·DÞë¥f^ÎÊqªGfY/%D9¢«Mõüªï«õãÝKuzô­3%~ îÐy
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/47fe2cd2933f3f5f3ab76aa2f149994bd5dd3b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/47fe2cd2933f3f5f3ab76aa2f149994bd5dd3b (latin-1)

```text
x+)JMU06`01 ªÜl)jO¸]Îúöï© ïÔºk·" üD
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/e783b52a9f7d8d1d035f7c3567e3040998c7f9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/e783b52a9f7d8d1d035f7c3567e3040998c7f9 (latin-1)

```text
xRïo0Ýgþk¦NP¥$ÚµËR)ki$R»UÓ¾X¾ 11(dêÿ>u?*Øw÷üîýÖY¾ówç¯^§2ÊJðaI­FYÇ©iõ§Wß~aR³-<FõKy°ïÊÅÈlÙ6/dæYp£ðÁ3º+ÃWhán4±:áê-VW_Â]áì6p
é.WËëù
û¶øÄ÷AèM'¨kñ¥­5NÅ3¦0Â´B7Êe¡¡4¸3¦áDpÍP¤{4QÒs~8`¾t®	áhÚó[hUF-ùFò¼æU¨K%á4/ïg¡ÑDÉ¶í¿9àÄ¬`
VäKhÄ[þ°H´íd¤Æ;S·Ó±>I÷E}È×½|©<ËØáTøs`°>ÏºÔÚ<ÀS·,FV~\[5&3Ø7ô¢­ãþâ({dãågv;ß.Vä	L2_^»ÙZæ*åð1àÌòÄnz,@Ôôï´÷öMÕ
wÇã·_ñ©Qnn³YêféXúA°<¼gþ7ÂÿÉºo<qñ@¾
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/ae2c6749d815c29f1e5cbdc22b291d8eb6db82

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f2/ae2c6749d815c29f1e5cbdc22b291d8eb6db82 (latin-1)

```text
x}SÛnÚ@í³¿b¤¼Ê
8I«¨¡q#.}èËÊxXaïZÞ5à´úýÂ~Ig
D@ZÈfçzÎÙiª¦àûW×ïMÐy*ËT©Íyâ	¤%Gh?c¾¨æéùâë¿®TÍçBÎô=ñgË&®PRåXÆs,Þpëf®´0BI¦Ml%XÎÛp'zì1º½þhÝc¸t£Á]¿Ç¾?>0ß°qã8Ä,"|ãñ
4
bÐ6E(éxyÁì»;¶»H(,òÀu
Æ7¼r)çR¨­Vÿ­ðÃz^|_ÀµghðÍÍ©¿:òW[¦,$åQz»
þ§ü÷¥æòTNS7+ebD&ÓÖP©Ö±4ÖªQr¨Õ¤·
uVJð#mÈÉhSçlÉöó9VpE$¶Ì-ûs­Ê"A²Y¢QÜl4îÖ½ïzEa7 ºÐ«g²Í´ªS"µÄó¾/y%°³çUã ÐI»,§È%+s{fs4î.èvÁ6¢}(b¡Ì	>m&üùõûUÿ~BÃLë¸àÈaZmÇGc©sUºb]½=$W´[ù"Â¥d~YÙa&$Æ>±©eÓ;Å ÇB(.¬ÀÝ¹øûõ¬µ´ÉlìÖ÷û-\/-·ëïÏøá©ÿèÁKBföY²L§¹ë·Z­ýp?°ñý0èÜ²Ûà®?NnÞ Ü¿uqåÕvV0<~SÛý¨Áí9o'xJ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8a/c0f37dca2100fff1faa7a9376e7e4c16db0995

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8a/c0f37dca2100fff1faa7a9376e7e4c16db0995 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg¸cìÆ"qneè­Ïª§ÖÉñþ~¢ *µ £²aí®O['l¨{¥2»¡ëYáe-N °óTå
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8a/7cca9c50c06fedfcce4d174793b304c2042e26

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8a/7cca9c50c06fedfcce4d174793b304c2042e26 (latin-1)

```text
x­WÍnÛFîYO1NRieÇN¢ ¬8DÉånäre-L¹4¤4>õÐç(zèøÅ:Ã?­(F	Úò@J»ó?óÍì:^à@Ç0øQøÌ]¯>óÅl6ïxèsï`öº¶µå··Â¿mâ·r_®<¢mVÇ¹9k¿*E»Í[[Êo°À÷ËêæwM»Ë¸l$nÅv(­ypÏñGÜòø4QR.¬£óëAß÷/Ì«I¬EO52îËÐötèoÍëï-âô?öõµZ³××æy¸mÀb1ã	ß=£Ç¿hµOö!Ï!¾<îX²f-¶"ÆL#­8®Ô ñð^0lB·ø¼X¤Ø2æè5c95Ð}vj??9:>ì´Ú×ÐýÆc,[m>e®í)5Ò;ßgkKû¶Sî2Ç>=y~|Ô9l·vÙÒnmg¶`hÏEÄ0ká
~«ØX(;´çQeô¨z,7ã²2ÂÒÿÛ^&lQ® ç+/¤éîÙçØì<~ ÅtZÈO[yí«ÖfJý%7rÊ°£­*ôþJ7²Ö¬Õ®4ÒP|§4TI¸
ÊµÔlë-÷¸_¯ýT¶GÛðå­Ã+8®CºGö\Æ¡Ozq6X&bËBMÌáuÿe"á¡|RuylN<.`8	ÂBQÂ¾°Y 9 mÈó«ñ	öº`,ö¿²"K»$ôtÓIºê$½õ)µ9'[¥De²ö&VlàyoJ;¬$CÕd,K¹!2²é·Tõ7Í]êà®tÈm(~áz& O~Pët<áßaéK@képläÛ»3Y$¨rªÃC,×6C2$"jo÷ÂNÚ¤ÙÜ%µÍ@Æ>û/p Òª*½¡AïïI*É(¬ÌûPúÝiP«p;À:´
0i ÆÊÏã¡öDÈÈ­`*|Í¸v±ïÖ(üs>¸Ô2 éy0Õ2ì×Úª^MF,`íå#Íìý×4£tx¦j#á6ëªïä9|[r¬T!?:Ìlßõx×X>]>Ñ¢¸ÿ:]ËkBµÍ¶Z®DRîÝY«¦½nuÿ]§bùÞÆs±sÞÐz½5MÌ·7;8cVê rªþàDkïàã¾»æÃÑÏjª|jua46YBF-CZÓAK&&²4ùÔXSw%nì¬jRIðv:i°e7×Ñû¢È{WDµ£r¦¶7â½µ°´yê+üBÿ»O]¬¨©¾ý¯!3ªpµyØ(³óU2ZUøà:P°Wö¾¼ÁdV?Ë©³Äë
äK[ý$j¥õ«dwòtw!:-¾2?õé½«hª¹S§tàä6V5© 
BQÚùè6¢Ø£õÜ¼ê>ÒäÝÙø¬<í½,094ra92òÿY1é´Û/¼ÇýÇ?Á¸6x¾2!xöÜÁi¸BÀ0<þM7¼û4¿ZN3Ô­¬ôLFIyil#²s c$|W0ÍÏdÉA?Ç&¡ålÁ|W}õC1¿Å&4#lÊÜ_SâÇc/ÙßºuZOü/UV±®×0}xö0}¼YÙ±æâq#Às98xëTÔRTÉ.vU©ób%dYaâ
µg&fNg`7¸º¹J®bU·ÇDg³w61GÃâ>©¬¥7¹Ë±9Ôñ¿Þí
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8a/f5c67d9408f2ccb42dde8040c2a64eef9d64b0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8a/f5c67d9408f2ccb42dde8040c2a64eef9d64b0 (latin-1)

```text
x½UÝNÛ0Þõâ¨ Æ¡--0$´1@ªFÅÚmwpâÌNñH{½Ø7s
Ó"->óïø,¹XB@WÝ<É¢Brxx
øT~³KZòb¯9µ
»¢Ì³ sÅ¸7pðáâ}8ûx<ÝX]ÌÃùø=mö
u5øEoî×ðÇj¤âå+fâðùÏu<\Üz¹¸eÒc]rö}A×hl¹ª¥­#nè}§:R²¬ðTÎX¬%dø¾Ä&ÌóõNel°5qF µý¦Ìø¶ùîô cpÈC3í[ÅÊu HsZ$¢æ}'ÂÓK^#ÒûWö _¡ïÔ{onIW|ÀÉìì<<z;?ût:×8]2®=-0=~ç8Z»'TaHõÍAZ§nÅ¨yú}8(D)9¤4g¨LVºÇS_K&caìÞ¨fþ¯ã«©Ë÷ô¦gQ(¥Lîêq"bæÅdQtà·ªù#Ç¹èP4Ì<¾é&wHq(·Ï¨>Æ£zµ«0
7ÓóÏð£ÊÉl1Ù_×f0·¶ m-ÿ¶àÈb=b§=Ö­-Z[ØmmaüÍR4fêRÈÔÖW/¼ ÊªûsÄ)5]X_§³à
(ÓÌ,pÙ-¸©[ñ ¢2§ðëg­[¿½ìÔhlÚp=×Eæ  /Ô `ØØÄô ¾(ÐQ>ÒØ%  C # »ÍÝ1	>þ¸!À¡aãÂnhÚöt#l_òpÉ®é·DH+àÓµàÏ'gÏ¡xû°ÕÇ [¾ev¢#Õ-N·²¡íºã:Ï½ß¶ì+J
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5d/412e78bc7d3f83cf0c4cee12d83875aac8b99b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5d/412e78bc7d3f83cf0c4cee12d83875aac8b99b (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CE~ç¹DNuõOÅ*¢NM_ÒwSi~YjQNb%C××cµS8>Ù¢{¯ÁáÐ2¿÷sS6 ¨.ÊLÏ¼0ÇtïÔ2U}µ 3]1ïx,jaFÿa¿`å-¶çÿåKEL01 Ì¼äÒTOîÿt.M¶··Úµè£çLï«w­!*
¯$l3õ^º à¯Í6w¯=â; Ö§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  Oµ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5d/3e7563b0cd3b30bb5386dc885bd36290305d52

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5d/3e7563b0cd3b30bb5386dc885bd36290305d52 (latin-1)

```text
xÎMj1@á¬}
] E²kJÉ	ºï*øGNâqðØôú+tûà[­e¶æ4º ¡&L1¸i§S¾¬"Ù$¿1[çò¢Þ¾Ëv@NÄ6dFËl­&âdí­ÚP
«vòs<Z6;|û*ð¹Ë½¥RÛõ^}y}ÄV¿ø²°%dg4ê¨ÇßÿKåsÓ÷qÛËÛÎPä¹ÅÒ6¯þ `=M 
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5d/bd22c8a7e352cb7d91a84e29f85d575e116be4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5d/bd22c8a7e352cb7d91a84e29f85d575e116be4 (latin-1)

```text
x+)JMU042c040031QpöMÌNõÉ,.)Ö+©(aØa¯whÿ7çöÍu³^åîÇ{úãYg¨ÊÒÄ¢ø¢ÔäÔÌ²Ô"½d«ÜyVö7©¶ozð¡÷õÆU¿g$g ~1,JmÛÞ¤Ô{göÆí)×>Í ÍG8`
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5e/107db7bca5bd3cb1c41d30d5353af1eb7581c0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5e/107db7bca5bd3cb1c41d30d5353af1eb7581c0 (latin-1)

```text
xUánâFîo?ÅH'Uú!@ÓÄ'µj êz=YëõV±½Ô^S¸ö¦êú¼Xgm 8¤¹C0ØÞÙo¾ùvìGÂÑé|ó'4Ê?|dËÅ&m<²4aÑùâv²ù'óþ?».7K©Ó­~3)\4WÏ8¬6æDÊ§±âÇF¶¸ôbgÌËXºâ=	N¼ùySsÆwÞp<97±îì©kMj0+ª9ÝÚwÞ/Ã<åïXS¿Ö´Æg0Ùh¶º¯}.æ1,IJ@@bû/2(©-nÿ¥@jI$YJRbá/,YùZìdADãæö*`!O¼u=ÛÞ;¶UÌ¦7µ&¶iy}~Õ ?{/DèY#s<°jÆºÙÒõEMçÍUMÏ@C|44ÐwU'cÍBôy6Á¢	Ð¨c·_ ;è»ý/!m51RûÍeM÷
ÑCã«dv§,ó	Juç"ªZYÆi&ä2æT/½<ç´Ý«êªX
ÃöÛþÈoh Äh\u;ífkæ8zá{S1ÉB¿gÞè«Äõup"É°!¨OzÝ«ËNû¢Õ|	K«YuÞaiÁV$)ü3¼E,YqB-Þþµæ±ÀþF²¬ÔíÐÊû­cÕfwÕä<]OVÅ¸9{ß2>'
¦êàª3s×w]µ¬.ÒX·öÈ:9¥ûV¾÷{Ø¼Ûï©}[9Óåh(h«ëZ±+4xh)F¡¾ßS.|<Ü($ªy{4æýIßÄq3Ã6«	M9WúÆJø/ÜÄÄ	ÔÀG)ðÙhìÚ·ï¾*Æ½51^ô©þCiY)Ú°§ã Ë4k¥ëþÉ!ÉÐâÙÏÛµêZ9á6O¶· ÀErªù¼b»ÃòùBÖ
 0*ª(Y¯Qdö²9SÌêÛ%uí¢-<ÞÂÈøG&Â<ÊÒêPº*âS&ó4×=ÂIy]øT*!f1]nN÷ëP&WIQ©*
f'bÞK#ð F%Gì{Ù¨òR
7j®¨··«¯$·*Ï=G4{ßüðb'+|5êpNQ¢RÞq\ºzÿùO½%fÁz­©CÛÀTI;vü¤ôZû¤ýÈeð
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e1/1c2e9b08bfb655e70b8eeccb8108e6549bba8b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e1/1c2e9b08bfb655e70b8eeccb8108e6549bba8b (latin-1)

```text
x+)JMU021g040031Q(M,*ÏÍ/K¥Å©ñ9©i%z¿µgÛçsªûâøù×vOþ.WÅ¡£(3=¤åÒÎKµÏ~v×?èæþiñíã d-Åå%É0æqvy»=kó¤Þúö²£'¬1U
Á¢fxÏ¦s¾Ý<µó^çWÞc	7CWåfCÝ^\XtãÂ©8K­Õ½s¾ó­åöâãöu^ _m 
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e1/0f0b80052e58074a12f32cbf832ab020ebf243

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e1/0f0b80052e58074a12f32cbf832ab020ebf243 (latin-1)

```text
xKnÃ0»Ö)x¤>¶AN}4M9,+°åûÇè
º|àI«µt°Þ~õ]X"G/d59Nè½zrÌ8Í#éÙ¼y×­jÀËOqÒ$9ÙÙ)å¬¢¸Ý@b
ýÕvømçO®
·C6ÚKå²þH«w 1¤@	Â7:DsÑë_×ÿ¦ëÑÖ²uÝ®þoðn×Wù ô¼N)
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/02a6cdebc5b34a89d18a543b099c8019882e26

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/02a6cdebc5b34a89d18a543b099c8019882e26 (latin-1)

```text
x}SënÚ0Þï<ÅY§UaÊ ögë¨ThZ¡r©¸TÓ¦É2¬&6¨xýÜsôÅvl£E$>×ï|þÎ4SøôùË×7ï¸Ò"fð}Åæ³eÞHepw}váíø³Ç+Ð$£&,?âVUöH2Y(F¦hFEÂâ£ñ	%sb9¯2¯;¸!½ÁÕ¤«°Ý½>6 =è_wnÈÏÞ-1!Ýð>ìÖÎ=Ïôçp¡ÁÒr¥`¹I¡4°n,
Ø¬OàÏ9ÎÈÅ¼0ÆÐªÈ}¬wnËñðß²²f¦~Ît0Ã{|Âþ´&­V7DØ& ÑvÎ)DÈw
xG1¥2HxþóH"ÜâE#^ÚÜØ·æ
KIL5½C³Øô¬4-ô¬üx/÷^Â:°×ÿèGEÈ-¦#ýmXé6-l¤íº(¾2ÌK>ø¯ORs¨ljP.b¶Àü³CÀrtþHåuNs4WXPË¢ùÒ?­J²²¾ð×Ùï Nw-Áí®±fôgáEÞÓGÛ.à+?ÿ&J`ZfF©4C6 Ô<åÚéÅÄ(dxÙ\íË¦Ñ|§íôÌÖÁøÇ7Có}ñÒü«(iJ¬¥ú¶ö©è>Ùhàî_¼À¦ÀÞiéNÓBk\¤
×t½ö<»¡Ñ8ìCÿ`%Ã-Åº&g4iÚÃÎÝ¸3è¿wd1ûÀ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/61330691c104cd15afa6221175e5676ad5e2d0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/61330691c104cd15afa6221175e5676ad5e2d0 (latin-1)

```text
xXënÛFÞßzSkHbËv/;ÎBµiW°"¹²nVð#jdMM
9tì~¢?èSøÅzÎ\È!E'YÂ0)ÎåÜ¾ó3ñ¾ývoïÛÏ côpqË?×¹ÀÀ_éão1q/ÅÁ³íÆ×"
ÂlÆáå¾ZÜ'Û7<x¸µxµ>4ã·"àõC		K·IvíêÀòFM÷Ó÷B£hÜ0¾¾Ñõ6ÞiïFxê¿_ö=äö.ÆÞ¨Ycthbß{ãõýÞà¤uÐh w.»£1hK É~ÉRÉ!åCÏxÈ¦<yÀLÌyÂ#É[ä¥T2)ô\JHeÒîñLK&/Ã!{ozG<öO½qoá±×ïþàõÑb,Vq
Í%O1¼Ë8JÏ¥öõÏEÄÁ{3öÏ¼·?»£cèÜuvîÈëáåxáÈ®2í1ZÃÓOØ,ÞIç®Û½ð[4Ä÷+~5Iâ÷W ¯&«§)á¯nÒly¯à;ÞK:Fg"ÿò%L³¹Ñäû«ëShDtJ£ünÅÉg~È#w
ÅÂ#WÊ,aèLPZÆÐ\1Ä.¡3Ê'mX²ØGx<Ñ6`ï2aB£¢¡¢ 
UG?6È;VýÂ	ú}$âÈÌ¡y&ªz½ Ë.F¯éUúu1¬0Þ-àß?kÅOÏîy$Ð¾vÓk«Ü4Y¬ye¥\¿x8hà_¿)1û?]zÑû/¦QïôÇ1ìí6Îü×§?ùÇÞIoàé¤Ò[¦×ïtøÚ<7	ëoµU=!¦
ßØ$X$ÍjgþøÇ×=ö/ÆÝ£³xL½àÆJÞéìÒbF_ê&úÙ1Éô*öçI ÞY
·"a
"Îæ"TTx&Oµ«Þ¤©±6è©}Z
OOzCKD-(fï"äÐÜi9È»ñs¯¹ln:Ît=¾©4jÃ2aôFäAÚ.ÍÐTs¶îì®!Ç¹|²/§-XÃÃ©Xf!Ü^GsµófEûÃ6ÿ$û0gaÊKû¡$Ñ^SËcxn¢Â²EÈ.h1ÊDÊH³UH|P-§,Û°`S
lÉ
lÄ«DÐ#Ó¦{U<²4ËBYK%ççÑ ¹¡Ü#±¥X5aò?;»wmãB'RµvZÙJÆ"ù#SL	]È^ Ad°RÔïÒvæ`jBY[¾°Z,#g$*q,¦-ÃÆéÝÑ©9À²sÜ,æ­4ó;6kªÝ76 â_AÇ¤CjS:°vÀæ&ð>aér§7Ð )¢ W9U®!E XèF½e¸.é%4T[ÈòÊÖª
ÌG&%M?ÇZ	è+á8b×Éi@K?þ]×¾#6,¼Î5)nc±iFÅKWÚÀäFÍ
íH>QuPb4rÙF5[Ê¾¥²L{Úë©ºlÇéû;_éxÍë¦Hª}	ÿÄJbWSò6>ª>0·¢E·&®¡ëÑ9<Ýj$ì,UÜ';èÿÃUçúµ&~§À3¡¾è:¢
8?¥â¡ÿSMF¥z=ÓaO´b÷a¬K$d¯Z¸Ñ ÆDÅ@D·¿H9®£íê¢*SéÈ0U4Õ¹3DUàçª/Ú­ºó³Bì½6(ÒÜu¨Ñ[M}ú)Ç yA®QÍ.:lr§¿3×^Rx¤!"î5h©F2§CÓ0¯[ªýg8j,t1|ü+á±	vÉÇ?Jb^ìáùKP¥¢n\µ´d¯½è,B\¥íàíeiMíxº£±çÏ«*Ó6¶¿ÿ:M¼À&Þ
¡»Ùô/D:.PãR~U'9GZ¾SÌý4Ú5üù5úJêNö²»µ¿@«²´C%ðU^¤)5&ªc
¹WZÅõ¹.iQÅÁé1ÚÁiæðw¤?êé]UØéWZó©Ön®$d·Vô~ØÜfï}r¶íõ\#¾©¬p¸U)ú#KöOó«²BQèÖì£ÁCk«ðÙÓæe÷µË¶K/3¯/Ö,«
³9Áb¦ó_e_ÒùþÏÝÞ¸BÃwÚ:¦§RPµê#ð£<«{Sü^mDµw¨`õ3)ó¹tqØ¢+¥t/>Pùô}H²lïI}¥¿Óø?.`7yo¾òÐ·R«÷IîÇ(&7ã*×8tUDªcÉ;?0µ÷¶>ödÌ¶>'Ù~º
Ë~ßÄ#ß%¹óñCÅ4äÎB£ÕTý Ü÷ÖN¬F{ò-åºÍûÊ©NòÃ-ÖYÛZ?ÑJabÎAWUú_+ûû6tè<Z RM£Hà·¶æÚ¾cêÒñ³Yqzßã©ºÕL÷ÓûtuvLtÔQ cs2jÃé;Û4FdàiYûâP¨¯¢X©£¿Ç©
|ñöÍèMËPµzµ¡{~ÞïuÇ½á 
GÃÁIïÔwÞ©-üóQo8êß¢"Qd
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/fa205d86df8dca340aebad7a8d8280eab35575

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/fa205d86df8dca340aebad7a8d8280eab35575 (latin-1)

```text
x­T]NÛ@î³O1	9ÔIªVJ8UG&TÐcÉ
Çv×òÚôUznÒtÖ?¡Ð¦RWJ¼öÌ~ûÍ7ßî8NÇÐzó®ýj'aEïïp>]'óLÿÍéãYüEñÆPN&<ØôÜ0ç!®f×vÅfiôIdO¦ê4yÃU8Ý²sGHô«0¤
²p$ÓÃp½¬ï»;qÝïnÁ±7èö>²ÏýS¦S\çã6
#L©@*
Jê°OO
íFxÅ~gä÷.Ø±çA«½ú¬¡NË~gÈÞYoÔó¦Ho,Ó¸¦7`ÿÉê×`ê`Ã0lºYòðãá{
AvËc" Lr=Ïf(ãÀÐ5òòG 1Ø5.Ì'ê-SPlX¿ß@£»RQòYk
ÅW- ¢±qHÙÄf(PÊb)i+cÄ¹Ù> ¶»
bY 17À-Ò}qQ*á¼ã ËºüÁg¨g§MJ-ëY7YÝZÅVëóQ'-¶H¡HãýCê·®3Î"5àÞ ¡)HÅdç)ªÖ$×YÐÏGÌw\va®²®çiýª'[ \À¢ìòÆõ+3µ,h2_¾æEòo1RâûHÝÂÑÿ _-¶ ûK)+~W`Vüà öö
¶´½iñ+åm»é·êà¿p£D®\§³õhFºúuË5#]F´XëT´Y;¢õô©KÒÀUÒ­tRe"Ê©f8Kº­ôzèk|2 uzgyåÜÐòNÑrtþu¯5íêK@:ÔÂ=h[Ð.]sQºFz=Ð1¯1ômÛtu_ô}[~§L$pph,_<ÁõL
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/929ff9fa9c3a10aefeeb522c9f7c4c7b0dda43

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/28/929ff9fa9c3a10aefeeb522c9f7c4c7b0dda43 (latin-1)

```text
xuÛnÛ0wí§à<·ÙÕV K%U`n2äÐÝ>°±PE$ÙHRôÝGÙÉÐ®`HH}üI1SUWß¾ø$u®êáÇ·åÞôTµ^K½öëe9^Ø7=lP;±IuºFóÊ6bSÕu©C©^cqYÿ1ìVI×ËT®ª\Ù³h£§ÉìVÜÍnV	7|üsFÜF³éxr+þÜýÞ%á÷<® ð±dR;è»PÒ:ÔhX^iëÀët;øeOÐèÖ:ï|ÞOþ
ô!µâLvx×-N> ûMÔn<ß «/ßÓÇ§K1\
	'ÝÞÁk&'â{x[9±E#·%T	º`¬&Ç+AÚ#lb°òÕ#aÑÈ-§_OÉy¾/Ôd:f!×L
h
ÿ p1b×ÿ\@±÷³ÍM¥hOÿíyæ4Ãø_^í6bwë¾[OW»£-«£÷8~TOáq^-ÏY8NUBZzÙøÔrø¶Fm
&YQû]]éàlá í¡ÉbÉ§|ÎÞôLü¶îï,VÃÅh>ù½Ì¦ïÝ;Ó!tû/¼¼m
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c1/bc088ae2b3feac4db9614fe5e4fdcfc2814f64

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c1/bc088ae2b3feac4db9614fe5e4fdcfc2814f64 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg¸<'g"oQZÌ<¥ýuu{wq}.(¨J-È¨,bX»ëÓÖ	[&ê^©ÌnèzVxGYË ÌT
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c1/9327167d4c9b66580e3819dcd062a3d94bfe60

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c1/9327167d4c9b66580e3819dcd062a3d94bfe60 (latin-1)

```text
x+)JMU06`01 ªÜl´[mÿðþV(
éó¯*nã\ ë
S
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a1/f9b90931cbee79ab905bf6ec304c8800ec3a03

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a1/f9b90931cbee79ab905bf6ec304c8800ec3a03 (latin-1)

```text
xKjÃ0E;Ö*Þô³¡dw(É×© ò+²ºüjÁ÷d©µt²ÓôÑ@fÝ´Gx±[7Zçh\ðaN!ceg<«ßØ°wÊ0V½Í[Üs²g¸C6¬7¯âÙ¤Ñ·î±®²*·GåyÉR¿ÈðlfÏÁúÔNk5Öñ¯ã}Suô,ûðå|ªèH)?Qÿ¿ER	
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a1/6c35a60d9576252f2c482652362d164b8c5f48

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a1/6c35a60d9576252f2c482652362d164b8c5f48 (latin-1)

```text
xTËnÛ0ì9_±/íÍI\ ôX)%R (ÉøÚµ|OO=ôÔOðuW¶,ÒNPwÃÙ¥æõîÆãO#(Ö»míª/ÚXÉTdö¹ÚR	iÌ7·Z¨ºB*À>Äj,6Ö<h{¡ÊfÓÀJ§_ï¿MÆð¹µA8üöíf{øµïë%$Eøe ¬P0w/ácä Öuil¢ÅåU*Ç`uã*®Ê\Ëæº¢ì¹;5Ø¥Ñ¤buÅÅÇú¶-Ikù¬»ÁÂpGG6 û¤NmeF.Rê]VjÌ4²`íJk]EÓsf§±ü71V8Å§HºÞeHÝOu®ê¨û¬ÏñàLÄH®Âx:åNÄ6¿xZ%ul[Þ:îf!¡ÕÏ<·~0¹âõP9óÖ
¤0
ëÜØgÃ©ëæ`@ÈTùÀB%ÈT´¸w3KDæQ&crü~¸ÁáÏ×}kXþ¾ìÇ÷°:üÙ·»Ü5ÆHË¯ÙÞÑ½ÓðàÙ¿B¯ÁÉ|ØäÅvçyYºoôïø±{Ý¶ Àµ
7fqèª,»5}Î{ôÐ{·G7#ÏÂhúÒØ"aæED¼Jÿ §'uã
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a1/9b50f2e1c87ed437cdb3f90354b1b6d60ebd1f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a1/9b50f2e1c87ed437cdb3f90354b1b6d60ebd1f (latin-1)

```text
x­½NÃ0ýWjdi{R5ý2°Xi|ÛXJâpíAÕGbâúb8)bi/>çï\o½ûÛ»DUV4
¤"´çORÚDÈ1H½c¿P­H¢hUÕ¤ÐxÃãó|&åb=Æ?
ÿ²#Of¡6D¬â!â§ñhÔ`êÊ"dºlJð5!|G?dê3Ò­0º¡Ì¡¤u
+=M¿câht!MJVúîj2æ3¦v^WB´}Ö«8J_ÆÓ1òIì»°²à©Ôæ¥Aº}»ÈrÆíÕI¸³Ü¹RÀ¼*å½ÁgXô:ÎªsìQÛ/Sö?IIíó¿¡öÇZI·q}õ½Ô²
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/2c/f9176e9f65d9583dc1221d265b88a7cc67763e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/2c/f9176e9f65d9583dc1221d265b88a7cc67763e (latin-1)

```text
xWënÚHÞß<Å©*EÐxVmÕ4]ÑÄiQRHtÕEìÈØã0ÂØÔ
­xÕþXi_#/¶çÌÅØ²«µ¢Ø3snsÎw.hÏ^½zñÓcºAæqxóÏ'«øhÊãO'ok[G_ï>ÅÇÉQæÄéNêÁl*ÉYòM¤îÜßG1Í¢,ÊkGGpÛê
@ÙSKR'.¸Q¤¤qæ¦ú=pöçö¹Í.ì½=¨ã«Ó½°¯[ïìë:Q4Óy 3ðÓ¨öØã¾9ØìÊþò®Ûê]@sÙ<.|ìÞömÀON¤ÌH³Ø)ÈÒ>&Å³~Ô-aú
Wzw5ç§j?Q¨iNKPL´Aa£oKmoÜ(Ø}0ypos¸)_m;ÕiS½åí;mãÆYbx6<káTëÓþÿße¾ÏcrZÌ]>¿ÿëþÏÈÄw#Ë¾mÔãÌg¸3höùrÎÝ{­PKâä¡$L1û³Ý°O·ö­ÍúíßlxvR»bûï?±û²Ý±%`t gÉÝWñG~}G|êPÀMbîx0w*ó8r1"N¬ÑHfÔ>øÐ³[¬?h_¬@ä»S'$Oç¶cÊR%[N}3ÏIåé­,×µ¡GØwÀGÿÔð U)¬.·8¨±ùpµ³;¼ T ZBÄ·8Ô\O9Ýñ´~PP©¼{ ³Â+vÙíatzä9D*P4O7ùSî:I9_çì$B*Ô%(³,pR.kQ½DF¤JæÈSL6ëcL¹uâÁ/UÃkð á%yxIÒh1¢dZ¸w~'Yzv\HfÌ×¾QÕÓ[Zúz½*¯uîÖnYKÓÖµµLÙs'ÆCU%gQ:w|¨¹ãF)O:7¸rÇõ%«ºAüXbÖ ËÔ ·&C_ø£lªK	.&FÞB³áC=¯X.àà \x_ËV«HHEóRfü°jðdÎ1IÇ«cµ®p<Dè	ã>Ô
GXt©DbZ	¾bØû¿!;Î¦IXø)83'DZ¯å*W8©Z­ÏÇ¨ý¬Ô¹ªdR¥D¾w¶Z£a}h4D¤çÑP£WîNl6ÊM"AkàbØÖ.!úT{ËÑÐ[Ð²yübU~ÈóäqÆ®@®®áâþ@üiÈóh¯¯
AFa}®(ÍF~¹²<Qò.BàuVr~ÕC9Ôµ·Uÿ2ÆÒÛb¨Sûxv|¯7%ð³Ü=<¬&fDøý,
ì¨´oÂmi.³`ºKér¨k´KO~[jÍF¸y$ÈæmNÌ;
PÌ¾]!¬¼·¡¯~@¡Uà.ÙB3ÑKo@KÔÿ!¥$nZüIÅ½$ÓN0¿4Ý³éLãP&?¯Ð2°ÚM%ØÒfÓ$ÐÎ¤
òÍ~ãM©0ì¿bÐ­ï¼urôt0Ï:]ök«=(Nää½øÛ½BÛt+Gé'£2r2=`òHýa"h%ÄF1b?Bª²kø+suey¿c	ÎBtn©ùÄÅA«s{}­sÎ/qÀB
`3ú1ÛaÊõPUµT=>VLz»jÌíY<+Ð#¥ÿ¥|"&z^ZÐ¤yn1t^©IÁ¹¿U²íó2vò3ÚÿÒgíN{ .³%ÒÖÍÍuû¼5hw;w;í÷¬°'ÙM¯Ýíµ_PÃ?îe^
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1d/f04e85792fbee84100ca13849177b8ced73147

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1d/f04e85792fbee84100ca13849177b8ced73147 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg¹Cmáó¯¢~Ù[6Ûÿñy|Í¢ *µ £²aí®O['l¨{¥2»¡ëYáe-N Õ_UI
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/aa/632620062f65a9b5652c27fa69399e5d971d46

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/aa/632620062f65a9b5652c27fa69399e5d971d46 (latin-1)

```text
xu½n0;ó§°´ªÔÁ±È
`dC´*Ò)ÏÓ©C§>/ÖA©:úüÝwª9ÀÚón\HËs	µ×÷¾·9Ó¡ûÚãù¥{oà±9ÙãWI(·6C-Y\¦HfebPë<5VhY`ò ôLEÔë8K×õ=Fð2Ry¶±ÉÑfñ©G~¸àñøwð§Z`µw@ ¸rfOfHCsÉ=iôGj;ÔHÈòÈØÀI¨&oÆJ`OÓVP,-aûçÿ¯½>·%4pê¾ÞªÃÔÝg{¬µFtmûNVé@!Uúpõp
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/aa/be898f0073522846b53f81f436ff56b877db79

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/aa/be898f0073522846b53f81f436ff56b877db79 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`xå£×9ýmqEÂåZß/ºx¾t²ºøÔ´½äü¼4o*üÕ-%ËwJÌºÝÌ©4¿,µ('±Áo«í¦ÿw"Êfþ½iò±îBC¼wê¢Ìô¨ÉW
É¾JÿÕ·ùðõ¬ém/bQ3º2ÜôÌì	5Ïì	H¹sè4sÐDQ PÈÌKÎ)MIe¸ç"=Eö@ì[	¡µvò%ÅEÉI9ùë~ð+fOuØ±û`Çß{PëÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  
 Ù
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fa/d74ebfe9ac4f0000a3d945b9ef89de915486f2

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fa/d74ebfe9ac4f0000a3d945b9ef89de915486f2 (latin-1)

```text
x+)JMU01d040031Q(M,*/.Ï,IÎÐË`£!u²Û"Æ+OLe¶øõézK\
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fa/452b6485de6d216b5042cc40fb59fdf1394d42

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fa/452b6485de6d216b5042cc40fb59fdf1394d42 (latin-1)

```text
x­ÁN@=ó´¸ÐDïÑÒBêÁË²Ó²	eqv©Ñ¦Oå#øb.©	z1xÿý¿Ùm£¶p{s}5¸­^æã¤Ò j,vÞ°«_Ë!$©Ê(¨Ýùéiµäaº¾Î¯÷;®eÄÃ
cÑºàyºaaÄïbv^øþ¸Â;÷²OäY¥%-ÆÄs fbk¨lÀmJ¡ õs$Ô03%íÑp­zªlÓ²ë cñcPDv0?ýìÄyqiÑd¸UDyDâ
î_ýÑ/ÒTõà Èª×8BF÷"!É®ÆÑo8½4ÿ©Gr_Oó@|)kØ
û¹ó	ïöÓ'
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/84/456f5feff32a55d987d034b1ad536e72fbd60b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/84/456f5feff32a55d987d034b1ad536e72fbd60b (latin-1)

```text
x+)JMU035c040031QpöMÌNõÉ,.)Ö+©(aH:á­¶ù¾CÊºôßýò²&³¡*sóKSã*âsªSóRô>=oÞª5¿¶W9¾Æ4ý1çã?Q$¤"ëX²ag¬æ\Õ«ìÔ64]Yé¢£$µ¸$¾85/lÁ4Ýu÷ìxè*ó­ºÖ§ÿ)gªr÷h0-;ûúèf¯Î]!Ös$;ôÔ ÊÁææ¤¦ ýrÖü\7OÃßÝlúxªwgÖ{?deEé ug#Ný-.¸ÿiöL!cµ¹Û?¤ª+M,*ÏÍ/K p\ó­ÍäÖªS}sÕþÎ<tU}Ï÷ÐuÀ,á«mæó^cv·ØtçO±VlÊ:lIQjrjfYjÌ
±'6ø¬j]ùzçþÉv+~ÏÙU=Ìüåé+fN{¹"¡ÓK4Q^K{åWÈË3K3àÆ³úf.®üÖ>!¨±äù3R"§cQ
3¼\ãsÏÐe;WX½~WuçÜË [¡Ê«r³¡IÉyé©)Àp½¥e¤<Á¶¶¾0ùjg^Êæk pp÷
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/99/6c0af21071b6a4f8321f71ab7b3263deb23c2d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/99/6c0af21071b6a4f8321f71ab7b3263deb23c2d (latin-1)

```text
x+)JMU013a040031QpöMÌNõÉ,.)Ö+©(aXá÷Ù0%$áÅÅÉ³¿5äLzêçU_Z_\XÔZ¤Ìpr±ìöb9Ó+§tÎ)Û×v¥¬!ö.TGIjqI|NjZ	PÙ=ÓïÝéëqúþ´?¢?õüt9ÝÈÊ2Ó3@êæªÜ?aç>cWýA¹µ³§^qþ	UWXT_
$@NÜàâý»¥ùmÆ×KÏ¾ò¬£(595³,µ¦^­Ù;NáÍ2yæàº
þ·f}ºõfVõ0'}äü¼Ô²¨;^.8®¨òñ%	Æ*ÈË3K3`Æ±úf.®üÖ>!¨±äù3R"§cQ
3¼\ãsÏÐe;WX½~WuçÜË [¡Ê«r³¡>zrFb^zj
0ú'<+8x¾MfBÜÕìÇ%ìçíí  $¼ÄP
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/99/b826a1c4cfea5afa3f39833ff9544ce3c9064d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/99/b826a1c4cfea5afa3f39833ff9544ce3c9064d (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^@ÂrMÙÇâq¿g_W|¾:SSi~YjQNb%Bìg>G|]]ánË«ÈQ9}ÏÕEéP'³
ÞürbbÉìÅû\ò/VÊ?Ç¢f´û
&vA§=³>üºBÀ}ö&@ SÊpÌeõ÷¢5x.HÙÌy­ã©¤fÅQQ\Ì°Gâ~êö
©²ZãÎßh8-ûéÔºòÔâ½ÊÜcMWÏ¼Á¯ö¬ìàÚ¯ùÌ $@7
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4e/e72d558d2d96f5c698536b3d7570b6ae9733ba

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4e/e72d558d2d96f5c698536b3d7570b6ae9733ba (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Ü£L6¡ÂÁ<©yßÅkgÈ.gXRÌzr|ºÛcÙj«;¹­f%BMI*ÍÌIÑ«LÌÍaàð\½(¾àösÉØ¥"K8\^)Î¼#3¥¯ö$ç)K~$?=zúøÑ ªÔÊ"µ»>m°e¢îÊì®gwµ<8>lP
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4e/ba053db2ffdc587699fdd934f17ed0805f4b88

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4e/ba053db2ffdc587699fdd934f17ed0805f4b88 (latin-1)

```text
x½RßkÂ0Þ³EèCÒb;pøcds*È&NÇÞBZ3-¦MIÚÿ÷åÒTjÙóòÐ^.ßÝ}ßÝ¨×éÞØi`èÔ@êäDdÞÐ/³¬}5mÏS¿â g*)è=¼._ðâ}<¿]+¼útç ûæÐÑ% Z=5ø²wÃÁ~.Lõ«Ò´¤¨/>ÿLô0~pS~ Â¥		ý>(°u
W,¦Y|OVæBÐ$seJéêû;Ï3
1s=x)«!ü
B7¨öêÚfÞ,S<iÛdt#	BC§$Dà½M#îÂD|ÄÊÓGê½J$¼^o
zh²½áÑÓjö1ÆÓÙdZ<0PÖ
4?W
Õ°H%étÙÅ úd.k¤Õµª6Âp@wä;âP«Ýh· nMçO¼wJ2×D[t6FÂ¾N¶ã&W.¨YE¸efàZ'U¦|YÂ¿½¢øÊ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c0/e5ba76ffced9001477c41a563de8b81e8bab14

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c0/e5ba76ffced9001477c41a563de8b81e8bab14 (latin-1)

```text
xOoÔ0Å9çSv¬«Rqi$ª¥BÐå@+Lbo2ªc[þ³°|z&N²ÛÚc<3oÞûMm¸<?³ûlI+èQ£
{7?§>¶¬	0`ôôç¬XÃµõhp<ÑXôÞBèIi	­26RBD£u ÕNéydµy½Ç}ØÀÅëkè­dÈHÚL¸Ìþw%«Í«j2­NRÕà¼uÊÇýü´	Z4:XHAeOu;àè»pìerÆqLDSÈ­o S±ëcXåú=Ó
ì=G¬ÑGÚbÁ=í!PÇ^`|$H¦KzöØ]lÁÛ¶=X¦éËbÍæ2øae¨UAc«ÝÅ
~æbk½QVÛ¸ÚÀjúòÔõqê)±$ E´æ²òjwqúü|Q®À|»¸éÞ¿{õÄÑØ"5!+!Ä$É
ïZB#³[§*A\}ºûv}{S=|ýR}¿ÿqu{÷a?÷Ð.ùGZT¿)öÕ´)
!gùO2CÌ£RË§ìUÛ®ãrñÀò­|âg.z
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/95/2bf513c9ecc38c4b3560b164e9b40075a2c1df

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/95/2bf513c9ecc38c4b3560b164e9b40075a2c1df (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgxl!Éþmòæ¬wçÕü^¼öû6ªÔÊ"µ»>m°e¢îÊì®gwµ<8Y0U¼
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1b/90401fdf6ec6cb9479e1a8042343a983db9c9f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1b/90401fdf6ec6cb9479e1a8042343a983db9c9f (latin-1)

```text
xKj1D³Ö)úúK&øÞgeôéXVÐ´rþè
ÙT=ª¨Ò[;´3<¡¨\d	u6©Ø7¯,¡CKµPÑq9oÅOøf06òN;§
Î¬!RÁWM²ÃDüì¾ûpO
ázâÞëÑúmoéx}Þ¾@¯Ê(¸H#¥XéúÇøÿ¦`<áÝa¦ÁÖqÉ<ñ1ýÉ°áõR1Ï]ü°°R
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1b/cd938750d2b2327780aa40e6a124f2e094e77a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1b/cd938750d2b2327780aa40e6a124f2e094e77a (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgP9q3£ÿ²¿ã»ëOß~Û÷È¢ *µ £²aí®O['l¨{¥2»¡ëYáe-N nAV>
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f9/bc6a984c87f38b6b3fb64398fe01829028a3bd

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f9/bc6a984c87f38b6b3fb64398fe01829028a3bd (latin-1)

```text
xTÝNÛ0ÞuâiR²U-°I`Lê  ¢Â¦m7ÖªcGþ	-Ë½Ån¦]ìAx=É¤¨&çäü|>ß±¿¹ÃÖ·¯=g"å6£ðþÓê0QXS­íéàQ|F |mËÉIßkã-YJ]h6u,Q&ÉeIq±&M¦æD¦/I§w) hIbA&T=ðaÝ©¶Ñg&ñ.ÌNþüøBj-q-%ø þð(>õãä ÞïwGqxÏZ°?<9ì%ßÇKéÇã~´ü2zÁA÷|Ôûìûg°µ½t»üãøë {Ïzç½áI¨äeRÉ#ÁË{Õ¯ tÁ(°ËC+nßþ@ìqFD ¢t¶Í	rå@Ñ±,R&áQ 
1,R²4Y2£Ð2aÞ%|+Íoé:Àñ?§ú *hSÖ²ûei´[MóTQ­}é,É5§´·7q>O» \{4$=¢M×ÀÝv^µ÷ð5§lÞònëÇO´xBNä<ùÔnÝÌylBGpøFÝ}:øxn¬UÇdó½d·Ö-yOÓó×hnÜ'ÓÀÒÖ²pi¡¯i¯±oGçè/X#H­62gW$>Gã©§PµW´"=dÕL½Íñ{õ<ÚÙÂyV&Ún¡¿1ï4QWÕÐ]Ö0X[Uì	¹OìK6åb÷çAõçPSuû/3ºÊ Qp5WäqQï'çÉ¨Û;CZ:å×;k¥í KQÚ¦(ÏWzAfB?ÜJ¢%ÓÖ	´ÆYjs«[
¾¢Æ*»ÁMð
FÍ6
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f9/777b89deb3ed5a055762e2b56411dc04677781

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f9/777b89deb3ed5a055762e2b56411dc04677781 (latin-1)

```text
xu1KÄ@­çW\£;¢©¼³±°Y&!	Ù
³³âøßrú`7÷øÚZ¼Ú¬ÏV³R	xXâCé¯<{­&Váp9ÜüâTñ¹HB=ëwÙ´xÃC\L%³ËFÆÎ$=wø¸hÛ8Ãî½>±û½¦ÜÏc±Úb$×ðYTîhéâLJ¨Ü)&ü¡M(	_w°k^ÇgwßÜmoó /jø9b5
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6d/51b98f7db5f20111b2f79044024a6abbb9e6e7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6d/51b98f7db5f20111b2f79044024a6abbb9e6e7 (latin-1)

```text
xKÊÉOR024e(I,JO-/Î/-JN-ÖH,(PòsqåRPP©vöuôvw
rõ÷ñwñªÕ/M,*/JMNÍ,K-ÒK&¬¶¸<³$9¬R¹iÙ©ñµñy%@
\\U©E@äÒÔøL Í%ùE@«TGùzÇ;ûû¹yº×êCUhr ¨J@
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6d/7e187bb7ffe810b4b96f10c816552cae49f2d9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6d/7e187bb7ffe810b4b96f10c816552cae49f2d9 (latin-1)

```text
x+)JMU051f040031QpöMÌNõÉ,.)Ö+©(aàÔ.ß¯Ï°vÆñËj?$æ?ùU¢Ìpö]¢ÅÅ95%/~ëuÝèÓû-9ª
¨ >%5©4¨lHödÍÅ&nAÛd[EËMi*ËÍ/-N/.ÈÉ,O-KÍ+*	þÛöüýÕÊ	3Ón÷ÌÝÁ(UQÑTTT»<¥ðLDmå£$½#O¥¾ïïª-I-.*ªlå¹^*8Í­~3BñI¾ÿZ}ª,M,©,K*ÏIM¹£æ#[É­U§úæªýxèªú5þ8te¦g´L©¿soå÷M7581%ÄäÃlIQjrjfYj0üÀVý;±ÁgUëÊ×3<÷O¶;Xùó{Î&d+àêaä/O_1sÚË	^¢òZÚ+ÿ¼RDÖP\Y7Õ7sqå·ö	A%ÏÿÌh9jáå{.Û¹Âêõ»ª;ç^¸¬Ø
 _¦ã
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/98/6941fdbe19d771a7cc6b59be2991a6fd5c4f99

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/98/6941fdbe19d771a7cc6b59be2991a6fd5c4f99 (latin-1)

```text
x+)JMU054g040031QpöMÌNõÉ,.)Ö+©(a8´âmÂÙÌÞ,íwS#N¶n°=UT®Ì°N${²æb· m²­¢åGÅ¦4
ICåæ§ÆädÄ§¥æ ÿmO{þþjAåi·{æî`*(hJª.JÌjhS>o»ÄÀ%mÅgS2¦8½ç+Æ¢¡8µ¨,39¨A~g·í$é¥×Þíµn÷Íx#ØÕPXT_
$@NËIM¹©æ#[É­U§úæªýxèªú5þ8te¦g´Ô<k¯î{-Gw^m²{¬¥(595³,µfØ¿|Vµ®|=Ãsÿd»?¿çlÂªfAþòô3§½\Ðé%(¯¥½òÏ+Ed
Åå%ÉpãY}3W~kÔXòüÏÆ)Ó±¨^®ñ¹ç@è²+¬^¿«ºsîeË­ C%Ö
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a7/6471fc1c8c187d5c39e2622ec4e51af4c78f8e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a7/6471fc1c8c187d5c39e2622ec4e51af4c78f8e (latin-1)

```text
x}RËnÛ0ÌY_±M@.Ü(¹HlÅªØ9ôB0âÚbL.E	v~LC>Ä?Rt$rKäaggg8¼ê¾EkÁ
Y©ªD¢7§yðË\Táë®­¨%Óâª]j±àrÙû]}µ°Fi©¤Ôÿ(ìU4mdEµSXã^¦À¹q¨ 
ÈÍ¨?Ë2NédÃ·~ºÐ
¯Óùyó8xÜ&Yç"JC
ÏKL yÕæJVKâ]øE~Øå«¥ÑUîA-^Ã%ä´4Ä±´ ¡¥»hÈøÂX;rÇíFSi	Nsrkw2xÇYâ[þxÎO?ÇcÌ×È|Ð¶¹<aÀ¶ö<îÖ¯ØfoÝ¸A6ÿ^AW(Ì+¹{Þ=)øU!Üï7¼4R LAnÃÔTÀj
(kN5|Kûûa×J3¬gCoEtáÌï¿jþgÛZn"t![1á´JÔÝaZz×:ÅÞ8ý1MGÃw¿äUûÁ°,ÃþÜF
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a7/b92fd7ff4bbf4d697c050bd5e5bc95d314faf7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a7/b92fd7ff4bbf4d697c050bd5e5bc95d314faf7 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^@ÂrMÙÇâq¿g_W|¾:SSi~YjQNb%Bìg>G|]]ánË«ÈQ9}ÏÕEéP'³
ÞürbbÉìÅû\ò/VÊ?Ç¢f´û
&vA§=³>üºBÀ}ö&@ SÊ ¹àÂËG5Î"ËØ:¯K~-}¢¢¸(ÁÑðrHCêZý=OÍ<Ð^ûØj]yjq^enCÇ±&Í«gÞÈàW{Vvpí×Ï|f _­Ú
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a8/4ef331645460d238d193599bf6806c92e54e44

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a8/4ef331645460d238d193599bf6806c92e54e44 (latin-1)

```text
x­½nÂ0;û)®C²ÀÀÒ¥¡?
¡CËÄb5SÛ¡*GêÔGàÅê "íP¡^}Î½ß9ö*+¸î:IV	àB¡9~*!5pG¥ÉËô]QQ8ÒZ©j§»©7ÇCÿ¢po;¼ÉpìSoEþ4¦Ù2ò|úD~¯× ÉÂ $2¯rp4æ¥B8­8~pæÃÔ
Õ²REae	ó(xÆ>èî®	E|^²Ë_h.+Tf&)+6È{	q	kçÖ¹ó0i4-®e¡kGwÀÃÂ(1.õkËúî&Ó-ª)c±¶xaËpm,Øó{É>-*ÚÞ¢ßIÒvïUeB,Pý	fPf¼K0Óè»£eM}õwæÚ»¡Ä&mYÞ¥vSªFjcÜ~|´L
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/54/aa1b5d98db7e15f6d772efec20ef31d0d1957b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/54/aa1b5d98db7e15f6d772efec20ef31d0d1957b (latin-1)

```text
xKnÃ @³æsT|RTõÙw9f×1Æ÷¯{nÞ^nµ®,êÛè"Fb"4IpÐè
¶8´s1Soê²_¡ÞdkY'þs<£âõ³Í\fEçøi¾ÛÙáIUàqÈÒx­ík©´n¹ÕO0Á£Æ¢»vZ«^Cþ_ªMæmÝ_0ä´së¸ÔúqLk
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/54/a6a8272e9229e0fd34c14060294b0fd9c09cf5

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/54/a6a8272e9229e0fd34c14060294b0fd9c09cf5 (latin-1)

```text
xAÂ E]s7\@3Phb'pïr CmRi©ç½ù÷òbÉyªµ=ÔY=¸È(ïì`~ã]ô}ì
¢î¢xÑÊK¬ Að Ù6ÎÂ¤1ä5R 	´×gYå£ì«¼SfyÙx,ÃËmÌ4ÍçXòU*gûs^@ö¶¾Êÿ¢òÖúÞßÊyÚ*/MhËQ| 4IÅ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/8e99bd376d1dae74536c7d765ef342ee2466fc

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/8e99bd376d1dae74536c7d765ef342ee2466fc (latin-1)

```text
x+)JMU047d01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õN¤üÄ¢bÐÛäÓÜxËV[ÝÉm5»(yÔÐÀÀÌÄD!©43'E¯217Ãsõ¢øÛÏ%c\.áp8z¥bLr~^Zf:Cæ*³¾U
w5ã¶Að{ïßU©Ekw}Ú:aËDÝ+Ù
]Ï
ï(kyp Æ"E»
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/be306e02e75c9ad6d10200e2c5805a8da7932b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/be306e02e75c9ad6d10200e2c5805a8da7932b (latin-1)

```text
x+)JMU06`01 ªÜl;/Ü]&Ô¦|C;CA£uc ò*
L
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/6e01d630210167daf1531f4442634b1c7c75a9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/6e01d630210167daf1531f4442634b1c7c75a9 (latin-1)

```text
x}QËnÛ0ìY_±qQ@ìèT¤@¶CBe¹ð#\b%!2a'È×ôÐñuIÅm8ñ1«ÙÙ¬Výöés%yÝä¾?ûr§£ZE%·à¾¾ÄFHK×L²BèWpçá ·t­#¨±Ì
ÊK& Hf×t:»Z%^q2Ë{0¥øÞNPWt/ `ÒÈýýoÕuÆøä
êÊX!\C%-´=í@Ê³+i,8I­x§¢ìÂc ø´ ±ºámÍÙX¿K`¾3W|®úáØtýÁñka-ÁMEnð%éV£QBp4Wã
ïdÐo¦AW© ñZ|s$N'a8ÿÿÐ@¾½üC¾s_Ãµªkêo÷þ>³áNï.×Zlú|Ûk×]»^±¬±½t¡¸ß?íÉç6¤qªC7^,IJæá¸zGÄÎ%c*T­=Æ3-V£Åxÿ\Æ³ôÛ;y!á_âÿÚ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/38221760ad47cfef5c17fdd70b2f8b348ca1e6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/38221760ad47cfef5c17fdd70b2f8b348ca1e6 (latin-1)

```text
x}QÑJÃ0õ¹_qÁí¦¸E[§e³[}ØSÈÚlm¤¿ÆñyÐ3iÖ	{rÎ¹÷ÜuÆ×pÝïSgeBàö»Wá¦D0]ìî¬?eT yênpJ|¡*ÞÐr]vàK{LAÒ¼Ì° Í7ÀEuÐI¶%K¸´ö&p$T­`zÞ-Ð'E2#¤°'hégáhi÷:«Æ©"v×K(þÖVxÔv×óAþáop&ÀG=Ù3E¨àP`CÓ§5AÑÃÂÐÈ¡oë)8ÐõzWNË¦a:>M§í·ï§¯Mg9.YõU}rÐ;2 1åg:>1DàÎ7®	ÝrÀº

çëê;ïXRaEcÍU-£ÕÊWU
Þï¨²¥RÕSnN{¨§oL6mÅgô
×ZËÕaµb0~æói0DÁ,t@oqÜ££ZMCóE0[ÑJ'ðKáâ½
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/c8d709688fd34f1241eed7e4e557dbed8ee239

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/24/c8d709688fd34f1241eed7e4e557dbed8ee239 (latin-1)

```text
x+)JMU022a040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ SÊuöÑÖµ?«Mó_^8çziG'DEqQ2C ó¿©n/êf83Á¬íbx¡&Ô¶òÔâ½ÊÜcMWÏ¼Á¯ö¬ìàÚ¯ùÌ c
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7f/010af727ebe5e3ab749e212891bdfe6d5d9bfd

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7f/010af727ebe5e3ab749e212891bdfe6d5d9bfd (latin-1)

```text
x­Oo0wî§h¸èa'éBÄ?AÜa¦ÒWiµÅm?ÒNû~±$Ó.WÞ_ßç÷PXàn÷þÎÂ^%ÇKÐû/ÉÂpThyü!	/r*ÒBrPvkû<w2x»N=á4'ÜQoØ'î<úãÌ&óÀí/ØuÚíãÈÂiÀHÛ
Ò\®Vì?u¦r(QÈÈ Ð<ÇÓÀ{ê}qkû{ïÍÂÃMúBRQ( JS
$i¶Ö_Ú2¤ì5ú^Hop
kÐós´]È´¤	¶ÊõZd¢|×ÈÔDUP©
Öj¶Ú aó\®RÌÇ ¾In¨7®£ø4`5l9p¥!Y£]Éwr¹\GÒG(A¢À>äyGéå%äúÿè|ß¨¼öw¸n¢j§ 3¿Ô
öªé?.8SmfÌ\h}ôG 
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7f/f211cfdabd2def20b4e173fb5a1789d5823eeb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7f/f211cfdabd2def20b4e173fb5a1789d5823eeb (latin-1)

```text
xSÑÔ0õ¹_qYZlwÑ]WÐ:ÈvôA6w:¡iRÒdØì¿vªU´izÏé¹çÜ¦¹P9'Ï^>zÌe!,CxµÇfÛéËÆÃútû:ø
¯PK³PeÉe»û,ÎpÇì¡©l]ÅjCjµC·ØæåÖÌðpÒ©¤%ê_Z8nãFÛnÈPQ: #µ÷Ç0	ì$2Â0·C  [¯ÈÝzù)KÉ2½ÉÞ|LÃ}]-àfýáÝûùrwKzJ~N³è*¸40-tÈbÝ/øãåIÝ?ÚB+!ÈPÿÚÚ½skmßÁèqKnÂ>do¿O½|»
ÏfÓ^º×O°®_G§CÅ»îëc+·=û9¯{uq|ñ¸s5ïoôám7´²¯Ï¿Áµ³î'Ü''ípdGÓ¯p*NFy,z¿3">Ö	½
ÝFÓs'á.½ºT|jã#?[w&×MÁ¤â¸d¼ Z[`Û*(T
¶¦`°6´BpÂphaÇ[KE4Xp:ý×Ëi¨1îGÏp$¾Fcµä*x~ á@
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/06/e04f2a6847dfd08c81f9abc021d16ab80aedd4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/06/e04f2a6847dfd08c81f9abc021d16ab80aedd4 (latin-1)

```text
x+)JMU0³4b040031QpöMÌNõÉ,.)Ö+©(aèv[p3ó«RÞöÎÍ)ëkz,OAU¦¤&¦Ç'å¤Æ§¥æÇçè%3|ÛdfP¤¹zÍ!¶Ð'ï¶/l~~
ú" z½E}VÍñyvÚqï»×jO¡êsóKSãsNIÍK©Ý§ãª¡¤Íïxò9CzÛ{Û×PÔäd@\T.Ï~sÙûgô'Tý_÷­ÁzÎ,¨rBE@µgrÞìYp=­I1¡ôB÷I3ÕÔn²ÐØäU9£3ºuG«Ó°sSNl[Z\u7På	¾¿WÕ>±NÓQÜÖõñó´·áO1U¼ÂúTÄHrÓÊªúI«Dï>ÖuÏ
ª²4±dfY*ÌàÔ´ lm&·Vê«öwFà¡«ê{ÖøãÐQÒrZp¢MãëßêÎøÅ×¨¬¬¥(595³,µ(>bØ¿|Vµ®|=Ãsÿd»?¿çlÂªfAþòô3§½\Ðé%(¯¥½òÏ+Ed
Åå%ÉpãY}3W~kÔXòüÏÆ)Ó±¨^®ñ¹ç@è²+¬^¿«ºsîeË­ BÊ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/bea4304306e1dc70e0c63123c11482c5471112

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/bea4304306e1dc70e0c63123c11482c5471112 (latin-1)

```text
xKÊÉOR046gPÎÌKÎ)MIU°©J-È¨,ÒÏN-ÊKÍÑË°ãBÊÍÖO-KÍ+ÏMÌKLO-BVªÊÍÏÍ/-N/.I,IOÎHÌKOMÑËPââòõw
sõ÷ô
ðÑÀ¡TÓ _3!
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/35acc76ce7972853896897c9e1eb60705afa3d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/35acc76ce7972853896897c9e1eb60705afa3d (latin-1)

```text
x;nÃ0@;ë¼@Y¢>"2tËHSL*4²
[îùë+tyÃð¤·V8ôocUqT8G2&8c
BQKÐèÍ¯ºcÉ¬]VGÄÓlË#ë)S'EK6¼¯¾Â½ï+Ü¸)¼oúì¥¶~y6®¯³ôöS
4<ÁÉzkÍa¿¡ÿ/ÍÐmÀ÷ pºÈk¯eéÐú¯Ø75äMl
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/abcb86578487f95fa9e5a313eb80f1730a37ab

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/abcb86578487f95fa9e5a313eb80f1730a37ab (latin-1)

```text
xK
Â0 ]çïÊkþOàÞåkòZÆÔ$½¿¹»a``bÉyë ¥=õÊÙÉdO2»h7ÊÎ*9ãp¶ÄÁ)5Ø©ò§Ãb?íÕdujf= úÅHrDþ*å¨ð Ìpm¼´år_3mïK,ù3C@pF(ÿ/EoöÊ­Á÷ ÆâôG¥
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/d77059945a1dc127118c47b489fd3f3e8e2c1e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/15/d77059945a1dc127118c47b489fd3f3e8e2c1e (latin-1)

```text
x+)JMU047b040031QpöMÌNõÉ,.)Ö+©(aÈ
ÜÙ_»õ£à¦ï\¼²vï|öª2
¨0¾¸<³$9#>3/³D/a¸SpÂI=î÷IÜDø³^Æ@U&Ä¥&§f¥v>ë¶»rx÷tÆvgýôÈæ²RÁ@Mu\©fÑMÞA=\±zwTÇÚ  ù×Ga
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/2b9b3f6dc644952de8c7cfeb3ee462fda15f25

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/2b9b3f6dc644952de8c7cfeb3ee462fda15f25 (latin-1)

```text
xmÍ
Â0=ïSzQ/RP|ÕnlÄúôFèÁsoÑ´8ç]7gõJ¤h óÑPµ(®oÝ	sDêÝí·
Óà¼ýBðEUeHOlVJÂ;ïA4µv,ìë¸Ë&ü×a]teN±Àá ?=¤
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/c5935a7672cdda09ee00e25092db6a8a93db13

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/c5935a7672cdda09ee00e25092db6a8a93db13 (latin-1)

```text
xPÑNÂ0õy_qÅa¢¾ $*YÃ_n»°ÅÑ¶[Pã¿ÛnD£@lÜÞÜsÎ==qQÆp{}svó¤¨R»÷íË kängýld};zL·e%JÅÒ$c|i?ëü	-QÖ¸¸VFÊò3:_L#Ð)xãØZ´ÿàÎèóüGVÄë-ËìÉÈ¹v±ØÑ"
9
;)¹T`Lµ\bÖôiR*i1Gk|
÷À$=ñ3[ë
¹|
ö9ÖÝ¦1úU%8Çd¥/ñCêDãmÛ  ¼Îº
L0ÎSýzeBO aþõÕ(Ýõ4S×·¶ÊDEAw{L\)¥ã0ýçîÓ²ÝeH|ØÁö³Öº³å$pBwáãQ³¿ ÂíÑg
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/0105543287ccb3d8bf4895af9f60d7e6c74b00

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/0105543287ccb3d8bf4895af9f60d7e6c74b00 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CE~ç¹DNuõOÅ*¢NM_ÒwSi~YjQNb%C××cµS8>Ù¢{¯ÁáÐ2¿÷sS6 ¨.ÊLÏ¼0ÇtïÔ2U}µ 3]1ïx,jaFÿa¿`å-¶çÿåKEL01 Ì¼äÒT}yLÏcf]»ÈÄðèhCTïòÉÚÅEÉÖkÓ­¦^Éb¸h),ÿ $ËØ9×j]yjq^enCÇ±&Í«gÞÈàW{Vvpí×Ï|f Ää
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/17c96c148c9d5867982d5c324da1f91186f9a9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fb/17c96c148c9d5867982d5c324da1f91186f9a9 (latin-1)

```text
x­S»n0íÌWX",²T]#J*ò!ºXßKSÛÐGOêÔOèÕ´¡©3çÜóÂ[Æ·h<¾»½1Å¬ PêëSP.@D@HãòäM`Zà
+.(HkpxÏ°³\L½ãè°ÛÎ|2s±³	wâõr8.¾÷ãh8¼0Ld¢)Ï §E,	i. D¾>Hd*{PXòBÄÚLçhxÐ5þ
ùÞ:¬eR^HÀ2gTa(!SÃ¸Ï`Ûb¯q¶aÐUÆUöõÊ÷B,}Iç	&¾­ÈÑwEÄÅ"ÂÈçáÕ·V×m¾H(¬»ZÀvµñ«ùBUô ¤¼\·ÔI¥®²&ÄuîS¥U×f`T*È@t (êÇNCzR:ÀÏà_cz2Û &Áª] yq«AÕn+è>é7nFcÝn¬æ¼DIcèÐec­.ã6EÔëé¾n=#úµÙÆ7¿<{
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5f/67f0f55ab9dd1e38682656a67240895d20039f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5f/67f0f55ab9dd1e38682656a67240895d20039f (latin-1)

```text
x+)JMU06`01 ªÜl2z³9öo}ÎÝ÷æt#Ç³Ù»ºòê
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5f/4a5cef19c2e25cc5ddcaec470d37050a98ad74

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5f/4a5cef19c2e25cc5ddcaec470d37050a98ad74 (latin-1)

```text
xAÂ  =óý]pac|w@mRÄ´øû¯dJom@äcUáÏÉÛàâ$L9°ÈDê9¶"OZõ= ³Xo±NµpÉâè.XOÎ»$ÑMYT¾ãÕWxôï
÷Ô.>û4·~{¶4/§ÒÛ00
"Æ Gë¬5;Ýÿþ_¡Ûí³Ìã5?ÛE&
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b0/96e2eaee995e70af1abcfdd42582abcfcb6a21

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b0/96e2eaee995e70af1abcfdd42582abcfcb6a21 (latin-1)

```text
xmTÛnÚ@í³¿bJÉN(Ð¦U*°!Q QÒF©eì5¬0^k½F*¯ý~b¿¤3¾@ÒàïzÏ33Dr­v»ý¦y §´»K¯,å®ÓnøpÐ4öDìGYÀáô'³µjÎ¹yÔ}y
|)|¾RbÉUÚ$O;	NE<mâú¾çV¯ãÃgÐw¯½[¹=vîtÌ|\Ìëp>¸¹¸ê»?®¿ºDqØ9Öaì<16¡Ýí7öÊ>2Ríiá/ãTCªUæk(²\\è@¯ÎÑ×Èí³ËÍ ÇîsLâÙ9AEY¼ ¤bÁc-ñ2ü@i!p%W^§<à#>QoëÝå0ùäbX«:TÛõfúJF»ÅÊdd%{iùYðË |DæÛ"GW¤®â^°Îs(ªoU<âl84k·Ýá¨&r«æL,z×á#]ÆÅùÃÛ8Âû4ÉÂ{ûuµWÝîIq40Ãh¸ÊÍÒ"Ê¦dÈC	Ê*/Ià
õ¨féË
V[?íÈz¼TRnñ»ðgöÇòbù)
lÆýy- $â)w!FÂd­ñ³Õh[TrâWâlP"P* Ú@'­\N;pëááómR(á½(.ÅÇxxÞçKÍ+·/.·óË1ÜG.C/±^yÉg!¡N~Ö-õÒgÙ	OENôWÙI®EXÉ"°êb	8¢^TI­×;ëµë||WýËüýýv1*Lù§¢³@°¦wQÀ»íö;m':îìÛG«Z=D§Æ)À)©ª¾ÙáY51eMËÞÆº<ÿ ft
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/20/5de8e64cc4e0f5ab78473e6d0d21087997bc98

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/20/5de8e64cc4e0f5ab78473e6d0d21087997bc98 (latin-1)

```text
x½UÝNÛ0Þ5OqÔ¡Æ¡--0$´1@ªFÅÚmwpâÌNñH{½Ø7s
Ó"-¾sÎçïø,¹XB@FÁ«ndQ!9<l >%Æì¼ØkN-DÃ®¤(sâ,èÅ\1®à
|¸xÎ>O7Gópþ¥~F¯{&ºÏü¢_î×ðÇj¤âå+f|jÿÌP[/·Lz,£KÎã¯Ð5"[ñTAR«Ö7ô¾SÙD¥,+<3kE	¾o±ó|½S9[el
AQhm?£)3±mÂ;=èòÐLû$g±²C}ÐH¤9-<¢æ}'ÂÓK^#ÒûWö _¡ïXê=7×¤«G>Làdvv½}:OÏNNÌkNëHÅ$Lß9Önå	Ux¤ú ­S·bÔ¼Gý>ÅIA¢J
R3T&+ÄÃã©¯%±0~oTD3Ì×ÕÔå{zÓ3Ï(ÒB&wõ81óâD²¨@
úà·ªù#Ç¹P4Ì<¾é&wHq(·mTqÄh¢g­¥D aãêL`ÓÍÀôü3ü¨r2[L§ábö×ÊµÆ­=@[á¿=8²¢XOØiO¢µak£Öv[{¿ÀC³M¡¤º2µµåÕ/¨²ªÀþ8¥¦ëëë`àt¼eå.»7u+DTæ~ýÌ°U`kñ··­B;®çºÈ|  à Ô ÊB»$ ²d ddd·¹;2ÀÇ?784ì¹°¶½ÝÛ¤<\²kú-Ò
ø´E­ ø³áIáY;ïq¶úø@g+ãk¡Xf'ú¤ºÅÉ2óV>t£]\çÙúÛø
_+b
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/21e94ecd76dc137aefdca1f04fff3d95a736b3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/21e94ecd76dc137aefdca1f04fff3d95a736b3 (latin-1)

```text
x+)JMU022a040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ SÊuöÑÖµ?«Mó_^8çziG'DEqQ2Ã¢_=êùÎëõ=æÏÜn=Ë¡¶§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  ÊµdÊ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/bdc9d122834117f3984b8b2080489b823d0623

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/bdc9d122834117f3984b8b2080489b823d0623 (latin-1)

```text
x+)JMU06`01 ªÜl"&Ë[}SXzN óâ` à
-
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/374be34bd3c53f3394758ed6576710010be3c1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/374be34bd3c53f3394758ed6576710010be3c1 (latin-1)

```text
x­TËn@íz¾b]ÀFã¢.
ÅøjÝLFæ
Cg[5~RWý¬ØhiÊsî=«X¬p¯÷p×Â^Ä9ÇKÐÇ/ÉÂpThY´ ¤@ZHÊjï_ÆCâL'ïéÐ=!ìz3î]â,}ß,È|ºô<zþ¡ÛéG TD'ØRdp¹âøÉ¨4!h¢D.#fùÞsá"ÛûßkFÞ|Q-Ù%¯$¹¢4Õ@¦!°NløÚªÌÂ×|6òÄ\£Õïl3ºHµ¤1¶bÊõd¢xW«©NUN¥&&Wà$µ6°y®))êë j@HÄNþoÚrUÌäIZ«F\E¤1§j¥MÒç l±«*jg»*nëÿ¬Jò0jÖUÆEY¬Úà·?í0lPþCUeò
Ró¸á$Jô¥ë§]BË*çNSf>M}oj³
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/e6f9453548ce8e2f481e9b6f450a23e5db08fb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4f/e6f9453548ce8e2f481e9b6f450a23e5db08fb (latin-1)

```text
x+)JMU06g040031QH*ÍÌIÑ«ÌÍa(M¬jù,¥·Z<XÆZ¸Î",A 8ª
Þ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c7/9a4ceb4c59eac57b8931e8379b130a50cebb86

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c7/9a4ceb4c59eac57b8931e8379b130a50cebb86 (latin-1)

```text
xT=oÛ0íì_qvkí¢A'°$
e Y¹ÑÀP»6ßÓ©C§þÿ±eË$­Õx÷øøÞ»£Vë~·w_>x÷û]m×¬Öí,âEÂRõ/TÉY!Yúov5çuTòÀ>²X	,¹J>¨F¡ÊfÛ@'»¯óÏð±D8þívwüÙÃ·~q|2
dö%ú"9(D]J¶Äb EÏÐïf¶âªÌ´±ÚÜPT!w§² a!©è&\úØØV%i-k,;22÷"Qä)ºósti)0¨»l­uZN/ÇòßÄ´Â><ãð®CÆx¬uÕ@=f}ä¨,BrDcTw¢8RA»Å3¼<®#éß$  ðÆro1³IZ
ö¬ç6&ãzGÔG¨:ëKRu&UKÌü{sjÚx0Xpó5­#ÆöÝ%$óXÄJÇdù}w¯zØÿ¼ì×§÷ÐÚõÕÍCî#¤åÚÞÉ½D§á _äø
NæÝ¦^l»yX/Ë°põy@ÿïû×]»LUØéhÞPy°~BÔtmXïÑyBÿ²ä¿B=:#<Ïfie
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c6/44abf772acc00cd01a3c149ceb2c4922263a0c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c6/44abf772acc00cd01a3c149ceb2c4922263a0c (latin-1)

```text
x+)JMU06`01 ªÜlo³&¤P[<Ã}iÑÚÐÃ;ÍMì ùöf
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7b/c59e23903edef61692f138e7e637ea1cf82279

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7b/c59e23903edef61692f138e7e637ea1cf82279 (latin-1)

```text
xKÊÉOR07f(I,JO-/Î/-JN-ÖH,(PòsqåRPP©vöuôvw
rõ÷ñwñªÕ/M,*/JMNÍ,K-ÒKæÒä BËG
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1f/07c209a6a4dfcc2f91347affaee706803b9c9a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1f/07c209a6a4dfcc2f91347affaee706803b9c9a (latin-1)

```text
xKÊÉOR04´`PÎÌKÎ)MIU°©ÊÍÖO-KÍ+)ÖÏÍ/-N/.ÈÉ,éeØqqék)¸¤¦eæ¥*ä+EóÒÆ$æä5¥*hésEùzÇ»¹úÄ»¸ºyú¹j ÍÇ0LÓ ÛR+©
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1f/b98b3d921ba5d6eebd3b83561f4d6a10ec1186

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1f/b98b3d921ba5d6eebd3b83561f4d6a10ec1186 (latin-1)

```text
xUÿÚFîß~"Eæê;î ×Dïj'W¥id­×kXí¥ö@Ú<LÕ?"õ5x±ÌÚ@ñq½Á`{gg¾ùæÛ±	f«õÃÐ(üü-æë´þÀÒE§ó×ÚÑR$f3Ìêøÿäº\/X¦V·úQÎ¤r^ß_=b¿Z)ÇêÙ"âÒE1/céSö(:E,ðæçL­?ºõ£Þ´o{®}ë'¶«WÂ,©ÖhxãÜz¿
ÞzÊ¿oßÛýÚ¦ÕO48éÔéA£Ù~ås	4Ï¤aAR
/x¡ALm¹tó/,RK"ÉRdÉ@ÈWb$@ð"ì7×µyÂàÍÄS¹½ñ]ß`Ó±ím÷Þ±lï¾Ûß5ÀÏÎzöÐõlÝ\5¹:;GÓº@sÙFÓ1Ñ

ífàÑÇ\±}@pÁ§h&4kØígÀöºî·6éüÍEMûÙAã«dv§,óJu§"ªZYÆi&ä2æT/½<ç´Ý«êªXë
ÃÎÛþÈoh¢Äh\¶[gçæ´ß7
ß#IÒø³ôF_%®ïI¾ÅY@}Òi_^´ÎÏç°4Uç-ú	`I"Â9Ã«XdÀ%')èñæïð×e¥n) ¼ßôíÒì¶'²íÉ
£7gïæâDÁX\ufn»ÚV{i÷ìghÒ]+
ß;×tÝw»=úËÊ.GCA[ÍÐX¡5ÇCKñ4òuð|L¹dð#$Bòp­¨æíÐX¿tÝ®ãgcUìrª$ô?/ð_8×Â	ÔíÁ_)ðÙp4qnÞ}W;Û1õªþCiY)Ú°£cË²ôÒu÷dä hñìW×Ø5­p'/Ð9I@`Á"9IÕ|^²íaJùl.õB (*JÖu*LÂN6'Yc±¤¦ýY´ ã-¼b"¬È£,­¥«">e2Oxe;CWEÏ¥bÓÅúx¿erª¢ h¶â(æ½8¢¿:aTrÄ¾*/¥p­æz{yÛúJr«ò\ÒSôH³÷Ïv²ÂWQ£è%*å5¥«÷ñäÁ[`|¡ë
Ú&Ö¤JÚ°å'¥WÚgí+<eô
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/97/f9a4346f8056b6343a3bd192adbc5a86df93c9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/97/f9a4346f8056b6343a3bd192adbc5a86df93c9 (latin-1)

```text
xVírFío=Å3ö DÈqÆÛIHØe¬J	»M[Ïµ#xÙnÇÓ}¼XïÝµ3å`¿ÎÞs÷ì¹EÉNN>|÷ZÄATÎÿàéâYv\Æ<z·øÔúf(ä+ðÝCR¬¸Ì:w©HþsBáË|çÝÙsÖI¥óåÖºûegî/9ËE,p:8û¦â¾|Èyù¬2yìIÔj½ù\ÄN
G}ú³®=5"ZíVû¹ Hâ,,EqbaÎ²Óà#\ÝÃ¥Ó±ÓcgTx¦µÏZ;¡tá
eaúÎÛs0ðE!
ìÏÎÀ Vp}HaöóìãÂAF
8¾âqÎòçÈiI¤À¼}ÏróßoÏªnì¥.&a­£-)/YÆïb`¡ûÔ:k]1ïÇc÷ÙÔ³{W¬ï\¸CòÆp³`iÂî\î\#åÉýÇô§ÔÄ<=öPpHEøt.ðPøq@q©$Hrõõ¯H`Ï×¿AòÏð»µJÆE"^Èê}ã ?fÕGÐnýÙ|"â`tÛ ÛÔ§È²¥dlP6á]&Î3A^4%TÄÌNn 3ºqWì§©Ó3º:H½úßÖ[åúÖK-EBEÌ
IV:ÂwE±È¸T­¨VG`ªiïºÂyÂèXpøV3/(<5ÊÃãO%->¥D°l»NQK
5À+üÂYMXÉä".ø:«Èè!­H·¨Ï
nms¼\±n\
±{{dÖÕELäe&µ,lIq?ãu´SDwJCDù 
oáï\°\ò~s	±¿¦J`³g«pµ4§äYÝòüªµ{×öÄ;ýýÐÜÛ¿Ç{fóìáÂÞD³Ãaäb=4ÄJ°äXß7B®oÚ)Æ°oý²óE{nd Ðº5ËÄë÷QÙ~»o,"¡=ñ È}@})7röIdYk6LeÊêsnTÌêlQ$ÝÐòóMo'Õ2£P¸R×Wmá7ôKÚSî°(nyÊÖ²úÆ 	:'ë`æ\ÖxQ_ÊÖ®@fHeQíTÞWÝ}bûJºéÏäÔïÒDæíæ©·t8¡Lûá3n#\Ì^!c}cu8µâu»Bòµª
9ºöÆ×svÏsoS4vFG¾´32¥ÆÿÚCJÌ¶©[Ú­Õ4åB>°À¢V1Vû(ù»*Ã¦.Váõ`P¦¤^)ýYÄÕäcUX©D}RhÖ?SÄ²pnUÖ©û«3ºXWÖöÎ;¦ ÕO·ñ«8V¯Þ'h{TÚ#ö³ízUÄT¾'¥´@Ë1L´Öµ®£JA-Büö­7§¨ã(ó§åDÿ=túe*q=Bk©ë
Ò{<¸=ÛsGCz£á{É}j1OÜÑÄõ¾àÿ Å%<
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/97/27979453df9d40fbce683003a3c47d1ebeab9e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/97/27979453df9d40fbce683003a3c47d1ebeab9e (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2Ó,Cþë$È8×4<:áã÷ÒnÇÆõU©Ekw}Ú:aËDÝ+Ù
]Ï
ï(kyp ÷ÄR&
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/af/d891926d328b505302150f1e64f3b8491cb86c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/af/d891926d328b505302150f1e64f3b8491cb86c (latin-1)

```text
x­UÍNÛ@îÙO1r¨@N(Ò`hG! èeåØC²cGÞµ! \û }ª>oÒ'éì®ó¡P©>x×o¾ýf3ÓÔ÷êïvxÆyðñ§£YVãÉ4æ]}²ÙÇ%o5ÅépÈaÖ­öâÓd\ËL²IZ ½r,ãÃ|ÁMÜrV.ç²¶|á¹ìØmzkßOÆ4ýÎIë}m1åâ¹®W9´,«V0M!³<`XÁ­Ê(d yø¢Á±{ÙjRº>;uû¬Ñ¹Vn3hèßll~ñÏÝÎs<ÅýÄR¸¦K^Ð>Ý6Ð^Ëk:L,Ö¡²wüc×k|v½5: ¢òïDxÃv£ßk]±¦ïÃA}ù³êô{ÝntY×?oõ[~ÇÎÒ[:WÀVû
ìmD¿[+º¶<yüõø3 ¿ã12Y jOÆUOò&ãÌÎy"?0	:áâC'~°-±R;Oò8¥Î =`å¼©ÓÝÐ¡c61âÔ®ïSÞvÄB£XcnëÒ{â !
¢TÀE£×4uÓÉ|L!CâLç]µ¨TSÏÓ±Ë&DwN¥¸>N³780Kãýë_S/fKI#XGMdæ'ÃiJ·UkHhuº}Ös=vå º¯±¿G3Ý+Ïä
 ×03§¼5~)¦HÀïoß}ÅãG)ñ]Q&Å¡dw4Lÿ¾½ìRünÀ.ùÁ>ìîj¶¾Tó8¨ÊZMïÊ¯òZTW¹,ÔÀ!GA2ÄAüLh j¤z°.<Â5UO4[Ï ~'su¡.rXlW,ã×üTÒoMek~¥¬È­Üm ÍÍðäëtÔÅEJêÌ­s×Æ¢ÔTÉs.Z"éPPõÌiòWÝUÖ%DÝºÖV-âîúÇjuNÔá©wb¥ÎMÆ"ò,ýCkný)W'
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/af/6e3fd5bc96035dc6e69c3e757e4ae0a1867640

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/af/6e3fd5bc96035dc6e69c3e757e4ae0a1867640 (latin-1)

```text
x}Uao9½Ïû+\UBK»jHèNÇµÒ^Xr«pé©¨e	K×Þ$¤â¿ßí] ç²Ç3oÞÌOtB../¯~y+W<É§üñ"ÖóMv¶ÙJ$æ½££©x\>Êä£ÈÔYÎ2}Ò@®äáÁraÌ©zÏi&æÆÄ;;#÷aHl<Oi¦%'<])MÎr®ÝyñÈ'Ò¾Æ×m
éM4ôá§ÛkEðÏ¨ã£E£^ozèöñTãýw2j<áx$ÅJS½Yñ(KÆ#&ð¾Pùr\ÏåJÿF5ä³ÑÕ¸YlÃ.nÑuª GÃ¥Î3FÖ>,[²±b1±RLuÈOÀ*Bí5+û²ºÞÖÆnË=.">Ë :0PC
HÖ"2U÷ÞNÅL®,%4úuôË}tÑAüoD>^x·ôïÁÍÚÚq72l:´Kõð# J¾tæH¦<äÒUc _Aô<lj¹Zg)Jí¸R¬[:ü«-:×·4Ð|óÆúuÍâð,¨ómX¶ÿéi\=¦rJÊì¾Ù~ÇbÿL?¼îÙêHÕ
>±zOsâ×]5qoA-ú ´_+´ÖLrKÛ½> ôà-\4MÈ:JÄÌ~Ø7ùM÷Ü8·ý{')%yÂ´°ÚòíeèÀù¾	
ç¯o½­W¸gOüòüäJdÚ§¢yo&g)Å¢ûÆCCýêä3iI3âï¤iZpòÃ²!âxZ®rÑ$ s¡ ½l@ë0x¸dÉPHíq¡]÷ïÇÀn¢_,Ò+×Âx<áUïc^¼båp_³pSÉ]¾b&×k1¥ÅûÎï±|Î`lT°bÒ»;Àô£C0É]püY¿»ºTNJE@ÃW%¸V.¢u¥ýKyÇsìøã3Ë6|+GÛFr×ùÿ+·Û£ÿñÐQâ:ÉÌÖÄ3:Û,\àJñ43¨ä}	©TF43ëåZdU!aÁMf?(gI2Iw¥
v\prÝûNÇÁßÝÌ)<[DØb¨R
ÖÂM´Òpu^Ý`>Ýø®ôÚö!1õãÚ wkZ3-ÄÊ·R9¼ë×4pîK²høZÇ;¾ÕFs^51%qÔX±ÑÁéàÛÆÝxh9rðî®_Ã¸×
Èu¯ÛohiÏ\¦wý¸×ß ÂÞç
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/af/ecbf3b817f77030dda6b78e57097cf1b32d50b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/af/ecbf3b817f77030dda6b78e57097cf1b32d50b (latin-1)

```text
xSÛnÓ@åÙ_1j_l°rã*Bâ(WÅ)¢¼¬6ö4^Å±Ë^¦(O| âx@â7ò'ýfIE%,ÙZÏÌÎËì8ÍÇP­Ô>:Yáõ-^'KY¢Ì0-%oÔlZÆ9fÍxÆ'(Ò'·¦Ír£)Í5²(áÙãRrr¯áR3µ:JDÛ^ÎiW"CèÖGÃÖGÖèwB¨ÖöáOÝ6kÝú
úakÔê÷\/|òÔ×®=x|´û	¸6é9N¹ç&[ÿZÿÌ
.áKÍíÚÌ8hRîXì"y.bPÅlK×L¿bw?ÅÁ_ ç3Zþµ=F´4èQ5¡HTªØJ©ñÚ­U¼³ÿovÅSUt£fCL+üG»UA}Hä1|6dq¶>æêªFEÖîé¢Üµ
x°á·HDà>ßý[ÎS¶ÁÝfaÐè÷¡[óAÂæñ4<0Þl»ÛjûâU+þ¾Ç&º¤èApupàCÐ±a½.Î·"Ú{û*>¼ åIªK¸ûöHþ¼8fålDjHÁ!
y§ÍFïA½ÉÁy«¸òØ·÷æz_3zÎñ÷¥OØÁzk§04cI2@î\»¯?)
\´þM	E9òk"$UJã¶ÒâpUHÅ3*Th§8Îmo«Exñ.l[âzüÅç?dÁúG
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e0/72c9f4a2e79549ee4ac83bde03f30b468ca703

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e0/72c9f4a2e79549ee4ac83bde03f30b468ca703 (latin-1)

```text
x+)JMU042c040031QpöMÌNõÉ,.)Ö+©(aØa¯whÿ7çöÍu³^åîÇ{úãYg¨ÊÒÄ¢ø¢ÔäÔÌ²Ô"½dV·â§QÓì>~êÖÑ[Ó[¶0q"+-.Ï,IÎ *übXÚ¶½I©7öÎì'ÛS®} ©­7v
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9d/24dfcd583e479fb1644a7fc11ead9b95d443f9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9d/24dfcd583e479fb1644a7fc11ead9b95d443f9 (latin-1)

```text
xSÛnÚ@í³¿b<ÄNQIS)JU¡@@Tm_¬ÅØÛ¬wÉ^È¥ê×ô¡R_û	üXgK 4Rµgvæ3gÆBáõ££»\fÂåïqR>èú
jâUù>Ú
	U\uúÿ+^ÝÔqÒ¦¬@½¾ÁM¶ß±dS®þqÃ1mSsÇmV¦¥¥ËP¯AÙìwÎ%]÷ê©Í:nÂõXÝ¤rScÅ4+,0÷Å¢¨Û?K{ý«n;=i·ºÍa;¦ü´ú§³ôKï<õ)ÝöÇv7iDÑn×\"ôÃÎ§´ÕïàõáêµÏ?oî5é ?ê\vú±Vw5ÈH öçö7n¿Ø("j§NÎ~Î~(`îÎ4Lf"]ÅÀb&Xäð¦ç$ÌSâ;.íqj!4\>Æß" ÏºWNx5°+5°ÚaÒ lB3ÐhL¸J
8(èCxëP2çÿ%
Je¨;fJ¡%Úÿn~Í	Ý©Ã2Ûí£ïR­+ä¡6%4;ïlËdÑEy4N`®5k~uÆ"(S&Ñö~Z©ø')+d8·s@·ÀA
æòì¹½¢ÒëÑãEï-Ht9µ$©IÊ*ÍUvIÑ[&(¢!Æû·ðò±RKÒdÍ@ÉiFäÍ·ÕÂ>ë:Ü:N®Êf¿`B«hÈ?eÀÇÄÕqÈ¹ñºûW(½Õð@iÀ{¬&BÕ,QÍ° ÜÜÊ¹zÒps:ÐhpÐX(6ÄÒ|Á¸±É4X®dV¶3ºl_´q¨,NÎ^WÄ uö¹£«£Ö°3»ºÿÜÁÿ_9«ÕR??úrF¡£?&Ïâ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9d/081dcc3602ee4b44068b39b7cdbd42c4624c4b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9d/081dcc3602ee4b44068b39b7cdbd42c4624c4b (latin-1)

```text
xAnÃ0sÖ+ø-Ñ1yAî9Ò
Ì@ ¯¿Ðëf°bµÃ¡7UXF!fR/ÇÏN1£_²F
HwâÜtí0QÐA¼DsÄHþÈSq1²0óìxëßÖàj[WÓ¯Þ,jç[årÿ«_F
ÃÞH	>üà½Û×ý_×ÿîÑJÕÒþôË¶J±áiímkvoß²N^
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8f/9054e670c1cf861c905ed56bd0c7183f9ebd88

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8f/9054e670c1cf861c905ed56bd0c7183f9ebd88 (latin-1)

```text
xKÊÉOR041dPÎÌKÎ)MIU°©J-È¨,ÒÏN-ÊKÍÑË°ãBÊÍÖO-KÍ+ÏMÌKLO-Â®ÊÍÏÍ/-N/.I,IOÎHÌKOM)äòõw
sõ÷ô
ðÑÀ¡TÓ mE4Ó
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/80/4c644bfb8483d23d68f5fea5cf5555ea495a9f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/80/4c644bfb8483d23d68f5fea5cf5555ea495a9f (latin-1)

```text
x}RïKÃ0õsÿc"t2­(07Ø:Äêd:¿nÉº²¬i:Öÿ»w]:dæCúzïår÷r©&pw{sr'Sq÷[±çÚ[y9o;Jª(ÈÃï¿\xóW"á+'&­RY¨
[ªµÀ-KbfHåÃ{öÇÏú~/è|w»\4 7|yx°¯ç'FÀÿðzÓq0=$s1vÇðMJïa:ÕJJV	 /²åL2cTÂf2RÌ´ûMëðí8ËóàUD!(Ðb¥´

%pX`!IÎ¦¦HÞØ´V}n¿­=	rØQ.µfoê,ñ¶r[Áïäíâù%ghaÛÍcTNT~²Í!mÑ
g¥m(+á:*Äê°²?YÇ!¬BMÍÌUjÀ¿u½nà×	=¦ÏÒSìÇ¥+þ=4
ýîÀ­;£w(Ä}-ÐÖÇ~i/ëýÖ¶ÛºÚ]]ÒÅ¨¨5J(9-!³RæØ#Ûó
:Y¾ÂL'i:?Î/Gz >
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/80/0acd4c49fb8fa7d7604603a506ca876a2b3a68

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/80/0acd4c49fb8fa7d7604603a506ca876a2b3a68 (latin-1)

```text
xm±
Â0Eó²(«¢DJqR\B¼Ð1&¡¿o:8ï9¸Òz	ëíjÆÉ8×FÍIÜû±5ãÃ	Ã89eFØ¨ÉÅeWý3é½!ËLûBªÞÉ¶ç)Ðû¡ßPÞ0¶ðé1Ôc&e9ñä,@
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/48/828f1be3a88c3e914008f86ed28d6bf09e0091

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/48/828f1be3a88c3e914008f86ed28d6bf09e0091 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`È¼ÀïsÐÈìPÈÕ-åRe!UÈêâsRÓJôóóÒ¢é$~¿yºÛü¯«Ù
Ëð?fJóËRr+º¾«ÂñéÌÝ{
ù½²EuQfzÔäïUÇø=:ß÷nLUºbIëíê;±¨ýýQC¶tÚ*ÿ,mJ~2ÁÄ 2ósJSRî¹gÏb=P'{ÆÖFBh­|&DEqQ2Cà2;×OIyãÄ÷æü¡©ü~yPëÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  R
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/48/f41d45d6e05e9f8f257c86b2fdcfe7bfd54ed4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/48/f41d45d6e05e9f8f257c86b2fdcfe7bfd54ed4 (latin-1)

```text
xKÊÉOR024e(I,JO-/Î/-JN-ÖH,(PòsqåRPP©vöuôvw
rõ÷ñwñªÕ/M,*/JMNÍ,K-ÒKÆ«6-1;5¾¸<³$9¬R¹Hjã3ó2K4¹¸ªR2*É9¥)©ñ)@Kò2V©òõwö÷sót¯ÕªÐä øJ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d3/c0f03054cd0554ba92180c904fdffc2e123039

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d3/c0f03054cd0554ba92180c904fdffc2e123039 (latin-1)

```text
xXënÛFÞßzSkHbËv/;ÎBµiW°"¹²nVð#jdMM
9tì~¢?èSøÅzÎ\È!E'YÂ0)ÎåÜ¾ó3ñ¾ývoïÛÏ côpqË?×¹ÀÀ_éão1q/ÅÁ³íÆ×"
ÂlÆáå¾ZÜ'Û7<x¸µxµ>4ã·"àõC		K·Ivíú0¾¾Ñõ6Þ+7j;?}/d°0 ^þðÔ=<¾ì{þÈ;í]½Q³Æè6ÐÄ¾÷Æëû½ÁIë Ñ@ï\vGcÐ@ý¥CÊ!(ñMyó8óG·ÈK©dRè¹(Ê$¤ÝãL^C8öÞô<ÿxìzã&ÞÃc¯ßýÁë+
;-£ÅX¬âK.cxq!K%íë÷fìyovGÇÐ¹ëì4Ü×ÃËðÂ]eÚ9b´§+°Y¼Î]·{5á·h/ïWüjÄï¯&A^MV	OS>Ã_Ü¤Ùò
_Áw0½<uÎD$ÿåKfsÉ÷WÖ#8¦Ð=>èFùÝÏüGîG®YÂÐ ´¡¹b]Bg/OÚ°d)°ð&y¢mÀÞeÂFECEAª
lw¬úôûHÄCóLTõ"zA]^Ó«ôëb =Y?`¼[>À
¿/~Ö3ÝóH }í,§×V¹i&%³Xó Ë8K¹~ñpÐÀ¿9Sb0öºô.=ÿ¢÷_L£ÞécØÛmù¯/Nò½ÞÀÓI¥·L¯ßéðµ!x<oÖ=ßj«,{BL¾±I°H8ÔÎüñ#¯{ì_»Gg%ñzÁ¼ÓÙ¥Å&7¾Ô)Mô³?céU:íÏ8@¼3³nE4ÃDÍE¨¨ð63M+jW½IS
>cmÐSû´ôZPÌÞ/DÈ¡¹Órwã+ç^sÙÜtéz|SiÔ3ÿd8ÂèÈ´]¡©ælÝ1Ù]Csùd?_N[(±gS±ÌB&¹1¼4æj1æ-Ìö'17>5l2þ
HöaÎÂöC+I¢½¦ÇðÜ(Ee]Ðb%f«8ø 2$[NÿX¶aÁ¦"4,Ø!Ø*W G¦M÷ªxdi²,JÎÏ£AsC¹)FbK±j Ã
"ävvï6ÚÆN¤jí´²EòG,§º½@"É`¥¨ß¥íÍÁÔ²¶|a)´XFÎHTâXL[	Ó»£Sÿreç¸YÌ-#[!i.æ1v lÖT»om@Ä¿I1&Õ§t`íÍMà+|ÂÒåN'o RD? ¯.sª\!C@°ÐzË:p]ÒKh"©¶å­ULJ>µÐ+VÂpÄ®Ó4:"$ü»®}Gl,Xx-1jRÜÆcÓ41 1®þ´É(Û|:¢
ë Ä:h2ä²j¶}Keö´×SuÙÓ=÷w¾Òñ*×M,Tû>þ-Ä®¦(åm|T}`nE8oM\C×£sx»ÕHØYª¸OvÐÿ%>«Î'õkMüNgB}ÑtD
0q~JÅCÿ§&Jõ<{¦ÃhÅîÃXH2È^µp£An
r\GÛÕ9EU¦ÒaªhªsgªÀÿÎU^´[))tçgØ{m*P¤¹ëP£·úôSA4ò\£]tØ*äO5~g®½¥ñHCD2ÝkÐRdN¦a^·UûÏpÔXè6cøøW4Ãcì Ä¼Ø%Âó JEÝ¸jiÉ^{ÑY¸
JÛ9ÀÛËÒÚñtGcÏWU¦mlÿ;txM¼Bw'³é'9/_t\ ¡Æ¥(ýªNr´|§ûh´!jø!ókôÔ#ìewkVe#iJà«¼HSjLTÇs¯´ë5 s](Ò¢?Ó/b´?ÓÌáï"HÔÓ»ª(°Ó9¯´æ8R­1Ý\IÈn $­èý°¹+ÍÞûälÛë¹F|SYáp«SôGìæWe¢Ð­Ù*F)ÖVá³§Í1Ëîk=m^f_%_¬YV	fsÅþLç¿Ê¾¤óý»½q)î´uLO¥ j!Ô)3GàFyV÷¦ø½ÛjïPÁêgRæséâ4°EWJé^| òéû:dÙÞûJ§ñ~\ÀnòÞ|å¡o-¥V-ïÜ;QLnÆU®qèª,4)#UÇ*w~`:k?ïm}ìÉm}N²ýtý¾G¾KrçãiÈ8G%«=©ú*&¹9î­X÷ä[Êu÷S3ä'Z¬³¶µ~£
Â&Å®6ªô¿Vö÷mèÐy´@¥FÀomÍ
µ}9ÆÔ¥ãg³8âô¾9ÆSu«î§÷é:,ê&*ì8è ©£ ,Çæd >0ÕÓw¶iÈÀÓ²>öÅ¡P_E±RG1~SøâíÑ¡jõjC÷ü¼ß;ê{ÃAÞ©ï¼S[øç£ÞpÔ¿EÿOd
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d3/c007b213cfa2717c760f066a0e35a1e64a5957

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d3/c007b213cfa2717c760f066a0e35a1e64a5957 (latin-1)

```text
x+)JMU°4f040031Q(M,*/.Ï,IÎÏIM+ÑË`ÇÙåíö¬eÎzëÛËN°ÆT5ê¢Ìôò*M3æ|»y:jç½Î¯¼Ç
o(  **
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d3/f5a1058084d6358d6110cb4942920a9c76069b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d3/f5a1058084d6358d6110cb4942920a9c76069b (latin-1)

```text
x+)JMU047b040031QpöMÌNõÉ,.)Ö+©(aðø"ëzíAÜü~Õ¶MÏ?ßÕï
TePa|qyfIr^2Ò\¾³lyõZïdDúêì}-?¥1Ægæe U«X('¬u?ÿ>FüïunýnÏ ªKJâRS3ËRJ§ÿ\bß¶ÍÄÊúâ¤µ{¢ÚîO>	 öJí
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/47/a13b05e7ca46c2233a0db82895a878569348a0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/47/a13b05e7ca46c2233a0db82895a878569348a0 (latin-1)

```text
xTËÚ@Ì¯h­/´R^DâÂÁöÄÂ/ÇHËed`´dl1Ò~Î*§öOàÇÒm0Dë3ý¨®ªée^.áóp4zgAPÖ]dË\Ü(xSµf*¼PzátülQp<²Àýî1%x	©äCÌUQq¶Ï o_FÃOð>µäpúõ¾:ý,aUnö®dÂgûfJSÆR1áÍyxÈçãb00!'±ïÉþÍ¬\JÑt»&]û_F|³;Ñ5ãNd]7\H"fé÷è4qãsÏå*¶;ëÀÓË\e»Aÿð¥®ßaOÀ@ÀÀ»AG­QÙ=4{³ÅãG¤wO\JÁãiÏ
x'vêKåó9÷Ç_»¬ÛË!CN¢~`1N¥PZÎÌÞTÅÁáyÈ)`Ìû_7ØÍ1¶§ßë:?{«8½uþWçFRÁ]F4Þy
ôØØèî6qdøÖä½X"âh>èiUJï¡®²b]µ¾¬¿ÛëÕ¦Ê ³ ³V¿qÏ3&*Äk"ºåûm1^Ök¤¦kÚ°Òºñ2
÷ð^öª,ª÷ÆD²(ª-bxéFOj`>nü¨5tq EtÜd{À_ÃTW¹8ãgbØµÞéb­aÝm$y¡wOÏû¨Õ=è-dùc]T°Êª²B{`©svQ}(·§ÃfU"F¤ËÓ!íN/ð-79Â\5wÒ¸UÂ§S4d×+)&ôóUwGvÂJØ¡MÉÝ¼)ÅjÐ¾Mtp½áàæÑyµ ú¾¹
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/47/e4902f5958414637dde5b450e3b8072438f485

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/47/e4902f5958414637dde5b450e3b8072438f485 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Ü£L6¡ÂÁ<©yßÅkgÈ.gXRÌzr|ºÛcÙj«;¹­f%BMI*ÍÌIÑ«LÌÍaàð\½(¾àösÉØ¥"K8\^)Î°øþ2æÛõ3ÿßÊ96E,jÞ*Ö×!
ªR2*Öîú´uÂºW*³ºÞQÖòà SÛP¢
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/47/a8080207114cc8cb496af0ff95a810479bd8f0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/47/a8080207114cc8cb496af0ff95a810479bd8f0 (latin-1)

```text
x½VÍnÛFîÙO1P!1$")ù/5`¤nb@h×n{#VäØZxÉewv\7§>@¢çÞ{ïôú
YR2¥¸H åAZÎ~;óÍïr®ô¢é8úbg'Øø?ûû×ßáµ.¯åMm\\\B%Km¡Ô¦ªÀÒ!ì;}fÎ(xÜzja\æx-jå×_[Ãn®«qGÀÂÊ¢²ð¼úöâôü»ÓÙ6^þ8p ÓÇo¡Ýg~ÑÀ÷_­à%ýuHZX-)úÿ û£ôý°Ò÷hX¹Âçè³}ã«uÂÕ´¾½æLVCùÚ
1çÇ(Û´	¼Ó([&l1î |6öKQ ·Ýæ»7Çf´$æ¶]²£.*á$¹È¼o*©hÉ3¢xHIrô¼Çx_%}^p oÎÏÞ¥'¯/Ï¾?Mß½y{|A D­Ð¾f!§¹ åª*XsTLãÊ¢Ùé×U#ü}\) zÄ~C×[E¥Ü Öá\¥3whF\×e&u)W²,Hêºl¡-åðsq;0u9ãBÜImØRFV4B¥K±7«kÈ(ã]yc_®ÑÞó÷#n[¿¦(äù Hk)ZLYC!*¤ÔNSØüQÈ¥Aé´?vk3Qàÿ;×óÊô=bè3\gäûNts©s²ÞÌÎA¦Udô=ª¢xiôO5å°@b.ä{âD©úé
è0­PÈ§ÜïKt /º3{÷üÒÐùÕl^ÿçi.ÚßZl«!|ZC'oObk
­5L·Ö°·µýÏÐ°~ù¾H©]K{M×iÛJÃà3ªé§§#Îâv vztn@ªº(½xJânÍh(.ûtVWþú£¤¹@³.JF£do¦ÁÀWï<A£¢	}>@´ÔÑÁÚnB<888x²¾;xâ} 	!¯í&$1$	Pµ'Sèðh£ñé¯ÝgcÄ§ÒrrÒý¨¤>ÍTa;ù;(eU;ºï|(yl
X-ÌÀÃ{~º¶°ÕåbéZPº¶¸BtL}IßPªÎz£Qps-L>Ê½ÖêâÛÁBX¼Ñ¹,t@S¸2ºÑ4!ùîýìVß¡u©ÖaI7¡÷]¥­ÍoRËÿ_H»×
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/60/50c7b123bf6a5123ef898b7ff654a4fa3db5ab

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/60/50c7b123bf6a5123ef898b7ff654a4fa3db5ab (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Ü£L6¡ÂÁ<©yßÅkgÈ.gXRÌzr|ºÛcÙj«;¹­f%BMI*ÍÌIÑ«LÌÍaàð\½(¾àösÉØ¥"K8\^)ÎÑö§ÙÙuÂÏç6õü´jvÍÚô¢ *µ £²aí®O['l¨{¥2»¡ëYáe-N ?PS
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/71/d460b6354ba5a050fd3c90864744f58c17b872

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/71/d460b6354ba5a050fd3c90864744f58c17b872 (latin-1)

```text
x+)JMU03µ`040031QpöMÌNõÉ,.)Ö+©(a¨gäú®þúéãÕ%ó5&îý;û/Ten~iqj|QE|Puj^j^2ÃY[÷]}w:gúÖ¯å×^=»Áj°EyqIbI*²e·Ë¹^9¥sNÙ¾¶+e
±wQt¤Ä§æ¥-XT³¡²á×yî &÷°«/ªÅ=æÿü5ÇJ`Ý¿×A:ók|ªyo9CÍÍIM+:»@x÷Î¢/òÙØ¿ø¾P±kâ\deEé uÝ±óí_ï*ó¯:O0Oa"s/T]ibQI|n~Y* Ôäïß-Íl3¾þ[z>4ôgÔ|dE©É©e©E0õjuÌÞq
oÉ3×mð¿5ëÓ­7ó°ª9ieÚ5K£¾ºÖñuÿß}`I±&²âòÌäñb¬¾+¿µOj,yþgFãÈéXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV¨òªÜl¨O!Q$Ñ}KÙÞ)xpÌPù HÓQwA!2N½ÀYòh­îóo-··¯ó ©3¤
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/34/7a6e95a10762c7244dd4c9fc1e0f114136e911

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/34/7a6e95a10762c7244dd4c9fc1e0f114136e911 (latin-1)

```text
x­½n0;óÈ KÒNíQR¡Ò¡EðM°d0µMúå:õúb5qÚÐ©3çÜsïwÌñº¹¾½»²QP¤¬¢PêëSP.AB@HëÊìM`ZàZ*.(H§·{±7ýà¨pÛÞd8ö±·"ãÅly>¾¢ý ß?°ld£/ çU	y) B¾>HâZ*PXòJ¤z¤,Ñ<
±o!ÔÛý
Elbr^IÀ²dTaØB¡úi«ÁVÕFë\Ë¢kÇëÛó0q4õIúhºz<=W$9,!|®@^kÝºmï*
kö@· 0µYü¬E¾Pfr¾l(uJ1(A¼hÖÎ5À¨TPè`P ÕÏFäÇU¢ ÿ¦hô®Lc e§êMÕv$è&»¬¤®6î
]¨7{U¦WM° úp­oñPbJ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b3/767692b880ce74faf260bdd4ea26f5a5748384

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b3/767692b880ce74faf260bdd4ea26f5a5748384 (latin-1)

```text
xSÛj1í³¿b YÃÇ&½@ÚB×Ô8uí¦/BÙzµ´vâ¯éC?$?ÖvcÖNh+½ÍÌÑ£3wRßA·ûæôÕk¡RYfpoLG¨eéªûqþ©õ,áJ¤ø3ørxF¡<¨,\¡r¬àÏÑ<Ü8f×Â¥93b;Òêt`PªÇß¿4ðò^HÁ
,¹ájåßËÃTòuÜVZd`Qel¨Ê½g^ÇðôjÙ- ÕÜÕ¢Üaµ}J(5gJlQ6±¹6h­ÐP¿`Ë¨wÒ>ûÄ\Ú IS-ÝhÛÐþ,7È3 £shVÍÔ{PT[+ti)FèL¤¼ ©qO_ÌBs1òByëu.$BÔ}ÒÅk³`Uk#6M.®ÆýiÔkS!ßÇ;]CEÂ«TpÐ5¡f%íR	å)2JÈÒ«9fT ë¨ýã8»§ßÝ¸T6Øÿ¿­d¯ËPâ±#CH
VtäRj'ï_FÍè%_ñMÎÓ$ÂÕA·afÁ¥&«
IÃñõ
$ì[ìIC8ÜFlp5!¼Imá¿@ncj0Xn¢Étê"L®ÌágÀïá×ÎÿõÖ[×û,Ø»8º=
ÉÛVå²CÑ$k´Flöy÷Y?ÇIÔ0È|½S¢xè¨Æ7û÷w¡? ye-
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c8/0efdd526f20431962c21b68af1ee0396ed57e5

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c8/0efdd526f20431962c21b68af1ee0396ed57e5 (latin-1)

```text
xUÛnÓ@åÙ_1R_lH-HM!jnjR¼¬¶ö´YÅ7Öë\ò5<ð|BÙuÚMÝÖ«õÎÌ3ãÙãK?ºú»ÃÆ=º~ê!|¸Áx²UÆ©ÊÖÉ'kÇîáL¸øII|Ø<E¢/2Vq¡bù5ÊsRM0L"Éó®SfM´!OÐS.KæB¹æã2±^¡×w¾³Ïîê
ko}ü³wÆÎÚ?z­!FqgÐ·e4¯ùØzïÀËBô+°µÑ±¬jNÓðöïíxº¾àb.9`8Óû4à Ðõ¹(®³Hx@xlK;¡:f
LÂÍIüÛzòõ$"H}®Ð¶¥X%StäLdDD!&|ÊÄGíFÍi>ðûA$ÀQä«ÁVÅâó5G`¾[DÀ[ ·Ü-?ÒY)¢k¯Ûà-*°Ù.ÈzP®`ÊÖcáNxHÃÅ<®8åãÚW÷ì`Æý!´9®Ó)å0ÐgúÑî
}¾¼;_eÛUÓ2®»LYDyj,7Gý¸`×ý:!£D4)ALÆ)KcýÎ®QÙNdÝz¸ ¿Z-}5Éõ6×1Ã×6ëz¨Í QQøÎYÌ¥b6FvyP{_èèvºk¨;ÍjõWÁ|)O³iÜ"ÔËaþ$Â~»ÓÿÖêã¼Ö8øþ ×îãjìziúúy¨¢ýv0]Ë4z¡ÖV§_óFã,sÚºèËqÞjô1RLúªâXC2ÆÈY&1JqûÏ.Ä~ä´BÑu ÐZ¡&49­t3óðl#9	0X£
ìÓh\§ú
ÑîW¨¢-å­bÖkµfÞglüõ¼Ý:a'íÓN¿mïðbÂ£q¯5Iïs®@ÿ¢Û-®ÄîÎñÅÒ6
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4b/9f4db6fc8c4a2be3d4e10829ed21fcfee36e11

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4b/9f4db6fc8c4a2be3d4e10829ed21fcfee36e11 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2ÓlWl:úþÚmÑæû!«j?²k|QPZQYÄ°v×§­¶LÔ½RÝÐõ¬ð²' GSÌ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/96/8b52716240738d962b769c8622f2f58c601a86

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/96/8b52716240738d962b769c8622f2f58c601a86 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLgØ'ä^^6íÒû_Úg}÷ÕÑQPZQYÄ°v×§­¶LÔ½RÝÐõ¬ð²' ÑÙU{
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/96/2daede3ec4482d230c1556aad1568e2ff26c9a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/96/2daede3ec4482d230c1556aad1568e2ff26c9a (latin-1)

```text
xuSQoÚ0Þs~ÅiSP#Ó¦Ik tQC@nÒ^¬\Áj°í ÂÄ¯ÙÃ~HÿØÎ	A®~È9÷}wß}çrvûó·\¤y!\íp½Ü*ÿÀ¼µüê¼r¹Xp±ðÉá«7([%"Y :»Ö>mÙJ6A.±À¬µl8N4¾f£ñà.
Ø èG½iàR¸ýq<¯ÙÏÑ
³!Qð=ãû0,ÄÓß§?²ÌRaÁ¯!ãz¨Ê¤jÏ 6H(³;É³jË,ÂªÃ®u7á·´î¥ºÐ¹$sÕOd/.ê¦*R¯4F%ÐéêBmW+{$÷Ê,Ë:·ÿqêTÉ<g6¾}ì©sh^#>EöÄXOyó]D*Hå~_KÚ*xgqÓªÂ[%»ä½í½ÿ+,¦¦S_
å¬$VA0ªd3ÓÄiíôiðñM{ámàâÆJ nÈê"ncdµU*á³/=vßed[2
@@e¶Ïï aêqíÒ»h7/HB½FQ4.
a¹F!¢Ê*Ø;ûR¼çá¨DÛAù¦6û6
zÒõ0·zÏÇ8Øiøè½¥ñ]|}×ýÛñ#¸±ÞdýÞ,ÇuÎÉ4{¤ ¦ïy/%
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e4/aff67d017e22770c18a19c275f8075cdf399d8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e4/aff67d017e22770c18a19c275f8075cdf399d8 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgØ;ãï´³6j¤?øÔûdÚ^ªÔÊ"µ»>m°e¢îÊì®gwµ<8V
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e4/3d6dce064c164d0d0049e53a7746dbb2f9420e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e4/3d6dce064c164d0d0049e53a7746dbb2f9420e (latin-1)

```text
xÁ
Â0y»+ ÐÙG,!Düy/°c84D)4[à·»Ò¬FJÎ©ëhSgUpCVfì"ï½ªD!²Î³"C óâY§
lÇo%ª·r#©xì¤ï[bô×ú(3ÜÊ:Ã³ÂiÑ{R.{æôÜKÉg°G²DH®zDÓÖæWõÒT]*è»Yn¡Ý¼Ò!óÓ÷S`\'IebóD¯Oí
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e4/74ea33ffbf46b431d47cf75127c9be52e5c9b9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e4/74ea33ffbf46b431d47cf75127c9be52e5c9b9 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Ü£L6¡ÂÁ<©yßÅkgÈ.gXRÌzr|ºÛcÙj«;¹­f%BMI*ÍÌIÑ«LÌÍaàð\½(¾àösÉØ¥"K8\^)Î >¹'ê¤F÷ÞàÉ+ÊçY
ÙAT¥dT1¬Ýõië-u¯Tf7t=+¼£¬åÁ	 ¿M>
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/32/a3a6ab2d459519ddabb11834c991d844ac693b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/32/a3a6ab2d459519ddabb11834c991d844ac693b (latin-1)

```text
x}UánÛ6Þo=Å»'m¶aYh
ÉìÔv:tKÈ]%W¤8fÏ²ÛIÙí?d<Þ}÷}wÇqáøäèç^Ê§e"à÷'±.Ã(2¾~ðvq/¹ØTÈ{Q¨Ã2.ô^ÉíùÌ3õ 5²TLwx·A6§t¬%gJÒEÉµ;WÞÃyø9:Ùù]Ãþt{çáuðGxÝ"N»}êÛçZï¿Á]ç1Fwâ^déåBîüatÇó?SÁgªªð¥Ìô¯LÃ¸ÜN«mÜ¥-¶ÈâèØ0!¡ÔeÃ"ÆO\Ìã'ÅX¹L&9ðÃ\U¨
²ÓÆ>¢ln âSoecåóbÈÔ!På"/4ÇR9
ÃBIì½LÄDf~»Cöé6¼
Ù ú;·ÇÞûspùQ74:Ìsõí»J>|ÒÚRÛ7Ùî8õáÓd c>zZ8±-¥Ö)KÙ~ìÁ9³«,>óá¨sL~]É8<3æ|®íÄ:FÆîs@]¢e¶_Å>Ø?ãêo{V£=©Z^Ñ'iø0©ÖQÛiJ{X¡BÂQ¼ªÊÜ"«#NÙ7¡[5`èS>\±^êtÖ8ÏSXHH°éMÁ{,ÐÇÎ­º`Ü»îSr^¦±¦
[ö.ïÜ`ùoI·WÞÊ«ÞÐÈÇ­½Í\X*Qþ+2«çMò¼ä*£e<p¹
 SgVN µîBÌÃÊ7êáiâVñÇ(.ãtÍ'¦Gö´¨ë]×¯GHn·¢l¬Ò«Ka<á!ÕªwA1±@9ÅÛç,Ü sfï1ÁµHX5ðÐ¾ó+¯ÈNVJz}Þq´Í%¹Ö&euõÛÐ%ãd¤ùeF¶Ìîÿý'IÞ¸VS¼<ÛÔÆE²n´F-i×Ò
Bí°{f¥ÀoãhµEëêEùÿ]Ýí±¿hè:PÒÚKÛÊÄ3M¸é¾BpA1£çÖL±ªÇH¯öEeRZAÞ®U|¶²ª¿MÓ²øÎx¦c²lÝ¿Lá¢sßs²{{}íà¯o¿q*l@GM5ÇöÖÂM»Úxv^Ýhßþô2õ.ìSd,Ú»Úw«h3Û-ÄÆ·¡]¢õ´I6ã^}ãxÍ·Zª]Î&FGåº ¾XÔ6>77×ÑY0z]ÎzÝèÕöÌevÓzýhø#üz%ÿi
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8b/5d9f3febba764f7d1d959e116e209e21037e4d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8b/5d9f3febba764f7d1d959e116e209e21037e4d (latin-1)

```text
xTënÓ0æwâ0H¡[aÄuÒV2µS»!àå&g­5Ç®l'kA<
?x^ã8*ª/çú}çÏ¤Á£'ÏÞº#T.«áÕg\.ÖfpF¡ÜYìE"©çs¡æZç¬Q9VrÅçh6Åç¸.ùró~^}EÅcöB¸|Á/Ü5ã­Ïå9+ueYÇ²|ÁÕÅVeã·ìhüæ4KØdíOÔû0Ó·ìÓÑ;æU²ä}õ^FÑÏB8Ú?¤ØpMáÑîåµ×|<Ú?fÇãizG±Ñ}ÈµìAì÷=¸ÍúÄ^Ø¢Á +õãûoxµRpKn8 ªý¾*98Ì%<C­EUÁ´¸Ê=cÝ¡	ü%ú]¥É²¯ËûàL½¤MÙ´¶1%­D\Æ»ÿvvÆ¥m¼³	Jäop÷5êð r+&u¨Ð=Ê:ðUãà>.z@¡¥´ó sC¥I¿×À-ûC+Ää/ÀgßÆºóî^ò»Û]¢°| ]Ñç¨4B"ç¡hµ°
BohÐUFïä=}ÉèdIE¸½ùÁ©º t­¡©©cJÐJ´%-5ªÑü¬Â"ð|bEg¬·÷Uÿ2¿bÝÝ®¯ÜÚÜh)YgÑ75:ëVãªYåU­uß¯4E-ìk®óÚ[W¢à@¬l)¬õ#ÑLñBiYÔz^'ûé4t?§mt£:ÁCê­@f7=ûð8T÷¹×üà§£Ãx+ñÒ-(Ý0´£¹»ÂÁö«×w(Öþ¿£íÊ¾¹9EW[¿Øô¶	ëºß¬k§VÖÚýK£ùîzµ½
CmhÒE¡#ê:O[NOQ27æ­¿9ÈÛLO¦ÃIzÜ<k7ØýaºÈú'v
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8b/415ea0d95109f5226eb75089b364af7c8c39ca

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8b/415ea0d95109f5226eb75089b364af7c8c39ca (latin-1)

```text
x­MnÛ0»Ö)8iã$to¨N!Ä
Ùé¢-N$¢¨)7?Èºêr±PS«( RE×Çyóø
·JoÙùÅÙÇTj$Ð¾þ$©
È
äÉOX²-mUf5I4áÉó×ë+7ÉçÓCE4¬¯gWsoÓt~³õò6çð)I_N§ÓãÁMØ¥®,²LMÉBeMÈöM^¹Ë)GF79;¼®Ù*M¾Ì6swÈØÉóïÍÉzÓµz*¿A©`,·YÁ«Å4sº(ä]Ø
í|ëÕ"Ù@º\8ÛÎs:[Dsöb¬,qÅBÅfhî$¡Û³_ÎÖ¯/Ê(¼³ÎÄ|6+FJ½ÃC^]L­¤=èá`j20I®Æbä!°hÞ(rÛ&­BÀ{>¢Î=À_}LFÈöãô¢ý{V¿Z¸gTÃ¶¬<×.¢´ÿ7y1¸q}ÕP.=$|ú	QlëöãûÞè<÷"»#Èþuû VîöX}õ1[GO%ÜOoè}
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/05/4673e55a96a0bbc7cadaf815d8b56784b40209

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/05/4673e55a96a0bbc7cadaf815d8b56784b40209 (latin-1)

```text
xVÛnÛFí³¾bâÀ1¥¸Ha')Xv	« ÑnÓÖXPäÊZ&é%i[-ü1}ìwäÇ:³Ë¥.Q"÷vvÎÙ³3%ÙºïO»ß¼iT1ð|±'K.S¼]|j}5óGñýCR<rYÜå"ûÏ	U(Ë½D*ö«â$"-;ëî'Æ'QFl½ù\¤^
G}ús¾;µ;íVQ¥ ÊÒ¢¢UTÌbÉy8
>ÂåØ1\:{=véÁ³Õì¢}ÞÚ¥7Âô½¿çaàB¸?xf8mÂ99÷.!ÂlUòâã"VÔcà<-Y¹Ê©!³'ü²Äì^¡,ß±fÕü·ÓÛsÓ½ÔÅò¬À0u´5å%+ø=(ñâ°©uÞºbÁÏí³iàö®Xß»ðéÆ0 hiÃ·.\KØ ÉÃcú¤&è±C.(¤s*Lãª{ÈÃ(C_þJö|ù$ø¿[Ð³D¤ËÙR½oBôÇÌ|DíÖ-Àçi!V§
ºM},+Ã%·¶(ÛpÅ.FïÆ /J²C.R¥D[XGÈÌÎÆL8Ï­+öÓÔëYG¤^ýoëzýKë¥±"¡"fÖ%ðm(VJYCÕ}RÓÞ5u7óÑ±X
á("ð	M]ÐxzÇK<"dÚ|Êà<»n#ÕX
=GGÁ+üÂY°)EZñµªÈè!¯ÖHÇÇ·èOÃw¶9ÝE6¬7®ÅGØ¹=@JÎ³ÓALäS6µlIð°àM´A¢;¥!ºQ?Æ[{à¬¼Û^U®©Ø,ÃÙ*Z6'ñN}~fgê¬kwÁaÖalÆíßÓ»ÁùÆÄð Îà`¢Ùá0r±)=l`
äXß7BnnÚÆpètÙû¢=·¨¤#tníZxýîÖíw·¸ûÖ"2Ú3ª2ôJÖ*÷lM¢%9eMå`=â¾JÂ[Y#ÁEò
-ÿ°íñ]Q=)31
+¡äQn)l6ÚÁßð/aêr5o'§ì,kn&arçcDHÊÍ¹lxQ_*9¬³%CªªJ£Ê}æîÛW:I0Q¨¾¢Lý6ÏdÙÞ¼3æè)ñÖY%ÍHé0^áénêU2Õ7VÓdB¼ÎsqWI¾ÎªB®ñuÀü¡ÛüÁ½ÑÑ©îL¹ñÿ¦öÐ ÙMêÎÖjò,
dU5yò»*Ã¶v\Õdx=Ô4+å3ãi8K¸l8Ä"ýIUb³þÙª Ös§²Ný_½ÑÅº²¶÷Þ1°Yýtx[¿£ñ¸y¿Ç´G¥m8b?»~`"6NPzOjk¶ci/¬k]G%AcBüöµ·§¨ã¨õÓv¢ÿ:ý<EøíZûÚ@ÚàÇ¿çþhhCo4¼ð/ÙFZÌÆ4ñÏ¸Ã?g1æ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/4d/825fd7f6f45bab87d6ad6f5b4147ddd2874eea

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/4d/825fd7f6f45bab87d6ad6f5b4147ddd2874eea (latin-1)

```text
xKÊÉOR04³d(I,JO-/Î/-JN-ÖH,(PòsqåRPP©vöuôvw
rõ÷ñwñªÕOKÌN/.Ï,IÎÐK&Ve|f^f	P¹&WUjAFeP 9§4%5>%³(5¹$¿(èê(_ïxg?7O÷Z}¨
M. f¶;
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/dc/e3f3bf2cbc50bb78d4aa6420269e097366095c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/dc/e3f3bf2cbc50bb78d4aa6420269e097366095c (latin-1)

```text
xµérÚF¸¿y
zDL9£;NÙa!ÔaèÐXñÃtú(y±~ßºqÜÕx,±ß~÷¹;w¼9yùª}ðKó?¤>3}Ç|êÛËUØ0Éo~?þñH`ß®{aeµáÄvÃ×4$®Gn½(`äY³òÔvM'²yó­W[¿i±;ÛdÕÛ&2.Ý`»v9àù.sJqo¹´ÝeÞ9øíM¹ÖÚ©"he[ÅEvÇÜÞ®±d~Ì-|µCs%íV³ú
9" 	Û¡2j®wÉcµRéÏéå°{Õ×éH?ï'úH+ñEàÆ¾þQïÓÞà¬vT©Ó®:£	6Fó#uÛ$¦ç!	B?2Ã*h¢[É1éê{§:íNè¹>Ñà5võ~çDïsÞ­¤?±×^ $WÄã.¶ØÂvÑ?Nè~}2ìº¤µiµ+OSËáÕX'ð äz-Ì'¢F2æÑBØpÚ~5;R  P½²Í!³¨ÃÜô4#ÔÒ.ÜÂÃ<Ø!¿WPb%Û5;ë®í¹rît.à£}ï«ÀË	ÀôrÀÚgAÀ¬xOnØ6ùYÊNZÏÚ$û¡ZN¡§Ó÷>ÌLx¡çÒc,0ø$ìïE1÷GøC_ÙNÊ
A:0)Äõ`B?\éW:÷>C.ôÎßMÈóÊ½ ]ý¬7ÐEfÏÜË/Âåu(Nß·Ðvº¶Vç·M¼Pñ¾òak
óe¼ w#½Ó¥ãIçô"#ß£ø·[HBæã5ñM-#4æÎ³-Qxe°ñý¬qà3£NÄÇ\}µÊw;µÙ
ôÑé_W¶ÃÖ®¥BªoÉBm/iîqêä
GàZéá#Ñø%ÍÃ4 %¤Äa$8[Y<¡µDÖEZfîl VõÀ\e?FÉÂp¡Z"GõÌ!nRÇJñúv2)bH$ÉñW{PÊp¢ïµu¡#o°PÔ¢amó»¶%»TnçöªåÝy$F$2çs,äjfZWv×XAA7åú=´ vËzäóåÌâQ§7Ö!Ë]¦¸ÞÇü¡;fÃê§Ñ@«êØ©=ètÏ3mË;$¿¶6ÕºôûÁc8ÞWîyá;5gÕ·ê¤ñ%©oÎeÜ¶mhî*ñaÆòyýP@5S¨3:§Wè»]-Ù­<ëöÂIÏ°4N|Ï¬¨oI+¾öh¹Ö½ìí<¯M§ÞæùCÛd»Ä0¾ð)Ò{C4èS5Yºã 'C¦yö÷g>RuäpOds.ÁÐ¿úh¤UOÄøáÁÈ¹p h·,4\Ë«æÝY8¼zvM
ïÿhãcr×ZÙÄit=ÎTÓü~d[*Ú«#BM2ítfSÞÙèl
¥r6~AÄßÑí,öÒÝ%
¯ãuAk3ZÛÙTkõñçCFð¹¥4Îf[a
ºûñ·Ã¹µ©S{ó;j0/6q9ý¹d_1JRr¹QB2ó-'´ÂÌwB\¤[,<§±Ö>×ºpüCØþ~ª¢büuÌejÃôPõ¤ÔÄ%¥êHâ¢VÈ}VÆ9vó©Ò/v5Ì$õ±p7¤¸)?kÕl_RÒá[S0YÝ;çÿ#b2öüÉÐÞüNRüNLU$ßÑ¼±epQj°]6äHar 4à»¡ìdv?p·ØÒJ¼Èa¤Ô.Ev*®ºPRxybÀÍF-±Ün¥$òVà"ïÖQ «á¬9¯.òzfq|ÃvûeÎVyd5Ér¢+¿¥6üÏ`8û/ä)b=æ1ÒOÞ$Ws1üN»2·o~~Lµá<ÄÕ£\Åø')ZRx2_l>Ï%C[ö¢âU?°©Ñ{".f¨
0mmåµ^ÁdxFIßæ¸°Òã	*ò]á©$èlÿ5å IãÙÂâYg.5nÖÉàªßþ©øÊ\cî°"ìá¡Î³ÔÁB&s­ä>gâIÅVîl§þá`Â­n.0yÈ3´P*ó¿÷ïuÒÂ³m|z.×´*'õ16Ü¦y.Cõåa®ìîÛ %tÅ&éá`l"À`|=izéÌÕlL¾N:ïß÷{§Io8¨Óáà¬wNSk}?ê
G½É5ðùd
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/dc/3253460418cea955daf325caae1d760dffe7d8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/dc/3253460418cea955daf325caae1d760dffe7d8 (latin-1)

```text
x+)JMU063d040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^Ã,æ¹{®¯{yáC@GTìÙ/»¶~ÄT_ZXÉðz}ï~Ï³UüïþÝÆõùÆü³¿§£¨.ÊLÏüíIÞÇkÌo_Ön¸¿ÞïÖ!ÃM±¨m¥k%zPbÛk_w{Më{ìa»ÓÄ 2ósJSRü÷¼¨Ôì(þyw·BÇì&[6e¨@'å'¥è¥g2D=ñÚðÏlölu~óå,ÞQW4d!F%3Hîþ¿%g£;^\¨Ïýû¶o¡Æ§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  m
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/dc/24d2f72ebb6dedb2197b3c668c06af1fee8345

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/dc/24d2f72ebb6dedb2197b3c668c06af1fee8345 (latin-1)

```text
xAnB!@»æsÍ ¤izî»fPRaò7¾zï%/yEzoÌf?Öd¾ë\ÉÆl0TÈáOÑsñ4jdÃ¤niòXà¶tveÏÚÕyo¸r1ÈÕjBÒÑù¬Ò¾.2áWö	?©3|Þù,Ôº|{j×cþÚ»
C@p@¨öù·øýR­û+þwÒ[òÂºÒd$õ
NÝ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/58cafd7370dff8029b991233269db7f17067c8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/58cafd7370dff8029b991233269db7f17067c8 (latin-1)

```text
xTënÓ0æwâ0H¡[Ç q´EdíÔnøc¹ÉYkÍ±+ÛÉZOÃã8NÆFÇ¥êË¹~ß9Ç3©gðøéî³;÷ÊeU ¼úËÅÚ.Ð(;ýhC$õ|.Ô|@ëoòòb5*ÇJ®øÍ¦ø×%_nÞÏpÁk¡o±¨¸qÌ^
/ó»a¼õ¹i´e¥®,2ë¸C/¸c±³Ø¢lüße	{³IzãÑQú}:~Ç¼J¼O²ÞË(ºWà¹PÇ§ô³)<Þ»ºöúïÇ'ìd<MOÓñ(6ú²¹=ý¾oX?Ø{Q4ÀQ¥~|ÿñM¯VB
n`É
TµßW%¹ä"r¨µ(À¢*ñWB¹çÌA°;4¿D@¿ëYQVÒÑPwc©°÷´)Ö6¦D ËxoXøogç\ÚÆ9 Dnñw_£P)·bRX

Ñ£¬_ÅÐDâ¢TZJ;:·Tôkx
Ü²?´BLþ,qñ]¬;ïé¿{}Ø#jËÐ}J#T!rV[qÙ ô]eøHÞÓNÙáÙáaXÛ«¿¡ªJ×:¦m¡D[ÒRs©©Á?À*¼$¢o ÈØ)VtÆz{¿Xõ¯òÛ)ÖÝíúÚ­ÍuÝqS£³n5®ûUÎQÕZ÷í)xøJSÔÂÎ°æÊqè0¿ ±y%
ôÁÊÂZ?Í$/ôå@­çurN8@÷sÚFH7ªÜ8¤Þ
dvÓ³Û'¡ºÌFä?Å[»4ÈnAé¤Í%Ø¥¶÷¡X½¾_@±öÿm×öÍýÌ)ºÚúÅ¦Ï´­LX×ýfíÜ8µ²Ðè_Íw×«ímjC.
Q×yÚ²tzI¼1oýÍ¤@Þfzv8NÒæY»ÅîÓEÖ?ë
´
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/ee6138d19c7c74f3d1f68d45b1436c8df66363

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/ee6138d19c7c74f3d1f68d45b1436c8df66363 (latin-1)

```text
xTÝrÓ8æ:OqvzcSO§JaqKHÚdhÊ°0FµFÇ
Òíäavöá§Èqì8¤tt+çOç;ß']¦êÂýÆÁ-Åixöot}"t&ÒñóÚ/®DÌe,îwi9ÚÔ¯fRÝ	Nê9×kiã1Óòjl)¤¶Ì¶o;ïÙ«~ïÂfeþpÚeÝèïÓÖ
úça§æiu@¬R<Úûðp#{<rúµZ½Çy¶üºüOÏ¿ÈTr
3®9lNû|ÊÁ8å5c¹1ÌLÀ,aqãå2³Ì;põÇ|[\?#2r§ÜZÕc VçÂ?Ähìf 1ReÜ¥OØÔ¤BÌ¼½øçG<5®"<W©½¯ØÂHsPÐÚäæSÉL03/¿d¬6p_¦20©ÏRåÓ VèÑ»6ì6q8Hù
"ñ¡J¬2cÁ ì$xHà¼UA8:ï0Ó _@;z×y±öDC?gývÔk½z©©tR ­§¿}§#ðþ*z`Ò0-xrãzð}ÐÂæ:+éBÎ°û¼Êµpa
¬À{2èôYÿb8¸dU9FØ»ÑaSQ\M© úÿrWb¸/·àu8&$D©Æ
ÉÂR0ë<RôLO¢Ò))1ÏpÛ5bÔ%©4÷JÈebÃ*qdX¸¦hæã'ä|]à¶@¸»è&´@M*Fc¯pÿâØ/íðf~¼¶<ÆPª~²a}RZ_¯­ØIóQQ÷Íu7,¬]g]ò¸ËTç®òOFJoHÄÙ8ÄÏ3hâg{{5q-ìéTáD9Ì¥Éy:ðw«+iÿºG¹ññDUmQ~õ$!H	Ûú*ª¶vvºàAè·Ëo´=X_J]ßj'
Çü´C7'RKeY »þ(V¥Ã}rÏ
½¡V
4U³bn5j
_¿ZmÖ;gwGL&(FóQÙÅZ³]ôz¿{ gÔÚm>ý
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/ec702832e118d763d0ab2847966f744d13d3f0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/ec702832e118d763d0ab2847966f744d13d3f0 (latin-1)

```text
x+)JMU06`01 ªÜlgöVß,kÓO^`É}urí éÏ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/81206cecbd9970df07630682216075d08bc951

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cd/81206cecbd9970df07630682216075d08bc951 (latin-1)

```text
x}TmnÚ@íobªAFª"Ñ"Ä¡¨"òñ£V=
f×Ù]#ªRÑDýÑôÜ¤'é¬U ¤ÈÂ²gÞ·3o<Õ_4`XX6S©A¦õÐ{%d§ÂûL&nLQKëÖÓP¬Æc!Ç
ºoÅgÓÎQ3|ú°i$Ê+dÆr,p9ÆÈ¥{½AN¯{îåU0ô7åÖàdÐ?ëvØóÏÌ¥÷ WizìB+«¬Hüùþ¦huVÁÝò,Î ápÊå¯åORAÌ#!ÉÖ<®{BZH¹vÝãªE1ÞZßúQôYµÇlãÑZÅ1ÛùrLWD£ÔZ%·R¡¢!Ø	BÙ"ñpêê*W¢Ìs=!½D+AãX´2ßQ½%ÄP+WvU³eøë/e¤Ñ>Ohµàð]öá`qvÖÜÊÊ(Ë%­GÚaò
1 ª²ñ:kzß¼Ú-ÐÌ£ÙÚlýZaáa6e,TqRj-Æê4,rÊmª	Õå9Ý)>"Å-ø/²°Fj	ÎZÁ
]Aÿµ¯Ûí^P è> Zn*î^d¬Ï"yÓ*%Ô`ßÍ`ONuÎº§í¿7ÄÅ£b-!_Kö×4Øþ÷¨@>úI>?ð5#ß§[ÂXÜö5$\s@9\Ã§îéªÆDi«!Îw©öm¬¬I;³|ÔB5ß§Ìò7ijDY=ûÎkS(¯¹.¹«<ÂÿúL=ÎWÛ-ÿÉú³ØP¢®í°Ñ;èåuûòdØ½¸êú[_5øó!¿D
·
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a2/7a5cb0798800facf0b5238824756d5e3a7a390

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a2/7a5cb0798800facf0b5238824756d5e3a7a390 (latin-1)

```text
xuSÛnÚ@í³¿bDÕÊ(ª­*!0©c!­Ô±'ö
³K×k¨ò5}èäÇ:kcH³õÙ3g\Âååç7o¹²"F¸Úã&Ý©ö
À¬~µ^@L.6Ù3|½jãfëP	ª¸±_¯ØZ9²\Y"Á¸6,Ë^³Éttç»läýÁÜµ)Üá4{×ìçäßýîúÍeµÛ0.ÄÓß§?âtª0áWó|ªÊBdÔÆ\ ¡Ìnm%«-3«ÛÆÝßÐº
l.4pèC·GæªÈ^\Ô!&,×ª4¼Ò@§«M´Y­ø|Ü)³T.ãÜýÇGJf3ñ³ødNCËBk)òSä«sà3¾ABJÄ¡H®éGó¤­R¨Wy ñx·­*¼U²KIÞÞ«¿ÂÂiêÑa:õÕPÎJkdJ6&3MüÖL,Ø|àÝº6nê.¼`l7&F[UÉ Bcüâþ»ØxG¦áH¨Ìîù$Ì<CÜØÝN§ÓìùIF]È1)áBh@:(«,àÑz,Å8Â{.J4Éºaosw0"]½Àµ«ðLxSÝÎÎKQ:ÜùþÉ÷ØwÝ¿y?ÜÛÌf¾7,¼iPçÍ½©CjÊúÂz*À
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d8/9ab5bed615eecb6c97b5f577d6eae6d80530b8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d8/9ab5bed615eecb6c97b5f577d6eae6d80530b8 (latin-1)

```text
xRïOÛ0ÝçüG'¦PíbëÔA@i+ñKÓ¾Xn|M"\%NÔtâ/qi`lHËØw÷üîý2[ÀãSÉR |ÛàcRçG2ãTÅ´úÉ©Ó©¯°B¥Ù+cþ¢ÜÛ¬Ø*+dæYp£ðÞ+ç"«ÐÂ%.5Q9áüMççwaÀÎ³p|¸´góÙÅäý^1Á}zCÇIêZ<ÊT³fsÉr0­Ð2Uh(
îi8\ó>éM$QyÎ/Ì.Á5!ìb¶tQKþÆH×££9ê2WpLf÷ãÐh¢dÛößp`DV0+ò=´Gâ-ÿ;X$Úv2Rãµ©Ûá©X÷¥û¢ÞåëN¾òLJ¶;µMüÙ1XLgQjmà¹[§a#+?A.gì'zÑÖfq½²qÂì]'7y&&LfnoJv¹J9|¸!³|±í5ý·Ú;û¦jëýÁç½ÝøÔÄ(7·Ù,u³lYºA°<[y¯üoÿ/uß`è<9¿ªj<w
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b7/a6f320ba3944d0f25ad7fcf362f92c98944967

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b7/a6f320ba3944d0f25ad7fcf362f92c98944967 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÔ2=Äï7Owÿµb5»aÞñÇSi~YjQNb%C××cµS8>Ù¢{¯ÁáÐ2¿÷sS6 ¨.ÊLÏü½*ã¿GçûÞ	³JW,i±]}'µ0£ÿ°_0rÈN[Åóÿò¥¢MÉO& Bf^rNiJ*Ãûµç÷´ÌyóocÛÉãa»NùÊzBT%3hêÈn"^ßñüõÙ-èB­+O-.Ñ«ÌÍaè8vÐ¤yõÌüjÏÊ®ýúÏ åv¶
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/04/1060a7291de3611711195efb9bd721e7ab692a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/04/1060a7291de3611711195efb9bd721e7ab692a (latin-1)

```text
xUMo@íÙ¿b_RÉU¿R©0¬Ð²DJ.+lV	*×¥ôßD=åÐSo½òÇ:Æì&­â;_oÞ¼ÖY±_/>¼Ãª¨K*×Ù¾7wòvu%ßõë-¦úëÊBOcÐ\/]Grø\Hq0Ù;¡WïcÈùüË'¬çÅæ	b8¨}Ùü,`SlÁYYo!ã®µÔPD8ó(Òáî5ó^8 ¢Ð_²i>
É¨0XºÂì£}Ý¥Í<ÁÛz}£' Ç_-OE®ØÍÌ·xÏÌ-'G¡º~b:
gÒa×®Íd(,ûjÀNÛ±¥e¯ÌÇ£{À}'²Åôk::ith]ÏÈ³{Kóìñ,}¸1]
Áç¡|@s+Z
¹d×l9ý<D½4^ á¦àzsßt\ù£T8[æèµ)Ëg#iZ¿ÿU¥
Ø6¿:ëÄ7¿*{V¹)g6C%qj¯ëE6'6PÞ:.&)¾W¹áKdío´[%¢R{¨Ë8O
 ÒÈIû»½Ú¤e5
Íè¨¯è%ß¯ÃQëú2ÔE[Vz5[ÀÁý£¼£ÕÞyYàá8
ÇìhZz1O*0uH«¾×
*Wti¼ük2ñálú@!Q;'
á¤ É·jwÿ°³ÚBÝÕy	¸,J¦ê
`têªØ6Uº)H;¤ãêÐìG¸×i0BÃf1¼2d
ëzgl$'\ OÈåYLÞíNIgFúÝ$ÏÞ7lÜïYoêÝ]/ÀA´ë%.9³HÄC\kÕ1vî-Î±ß¥²^iY©m\Cïê
îTÞ<í¯×FÙgvH($>Ù·ðcûmÒ&zWi@E-ö×úÄÞé±ëÞôî`÷1h;÷w´ÈãlÛ¸æOfV¼öAu¨yë-½£¿Ud$ó
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/36/a623dd1d0add778129c14e0b75866efe79a254

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/36/a623dd1d0add778129c14e0b75866efe79a254 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgx,ÑúÿãcÅóOyNÆ,ÈPÞQPZQYÄ°v×§­¶LÔ½RÝÐõ¬ð²' OÚU$
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d9/a77a4662976a002213db4af0a93537a1e8e112

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d9/a77a4662976a002213db4af0a93537a1e8e112 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg(QÛ=9°\åcü2£ôSMlêÎêj±U©Ekw}Ú:aËDÝ+Ù
]Ï
ï(kyp VÙRW
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8e/1103f8fd65d2dba28b00cc903686d1576a3129

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8e/1103f8fd65d2dba28b00cc903686d1576a3129 (latin-1)

```text
x+)JMU042c040031QpöMÌNõÉ,.)Ö+©(aØa¯whÿ7çöÍu³^åîÇ{úãYg¨ÊÒÄ¢ø¢ÔäÔÌ²Ô"½dí­ÿ{ÖÜÞtSÄ§XöÈ\÷U·g$g ~1,JmÛÞ¤Ô{göÆí)×>Í P7T
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8e/c31f0d44e3e88972db934207175a5e1ed2017d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8e/c31f0d44e3e88972db934207175a5e1ed2017d (latin-1)

```text
x+)JMU06`01 ªÜl»ëXÒØkißZðøÍgÁVqãF ñs
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/35/7b48a324baca134a8036e6585aaae74df11697

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/35/7b48a324baca134a8036e6585aaae74df11697 (latin-1)

```text
x+)JMU047d01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õN¤üÄ¢bÐÛäÓÜxËV[ÝÉm5»(yÔÐÀÀÌÄD!©43'E¯217Ãsõ¢øÛÏ%c\.áp8z¥bLr~^Zf:C÷¥F"î<¨ü±qÖ¾ïU©Ekw}Ú:aËDÝ+Ù
]Ï
ï(kyp ¸ET
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/29/ba795a5830dc0db2042e739073b5ba90f01208

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/29/ba795a5830dc0db2042e739073b5ba90f01208 (latin-1)

```text
xS±Nã@¥ÎWHÒrÒQ¸pvÇaÛk­× Y9à)Ø(¾Dâ{®ºâ*>!?ÆIâõE³oæ½yó¼\5K¸½¹=CÒlÚ
ªº\®ªÐi¤fî!»L«Ôªt¼ùÕD9RiôNIg0ÓÆ:{¡;ëjý¼þ5¹"4a÷JØVëv÷§Çæd^ö#s4*}ns$)2ë¤QLO ¤(×1õhäKÎ³XÙá]É;©5Û±éÈ¿_ñ[v¶k÷S¾8~î,ÙÄýÑÝG£|ê$.@ÛPÌ{ñü"¤p¡HÅ=<3ZÂçÄ	zk½É*UlV|ÎXó½Çå*ÏQ )Â"¶.ÆÆÁMßuú8ÃPi¤ÀDKäQtZ>7OÒòJÇðöý2
áïçm	
¼ìÞ6«ÏlÕ»ÛjõswR)H×ûÜ2±½D¾ÅÛ¶/S~âãkè¾1ð¿Õ¬j
¶¬`îPsö_×Õãs[yÔ5¤DD} Ám
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/29/2c1ecc5b821294177f88e7ebb01db4e3e02d71

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/29/2c1ecc5b821294177f88e7ebb01db4e3e02d71 (latin-1)

```text
x+)JMU027g040031QpöMÌNõÉ,.)Ö+©(aX8;àÓÃuWÌÏnþÉ²qÛ5¾½òP¥E%ñ¹ùe©@¢´8U/ájv¸ø^ûÉWÖè	o¼#øYqQjrjfYjQ|NjZ	PýÎÜùªªW}
´ö»Û&pà^åU}QfzHF¢1ÛÄ,gE×/S,}uõÑd
Åå%É0ãÅX}3W~kÔXòüÏÆ)Ó±¨^®ñ¹ç@è²+¬^¿«ºsîeË­ µ@ré
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/29/a0c820e9e27c4314a7e43e3543ae63e16b1bdb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/29/a0c820e9e27c4314a7e43e3543ae63e16b1bdb (latin-1)

```text
x+)JMU06`01 ªÜl¯Â·}]ÝUøÚÖéøÿ	¡YR 'Ã
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/01/04c8076aa41875d444444eb26c89fce842236c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/01/04c8076aa41875d444444eb26c89fce842236c (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2ÓvÏSõùé£ûK·WE¸^à1ØQPZQYÄ°v×§­¶LÔ½RÝÐõ¬ð²' tTi
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/01/0210dcb6bb71b1262df59eef3da9bf0cf466f8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/01/0210dcb6bb71b1262df59eef3da9bf0cf466f8 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgðhê~¼¢Çn¢Ç¼K½Ùæ1L(¨J-È¨,bX»ëÓÖ	[&ê^©ÌnèzVxGYË .ñT¡
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/01/a195d00974e2ad2ddccf89ed39b773c73f7e4a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/01/a195d00974e2ad2ddccf89ed39b773c73f7e4a (latin-1)

```text
xuËjÃ0E»ÖWdÓnêE(*BªUºÈFÈÒÔÖÃH£R§ôß['Þ8!³»sîGeCóùÃÍ¬ªv
×ÈØlïµÍaqÀ®écA}é¾Y^£G{\[àzNyUc0K³&8¸VºÊDPêFù
ü0ø¯¢
*¬7e)¶'.1ø	&ÀÑãczïéQo>ýD&µrê£3ªL|âì3¶{{âC¼oå³X¿®Jq{å;Îþ RrA
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cf/8a35c1bd2734798d65c91a12bec8d516fff648

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cf/8a35c1bd2734798d65c91a12bec8d516fff648 (latin-1)

```text
x+)JMU01g040031QÈÍ/-N/.ÈÉ,O-KÍ+ÑË`øô1EÇçÁY/E¯UmåÅgM 
t}
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/62/c8415b26b3df4064ae6c676014fb8f1f1d349b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/62/c8415b26b3df4064ae6c676014fb8f1f1d349b (latin-1)

```text
x­MnÂ0F»Î)FE²vÁP
UDøQ]tcx V8µÚ8RW=«CB7@ª®ý}7Ïñ2Kx¸ïõîZàeQRp`\¢>|K.0)C©¬-æñ§$¼1$e*ÒBrTv{÷2w:zOûî)á\n¸ãþh@ÜE&!O; ^°ïv:õ'¬E¦")Ø
Ó\"G¾uL@S¹FM(dd`hÃ,ðûáÀ´w¿GùÞ<¬mÓWB!Qj$QL³5²Ndzeñ]­DÊíæ3ßI0õ
´!ú¾c´ÀÅLKP& Õ[òìÁºÀUP©±|$¸Òézç:R±Á³)­h.ùA®4f(Od×;â5J×»8&
íÊù%Ïc¬µ?#×ÿi]òuÜL{Æ÷óÖuúâfæßpYÇt
e´gÌ<Çú_¦ZË
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/62/726b4dfc7ceb2fb2d8a4575908f6bb726625b7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/62/726b4dfc7ceb2fb2d8a4575908f6bb726625b7 (latin-1)

```text
xI
1 =çý¥;Ët"¾À»'É$0f|¾ó/u((¨Ôj]hC»ÑE@l,eâÄ¢53&òBÒìGv)Böj]^0`KF-%x¶3Ñìýdsb¢P4è7¨øÖáÚ>.±
ßroy©í|¯qyR«' vÖMNÃ
¢Úìö7äÿRÉ{5z´Ké74P/¤öDõÏ>G
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/62/6c6faef80e77216833954350b8a30bc188fdde

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/62/6c6faef80e77216833954350b8a30bc188fdde (latin-1)

```text
x+)JMU026b040031QpöMÌNõÉ,.)Ö+©(aXÇ¢ò2Dx*^÷OÙ¹þ1ÌUYXT_YZV¢Ì?ßàFØ¥eMBÓ;Ä¦½Àª¾(3=¤!o« Ó½ÀÍ·ëqíîqÀ±ã ²âòÌäñG§iÌ¸½ý¾ÉË
iµªXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV ²¿^`
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fc/07d0325a406b1b66aa0cffd3f8a5158263e490

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fc/07d0325a406b1b66aa0cffd3f8a5158263e490 (latin-1)

```text
x½UÝNÛ0Þõâ¨T
MôÚ U£bí¶»ÈMX8qf;üñH{½Ø´¸iHÖ>>þüù;?s1 èwß4'ZrxxøDj?Né)¹Þ]Ö.ÆíR²è:c,å
ÞÁþ§óñäóÑxkvx>§ßÚà·¡¿}Ð¶GW÷[s?¯ÜÛ{K÷ÇjIÅ)-íÄáó	ûpqëâJædÎéKôÍ
Vã«ÒDF´¸&÷jORJIsí©ÒÔÚíöß¯©æùf¥[lÍ£ëxXÖÖsQ{vïFÖy¦$§©ªæ¢È
¢^Ñð¾,ðGMÞxd÷1ZvbßÙiÖ¿Í¦ù0ãÉéY|ø~zúå(>9=>9ØNZ& /+ Å
©`
8Áá2+'sÊ
¢ÆGkYC8#
ïû°@zFÄfE×Ê²BHMrM¡ Ø%M(»¡r'2OÈ´ ì´ ¹æ8üÈ®Û²Ì½9½"7LHsRA%+®¨$<^í±¢#îÚ«óRKao^ñ~ÜV§ªTé0e¦ªe(ÈHA1´¹6ÒÙ­2IâZ%$÷wÁþ;Wãjè[ÏF8#Z²;GÝz7ÑÈÀÄ <â#Å©ßK
CLdNØr¥'böãÕÁÍ8¢=íöp7]l¹	3>û
?«ÌÆãx6ùk©.n "D½#8*¢6Ï7'±1BocþÆ¯@X}l]ÄX®¹º2«KÉ[^QTU==mq*ËÓ~ä¼e[sÍn}±).êDR~ÿÊ±/`¯¢h°ôÆÆ`sÓA}¥VVCÂ.!½ÕÕ> ò!ê®¬FD!D`¶G}pxÔÃöiÖ±ñyWZtN|9ÓÞSOE
«îø/EQ'
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fc/7f4df9c8c307d36f9823b31b3f640aec3a2c22

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fc/7f4df9c8c307d36f9823b31b3f640aec3a2c22 (latin-1)

```text
xÎÁÂ0FaÎ®bXäØ#!´ìã$þ
1FÙÕ¸>éIßTK±ãC[BÓQ$Ä!jö¾C|X$áÎ1O]ñhÔ;UçsÔÁñ(°Î§­ºü®gF_íVWºÔ×JZ@§
×æR¯Eçå8Õr¦.ôÄzfú±ÎZ³×Ý×ðýiFÝ@ïr'üïÒ².Ëªù æJ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fc/e620b403b4fac0b0ce6c8d9eb05f4ac7a1b9d6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fc/e620b403b4fac0b0ce6c8d9eb05f4ac7a1b9d6 (latin-1)

```text
x¿NÃ0Æó§f­B©CÇ¾TVþ8rHt±Rè&RH}&&!/Æ¥44!Æ»ûüû>ß­ëv
ÛùYµ« ÑáâúÆÃeÁ´Aèß n³{ê_[¸o· vå¸ÀUÊ¥ÍQKûûSgxfejPë"3VhYbúK@Ïs£ß8®ã8ç°cý/jD6Â»@1-¬ÆLi3uÆ*rgÍ·Õ=Ø<°KÉÑæñ`cpÁ-ãÉÏæQi%
nüy	3g²Y¦ÒÐÎä
4òcµ&§¬±ÄØ÷ \ðÀêÄ8¨iã(Î)}SaOÿy$öüØUÐÂ¶ÿxx©¿NÞôïÝ¦>s>lP#Gº¯¶CCP:}H>Øp¬Å
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/27/e576c4401ccfb7243d4de0a192ccc6c569468d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/27/e576c4401ccfb7243d4de0a192ccc6c569468d (latin-1)

```text
x+)JMU067f040031QpöMÌNõÉ,.)Ö+©(aàHÚºÚY(Û0©ÓA­õ3ó¼v¨ÊÔâøÜüÒâT½dÍeev4+ùõ)aïWj_4·@Õ&Ô¥BÇç¤¦ uÔ|dk3¹µêTß\µ¿3]Uß³Æ¢Ìôõ7&NÊ5êfåKù¼ÃSfG²¢ÔäÔÌ²Ô"bÿNlðYÕºòõÏýíVþü³	«zùËÓWÌörEB§h¢¼öÊ?¯5g$gÀgõÍ\\ù­}BPcÉó?3g¤DNÇ¢fx¹Æç¡Ëv®°zý®êÎ¹.+¶ Ég
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/27/d174bf70477442117d461326d7e19231db9268

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/27/d174bf70477442117d461326d7e19231db9268 (latin-1)

```text
xKnÄ D³æ}Dí64 EQN}|$c,ß?\!»Rô*õÖêÒþmðÑíb[Ê¤ yOØéMr!Ç¼ºÂs%:dD*²ÚXãÑq­L&Zîùì~û=à'4Ï<z®­?Z¨ÇGêí6k4ãB4¼ã¨V»ü¦üT¯ëXÏÎå>Sígx¤e=Âz=eEõ?ÃO£
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ee/84e094a1cc0802c1c9df9bee641b902209959c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ee/84e094a1cc0802c1c9df9bee641b902209959c (latin-1)

```text
xuTMo@íÙ¿b.©JuV¹øam£Ø,] RrYáx bpÁ¶äþrè©·^ýÇ:ÛávfÞ¼yó1O²9ôï®ûeBJ£y¢zwGÎX>Íî¥Ç7pÜñ`§¿Îxè3|2@s8¶Ìã"Á£Çdí^^GÑë»ÛÏp"`°¶*/ö¿3xÎ`ÏÌ-¤ÏcNõ$&"ôiç¹èÐÆcß:Anù$2i17	ÃÖAzÞ0ôõýsÎ%\ëÕftÅHúÕr~Pcì	6uÑ0iKþéÕr72~OÝÿ>{\ä={rSÔ]Â¬þý:t4Æ2eÙÌÒ6{p,ÕÖ½G6Ë¶¤iÍ!àvh¬ÐÐõBÏÙ¢;®à$8O¤S-ËÓH6ºI|w¦åÈ§²6Ü´Q§Æ[ na ;â]Ç·Aáô1[ÏM(C¹¶$©Ð¦7ãÌÀ`®ãm,÷¤ÿtÿg«£Ì¥öYg]PyU¸#R£# -`½tµã]#
½nì¢êÕÒ;4Ëò ±KKÛ¾Îº£8Ø5xøc Þ¤¸P9`
GÄ°n g¦k;ÒØCºÄ·\1s´*Sãí¸^Ôê`"InÃJ«.Få^©ë¾ykµ`¡ NW5¼¨tÿÇÏ,2xR«×]Þ3j54&k0VI¼S²Èc¼ðkùãªúT©¥
ß=zÕuiK çu¶K¾z³4J®`°ÿ·XÑÍ^¨ùæE;Ê8zýFÃÏµë4µNnÀ$ÇH9ÊA¥Piåªè²óëW+ïA´ÒWT ïqR©¶*]géZs!«áø²ÏþWj¤ß6åÓ>	»¹îýrEb
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/94/7fdcdea9f7b219d8812809e602605f706c7363

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/94/7fdcdea9f7b219d8812809e602605f706c7363 (latin-1)

```text
xTÍNÛ@îÙO1¢ªd·QLZ!R*¥`PDBP UÛµ±dµ×ò®MâØ·è¥ê¡ÂôI:»¶C¨¢9lÖóóí|3ûíDÈ	tÞ¾Û}ñ§(b÷×Í¹ÏÓ¬ÐÕÚ}pøç§(6ºNy:õé£?ÆGh\ë°ÉÜ/X®ÃDHK¡0Ìùt¦A4aêëhvò
KL	¥lùSëV~uÊ×¡5Q$ ø>üùñR©¤µ`ÒqÈ³Ö	ªE`Æ8)ÓUb/æ)*PwÖq£ãp8:ü4ÂÃà`Ðîu2oÁÁèô¨~&d|^ã%'aïbÜÿçÐÙYMüIðuØ;ÏFçýþèÔÍåU")<pÍÞ×²ßk%rT¤w¿ï~I`ÅÎrÈXÎ ÓÒìÆH0P<)¸(ÈÌcÂsfGPJÂ4ç¸têÝP-¥ù°%Ý8Ô[°C®§WAëzÒ«ê[ ó½n5³²©ó0Q1sw¶©?Ï»dBY4Þ2àn*¯Ê{|ÝS¼hÙLsôÓ_´|Fr)Dø¡ÿ<ºéó¤ÐZ¦ÊÇjîÓáÇcwk£´ö ^ì¿!^µ.ÉZò½Æ¤íÖCbÔ
Jm­W;²5Ð5¶Pëiö5j¨PZ&üÅÒÆ(z¤4QëM¤@Ø'VM×Ûñ¾×çÑÆ²ÖÑvÃìÍöAã5Y
Ý5oMõ®òÝ!Sñ	P`Å&C!!0Ï«g\ùÝOºÌ,UÌ5cyyÇô~z{ýóÀÅÒ(¿>aT+mÞzRHªH$¬)ôÍ\ÛÜJ¢%Whc©àé<ÌÖôp»ìl7"ZI¬¯ëû¬ª G]ä)lw[ç/á]ë×
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/94/26e40bfb52d36af6fef81e35100d957ed6da58

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/94/26e40bfb52d36af6fef81e35100d957ed6da58 (latin-1)

```text
x+)JMU0´4a040031Q(M,*ÏÍ/K¥Å©ñ9©i%zÉ_?øX>ºÞleónvíi9á|8te¦g´4¾ã{ô"ã±©raE~ðñ¨OÍµg$gÀ,ÇÙåíö¬eÎzëÛËN°ÆT5jáU>fÌùvótÔÎ{_y%ÞP< N§S
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/94/b12c701b56c8711a7368928f7bcd3d755f625d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/94/b12c701b56c8711a7368928f7bcd3d755f625d (latin-1)

```text
x+)JMU0´4`040031QHÎ/ÊKÕKÎÏKcX¬¦À¦ºrkªú¯LËy±ÓeÝPTe§Væ&0Hæ÷½º³ß«ÕDeNWÙZþbyÕÅç¤¦èå¥å$V2Ytíaözû²ZÙoô=ÏØ¼ÙÄ ¿âû¾6?xýKÆ¯MZtnÚo¨Yå©Å%z¹9Ç4¯y#_íYÙÁµ_?ó1  ](OÍ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/eb/266f079679fe474991fc03f46a2dd1a78ffac3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/eb/266f079679fe474991fc03f46a2dd1a78ffac3 (latin-1)

```text
xKjÄ0@»ö)tdÅòJt?KEVÒ@<.©sÿÉº}ðà=í­mòÇ8Ì`öÉrXêJ $¯c¢Pa²LDØýÊa¯¼aµÅ%#VåZULCÂ:%d¥¦àä?ýg?øfðùgk¯[ëµÉ¶ßµ·/ð)úB§ 7ÝE¯¾aÿ7ÝnõVm>WØ^×âÐÝ/GÐ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/eb/af8dbf49cd7a0feefed9960af3d89ff89bf767

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/eb/af8dbf49cd7a0feefed9960af3d89ff89bf767 (latin-1)

```text
x½VíNÛ0Ýï<ÅU&U54	mi)CB¤jT¬Ýö/rV8³>Æx¤=Å^l×iÚ9iHim{||®ïmç\Ì!»ÃW¯Yó"¡à.èý\ì$Z1×q: ÝÀÒ4£Òiiªt´Âø(Mt¡à-¸bAîÝó8rVÄZò
S©ý(¡¤àzjÃ
b¨®¤(òÀ0¹¢ÜÐ|¼øM>ßÌ.¦Ñôkü6ô·Û¥µ
øÅ>Ø:­á(ÔD½æs©JqJóÄr`éùÏ*.n½\ÜRéÑÌ9}N~éx)¿Òú$').¤¤öTNib
^èû!UÂ<ß¬´jÚ@¢4hc=#)-ïCo·
nsw£Sä4Q·±Hs¼qxDäw¯r&<À #Þ<é}3û¯È·"ÍÁ·¤e¾ù0ÉÙytônzöù8:=;9µo8Snv)*a|üÞÚhãbÎÂ#=¬ ãSk©¨~°p3Q`J	È4U¢3`M|Qõ­ 2%ïBÅ$ó÷¡ü´öªûò=]´KW:-Ù%=a"¡^Â$5J0¥¸EÐZ?jJÇ7vb)Ç¢XÑ£:ß(aêyÕÆJjlÿÃ!¼±30>ÿ?9ÌÆãh6ùkáV )C·÷oËV4ë»ÍE4fè5fè7fØkÌ0xC½ËB´$º2­jË[O¼ Êö'Ä*5SX_]«³à
(Ò¬îã´]pc»âAÄENà×Ï[¶g'Ü]£±UâõØ  x¡º ½Ú"¦ýEò!j«AÁ.]zô!Ø«¯ BèCà°dTçÂnh~`:ÛÐ±}IÂ£9½&7LÈÊÀ§-jÀÎ´WÅ¡y#Øî,ÉVÁ×BÑ¬'Ì[qF»¹ñ:ÏóG¼
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/de/89e61568c5014027a46c7a12832de155373420

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/de/89e61568c5014027a46c7a12832de155373420 (latin-1)

```text
xTË@ÌÙ_ÑZ.´RëHÙÆ24Ö6£]KösV9í!§|?nlÌ'Z|éîª®*fæø|wÿÎe^
ToR5²|oæÌåz¹ïxÂñægýtéG!Ã#´Òï-9|.¤xì°*2>ûúåÛø¼L.4¯ÃQeó3m¾{i~èG;¦«PD:ó(ÒæÎyWÈ(ô]6ÉF#r¸nÑIÅÒbà-Ú¥é^ñMtkÁ¦¾É;!trtÝJrê£;Þ¡£p*m¶r,&CaZ<ÝX¶%Mk9<<Ü·#KLn°°ðfÔK«Mv<G ÌÎììø¸>ù=0Zðx> Ã¹BºlÅÜÉ]ßu}90`p¼?,\ú6£Qh-³ul2ÅågKr@Û÷¿i0«Ý1öÍï¤NOÙÊ_GþÜZÊÅ0HÖ;m0Ý:/rß|PKbQ}íÏ ú´Jd¥
¨Ë8Kr è[È(úBmweØØ52ÀÌè¬¯ÎèZï·Í°Õ¦~T¡4=h«JÆó
hÜ?v@Âú²·yVæøn\DíGBvC´,]ùI ¨ã®áG­ RYEÑq­RýäA8<Â$ê ²DAÒ¿((òZèÕ-¨=Äéc°Ë¼Äxà¨ ®AoQ]åûæ¥Úms$ÒtþtÈ»æâÍ.EI®EÃfÓh`>2dó9ëEúéêì[ 
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/de/44136b9a041dc07e1dcc3d3c1812ad3e1f7429

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/de/44136b9a041dc07e1dcc3d3c1812ad3e1f7429 (latin-1)

```text
x+)JMU06`01 ªÜlËØ7	_TXSÆÏÅgºðWd8 ë+

```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/6a853c4203f66d4e8738c452890ba77c15ff5f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/6a853c4203f66d4e8738c452890ba77c15ff5f (latin-1)

```text
x+)JMU043`040031QHÎ/ÊKÕKÎÏKcX¬¦À¦ºrkªú¯LËy±ÓeÝPTe§Væ&0Hæ÷½º³ß«ÕDeNWÙZþbyÕÅç¤¦èå¥å$V2Ìqã$§nßºÅ1æÿS°4¾/ö>ªº<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 ¢À@W
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/112b77bf2f00adb628c7d326f961f8616fe4f7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/112b77bf2f00adb628c7d326f961f8616fe4f7 (latin-1)

```text
x­Ïn£0Æ{æ),Ñ\Rõ°ê9¢é
5m"ö°Á°d0µM¶ÔGê©Ð[ª»ÔH{f>Ï7ßü
rþãââÄ'qñÊ$êwÉ"I)E©¼g¬'	¬-¢mU¦d¨Ó_7×-n¯â¯gûpXÝL¯gÝ%Éìv
«Å]Íà2N^Ï&ãO|r%*$eS@aYK$]7NehdfÌ¤uMI|?]Ï<BN_>7Ç«µmSF!¨3
¸ÃJO²Áz(nÜÔÇ¶ÚÙWËy¼d17#yé<4ù$2ïÊ§TT
J*Úo®|7©Ô`²G¶C	·Öø·õé¬!(ÅÁ¦ÔëâDjÃ´ùØåÙðÝ8S+J<9wû
G»aÜAtð#|íaÒ©Æ1²nÇpÿÚÂzÈ·%JVxD®=S¦ÿ'qåÅ8äF(zÌõUCmYE
Õt¿ÙÃÖcÇµ/ì¸ú .àé³Ès§°èÇ1í5íñ(¬ÌïÜáº¸K0UÔüôBïðÂþ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/663c186fa5ed4c03ecf6cb55d48433d0100413

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/663c186fa5ed4c03ecf6cb55d48433d0100413 (latin-1)

```text
x¥SÝNÛ0ÞµâHÜ¤,¢?»`cRU¤¤
eÝXnrh­:qe;¸Ýì
¦]ìAx=ÉNÒiP&Ø|a;9ß÷ãÒ#h¿kí¾Ùy¢áÃ-Î&sÓù¬p}gò=±OÑä¨6e>nÒ¹Ñb)|dÊ¦ÍBÇ3]"mEnäxâq³×Ò%ß.,y?:<~Ý8ðn³©ÑéQïîðÊ%>ac±DçÖu¦H,Á6dÚJñJæýî0î]ð(<vgý»Ju\ö»>ÎzÃ^tê}íC¢U¼êÞí?¢ßW5pTä?¾kÅTR	# ó²º Ì:ád¥)XÌS>Å¹WÈÜ½çê«ºðZµKq¬Ì
%ÜRÈ5F46öÈÐZ[NyfâÌë´H '»ÊÖÙ(Y
Å
éîkê1&8BHEª-wã!à7PÛe¹Ó`0ËRï0¢ºàóx&¼¥é_ª°>]+§ùlb´Rü®-½jÌ¨pæ¬wÖX+RYn°õ[ãg ñ÷h}èÎ<B~áQZiNøQÓÇË.É+ðê<ûÐª*­XÏLÛ6µú#àç¯e-tùðMÉT×þ÷ÔÅMÁ:àg_Aå¨ÌøoL`ì³`þ	[÷¥09´öØ=û­Z
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/0bc10cda0e7b61b1c13b6e9979eaac666ccce4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/0bc10cda0e7b61b1c13b6e9979eaac666ccce4 (latin-1)

```text
x+)JMU06`01 ªÜl(k§©¯·¬[j/.ÆÆf,  ãö
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/d892e193522b0dfd7828f40b83772e8e39ad8b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0b/d892e193522b0dfd7828f40b83772e8e39ad8b (latin-1)

```text
x+)JMU027g040031QpöMÌNõÉ,.)Ö+©(aX8;àÓÃuWÌÏnþÉ²qÛ5¾½òP¥E%ñ¹ùe©@¢´8U/ájv¸ø^ûÉWÖè	o¼#øYqQjrjfYjQ|NjZ	P½ÎOñ¼ù©7#l*ÉªEw,?^fU}QfzHCàÚs$ÿê1üç([8¥`anS²âòÌäñb¬¾+¿µOj,yþgFãÈéXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV ¤tX
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d4/7170a21dee5a67fa8eb703c3d76a9786d371d1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d4/7170a21dee5a67fa8eb703c3d76a9786d371d1 (latin-1)

```text
xR»NÃ@¤ÎW¬:@A@áÂ¾[Slßi}4§R å!Ä÷PQPñ	ù1öÇDòvggfçv2[Nàö¾{Ö3^aAéÍõ]÷Î«,ÂæÆ°®^6Kx\ÎAæñE«B©ê¹IÅYô*~Ì©Â"Qe¬¤X x¼ÔFVkÇ4Êû®4²=.9b¬XXb±Åi?	mgØy@FÑUðuàßTÐ+(u¥Õ0ÑÚ:;4èz°Gè}5Y2LzòªLëÙíòo,¢ÃDÇ$Yßhò };×Ué½Õ½\M½ôÛqJ ï~0ë;B
üwq7¤e%lÔfM` 0°Ý
VÌªPÿ_|ût2Ýk:ç'Iã*³.ÃfQ ]@©¼kÍ×ò%á5°Î/ÜpþçÁÅ¯Ïë1,a¾ù~zmÏw±ùZOgGÊuùVÉyµQ>ãu~ ³é
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d4/9e5b073a39615a8d6d98af46f5cbacd3cd99f3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d4/9e5b073a39615a8d6d98af46f5cbacd3cd99f3 (latin-1)

```text
xKÊÉOR04±`PÎÌKÎ)MIU°©J-È¨,ÒÏN-ÊKÍÑË°ãBÊÍÖO-KÍ+ÏMÌKLO-BVªIëñ¹ù¥Å©ñÅ%%©ñÉyé©)zJ\\Q¾Þñ®a®~!ñ¾>8jZs òN7h
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d4/f03d3aa8f691d2985929b23cc13bb5180e5bce

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d4/f03d3aa8f691d2985929b23cc13bb5180e5bce (latin-1)

```text
xÅTÍnÓ@æì§R!94jJ% 7²pãÈq*ËjoÒU¯Y¯úwä-¸ }¼	OÂ¤	*"ÙëýæïÙQ¬FÐ|ùzÿÉLÆq	8º]Ôc±HòéÞù;kcK¤çº¹·´Õ§©TÄj:É´OÚ·<¿ËNüÎÐsXàtÝAèö:{
Ú~ïØí²O'EzÎ©ãU-«^ÏéLÐü÷{Í}Pyñr`íDb"AQ¬ï! tBÖó;×úàx6lT·ÃÜFAó  áyÐR®9}Ê|Îe&4¦0Z®ee9±J2ÑùØ@)<O6Ht®dëL¤±é[®-ÊFað:Î©ÛvRì:¡½"MRý´f2cZðèÒ¦ÕE@NØnßõKàD(¢+E1ôÓÂä:)×·eR¥2aXÊDNs-
øZ)Û«a2ö!kµC÷ÔY"®fÂü~¨Q=$)Çj&w¥Éb9å*_·wlWÈI´ïY~J#y,¯DTY'ÇDHs-ä(ÉK¹!ëí[à3#OL
h¹ÿ×ù%e+
	±onà´$nÅ1r(]÷wêN0ÖFb ÑéÆ!>J¾øº»»bHÖ<&fsÃÂ¬,"µ×eÞÛû²n?aÜn©M®±½¹+®ÿSÍÇê+HÂ{hÂ Z±o°ÿ~~û
n"ÇEgñÅÝâ5[|Çñåt{`f5ÎäÔöÄ²/§©Ðö'y&¢ªu]HÛ
ºlØ½Ü(%ßF´F³MATg7¼¿ ûb½­~ßsÛ­Ðõq"WãÆ·â0ë®¸áfø¬:ÏÖ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/61/ad551ce9f66c7047832defd69ea6f7ff1a0a9b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/61/ad551ce9f66c7047832defd69ea6f7ff1a0a9b (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2Óbõ*öÔÚ7çñy'tÃ¢tÕ³!
ªR2*Öîú´uÂºW*³ºÞQÖòà RÌ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/61/5d2126692ed45f6085fc707e205c6357999aa6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/61/5d2126692ed45f6085fc707e205c6357999aa6 (latin-1)

```text
x+)JMU012a040031QpöMÌNõÉ,.)Ö+©(axôÑÐiUVõÒ?s¦uÎuä¸ïµª27¿´85¾¸ '³$>µ,5¯D/A$øo{Úó÷W*'ÌL»Ý3wO£T9D!DSQPm¦ÈÉ±þjWÿÜÓ>}"tÕi¨ÚÒÄ¢øÜü²T ²$'5
dzÍG¶6[«NõÍUû;#ðÐUõ=küqè(ÊLÏ iù¹'kOûçîlûmÎ3þ16MÐX¼YKQjrjfYjÌ
±'6ø¬j]ùzçþÉv+~ÏÙU=Ìüåé+fN{¹"¡ÓK4Q^K{åWÈË3K3àÆ³úf.®üÖ>!¨±äù3R"§cQ
3¼\ãsÏÐe;WX½~WuçÜË [¾6µÓ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/70/13bbb97260c8e9e50e3c3fe8f7a1218a919d4f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/70/13bbb97260c8e9e50e3c3fe8f7a1218a919d4f (latin-1)

```text
xTÍnÓ@æì§ÚÜüC¥Rd&Q¢ËjcOj+ëÝ`ïº´¨W7@ú yY;)m ËÏ~óÍ7ßÌz.ÔÚÏ
!¼ºÅU|5Iø³s.X Ô,å_aöøx7)_=Ï1æE¢fÜ¦K*#Ë5×ÈÂË+ñÁU
Ï4Ë¯ÆLàBÛÎaD"ugSÿõÇÃqËP¨$eÄHk©OL]{PJÁèÙ­'©V-åô@gNK8éÎâÊí´6ÿ!Xp?Íp·M:!$3.6Þ$×(1sC%s
Ö´j
^`\7Pæ¤1¬0OKø^ÏÙç]â«Ü×òZf|%!_ß¯(ød¬He@*¨Ö$pcQë²ænÉ:t*²øùõ}(F¨2×3Ô&ðñì=| w0±Þy¯7TÊÈªmÚçp³XITÑþèl©¡Ì£ÁÔ}Ú{oÏLÈ-÷þÔÌüñh/ÃÏÂ!wá­ÊÖ÷LZCR#Mß<WJ[T½ßvQì¡½;6+×.|íú?ö Ì+w¡Ú~kh#úL»Ñö¶hD7èìò0SB0k=[ônxn´¦ý½£Nm%êvª;¥?á"¥ÂSßÎ~Úõ»QlÍ²¶N_p0äÏ*ÐÆºÉÐïwíL<èGoýwl'V¦°ÉÔOýÙ%ÿüo¡ð
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/70/2f166eccde4171fea27c13f89e65e36ad1cf37

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/70/2f166eccde4171fea27c13f89e65e36ad1cf37 (latin-1)

```text
x+)JMU035c040031QpöMÌNõÉ,.)Ö+©(aH:á­¶ù¾CÊºôßýò²&³¡*sóKSã*âsªSóRô>=oÞª5¿¶W9¾Æ4ý1çã?Q$¤"ëX²ag¬æ\Õ«ìÔ64]Yé¢£$µ¸$¾85/lÁ4Ýu÷ìxè*ó­ºÖ§ÿ)gªr÷h0-;ûúèf¯Î]!Ös$;ôÔ ÊÁææ¤¦ ýrÖü\7OÃßÝlúxªwgÖ{?deEé ug#Ný-.¸ÿiöL!cµ¹Û?¤ª+M,*ÏÍ/K p\ó­ÍäÖªS}sÕþÎ<tU}Ï÷ÐuÀ,áN³È_úÖùÍ·Ó¡WZ/°#[RYZ³Bìß
>«ZW¾á¹²ÝÁÊßs6aU³ yúÓ^®HèôM×Ò^ùç"²âòÌä¸ñ¬¾+¿µOj,yþgFãÈéXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV¨òªÜlhà@RArFb^zj
0\o)g&)O°­­/L>¤å²ù ¯

```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/74/26bb93517724f15fa63267ca8206274327265d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/74/26bb93517724f15fa63267ca8206274327265d (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÚy/³¾·¯úhYOS°×,û`©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨ÉïZLYxéàÉû³ß¥HOPâ:ZÑî+8Ø}NöÌúðê
÷Ù7> Bf^rNiJ*Cßay^Ç/:nOvb»ÄXQQ\Ì['Q½ýÿ-;óNê¬óütj]yjq^enCÇ±&Í«gÞÈàW{Vvpí×Ï|f |Ú#
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/df/639c6c910a0d72665c9e22bf7e7ebdba0af372

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/df/639c6c910a0d72665c9e22bf7e7ebdba0af372 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÚy/³¾·¯úhYOS°×,û`©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨ÉïZLYxéàÉû³ß¥HOPâ:ZÑî+8Ø}NöÌúðê
÷Ù7> Bf^rNiJ*Cßay^Ç/:nOvb»ÄXQQ\Ì´ð¡Ø³ô8o>¯ÎQ?§õG¡Ö§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  6
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/df/1e646074630f184f42be23fabada8bcfec9f2d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/df/1e646074630f184f42be23fabada8bcfec9f2d (latin-1)

```text
x+)JMU027g040031QpöMÌNõÉ,.)Ö+©(aX8;àÓÃuWÌÏnþÉ²qÛ5¾½òP¥E%ñ¹ùe©@¢´8U/ájv¸ø^ûÉWÖè	o¼#øYqQjrjfYjQ|NjZ	P½í½ÿb^îÚÒr`þ÷'b{ò±ª/ÊLÏ i¸|àAÈYÖ]$x&øßÿ£'d`¬¡¸<³$9f¼«oæâÊoíKÿÑ8#%r:Õ0ÃË5>÷]¶sÕëwUwÎ½pY± .uÛ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/df/55ec40255ac8f9fd67c7b78772e67f23a20bc6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/df/55ec40255ac8f9fd67c7b78772e67f23a20bc6 (latin-1)

```text
x+)JMU047d01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õN¤üÄ¢bÐÛäÓÜxËV[ÝÉm5»(yÔÐÀÀÌÄD!©43'E¯217Ãsõ¢øÛÏ%c\.áp8z¥bLr~^Zf:ÃÓkGt|×ø÷gëiÛ¬]$/CT¥dT1¬Ýõië-u¯Tf7t=+¼£¬åÁ	 ÝXF$
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/69/51bc2a585a667fd1c308a2ae53312fc099aaaa

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/69/51bc2a585a667fd1c308a2ae53312fc099aaaa (latin-1)

```text
x½MKÄ0=û+BÅB©KÅÝÕ=É"uöVÒv16!ýï¯X<ï\Ì<IÞy§£¬CÕbyò±W¢KdB¡p;ÀÑT­þb±wÁ4/£Mr	T¢{t·iÚ×Çç«ÝC³m·ûáÝduî¾°h3¼ñømV¯ñß%)) ?ItHÏÚ~(
Î&¤£ð|ÛAê<Z¥"J[ÓöI¾§×BÀ¨
ÉkhYV×CÂÀ
l+þ±ÓÀfDÎ Y}$_àþóNr8Îè0J[r
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/69/d1500f4cc13236c254d5b4771a787668547a39

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/69/d1500f4cc13236c254d5b4771a787668547a39 (latin-1)

```text
xÅmSÛFÇûÚâBZh©,	[ál$¡I©EÐ`lÆé|öìþWåñL4öv÷öN«];½AGm¬7*­Ôª²7wÃäÝeª¯¨J¹RVÑe¬Nûdê§Ã¤s#reïÐwN:9û£¸èuã~\$ñð/Õð"²
§Iÿ¼wÛÕN|Ù~ÐÜµn:JvsnZì$ýnÒ7*}¸¾*]Åw£µËoytR¶JêcAeMºnßäÆp>¸¾i§I§«jâ?×¥ÂÃdãÛ/Ú·½ô¬×¾«TRÅïuqð{¥"«Ê·CÅ<]0 #m¯!µh«4ðÀÐgVCßV÷ÓÍNÌ!è{`
d:¤Ws
î¿²Abõ½gÂpÚàXÙ£	©!1c°nÈ³8æë^ÕZ9éã'B·Ék!ciÌ¼9Í½ëì´|utñ1èxd¯1¢ó4Êq¦¦<CC³m¢k¤'Xp
AÜ)ß¸×AÊ6;S¶35eÐmx"RóN#ïì
Ó	hG %÷&Higgû ÑÝ84{¡åépð©kùz Ö³÷Ð·lÊ6äÀã½Ì!!wwfÂUõÿÇÃÐfë¨Ä
¸n[ úÒà6ø'Xfæ»¬Ù: U´Î¨nà'itsÜäqË'5ô¬ÈÚT=8 Và|í¤ß£=&§{L´¶X'¥ç?£l¨eCW«r~@¥5¶Pù½Tv)e\ÇÎeJß¯V'K:l÷GÙÍt
G³éMzË¸xJ^öx@ï|<àåøU@vaHe zª¶åFÕ)è	)þÄ§ ÝjöÇä*]hõ0}â¡sE?Ós²Þ$y»¿°¹éâÁÓò¤á!wýxóÐPY|uùm?ã>l'£øôýtÇßàSðgðó_HËà*ø\aæûÞ®§o5"Ùðx	þ¾ßÿqÉÃõñgúøüÄ\º_âÍ|6!é>}³õ³g«hì{ª9[¹:Ü[£p,iÝºÊãhþ0ØtKuÙ9U¬OÿPØnQ°IûL	0Ñerà¾néáGCÔ×lÉáì¶,Ù¬®îsÓêK,TÍIY¬#+µÙá·ð¢­¦ãf¯iuU
èO,J¾çËÿÈÓÅ¶çÛá6?)E0í°Ü»c³,µx÷Õéü¦ßËxÂ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/69/aa3684d04d7ab131b8c49a98db3053ff3f4bfb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/69/aa3684d04d7ab131b8c49a98db3053ff3f4bfb (latin-1)

```text
x+)JMU043`040031QHÎ/ÊKÕKÎÏKcX¬¦À¦ºrkªú¯LËy±ÓeÝPTe§Væ&0Hæ÷½º³ß«ÕDeNWÙZþbyÕÅç¤¦èå¥å$V2ÄØ=¯=þîê5ä ¥¾]|eª.O-.Ñ«ÌÍaè8vÐ¤yõÌüjÏÊ®ýúÏ µs@¼
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ac/c18a84c21c67e93a9044e4a6f8f0bd7011eb0f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ac/c18a84c21c67e93a9044e4a6f8f0bd7011eb0f (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2Ó²=5äRÒÓ.îÚ¸áÜ³U©Ekw}Ú:aËDÝ+Ù
]Ï
ï(kyp ñ2Q÷
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/72/140239feb54d6405808ca191902ce8d8117e20

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/72/140239feb54d6405808ca191902ce8d8117e20 (latin-1)

```text
x+)JMU021g040031Q(M,*ÏÍ/K¥Å©ñ9©i%z¿µgÛçsªûâøù×vOþ.WÅ¡£(3=¤åÒÎKµÏ~v×?èæþiñíã d-Åå%É0æqvy»=kó¤Þúö²£'¬1U
Á¢fxÏ¦s¾Ý<µó^çWÞc	7CWåfCÝ^\XtÑ¶½ÓÍ²DÎ®}µ°÷C®¡QyÁ 
8lð
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/bc/18df8a25b7b0651db0855f00cfd880cb1df2f4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/bc/18df8a25b7b0651db0855f00cfd880cb1df2f4 (latin-1)

```text
x+)JMU012a040031QpöMÌNõÉ,.)Ö+©(aèv[p3ó«RÞöÎÍ)ëkz,OAUææ§ÆädÄ§¥æè%3È³â\¶äþý&Uÿ×=gk°3ª¢¢©¨¨öl£BÎ½3î³'³5)&^è>U[XT_
$@ä¤¦L¯ùÈÖfrkÕ©¾¹jgºª¾g?Eé -§'Ú8¾~°Ùù­né¬_|Ê:ÈZRS3ËR`Vý;±ÁgUëÊ×3<÷O¶;Xùó{Î&¬êaä/O_1sÚË	^¢òZÚ+ÿ¼RDÖP\Y7Õ7sqå·ö	A%ÏÿÌh9jáå{.Û¹Âêõ»ª;ç^¸¬Ø
 ®²L
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6b/49281e6467676162c5a38d12b1bd0d00ced0cd

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6b/49281e6467676162c5a38d12b1bd0d00ced0cd (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^Ã½Îg¢GÔäT	5ë>57QÀT_ZXÉÐõõXíOg¶èÞkp8´ÌïýÜ
(ª2Ó3 &åóÚ'òÕÑêNÃæ³¹ÎínÃ¢fôöFQÙÒi«xþ_þ±T´)ùÉ PÈÌKÎ)MIeàæ>Ès¯:qãAë¼¯Ö¤åyQQ\Ì03ë@á¶%?äWW%ßÛd£µ®<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 '¹
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6b/62a1e116e6675e4b0e4a897074154e42afc563

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6b/62a1e116e6675e4b0e4a897074154e42afc563 (latin-1)

```text
x+)JMU050e040031QpöMÌNõÉ,.)Ö+©(a0©Êº=é¸ïäøÍ^
BUæ¤¦Ä§¤&¦ë%3¬É¬¹ØÄ-hl«hùQ±)BÒPe¹ù¥Å©ñÅ9%ñ©e©y%@å"ÁÛÓ¿¿ZP9afÚí¹{"E Ê!
!*j÷®ù{SÞM iódÀºêË}¡jKRKâ¡J*[y®
Ns«ßÌ¢P|dR ï¿Öc_¡*K@*ËR¡ÊsRÓ@î¨ùÈÖfrkÕ©¾¹jgºª¾g?Eé -óVÆ7¿øëë¬Î>þýjW#k)JMNÍ,K-Z!öïÄU­+_ÏðÜ?Ùî`åÏï9°ªY¿<}ÅÌi/W$tz&Êki¯üóJYCqyfIrÜxVßÌÅßÚ'5<ÿ3£qFJät,ªak|î9ºlç
«×ïªî{à²b+ ÖÐC
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/68/2914ccc0635d4f26d5fcde2d1a5bcbc855aacb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/68/2914ccc0635d4f26d5fcde2d1a5bcbc855aacb (latin-1)

```text
x}RÝjÛ0Þµâ¬cà4.ÒB×^8ñ237.NÒÝÕ>µ(r&Ë&éØeß¢7c{¼É¤B[§ÂÂè|?çè»áÅ
¿ñ<(W)²,ª\÷Rç)¯2O·¸Ê7Ò[ È{ùEûó9sO/îk
:GùÊuéYeë¢A´++*Ãw69Î©r¢xH.ãÁ4
HÃñ$HÜçýt¡>Còíò+1åQpD3Ç)U,&äTdÉ¤¢Tp»\Ûwà§ã^zlÿîï4uVTRÐPì÷àô0Äà[ý5¿T²J­L«LÖpþ*«íè.6÷-ÖÆù5K¢ª¤0Hp­w0êûQpÖÔü²H3?tLÕÙ4@c²õùû²þtëÃl½;7Úzý.)PUbûwû§Â÷íoÀ5+(Ó¬T§ARn§¢fTÂp°¸*¤jÌ¹uÁ²Î¾GwèÂÝnþ×¶n¹ÉIÉ¨ÂW²»'
Þ@ÇSÜOÂ«I^Äì	|ïkÔÙ* 
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/68/854c0adee7db9935f2489688f60e7ab931b348

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/68/854c0adee7db9935f2489688f60e7ab931b348 (latin-1)

```text
x­½nÂ0;û),Á,0UjG*âW!tèbøB¬&qj;´ñHú}±:?* ¡^}Ï=ç~¾^Åbïïno:ØKÃ8çq	úûKr¡0e ÚA}HÂ"¤¨
µÕÝ?OFÄMÞã¡_WØÍ
g2¹ÄYú¾;
Èb¶ô<xþ¡ßë[ TE'ØRdpiñýÉ¨4ÐD\&
Í2<÷½§Aà"»ûs±·*]òB+ JS
$hºÖ_[Õ0¤k1{ñgc×dõcÛ´î`R-i­2A½æ (î35¥Ê©Ô&Öêl1¬µÍ¹<J)2|´¨7®ÃèTÐip9s¥!y5¥O
.Qµïä¬· V`U¼ç yÁy±\ÿñ_xo¢Àkzí%v¥R  5?ï*äZñ]ÊÌ"ÛènF
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/68/9e8490cbcef2da80bcc237ea3ae942d14a6a46

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/68/9e8490cbcef2da80bcc237ea3ae942d14a6a46 (latin-1)

```text
xÍNÛ@»ÎS)Yñ
©bGCZET2©l¬ô*ÇÌOÔñ0U¶y¿×Úlºçø;?3-Ýgg?t³qK®,5ÏÍÏTJÔ9Å
cåLóÚ³@°Ól¬ÌúdÅ«¨ùX¨eÅ¾oNdN`EµO1y:Wê-W?ióØÖ±vAb³ñâp?¾RÍÄ!pÚ+ôã	ØJdÆ´àk
úñgDM )øNÖ!M­hèü¯£ÞZ._'G_²àÍ±ªÆTÅmÔ¿u:2®É<`ßðÃãrqº»É4 B³=Ã&Q:i/ÂûN·»æ7(6/ªI;È?$YmÑÕuvPßgeHéb´+¸_1%ÓRíËèúBÿÎÙùÿè­ã«a1øçÃÉmñi4¹È¿£ü)Sb×¿ØN÷S÷ÉÐ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0a/5929d16896334992d681a1b0099e960231c719

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0a/5929d16896334992d681a1b0099e960231c719 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÚy/³¾·¯úhYOS°×,û`©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨ÉïZLYxéàÉû³ß¥HOPâ:ZÑî+8Ø}NöÌúðê
÷Ù7> Bf^rNiJ*ÈmU¬>í÷6áÒ¯/ÿ¿3ºCT%3$Æ*ªeê]OhýSP§>sÖ2¨uå©Å%z¹9Ç4¯y#_íYÙÁµ_?ó1  *ô
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/12/dcb33876a5d6fac1cdf630c6347ed5bf315a46

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/12/dcb33876a5d6fac1cdf630c6347ed5bf315a46 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^ûBkÖç§Ü)[ñîÐº¢"l²ÇL¥ùe©E9]_ÕNáøtfî½CËüÞÏMÙ¢º(3=jrðâÌY«ü;7ø³^Øe}yq«c)µ0£ÿ°_0rÈN[Åóÿò¥¢MÉO& Bf^rNiJ*C|ú¯Q;ïÊYd¨-+rèU`QQ\ÌÐâÿþ³VèÍö&×çý¾Æ
µ®<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 i¦
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/12/6a0b783d7c46242880748302afbf821acfe64f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/12/6a0b783d7c46242880748302afbf821acfe64f (latin-1)

```text
xmAK1=÷W²Ã"¨xPöæÑ{É´§Ð¦¥MÅ*þw;è!äå½|}áâp8RÆçÙRcã«%¸}£´¶<IKTöëÝ_¥´2Uqþ·XÄ:mÖ¥´6É×²¢W¡Ì°{ØÁ»­[ÆQÁG~q5@Âæ#Zè!ÖB°Íï]È±dôûÍôyÉÄÐóÐÆk¸¹I§îê4Ð;Ñ_a£¸¥ÈE võJÏZO|vóïßÔoj§
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/12/561e3c001662dd416a2608a9db27c743cfaaab

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/12/561e3c001662dd416a2608a9db27c743cfaaab (latin-1)

```text
xAÂ  =óýfaaÛ&Æøï²h)¦ÐÿÛ/8ÇI&¹²tp§¾©Ç`=rdÙrfQJÊÌ:bÑ2ztÖ|eÓµÃÈC\²¤.*ËIæ!Eïcsd2²÷wÝàY÷
R®M_5-¥Þ_EÏe®åv`ÞÃ	Ñöøëúi¢4®­+4]º75?hóH<
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6c/361361a16354f6e8c12d9b9040f3d72328c7c1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6c/361361a16354f6e8c12d9b9040f3d72328c7c1 (latin-1)

```text
xu[oÚ0Ç÷OáMr¦´L}ÚÔÄÅtQÓèÃ^¬\ÄjpPìDÀÔï¾ã&º+²cã¿çeB~ÜÝ}ê	uäçvù¡êåf#äÆ¬·ùÐº°o_úÐÔ|ËxÕ³}Ü¾ðmY+àJÇxÇrÙmnÿ§¡vÐý¤¨A¥Îû
ªF¤`Ô,þÀæÓÏøMüQÈ(êºd2fÞÿýôÈÏïÜ[eÞ)Rîq½çP$T4-¥ÒÄuÜ|Ü!,£3*]Õiçó<ú7d@bÅ¯DGQï¾kB?Cã´£_®+I2{ÆK>^Ç>Cîº{gÁ÷Sz^´ð½%ç½Å/üNÕªdhÚ4òDóTbC\Ì(­Ññ;Ç`h\¢ÄÊ5ÅHÔVg@¾³aMf½`Fm&g%Á LÅÈÍdûÁd3«´*·'§ÿö<ÑÍ¶û/FÚhnÙÞíÖC·EÞìN¶¤Öx~%P(8ÕÎÈZÔÅE¸$`°+ÔÇíàÛµ!P±Û5)<kZ=LX·¨x|µ^¯Õ¶-YÀBú®ÕÜ÷Ýo;ÑjM°Ko|tïJcáí¿úÙ*¯
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b6/e18d97366a14cdadeaa18df06d3631327770a4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b6/e18d97366a14cdadeaa18df06d3631327770a4 (latin-1)

```text
xuMKÃ@=ï¯èE/æ "HÝ­Pzð²lvÇ¤d?Âî¬þ÷&m@ÚâÜÞyw>JãKxx|º´AVVw
l2I#L·ØÖ]È¨k1Þ×¯×NÁ¡¹°lá:V:Yal)$E°µ°>E$¡PµtjØ1èkpOQ¥ÆdÌEÁWË.Ñø
ÚÃqÅ1½qô,ôo~&»ìÇ@TÁ#FìªÿÇ§1P&"ïbÎö9c_Á×üs%ÞùlþVðÛ~ºëav sÑ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b6/d8ae962550cf847a1b0df8eb5a497c2e2cded8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b6/d8ae962550cf847a1b0df8eb5a497c2e2cded8 (latin-1)

```text
x;j1 Sëï1Z==­&ä !E:z;ÖÚ?ºB)FzkÛñeìfP(ðb"%2Rò¼¤h£÷+Õ ^ÝOÝí1m¥ìEÑ3æ¤3±b
Å£'¥àê1¾û~ìðYÁùi·®[ëï·V·ûIz{e¥\Bk×Yz7íüöÿÒUUhýxÚä¯Á®ð_îÚþHø
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1c/c2b356238c1d926a82ccdc532ecb095c3fac19

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1c/c2b356238c1d926a82ccdc532ecb095c3fac19 (latin-1)

```text
xKÊÉOR06gH*ÍÌI±âRP(N-)ÉÌK/±òRâòóK¬ô¸ >ø
°
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1c/7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1c/7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21 (latin-1)

```text
xA
Â0E]ç¹ÉL7ºtáÎLi-¦´éýí\}xð?ÕR¦­Å]E´P aÄ®ùHBêÒ)³â¶=©gÆÌH<:O9w1pÎ		r@c!)^Û§ÎúU×Y?¸>/Ò×<zíßCªå¢!8ráhõÞl	µÑí_ÿM5>ï<æÛ2¡}P?UEK
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c2/a8ed6820cdb8034b0487dd6558c985b03915c3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c2/a8ed6820cdb8034b0487dd6558c985b03915c3 (latin-1)

```text
x­SËn@í¯°Ñ¦`(6D|µn&8sIÎôaü¤®ú	ý±b+Ý &]sÎ=¯aÃÅ
·w76
2Â( ¿>%
Q@	Ä¤²Þ!OÞ$f®PDÉ@9½ýÓt½ùl<'ÛÎð¦£½uù³^Î×çãû :úýó	ËF6L""-Rä(Hs	è(òõAc×Ò±ÜÆJ3q£E<V¾PoÿW(«Z&¬rÎ42Ý'­xSØ;s-m:0®²/a°ÂÑ<4Lhºæ<sWÆ9<¦z.@RQ}kuÝæ»¥Æ¦{`%HÌa[¿HQ/Lä
B*JÀuKTê*k©s+­z¸4gJC²AÒ?¶:ÀO3ëXþU1ý»pN=Ó$Ë8/U½n¦ÿs(ÉvÉuK]ÁhLÕÕÜJ,]6ªï²TSD¿ïÖ3j~×ú((ui
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c2/9da8607847464469a7999a4dce5c96e44d5e63

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c2/9da8607847464469a7999a4dce5c96e44d5e63 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgpÓ²­9´AP'xÙÝi©.^Û³-!
ªR2*Öîú´uÂºW*³ºÞQÖòà Ó¦R
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d2/b9d27de6f98b7f33e08b0bf938f6f041fc4c52

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d2/b9d27de6f98b7f33e08b0bf938f6f041fc4c52 (latin-1)

```text
xmÍ
Â0=ïS,ô¢ BAñUB~&4?%ÙëÓ¡Îa`¾aFù¤ð:ÜÝå$¦¨	 sQûjoíûr$±Ïß*L½uæÁEÆ*3jVìFËGÀ¦VÑ¼Î»¸îbÑ9y/þÂmX·#US,pºÃâ>
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b8/3f2ec2bf90eccebe9d463baa474e0dcbf1cd43

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b8/3f2ec2bf90eccebe9d463baa474e0dcbf1cd43 (latin-1)

```text
xKÊÉOR043c(I,JO-/Î/-JN-ÖH,(PòsqåRPP©vöuôvw
rõ÷ñwñªÕ/M,*/JMNÍ,K-ÒK&¬¶¸<³$9¨R«*µ £²(>3/9§4%5>%hPI~Q&Ð~ê(_ïxg?7O÷Z}¨
M. Á:
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/78/6f89ce61092714afe4631679425aca97a48ed0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/78/6f89ce61092714afe4631679425aca97a48ed0 (latin-1)

```text
xTËÚ@Ì¯h­/´RK¤\8Ï@,üÒx´\FF»HÆ&#ñ9«rØS>Á?nñ8$Z|èéGuUÍ,³b	ÃwøEUjÐyºÌôÀ	;U¦¢Ð
¤LG'3êIÌ1dúÝeJð(RÉÇ«6	³¢tB.&_¿|~÷-$ú¤pÔû²þYÀªØóí]Ë×öÌ!T¦"¤bÂóà&Å¡ÇGù``B#Ïý-¬HÑL»]ç_V|s:Ñ5ããÐ-&8:n(¹D ÍÖ-î+ÑI<VÏ]«XÚÎ¬O'síøýà%=!K9ºÃwZ£³¸iv$gÇIï¸TáiÏ
@;ñ¤òø{£®êöp`ÁFà°èS+3s6uãò<`0öý¯ìÃæBÛú÷ºÊÎÞÊë×£ÎþÜH*¸ÃÑHÖ;o=ÐÝ&.Rß¼KdQ~Íg]­Qé=Te¯ Ñ÷õw{½Ú)``ÕÀêîyÆDxMD·|¿-ÓËê	2ÔtCVZ7^V@áþ±ÞÑÍ^yYà»q%!,L¤j^ºÑX C
?*
è!:nÒ=à¯aªëÜ«Ç£1lÁZït¾Ö°î^$y¡wÏ§ýGÔêôÒì©ÊKX¥eQ¢=°Õy ®AoQu(¶õËa³*H#Òåêvõ<§ËM0×a
ÆÇIO|UÌ§S4d×+)&ôóQwFvÂHåÛMÅÝÜ)ÅÆ4àL®¬¢
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/78/1980c4eea20d8afae8937cef4c97ccdd5e75cd

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/78/1980c4eea20d8afae8937cef4c97ccdd5e75cd (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Ü£L6¡ÂÁ<©yßÅkgÈ.gXRÌzr|ºÛcÙj«;¹­f%BMI*ÍÌIÑ«LÌÍaàð\½(¾àösÉØ¥"K8\^)Îð±üdv®ùíü3JÿíRù2Iå&DAUjAFeÃÚ]¶NØ2Q÷JevC×³Â;ÊZ 5Oè
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/78/5a3b4295ebb4a89d753f125757160056063310

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/78/5a3b4295ebb4a89d753f125757160056063310 (latin-1)

```text
x+)JMU021g040031Q(M,*ÏÍ/K¥Å©ñ9©i%zÉ_?øX>ºÞleónvíi9á|8te¦g´4¾ã{ô"ã±©raE~ðñ¨OÍµg$gÀ,ÇÙåíö¬eÎzëÛËN°ÆT5jáU>fÌùvótÔÎ{_y%ÞP<U^
u{qIbIj|rFb^zj
ÐE?Ë«;ïm~ÅôhkàôòF ±iN
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/46/2a3d157cc2b0112c53a6ec2d9665444ab76b39

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/46/2a3d157cc2b0112c53a6ec2d9665444ab76b39 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÔ2=Äï7Owÿµb5»aÞñÇSi~YjQNb%C××cµS8>Ù¢{¯ÁáÐ2¿÷sS6 ¨.ÊLÏü½*ã¿GçûÞ	³JW,i±]}'µ0£ÿ°_0rÈN[Åóÿò¥¢MÉO& Bf^rNiJ*Ãûµç÷´ÌyóocÛÉãa»NùÊzBT%3ÜKI(IæðwÚ§ük×­îóoæëB­+O-.Ñ«ÌÍaè8vÐ¤yõÌüjÏÊ®ýúÏ òMó
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b9/6d9f252508d54c702a72bf473d61c0400baa4a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b9/6d9f252508d54c702a72bf473d61c0400baa4a (latin-1)

```text
x¥XýnÛÈïßz9jP.}9Øq
M»É'Ë9¤º Èµ5E*äÒøa÷GÑ¾_¬3»$wIInErgv¾3ËiOáÇ_ÿü§yd	÷¹xà	ùL¾òá;Àôéü8IÄ<xqÐøVD~Þ|æËù:9¸çIÄÃWó·K>ß¾¬ôDo%Ø¾Æww"º;Àßãâ^mÇÒOBúsmGU­b?p¶³T)×è
.Ù»ÁùmÏeC÷²{3rÎ¦OZ@t=÷½ÛcÝþEó¤Ñ@ßÝv#Ðãý#K%CQðÐòfqñG7É©ô¤ðÑ±Q*!IæËbJ0Å NáÜ}ß=sÙù]º#ús·×ùÅí)ýÚÍ\XÆ)8.bøq²¹TÒ¾
øLDÜ÷#vå~øeÐC{Õ>lØ+ï·7.à+GÊ´kÏÑ.yâñ1Û«Ng2æhë%øÓdìÇád¼Lxò æÜ¿O³ÅNßÂO0]KZFg"?3©ìdÓl6~=9)¼ëÕEFÆB{_-¹/y4ÅÅ%·Ê,ñÐ± 4Áw;§/4[Æô@¥Ho1}ú×"
L_ä§Âãý>qÓ]_ÍD/è*ÑK¿6èÓí¹Íâ#ÜóµyÜ*.÷y°2t$°xm±ÓëB¹i&%¦¨áyÔ^Ò/OøWæVÇÅaôGì×[÷Öe7Ý¿¹ðýQã½»¹ü»Ý¾«KÅ^;oÞ}lA*>óxæäl¸½ÙRÅ¶]F~(jap/ »b£¿ÝÎ9»uÎ®6ecú÷-8lo^¹ô{&õ>F
ýôté_'±9ïåéÂLUÊZ>Ä"°9Oµ³£Ö^x-Ð7ÓâÆo6¾¨DÚå-u X}sØ´2îCÙÎ¾Ñßvõ¾zhÁ»1^CrmGÆOpÍ«\g¬v[ï!ÈÙr\²ÓJjÃ©Xd¡'¹d§BF¤Z
¦ð+¬Ö3ËXÏ-çu,|Ç0óÂWöC#IbqM1Qî-»Kn1HAöûF·`ÕÊ­È×Õç¼þti/eU,uß}gOy)F,K±i À
Âã?·V{,+N[Í,¬~T>xl<*?óÂpe ûØwXßbáR!¿ÚµDö§ÎÖæ°Hcl®*"Tñswì¶MçÜ1´Õ¬Vi4³§/pÔîû>lÞBÛÎG1U°£è¦]ö÷ÁoðÍBA#¤2~Ø2t£S
Qø{Âq\y»]Úl0læ0f
µiÖWVÇ'ÒüåKì*Çl¶jPçe-úé8¦æe2ãO¶ÒDFIäÎ*S¡¸ÄÎ­½Ø¼¹ô¾öjiº¡n±´oqÍV\ÐÐoélc´¥"T¨ñ%|ú7NP§Ó½[x«Æ\ð^4ËÉÄ6x{hNOá¨
Êñ!:ý´ju2c§¹?©,ÓôÃY´ë£ðsJ)Xúÿ4
Vq°sH²µíúèND
JFDO¿C¶÷¢·j¤tÈ*ìj¯rô2î¤9ðpRË?Ú±Bb¦ÁBXñkÈÏC¢ßÌEz«±QßIßðo±¹ÄCÑßÅm{5t¬@6K=Ì%xæÃõfÒ)ð®àÏK ½7íhýåËº2¼Þáï§;FàNÅ
¤¸¥_2¿dF¸5v³yªk2Ù¦E?åeº²×9Ø¥
^çTE/[Çb·Öÿ ]ÕhÚÍØR'¶ *YÅdu©Óé¨0]»Jí$#Æã1¾5ÄásE=ãm(z,3CÅ× £æÉG¹
AGµü!§»
ïå(¾ºA?Ô¸,dÝeÔNdÕÅ
RáéµYõánÓp'ën5kÔ¾Ù°²BÓ7ü0°Ì¾â0Ð°ß:ÝQ
)h/¡v«/Ô©kLà¡FyN¬øgú`QËâC·c¼!Ù]PÖt[YËï[ôeI¾ÁìûFÂa"U£æÚÑ­¥ìÏ>QL¾öµm":,K"
¹©J|d~>t³rîe8}6<ùx.ìßözyLÊ=ã7
¹aCUÆÅÙù¨äöÐ:ÃÚBôI¸ÔÑt\L±67fÄoL2R_mOåÿVÉ¯[Ð¦ªIJEF!ÀÏoÎÚ½ªúbF¡ 8E½é©+]Jt²dØB§hrÿë°Üãö8àÄgO
áôámc> ~
é%8/B}DÅ¯PQèÔ¥7hCwdùqC«t®¯{Ý³Î¨;è·àlÐ¿è^2ëÚ]»awôõû#
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b9/e7aac534da6103ae13fa167be1babd4ebcad7e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b9/e7aac534da6103ae13fa167be1babd4ebcad7e (latin-1)

```text
xAÂ E]s¹fèÐOàÞ¡0TRJïo=«¼äå}_rN
:R§VÁêN[mUO!Ú 0CäÈ+$ìFËbuQ1Eç#*ÔQ²VÏ,£Ñ¡÷»Ø%ÜÞ>¥Â«ì.3\7JH¹<¦ìÒ|ñ%ßAê%
ñ¨ÿÿoÆ[´¬{{W^KýÍ7@ñJß
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6e/0f6f058a4b93e9d3ed40d9e8ea3324bd5b48ce

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6e/0f6f058a4b93e9d3ed40d9e8ea3324bd5b48ce (latin-1)

```text
x­WÛnÛFí³¾b¢¥Ò%ËGYq(!Ë)Ò" xYYS¤@.
)úÐï(úÐñufyÑb -táÎÌÎíÙuüÐNë¸ûÝ÷<pýÄcðò[-6QóEó¯j{K~xsÃ&~W®ÍÅ´²¯êø	a(ÍâW¥bµycñ7¹]³	³ËÛ¦Ï<ËcNRö;Ö2¼cøÄÌòÙ\îSM.¬wóëÑÐ/Ì«ÙpªÅ+4	º,íë0ßÖ/ïÞZ¤3¾êgµZ³××æy¿IlÂE|µ`RïEñÃ_!´Ú§Àð@t;¨C£Y-¸±W#¬$áÒ º³è»L.B¯ø¼Y´±eÍÉkÆzn`øîsûÙéI÷¸Ój_Fº%ùÇX·Úlîz¶óÜH¥QÂù6w<[Ø_ñÅ3Ïuìç§Ïº'ãvë1_Ú­]áÌLí9]¬Z´á*qb7âÙË¸2{Ô@iY`éÿÙ~R-Î7ÈõÊ/Òrlßwl÷?A(ø|ZÄ\&Ûø¡í§öZf*ý©%vjÚ°\GÛ6594èóÜ©&þÙªVÒHSñÖpãXÀ]È=hP­uÙ³­.zî³ ^ûMvv@Ëðù3½Ð­CºFþEL$Q@zÑÍ,±e!fæøzx&-Ü×äWº]Ì¡dN°Æa ø*¤´¯l7ÉÔùÕø=0ÖFû_yÆ[MzziY®:Yo}L}ÎÅ6©PY¬½+ú¾Â»Ö+Åpë]±N&çÆIÀÚùtË2Uü¦yk¼¹Å/|"ÈSÈ¥ÄÏ[ì~!ph-ºF.ñx1±VhuXáÙà.¦.Zâ11Ü·%S*°Í£R®Àê<	Üÿ
+m¬60ºôùh K%9¥ß;È ÔF¬Ìñ±mLÐCÃåçéX{¢$åäûm`Î/òÌÃ$ðêOý%[ÆLhÜÁÀ¢óO,kÔÙª^Í&8xäÉ]®2Û¯hRéðTqÔ*Ã-ÖÕð)0sü¦X©Id<:,ìÀóYÏXÿ°~¢%òðUú.oGJUeBÛjÓTÄ2Î¦5ê}ÁÄÛrìißÙx¨º¤sÛ`0°ÆùæÃ×T­,¶¨pºµÎæÒEïû£ëaÎp´ß'®ëfÆÈ5Ih®]2>jbø<
õc>%{0Æ	y	K%¬Ýi¤É-S´¥ª¡$sµ°ÞôìU'­¹ìÂ4LÞ BÍ{`~ÌéôEk'$©¿¶Öæ¶¿)wOÕÍ½ÕÜÞ¶räª¡þ¯X%7ª ½¸HÒÙñNNvµóñ=©äÝÜ2¯æÒYè
×sdâJï%Ißòé=F%i/õiFäê%,¢$S­AN£U-ªÂ7RñQlRîÝr87¯÷tú©?íð,
s%&GJn,Jþ?Ë1æ1´ÅétøðÇÃïû£²g	À·NâU¦ááoº Ð=$JøbOVÎo¯²Ò#!eYå­ÙGggPGáwñhlMÎ¼
sèÑÔêkSrsBé¾Ï23e7xÞä1ÑÍNê1ò´rìØÎrÒÇ7ùßt/£#z/SPj®â½^»Ç
"qÞíìDË?ñ´âÍ ¼ú*Û-ªÁdWKºÐy±2Ç¬HFÃ"íé®YÐÞ
ÙW®äe°êþ*7Ñ¡y92ý97Zå]z¼©9û{üb
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6e/b51102de51b3b3b72c360abb8c419008bf08c1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6e/b51102de51b3b3b72c360abb8c419008bf08c1 (latin-1)

```text
xWÍnÛFîYO1V`J[v¦¬D»Id·©ë,(remE;}¢¢úz±Îìr)êÇª%/gç÷oÆã ÃÓß>ýæ½ ÷9¼úÌãé]r0ãIÈýéÚÆ+ÏÇ·¿JÄ'éÁu,¢¯
änm¡Øþ"½KâDÙlíÞÍì´±ôÈ¼)KÄõTj¨À#$Qõü\ØçÄiYÝv6ØÃÑâwüA¶zoûNÇj÷H®^{äó9tì6ëöÚ6´GÌê8ÖÐ¸ßlÔÒÌÍ^¦¤Y{PÄÌG/bîÁk8í;=W}»ÅNí¡õR:m×¶ªRùÇªiÛNË&E¤¿È¥õÝ1H¢Ù =kßõ¢Ã¹5½Ëæ­e]]ò93ÝÅüê2>]]zQ)÷fi~s¥ÍçÖïXã|rùüêXã)±8JÑ¦2cSÀY¸»øp÷3Ý¤­HÚG2)².ð¥øÑ¦¯£«èñqí^Ù>ÁY7[ü
ÍÂ|ªìë
R2}awGìÝ¹}n³¡óÒµ3övxúµí§kË<2åÑMzýÑT|æÑÄØFÃ6ð¬¨Ã0s½pÈ¦	w}¥8<¦e(ÔÃÓ°N~ØV
GVëL;`b8ofÂóÃ#4RÀ¯pnÆ
C$§~2ßÍ\ÌØ<>aj9C>vMP?Æú×¨©mZeUR	?MEÀÁ8l%¥3ÄÐ'@P=>æò
	fü7|ÆQ¸øgÎ©îÍ%]óÌØ« EUaOÄ3vÒ`aºEq'UÙlRt*x½mVn(ö0êªCvS0v}s×oüÖÍRÓ÷PïÒ:¼úÜM9¾Vêú'Â½Q® Þ&b2ê{|,üè%úaYøØmý¼öe´VÞòc=moÃtiº4áÄ2
¦â&Ü+>4¶ù_]	DLÀ e¯ Y-/Å©c´RÁ°GÈB÷°+«¹Üf¬bã~YD¢-ê ?òéM"ôç.þZü*c,¥<C¶5öÝ&VÏXpÔàvË8lJ~ÔuÚ~¿YÜ¿¯¡kEwÉæ	õÆÆ
ÓkzÆoÝ:yÊÙtº4Ëy«-#õMÄ$bD
Ô°çQ ðf5áëÅ}ÆwÈê8=áJe6¨X%?#Üao<Ø!à[Özù0L9_¶R"þBÓ'W%í8%nÍÌóuÍ:XYv9lPi<ÄQ¢3OßZ±\H= ÝUH<}HB72õì1~ó8C
Ô3ÕVüü äË_)èò¦tCÑz(@Ý"eWp¾ø#@ØA	Ì0AÐä!mû~Ýõ
ÊÉ}ÊêÓtVGËgYqIÏ>§IÑü¤=aEººþà Àä}Y¹HÒ+¤[I®¹)©
OT¶ùN+¯î×ÊBs&½À7T·b¨Äù×J·Ç~²QCvÌ×Ê)×,pwÀ¦*Òt8ò|,ï¾¬FPZ+ÔZv«5£¹9àª¹©¨!B,-þ½ÈkõºáJªZrÍÚ¼­ÏrÂk&¢|ì(Êb"¼sGkì~%Y£µ/QqÁqaD£Åõï0¼JP8 ò$TSî¼ë<áKvkpï|Ô?1§kµFÎÊd[½#Üê
îÿå´!IW$çÁ÷(VÒ5¹üjvz¸uÏ;"ÖòfrËpÅ\
kçõFÅ<ÌQÆå0ªn`¦Ü½Õmm·£=´wBP»]c³#¨·Ö7åÞÊsýt>/LhÒÞ¤!^¤[X&0SÌ?RE^@Z,d
Jtáÿ`[ ,ò§pBÔJïX~g¤í
&Xý~ÿ=9½®ÿuOSV9YàôÎè=Zø ÝmÂ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/14/53fd8766e7efd57079909966db8c9dbc580114

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/14/53fd8766e7efd57079909966db8c9dbc580114 (latin-1)

```text
xKÊÉOR041`PÎÌKÎ)MIU°©J-È¨,ÒÏN-ÊKÍÑË°ãBÊÍÖO-KÍ+ÏMÌKLO-Â!]¬_Z_\YÖRÉåëïæêïéà£Q¡PÓ :á4«
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/14/d8b6d325e0abcb4a5eed6200d2faf4fff70147

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/14/d8b6d325e0abcb4a5eed6200d2faf4fff70147 (latin-1)

```text
x+)JMU06`01 ªÜl:÷£-«RZÖË-2¼Äßn àÅÐ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a9/4dd36d88c20b2bc94f169628adf20e28b369fc

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a9/4dd36d88c20b2bc94f169628adf20e28b369fc (latin-1)

```text
x+)JMU°0e040031QpöMÌNõÉ,.)Ö+©(a¨>:OyÝ½ob>Z<fþJæR%TeibQI|QjrjfYj^2¹·nØäå¡aÓäó13OÏ3 7}"Ú
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a9/66d63910328e747ee092ae0e8bffbbc0a47329

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a9/66d63910328e747ee092ae0e8bffbbc0a47329 (latin-1)

```text
xµérÚF¸¿y
z V9£;N0Æ Nê0tGHh%¢Ãdü0>J^¬ß·.ãþ¨Æcýö»ÏÝãÍÈËWæ/õg$2üúÌdöó©o/aÍ$¿øüøÇ#}»vì¹mAÖoÛ
_Ó¸¹õ¢gõÒSÛ5ÈbäÍ7¶^nýºÅîlÕo@>r
êÈ¸píÚÅó]æâ8Þba»:¼sðÛU¹ÖÚ©]ÐÒ¶vÙsCzk¸Æù»`n±à«Ki¯´åo·+Ê
CÐ5»`À¦\*õz5h_÷t:Ô;ÝÑXV
 ÜØÓ?ê=Úí_TOJ%ðÔuk8&Â°hs¤nÄôÜ $AèGfCMô%9%mýc÷\§í1íèã
¼ú¶Þké=Î»QôÇöÚáú{Ü¯Û.#úÇ1½ÔoÎ­a46féi
r5¸éqQÏ¢ùùBâDÔHFÎ,ÃM¯¦'J 
¢72P¶Y33duÞÆÑÑaáQ@ÚÛC¸G8ï÷J¬D°p»f'bÝµ=WîÁ}@Â|²ï}Xb9SXû, ïÉmì¤õ¬M²ªåzj90}ÏqèÀÁ$gQz.;Æ" AÂþ^T ±pR?ôÅí¤Ü¤	cB\÷ÇôÃµ~­ÓQ÷3äB·ónL.éÕ¨ó¶õn_!1X|.× "}cÞ¼²×µUÞ6y¡â}é3Ã×æ
e¼¤ãwC½Õ¦£qëü2#ß£ø7GHBæcECAø¦sçÙ¨¶2Øø~®pà3C#âc¦>Ìjé;È½Úlúèô¯KÛa¤Ò¬¦BªoÁÂÊA*ø"Op4rI/CðÎ-ôðTø%ÍÃ4 ¤Äq$8[Y1¡DÖEÎ»Ù{È¤ö ë!°L1òÂÀÈ1NÀ2ô@Kä¨Ã*¥x¬¯oÇ)"tH,qµ5 |	×)úø®YX:ò&»ZÔ¬m~×¶`ÊíÜ^µ¼#/Ä(Dæ|\ÍrÀìOëÊîjKH0h¡\_ qÖ´ÇnY|¾ºY<luG:`±Ë×û?t'#rÂlbSý4ìWÊ:6x:E ÝsÉLÛòÉ¯£MY¾Bb?xÇûÒ=/|çãÌ°ðV4¾$õÍûÂ¶
Í]%>V>¯ª ¨fc
µzÝ¾Û®$[³UgÝÜ{0ÞV?05Õá-i¤Ó×J®õBï%Ä$OàkÓj¥·£¹AþÐv#Ù.qL/|vé½!èSUYºã 'C&y§>RuäpOds.ÁÐ¿úpX)ñÃ9sî@!ÐnYh¸WÎ»swà@òêÙ7q(8¾ÿ£%NOÉQ^ke/^'MÐõ4SMóûm¡h¯N©×É¤ÕN0x§(¢Ó	ÊéDDø¿
¢Ûiì/¤'-ºO^-Çë9¬Ítbm§QjnÔÇSp4ÁOäÚ-¥q6ãÜ
SÐÝ¿ÈLå$ÓßQãLAxÁ°Ëé§ÐÈûvc ©$å(d!#1ßr2A«ØyóNtë®&sÏçéGl5Oàõ¦.ùvxgª¨!rE¤Ú0½#T=)5q	c)F:øcW+ä>-â»ù\é»fÍúT¸RÜÕr¶/)éð­ÄÑ!LV7ÄÎyçÿ=2ô7¿ÔD¿CÉ7dôolGl59eå $8àn(;ÝÏÜ­¶´/r©"µOýk¡.SpQM,·_)¼¸ÈûuÈj8+DÎ«|dß°fÅ~³UYMrèço©
å3Îä>ÃKyXG9EôôS«;ÎÕ\?$Å¾Lçí!Sm8qõÅ¨÷EÆnÏIü-(<Â/J6ç¡-{;Fñ~ØÔh=3ÔË¶¶òZ¯`2CN<£¤os\ÍXéñLù®pTOt¶ÿrÐ¤ñìGaÀIñÔÄKé_÷zÒ1CkÌB=< Ôy XÈäÑqç\+ù¤ÏÇxR±;[ã©p!Ø¦p«ÅÌA²Å-Êü/äý»Fx¶M¢oCOÀåZ¥ÌÉg}ã
·iËÐ#`}yØ¤+º0¥Á6Ø
ºbôp06`0º4Ý±tEæ>6&¯Öû÷½îykÜô5r>è_t;4µÆIÐ÷Ãî`Øß %Õ_Ë
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5c/615acde2b56884adf97b356fe9d0ce45d2b889

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5c/615acde2b56884adf97b356fe9d0ce45d2b889 (latin-1)

```text
x+)JMU06`01 ªÜl_×ýö¿\ãÏÀ°ø¦ëÎ÷÷&´} £
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5c/3ee77dc7eed5d62c635222f14df344c4f50054

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5c/3ee77dc7eed5d62c635222f14df344c4f50054 (latin-1)

```text
x½RÑNÂ0õ¯¸á(ÙÂf¢AD}Rc ß®»ÈbYk»IÐøI~?fÛudC}µi²ÜÞsïÎ9÷ÆÇÐ?zðÞ}è+Ì\`z]#¼©B	g3×ÀÃd¶å×§J)èöl¹«xC±ÚJ¯ SC«ã¤Ùt~ÓË)L¦·õ?ûÑF®£²¯íù1léÛê4£¹dND	.IÁò4ÂÌ'ÉÖ¡)ÁùÝì:º_ÝÑÑâÑÀÓ£±·càÕÙÏJxÿh<ÜÁ5Q6|Í·d¥¢¨(Ú Æç	Vo|Á7(}ÌHÌð7úÖqKßqU9ÉcZ?m»¬¡å¾14OÀâæ&SnJ5°=DXCXöòY£ý·wÛ¶Åi%S'µhìÕ ¡+4ÖP¾$Oµ)Fiµ	õõNúÆ'ÜÚHbd¦;Ò.©éû
àlï
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/89/0e64e4125e8475a2c5a9c90b3e50bd486fe981

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/89/0e64e4125e8475a2c5a9c90b3e50bd486fe981 (latin-1)

```text
x+)JMU054g040031QpöMÌNõÉ,.)Ö+©(aø-~2G¤gnDúÝ#ß?Û~®ªÌIMOIM*M×Kf¸òÁÖjÅ·fDjn²9h½U/úTYn~iqj|qANfI|jYj^	P¹Hðßö´çï¯TNv»gîF¨rB¦d ê¢Ä ®Ssä¿ýsÎWÜ}òfC,zjX4§e&§5Ä	Ônß³t¯ÍÆ#²WM­>¾.m< ÕPXT_
$@NËIM¹©æ#[É­U§úæªýxèªú5þ8te¦g´|Uyd1áÀjùC3m>Ð´ÇÍëÀd-E©É©e©E0+ÄþØà³ªuåëû'Û¬üù=gVõ0ò§¯9íåN/ÑDy-í^)"k(.Ï,IÎÏê¹¸ò[û Æçf4ÎHE5ÌðrÏ=Bí\aõú]Õs/\Vl 7þÚó
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/89/e68b3ed4c3bb9701f892bb6bf5f2e23cc4300c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/89/e68b3ed4c3bb9701f892bb6bf5f2e23cc4300c (latin-1)

```text
xWÛnÛFí³¾bìÀ¶ä$½ÄI
V¦]Âª¤HrÚÔu¹²·¢Hùøc>}èS?Á?Ö].EJrê³s=sf4	¢	<ÿú»_=¡ä>×w<¾ºMög<	y°wõ¶±öÊçáñÍ¯±àIºè¹dD(6¿HoÓý8a6[¹7í6^Ì»¢'>C×>b½þ
GcfukdÜo5iæfÂ/
ÓÒ,É½Èeæ£{bðNNáÕÑÀî°{lh}¦NªTà)¹jì÷NÇ&E¤¿È¥®õÝ5H¢Õ$=ûû0p½(ãpf
Ç¯à¼ucYç|ÁÃe·1¿8O¢ës/
ðqÅ½YÏ/´ùóò-Ë`OÏ_^êc<¥#G)úÑRfl
8Ëbn2wïxè& mEÒ>*I-|Ï
À6µôì°v^ÖÐãÃÆ½²},5³nöð7´[ùTÙ×¤d0û½Ý³wgöÍFÎ¯6J7NÙO£wìÈ>vz¶Ì#SÍÓËO&¤âGScCMSZXSjÂ¢£ÌõfÀ!»J¸ë«,ÅIäñ4-³¤ÜD¡X¤F5tjüãÐ¶ØhluNµs&óf&¼l ~s3V"9õùnæbÆð	lPËòô©kú1Ñ?¼fChCÔ*»¨Jx}%F»YÎ6B AõøsÈç<Íøï.ø"£ðá¤º7cpvÉ3c·U]YNÙqURé}&Q@`Ve³IÑ½%ªà
"ö¦Õ®ÜPíol«ÙIÁØñÍ¿ù[¸m¾í)ÝW°=äwS¯z§þ°Do+·YíJBÂ=>~ô
ý°,|ì´~Yù2:E+BÿTù±¶·fº´M]pb
@Åc,ó<p3nlò¼·Aj^C«ZXPGg'InÝAºÈ¸ýXÍâ&c÷Ëòaö	øÈ¤óDèÏ}øëáÏü¨ÀN¥ä×X,åò¬±¸6¡]Q>ciÀylPkÛ£ÝÌ¨+´ù~«¸ß@×¾m!SéMÇkbÆoÝ4yÊÙnºy4¿yõfú¦b1"CjØõ( x[O8&ÆºDqßÉ-ò9N4O¸Q
*VÉÌtØÝ¶òµZ>!aÎp­Ô(¿ÐôìÙH;N[1órU³V]T@Û8Dtæé["G$°¯
çIèQ¦^<"ÆopgH~zÚ¡Ú|ùÐÃñRó.ï`J×­fÔ-Rö³Øþ[0¬qYP¥¢:¤mbÇ¯º^A9£OY}Ëêhù,+.Ùç4c2´!Ô¤+H ëR?&ïsí"I×è¶\s]RHlý*9>k¯îWÊB&\=ÿa»@íÕ­'qþåqÒë³-gÜó¥rÊ#Ü-°i4Ý;Ë»'kGV
µÝjÍhb¹jn*æ'jUKÿÞdÄzÝËp%U-9¦-Í6_9Û5Q>¶e1JÞ¹¥v/¬YZ¨¸à¸0¢¡âú·^%(y*À)wJ^EÌMÅeð%;Ë¸6Ó³:cç½Êd½#Üèìÿå´!IW$çÁ7(VÒ5¹öjjz¸õÎºÝ"ÖòfrÃp¹\
kçõ.Å<ÌÎXFÕÝË[W±´­lu´ö©j«k®wõ½¯®mÊ½Ú³~ºCoLhÑÆ¤!^¤[X&0SÌ?RE^@Z)d
Jtáß§uÕE$ ü)5¡ÒÑß«5{M¥	Ö`Ðu:ÖØé÷Lèô{ÇÎ	«ÉËl0túCgü-ü@Z
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ae/0424e9541395022e8bf91d9db0fec4316e1891

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ae/0424e9541395022e8bf91d9db0fec4316e1891 (latin-1)

```text
x­±jÃ0;ë)É`/ÎRÚÙ¸nqb#;º|"2g¹¥
y÷Ê¤`º:ß}ÿÿÝí­ÛóÛ»ûÿÀ¾{'0'mÇ¡5Ú;28DËóËf
Y¹}OÕ×FÌ~$²MºÎ!ÛIo¨ËÌrxò²J9CtÍ©¢®
Ñ,@L¦EÌ8÷èap#é`£úWR<§M/Ïß»
Q7×¦QpW$°xðþ
2¼¯»Ú£ÉeÁ+$ÓwHÊòÈªÖñéSÆ»4%sìþ¦:ÁõÔ¯Æì³
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ae/146b9329a3344652b61d851577c5169481121b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ae/146b9329a3344652b61d851577c5169481121b (latin-1)

```text
xÅRÛnÓ@äÙ_qHäÐ¨NZ*!R@%ÙFn'¼¬{ã®âxÍz)¥ù>ã°,ímvÎ]¤j½óWÝg'2Ò2pu¿^9©y,erv÷Î:8ùÝV;±ØÈH<}¤åFèÂIr©¤*Id88Ò¹åù#~ëgãS6r?lj7Õ;0ðÇ7î¾ýÈ	é±9óÚ}ËrðØdfÎà?éõ.@ÕäÒ:ÅRfP|âO |ìwýy6	ì¶ÃÜ1¢ w	ôaÔòP´UøRÊBh,a´"^Ë*LhdÊ
Ñed 6^æJºQ2¦!.3ilÚkÃWªÞÂÍÝã(qÄ{/:%\ý¼&æ²àZñÖ¦í=
¡È 6Ú­ÑÄõkâL¨Ð-¤"}ZRgõzW 7x.3­,eRjQÑwjûÜqû³`2øõ pçì'csµæ÷KÝv¬ÔZ|ÿ¢5E*0VuQÒëoì%ñ½1OidÊ{·âXe6F.R­xÞ.ñ	¼æké -/Îq4Üòu±7¨²°2ûáþÁKÒV]#+äÒøêþÎÝ%bmîöq¸ªõâôôt¯¢9ffï Âv
ÛM¿â=Æ4ÏàO»GnSª¥R|Þ¡{­ÿÓÍcýU"á=ôà
P¯;ëu½yä
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/37/167793906508c801fdd950996ea3920a7bd3c1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/37/167793906508c801fdd950996ea3920a7bd3c1 (latin-1)

```text
xisÚF´ùgê±j°s4C;ØÈc	ÆI]îidèpp2þ1þü±¾·.íj<^¡÷öÝ×îÔ¦äåóß^ÿÔxF;iÈÆoXHC>_ÄûùÀ¯èÇ¿øõÊã3îØ®MVvhîÇ¯iLü\IÄÈ³Fí)÷/qyû­·aÃe7Üaûß+@!rÈ¸û¼°d¡Ï¼Ê=^0sÞµ¿^6ï®:Ú-¸»ùQä:¸aT(¨RÔÈ
´è+ERë
ÎèûAç²gÑ¡uÖ½YC£ÂÆ&AÄõÉêÑnÿ´~T«3.ÛÃ¶C³F±s8Å$ÃÄS¨¤î"-Ò±>uO,ÚÑ3kdÀÒt¬^ûØê	ÞÍº¢?â« Ý0?ë\6ã>#Ö§=·®ía4×ÍÚÓäýàòÂ"ð äPzÌf,g¢&*8¦ÉLÚd|ðjr¤ A!¡ z³ eësbæRùy4ÀÊ.ÂB-¹"ô{
%Ö"IX|»bGò»Ï_á ¢#7á|ôæ0ø*wÉÏÀ	¼jÀ*dQÄÜxGì6ûYÉNYÏ]gxÈPÎmÏ}0ð<z/°DðÛõRÅö4ãÀ§3ÏG`2ù3ÊØßÉ$îjð¾8å^Î
Q>0)ÄuD?^Z½èþ¹Ð={7"ÏkçôýÅÙGÚ±N»}KfôÌu4ÿ"]gBÑùÆ±ÕµuSÞ6&y¡ã}2Û×ÚÎe<§£wC«Ý¡£öÉyA£ù4Ê?%ÆÆ5ùN];¶å.0ÌMÀ]YPU°	|	6ðmù2Õ/N½ö]äVme¶}tú×÷1ê¹Ðg¢ñæ,6vsy·è®È$çôt0ïÑBHYÄ!pöì(y
¥>_$Þ¤Û`«!´Ä³c¦/à!®dÙ°ieÞäº¬RüA 00òÌl/bz %rÔÏÂaS<UJÔ·
Ê]À(C²RÑ(öÝõ6qüö~¸ÎäGa=ÀKerAÞ¬õÞN¼¸hlS}cÇ-Ãeô£s¸¼!?7×;¦2B.p*Í®½p'º«ÝRrb{ÞóS4¿¬dÉäLU$U6Bh:`	EFêÒåÛò´gô²¬cd¨Å¼q<ã³ f"Û5ñ]Ç$o¿f>!ø¥fÝìî<·u»GGåAþûj@øL>ôÞ*]Ã´¥ÖËdSÈ¸ ÏÞÞú«R9Üù«øýk
ÆÎ±lè0ö3ò@c±í»ÁN9n6[8RÒÏ¶®á¸þOK´Zä°¬µ¶YÇ k«PÊøÈ¶R´WG4dÜnOÆ8LÆP&c(>±*1ð"~%×Ô_HOYt(¢ª<Z×r¸ëÉØ½e]¸Ò/NÀÑØ¶£ä}ÕOÍ8	Â\qóãO$rs­R9¦IÉïH¤ar|Ó´õZidó4\¯1Yä[º
\A2ó­$S«ÂÍe'¤A¹uSYô#`G°¼­ %íí :fÈß-!£Tó0Bõ+ø	UM7BÉüQa à>©âºùDëºZ²%Ý
)î¨×úÎfÓÑjqÌGSÔ
)¼¿&¬×
ÍÄÁ@Ãõº-b
£ÀßInÆß¡à«ùá*B[_aÏ#JØ£ÃR  l$²SÀ~~/¶òJ¼(íÈ)É&ëÓºfn/TB=Ý ¤ð´DbÀ@=³Üv¥ôè#÷VnÞ®£Ü¬ç¢ÊÍeuÔ³°y]¹ùeÉVåÍªÎ¢Î®x¢UÚ¥ÁpÊ
ËÕ\¾J3÷ôs»;*Õ\?$Å¶Lí[È S90ú#.YìÍ^ø}(=só\6´¯(^ê#ÍP±'òªr¸iëV]à¥FaÈIgüý aW~<S%¡/Ý£¿PG
4ý(89¦<ÅèqÓ$ýË^Où#¥®)óí©ÇrG>!R:mü³O:¶J§U<GN%ÛÜÞzuá«LÏC¥Rÿ¼5IOYT
4ô\W;|ÑÇ0Np¸
|ë«ã3ÞúT Óè6Ú*D;ÊÒÁØDÁÅÕHÓ)W.1Sò&iøÐë´GÝAß$'þi÷æ¾	ôÃ°;vGWÀç?X¹!
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/37/f9f691852551c47563ed78f8076d2f7fb5e51c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/37/f9f691852551c47563ed78f8076d2f7fb5e51c (latin-1)

```text
xÁ
Â0 yg
/Pä$Æ!BLÀ§[R¦ûÓøt§j)KÎÞÌ@³¤$ÄrbAÁGI(9bogó>¸¯4ût0Ê:2MIQ)Û)îbÇðÌÐlýU<êÖà.Åà²Ú\u)õ6YÞÇ©+øÄ>EOaÀèvºÿuûßtÝÖn°àm:¨Ûì~æGJ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/37/4b2d5693a75556961f6f71e6035303909f0c95

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/37/4b2d5693a75556961f6f71e6035303909f0c95 (latin-1)

```text
xUÛnÚ@í³¿b(YÁ$ªRõÉZPÀ¤JUieÖK²Â±ÝõVù~K¬³ëKÐJõ¶wgÏ93³Ìlíó³³û<¥É2fðîËoW¢µ`"eÉÉíñl+f÷²Ý[ß3Q´nrý3`	¹3§\m ´Z2Êâ÷/Á3È#ÁäzBü¡ÖsVÅªhå§rQ§ërÉ0öc6ç)×%Ã ëA7$îÀw'fÂbÇ2
INfi!¡bI%($¤È÷p9ò©×!^hÖx¶.¬·ÆN¨Ò38Vº¦ë]ùO)¼)J÷70Uc­áTd¤`w vIÉH½á·ú$ü8öÜ.n§Oº^ÏzJAAtaÃ«ö)bUê(y+X+M¤|ÔwñryðtQmzõ8²¡|ÕÔ2~×÷[00ÛïjM&2Z0óp¶
}ÒÆÞ7Fj*T]Úì§(JóÉÙÐ^@À±ÜìO¯c¶mSý·|§Ê4Âh¯«÷Zâ²`BSK]b½&(º¥¾]I×xs>ÏrÖÔT	pÖ});ÒÜºã¶8LüèÎÃsú`}M÷lÀlº)ÝÞòs]â¶
Y5Qºµ>óe)ðBó]©9É3!­]T±É¡ò&Í$âR\#'\´¬æ£ö¥©':<ç7KÁªª§(£ióìvBÿÊC0·rw'3mâÿPÓß([S³ÝNÙs:L×oFI2Ãq"M7¨.Õ£j#Iq&ÓÁ ²¤É¥Ñ,a:¸ÖX¡h¥Äzn
¢­'³à­ø_¼ ÷4â­¹ÖcPßâúô6~wæÛôñ@"]?DÆ88õù­_ÊmOÝç
¦Õ7!ÚæÊ²MÀÑ¨Íi¾_CÚàF¿ã~0´¡{þ%Y[Ód4ö±^ãþ $	
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b2/3828b24a79987f095b85b88542c856ce94c8b4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b2/3828b24a79987f095b85b88542c856ce94c8b4 (latin-1)

```text
x}RMoÂ0Ý¹¿"cT&6ÄmC¡Ch¥L|vJk "¤(I+`Ú_ÜiÐnQ4yö³ýì%Kä¥Õº¹yÈÒÈë	ö£hnAp`O®UX²^Ç|ÝÔç¾Û6!®è.àÁÄ°lîT{+{ ¥åt4îÏ=NÜÁp:s'¶±1öâÐ ½±ÿ6ÐÏÑ;EsÏ]¸^½mY1W$
d 7äg°R¶EôÒè3U$:4.®Ç«EÂ­|,Óh*piad©l±s]yv¨Í9í¶¦NÄlêä+ÏÃR446%]´uF:$)J°­¹Ú¦¤±o!;3cÑT*8A©Üþ\F¹ãx®qù¶rO±ïìÚB3òlK¡´xûDGÜ©ò³lø^è¢kFZÌd]­¾9æ<\Ü
¬ B}Ñ½²³ÿpVF¸âüO-M>a8~i
)¥¢QÑq2ºNçÎ´7~Ìcÿj¹W6U3ü o335
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/17/a453eba9399cd6fea7ca2479247df71a4ee232

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/17/a453eba9399cd6fea7ca2479247df71a4ee232 (latin-1)

```text
x+)JMU054g040031QpöMÌNõÉ,.)Ö+©(aø-~2G¤gnDúÝ#ß?Û~®ªÌIMOIM*M×Kf¸òÁÖjÅ·fDjn²9h½U/úTYn~iqj|qANfI|jYj^	P¹Hðßö´çï¯TNv»gîF¨rB¦d ê¢Ä <þ|Ö.ïÉ//¿u¸ùâ±ÊÞhùÈSÊ2SÊsî±]~ úoÉT¶£f¤1*@m(M,*ÏÍ/K §å¤¦ÜTó­ÍäÖªS}sÕþÎ<tU}Ï:2Ó3@Z¾ª<²p`µü¡6hMÚãæuà²¢ÔäÔÌ²Ô"bÿNlðYÕºòõÏýíVþü³	«zùËÓWÌörEB§h¢¼öÊ?¯5g$gÀgõÍ\\ù­}BPcÉó?3g¤DNÇ¢fx¹Æç¡Ëv®°zý®êÎ¹.+¶ ¿9Út
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/17/938c5ac9285e0bd08d535419a1a8779e39123e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/17/938c5ac9285e0bd08d535419a1a8779e39123e (latin-1)

```text
x+)JMU022a040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ SÊpp²ºX­Ïì´>É;ßôþ QQ\ÌpùëBÖk¦½§=&qÍ)c
µ­<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 ÷`
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/c5/02783c5513530c656ef71701617d981da70010

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/c5/02783c5513530c656ef71701617d981da70010 (latin-1)

```text
xOkSAÅ]Ï§8.ZhqWÓVBMgtó¸¹¼¼çOÐ~q!ºÍGx_Ìû	êªYÌ{Ï9¿7:Ç³§ÏP±×5·ºÝwEdj$ero[õÝ/l"{IÀðÝ.ÈR1ô  ^´¥6®(smB-Ç¡?E%mQÄK¤ÎÝpûPÖXh\!ôvM»]ÅÇéµs3EârØÝ)8Hf§´â×.
ó
E´¾)m5P§2b)²Æ¯ÇGw6[ßÌ®&¯îG)úç¦Ôæ¹yïsìµ]È2áÐî­âv½:Û¿Ì©ÛÌ¡ÿç°Efd¥[¾:7à}÷
»¦^HÉD?ÙªmûÃ!)©E`²¯q lò¿Xö¾1³_øÙ#jãèn<=¿¾¬ÇïªêrvS¿ÌÎ«õÅ¤ºK½ïY?ú
c¿ã
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/2e/a2c14caa9f544ce6cb41944dbc3eeb2681e451

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/2e/a2c14caa9f544ce6cb41944dbc3eeb2681e451 (latin-1)

```text
xUYnÛ0í·N1H~¤Ô¨R¤(ÛJ D^à%è¥±M&ÊVä4ýèz\¬Cy8+°Dræ½y3
5Ããoö¹LE!|ºÇ|r§«SÔÅ»ÉgïÙPã1ã*ý»ýõ³i¯QZ6Kd2FýÄ~¹mª¥Q_<+Ã-WXdé$cÌ£GPo·Î£ö­yÉz8êoâB`¹àå¨y>AÒ_aÖî£ÌøÈóâök¶8dÝð"êõÃ®á°³¡ÀÊ:;WazbÃ%Bó¬ß¾°z;îÁáÑjÙ¼¿6Ï:¬ÓîEý¨Ýòµº©@ªD ¾{ààë·à»ÍÀóªUh`*<þ~ü¥ÀÏµ²,ÏUà]+AhËÌ
·é>+Kæãõ.í	³P¢-?ÈqJ	È5ã" óBÎâhÈ	P^»÷bu4<W
BLuÌØï^Ä	à§ôl¡¸LD¬.08¥ÓÄ¦ãQñ]ÚOÙÌÄÜ?zOtwö8J)]Çv£·o%He@1§¡:Hcá~6/P6pâ+yçU*pV«÷ó->?1ÌY®Þ'ëe^\$ÌÝ²{È¹ZÔ:÷÷à{-¡Ö? W6
Re,f{Ô< RØ°¿¹¶9rqÜn%ÒY4)M
&ÝØ+½¹á±cîÀpÕø%ÇÂl'7×«y½.Øðu°Ju#ö.ÇUQæÐh-ÁMð~a«ÏjöÔU¦Ô[UX­n,JÔ:U¥ÔÆGõØ
¨ÖúZH¶ò\Å$rLj½z7ê#h5ÙVfO¥JVDjGÃÍ"#;#oÔ%ÇgõXØ:£´5ü§· ë¶i~×)³Ý³8ø æbLé{~KÌ3±¸'þ0Y>
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/58/86fc83434590f9e73c7fa24e2a7cba9ab462f3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/58/86fc83434590f9e73c7fa24e2a7cba9ab462f3 (latin-1)

```text
x+)JMU0´4`040031QHÎ/ÊKÕKÎÏKcXË¾o­Ç÷o¿mJ
üôæTªìÔÊÜÄW>zÓßW$ìX®õýâ¡çK×9!«ÏIM+ÑË/K-ÊI¬d¸}âÿÆgù©5¶¼L×{¾Ö&V·ö31 â¢d¾s;qkô¦±öÆæÌ?P³ÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  K©Rµ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/58/e63f413af6397d6603c9d004146deac9adc020

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/58/e63f413af6397d6603c9d004146deac9adc020 (latin-1)

```text
x+)JMU0´4a040031Q(M,*ÏÍ/K¥Å©ñ9©i%zÉ_?øX>ºÞleónvíi9á|8te¦g´´uíÐü^¯ÝµfËöw[/?*°CÖR\Y³`g·Û³9Oê­o/;:yÂSÕ,ªaWùl1çÛÍÓQ;ïu~å=PxCñ8 ¯÷T
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e3/ea0efc67ad6f53afe901f1f1d69752a2ce96fb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e3/ea0efc67ad6f53afe901f1f1d69752a2ce96fb (latin-1)

```text
x+)JMU07g040031QÈMÌÌÓKfâ-·;r·ÁcëB¥7W­¶f@U&Ä¥&§f¥ûu·ïYq+÷#Á­%Kï&¶d[ Ï!Å
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e3/381e5b5907f693b36a99dd9e7cfba3adda07b6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e3/381e5b5907f693b36a99dd9e7cfba3adda07b6 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÔ2=Äï7Owÿµb5»aÞñÇSi~YjQNb%C××cµS8>Ù¢{¯ÁáÐ2¿÷sS6 ¨.ÊLÏü½*ã¿GçûÞ	³JW,i±]}'µ0£ÿ°_0rÈN[Åóÿò¥¢MÉO& Bf^rNiJ*Ãûµç÷´ÌyóocÛÉãa»NùÊzBT%3pßôpr6ïß
/ÜÍåz}k»¡Ö§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  ã®X
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/09/0cbfd02e40e9874b11b8864dc7119f219a8219

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/09/0cbfd02e40e9874b11b8864dc7119f219a8219 (latin-1)

```text
xANÄ0 9çþ ÈqÓ¸V>ÀÁ£ë¸»õ*þ~ëhFõZ·4O½A\´ÌÃÄ#Zh æ	EZHi%Ã9³»4»u@ãuZR.s4,'ê"EP8¯4+E²÷7øñ½ÁTÓÃÎ^¶êoç*ÛõE½¾Bä1È9exÆ1ôøëöÿ2èÅô÷±W¸9ÜwW¿:|¿~?ilJ²
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/11/004d6bcd7454e2c03dcffb3bef6f25ace5bc4d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/11/004d6bcd7454e2c03dcffb3bef6f25ace5bc4d (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÚy/³¾·¯úhYOS°×,û`©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨ÉïZLYxéàÉû³ß¥HOPâ:ZÑî+8Ø}NöÌúðê
÷Ù7> Bf^rNiJ*ÃN¡Ça·æ
}¯~º¸âµóQMN{ *:ùRÅµ.:ºò$·]À^üPëÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  4ÿi
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/11/348c8c502520126e26deab13e14bf5a76f9c13

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/11/348c8c502520126e26deab13e14bf5a76f9c13 (latin-1)

```text
x+)JMU066f040031QpöMÌNõÉ,.)Ö+©(aøåªÒz/W1;ÀéÃïÈ¿-} *KJâsóËRDiqj|NjZ^2CO÷ïæK¶_ÿ-=úÊ3j>Eé -¦=zõnf\Áz©=¯¨6­>:KYKQjrjfYjÌ
µ:fï87Ëäë6øßõéÖyXÕÃ,0+<!ããß3óOâª¾|YCqyfIrÌx1VßÌÅßÚ'5<ÿ3£qFJät,ªak|î9ºlç
«×ïªî{à²b+ ¢çÛ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f7/7a68c60f4889ef8db1609a75a8a48598b727b9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f7/7a68c60f4889ef8db1609a75a8a48598b727b9 (latin-1)

```text
xRÍÓ0æÜ§m/p[  ^rHìI°ØÖÄ©´{±RÈ©H»l%N<B_qÆY*ÄÕóÍ÷çÙí¬×_-¡:èúv·ïÂè\þ¾ÚxkvJÉ÷Åb	¶}l¡§üÃ»õê^7)9ãOháÐ=>ðyx Y¥o<²ÔH*-yz	ki¨±ÎKR[ÔW ^¯MI¿û©m©cgOOëjG,Ö_Ï³8ö-ÙOÈÈ:y}¼3²zr_;Cè	3cww}a	Âàk.Ìq37u633fùo-bwII²¾5§ZÃ¸2M¼f±¹õ¥Ð©<¶ã%n@ÎM4&B
êåã·dd#\rÃÀ@`àM8KÈ¬´rüÿê>tqi§4á &øØççâ|k#?°Ã<mJçKÜb¼[×ÃÀVÒ¹y	¬Ä@Å7r®X2ZúPÓ,ï?Ï4ýöõÐÂ Çß_÷ç£ï¿Ýþ/åSïùÂ)Ä;§àãÏYçÍ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f7/c6aa6e0c8d29ab9294d20f5eae4e1e56e6aa2c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f7/c6aa6e0c8d29ab9294d20f5eae4e1e56e6aa2c (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLgX¾Sÿúïý¾5¬ÜWîzYä×wªÔÊ"µ»>m°e¢îÊì®gwµ<8ísV"
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f7/ed8236307229abacc2448655e4eeb7a183e7d6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f7/ed8236307229abacc2448655e4eeb7a183e7d6 (latin-1)

```text
xUÛjÛ@í³¾bH^äÔÔMB!Å¥ÛJõ
Ë½PYÛ×»bw[É×ô¡ÐOÈuV²ss\!´»3sæÌÑX¨1|³Ïe"òáÓ-f³]£(ÞÍ>{O¶N¹Öèéö7,æ5¼DiÙ"ñõ#{ÚÎcm¹â61ûôDáÀÔJ£4+¾^<)Ã-W[dÉ,SL_BEN3Á-ËPól:]n¶{ç¬ÓkÚça4~ã|ÊÆ«ÐìuÏÂsö½ó¹íà"hWêÑâKÎép~eÍ^;Ã£õ²3ø|ëöY¿Ã°×õµºªB¢D|÷^ÖoÁwÏ«Õ u|ÿçþ·?ÓÊÞÿµ<S·y©x
Ô¾È£Äqìç\Úf¡·ú ×U+% ÓhË<å²ç×\ðXCFQå¥{Ï1XÄsó¤L¥JÙo^S_Ðõ2ÂU°:ÇJ¾Fåua>g#3ÿè=¡ÝÕá$¦ðH#%ì³Îî¼UFDR,¢Ô¡:Hcáv1/Ë¹´
kªpX©×j·å:æÌ6åìéÅ3ænÙ]Ù©,ìù{ð£Ñ 4Fç?!*Úö©(Ó½%-w3l¾Q¶9ry\émÒ_¶ -ËÜØ+¹
á±CìpÝîÆÜlWJÕå¼Y.Øøõ`#9êJ.CØ×E)5¡ÑæZÁÝAwÈ£¶îªM³iÁ-Ê­V7%jCMªêXãÂ#µzÅ rÓ©»9z­>0IÃD£FÔýbþ¬ÇÚÚì±TÉ@íhø¼Èþ#ðöéLÃ³OÊ#tO¶¿1£~;²Aw¶ù¸c¥ú=ý7LìÓ¨ãïZî
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1a/922a82d93b3b9c7480d4ab11958d89a17672b7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1a/922a82d93b3b9c7480d4ab11958d89a17672b7 (latin-1)

```text
xS]oÚ0Ýs~Å}hÒ¡ÒvÓTi£i
A;m{LrxuljÇôcÚ¯ÙÃ¤½î'ðÇvm>
c89¶ï9ç;j¯Þ¾Øá26Cx÷âA7nPKûÅû`*Ï¹Ìôÿ^Þ4p²JJ&Yz¾ÁM¶ß±`S®þqÂ2]%æWihFZHg¿3+ Þ(é¸[PTehx×Ë¤TÖ`b*VaLæíµ èöÏ^ÿäª''q»ÛÆ!m¯C»qÚ9K¾ôÎ·¥»Q3v2¼æ¡×ºv>%í~wG«×nÿyü¹×$þ¨sÙé_ZÝÕ!U"Ð­#ØÛ8ýBFA@ªN­ýýPÀì=i0Í¼:ZÛA©`ÂS*2KHvh¹¬
|Áå/ü- ú¬[ixi3Ã{ºâXJ[´Ø4ãF NÂ£·%#zÖ¸_"© Pªcªd)jX²ýïâ×L_*Q 3¸]>ø¾iÕºC`SbSS¼¶mSÒIª(as_¨Xë«520eBl¥+{b©Ò¢F>{ó${v«ÔáõÜ]½ë!ºz=^ |w!¢Ë©¬$«ÈMrXi¶?FÞ2AïßÂ39(¤J,®Z¦0lI:¦¤Ij»h>¨ìa±îÃ­åªtö&4EòSx~L,YMç»ëqÒÙY.¼Çr"TýIÁBÝéGG9SOnv§éÕÇPjðR/ ;6©æ+øí.ãxú}Ä)Ùë.4ÎnïèêÃ¨=ìü¬®ïÎn¢¯l¥ÕÒ×?úr"F¡?.#Î
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/1a/c9314efdd92f248b3197eafee06ccb403e348a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/1a/c9314efdd92f248b3197eafee06ccb403e348a (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgðW|éw¶ìpÕû;?øÿ·ºÜl3DAUjAFeÃÚ]¶NØ2Q÷JevC×³Â;ÊZ l:V
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7c/13ccc5b65ead792347f90cd65dd4be4295cdc9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7c/13ccc5b65ead792347f90cd65dd4be4295cdc9 (latin-1)

```text
x5ÈÏ
@@qç})JþÜyí2!kV»3ÂÓsàòõë3Ö¨Ê*w¯§M£U¼Ð`eDhoÜçË+zBÏR1öÜoN¾=0y_Ý3g?¯ä³fG!mÔ%ë
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7c/f1068634daaaca8e9d26fd9851c2d527bcac4f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7c/f1068634daaaca8e9d26fd9851c2d527bcac4f (latin-1)

```text
xOO0=÷S¼fæðæ¹%û9£/
¬Èº²¿»oì 8å@~Oûö}h(TýÛËD®EÎ8ÜxÚÝp-¹èÅ#Ò¢DF.?òíÆÖüÈ%KU"MÖò@ºU;¯<ãTðc)â/çt±­|Î¼©?~ñÃvÓéòéþaNßÔ"¾÷æù!¸=´mæ`Ð§Ø¾Kà·§f¿l­ôÿä¹ºyU8ÌQ2ëÀ')éºðÌ£ h*m Â`
°ñÉÎ×Ð	Eç½¾ªÆá)¸µl#Ç*³6°ÒØäHje~Ä¯G¡bEÑ=Ñä -*lT´DUsW³ÑÚ+bõôgRqxºOî Ò@ÛfbpV¯wâ{±Dsk­·Óµ¤NÛý ki
ÈùRúþ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/7c/eadd5f6bf1e4f298aa7b7d98ddc86b1c060a5d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/7c/eadd5f6bf1e4f298aa7b7d98ddc86b1c060a5d (latin-1)

```text
xTÛnÓ@åÙ_1m_ìê4H¨Ò Ym(ÐjkO°õn»»N"øøþ³vº7}HìsÎìõ¹Pçpø²óæÙ^.Q¦o¯ñ"[épZ¢8È¼F¨¸@iYÁ%ÿú°	
J£4«ÀAY>Ü,¹¶Ì\å6ÉÀ}Q¨²B·(/aµVvwh}L¢Q¿wv<x xzóÜk4G§½ãÃízÞ^³\"{ÓIôõG§1v¶Û_'ìdðeØ³ñ(¦ÑèÌ×êªøî9ý;ìçà»`àyÆr'°Py
TÍqå¹´¯JeóR©ýôV³
&/JÁmmt·Vt	L¾ÇÉäº¢ÏYaâßiÝÿqa*E°ýò¶Èd\¦Y³Ñd\×Å¼n<ÙÜÇ,ÚY4tø¤Æ4©tsïæADº^å&¿SA7²®hm©%´kÇng[ïN:A7<Ü¶[ðÊEWkõº7éÎQ%yqOº,åk?XpQ¢û=¬­Û®þÒY *÷3^p0%Y)oþÞüQËÜXª_
erÀ¢CÜöö^Ì¯"Îeºl¹?Z0E#TÂJ  S:¿VÒrq^=^ ¦1n@©hëEº&ÑJ¶_:¥á©º(/KNÉê:Âc¼e×n2¸£ÖÒ`o¨È/K45t3·ý§»;{ÅÓÁÙ`â¯?UeQ·Zqøãû¸?ÆÕ¿O»?Äù1 §M
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/63/f5f04c39e2d7833a3cee9b783dcb1e13c80e78

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/63/f5f04c39e2d7833a3cee9b783dcb1e13c80e78 (latin-1)

```text
xmÝ
Â0½îSv£0,¢ >IéÚ¸µÍèl{Å³²!^,sÎRªàp<mÞËÚJ §­S&ië}3zÞ¡whöÍí?²oZý5çp¯ÉK¤)@nÁ]Ì*¼_­gY^¤ÂÒóH·sz(
ôX2X©Ê1büñ1¬_M¶?*ÅHN<¬0Ë°»°¶3U
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/63/80afd226ac3ea3c11675ade5cbfe4fd03f5d16

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/63/80afd226ac3ea3c11675ade5cbfe4fd03f5d16 (latin-1)

```text
x­W[oÓHÞçüHE$Ê.e+¹Ódk'Æv
ËKä8Ck5±-Û-´ÿ}ÏeÆ±ÓK¨ ª:s.óË93^¬Òx}ðöÍç-ñ\ôÓì&Ï/Jñ,ÚûÝý®.¤øì()óxqU¦yª¨í»OG2)¤1^Ê¤¿Ä2'q òN«õt)¿Ä	ÌÝéx''ó54gv0w¦gÖüÌ´Eo¿Û¢ÓÝîÃKü¾gÓý7Vôº`$N¢ÕÕR÷q],O#YàçËeYÄG5ï2»¸É;ËÒXÄÉ2NÎ¯¡ÿ¼(]ÊâåE}ÝB^×ñ]u¨ïëËÎ¢l®Ü_Ê-ìmôª(v(eiÙNÎ6/P¡Õj¯××sq¾R&2?½Iø[¼o³ù·y+PÚ½£Cñß!BÑ# (OW«»aÄì£H°ÓÄß²4ì£h~P]R-ãµ4ÊÔXß"ri¬Ô|Óíj]¬WP?¸p)WáRÙ(0&ÿ'dk}­üyÐÈNÙO8<ç272Ç©v²wptØB[­X"½ªit*sÿBqñ®NÔTP-J×¤l±'Pr/4Q±H>9$+¨¿U¸+ÔvMÏ#Ëû[*OÕy0`KVZÈ[DL{û2¶5æ5À£Ì÷Æ'£¦`I`Xäat)Ëwzò£<öÌþ©ürÞñi £²ÍgîØµöjIÙ
Fr(ò7bý0¼¾c¸Ö&îô¦uíÕÀ/µÐãÃ«U93m¥ÚbÞêzÝ´°p,¿~àá#-@¾Ç*ö¿Fë5GäOõÄ%	²}·O¦m4Pä<ø<*Ý!3NÁÿP}¤i$þaSÍÃù¶ø~!å±í~à2?óðÊñÏq\ÃEõ¦pÔ¢©ã@üCþ`ªú68,Ïpß÷ë<'5Á`v¨ÍlØñb¿R æ:=RÀÙ>¬áUmÒ¯Lpð]³o=ömÓÆHôª(^Ú@¿ª0AÁEÜÎGu.ôqÆ~ùÏÖu`bþ¸ÅØædæ[Þü¯õ'y	)éÛjI ôw4uø4`L@»ðjÒe èÙ¦¾­	×/A´k÷/¶¡µÚe&ÂÝòðÕGø°"Æâ%ORxMz½á% òL?ÜP´ÀP½ñ0ÿÃBñ r*ªA«-VRxH²]CivmC«ü)©rMÑAØEEig<ù÷W=)ÞÊR#k·¤ÊTYih« Ôï5zG¹æa\È-W¸Ñ b÷Àª]£JmÅ15RjØ_×©~êzý	i}êS_åHÙe[µ·)IDÞe]Ëë^Lh³	ÖL¸4h:2}Õ ¶­§î|0>T;ñÌ3ë×°>Ìàó¬®r#Æ`=óÙGÌðfªuLÇÝQO:`]8&3ÊgÕ§)!¾$wÖÌ2.2|F'áÃÉÖS¤y³«¶²{à|±óA^Ði>©f=ØV5
­:ÑmS
áµ¡6t85ëa·¨ùøxlÕnx±¡ÿt³Ñ¬¬:6Z½õ«kTú¶·}þ«3/èLcç2ºs´ã3X­±EÁ  /pÝö5­Û¾¦¹íkJ·ýÕáÓ6ªq
Yuú6¿®ÚHy
ÊÞP¿v
iÀÜ¯3W×BvåhôçgS.aÜk¦(L¢Y@÷5ÊèÃÈô¼©zÖ>æâiº4Ü{µkwî× ª¦æöjºaÊ¬AWßÕ¯õ |'±"Ìàï­¡í
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a3/dfa603db7f99ffda6cc69804165a9eaa05f9d7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a3/dfa603db7f99ffda6cc69804165a9eaa05f9d7 (latin-1)

```text
x+)JMU022a040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ SÊpp²ºX­Ïì´>É;ßôþ QQ\ÌPþïmügYßØþ|³úÆa¨må©Å%z¹9Ç4¯y#_íYÙÁµ_?ó1  Äc8
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/79/6ae00868f698b90c3ff5a111a54e810c9467cc

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/79/6ae00868f698b90c3ff5a111a54e810c9467cc (latin-1)

```text
xK
Â0 ]çï|L_
"+7î\¸LÓhú Mïo®àv`f(§N­Á­¥pÚZ\â2bÀ¢¦£6^Ë9ÂíË>|TxùBpÝ)ñßSñy(´Æõødà,¢Óþkô¿)[nÙ¯ðÞ»ýà-æ4B=:º
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/79/5735cc9b90e32911ccbc5064dcc2cb03529115

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/79/5735cc9b90e32911ccbc5064dcc2cb03529115 (latin-1)

```text
x½ßOÛ0Ç÷Ì_qÊC5P²$@ntP	m¨+ÓÞ"'9¨[¶ÿãPñ<?´öùë»ÏýH)d	yv(ÞVVØì[Ó6+j¼e°'ïAB²;-;dTðý×ògqýg~õùæt¹*VÿbÈb8ÚÅ>IÇkG¾ìåÇû³éVþÒoÝßÒD5 úÃç?R>B>&J>¢N°e¥Àð)¯q`5ÙÉ{öõoªNklmbbMÍóÃ¯Y
dtÓ;¶£ÈG
_ û5èc~G1D^ç84
k¶h%Å,w)÷â2!E'EóT8Ë	¸"½¤;Òû)Ð.opq½ø]­çÅåââr64ÖHpÉJ¨ÝZr¹ív*È`%
Â¸1¨áj~>¢Ø&83.ßÍÖÃ£"Nz\7JjËZ fþ(4VÈP©à¶k+.[¦½a Ó¨ÖÒ`8Hý3ÑznîcÝµIköÀ¥¦p
5WkÔLÙÇT®íc{!AvVKþÈÿË¾S{.ÜG~{Àò¾oD6w&¸MÞÀ"ïÚ½ëc¼"
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9b/170d648a560dd54b3c4a010c7f8cfbaf0d04bb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9b/170d648a560dd54b3c4a010c7f8cfbaf0d04bb (latin-1)

```text
xm=Â0ó+]t±à BEÍäÇ âàÒöhKóQØÿ][;Xð¶÷};.&¦³ùbTVdJP£ $(t"}
tÕ@×6,ÁjÓ|ýTÂ4r%´ÈÀ¶8´>AÚ¨+ãpWÉy'Ò'¡iÙwi"u}¡qÉ¦a¬Ñ%ÖHÉN_ö¦ïÅÑhWDÈí¸çìÊN¾cÛÃæÌÆ_Dä
ñ^[m
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9b/8352a00ab1cd2426fe029920c6841edf286632

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9b/8352a00ab1cd2426fe029920c6841edf286632 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½Üy-Nût«aÏ!óWV/.ze¹AIÊO,J)f=¹M>]Èm±lµÕÜV³G¡¦$fæ¤èU&ææ0px®^_pû¹dìRË%®G¯BIÎÏKËLgXµ¯³¡8HÃm«}ã³ÿa;ÊoWBT¥dT1¬Ýõië-u¯Tf7t=+¼£¬åÁ	 6TÚ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/44/6abbe60cb8d30be0bd8054d37db71c04fa8213

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/44/6abbe60cb8d30be0bd8054d37db71c04fa8213 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg(çÑZôååæÝby_'4x2±ý2(¨J-È¨,bX»ëÓÖ	[&ê^©ÌnèzVxGYË æS«
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/3c/ef7b812868b485d9091ecba5fd8f71295bfa9b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/3c/ef7b812868b485d9091ecba5fd8f71295bfa9b (latin-1)

```text
x+)JMU05f040031Q¨ÊÍÏÍ/-N/.I,IOÎHÌKOMÑË``\8õgÉ£µºwÎw¾µÜ^|Ü¾Î 3
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/59/6733407dc946ddf151327757d9815dd8f4c39b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/59/6733407dc946ddf151327757d9815dd8f4c39b (latin-1)

```text
xKÊÉOR044aPVH,JTÈr35²01PÐu
qU8¼R!Q¡,µ¨øðâ|äü\_GM.g?7O÷ø`× OGÛJ¤%ÞÓ/Ä5((4 $Þ%È3ÌÕM¨5ØßÇÕ6 á4$Æ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/3d/a3461635640aad165b7addc3007b1d73021c44

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/3d/a3461635640aad165b7addc3007b1d73021c44 (latin-1)

```text
xÎAj!@Ñ¬= U¥]
!ä³Ï*ZÎHÆ6ôØäúé+dûáÁÏ£÷6- ¼Ì]ÕÒ¢´:¨a
L".¥hHbb· !Wâ`~d×íK$ ) â£Ê+HÕEsJ29æ}ìös»½JWûöÔÛ(­[öxÍ£¿[¿"l/3g=ÿ¦þ_*ßúõüm3ßm=¶ÜÆ&[æàIÏ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/3d/90bd1039fe5ce9b91ab484c09ff7e416bc6f71

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/3d/90bd1039fe5ce9b91ab484c09ff7e416bc6f71 (latin-1)

```text
xWënÚHÞß<Å©*EÐxVmÕ4]¹Ó¢¤éªØ±0ÂØÔ
­xÕþXi_#/¶çÌÅØ²«µªÏ9o¾sÉ(FðìÕ«?=¡d>7ßù|²¦<yðtò¶¶µåóðøî­X,xenî¡¨nÌ¦R%ßDêMXÀÇû$fÑ³Y%Òxíènín?µ$uSáI
Ig^ª·à	ùgpá|n;ì¢ÏÞ;ý:¾ÚçÚ~ç\×I¢ÙhÖHm_Ì£_ð0j}>!çs]9_Þuìî4ÍãÒÎÇÎmÏ|pçDêyÇ<&E1÷øüþ¯û?#ãg&ÂôKa/§fWigÐ,­óå{)÷£Pm³Åf±[pXOA1úQ#ßY½ºóSµ(Ô2$§5¨C´@9GßÔ)µ¼Ùð¢`÷Æ<æIÂýÍæ¦|µùÜiN#ä/7rdÐ,Ó²qn¥)r`sf
3ja}ZÃÛ¥
%ùU§óÙi÷Ù§[çÖa½Öo<;©]±½÷ØsÙj;0ÛYr÷ÕD|çÑ¸¾ú%º¥Ôçp»>Ì]¼Åyykö%ò0Zïè:öëõíó«È|ojÁqóôé<Ð~LYªtK.¨ßÌwSWp£å¶"ôû.Ú">i$Õåò×õcd~xÚI§((h.ëÛDêÇå¦dw<­L*t$a-¸b.ÞN#Mô¨Òu)ótCí¢vÏMÊ	ü:?N*¤A]1Ë7å²ÕKb$ª¬ }bXlc6<´­s~L`¯aì	/éÃ É¢yFÈi!î<&Yzv$%sÁ56ªzúKKG¡¿WåoB»­gÖÒµum-³éÜ
ÒPdIäY¦îjîzQÊÃÎ
¯¼Q}gÉÆªnX?5ì2©îÙ$ïp,Æ£lªK
&FÞB³H1z^e±ÌÂÁxð-m»(HÁ¢{©3~
X5x2ç¤£UÊ±	O¸A~Eªº6px8Äbm\%Tc'H2ø×Üÿ
¤Øq6õÛÂ²áà;sÃI¤íúQn¡ÂIÕk½?8Fëg¥ÎU$*­åu`ÛÃA-b8@¦Èçá@³¿&Ü&Ùl»DÖÀÄ°m]RôÿöÃ¿"²®ÿaU~Èóä÷Ý PpqÿG 
xñü¶Ëaå_KFe=®,ÍF¸ÜEY.OHÐE*Ýr·ÎJàWÊ©®ÑV}ß8KïqCÆ{Ç§øzSÒ?ËÕÃÃªj:l.~?ÀIÖÍS(ü¦Ñ¼Úî²GK#QnÞ%
rè1;æ_
] *%}»®°âðÞ>XýB«Ào
³ÆcÞòi,IÿgtÐêO*ðþM;ÁüÒrÏ3C¹ü¼"[ÈÀj?4`.JM@gX8¥6ýÎ.R9°?
u@g´y+ò5èé`=<´;ìW»Õ/Nò^þíç^¡¿mºÍñô'£?dädzÑäúSDv Å|9Nê¡JMUÙµDüyº²¼ß±g!Ú·Ô|âá Õ¾½¾Ö9?/ÝQÀAM`3ú1ÛaÊõPUµV=>VLz;jÌíYNèKÊÅÒÿ¥|¢Cô¼´ IóÜæÆ=¼R9s¼U²yYD^FáLÅö¾ôX«Ýê«`¶TZ`ßÜ\·Îí~«Ó¶à¼Ó¾l½g5yÝt[n«ÿ-ühe^
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/41/31d3548065ad2fbce53650e054e02853ade34e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/41/31d3548065ad2fbce53650e054e02853ade34e (latin-1)

```text
x+)JMU031e040031QpöMÌNõÉ,.)Ö+©(awqË·iË~·óª¸oÎaÈ­ªLIM*MOÊIO-KÍ+)ÏÑKføþ¶ÉÌ HsõC.m¡OÞm_Øüü.õE@õzú¬âóì´ãß=v¯ÕBÕçæ§Æç 
R[óên|öÇ'f¬ª®q÷D¶W,TmqANfI<DGQPíÙF7{gÜgOfkRL(½Ð}f.²ÚÚOëtÒ=o/³÷¶¦lß¶ÛMPsKRaÆ|wïïUµO,Ót·u}|Ç<ímøSL ·¦°>1Ü´²ª>`Ò*ÑûuÝ³ª,M,Y
uoNjZ	PGÍG¶6[«NõÍUû;#ðÐUõ=küqè(ÊLÏ iYcâ¤\£î`&Q~¹Ï;<evä k)JMNÍ,K-Z!öïÄU­+_ÏðÜ?Ùî`åÏï9°ªY¿<}ÅÌi/W$tz&Êki¯üóJYCqyfIrÜxVßÌÅßÚ'5<ÿ3£qFJät,ªak|î9ºlç
«×ïªî{à²b+  
ù
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/41/e87efea6e739a4519794f833272f3427dcf163

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/41/e87efea6e739a4519794f833272f3427dcf163 (latin-1)

```text
x+)JMU047d01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õN¤üÄ¢bÐÛäÓÜxËV[ÝÉm5»(yÔÐÀÀÌÄD!©43'E¯217Ãsõ¢øÛÏ%c\.áp8z¥bLr~^Zf:C#âOÛú<ÿ8û¼½òRë#W@T¥dT1¬Ýõië-u¯Tf7t=+¼£¬åÁ	 CöB¼
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/39/c594cc8168d25bb807df34e9781b40ad318825

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/39/c594cc8168d25bb807df34e9781b40ad318825 (latin-1)

```text
x}KoÓ@Ç9ûS©*9%4´E¥¤($¦G
¸¬6ö&YÅÞµÖëöÃpêâÂ5_? úwÿßNÆ¡ÃÁÑÃg;Rùaxw+âÙ©ÏQ"Ü8[®PO§RMëøþÇÍ1ï&âñöùXÌøBj³íI¹±,¹Ö±PL,E8½á)ë;zëxí^kä¹·Ñ¼íáàc÷}í1
éyW^¯zì8õ:tÄD*ÔòO$Tãë0U<Cr¸5òÂå¯©ô9¸m"¡	edÕÙ	¨~ërÔýÌÚÃÞú³múiH-?U }!Frb!
µt¾®Q¹u)öÌûÒo³óáE÷²;¬£À%»
{:¾ JTG*áVd¬ÜÝo¬iù5kBlD 
ßÀ§ù0¨û£s¤w!¦©ájùÀ Òrà>æ¢¸X'rù°ü-j±üÊ'edá¤	¯áît½¯ì=è¡[óF#·ÒU¥ &ka¥V
ÒÑÜ
2~ø®Ôraâ¸lIU°©QðÒë®Z½ë>C2
NuQêwP`ðµJ,$Ö¤¾\7V.-K¼o5½ÒhfÓÐ(/=
Ë2´e<ãÉàÖVãÐÂR*Á{^T,1ÑùÑ@CÙp¢S ·àÝ ºÍRÿ¦ ò.&×,ÿmËBåöËMÉ¬Dïo-ÍÚÚke$Ë£ÁÏYÓ7Ñq«yÐ}	 âÄõ6®¢[ ¨åó!Æb©ók'X§neãO»É&*h¬Ø#:\*¤¡m ]YOMzÒð*YTOÄðõUR-[ìfÁ_ÇÎ½ó"®
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d0/bc97dedc8e8c42f7e58f588f65cf971e4c1cbb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d0/bc97dedc8e8c42f7e58f588f65cf971e4c1cbb (latin-1)

```text
xÛn1¹Þ§µÝ-i
AH!Ý¢¨I%-n,gw5õÚ©éñ4\ qË#äÅoMÔt³c{þÿó?#©GpøòÕá³]¡2és·8)îMýBù¢xm¤×éÿ_õòºST\ñ1íò5Þ|²ý~
ýÇì­pYÁ$^9Úõ:XôÍ~çb¬d£¢Ýád:G».d=×¬ÔÞ"³;dYÁÕópXuzX·wrÙIÙIÚê4iLëkÐê¶?°/Ý3tÒi'iDÑnWB!tö'Öêupx´zÖ¥»Í>ë÷ívï<6ú¶	Äá9ýÝÏ!Å$ÈÚ©W³³¸¿Rpnxe}ÉÁa&y¦ZäCå¼Ç^(wÌT
?ªÆß" Ï:N+J/Àu%±ÎxL´Äô
Z[í$V"Nâ£*ÞxTÔy¾I£B[jVfh`)ö{_qi«æÔ`¹ÅíîÑ÷MPë|É§$fGmH-åLQ@ãæT¨Yó«·A[r©ÉuHÓ
J~ñL\Ó5UüæY®Ô­ðÔàõÎÞ«JtôzõxQ{Am"T3_B5HÞrI1Þ½'bP"È\µ4MQØ,°lD9StCá ù¨:ØÇbÃ©lö&4HÒSTú¸\ªr¹°{¸âUÀY.
÷µ¼Ãr"uíÑÁÂYM"h?r®nÞN£*tÞ(8h,
pLFé~ÁúÍ8¡UT
l{x§xNN¹^D,hÃÒáåûakÐîWº¶ü)ØUøI¼öÎè%p{ô'HMþ ­ÖÍ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ad/baf2b590b4912dd4796b808ae671dc232a4809

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ad/baf2b590b4912dd4796b808ae671dc232a4809 (latin-1)

```text
x+)JMU0¶`040031QÈÍO)ÍIÕ«ÌÍa9´9L¹GvRVÓ;Áz§9cì×H Wd
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ad/0757bead1c08bc47c9edf736b26551f2ecca78

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ad/0757bead1c08bc47c9edf736b26551f2ecca78 (latin-1)

```text
xu±NÃ0ó§f
¡ !k_*«N9N.V
ÒD*©ÏÃÄÀÄ#äÅ¸F	A>÷ßÿßíªfÁÃòÊ´<PèþnÜÂuÎEè> v|éÞxl bvãùÀuÉµËÐH¦ÂÓXéÛL,§Ö	#Lþ Ôiaíù7×º¼ÏJx¨<[9äè2Ëø¤~¸àñøwñ§FÛp±7@ ¸ð&ÎGeHK¹äIiÐWz=ÍAO2±\Y§°@ >L"=êö`¬ö4mÅ\eE10®<qþï"Ùës[Bîëé­ú9KÝ}¶ûj6ù¼AéÆõ>ÎFé<Íù¥=
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ed/bdce9aede868af92441e8c4f62997799921379

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ed/bdce9aede868af92441e8c4f62997799921379 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2Ó~3²µÙ|c¿ÇÔõó®?;î
unUjAFeÃÚ]¶NØ2Q÷JevC×³Â;ÊZ @uS
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ed/65631885fff1e321cf58e50cc9155ca06823b1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ed/65631885fff1e321cf58e50cc9155ca06823b1 (latin-1)

```text
x+)JMU022a040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ SÊuöÑÖµ?«Mó_^8çziG'DEqQ2Cì^¥Ë®¸ÂOóGlx`ö¨må©Å%z¹9Ç4¯y#_íYÙÁµ_?ó1  d 
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/bb/9e9c7af3e5ac32dfa5e7877a5845d00c3658b6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/bb/9e9c7af3e5ac32dfa5e7877a5845d00c3658b6 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^Ã½Îg¢GÔäT	5ë>57QÀT_ZXÉÐõõXíOg¶èÞkp8´ÌïýÜ
(ª2Ó3 &åóÚ'òÕÑêNÃæ³¹ÎínÃ¢fôöFQÙÒi«xþ_þ±T´)ùÉ PÈÌKÎ)MIeøäþOçÒd{ûx«íY>zÎô¾z×¢¢¸(aÒ¢£³ºã.Ç[kg5ë­[¶¿]j]yjq^enCÇ±&Í«gÞÈàW{Vvpí×Ï|f Ù¹
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/be/2c452822206b0f41c9e7006786ef3884dbd612

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/be/2c452822206b0f41c9e7006786ef3884dbd612 (latin-1)

```text
xTmOÛ0Þçü4tÝÚ6!ñ"Q¨¢Ðª-hÛ+ÄµÄí@ÚýýþØÎNZÊÛ¶(û¹çî;ße"/¡õ¹µõnMdqRp;ÌÇ3Õ Ê0ù4ÞóÒIo03,²èÕÇº¡1ÓR1~	þr³aúVxÌ¼2o Ry,ÆÊk4`

VWè¹£ÎÁþÙa!ÃÑÃ/ZØßÞi¿ÓÝ?ìYÜªç­q¼ÂéþhÐùÊzÝ!´6ÛßOOØIøít¿Ïú½agÔéùJÞÖ!I ¾]P{bý|{x61ÜHÁôàl3¿ÙbËüÇ±Ý{@Ï²
Z¤E2Ñß:U`°M`Ê»¯Pk!³H9ó	KuûÍ`û¿	¯¢D;F"ÊÄ¼JöÓ[¤$²Äv)eBWÕÈ£xÆ%¸¹AæRP&¥Ð*¶`üV;;°Ù
XÙæ¶GÔX³Óc,92>å¥lsÖ:TÖøti={«Zð)ìN÷ö õ% ßÍéÑQ¥KERð¡ÊÈOÚÚJ£?nÏÆn`e<A¦óDÐ%±]JÝiwé¤¼
¤L
ÇóXËCMK"ÕYAÅDxj9ifi^øDZ)®À_ÉçlSUúÛn/è
ÏF¬}ÞnwÃÒô·0ª¾¸Î¤Bp÷VÃ!{ø-AÛXÔ@CÂeæl³ç=ÜI5¾wÀÄaç¨RaÐ¹¥»ÛÖ&Z\G)P\i¤4|ÐñU1WUtåjÖÁÕ:Êz[î¥ê°nûfÏH/ìöÙaûØ_`âävõ+³>Ý}Ï¾«äL-}Û¨»³Ïæ_ë@AÙwîëo¥ lºá(<~5å6¡ª/ki¶­5·Nß
¨çf¶gç1Ùü
çX
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/be/17427e1360c92e0bef620bc015600f6ae95f30

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/be/17427e1360c92e0bef620bc015600f6ae95f30 (latin-1)

```text
x¥RMOÂ@õ¼¿b/%i¤M0&mÀB 8mv
e·în1bü5g~Bÿ»mb(F=ÐC3óÞyûæÃõµwvÎxd1MW/²¾¦Óäbu~´gú¨±Y×3"5VÏLG+ÛDõ:+IIO-a Ø&Kå4ß+h¢ËÇB¡­`1a]08¶^Wæ[cP:<íuFAwê4kµ*zÐRMSÇs¡á5cUCá4<ÏØÎøI%ø}Î¤Sâÿ×i¨Sâ¿uÞ§®)R"	(GÞOzí.îöú~Ðs
Ò,6xÍK·â[t!x«ÿ+Ì[xÖD~Æóü]	M8"à$1y0aJ"6ò}Ì©&yþ¹©!¥fÁê¾åªFRI^§Nè)]\¹8Þ¡¸¾åÄ®1°)6EÓÙûVl°z.´Çã¡ßiþ(pÁÄ²ïßáZÃã?øáÌ8ðQ# 
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/be/126247777696d2d0df40f4879b36f74a9a8881

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/be/126247777696d2d0df40f4879b36f74a9a8881 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÚy/³¾·¯úhYOS°×,û`©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨ÉïZLYxéàÉû³ß¥HOPâ:ZÑî+8Ø}NöÌúðê
÷Ù7> Bf^rNiJ*ÃN¡Ça·æ
}¯~º¸âµóQMN{ *fd:þÝ'y½pùìÈ}ýñ	µ®<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 yÞÅ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e2/f13142aa6a7ba5fca16c968b719d4108df4ab0

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e2/f13142aa6a7ba5fca16c968b719d4108df4ab0 (latin-1)

```text
x­ÁNã09û)F
äRÄeU((¢Ð*-{àb¥ñXrâ`;]XÄ#íiÃ©[5ì¬#m®æß½rçß.NHê\´WhÞ+.503JØ/ò®!íªr#G¾>ÜÞÐxqw\¿í+¢aE|;½Ñø>MgwkºZÜ§ñ^&éÛÙdrlAàJÖ!U[A¨±jÂnÈû/EÄdª@CµlUnÍdMË4ù>]ÏÀéëçAódµvc*Ùj¤ºÜPÜbm&9á¡[v;­ódMÓÅÜZµ>Óé<²Mm½Ê"cP?µ¨ìþ
ºòÓfÊP)ò-**ð±3öûzDÿà&/G*¹Eê¶÷â"rõ¼7ØÚ÷æÚ`ÊC`P#r¶ îÜ4¢*ü}96Á1²Ý:½hÿÕ#ì±GÆÐÑ¶DÅÀuÿÉâE9¸q}ÕP.=$|ú	QlãöËRY^d;Ìó|öîNh¬íÛëA÷.®c¶Ù,"q°ål
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/51/e279078e558592db9dc988e55fc29e57a6c4cd

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/51/e279078e558592db9dc988e55fc29e57a6c4cd (latin-1)

```text
xAnC!³æ¾@#0ð?ªª'È¾KÇé*Brþr.ßè4Ò[«Ð§Óª@â40ù=/ÄÑqKðä"Gg~yècB¼qÂImÉ~Ý,R¸®IbIJ4ü÷>à§¿\¸)|>õÖsmýûÖ¸géíÜióiß|Xo­YtõMý¿i¦>'­ï¥Ëª|@áã¨¹?ö¬K°
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/51/add89c19fd2fc431fe411d70619470a16d826a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/51/add89c19fd2fc431fe411d70619470a16d826a (latin-1)

```text
x}UmnÛ8Ýß:Å»'mÐÅf[@(©¬ÚNÝÀ%d	Ë+RÎGÃìYz±Î-ÙÎòlÃ7ofÇi>Ã£÷¿½OËDÀb1}(ög¢ÈDúfúÑÛ:JÄRr±û¨KQ¨ý2.ôNÉÍùÌ3u'5²BÞN·¿×A6§t¬%gJÒEÉµ;W>Àiø%:	ÙéÃþt{§áeðWxÙ"N»}ìÛ«çZïÀMç>F7b)2ÍôÃBnüntÃó?SÁgªªð¥ÌôïLÃ¸Ü«mÜ¥-¶ÈâèØ0!¡ÔeÃ"ÆO\ÌãGÅX¹L&9ðÃ\U¨5²ãÆ>¢ln âcïÉÆÊ9æ#$Ä0©C ÊE^h0¥r((1(Ø{Ì,1,üvìóux²Aôoo½ö÷àü3;
Ï¢nh8uçêö»J>|ÒÚRÛ7Ùn9õá«É@Ç|ô´qb[9J­S²6üÔS6'
4Ø$|æÃAçüºqxfÌù6\Ûÿ,u-s@½EËl¿}°ÆÕÞölv¤jyETÃ»©L´Ú®¦´
*$W½  ³2·ÈjÆSv+tk¯Ì½gzÂvÖëc¡úD"Ý¢5Îó'lFcúfÝDðô¾s`{íw7}JÎË4ÖÂaËÞÅFól1¿ò1)Ü÷äUL¯iäãÖÎIÅa®H,(ÿUÃó&yßDNrFÑ2ö8¹
¡SgVN µBÌööÃÊ7êáiâ
"lAÆ(¨Q\ÆéOLìiÑÔ» ¯_Ü
*nD?ÚX¥W/ñx:BªU"ïb>cåpo³pæÌÞ=c&îk°JðÐ¾óoÈ*L+%½ºLo9Úd\Õ²ÊºúmÔ%£2~ÉÙòç©LòÆµZÈË³CIýh\$ëÆhÔö·-mAh¶Ïl)ðÛ8zÚ ËMõ¢üÿ©îöØ?A4tF(ií¤íÉÄ3C¸¾BpA/1£÷Ö¨X5cT¯öEeRz0BÞ®ªøleÕ|f
eññ8MÇ¨²l5¿L¡HÑ¹oµ£Nv¯//üÕÍâáó7N
è¨©dqo-ÚÕäÙyuÒ¾!þô2õÎìSd,ÚÛµ!î×ÑFÛ-ÄÆ·Q9ºDë½ÚuIÖrG¯¾q¼â[=¨mÎ&¦$Ë3M:|°¨
m2[.}®®.£`õº>ôºgÑ9«íËìªõúÑð+FøÊ	 ?
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/51/f4911c28b9af9464ec420eeccfc295100f4e6e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/51/f4911c28b9af9464ec420eeccfc295100f4e6e (latin-1)

```text
x+)JMU026b040031QpöMÌNõÉ,.)Ö+©(aXÇ¢ò2Dx*^÷OÙ¹þ1ÌUYXT_YZV¢Ì`´xÙj]×©wWo099ñËLk¬ê2Ó3@ÖçÙ_Ý39öØ³9v¥u^¶9 k(.Ï,IÎ/Æê¹¸ò[û Æçf4ÎHE5ÌðrÏ=Bí\aõú]Õs/\Vl ³ja(
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/90/e1da5586b8b9c4197e2d8e2ba7fc2f919eb5f8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/90/e1da5586b8b9c4197e2d8e2ba7fc2f919eb5f8 (latin-1)

```text
xuQKÃ0Ç}Î§8æK
£u
LÑ>¹)V|ð%dí±¦iIÓê&ýî^¦ÎíaÜï÷¿ãº^ÂÅÕåÉia2Ýå×lÔÚF%Z:T·lOªÊ{4NTÒÈÚy´!¨ê®EÑ:éPdJæ¡1Ö×E[jßV8eQæÜã ¾P|¨B#ðÉ_îY)ZØðHãû§ÅCÊÏ`Ê¶õ^oí2G&öpóëî«}ù'±ÉÙxçñC×D÷à0ÝéïóßâÅ«x¹KÒcOø¦
±(¤j4Vt	5Í¤O
´>Ó¡k²dþüÈìK¾ßÂyy
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/90/7fde1bfd399a382dcd504b697ec73d1010e2ed

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/90/7fde1bfd399a382dcd504b697ec73d1010e2ed (latin-1)

```text
x+)JMU047d01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õN¤üÄ¢bÐÛäÓÜxËV[ÝÉm5»(yÔÐÀÀÌÄD!©43'E¯217Ãsõ¢øÛÏ%c\.áp8z¥bLr~^Zf:Ã:Òa'
¥3&õWµ-O(¨J-È¨,bX»ëÓÖ	[&ê^©ÌnèzVxGYË n®C
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/b1/007e84fd34942021c56686276a2952e82c7aa5

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/b1/007e84fd34942021c56686276a2952e82c7aa5 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLgdðÍ>[òèíùßÖïóU×<ÝãQPZQYÄ°v×§­¶LÔ½RÝÐõ¬ð²' ±õTí
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d1/1db376d826bbe573eab2789d18872d38741967

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d1/1db376d826bbe573eab2789d18872d38741967 (latin-1)

```text
xT=oÛ0íì_qHæ£E
²D;D$Q ¨ ÉBÈ±
%×²¤'SNÝºúõN²,2¨'÷øî½»ãÍËz§_ÏÎ?!¬·MyÍË|ähÊgú6¼Ò±àâÑÌy4OC&Æ`@/¹¯%TZÝÄL÷ DÅÙ:JN¿}»øÇ©+Ý3dð¯ÝS
wõüÐý8P&Lr70Ð5ri¬´/ù5^PQ"æT£$qÀm£=ÒÑÚc®2mvñÉÖ1/"çô
þl@
ù"9Õa&Bìk4%IFºl6L:Ü%ùi2!Kûz³ÿÿßÒÅ»Wö]B~«m¿ö4RµÔ}QSr´Ï®¹ÇÐë]
b)âùv½Ð>ÜÃc)üÔSÎJ÷3¸Âà·TÞz h-åtgÖâ*ºi tÀ®Yà·^/ Æpðh*l`(|FT8wÌ7sËÍ³È×T&Ãï»£ênjXîþ,¶e7øÕî÷C^¾ÈÜÖ]2áK²×¹À0¥jX §×?7+@y7HmG¯YM·4B¿1,ÛíA[ñ¾¬'ñDçñÀcÀmôs[4ùÐÃaØÍHéÐÜUB£Ñ
émÀ[²ºÐÍ£8ENjµºÌ¥F×Ú¨YÞ
é}_í¼)M¾Ì`CQ­¶¸Ï«Ýóº¸«aQÃm¾úþ¸{=5&;p¬Êb9NÉb]à_Ë'-Õ§BýUrøîZë6È`Àêþ
ÆÅê®¨«¬<eÖÀîï¦(aEÛzÏ·÷Æ:Æ4ýýì¬¦vÉÿHÚà
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/92/a2c59a8b5e20d35f3b2b736a832eaea6bf872d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/92/a2c59a8b5e20d35f3b2b736a832eaea6bf872d (latin-1)

```text
x+)JMU03µ`040031QpöMÌNõÉ,.)Ö+©(a8#8I£yÍ¡9Üí.;`ðZ]vYTen~iqj|QE|Puj^j^2Ãï££ÊÎÞâ|Çð(`Òí¬®É·Q$¤"ë8¹Xv{±ËéS:çík»RÖ{EGIjqI|qj^
ØEU1*;~ç²hr»úxùâ	¨ÊQÜc&¸09äÛº³'8|¾®¬qü T9ØÜÔ´ ³/ì~ïN_Ó÷§ýý©ç§ËùÈìFVVR7WåþÙ;÷ùS¼êÊ­=õóO¨ºÒÄ¢øÜü²T 
¨É
>)Þ¿[/Ùf|ý·ô|hè+Ï¨ùÈ:RS3ËR`êÕê½ãÞ,g®ÛàkÖ§[oæaUsÒ;ú=÷ÕyÇÁ#4EÝà»²âòÌäñb¬¾+¿µOj,yþgFãÈéXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV¨òªÜl¨O!Q$Ñ}KÙÞ)xpÌPù HÓQwA!2N½ÀYòh­îóo-··¯ó Ìù»
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/92/c63d53b3e99161749ba173be446fd1791f37e7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/92/c63d53b3e99161749ba173be446fd1791f37e7 (latin-1)

```text
xTMo@íÙ¿b_R)ê|T¹pÀ°¶Ql.)¹¬p¼MP1¸`[JÿNO9ôÔ[¯þccvãDõ	ïÌ¼yóæcs\®>ôaVl**Oæê9Üycy?»÷üÈóÇÖ³þ:ãqÈð©ëÄs¥`î&['ô
2\®Î¯/?ÃilÁîØª²Úý*à¡X;³?v!=ÕPD:L8¤+¼[æ9 £O÷:,ª$¦^dQ?IÞÒa~$0]®ÙØYH*0ô­Áø
XçÕåóÅH5r¾×h6xh´%úq8¤özÄÙÿÿ¯4qÃîÜmßè_Ý¯}µT5t+êa
tÙ­ç0¬Êvn:²dq\GÚÎÌ|Ü»»±Y'H	ÐÐñD«^Cö|/ÂðîI¶ô)§a4S>9Åd8²ãi$§ìM­.êØx	ÐK°ÀóGÜtqÎsõÜ2ÄâïJI«÷ÝQµ×é6»?MÖ~¾û½UÙ«Ìµî9§\PyM¸ #RÃV¯]7Ã@Ê¼k¤ÁÖ½cT½Z!Í¿>,ëëF¶_ÆJ¼EÑz>àáGðýØ¤*kxE»éGrfûöØÆÒh´B|ë5xVc:x{~#&µ:fS£»°ÚªÑ¸×DÇ¶¯Õf^¥ÕZ-X(HóÕf
*ß½éCîÕêé¹ìõ[-4&;`¬²t
§dQ¦x!áçòûY
õ©"SJ¾{ÖÒ@Î
ë6m§|õyÁ2©`÷wf°¢k½PóÍ£vq õú	Í\;£©mò>Ly4Y*WE©*]Èü°Ya|e?¡	|K³ZLµUùº¨H×à8ÙÇ×Åxèt¾P#Ã®){3ú(ìâ¼÷³À
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/92/bac9e5af2351e61394864ea1544d408de53eab

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/92/bac9e5af2351e61394864ea1544d408de53eab (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^CÚy/³¾·¯úhYOS°×,û`©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨ÉïZLYxéàÉû³ß¥HOPâ:ZÑî+8Ø}NöÌúðê
÷Ù7> Bf^rNiJ*ÃN¡Ça·æ
}¯~º¸âµóQMN{ *Ä¿^i9çÚ¿å§T*Uj¿Kù=2ZWZ\¢WÃÐqì Ióê72øÕ\ûõ3 cé>
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/2b/68482affbcacdbb2d9144c731dc4bc6d47aadb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/2b/68482affbcacdbb2d9144c731dc4bc6d47aadb (latin-1)

```text
xWÍnÛFîYO1v`J[rb¤¬L»UIä´©ë,(reoEÛ¦è¡è¡§>_¬3»\ä Õ³óûÍ7£IMàùËÖwß<¡ä>×w<¾¾Mög<	y°wý¶±öÊçáñÍ¯±àIºè«¹dD(6¿HoÓý8a6[¹7í6~wM/O|>!®}ÌzýcÇÌê:ÖÈ¸ßj6ÒÌÍ^¦¤Y{ËÌG51÷ Åà
>Ã«£Ýa§öØÐúL)6U©ÁSrÕÛïMH~K]ë»kD«Izö÷aàzQÆáÜ_ÁEëÆ²./øËnc~yD//¼(ÀÇ5÷fi>¿ÔæsÌË·,I>½8¼<ÒÇxJG,Rô£¥ÌØp'.Ä.>ÜdîÞñÐM@Ú¤}T "[ø _mjéÙQí½¬ ÇG{eûDkfÝìáoh·
ó©²¯+HÉ`ö{»7fïÎís_mn±F§ïØ±}âôlG¦<§WLHÅ¦Æ0¦´°¦ÔEFëÍCvp×WYÈãiZfI¹B±H=<kèÔøÇ¡m³ÑØêiçLçÍL8l ~s3V"9õùnæbÆð	lPËòô©kú1Ñ?¼fChCÔ*»¨JøùZv³()!þl>êñ)çÏ5$xñß]ðEGáÃ?H=toÆ(áìgÆn-ª
»²$&±þ«8¤Ó-úL¢(8Á¬Êf¢{KTÁDìM«]¹¡ÚßØV²±ã;~ó·pÛ,5}ÛRº
¯`{Èî¦_+õNýaÞ(W o³Û{|"üèúaYøØiü²òetVþô£ÔXh^
K_ó¤¼HMp"OEk,ó<p3nl
¤¾Aj^C«ZgrKk'InÍBºÈ¸íYMê&c÷ËjQ+P ±Î#¡/<÷á¯?#ð£Jenc²gH»Æ.ÂÜvEù¥ç±AnwvK¥.Øæû­âþ}]+ÚLvL¥71j¯y¿uå)Od÷é^ÒtçÕ{GêiÄ#©a×£ àm=áë
Å}&·Hï8à<áSe6¨X%Q#îaw<Ø¢°¬Õòas¾Do¥4
MÏ]"´ã¸3«u°²ìrê ÒØÆ¢3OßZQ\H<"mVH<LBw2õâ1~9C.ÔÃÕVüüäËGN¯tySº¦h5 n²½E¸xø#@6ØaÌ9SÐ$$m;~Õõ
ÊÉ}ÊêÓVGËgYqÉÓ>§Ñ ¥¡&]A]t`ò¾Ô.t}+É5×%UáÄÖß©ã³öê~¥,4pÂÐë Lq5¨] ºÓ%Î¿>]z}ö³å²c¾VN¹`a»6­V¦;ÀÙçcy÷dí(0ÒJ¡V²[­
Ð!WÍMÅòDmbéáß¸R¯{®¤ª%GÑÐ¡Ñ",G½f"ÊÇ¢,&RÉ;·´ÏîÅQ5«QkðF4T\ÿÃ«"OB8åNÉ«¹©¸Ê¾dg¹÷ÏÇó1szVgì¼·Qc£wÄ=£	þ¿\6$éäóÜ àBÅJº¦1"·@SMM·¢Þy·[ÄZÞLnîºKaí¼^­9ÂKÃ¨ºr	+v¸%Òþ	B-yÍõ Þ¢÷Õ-N¹W{ÖÐOwèóÒ-PâEºue"3Ålñ#Uäå¤B¦ DþZGX]D°ÈÂ	Q*}aù±Úº×T`
]§c~ÏN¿wâ²Ê¼ÌC§?tÆÐÂÊ	[Î
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/bd9da983f722d72f1ac6addaf8d102c6987be7

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/bd9da983f722d72f1ac6addaf8d102c6987be7 (latin-1)

```text
xIj1 sÖ+úÚZãøc·Ô3,#Kÿ÷|!×*ªôÖ	Ö¦¯9DÐ%Î©V.¥sFô¢C©-§-"T/òlH»d<kÇã,8Ù-ºÓõÁø­ùÛüô5àAMàú½×£õûÞèøû.½ÝÀDt9 í´V'=ÿ¦üßTSÞµC^;,S} Â\H
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/49aba25f70dbe7195da514d374084510c5d471

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/49aba25f70dbe7195da514d374084510c5d471 (latin-1)

```text
xMoÔ@9çWX»Gv*µB"q@T-(¡Äñ&ÉÌh>ößã|ìnWâÐcì×¯_?¦w
¼{{ùj
GØrOÐ¥"¤àÓçÜÀGØÙ¦À/5Ü¸ /Ã`à5Ä©7 ÝÐ°Åi`hÌh4@rarzÚQ¿¡5â¶b¸ØùàMÁõ³
[Ã;6³ÿ])nËª­î³¡|pBÚ_À£Ë ÑöÑA4eªõ¿IahãI+.bå1
[Á1Ðd$úêhÙ{JõØEx"ßíÎÜìÓ5Ä[ÔIY$Ó([Éce,m9v0ïq9ù$BpêÐe±pø~ÂÊ²¦Ê¢uÕîj¿D§¦vÁRÕÓ6­6°¿·]%± u0m}_Ú]/:°¼]	"ælÛ7/8;XÍÈJ)v*x­rlTväôT%¨ëO÷ßnîn«§¯_ªï?®ïî?ìÝíR~¤ê§®E¥Tq$ðìþ³CÌñÌSñrù»øs[$½
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/62b5ab43126b316289440c00268405f3039e87

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/62b5ab43126b316289440c00268405f3039e87 (latin-1)

```text
x­Mn0»ælÒõ%
ù!]tc9xVSÛ¤M¢©«!«TI7ª®=ÏóÍ{c¯¾B·w7÷W=äfaR0D uüKDÅ@(iì ·³².«BÅiö÷Ï1¶gÓûx¸>UXÍ
{2;Ø^ú¾3
ðb¶ôm?¸þáz08_aôPx¦ <-RdJHs¨jrü ÄÒ%¼¡Æ!yæ¾û4}Pÿ³ç.ºÕ.}Á)/$`©Æ$B­³­Íz(\Î·{ný§±5³?ô,i<2%HÌP@¾ (/Ï¸4VWAÂÚ_`8µÒH-$ò©0î HùN\té5 Õvw0© q"û]S[ÜA¦@ªËY:·ÐY$Ì:©9Çp«\b¦þ3+Á¢¸[XiµSUVµIiû½	<:äªþ°Lÿ,-ÈªêóÄ:Óê·i_½`
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/66f0b53dfc0dfb2075548e4f7a7213860f9378

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/08/66f0b53dfc0dfb2075548e4f7a7213860f9378 (latin-1)

```text
x+)JMU01d040031QHKÌN/.Ï,IÎÐË`hà:ëãù»ùõ7æ¥l§Ú³´­2 ås
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/da/236a316223903d7d7f7163c2256a496e64b3d6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/da/236a316223903d7d7f7163c2256a496e64b3d6 (latin-1)

```text
xKÊÉOR041dPÎÌKÎ)MIU°©J-È¨,ÒÏN-ÊKÍÑË°ãBÊÍÖO-KÍ+ÏMÌKLO-BVªJq|n~iqj|qIbIj|rFb^zj^W¯w¼k«_H¼§o¥Ö\ `ñ4
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/feed8e1ff33448689af7a03dfe9c63d97bd8c3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/feed8e1ff33448689af7a03dfe9c63d97bd8c3 (latin-1)

```text
x+)JMU047b040031QpöMÌNõÉ,.)Ö+©(aðm¿þíKôêökkó£Ýï^j÷{UT_\Y¡Ì 4ïìÅ#[^½Ö;¾:ûe_ËOiLñy%@Õ*Jâ	kÝÏ¿ÿ{[¿Û¤gá3¨êÒÄ¢ø¢ÔäÔÌ²Ô" Ò¿Å²7«¯ÜùtçËw»ï=û L§
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/28f38cc055a6b9a83aebee7adccee95044a8b5

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/28f38cc055a6b9a83aebee7adccee95044a8b5 (latin-1)

```text
x}RMOÛ@íÙ¿bjä´)p© PgI-%µ½¬x¯âxÝÝ5*ý-=ôðÇ:ë844m}ñì¾÷æãíL9ý7/vD9+êáÝ=Vùê.PXìå§ÎTÈù\ó.ýÿÀÒÝ-Ójû~yz#¤ÚFêT®oå\yn¶)x¥ÑÝJja,¹6©A>ËÓrÑº]ì)HÈ1ÍPA&¡ÑIÇ!t
Üô]³QtÁ°ÀO¿S`a2¸â XëÄIÞUÌxq0bÞýrámxõùçÁ·]³¸sì8;~%Â ¢<Lâ1ì<][þû4.ùe2&Q2ô¼õa&x6îÀ«gê×àY°Óq^?HøZ#`y#ÒvDø»5`º*³9¢4°é¶Ëº°N6¶{5áo¹¦£õû0²J¡ÖuàôYÂáÑ×¥áþ;ÙcuÚ¨zfläkåó÷\DÙVu¬fOËZÍ°­°¶'ÁñðC0ì3>N®F!£çØo*­vUHØv¿¬«[°]¬
Ô%Ò-+¼®ìÏÑxé¡ÇzªÐK¥B#ÿ÷\^³´%¶/»5½³¾çn¼ìjH
x»»äóÉéSctö©®sD±û»Q¬
ÞÛ.«°ÀT£KºvÃü§t6i;¡¨V¥½8v_KÞ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/c309bc3da7c05bfd749506c5a1a56866012050

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/c309bc3da7c05bfd749506c5a1a56866012050 (latin-1)

```text
xUÛnÛFí3¿b ä2&%ËºÔu ¢]"ºº¸HÓX.ÒÂ$W%6Sô!@C?YRREËuBØ#;;sæÌÙ¡
êf³õÃÓ0óüü-Äx`IÌÂóÅkíd)ó9çþ>¹.7KªÓ­^1)\»'CV9òq¬èÁH!n$²¹)KV2åepýBæ»>ó²©ÖÝºQoÖ·Ý±}ëL¦ö¸R´¢:X£ásëþ6xë*ÿ¾}o÷«Wfip³ÓZ½ýÊãhJÁ$ä8¶_ðFÚr/èö_X
d%$Ñ!")þÇÅ_]|ÁS/ÒsÜlh/|ðÁ©«r»»¾3Å*fÛØã{Ç²Ýûn~× ¯½"tí¡5êÙs]«ëæú¢æ²¦ÕFÓ1Ñ
õõÝfàÑe®Y>OF ¸àQ4>CUlø3`{Ýi÷[Hë5Ô¸@Ó¼DÓn¡1;h<ÌÇîe>B©ñT¢"PU+óÑ"M%B*Jð¤eÜw¶¢{eiåp]bØbÐù
LíVû²yÑ¨Õgý¾ûÀTL²úÄë7ú*q}Hò
,fÀ|êN»Õ¼l\ÔkÏa©×ÊÎ;,Æ`EBÀÃ»H¤Àâ'	T¢íßk	àm$KÝ¦3@y¿éÛU¥Ù]5eÛ%F1nÆÞ×Íù:»êÌÜv§Sµ¬nÒîÙ7ÎÐ>9¥ûVä¾wcgÐ¿Ûï©¼,éb:ä´Uu-ßZ<´O#OQ?ÁÇK?B,$6
jÞõKwÜµp\àÌp¬rCSÎþ§ñþ7¶pu{ð×Q
|7MwßãÎòÏzUÿ¡°Ç¬ämØÓqeYÂuÿæähþî×±3µ«Z1á&·_¶ÿ À2¨½b»ÃðùBVr 0Jª(X¯P§ö²9SÌêÇÅUíÏ¼-<
>ÂkHù'&<ÒªP¸*â&³$W¶3ÄIyø\(!b]nN÷ëP$WIQ©*
f'|ÞK#ðAÇJØ÷²Qå%®Õ\Q0wW_AnY+zIú¾þáÙNøÊkÔáõÌ}õø=Tú
z!Ü%æÂ/{¥¦CÃÄÊÔ*:íØØÐ+í³ö>gì
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/0c2aa2f4dc39b3bb166ef59080490206fa3350

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/77/0c2aa2f4dc39b3bb166ef59080490206fa3350 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^@ÂrMÙÇâq¿g_W|¾:SSi~YjQNb%Bìg>G|]]ánË«ÈQ9}ÏÕEéP'³
ÞürbbÉìÅû\ò/VÊ?Ç¢f´û
&vA§=³>üºBÀ}ö&@ SÊpÌeõ÷¢5x.HÙÌy­ã©¤fÅQQ\ÌÀöÀ_+ÃýþÆ«(^ÌÚÁõö
ÔºòÔâ½ÊÜcMWÏ¼Á¯ö¬ìàÚ¯ùÌ ,_p
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6f/a767a89996e9a860894a15611f2a2ba9fcea21

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6f/a767a89996e9a860894a15611f2a2ba9fcea21 (latin-1)

```text
xÛRÛF´Ïþ
2rPÁkCÁxpìÄ¤©ÇÝ¥5h,$¢1aø~K¬çìEÚe É{ÎûmwÆ3òrï÷×¿ì<#¹d4a®YBàü"ÛöÈ³ÆÓ òÂÜgäÝOvuqì,X±pûâý*Èg×ÇêA	NwO-Bõ0>?¢óxW6^.89þ2ïB
mÊ¥P.ãkF/ã<e%Z£?<¦Ý³¾CGÎqïtì¬;ØûÎ§O{£æ~£;ëÆD(fJ37<âÅQ4Kr/+ &´I×ùÒ;thwL±¯Á°ëô;Nón5%ýqp§@°ke1wÏæAÄóeLOoÃÎ¨KZËÖnã©ù8<;u< Ùã¢äó9KÄ¥¨yeohFfù\Ød²ûjº¯ 
¢·([^1/c>
Y¤£ q´@'®©´·WKì!n(±IÀ²+¶/Ö£ $âI:b.à£6'ñ±K, /ëW	KSæÀ;²`7åÏZvÒzþ²ÄCjYÛ®-§^!½X!¨ÔåYÁUr»#<ÅÂÝ~þÐôGA¨Y=ÕãCBÆôósæÐÓÞ_ú½ãcò|¯qB?¦]ç¨7pD"G\¦çß§l?Y<·Öz²ió8[ÃÆ&/Tx_$ÌõÁ®·@OèøÃÈétéé¸sxbÁqÿÝÖé&ÅXÐLã%¾©ïf®Ø¹_Ô8[_-|æÚD|ÌÔ×lÜòø[«­HN >þqX»M-RïeÖ¦öºE7¹D69¡GÃxgBzøÒF,³-e¼ÐyxnjÖ·Åv$ÁÙÊyèf²Zâ
6üÛEö=`È¥ûÀ2£Èê #oÉÜ
SfÐ-£zfMñB)^Îj4ªVôuÊð$ÙöëÄðûá*qõ /ÉúõÖPÆ)P¡Ì»yæÀîôu4°6Ñ)|Bº`^àÇoÉ¯­½å-=«P­ùÃ;Îñ®qÇKÊ¡3ÌSÞóÊR&7©TÛÿ KªðÌT©¥Ê'äééÙ X×*QÍüâñ<æ1+®oqâM ïÞÁXØÝ´Mln<¯e§£££ò D¹ì;¸&À>«ôÞ
~SÅ¢6«dÈÄgkk
mUªî<Ñê.¢ÑÈÚ8}FdB~è[,s#?Þ¨Æ©5vn¤¤u­[Áñý?-Ñn½ªÖÊ^|ì®mcv©â#ÛZÑ^í²³C&ÎtSÁtåi:"4ÈR¿ âi~95T]'
¯.ãÍþr:ño¦Q¾©?§àhÞ¯ëÖ
Pd30N\ÿûOÈ¹µ©\Óî´âw$`DÚpYj\Ä_\ÅA|â£kÈBFb¾Udj×¸¹ê¢0H·®j2~$ Øî>¼ÞÕÐ%¿qØÖV* büÝÖæà Æ`ªG+¸ª¡þ¨1 pÖq.Ü|¨ô+\Í
Ùî÷ägscµù(	8ö#1uC
ïT«¢ÔhÆÏÓucØóq
¼yK´Y~&*®Î¶>cÏ#J
ß#É^% [9AÙ1°ß­F!]ZlÊ>­jæúBÅµPS´K'î¥åÖ+¥F {6¯×QlVó;¢É¹ªniNcó²vóË­ªe%Kð +µá¯jÃá6axóùUþù|0¤_;½q¥æbø!1(Öe:oßüdÀI;8ÓqêÁ»ÚÁ+?¢¥§6ÏCyÛCñÔh=74[ ¶näýÞeCN1£è×"Qf]úx¦ÊH¸G*É'º ùN=9hÒbö£0àh<mqQã¦Mgý¾ôGA%YR¹³i:)RË<­%ýäiÄ­Ê©ÏÓÃ#ÁVÛÛ¬/Ü\`éÚqT(eü¯åýÚ&-<5QÉÑÐpKempò¦aàZ*z¬/Ñ±u4½IWÃ¢®@~Æ&N¿4½±tq¿X·IçÓ§~ï°3î
69zÇT[ã$è§Qo8ê¿ÿ tú
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6f/9f30d856d2a63182505912978817e166ed1e58

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6f/9f30d856d2a63182505912978817e166ed1e58 (latin-1)

```text
xWÛnÛFí³¾bìÀ¶RÄI
V¦]Âª¤HrÚÔu¹²·¢HÅNà)úPô¡OýÿXgv¹IÉªJXÎÎõÌÑ,fðìeçù7Dè¹Ïáõg_ß&<8¸~ÛÚxåóðøöWXñ$=¼EôUÜM²­"Û_¤·éa0[4î-¤¥Dæ]³Ï¥Ö#ÏEÈ¡o³ÁðØã)³ú51îwÚ­4s3áiiä^ä7óQWÌ=@1x§#gÈðêdd÷Ø©=5´>SJ§í£ÖVU*Kð|C5Çö{§g"Ò_äRßúÞî$ÑiÃC¹^q8·ÆÓWpÑ¹±¬Ë¾âaÆ²Û_^$Ñ§Ë/
ðqÍ½E//µùó-Ë`Ï/^\éc<¥#G)úÑQfl
8Ëbn²t?óÐM@Ú¤}T "³[ø _ZmjíÙQí½¬ ÇG­;eûDfÝìþoèv
ó©²¯+HÉ`ö{{0eïÎísM_ln±'§ïØ±}âlG¦<Z¦WMHÅgÍ-a´MiaC©	Ï:L2×[ ì:á®¯²'ÇÓ´ÌrbzxÖÐ©écÛ:f©Õ;ÓÎ!"Î[ð¢ûð+[°ÂÉ©Ìw33¶OXd³@ZÎ§]Ôþáµ[ªD[¢VÙETÂO×"à`tÛEIéñg#ô	T9|©!ÁÓÿî/Ò8
ïÿYñ@ê¡{F	gW<3ö+hQUØ%1áÇXÅ1enÑgEÄ	fU6=X£
Þ bo:ÝÊ
ÅÆ®ê½=ßÜóÛ¿»f©é;ØÒ]x»cp7åøZ©GpêKôF¹xèÅØ­ô $Üã3áG¯ÐËÂÇ^çéÏ/£W´"ÏÍ8´½
Ó¥mêÒSÈde¸¬fls¿¹Aº^C§Z]
Sh'In-BÈ¸MYMå6cwëkQúNÐ{ÿ×ýøQ 2TI²±YÊ3$[cÁmB·¢|ÁÒóØ þ¶{F·#éQiûýNqÿ®®Í%{CæÓ5¢×ìßºsò'²çtióê#õÍÅ<bÄÔ°ïQ ð¶pLuâ¾³[$ump¤2T¬í°¿ìî-«Y>!aÎ×­Ôx¿ÐôäÉ%"I;NkyÑÔ¬e³Æ.NyúÖåBâéØ\Ä³$tß(SÏã783d@=òPmÅÏß|ù
¡3¦æ+]ÞÁn(jfÔ-R6µW÷È;0®°Yð¥â:4¤mbÛ7]¯ Ñ§¬>
gu´~ììs4OZjÒ$Ðõù÷¥v¤k[I®¹)©
OL¶ùNµWw²Ð	WB/0Ç vêVÌ8ÿúLÙO3mËùZ9åÖîØ´PEî 'å=µ£ÀJB5²[­Í1WÍMÅóDíbéþßØ¨×WRÕ£hÔÐúÌh^3åcGQ©ä[Úbâ(ÉÚÕ¨5x#,®áUÂ'¡r§äUÄÜ\\å	_³³ÜçÓÑù9«7uÞÛ¨L±Õ;bÉ­ÑÜþ_®ItEòynÌpb%]Ó»©F§»Ðà¼ß/b-o&77ÜYÀ¥°v^/TÌÃe\£êfÊÕ«ØÜ«­¡Ã*ZíÚA½ÕÜÝ{µg
ýt>/MèÐÚ¤!^¤[X&0SÌ?RE^@Ú+d
Jtá©MÕE$ ü)5¡ÒÉ	ßª]{C¥	ÖhÔwzÖÔLè
'Î)«ÉËl4vcgú-ü©û^
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/6f/a32f2683f005fd38da3206ebec9f265b45f6ea

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/6f/a32f2683f005fd38da3206ebec9f265b45f6ea (latin-1)

```text
x­»NÃ0ýÒ!YZ1v¬B¢¦¥)åÆ§EÛ)ÐªÄÄ#ðb8Â«ÏïóÏö.;<__YØË¢¤àq	úýMr¡0e :A¿HÂË"¤¬´=8ß/æÄ]-gÞíeÔT8Ý	w1O»
é2$Õ6p§äÆ.£á°=Yx&2
8ib[AKÀU÷WF¤©<&J22(4Ïñ:ðî&áa<8oã{°nrJH*
DiªD1ÍÀrâ{»smÖ¾`å\ÃL|Çma2-ií2A= (÷:º¨
*µÁ:BÃÀ^$lÖÏ£T!sÀ Iÿzâ:ûjUò$\iÈ@6TV×W½¿iPºr$
ìÚø$Ïch¥ëpþ©OòCÜSyã¯_¢¡ÿ °ò¡ 3°ôªºE2ú2f³> pG[
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/88/c6c13483ab99d8680f26e676c1adf5f30e3600

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/88/c6c13483ab99d8680f26e676c1adf5f30e3600 (latin-1)

```text
xmAnÄ E»SXÊz J»Ê®gè	Hp-`D3§/dªªê
Ûÿ¿!Ð om÷Mò²ô Yð^\={J=¬­êêWÁHg÷
ÉDìá¿&_âf
>¦ ®áÚs"{­g/nÔHQÿ7ðn­zÆd#%1>ù4Ã@¦XÖì<úÅ*°£I0 ÏÃ°a#
| þX°4²ºcv·}â(Ê¬_U§ZmqÅ@Yo~QNbhN1×Ïò ó+ÿûÀó3éÁäãºÅÝ#ceÙë÷Ø/ßkÉ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/40/514653231d315dff6ae3de666e80b5b1604021

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/40/514653231d315dff6ae3de666e80b5b1604021 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg¸ZÿkÏUÊ6O¼|µcÒÂU!
ªR2*Öîú´uÂºW*³ºÞQÖòà ,(W
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/86/23cf346da430446206a8e0e694689442ef0e73

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/86/23cf346da430446206a8e0e694689442ef0e73 (latin-1)

```text
x­WÛnÛFí³¾b"¥Ò%ËDYq(!Ë)Ü" ÈåÊZ"riHiüÔ~GÑ~¬3Ë(Q¶|Ð;3;sfv/p c­~>óbÃ«Ï|1[Í;úÜ;½®m-yÁí­ðoø]¹.WÑÊ¶ªãÅ\5ó_&òÕæ­-å7DXàûåíæwM»Ë¸ì$.Åv(­ypÏñ#¸åñ©Ú¤6]XFç×¾5î_WþX idÜ¡íéÐ
ßÖ/Þ[¤3èìê/kµf®¯Íó4qÛ";ÅbÆÞ=£Ç¿hµOö!Ï!¾<îX²f-¶"ÆL#­8®ÒPt#âá½`\-B·ø¼X´±eÍ	ÉkÆrj`øìÔ~~rt|Øiµ¯]ÉüÆc,[m>e®í4ÊR8ßçkKû¾Sî2Ç>=y~|Ô9l·vùÒnm
§¾`jÏEÄ°já
~«ØX(;´çQeö=jY©`éÿËí(Zmé_$åîÙçØì<~ ÅtZÈW­¼ÀvÁ-b Xf*ý%7jØ°£­A@}~¥ÕÄ?kÕêPI*¾ÓnI¸
ªµ®0Û:FÏ=î×k¿)T)h{´_¾Ð{xÇuHÖÈ¿Ë8ô	¨ge"·,¤ÑÄ^÷_*5õlå¦áÄSèÆ!Â0¢ ¤XöÍÉ	 ´L~ Î¯Æ'Øë±4ÚÿÊ´4îlÒÓEN«rÕÉzëSâs&¶JÊbíM1Dlày
oZ;¬Ã­7Å:©X'kCbäÓ.«Tõ7Í]êà®tÈ|ÈáûÔQâ ÖéxÂ¿CèK@képldË»+U$ªr¤ªÃCk!GZµ·{a«6YàlR±ÍåDÆ>û/t TÑÐ Ïï¤Y*ÙÈ½ÌúPò½AÚ¡ÂíêÐ6(Ã´=4V~µ'¼l³L/¢wAÃÓ öÝúþÏ#.µè``¹ÅgLµûõlUA¯&£Ë9±ö²ÄæÔöþkQ:<+8jå#áëÅØ)0sø¶X	!*f¶ïz¼k,.è@YÜ¼Ë°H©ÚÎf»W)÷î´UÓZ·ºÿ®K±¥|oã9TI9kh½^Ï&æÛ1+	 5ñàDkïÐã¾»ÖÃÑÏiBI6µº0Ä<Æ!£!­Íé ©	,M¾R¨¹26ÖbMÉîv:I°c7×ÑûãÀ½fDµ£v¦¶7â½µ±üW5Âò¨0úîSñ²"þWÂP U¬Z<lééJ
Ö"yð=OsªWv¾¬½¤^?Ë¤Ó²ëÂø*U¥÷©ä·zº»ø@¯¬O]:S/*%jí$è8·ñ^R-Z °H|£¤ïÐ]¤àSÆÕsóª7úHwgã³Eð¬oöÒÄdÄÈe¼Èþ§9Æ<&³n?ð^0÷ÿxü}ãþÙàÂ½2!xöÜÁY¸BÀ4<þM÷äºû4
¿	¢&Ç	êV¢!9ÑQamB¶p
tpÈï
9ðù<y3ègÔ$£-ïÂ(ùö4-c~ã>TG4#l©¿¥¤^ò¿sénÚè½¿¬ü½^{ÀòáÉÃôñ^eÇ2?þ Oåàà³°-µÀb0éµÎÂ*5¢cBDBêªhx¨=Ût1
:%»¡0qus¥.bUwGµg³w61GÃü6YxÜã.ÇæhlNnp kÞ×
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/86/8ab829f77f276b8aacb49887eeb413d3e2703e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/86/8ab829f77f276b8aacb49887eeb413d3e2703e (latin-1)

```text
xMÍ
Â0=ç)zQ)-xP¡"ø$¡MÖ6Ð$e³)­Ooúºeg¾¦é}ëí
T·¶ïÌ8ÕGð¬ã¢{þiºJMfD
e¬iNä@ySTG£Î$ÓQAY&ñmÑÐÂj*\Â$¶ãB	¨Wë©NiR»dÖ[?¢´>Ü zÊwôH³;Aï{ùówaÎ!îHSóS%¾ù`L
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/86/50d20252d13e2be6a8d79ac7f33b44bfbcf9a9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/86/50d20252d13e2be6a8d79ac7f33b44bfbcf9a9 (latin-1)

```text
xÎMÂ @a×b. Ê$Æx÷.*RÏo¯àö%_òb«µ&{®1+"M1ç,3#¯eÇ:JzoÄJÁ³#FéDV¢"*´.°æ)9´wëðj{'UÛÆsK¥¶Ç\©|.±Õ;HgÑXe´3*DqÔãoðÿRÞeÝ¤^¾ÜÅiI
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/23/8a2a1f700e28f90de8075bf4640382b302d356

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/23/8a2a1f700e28f90de8075bf4640382b302d356 (latin-1)

```text
xMOK1u¢ÀM
: ¸Y¸ð!¢-L*MRì£ÍÖVÁYïÕûT
,×_³!é>hl±[_Â.31úÅiÿq8]SwÆÄøX5]¿L´§±fÀáç»¹DràÑ)¦ô¤¸ù¶ôGÊö%oSZzÁóÛn<ñY
Z¤öµX6JÀÆÂò	\-+vèõUüJ?P¯;Ù×ù¼%ßá¥,Z°ïV ]
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/23/851c22d01c995ad94f8cf8db418e5064b2cdfb

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/23/851c22d01c995ad94f8cf8db418e5064b2cdfb (latin-1)

```text
xÎAn!@Ñ¬9/ÐÈTU=A÷]z°IF
¥"Ìý+tû¥'ý:z?áeM3 ­]'õ*Æq©²rÚ¬HfSjÕýÊ´w-*%ÆDÊÔ¼Ô$ªÒ²z¤JæÝØÉ¹îcÂ÷8'|I7xÚmèÑÇç­Ëñ¸ÖÑ?Àó}ñÞ0 ºW}ý-û¿tH°NËýE7
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5a/0d773ec554dd8048ae45a122606cecd53ab568

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5a/0d773ec554dd8048ae45a122606cecd53ab568 (latin-1)

```text
x}TÑnÚ0Ýs¾â¾$ÕJ ÛÓºMb²¨*B×näälNý=ìCúc³è¨Ú./r¯Ï=çÜL¹B»ýîí«ðÐCèÊÕF±ùÂpÜ:nÁdð}pfKÂ(6-TÚ¶ºîô¼wu°Æ£8GaØ¡zxbë¡ç0ñ2Gøp«ÅFKTysñéi)ÇµúOÉ(|¾¬Ñ&æ:Ü=8§¸Ïm[hï®!õÉ`Ô»H"2úq:Æþm±|ÝÑð4î+¸$ú%ÁAhØùD=¯­§çIç[°?³X9Ó+N7%ñõ¼Ö"g3ÏCèaÆ©¢÷îKÈ)ÌJQ?_tÆ`ÅcaÍ¥¶T¢0C¶FÕÌ<üi¬©Ày\"L0ã¯%Ëy;¦³IaA´FrI Â » ë2á×N¥Èq¶sÁQ Vj:J"ïà*a-FÅ,BKÀ4i rÌÏÑ  QÆ
ï`+ÝQ®ÆV$áörÇÃS¿q<.¯ÆËKH£É$öÓ ØÅèrª7º6Âvð5.iîÛ;2®è¡RðñY	5
o{-]wÌQÆc¿ve·Æ£ÝRcm¯ÄcîD¸3wUövqÛæ¨j°Q$Û =x!q÷9¥ñU­ßîúRª%U²9Ì¤´ÀÌnKX¸Y0»=¿½¯¯¡zITäsÈÑu×h¸òÏÈ º~»<hÙXß!´ÑVUõCp8
MiÛ:ñî¼¿éZi
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5a/e44ab0fe369b9b27080f37a7044b5ad429521d

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5a/e44ab0fe369b9b27080f37a7044b5ad429521d (latin-1)

```text
xMN1Ys
wXQM»¥À
PfâVV3ãD§â\$ó[$$²rìûóKá¸õýU×6üÕÍÉkéc­ ê²Dç¶ð´ÞmÒTU:ãTZÒXËsxªÁâjªX!JÅµþS<ãÓJ®ã©p8²su¼K½]¯lÂú¼ÄxÁI¡aApuIF C¯»å/a=LWÿÄIêMD<Dï¢Añ:<Vn§­g°Hû$#õX£ôlÃu÷OtÆ¦ÞøSüÖÌà¬Í6~.ØÜIv{¸Eqæ}Dÿ6Þ¥\ÿþâÅ ø t´h
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/5a/a62e1461f7d9cb8b37fd3a0536d8395788fc36

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/5a/a62e1461f7d9cb8b37fd3a0536d8395788fc36 (latin-1)

```text
xR½NÃ0fÎSÚ6D`ÉÚÊjbGS.V
ÒDji%Gèqn4¥B¬wßßùó²¬ð0]
!®·*_ÇÅÔ.âMFÈ©ÿîyCHòuïïÇ·pÚ ì?!]±Þì?jx®WÀãàÀJZñ»£YE­³ÄX®Ååè©Ð¯<¯(M"aÜËxYM`ËP}pëHÃø×Ý=Ã§
4·¥_Þ­c¥Øî(`_ºÍÝEÌÒå8mj6;wÆ
X|>làV<cÆ'8p=´~'e!¡g$¥6O¤\oÜ%w4+mth@	Ã p?:±.c!Á!CuG'EÕ"ï{;	[×@ïÞ?CðöºË¡Õþûe[ÿVµÿÚå/çC¥ÒGÒî¼ãôÇBòù"ªÖâ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/16/fec8b04caa85a9eb9849bf933ec179f9f76cb2

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/16/fec8b04caa85a9eb9849bf933ec179f9f76cb2 (latin-1)

```text
xéRÛF¸¿ý2eäàbCf ¤ã`A=861")õ¸;²´eÉd°áaú,}±~ßÚ|hdí~÷½;
ãyýæõÁ/õdî&MÇ{Ð³}¼¨WÎ}FÞ}c³»eR°$báþÝûÕ-Ý[¿ Ý´lÖQ°~#ooè¶ïâtÂÉÑô!È¼;!sQ,1ïÆóåPNï~ìµ®;6íÛçí+Çî[«F¨ëØímwÏªÇ
ëºÙwÐmfnxÄ£4#iÌ½,ßå$Ñä´ìÏíS¶zn;¼º½Ýi~°;s£*É;Á,Na÷,Êbîû³C/ì½f¿EÆAå¹±ó±w}ex`çKúa>³D¬%QöfÂé(ÍÇ7Ãc¥ w)tB ØbÆ¼ù`ßH¡l4F6OÜ¢2ÒD¹i(×äù^Aátru9cÇb=
âHÂ $#pÄK,ë
/×oÌ¦Ì×dÂús-;iH¡á¡Z6ÐåÔKâ0¤[7KZ£yAinÇµXx<®ÀZþ,
£§faðBD9¢ºëÐO×öµM¯ÚÛäåaå~¼:ÿD[öY»kà"1Mo¿ÖH|cñØÚäÆjÇÛz5òJEù]Â\¼èzï:öíf^9ÍÓU	8`4Ì9)Ãf)±@}7sIi5Kb|íNUvÝÇo»<oñ½n#õÃ«V¾ó°Üd½À=ÿpXU#~'ÍIoYfíj¹MCïò¹ g½>x«¦Crø²G,³/ed1YxnZ¬G9:à\eùLé<t3Q!­
.ûYµ-Û_Û¶e?FÈØ
SV J"Gõ L&Þ¹N¼Ú­Q¨Tí7éÂófß_lVî/·ï«\þ!¨'xÉä.hÿ1 ø»ó0+Z[Ö~×Ú±EÿðY
½éy_t¨6k­®ðÈz¬<òêrêáÓ7BÝWJyä¬µ=:§Ê"hÉ	ÏQMªÐyBfÿ^w¡«µ,
ZÌ)Äã`Ãøâú'¾ëA¡¨÷¤afC0&FE't5²»K<ò~-Mõ² ³cR¯Îô³Ñ2cPå/pÃÜ_`e¯õ¬Þ:CUÖOó JµÌµ°;(|¡Ø{{Cè³ÒJÈõ0H$£¼à"FÝï[;r9(ñôãúµëÇ5menäÇ;¥X[á);ÒUY ¾sæ2líª%¦ÌºÑ],ìóÉGYoÑrX¶Ü
äà luRÊ8Èe£2o¸çÍæpA PèYÎàÒkÎ§Ã\C$)²M"^Å~J·eqüÅpà/QnÔ¿YQOô1W=yÁQâüþ¿C(+ñ*ÒXÈ:¢­ÆgÈa)bDzk°íÁð««¢J_¹ ¼.]/|õâé,db F |®)0êuAeT½h¢Ý¬Oe\à#8ÿySû|¶6!ÆqÂË	 ïáõÎÅdK~ãû{{eþHN&ùçÄ@G_0îÄe´L¥Q«Èú«,Épy@åöÈêH§»ª<Ê  +i¬ä«ýtE¥Ö%÷0tLFE°Ê+CØMñY á®qÌ3Yn+!&¾cêïXóð,`RD9N·ý)GÎ~+Ka5TÉ[1ÔXVèU	Ë¨­ÚX[ ¥NxºÁ¹¸Z´äfÕøÍú
jCá|°*AYumâÅF¯K¶+}¬¸
¯¤vüU®pM0¼ÛÙü3ÝýÒl;¥NÑ´p
ÛTBø,ÃÏ¶ùÊ¸#cgRn`)1%]ß4Èæ4/Ãm1ß\^ºfTn5Fâü
ï»øÙR
¾¨þ3q§DÏ²K=­ÆÃ|ª3ï¡¢]áúKÓ`Ïy	JKpõä+õäOóÁÂ ¨Y5Õco÷ºÓ.Ëi$Ê"w2 <bÔz UÆÌ#®q47~!ÜTèîð²¢w¦yRZ]=!¾áO<É¡OáÿZÎ¿×Hà:f9º î­N=÷*¿èC×?z¬.¯* ³
YrtÒ`Ð2çpFÚ_¸{¿º¹QÚaI¯æåe§}ÚtÚ½nöºgísj¬q
ô²ßîõÛÎ
°ù¨xr

```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/16/054d69a379f68790528174e7fc988198645997

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/16/054d69a379f68790528174e7fc988198645997 (latin-1)

```text
xRMoÓ@åì_1rÉ¨¡E Ô"ãºiT'®ÕÆÞ:«¬½ÖîºUúcø¸qÍcÖIH |ø²ë÷ÞÌ¼©S8zþòÕ^¦¢Î¼Y°jö :s¦J&ggÎ^HÈ<çeÞÁó·x1GÞCA«ý÷)Ñ;.Õ~¤¦Ê}ÏM:#Ý}»c¥ÑJjn¸,6Ô0Îh³á ,eZ/¿(.¡¢¢\3²(æäÏDÇ$ç7qDÎ£0Fð6Éð¢ß#WÄBâè}û§YËïSÐ©Tº¤2
5/@,¿å<¥àÍ.oP¾s±[¯`2ê a1ÞT¤µ °üZf<e GPÛáÊ&ó¼o[±­-ï*ú8®Éu2îOúÉpÏÞ}xúK¾gàY	ßqxi`×xÍ¬ ]µðj¿&¤d¶a*¥J¡Ó,óá³øYÀco|ÆÎÿYZiyÚ¨:5ð÷	A3xT[å±C-k­2lú&ãI0Hx{'7£0ÂÑAÜn2­vk¸®~'²S÷æº5¼`¸qEÜ9©+ûOrf<z\·c-UÌ êç5}áFÙºì¿ëyîÎ8 .&ÐÒ@M3ùn+k§Ý³­ÑöQs­ÌÝVm×Â[p«'à*&ÕÌEÞz£Ú?å¬±nÙx­UiSçÑù>àY7
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/1e4a937d43c98c1f8292da214c1cdf43915a51

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/1e4a937d43c98c1f8292da214c1cdf43915a51 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9«ÅÜ~.»Tär	«ÀÑ+cóóÒ2Óö^fàû:uãìÃ¼|·8¶±-*¨J-È¨,bX»ëÓÖ	[&ê^©ÌnèzVxGYË ²R[
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/bbd04371bc2991af23abd580c79bc9b0c9a97c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/bbd04371bc2991af23abd580c79bc9b0c9a97c (latin-1)

```text
xKÊÉOR06fPV(-QHÎÏKËL/-J,ÉÌÏSÈ/ QÅ
©E©\ Ñ4
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/2c6e54581ac98b385c4b0a6e16249b17d79793

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/2c6e54581ac98b385c4b0a6e16249b17d79793 (latin-1)

```text
xKÊÉOR04³dPÎLËKIMSòõu
÷qö÷àR
gæ¥báRÎÌKÎ)MIU°).IÉÌ+ÑË°CKÊÏÏ	r%JJâË3K3â3sKsKR5J2ñ%
Eùå:
0Nr~H¯BAQjqqj¦5rj^Jf 6Ý;2
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/35d6c42c4d43adc8fefcb5cb10f8b63b4419d3

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/9c/35d6c42c4d43adc8fefcb5cb10f8b63b4419d3 (latin-1)

```text
x+)JMU07a040031QHÎ/ÊKÕKÎÏKc³ûsáÍëW_m8>ûä+k ªÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  "i
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/26/7e034b5e20eca61f03537eb04fda9af2daec9e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/26/7e034b5e20eca61f03537eb04fda9af2daec9e (latin-1)

```text
xéRÛF¸¿ý2eìà!G3Ò1XPMIJ=î,­aÇ²äH2ØÉð0>J^¬ß·v%$Y»ß}ïhH^¿y[ûeï¹qJcæ1~Ïb°Qºëß|$ßÿHÂ'Ó¸çú.ñ¢	áaú¦äÅ^é9½`æ3òî+Þ-â½1CìÞ½_ÞòÙ=÷Øê­9'{(ÈJ òÕAt{ËÃÛ=x'cA&<õî¤Vy±4Ä$ºgtÍAZsú¡Ó¸n9´ë7¯zN·¼l¦*A¸óÉiÑfû¬rT*9¯ëÝÚ¢ÔM¹$i<óÒlWDcÒp>5OÚèÑs§WW»ÓpZõ§%8×*|O£(vÏÂ4nðÙ8zôÂ¹9éÔ»
R×öKÏ­ë+À;BÒÙhÄb)°t¦ü	G³QÿÍàHë 2hPtÜ¥(Ò1©­`ó)óRæ}C	vrÐé,vóÊ(îBO·o%^K§VSv$×C
áøhä8zXrÙlxQ°zc³$a¾Ù|$c¶0+Ù)Cúsõ²n-'^Ý¸Y ¨ÕÎÒÂÌp{$"®åÂãQ	þÐòg<°Ø!Á}Ö£Õíýxí\;ôªù·C^.è«ó´á5ÛLÒäöKÊÅWÊëÜX©x[Í£J^é(¿ë]oò]ÐÞ]§Þ W½úéÅ²°JökHAåaLSIÍÄ\ ¾ºÒ$=	i5#|íNtvÝGÜ·Â]/½nÈCýÃ«¾°\g½À=ÿpÇFÊû+~ÇÍIoYZÞ6rÛÞUrAÏ:]ðVMäðeÌ®Åfá¹I¾ffèHBpUåzÀ,pSY!Ë90\ !v!³ª¶!¿6m«,#(
$,GDúB-½3Dµ[¡©öëÔ)³ëÏ×	ªö÷uÿÔ¼T^çÂP÷ÝYæ
Ýês·]ÞrdëðYméyÜÉ¯µùVUùÒ×öB=Ea9u`+z i)òåí¦N èÆ±HOHºÆyRz÷^·¡¡5Ê4N"~G|ÁlãúeA|ÛQ!ïIÍN>"V1Ëú44²½M<ò~ÍëuõRÎØÙÛ#,2heÃEÊ Às»Aæ/0¶×jVïHBENî J¥È5·ÛÏ}aÞÙ@UVB®AY1n·¼u"G âQ=@+N¡U»~T%ÐñXê~´Uµ%²§#]ýåÞ¯að03e+èT
9Ø¤îÄ
ï"ed_=Ìj¢å ûû`«ãÜØTÄA.ky#<ß¯×ýjë ÕoÐ7è«J_^ãd6d"IåMöSâ¼-ãÏ}1èËZt£ü5è«òx²¡¼úÉ*N¡ç÷ßÿ
 x@¬xl(ªHm®ê±D1XºDH1bfHÍL¿
Øæ`BøåÂUY¥ä¯Ì^®A¾Â¡f09K#>y×äCõÀº`Ä²*Y´QnÖ§*.p¸åÿ¬Îé}1VÛ£(åpÈ»ý#x½³d±ÙÂ!÷wvüLòÏ±¾â0éÛ­Äe´L¥Ñ¨Èæ«(É`Y@eöÈêÐ¤»ª,Ê Ë Ëi¬å«þty¥Ñ%ó0qlFy°ÊKCØuñ#ás×:áÙ,7ß5ðÁwN
¬yx°)¢GågÚþF£Æ¾%F0BªäÆËz8,*ôªeÕÖuJ­­­AOÊFÇ"ÝàÊ£·äzõøõúJzCá|°,AQucâùZ¯¶+P},¹
ovâU¬pC3¼ÖPçéìÎ1íý\oö
£iá¶®YFk!ó9Ç##g.`)1s]ÝÈú4ÏÃM9ò¯®(]Ó*·#qvýW]âX©_Tÿ¼N¢<³ìÂL«¹ñ0êì+¨0BW¸þÂ¶ ØsÒÊB=¡âi6XS
K»¦zpâm_·ZÊexNYèfÐ DD>S¤J}ºµNå6y¶Ï½Âµ ÞStÎO*P+Ëg0Ä·üÇ!uI õÉý_Éù÷*©áÙÛÄ¬ CÀU`yKPÏ¼*îøÐµÄB ««[
ÈlK%Y$t)ÌQönÅä¯n®@fÏ2G¤WIýò²Õ<­÷vvÚgÍsj­	
ô²Ûìt½`ó?AÛ|ß
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/82/7e0a65365b824b52fde2e211a8abbb5a88ad50

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/82/7e0a65365b824b52fde2e211a8abbb5a88ad50 (latin-1)

```text
x}ÍnÓ@Ç9û)TZÚRRSEÍG
¸¬6ö6YÅÞÖëöa8õÄ	qácÆö&)Aõ!ï|þ;ÅzûomIÆY$àÝ­MnÌÞT%âÝÉ±·áõx,Õxßÿø)æÝ$|¶y>>Úlz2n,K¯¥
'äôºÖ´?uÖZÝæ0ðoi
ZþÇÎ	ûÚ;eÒ
.nõÈóöö -®¤â A-þ$Âh@!¡3ÅS8¤[#o!^üËßÒ¨°à"«ÞVDuôÃÎgÖtÏÑwhñ8Ìbj±ø©"
1à0Ãù¥¡¾Ñ×5*·*EÓ_zÍ3v68ï\týUødWaçQÇàSªçIeaKe3XágèyË,äýÜ&Õ`¤u3#ÒTDUøî>. æ7Â äWÎÜ¹g«Å¯KËºf:ÅoTóÅXF<uiò*×
Ç
x
ww$ì5n®7ö .,ýJGÍ9\¼ZÕIGc;ÊÑá»R+#×ªa3£àeÐé_6»K×}!d ê¢Ô'ñB­R©5Yh7¹Ue#W­Æ°ãF>
BqÅª³±°,Gëâ·LFßüü°¶vR	Þó²¢ÃDçKF}
®áÎTÜOx¶£ê&JýÊºÜ°â·Q.ÛuR(XÞ]#ëÌÚÊke"RË²lFßDÇ¯A÷ 6Å1êm\3=¢_"¨ó!Ær©k'Xí'~eíÿÛé:*h/Ù#:\*f±­£]YMMzËÒð*¹Y:TOÅðÕUR-[îfÉ_GÞ½÷'â©ì
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cb/11913c5041ebe0b343ed2d759a58fa0e81232c

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cb/11913c5041ebe0b343ed2d759a58fa0e81232c (latin-1)

```text
xTÍnÛFîO1HQJÉ?hPÄM Åf!eØNöB¬È±´ÐrØÆ²ácÞ¢¢ò½êMú$]lEÊÃr83;ùæ
5ý/øËL¸á×[,çKÝç²t¶>{ó7ÑûµD±Ó$ÔlÆå¬Oïö+¡7m-}Ç´MU!Î`ªùlnhÝÌgn³ùÆåQ(¬PR,&ÙõÓÁlúõoL)¸M< ßþøR£è¬£¢Ñä4ON>ô$9
.ø¶Xtáxrönxþ>~zQò1u¨¾¯¹D®.ÒãÉèöÖjïÿ>ùm<8OÏ'Ã«áä,Öês2%:{¹ÏÜ~±7v¢²|çäêëê/ÌÝpÁi(+/»ÅL00¼påâ§nªÌ¸Lt"cåTç`Pæé±ãÒþZ©´!¥»àÐ§¦uhÛ4k}¬vØ9ªÑ<×hL¸ºH#Ëø`ðùî`×L¾@Ìàp÷Êó [ãR®þ
±¸ÃxAôP+ðáC
®!.QórÚcD3E¸:Ã$9µt j}ÃÔ-
ùæ%³«o
/uªÃÞÏ½½ÅêGn
ácªÇ
îùM7Tçáyú´NËïp2VB¤ÿÃõ?Ýraê¬UÒtà.
zÎ¼=íàWß¼þ)|éÏ&¥ iÓóú&&ÏFhÐÕîúâZ"]ØAT3°nRæU¿¥öCÄÌìîÞÑÃk*ª½ßÐ÷v;zùÒk¶ íµ¾7´V«­vËÚäOÆFªm÷z?ËÊ($~¹Á¸^nÔ«?iÞ4¥ÒÖóØß	$öÒã÷­¤³«ôb0¼Lb¬üròBlÒ,WÀeN³¢Á¸æUònÈ5[ 
_0õ©¸qa>ê8ëõ±ßý6¾Fë´½£è>ú°
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/cb/c4bd44b390ed77b23d1e464a33cef77f9e421a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/cb/c4bd44b390ed77b23d1e464a33cef77f9e421a (latin-1)

```text
xÁ
Â0 yg
/ rìÔ!BLÀ§Û¸¥iPîOWà{Òn¨¥Ì
èÔV3ÈIcÔ B)"yÎ}Ð5qÇQ½]Í{r_]mi`³äÁPÂà%dÌ!YÇG&Hî{S 4§{{×^u_á©Åà¶ÙTó\êc*:.C-wðQ|dÏ,pFFt=þýoºf[380îû9yE"
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f5/24e23890c0ab1fc2993cf0c02a92bc464ac0e8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f5/24e23890c0ab1fc2993cf0c02a92bc464ac0e8 (latin-1)

```text
xSÑÔ0õ¹_qYZlwÙuÝ©Øu@ÐEBÚÜé¦IIa;²ÿnÚifªVÑ>¤é='çsIs¡r¸LË'O¹,e/Øì:sÙXs\ï^¿ájbª,¹,c÷Åîy=4­«ØRmH­öèÛ"Ñ¼ÜîQ:"´DýK'3Àm|ÔhÁ
J3JGtd¢ö¾&i@FævHd5¹ß¬>e)Y¥wÙëix¨«Üm>¼}·&_îß¥Ó,º	.
Ìò` þøxR÷¤¶ÐJòÔ¿¶¶cïÜ£dÁ÷`0ÚÇ[½Y³±®] ÛgX×¯£¥¡âíõõQÓm/~æ¦á.NO;WóFÜTûyy
í¢ìëÕ7¸uý(dyÖGv4÷¹8Ù©èýÎøXghô6t
NoTo»pôêRñª­ÿúÒcØ4Wkàñjhmm« P5ØÁBPØÒ
Á	h
Ãí=o-×é¯m.¸¬HCq¿kx¹«ÄwÒh¬ÜÁg9
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f5/13dae2f5ab8a5e5a71eb3d42c7ffa960556a1a

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f5/13dae2f5ab8a5e5a71eb3d42c7ffa960556a1a (latin-1)

```text
x+)JMU0´4a040031Q(M,*ÏÍ/K¥Å©ñ9©i%z¿µgÛçsªûâøù×vOþ.WÅ¡£(3=¤åÒÎKµÏ~v×?èæþiñíã d-Åå%É0æqvy»=kó¤Þúö²£'¬1U
Á¢fxÏ¦s¾Ý<µó^çWÞc	7 ò7W
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/f5/f819483167673be4167c8c69ccaacae70ec2aa

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/f5/f819483167673be4167c8c69ccaacae70ec2aa (latin-1)

```text
xI
1 =çý%{2 â¼{ìNºuÀÿ;_ðTPPP¥·¶N°&æ`¨.u$ÃN¼dJ"1xô®R@RüPõÕJ²L+W²fIäJ¹èb9;nóÙÜû6àáüåG¯kë×GÃõu*½]À¤àõqpÔNkµÛýoòÿ¥µ±úDq
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/53/b86109648e7dc9099c94a4f863e5c5cbc7c552

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/53/b86109648e7dc9099c94a4f863e5c5cbc7c552 (latin-1)

```text
x+)JMU0´4`040031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×PTe§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ãíÿ7>ËO­±åeºÞóµ6é´ºµ(%3ôrÎº³17^®»¼Òc» Ï:a{¨Yå©Å%z¹9Ç4¯y#_íYÙÁµ_?ó1  õR1
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/53/aa34f8a632b90ee034ddf0a38e4e874be152a8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/53/aa34f8a632b90ee034ddf0a38e4e874be152a8 (latin-1)

```text
xA
Â0 =çû%&Û/=DÐÛ6ÙÔBc¤ÿ·>ÁãL(9¬¥UDÀÎ ¼¨wØlm=	û)ÖLzó$¯
ÎEÒØs#;¦`I²»ê³Lp/	.ö³ô%¹ûÌÃ¸	%À #D´a­·Z«Å.Uþ/U¹Âã|öÖ^®xúÉH:
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/53/a3699aaa4f89b04f05d0ba3bd3921833854175

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/53/a3699aaa4f89b04f05d0ba3bd3921833854175 (latin-1)

```text
xTÁÚ0í¯m.ímÙRµxµHìÈqv/VhsX	
i¿§§zê'ðcBì¥¨ÐÌó7ÏÏY®º%L>OßPtû]í¦Y®ÚI"EÊ3ó\ÌM)¹Ð\dá«[-d]!p ¥TÚè§Í "TÙlØ¨ôÓÃÙ=¼¯#¥¿ C»Ývðµ[+¢#eG¹;Ä3$ªKmâW RTÉÃÍÄU\9×þ}É(ÂV4lsuÄÄcÛ$©|DBVátTj}rÈFÔ8O¨ÔTZ*$b)Ïe¥ÂL¡Õå³ÑÐñ¬¥¯«ØYèbÍÙýÿc)æøËH
wDüÞíõ·u¾?gTO=XzÉ É1<AÚ*Jæ£XÛIXb¢¤ðgx©$«Þ$  ðÎÙÞaækJ ¶^KEO¹=BåÌK)HaÕ¹69.0?§®3 f©ôdh©(uÈÜÙ%¦åQ0cmrö½ÔèÇË¡ÖÇ?ßö«Sì7Çßvõfrï»Â)ãÊ®wÚâZ7<ìÃ×°ÎÜlÚ`»ÍÉ5«»­Ë/uÿí ¦/ëÖøÄðõÂG oÑ÷ýË®ÝíðFÝ¦Ð¦DyÖ°ØFcÕÛ?# ·tujLþ³oJ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0e/7f0c8b46d91e0dc427e091cbada0a76f29c21e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0e/7f0c8b46d91e0dc427e091cbada0a76f29c21e (latin-1)

```text
xInÃ0 sÖ+øµP"/È½§h×5¶Ü÷Ç_èuLnµÎÈS_UÁEäJ±¥ædiÈÖ+~sH1ê¨<o~eÕg<¨JæB´9ï	£w!ÄÌÅsFkdï?m¯¶¯pªpÙtje®í:UÜê'X> [B8£C4=þºþß4ã¼ý;FÛG
÷ºM/ó³IE
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0e/7d85964cef289b8b169743f2a0e60578b26ac6

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0e/7d85964cef289b8b169743f2a0e60578b26ac6 (latin-1)

```text
xmk0Ç÷:âè(X)c²®im)³Êº{|ÔDb2´cß½ÑÕ²ç-/î.¹_î.ÿ9áúj|vNY«Àíi#¬Fòô}Iå<I(K,í?åÌR¸àÏDU,hÊC¿Äk¾ó\<wg³u}0ó7Õ?­ïqxî£ë&Q&áÛjÎ±¸6ü´z¦ù©"Áóÿü­¯:6U#xAÝNIXP-JA¼8µ$"!ÕQ¶¬6c°nõ³}87úÍÓalBÜt®üýæ
8¶ÚõÐ¾¬EÐÂé
&ô×O>ïçÖÐJ+T=A¯è ÿÀ¡,
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0e/501c6c418be9cf92d3e1ffe1592b8c35f361c2

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0e/501c6c418be9cf92d3e1ffe1592b8c35f361c2 (latin-1)

```text
xÎAn!@Ñ®9/ÐRTõ Uö]0	RÁé¢§Ï\¡Û/=égí½màÞ¶)b¥×LìøBvuQÃ«_Ñ<xÊ8 VÇ©fdâÅyÒºV¡ñl9ZrïÛ]'|ë>áÊ]àòÖõóÖ¹ý²öÀs<wë­5G=þ6ù¿4]÷§@ÝGn:x¡ðÙº´Éð+æÖ#NÏ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/22/9d0ecdd1c4b4eaeb2ec95867ab6be98e84f91b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/22/9d0ecdd1c4b4eaeb2ec95867ab6be98e84f91b (latin-1)

```text
x}ÛnÓ@¹öS©"­iÚrå 
¢æPZ	nV{¬b{Íz@§àÅõ¡
Tª/¼ëùçøZÂåÅUûÕL(zL7{ÝÚ¢N0:ß¼wIZ¯e²nÑùo)nô¹}±J[å4%¬Äyö M°)ÔÉ|Ä§óáÝÄçCÿz2Xøìo=¸Ï>GüÛô[ïOÜ®ã´Zp!*@ä#Ñj¹ßsRVÐëA~WäÒKkÌRÐÀBÁßI(P@,(§pÎB\ÉÁ¼ñ¿N·üvþyüe<Ù^1ËÄ¼»âÆµf·¨åR1f«¹C*LÉ3ç0XÄµ¹"Mb?(È¥R¤Ôe¡? §vÄ5ôá¢ûh¶Å!U4R%$½Ø11³éd2£óÀ æõøRd
oêK¿ÐK*|-Ô~\.Ã¬0zmØÝØ:rìu©ÅÚíýÅ5f
êBÂ k^3t^IÅ",ç´1M®xëg÷Ii?e^ãiå»_Ñ´éÎkeëE»ýe}õT#cÌS"½åyj¿-æNÇzr*J×?xe²SôËW3³êôÊþ_µõr:KiøqÄ'?43x"ÕfH´ª0ø âÚ44F(2<IXÑTD+tt£óKIö
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e9/9a9f646d04ece557eed982f1ca8dbe096aef4e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e9/9a9f646d04ece557eed982f1ca8dbe096aef4e (latin-1)

```text
xSKnÛ0íZ§&¥PüKÒ°
§êØåI7-ÑtIÊùÙö ½AÑEâô$J«|ÜÖÐÂß¼yïi.ÔÚí×/v¹E0x{Ãéµn^0-h¤ï½ÚQvÑd+&-É¨¤çL?=¾`×]>­ÏYJW\=¼±sS&þ%Ê
#ÆRËHRyÎFºó@Nµ%æÛ8%-¬åí&lÁ%ãîlþxA»ãyÇ°R<ÃdBsißZ]P½ÄJìÁWðW`xÇÇòØÕ9Û;,Ú·-ýNë¾ò? *Ìó·ÚÈb[Sq¯àÆ2É´+i,8ÑJC,¼biµ@yhc\ö<#,ö¯àPC¶(ï#^¹àF¸V ¸"4ÊÇt}·þ©àKÎÀT9HC¯Ð/ÀÉV1§î­@§D;_ß¾C±UÜuÍÙ\Kø|ü>á3ÍHï¤×Jj¨ÕÌv ísXÇ\­°D87jF³Áh0õ?Øb
ÊånG'½¨?
'³p<Ú°EtðPÞýý}8Rz}G!Ï*aðã´íw*Ï²®«
¸K;t¶ùÒw¯TÿG$»ÄaÊô;=É¾·äZÁÄZ	A\_ëiÙu×ËóÜZLìê-.ê&Î:[§Ý0ø%ÇÁ;à ´µ¯äë©S4Å!Ö¢Åê½Ç­CÎ"Â_(îd2û]çR ýñè(ü@jµâ
LÃñ4!¡ß|U«
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/e9/bb7e046607e728162bdaa0e3ecf31185173381

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/e9/bb7e046607e728162bdaa0e3ecf31185173381 (latin-1)

```text
x+)JMU023c01 Ô²Ô¼b41Þ~¹-ü÷jòô@ÙÐÀÀÌÄD!'5%>%5©4]/A¹KK¾Oã'ïöè/)ÌM.A&Äçæ¥ÒâÔøÔ´ ßÚ³ís¹LÕ}qüük»'IÆ«âÐQÒriç¥Úg?»ëtsÿ´øöÁñO²âòÌäó8»¼ÝµÌyRo}{ÙÑÉÖª`Q
3¼ÊgÓ9ßnÚy¯ó+ï±ÂÇÌ¼pÞ
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a4/03191a8f722ea798bd88645c031b15b2bd5658

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a4/03191a8f722ea798bd88645c031b15b2bd5658 (latin-1)

```text
xuRíj£@íoâÖ¥`´iÙ?ÙÚÔ©1K>º°ãÜU©	ãDbK¦ÏÒÛ;¡IôÜ{î¹ç¸(ä~^þ8ú¤Xs_O¸ÊjÕ}D%°8ÏÎTÈ4ÍEÚ¥ó¾|ìbB³e,âÕ.å|÷#
¾¹Ðå'È}":ºÙR®Kd¥5²$EÄá:N8¾c£ñÍ<ôÙ?¯&¾Gå£ÛàýÝ3Sú~xÚsÃ'@@}¬^"E©ÁÌ´khøÙ)<;@K­Ö­Ù£ê+èC\²Â=âë5tù?ð±Ú²	FíIä¹¾1QÒêíµÈ¹tÛS¤P¯Ëòâ4d¦3n=wd¼¥¬ø¦Â×ôt;ÕÙoÚ³6v²ÛP2­'
WRÑêíÙo1pl¼V};,$¯Ï9ÛvÕø®·pmáÆîíÀJúv4Zß§¥péÌü÷1"/5
TdÓ;_Oà÷,Gú$HÿZû5
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/a4/b0b95d29906d25d50759c227a5558082d4a94f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/a4/b0b95d29906d25d50759c227a5558082d4a94f (latin-1)

```text
x}SËnÛ0ìY_±u@	+
z(êØ@ë(Q?;)^J¢%Á4)P!¥è×ôSúc]`¹vyác³»ÃaÀe ïo?||ó.!/"w¯,K*åm±óOË8NEìá|ßm=¶gB4fªî½¶áÜÃ%ÙÉ"g$×T3&TÄ,$½Ãt/¢L¦Bçª;C¤ïU]îYCÏÙF#
<dÇQÆ	!b#ÕN#é8³å#/ï_f>¹÷'³Ï+ßÅ},ÓGòcþÈÌÿæÏ.ôÊy@Ã-dTQÐjª VCæÂÖí:¦Ý4ìÈ4ýó4×L0EÂÀÅbr
F!«¥+\ÂOpØ`®UZÌ	¿ÐÙE>,ÚðaáéÜ·lßfÀ3Óp34Û?¿%0ì. Ó×y[ÌÜ@Ü/Kj¤.ÜÞÜ<±½ý	¢rtõ!ªê)ät6Z££òâæö{¯_f°ýõ8*ûv®ìÜRuv
¦!;h÷ÅßY±L*
1þ ÊMCø¦u¦mÑaôU3êç1á»#ÛÛf²Ûëq £jÒø.¶aìU¡ª¨¶ß«Ýþ[v±å	l£©ÀÖØ4F1EO`¬vfû-I?ôµðÒÐAcÔfº~öþÊ=tmëýþ¹Ëë/ëÉjúô<].Îñ;üïâ£
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/8d/15099adcb16d5f1e740b777948b7114cae133f

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/8d/15099adcb16d5f1e740b777948b7114cae133f (latin-1)

```text
x+)JMU°0e040031QpöMÌNõÉ,.)Ö+©(a¨>:OyÝ½ob>Z<fþJæR%TeibQI|QjrjfYj^2ÃßâÙÕWî|:Áóå»Ý÷ý gÆ(\
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/fd/7378d1e107835327a9b9e59049e9eebbdee6fc

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/fd/7378d1e107835327a9b9e59049e9eebbdee6fc (latin-1)

```text
xVïnÛ6ßg?Å­C¹b9m¶bY
h¶	qmÃV2t[@ÈV$U¢²¸C¦²Û)Ê²ã>XyüÝÝïþyd8yûîôïD%UÌá§Ï<_mÞ)OWï;Ïbþ "~ø¨¼({w¹ÈþU 
yP@¤âðA¹){y!R¹¦{m«î×½õnÌ"å0òl<z0;òÝ¹ðØévJJA¥¥RU$le±deÎ#@18Ë©?axu>õìÒ,g+é²{Ö9¥WäÂ½àaàL¹?{#$n§BÏÞ1	jùûÛ3»´Åò¬D@g«·6~ÍJ~ÆâPôuÖ¹bÁ/3Ï²yà®ØÐ»ðÇ1ÀÐÿhmÃiÿU×d4HrUð0&
^*HTù	½½HDº®-µû*´A/fu;u ?W"á`õ» ¿iOÙËd¸æÖÑÕ6\±ÉÌ»ñfhÒ£býB¥uÆÙÐoI `Âyn]±so`õÅª¾ýµûN}ÿ©óÔÄQ9¡,ÖN~ âÛ¸X¼PäWMô"dt×®+¼¥XfµÂQDÀ{pÚ¼PØë8¿~}¡6H&`5IpoÚéÜhç<Lnr èÜôzà<:}ÜÊ^6}9øUð%o¸n#­ù&Ê°h>ÁàHæ Ïæ-øúþ¸Ýg±X
l	5ÔB ôï/TeggðôS¦2Óô)mø£ëÝzqíÎA¹wþ26F;/G@e½þ#}ak9EmDmÒ`ìw,%rÛÄa![ûEï×
S4Z5­TÜ·zJt,EÑ®=Á'àIÉUhißÉj´×aûúçY"¿®y[Fa;y`e­J¬ÄA?vÙÔõ}S`¯¾÷ÜoÒz1àI­TUnË±à§¡Âh2¨¦c"÷­®N&JUbêrÇP²Û ñÛ8ºCÓÒLbñf74Uj´9MBâ®*ø¶©91¹¦×óÇî ðo<_­£pÐ2Êðÿe¢J³­Ùï¦nJLµ!Q|bQ$ ¬i`ÔXÕ0²õ°¯G£:\ÍÍâñ4\$\	Í,`R)1ä{³ÃVÃ¤:{SiîÿæM.¶S©k7y`òÞØ;Ú¼ß÷~À>G3e<a¿º~`,6 øÕ©È`$2Ý¾&	ñ_ÈóDÜQá¨ùÓéD9 ósÌ?PbºÖym mp§Ó?p2¶a0_ø¬µ§.³éÌÌüà#jø
Úë%
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ea/4c2e8997ed737860b8a72af7d1c2d1cf75ae42

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ea/4c2e8997ed737860b8a72af7d1c2d1cf75ae42 (latin-1)

```text
xÅVkSÓ@õsÅOÄ1MBÙ¤øÀFÉPZ¦
:(úÛ½÷Ül¶Î8îtÎÞ÷nîîm§7è¨ÕòÚÒRA-){pv1L>§êÞÑ}U)WÊ*:ÕAc\ýttÎÓÁpD¡úÎ~Q'Gq½nÜOOI<|®^DþR¡p+éõÎ»±zÑÛ_Ê]î¦£äeÎÓM¤ßMúG¥o§'¥øb´|ü»NÊþBI}/¨lPÒiû,g0£ÁéY;M:½Xm¨ªÿPBÖãdÛ?µÏ{éa¯}©V©¤ÿjpñK¥"«ÊÓbÜºÀ Ù÷R¶JÜúÕÐ·Õ¥Ô´£@swtÀ#ê^KÍ-(¸¼Ë©Ö7#Î8chwU G4!5¤æC(ËÀ£r×¼b\ªZË£ ½âPÆmòÚAÆX¹3ÕÌE¢³~ÁA'gh±H;Ð÷.0,ò
4ê1§Q33õê´ÜmS]£Ý`!(:ÀM õsHÝæ`êvf¦Ãº
O"Ø4úÎñpímà.¹	¤¶s°½ÝhÈníÍPËòt \|fpææ/Ô
2Bß²©áª§"Á5¤äËõ9×ySoð5þ­à&V«À5à# ]2õÒàSà3`1Ï²jdëLÑ
;¢
p¸|DÈIÌqö¬·|Â .Á®ÍlìàX}
¯¶NÇýcRxcbý[áv4©Ç|§ÔêB(ÔøBýÏ²è¤Oe¢³ÈeÆDì¤tt"jQÄÐÕb&
ÝêBy¢¬æÞØàÒ±±àlÓÉ±@GÇSàÕêäIíþ(¦Ùj|¼Uª%×RrYãô©sÅ>Ç9YoñYLò\ºD°Çð,øL¢üdó°\ösÛ¶Qüxìx¼¼
¼db~´\ÞÞgÌóÞ¼®Ô§ß|EDl ßßß?réÇõÏ%ú øøqár7óÓ¤yv·íóo«X¯Ï{y[ùv¸û¶ÆÅ±6u+ÇÑLJðÞq¹]¶'¬VÃ§(ì·Â(Ø¤}KR#yNqÙkx5KYÆð§¡jÃk¶äqvwZlVW·øSÕ%ªæ¥¬Ö®;MíÙÚ³:2ÛÊm57û|M«ËçUú$Äïùò$ò´E±í+ãå­6k±ÅÐe»¹­Àv}öÕéý¦ß/Â¢
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ea/5d06b80a55b8b93aea9a6bbdd2b81434b6f2f9

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ea/5d06b80a55b8b93aea9a6bbdd2b81434b6f2f9 (latin-1)

```text
x+)JMU064e01 Ô²Ô¼b41Þ~¹-ü÷jòô@ÙÐÀÀÌÄD!'5%>%5©4]/A¹KK¾Oã'ïöè/)ÌM.AädÄçæ§Æ§e&§5eqWØÖ¸©h443­ßß$uþ?TCibH}Y*TSNjZ	PÇoíÙö¹Ç\¦ê¾8~þµÝ¤¿ãUqè(ÊLÏ i¹´óRí³ÝõÆº¹Z|ûàøÇ'YKqyfIrF<Ôy]ÞnÏZæ<©·¾½ìèä	kLUC°¨^å³iÆo7OGí¼×ù÷XBá
Åã 6Ù
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ce/d215df91eacea3ae7c51f01f6d5a65aa53c588

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ce/d215df91eacea3ae7c51f01f6d5a65aa53c588 (latin-1)

```text
xÎKND!@QÇ¬¢6 )þt+pî°¢%i^uhWooÁéMNr«Ì96ç_öbä¹½FSac2§+×R0%4{ÑêN
\Lc1wvÑå¬{EÛ] Ó¦z§jû[|É¹à&ÃåÁWicÊÇuÒ¸½Uï cÐÙzë2¼¢ETÏúüÛü©¦0,èçQt4ûÇ"øá_õ1BN@
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ce/12e78e8ebd7642cfb539acb2376e3bc8c170f4

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ce/12e78e8ebd7642cfb539acb2376e3bc8c170f4 (latin-1)

```text
xÎMj1@á¬}
] A¶Jé	ºïÒúi:ãäü+dûàÁ'Þû6!e:ÍaD¥1[AáªÙµâ4/ÊK¤VSÌá¯
Û'¬5ªH.Ì°TÎ+/¢¬J"!í1}À·?|µnð~·«ëÖýóÚÛv;÷K°¼aFG=|Ó^?Ã´û4±µ]v:Øó0{ø{¹K
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ce/fadd8ee673850bb0c4538574a5dd6055846b3b

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ce/fadd8ee673850bb0c4538574a5dd6055846b3b (latin-1)

```text
x}U]oÚ0Ý3¿â¶ª¤Ê
lÚÖUÊ °FªîÅ2)!ÉÓ­úcª=ìðÇví
.ì{¯Ï9÷\3Ó	Ôß}|óâ%2p<æRL£IBÎaI¥"3.n¸<cÀsµzÀ
½ÍÒE&b¥GÇÊK°xq8¿ãÙìVVç\&<>]<Ýø`üðÔåÕëL¤ÿ
ÐÀDè
jÎ_AØó|õ E
WCâ÷üÐ²tÄ§"áÐõ¤4=hÄíúîÐyT³+¹¢J0$ä
r%LFF"Eò3À0øí¾Lö½i{¡UÖsLtnªì(øÃ©æéMoì7<]@çâÒu¿x]KGÔlÌ/¡¬AÌIÎEs"ª¨þ1~xnC·Ñ!M¯å÷<M 6wàmý5ÖZ³ÚR3Éi¤¹âèXï&Åò$É|½iÕSê@ñ2)_]ù]|~ÎDÌÁªÛPüÖk0QtÎ­ã©¶Ò
ÞØ 4ª#r&$¦PlëÁ9PßÀ1çÕ!ß^Ãª×LEösùµuþ}å~#¨!a±u°KØ­â2çÒSR]D} 
ª¥Ï^S7õ¦bâèÐÈ2N& P{ªË5~Om¨ËI$Úå¦%1ë¨0¹9÷V·þ,K¥²m\-eR(¼QùNÅõRòGQØ8&n#ôÇb1ì¡¹nÕ7E·
Æýn×60#?£q<AÀºñÆýNár6ëºÝµ,LùðNbnK ¥W	CýJ»çmÇ}={S3ô¿{AëqjlÇ`-U~ëÛcQÀÛù<÷Þ 3N.]?DÄèE¼ª.%Í2.wï¨rTÑe»71ÉoóÂÏY¶ô;hQo4ôÚÛòízi½SØj%¬Æ.(P.ÕßÕ(¸PÀî2AcqG
ý!rÅ´²¹bM6çpûý®ßpC?è9Ðz-¿M¶ÖÌýLú?øá"û 9 ï
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/0c/d0f189d0dda6128623d81d0b5a08202885b16e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/0c/d0f189d0dda6128623d81d0b5a08202885b16e (latin-1)

```text
x+)JMU022g01 Ô²Ô¼b÷Õ[ZorÊ^ú·¿P3ú×lC3ÒÄ¢øÜü²T QZV¢Áüõå£ëÍV6ïfWØ>ÁWCGQfzHK£é;¾G/2*§Väú÷ÔYKqyfIrÌy]ÞnÏZæ<©·¾½ìèä	kLUC°¨^å³iÆo7OGí¼×ù÷XBá
Åã ?a®
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/81/0c21f9403d7f6e4f5e24df0d8d1f1ac37f59a8

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/81/0c21f9403d7f6e4f5e24df0d8d1f1ac37f59a8 (latin-1)

```text
x+)JMU043`040031QHÎ/ÊKÕKÎÏKcX¬¦À¦ºrkªú¯LËy±ÓeÝPTe§Væ&0Hæ÷½º³ß«ÕDeNWÙZþbyÕÅç¤¦èå¥å$V2Ytíaözû²ZÙoô=ÏØ¼ªº<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 ¨@
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/81/35ee0ee2e868e335236631786f53c75afee536

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/81/35ee0ee2e868e335236631786f53c75afee536 (latin-1)

```text
xUA
Â0E]Ï)ºW´W	M:ØÒ$&hïnÝäïÞçñ\`×{ê²ï8 'O Ý|¨#áóCyÚä²$
çéPTªW\Y¡Ì¢øÜ7'}XÅq5
n
/mã<ÌºúÛ^rUS1ðCkóà
ü:¥
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/2d/bcaeaa08200693258eecbc66122c2136badd96

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/2d/bcaeaa08200693258eecbc66122c2136badd96 (latin-1)

```text
x+)JMU02°`01 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ùcòRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLgàÔ¼1ÍØsÒµÆ8çMc2<.	QPZQYÄ°v×§­¶LÔ½RÝÐõ¬ð²' fRï
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/02/3954ff2c601c437c80e312c84c4ee93eb8b1af

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/02/3954ff2c601c437c80e312c84c4ee93eb8b1af (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^ûBkÖç§Ü)[ñîÐº¢"l²ÇL¥ùe©E9]_ÕNáøtfî½CËüÞÏMÙ¢º(3=jrðâÌY«ü;7ø³^Øe}yq«c)µ0£Ã]^zÜÚ{øâ»0cçsî9ddb 
yÉ9¥)©ñé¾Fí¼+g¡¶¬È¡3Vy>DEqQ2C¾XÞ{ÿÕÿú8ëâys¨uå©Å%z¹9Ç4¯y#_íYÙÁµ_?ó1  æ¿
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/ef/74adcfbc849cecfeb186c9c756baca524d1d49

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/ef/74adcfbc849cecfeb186c9c756baca524d1d49 (latin-1)

```text
x+)JMU06`01 ªÜl*Í3Çî,ÊÛñöo¸àgÏÖe©SÝ ;
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/7ffabc94b8417a233ce4e0e9eab892c471aac1

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/7ffabc94b8417a233ce4e0e9eab892c471aac1 (latin-1)

```text
x+)JMU062`040031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VY]|NjZ^r~^C] ½SÜt+ç'R~øy'¶^Ý©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨Ée7ÝPÛý´øÕ¦¹íº%éXÔÂv_ÁÁÄ.èsâ´gÖÿSW¸Ï¾ñÁÄ 2ósJSR4Pxù¨ÆYdù;SçuÉ³¥oCT%3¨?-;â s~»­ïÎ;éÖµ®<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 
8
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/6b5717b08d1c5cdf6349d4ac2e13b1da5c11ec

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/6b5717b08d1c5cdf6349d4ac2e13b1da5c11ec (latin-1)

```text
xuRÛnÓ@åÙ_1**r"§Q%ÒPÕ!REQáÅ²½ÓdÛöRÅEý¾ñù1f§\û°;93sæÌfÊ`øløè±¬òÂ	w¸ZÔ:\¢®°è-^y{¡BÍç²ôþ/áB}'Vb¥deÍ~È¥Ú&¥ºEºAxa·ëA¢êV¦àJ °,±²
¼_Qm1ïÎÇ°Ju

rÂé´èQ®ñÝ%5Ñ*O·u*(×
®Áz4x)ÐÝá¤úßþ9kUe`ºùfr&C3e7?ÐI{#±àúÁ
¼±ÈÒr¾ óÌR
Q`C¤á¢Ñ:]A°ãr4FïBÎ·@­=/Mél|GÉ8:O/#ÿ®\p6{ÿö||^$£QÜ9ñ<Ú´úôÍ|ò
K°3ë \k·3và«tÕ.·@MÚûvÆ¢fJÔ°µi°-sz;FÐZAS«dM`jþ»«fWÝxî59iCîýð½Cæ4ü'[
4.çñøã7ÿàêôòCûøóQËÑ¡ .|·´FýõapÍ}È{ðb}	³Q,)ÇÚ¥ÑsâÝ{?÷G
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/64d0bc3dd917926892c55e3706cc116d5b165e

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/64d0bc3dd917926892c55e3706cc116d5b165e (latin-1)

```text
x+)JMU06c040031QÐKÏ,ÉNM-`x6÷ÑìM¯9{wk®+ºqèIOðD [¨
```


## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/f246210ca98f822587b2e660f08de23bb1aafa

```text
## arquivo: /home/segodimo/zmkpromicro/.git/objects/d5/f246210ca98f822587b2e660f08de23bb1aafa (latin-1)

```text
xVÝnÛ6Þµâ4E¹;í°¡i;h	õl×vºuAÈpVDÒ¦CfÃ.öy±C²ü³Ó%ç÷;ßá<sxv|Üùê±H£¤9¼üÌ³ë;u´ä*åÉáõëÖÖVÌoEÄwo)qËU~t	ùE2TÅNÝù]~)Ës7Ë#ÒÆò¢®i³õ8ærèû§l0<õátÊ¼~àMÇv+/ÂBDÉ4/ /T@.³Õd<Wp>
NF~ûSÇêsµtÞ>iíTeOÈ-Tsê¿z>)"ø"úÞ÷~ß!NôÁ(dÁáÂO_ÀeççÍ.ù-OVÜe|v©äÇÙe$5Zb6¾eÌËÅåóÙ]ÆUZbÌÑzÇ(÷)Ì¢T!d!þê&üÌÓP¶ µUT S¡ÓYYß[5µòçdm}[_@?OZ÷ÆöH¶ÌÅÃ_ÐíTæscßÖRÀüwþ`ÊÞ^ø>¿ø(ÝzÃ~¿e§þY0ðuöñè&¿úàB.>s¹pvÑvµ-¥.<¯²?)Âh	kÅÃØd)S2ây^gÉ¸BÈ#\0tjúÃØ÷NÙdêõÞXçBq-]øº{F*ÐUÎ-YeäÌ'Ã"ÄÝJÙ<©sôêÐó1·Q»eJ´#j]TI%üx-N·]Öu> AõøPr(o,$x^ðßBEÉôáï[h=tnÉ(áìÎA-¦
º$.¼agÃ1VqL¦SôÌ¥L SUÝbZôp*xýÔé6N¦wöL_ìçàìÇî~Üþ5ÝskMßÁÞîÁØó9Çm£Ái?èqð4ñ³×è<P<âsËèçáÏ~çøçõY®uTº6±·l×©M'Ð4ôÅrqS&aÁ]®×ñ6bpHÍKè4+KnÙð|¥$Ût+(x
ÙLã.c
÷«úOø	ùH 7D(|øóá	±¬ÀSG©i5)Ëyôê °]è6/Yp9ÔÛ~Ïév4!Úí>ß©Îß·Ðµª±t_èTFsgÚ-ãÛvMs¥ûÍv%¸h½[´¾XHF¬àh
 ¯×ñ®P<a~4,a¢QTgUS3" GyÏÛ,ÆP´ä+¼6ê@_izút ²Sâ6Ì<ßÔü¯TzØôÓ{­=õ°éÎ¶ðt<N~ïÚÆÎ«¶Íê|zô¶qRz+BdW
KYM,XàY¤0+&ÊÊ/3Ñ`È~òi[çz3dÙöUÑ5á#ðiøJÛ(<#1jâù!jÑßºî8xÇÜ@6\ÕÝë/ì¤èjÅè~¤g.%áA8¹é]s3©v3T"unÕ©$
ã;©ÑÈ'¥J
î;u"(âªT|ÕÌú4¼.¦,x½iðÎGe:ÞQSíô(þ¹¦mèêÂ$ãÄeuwëèkkH6Â±9¸è÷«XëêÃËÐ<áZØ:og/0GHÉÄ]ÍYíê)]
ù[ ÝXgTshowöcÞ¸·ö[äíó°×Uºmu"Çf**¥)ò1iéÔèÂKö6ÂÖE4 «üÐNÞO°üÁÔ\Ë¶TºàFý çMáÀÞpp³Æ>ÌFã`8¦ïÑÂ?#PÏÆ
```


## arquivo: /home/segodimo/zmkpromicro/.git/info/exclude

```text
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

```


## arquivo: /home/segodimo/zmkpromicro/.git/logs/HEAD

```text
0000000000000000000000000000000000000000 796ae00868f698b90c3ff5a111a54e810c9467cc Your Name <segodimo@gmail.com> 1753818193 -0300	commit (initial): Initial User Config.
796ae00868f698b90c3ff5a111a54e810c9467cc 5b1a03814b03b4b7f82b606b82f73b954614d595 Your Name <segodimo@gmail.com> 1753952310 -0300	commit: uart habilitado e recive no zmk compilando
5b1a03814b03b4b7f82b606b82f73b954614d595 08bd9da983f722d72f1ac6addaf8d102c6987be7 Your Name <segodimo@gmail.com> 1753976066 -0300	commit: testando debug uart
08bd9da983f722d72f1ac6addaf8d102c6987be7 23851c22d01c995ad94f8cf8db418e5064b2cdfb Your Name <segodimo@gmail.com> 1754001911 -0300	commit: 02 tst uart
23851c22d01c995ad94f8cf8db418e5064b2cdfb 54aa1b5d98db7e15f6d772efec20ef31d0d1957b Your Name <segodimo@gmail.com> 1754048782 -0300	commit: led blink testando entrada uart
54aa1b5d98db7e15f6d772efec20ef31d0d1957b 796ae00868f698b90c3ff5a111a54e810c9467cc Your Name <segodimo@gmail.com> 1754080425 -0300	checkout: moving from master to 796ae00868f698b90c3ff5a111a54e810c9467cc
796ae00868f698b90c3ff5a111a54e810c9467cc 54aa1b5d98db7e15f6d772efec20ef31d0d1957b Your Name <segodimo@gmail.com> 1754085264 -0300	checkout: moving from 796ae00868f698b90c3ff5a111a54e810c9467cc to 54aa1b5d98db7e15f6d772efec20ef31d0d1957b
54aa1b5d98db7e15f6d772efec20ef31d0d1957b 54aa1b5d98db7e15f6d772efec20ef31d0d1957b Your Name <segodimo@gmail.com> 1754085289 -0300	checkout: moving from 54aa1b5d98db7e15f6d772efec20ef31d0d1957b to master
54aa1b5d98db7e15f6d772efec20ef31d0d1957b dc24d2f72ebb6dedb2197b3c668c06af1fee8345 Your Name <segodimo@gmail.com> 1754088008 -0300	commit: tst len no zmkpromicro no funciona
dc24d2f72ebb6dedb2197b3c668c06af1fee8345 f5f819483167673be4167c8c69ccaacae70ec2aa Your Name <segodimo@gmail.com> 1754097513 -0300	commit: readme
f5f819483167673be4167c8c69ccaacae70ec2aa 15abcb86578487f95fa9e5a313eb80f1730a37ab Your Name <segodimo@gmail.com> 1754099080 -0300	commit: tst press a quase
15abcb86578487f95fa9e5a313eb80f1730a37ab 218d64a622bbd5aa1b831af892afe63decbb25c3 Your Name <segodimo@gmail.com> 1754314901 -0300	commit: led blink tst UART base
218d64a622bbd5aa1b831af892afe63decbb25c3 3da3461635640aad165b7addc3007b1d73021c44 Your Name <segodimo@gmail.com> 1754486238 -0300	commit: fake_switch funcionando
3da3461635640aad165b7addc3007b1d73021c44 1c7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21 Your Name <segodimo@gmail.com> 1754503182 -0300	commit: nRFandEsp32_01
1c7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21 c9eeac788561283234420643582a6c770d4769f1 Your Name <segodimo@gmail.com> 1754505101 -0300	commit: esp32toNfr_02
c9eeac788561283234420643582a6c770d4769f1 0e7f0c8b46d91e0dc427e091cbada0a76f29c21e Your Name <segodimo@gmail.com> 1754507120 -0300	commit: fila de eventos com k_msgq
0e7f0c8b46d91e0dc427e091cbada0a76f29c21e 090cbfd02e40e9874b11b8864dc7119f219a8219 Your Name <segodimo@gmail.com> 1754507646 -0300	commit: checksum no protocolo UART
090cbfd02e40e9874b11b8864dc7119f219a8219 62726b4dfc7ceb2fb2d8a4575908f6bb726625b7 Your Name <segodimo@gmail.com> 1754561052 -0300	commit: esp32toNfr_03 fix col0
62726b4dfc7ceb2fb2d8a4575908f6bb726625b7 27d174bf70477442117d461326d7e19231db9268 Your Name <segodimo@gmail.com> 1754606624 -0300	commit: split no funciona ble central peripheral
27d174bf70477442117d461326d7e19231db9268 5d3e7563b0cd3b30bb5386dc885bd36290305d52 Your Name <segodimo@gmail.com> 1758741073 -0300	commit: ajuste uart_switch_l - mo funciona
5d3e7563b0cd3b30bb5386dc885bd36290305d52 b6d8ae962550cf847a1b0df8eb5a497c2e2cded8 Your Name <segodimo@gmail.com> 1758924276 -0300	commit: add mouse move para L e R
b6d8ae962550cf847a1b0df8eb5a497c2e2cded8 1535acc76ce7972853896897c9e1eb60705afa3d Your Name <segodimo@gmail.com> 1759153539 -0300	commit: test kb R e L incluidno move mouse
1535acc76ce7972853896897c9e1eb60705afa3d 21f2abfc1a4a62325b86dd551fe4f9170a904294 Your Name <segodimo@gmail.com> 1759159028 -0300	commit: simetric uart_receiver R e L
21f2abfc1a4a62325b86dd551fe4f9170a904294 0e501c6c418be9cf92d3e1ffe1592b8c35f361c2 Your Name <segodimo@gmail.com> 1759343154 -0300	commit: mouse funcionando no L primeira vez
0e501c6c418be9cf92d3e1ffe1592b8c35f361c2 e10f0b80052e58074a12f32cbf832ab020ebf243 Your Name <segodimo@gmail.com> 1759519090 -0300	commit: teste lintener testes poc falhido
e10f0b80052e58074a12f32cbf832ab020ebf243 54a6a8272e9229e0fd34c14060294b0fd9c09cf5 Your Name <segodimo@gmail.com> 1759627778 -0300	commit: test event listener fallo
54a6a8272e9229e0fd34c14060294b0fd9c09cf5 51e279078e558592db9dc988e55fc29e57a6c4cd Your Name <segodimo@gmail.com> 1759638764 -0300	commit: test receiver central fallido
51e279078e558592db9dc988e55fc29e57a6c4cd 53aa34f8a632b90ee034ddf0a38e4e874be152a8 Your Name <segodimo@gmail.com> 1759777207 -0300	commit: test ZMK EVENT fallo
53aa34f8a632b90ee034ddf0a38e4e874be152a8 fc7f4df9c8c307d36f9823b31b3f640aec3a2c22 Your Name <segodimo@gmail.com> 1759790422 -0300	commit: base zmk events fallido
fc7f4df9c8c307d36f9823b31b3f640aec3a2c22 f4e3fac6c0b0407f1349918cee1f87d5ca02f5d4 Your Name <segodimo@gmail.com> 1759949736 -0300	commit: base test input peripheral mouse
f4e3fac6c0b0407f1349918cee1f87d5ca02f5d4 b9e7aac534da6103ae13fa167be1babd4ebcad7e Your Name <segodimo@gmail.com> 1760136738 -0300	commit: test input_report_rel = 0
b9e7aac534da6103ae13fa167be1babd4ebcad7e 8650d20252d13e2be6a8d79ac7f33b44bfbcf9a9 Your Name <segodimo@gmail.com> 1760563546 -0300	commit: test input driver
8650d20252d13e2be6a8d79ac7f33b44bfbcf9a9 12561e3c001662dd416a2608a9db27c743cfaaab Your Name <segodimo@gmail.com> 1761000044 -0300	commit: base teste send mouse
12561e3c001662dd416a2608a9db27c743cfaaab 9d081dcc3602ee4b44068b39b7cdbd42c4624c4b Your Name <segodimo@gmail.com> 1761341655 -0300	commit: primeira vez funciona workaround
9d081dcc3602ee4b44068b39b7cdbd42c4624c4b ce12e78e8ebd7642cfb539acb2376e3bc8c170f4 Your Name <segodimo@gmail.com> 1761594084 -0300	commit: teste criando novo evento
ce12e78e8ebd7642cfb539acb2376e3bc8c170f4 a1f9b90931cbee79ab905bf6ec304c8800ec3a03 Your Name <segodimo@gmail.com> 1761647828 -0300	commit: teste listener ouve o r e mouse vai para baixo
a1f9b90931cbee79ab905bf6ec304c8800ec3a03 e43d6dce064c164d0d0049e53a7746dbb2f9420e Your Name <segodimo@gmail.com> 1761660624 -0300	commit: test event, compila mas não funciona
e43d6dce064c164d0d0049e53a7746dbb2f9420e cbc4bd44b390ed77b23d1e464a33cef77f9e421a Your Name <segodimo@gmail.com> 1761731336 -0300	commit: teste com fun
cbc4bd44b390ed77b23d1e464a33cef77f9e421a e43d6dce064c164d0d0049e53a7746dbb2f9420e Your Name <segodimo@gmail.com> 1761731405 -0300	reset: moving to HEAD~1
e43d6dce064c164d0d0049e53a7746dbb2f9420e 37f9f691852551c47563ed78f8076d2f7fb5e51c Your Name <segodimo@gmail.com> 1761731436 -0300	commit: teste com led-debug
37f9f691852551c47563ed78f8076d2f7fb5e51c 1b90401fdf6ec6cb9479e1a8042343a983db9c9f Your Name <segodimo@gmail.com> 1761738131 -0300	commit: teste no uart_move_mouse_right com led-debug
1b90401fdf6ec6cb9479e1a8042343a983db9c9f 5f4a5cef19c2e25cc5ddcaec470d37050a98ad74 Your Name <segodimo@gmail.com> 1761911187 -0300	commit: test split-ble
5f4a5cef19c2e25cc5ddcaec470d37050a98ad74 eb266f079679fe474991fc03f46a2dd1a78ffac3 Your Name <segodimo@gmail.com> 1761925634 -0300	commit: led-debug init auto
eb266f079679fe474991fc03f46a2dd1a78ffac3 ced215df91eacea3ae7c51f01f6d5a65aa53c588 Your Name <segodimo@gmail.com> 1761935349 -0300	commit: mouse l e r funcionando primeira vez

```


## arquivo: /home/segodimo/zmkpromicro/.git/logs/refs/heads/master

```text
0000000000000000000000000000000000000000 796ae00868f698b90c3ff5a111a54e810c9467cc Your Name <segodimo@gmail.com> 1753818193 -0300	commit (initial): Initial User Config.
796ae00868f698b90c3ff5a111a54e810c9467cc 5b1a03814b03b4b7f82b606b82f73b954614d595 Your Name <segodimo@gmail.com> 1753952310 -0300	commit: uart habilitado e recive no zmk compilando
5b1a03814b03b4b7f82b606b82f73b954614d595 08bd9da983f722d72f1ac6addaf8d102c6987be7 Your Name <segodimo@gmail.com> 1753976066 -0300	commit: testando debug uart
08bd9da983f722d72f1ac6addaf8d102c6987be7 23851c22d01c995ad94f8cf8db418e5064b2cdfb Your Name <segodimo@gmail.com> 1754001911 -0300	commit: 02 tst uart
23851c22d01c995ad94f8cf8db418e5064b2cdfb 54aa1b5d98db7e15f6d772efec20ef31d0d1957b Your Name <segodimo@gmail.com> 1754048782 -0300	commit: led blink testando entrada uart
54aa1b5d98db7e15f6d772efec20ef31d0d1957b dc24d2f72ebb6dedb2197b3c668c06af1fee8345 Your Name <segodimo@gmail.com> 1754088008 -0300	commit: tst len no zmkpromicro no funciona
dc24d2f72ebb6dedb2197b3c668c06af1fee8345 f5f819483167673be4167c8c69ccaacae70ec2aa Your Name <segodimo@gmail.com> 1754097513 -0300	commit: readme
f5f819483167673be4167c8c69ccaacae70ec2aa 15abcb86578487f95fa9e5a313eb80f1730a37ab Your Name <segodimo@gmail.com> 1754099080 -0300	commit: tst press a quase
15abcb86578487f95fa9e5a313eb80f1730a37ab 218d64a622bbd5aa1b831af892afe63decbb25c3 Your Name <segodimo@gmail.com> 1754314901 -0300	commit: led blink tst UART base
218d64a622bbd5aa1b831af892afe63decbb25c3 3da3461635640aad165b7addc3007b1d73021c44 Your Name <segodimo@gmail.com> 1754486238 -0300	commit: fake_switch funcionando
3da3461635640aad165b7addc3007b1d73021c44 1c7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21 Your Name <segodimo@gmail.com> 1754503182 -0300	commit: nRFandEsp32_01
1c7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21 c9eeac788561283234420643582a6c770d4769f1 Your Name <segodimo@gmail.com> 1754505101 -0300	commit: esp32toNfr_02
c9eeac788561283234420643582a6c770d4769f1 0e7f0c8b46d91e0dc427e091cbada0a76f29c21e Your Name <segodimo@gmail.com> 1754507120 -0300	commit: fila de eventos com k_msgq
0e7f0c8b46d91e0dc427e091cbada0a76f29c21e 090cbfd02e40e9874b11b8864dc7119f219a8219 Your Name <segodimo@gmail.com> 1754507646 -0300	commit: checksum no protocolo UART
090cbfd02e40e9874b11b8864dc7119f219a8219 62726b4dfc7ceb2fb2d8a4575908f6bb726625b7 Your Name <segodimo@gmail.com> 1754561052 -0300	commit: esp32toNfr_03 fix col0
62726b4dfc7ceb2fb2d8a4575908f6bb726625b7 27d174bf70477442117d461326d7e19231db9268 Your Name <segodimo@gmail.com> 1754606624 -0300	commit: split no funciona ble central peripheral
27d174bf70477442117d461326d7e19231db9268 5d3e7563b0cd3b30bb5386dc885bd36290305d52 Your Name <segodimo@gmail.com> 1758741073 -0300	commit: ajuste uart_switch_l - mo funciona
5d3e7563b0cd3b30bb5386dc885bd36290305d52 b6d8ae962550cf847a1b0df8eb5a497c2e2cded8 Your Name <segodimo@gmail.com> 1758924276 -0300	commit: add mouse move para L e R
b6d8ae962550cf847a1b0df8eb5a497c2e2cded8 1535acc76ce7972853896897c9e1eb60705afa3d Your Name <segodimo@gmail.com> 1759153539 -0300	commit: test kb R e L incluidno move mouse
1535acc76ce7972853896897c9e1eb60705afa3d 21f2abfc1a4a62325b86dd551fe4f9170a904294 Your Name <segodimo@gmail.com> 1759159028 -0300	commit: simetric uart_receiver R e L
21f2abfc1a4a62325b86dd551fe4f9170a904294 0e501c6c418be9cf92d3e1ffe1592b8c35f361c2 Your Name <segodimo@gmail.com> 1759343154 -0300	commit: mouse funcionando no L primeira vez
0e501c6c418be9cf92d3e1ffe1592b8c35f361c2 e10f0b80052e58074a12f32cbf832ab020ebf243 Your Name <segodimo@gmail.com> 1759519090 -0300	commit: teste lintener testes poc falhido
e10f0b80052e58074a12f32cbf832ab020ebf243 54a6a8272e9229e0fd34c14060294b0fd9c09cf5 Your Name <segodimo@gmail.com> 1759627778 -0300	commit: test event listener fallo
54a6a8272e9229e0fd34c14060294b0fd9c09cf5 51e279078e558592db9dc988e55fc29e57a6c4cd Your Name <segodimo@gmail.com> 1759638764 -0300	commit: test receiver central fallido
51e279078e558592db9dc988e55fc29e57a6c4cd 53aa34f8a632b90ee034ddf0a38e4e874be152a8 Your Name <segodimo@gmail.com> 1759777207 -0300	commit: test ZMK EVENT fallo
53aa34f8a632b90ee034ddf0a38e4e874be152a8 fc7f4df9c8c307d36f9823b31b3f640aec3a2c22 Your Name <segodimo@gmail.com> 1759790422 -0300	commit: base zmk events fallido
fc7f4df9c8c307d36f9823b31b3f640aec3a2c22 f4e3fac6c0b0407f1349918cee1f87d5ca02f5d4 Your Name <segodimo@gmail.com> 1759949736 -0300	commit: base test input peripheral mouse
f4e3fac6c0b0407f1349918cee1f87d5ca02f5d4 b9e7aac534da6103ae13fa167be1babd4ebcad7e Your Name <segodimo@gmail.com> 1760136738 -0300	commit: test input_report_rel = 0
b9e7aac534da6103ae13fa167be1babd4ebcad7e 8650d20252d13e2be6a8d79ac7f33b44bfbcf9a9 Your Name <segodimo@gmail.com> 1760563546 -0300	commit: test input driver
8650d20252d13e2be6a8d79ac7f33b44bfbcf9a9 12561e3c001662dd416a2608a9db27c743cfaaab Your Name <segodimo@gmail.com> 1761000044 -0300	commit: base teste send mouse
12561e3c001662dd416a2608a9db27c743cfaaab 9d081dcc3602ee4b44068b39b7cdbd42c4624c4b Your Name <segodimo@gmail.com> 1761341655 -0300	commit: primeira vez funciona workaround
9d081dcc3602ee4b44068b39b7cdbd42c4624c4b ce12e78e8ebd7642cfb539acb2376e3bc8c170f4 Your Name <segodimo@gmail.com> 1761594084 -0300	commit: teste criando novo evento
ce12e78e8ebd7642cfb539acb2376e3bc8c170f4 a1f9b90931cbee79ab905bf6ec304c8800ec3a03 Your Name <segodimo@gmail.com> 1761647828 -0300	commit: teste listener ouve o r e mouse vai para baixo
a1f9b90931cbee79ab905bf6ec304c8800ec3a03 e43d6dce064c164d0d0049e53a7746dbb2f9420e Your Name <segodimo@gmail.com> 1761660624 -0300	commit: test event, compila mas não funciona
e43d6dce064c164d0d0049e53a7746dbb2f9420e cbc4bd44b390ed77b23d1e464a33cef77f9e421a Your Name <segodimo@gmail.com> 1761731336 -0300	commit: teste com fun
cbc4bd44b390ed77b23d1e464a33cef77f9e421a e43d6dce064c164d0d0049e53a7746dbb2f9420e Your Name <segodimo@gmail.com> 1761731405 -0300	reset: moving to HEAD~1
e43d6dce064c164d0d0049e53a7746dbb2f9420e 37f9f691852551c47563ed78f8076d2f7fb5e51c Your Name <segodimo@gmail.com> 1761731436 -0300	commit: teste com led-debug
37f9f691852551c47563ed78f8076d2f7fb5e51c 1b90401fdf6ec6cb9479e1a8042343a983db9c9f Your Name <segodimo@gmail.com> 1761738131 -0300	commit: teste no uart_move_mouse_right com led-debug
1b90401fdf6ec6cb9479e1a8042343a983db9c9f 5f4a5cef19c2e25cc5ddcaec470d37050a98ad74 Your Name <segodimo@gmail.com> 1761911187 -0300	commit: test split-ble
5f4a5cef19c2e25cc5ddcaec470d37050a98ad74 eb266f079679fe474991fc03f46a2dd1a78ffac3 Your Name <segodimo@gmail.com> 1761925634 -0300	commit: led-debug init auto
eb266f079679fe474991fc03f46a2dd1a78ffac3 ced215df91eacea3ae7c51f01f6d5a65aa53c588 Your Name <segodimo@gmail.com> 1761935349 -0300	commit: mouse l e r funcionando primeira vez

```


## arquivo: /home/segodimo/zmkpromicro/.git/logs/refs/remotes/origin/master

```text
0000000000000000000000000000000000000000 796ae00868f698b90c3ff5a111a54e810c9467cc Your Name <segodimo@gmail.com> 1753818195 -0300	update by push
796ae00868f698b90c3ff5a111a54e810c9467cc 5b1a03814b03b4b7f82b606b82f73b954614d595 Your Name <segodimo@gmail.com> 1753952325 -0300	update by push
5b1a03814b03b4b7f82b606b82f73b954614d595 08bd9da983f722d72f1ac6addaf8d102c6987be7 Your Name <segodimo@gmail.com> 1753976070 -0300	update by push
08bd9da983f722d72f1ac6addaf8d102c6987be7 23851c22d01c995ad94f8cf8db418e5064b2cdfb Your Name <segodimo@gmail.com> 1754001915 -0300	update by push
23851c22d01c995ad94f8cf8db418e5064b2cdfb 54aa1b5d98db7e15f6d772efec20ef31d0d1957b Your Name <segodimo@gmail.com> 1754048786 -0300	update by push
54aa1b5d98db7e15f6d772efec20ef31d0d1957b dc24d2f72ebb6dedb2197b3c668c06af1fee8345 Your Name <segodimo@gmail.com> 1754088013 -0300	update by push
dc24d2f72ebb6dedb2197b3c668c06af1fee8345 f5f819483167673be4167c8c69ccaacae70ec2aa Your Name <segodimo@gmail.com> 1754097522 -0300	update by push
f5f819483167673be4167c8c69ccaacae70ec2aa 15abcb86578487f95fa9e5a313eb80f1730a37ab Your Name <segodimo@gmail.com> 1754099086 -0300	update by push
15abcb86578487f95fa9e5a313eb80f1730a37ab 218d64a622bbd5aa1b831af892afe63decbb25c3 Your Name <segodimo@gmail.com> 1754314905 -0300	update by push
218d64a622bbd5aa1b831af892afe63decbb25c3 3da3461635640aad165b7addc3007b1d73021c44 Your Name <segodimo@gmail.com> 1754486241 -0300	update by push
3da3461635640aad165b7addc3007b1d73021c44 1c7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21 Your Name <segodimo@gmail.com> 1754503660 -0300	update by push
1c7e1b1fd5ceb4757b47285b8c8d70dc62e2dc21 c9eeac788561283234420643582a6c770d4769f1 Your Name <segodimo@gmail.com> 1754505115 -0300	update by push
c9eeac788561283234420643582a6c770d4769f1 0e7f0c8b46d91e0dc427e091cbada0a76f29c21e Your Name <segodimo@gmail.com> 1754507125 -0300	update by push
0e7f0c8b46d91e0dc427e091cbada0a76f29c21e 090cbfd02e40e9874b11b8864dc7119f219a8219 Your Name <segodimo@gmail.com> 1754507653 -0300	update by push
090cbfd02e40e9874b11b8864dc7119f219a8219 62726b4dfc7ceb2fb2d8a4575908f6bb726625b7 Your Name <segodimo@gmail.com> 1754561056 -0300	update by push
62726b4dfc7ceb2fb2d8a4575908f6bb726625b7 27d174bf70477442117d461326d7e19231db9268 Your Name <segodimo@gmail.com> 1754606628 -0300	update by push
27d174bf70477442117d461326d7e19231db9268 5d3e7563b0cd3b30bb5386dc885bd36290305d52 Your Name <segodimo@gmail.com> 1758741077 -0300	update by push
5d3e7563b0cd3b30bb5386dc885bd36290305d52 b6d8ae962550cf847a1b0df8eb5a497c2e2cded8 Your Name <segodimo@gmail.com> 1758924287 -0300	update by push
b6d8ae962550cf847a1b0df8eb5a497c2e2cded8 1535acc76ce7972853896897c9e1eb60705afa3d Your Name <segodimo@gmail.com> 1759153554 -0300	update by push
1535acc76ce7972853896897c9e1eb60705afa3d 21f2abfc1a4a62325b86dd551fe4f9170a904294 Your Name <segodimo@gmail.com> 1759159032 -0300	update by push
21f2abfc1a4a62325b86dd551fe4f9170a904294 0e501c6c418be9cf92d3e1ffe1592b8c35f361c2 Your Name <segodimo@gmail.com> 1759343158 -0300	update by push
0e501c6c418be9cf92d3e1ffe1592b8c35f361c2 e10f0b80052e58074a12f32cbf832ab020ebf243 Your Name <segodimo@gmail.com> 1759519093 -0300	update by push
e10f0b80052e58074a12f32cbf832ab020ebf243 54a6a8272e9229e0fd34c14060294b0fd9c09cf5 Your Name <segodimo@gmail.com> 1759627784 -0300	update by push
54a6a8272e9229e0fd34c14060294b0fd9c09cf5 51e279078e558592db9dc988e55fc29e57a6c4cd Your Name <segodimo@gmail.com> 1759638870 -0300	update by push
51e279078e558592db9dc988e55fc29e57a6c4cd 53aa34f8a632b90ee034ddf0a38e4e874be152a8 Your Name <segodimo@gmail.com> 1759777210 -0300	update by push
53aa34f8a632b90ee034ddf0a38e4e874be152a8 fc7f4df9c8c307d36f9823b31b3f640aec3a2c22 Your Name <segodimo@gmail.com> 1759790426 -0300	update by push
fc7f4df9c8c307d36f9823b31b3f640aec3a2c22 f4e3fac6c0b0407f1349918cee1f87d5ca02f5d4 Your Name <segodimo@gmail.com> 1759949739 -0300	update by push
f4e3fac6c0b0407f1349918cee1f87d5ca02f5d4 b9e7aac534da6103ae13fa167be1babd4ebcad7e Your Name <segodimo@gmail.com> 1760136746 -0300	update by push
b9e7aac534da6103ae13fa167be1babd4ebcad7e 8650d20252d13e2be6a8d79ac7f33b44bfbcf9a9 Your Name <segodimo@gmail.com> 1760563581 -0300	update by push
8650d20252d13e2be6a8d79ac7f33b44bfbcf9a9 12561e3c001662dd416a2608a9db27c743cfaaab Your Name <segodimo@gmail.com> 1761000048 -0300	update by push
12561e3c001662dd416a2608a9db27c743cfaaab 9d081dcc3602ee4b44068b39b7cdbd42c4624c4b Your Name <segodimo@gmail.com> 1761341661 -0300	update by push
9d081dcc3602ee4b44068b39b7cdbd42c4624c4b ce12e78e8ebd7642cfb539acb2376e3bc8c170f4 Your Name <segodimo@gmail.com> 1761594090 -0300	update by push
ce12e78e8ebd7642cfb539acb2376e3bc8c170f4 a1f9b90931cbee79ab905bf6ec304c8800ec3a03 Your Name <segodimo@gmail.com> 1761647852 -0300	update by push
a1f9b90931cbee79ab905bf6ec304c8800ec3a03 e43d6dce064c164d0d0049e53a7746dbb2f9420e Your Name <segodimo@gmail.com> 1761660628 -0300	update by push
e43d6dce064c164d0d0049e53a7746dbb2f9420e 37f9f691852551c47563ed78f8076d2f7fb5e51c Your Name <segodimo@gmail.com> 1761731440 -0300	update by push
37f9f691852551c47563ed78f8076d2f7fb5e51c 1b90401fdf6ec6cb9479e1a8042343a983db9c9f Your Name <segodimo@gmail.com> 1761738139 -0300	update by push
1b90401fdf6ec6cb9479e1a8042343a983db9c9f 5f4a5cef19c2e25cc5ddcaec470d37050a98ad74 Your Name <segodimo@gmail.com> 1761911190 -0300	update by push
5f4a5cef19c2e25cc5ddcaec470d37050a98ad74 eb266f079679fe474991fc03f46a2dd1a78ffac3 Your Name <segodimo@gmail.com> 1761925637 -0300	update by push
eb266f079679fe474991fc03f46a2dd1a78ffac3 ced215df91eacea3ae7c51f01f6d5a65aa53c588 Your Name <segodimo@gmail.com> 1761935352 -0300	update by push

```


## arquivo: /home/segodimo/zmkpromicro/.git/logs/refs/remotes/origin/HEAD

```text
0000000000000000000000000000000000000000 54aa1b5d98db7e15f6d772efec20ef31d0d1957b Your Name <segodimo@gmail.com> 1754087828 -0300	fetch

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/pre-merge-commit.sample

```text
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/pre-rebase.sample

```text
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/update.sample

```text
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/applypatch-msg.sample

```text
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/commit-msg.sample

```text
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/prepare-commit-msg.sample

```text
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/pre-applypatch.sample

```text
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/pre-push.sample

```text
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/sendemail-validate.sample

```text
#!/bin/sh

# An example hook script to validate a patch (and/or patch series) before
# sending it via email.
#
# The hook should exit with non-zero status after issuing an appropriate
# message if it wants to prevent the email(s) from being sent.
#
# To enable this hook, rename this file to "sendemail-validate".
#
# By default, it will only check that the patch(es) can be applied on top of
# the default upstream branch without conflicts in a secondary worktree. After
# validation (successful or not) of the last patch of a series, the worktree
# will be deleted.
#
# The following config variables can be set to change the default remote and
# remote ref that are used to apply the patches against:
#
#   sendemail.validateRemote (default: origin)
#   sendemail.validateRemoteRef (default: HEAD)
#
# Replace the TODO placeholders with appropriate checks according to your
# needs.

validate_cover_letter () {
	file="$1"
	# TODO: Replace with appropriate checks (e.g. spell checking).
	true
}

validate_patch () {
	file="$1"
	# Ensure that the patch applies without conflicts.
	git am -3 "$file" || return
	# TODO: Replace with appropriate checks for this patch
	# (e.g. checkpatch.pl).
	true
}

validate_series () {
	# TODO: Replace with appropriate checks for the whole series
	# (e.g. quick build, coding style checks, etc.).
	true
}

# main -------------------------------------------------------------------------

if test "$GIT_SENDEMAIL_FILE_COUNTER" = 1
then
	remote=$(git config --default origin --get sendemail.validateRemote) &&
	ref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&
	worktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&
	git worktree add -fd --checkout "$worktree" "refs/remotes/$remote/$ref" &&
	git config --replace-all sendemail.validateWorktree "$worktree"
else
	worktree=$(git config --get sendemail.validateWorktree)
fi || {
	echo "sendemail-validate: error: failed to prepare worktree" >&2
	exit 1
}

unset GIT_DIR GIT_WORK_TREE
cd "$worktree" &&

if grep -q "^diff --git " "$1"
then
	validate_patch "$1"
else
	validate_cover_letter "$1"
fi &&

if test "$GIT_SENDEMAIL_FILE_COUNTER" = "$GIT_SENDEMAIL_FILE_TOTAL"
then
	git config --unset-all sendemail.validateWorktree &&
	trap 'git worktree remove -ff "$worktree"' EXIT &&
	validate_series
fi

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/pre-commit.sample

```text
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff-index --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/fsmonitor-watchman.sample

```text
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/post-update.sample

```text
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/pre-receive.sample

```text
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi

```


## arquivo: /home/segodimo/zmkpromicro/.git/hooks/push-to-checkout.sample

```text
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi

```


## arquivo: /home/segodimo/zmkpromicro/.git/refs/heads/master

```text
ced215df91eacea3ae7c51f01f6d5a65aa53c588

```


## arquivo: /home/segodimo/zmkpromicro/.git/refs/remotes/origin/master

```text
ced215df91eacea3ae7c51f01f6d5a65aa53c588

```


## arquivo: /home/segodimo/zmkpromicro/.git/refs/remotes/origin/HEAD

```text
ref: refs/remotes/origin/master

```


## arquivo: /home/segodimo/zmkpromicro/.github/workflows/build.yml

```text
name: Build ZMK firmware
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    uses: zmkfirmware/zmk/.github/workflows/build-user-config.yml@v0.2

```


## arquivo: /home/segodimo/zmkpromicro/zephyr/module.yml

```text
build:
  settings:
    board_root: .

```


