# Projeto da pasta: /home/segodimo/zmk-ws/zmkpromicro

## arquivo: /home/segodimo/zmk-ws/zmkpromicro/Kconfig

```text
menu "ZMK Promicro Module"

# Aqui você pode adicionar futuras configs:
# config ZMK_PROMICRO_FEATURE
#     bool "Enable Promicro feature"
#     default y

endmenu

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/README.md

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/build.yaml

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/module.yml

```text
name: zmkpromicro

build:
  cmake: config/src
  kconfig: Kconfig

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/corne_custom_transform.dtsi

```text
/* corne_custom_transform.dtsi — versão auto-contida */
#ifndef RC
/* Define RC(row, col) como um único inteiro: (row << 8) | col
   Isso evita dependência externa de dt-bindings/zmk/transform.h */
#define RC(r, c) (((r) << 8) | (c))
#endif

/ {
    keymap_transform_custom: keymap_transform_custom {
        compatible = "zmk,keymap-transform";
        rows = <4>;
        cols = <12>;
        map = <
            RC(0,0)  RC(0,1)  RC(0,2)  RC(0,3)  RC(0,4)  RC(0,5)   RC(0,6)  RC(0,7)  RC(0,8)  RC(0,9)  RC(0,10) RC(0,11)
            RC(1,0)  RC(1,1)  RC(1,2)  RC(1,3)  RC(1,4)  RC(1,5)   RC(1,6)  RC(1,7)  RC(1,8)  RC(1,9)  RC(1,10) RC(1,11)
            RC(2,0)  RC(2,1)  RC(2,2)  RC(2,3)  RC(2,4)  RC(2,5)   RC(2,6)  RC(2,7)  RC(2,8)  RC(2,9)  RC(2,10) RC(2,11)
            RC(3,0)  RC(3,1)  RC(3,2)  RC(3,3)  RC(3,4)  RC(3,5)   RC(3,6)  RC(3,7)  RC(3,8)  RC(3,9)  RC(3,10) RC(3,11)
        >;
    };
};

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/corne_left.conf

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/corne_left.overlay

```text
/ {
    keymap {
        transforms = <>;
    };
};

#include "corne_custom_transform.dtsi"

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/corne_right.conf

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/corne.keymap

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
            transform = <&keymap_transform_custom>;

      default_layer {
              bindings = <
&kp ESC    &kp Q  &kp W  &kp E     &kp R  &kp T           &kp Y        &kp U  &kp I            &kp O    &kp P     &kp BSPC
&kp LSHFT  &kp A  &kp S  &kp D     &kp F  &kp G           &kp H        &kp J  &kp K            &kp L    &kp SEMI  &kp ENTER
&kp LCTRL  &kp Z  &kp X  &kp C     &kp V  &kp B           &kp N        &kp M  &kp COMMA        &kp DOT  &kp FSLH  &kp RSHIFT
&kp A  &kp S  &kp D  &kp F  &kp G  &kp H  &kp J  &kp K
                        >;
      };


    };
};

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/corne_right.overlay

```text
/* #include "corne_custom_transform.dtsi" */

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/west.yml

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/include/zmk/led_debug.h

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/include/zmk/uart_move_mouse_right.h

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/include/zmk/split_mouse_service.h

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/include/zmk/uart_switch_left.h

```c
#ifndef ZMK_UART_SWITCH_H
#define ZMK_UART_SWITCH_H

#include <stdint.h>
#include <stdbool.h>

int uart_switch_simulate_left(uint8_t row, uint8_t col, bool pressed);

#endif

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/include/zmk/uart_move_mouse_left.h

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/include/zmk/uart_switch_right.h

```c
#ifndef ZMK_UART_SWITCH_H
#define ZMK_UART_SWITCH_H

#include <stdint.h>
#include <stdbool.h>

int uart_switch_simulate_right(uint8_t row, uint8_t col, bool pressed);

#endif

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/include/zmk/transform.h

```c
#ifndef _DT_BINDINGS_ZMK_TRANSFORM_H_
#define _DT_BINDINGS_ZMK_TRANSFORM_H_

#define RC(r, c) (((r) << 8) | (c))

#endif

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/CMakeLists.txt

```text
# Inclui diretórios de headers
zephyr_include_directories(${ZMK_CONFIG}/include)
zephyr_include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

# # Fonte comum (sempre incluída)
# target_sources(app PRIVATE
#   ${CMAKE_CURRENT_LIST_DIR}/mouse_split_event.c
#   ${CMAKE_CURRENT_LIST_DIR}/led_debug.c
# )

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/split_mouse_central.c

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

// static struct bt_uuid_128 split_mouse_service_uuid =
//     BT_UUID_INIT_128(0xf0, 0xde, 0xbc, 0x9a,
//                      0x78, 0x56, 0x34, 0x12,
//                      0x12, 0xef, 0xcd, 0xab,
//                      0x90, 0x78, 0x56, 0x34);

static struct bt_uuid_128 split_mouse_data_uuid =
    BT_UUID_INIT_128(0x0f, 0xed, 0xcb, 0xa9,
                     0x87, 0x65, 0x43, 0x21,
                     0x21, 0xfe, 0xdc, 0xba,
                     0x98, 0x76, 0x54, 0x32);

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/uart_move_mouse_right.c

```c
#include <zephyr/input/input.h>
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/device.h>

#include <zmk/uart_move_mouse_right.h>

#include <zmk/event_manager.h>
// #include <zmk/events/mouse_split_event.h>

#include <zmk/split_mouse_service.h>
// #include <zmk/led_debug.h>

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/uart_switch_left.c

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/uart_receiver_right.c

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/uart_receiver_left.c

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/split_mouse_service.c

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
    BT_UUID_INIT_128(0xf0, 0xde, 0xbc, 0x9a,
                     0x78, 0x56, 0x34, 0x12,
                     0x12, 0xef, 0xcd, 0xab,
                     0x90, 0x78, 0x56, 0x34);

static struct bt_uuid_128 split_mouse_data_uuid =
    BT_UUID_INIT_128(0x0f, 0xed, 0xcb, 0xa9,
                     0x87, 0x65, 0x43, 0x21,
                     0x21, 0xfe, 0xdc, 0xba,
                     0x98, 0x76, 0x54, 0x32);

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/uart_switch_right.c

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/led_debug.c

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/config/src/uart_move_mouse_left.c

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/boards/shields/.gitkeep

```text

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/index

```text
## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/index (latin-1)

```text
DIRC      i£5TILi£5TIL 2  ¤  è  è   uazYTó.«S;~8V` .github/workflows/build.yml       i£5TILi£5TIL 2  ¤  è  è  }D
z2Ðùd@fÿñ÷ 	README.md i£5TILi£5TIL 2  ¤  è  è    æâ²ÑÖCK)®wZØÂäS boards/shields/.gitkeep   i£5TILi£5TIL 2	  ¤  è  è   !¹·OsÑÖÅÌ>¹ÝOµtªÒ boards/shields/corne/corne.dtsi   i£5TILi£5TIL 2
  ¤  è  è  X)['æTÏXOO¢)¤<Ô¹ *boards/shields/corne/keymap_transform.dtsi        i£5TILi£5TIL 2  ¤  è  è  ÀåºvÿÎÙ wÄV=è¸« 
build.yaml        i)@hÕói)@hÕó 2
  ¤  è  è  åçê8d"KÊÎKzä[ ÞÌ config/corne.keymap       i£5TILi£5TIL 2  ¤  è  è  6fÏJ6èMÛÕM*; ;)vð5 config/corne_left.conf    i£5TILi£5TIL 2  ¤  è  è  iQ¼*XZfÑÃ¢®S1/Àªª config/corne_left.overlay i£5TILi£5TIL 2  ¤  è  è  îà¡ÌÁÉßîd"	 config/corne_right.conf   i£5TILi£5TIL 2  ¤  è  è  L:½ þýJÝ-ªÏ»B¨wò config/corne_right.overlay        i£5TILi£5TIL 4cÙ  ¤  è  è  #*p(ù
è[ôd³ÓV config/include/zmk/led_debug.h    i£5TILi£5TIL 4cà  ¤  è  è  7jx=|F$(t¯¿ÏæO (config/include/zmk/split_mouse_service.h  i£5TILi£5TIL 4cá  ¤  è  è   ºû+?mÆD-èÇÏë>äbý¡_% )config/include/zmk/uart_move_mouse_left.h i£5TILi£5TIL 4câ  ¤  è  è   ¹Ò¹Ò}æù3àù8öðAüLR *config/include/zmk/uart_move_mouse_right.h        i£5TILi£5TIL 4d  ¤  è  è   ®	KFæä;Û¦Å¬5%T %config/include/zmk/uart_switch_left.h     i£5TILi£5TIL 4d  ¤  è  è   ¯zL²öÙËZ¹Þõ
Æ`qØ!Ç &config/include/zmk/uart_switch_right.h    i£5TILi£5TIL 4d  ¤  è  è  ªolÁ5>%`¸9x@â]ãjÎ config/src/CMakeLists.txt i£5&íi£5&í 4d  ¤  è  è  ÕÔð=:¨öÒY)²<Á;µ[Î config/src/led_debug.c    i£5&íi£5&í 4d!  ¤  è  è  ¯î:Çº:IkRÃªW  config/src/split_mouse_central.c  i£5&íi£5&í 4d"  ¤  è  è  Ëý¸¸[±,Y/ðq"¼¹b  config/src/split_mouse_service.c  i£5&íi£5&í 4d#  ¤  è  è  '|ñ4ÚªÊ&ýQÂÕ'¼¬O !config/src/uart_move_mouse_left.c i£5&íi£5&í 4d$  ¤  è  è  oVg§Ög|P¡*«ÄÌ "config/src/uart_move_mouse_right.c        i£5&íi£5&í 4d%  ¤  è  è  þÈ°Lª©ëI¿>Áyù÷l² config/src/uart_receiver_left.c   i£5&íi£5&í 4d)  ¤  è  è  ±o§g¨é¨`Ja*+©üê!  config/src/uart_receiver_right.c  i£5&íi£5&í 4dW  ¤  è  è   Mi£yöRtçüdY config/src/uart_switch_left.c     i£5&íi£5&í 4d  ¤  è  è  w(óÀU¦¹¨:ëîzÜÎéPD¨µ config/src/uart_switch_right.c    i£5&íi£5&í 2  ¤  è  è  ÆÁ4«Øh&ævÁ­õó6  config/west.yml   i£5&íi£5&í 4d  ¤  è  è   %Â³V#jÌÜS.Ë	\?¬ zephyr/module.yml TREE  Q 29 4
ÛrøwrGu+?¸Ö$Jk(Ùboards 3 1
»vQwG¿L÷B¼Ä®oê±shields 3 1
Ä eGzO9T6òÅ£û2>corne 2 0
»N÷Ü*YÕýûSk³úTiºconfig 22 2
HÔücîÃæ¯{è3DßÕsrc 10 0
üFfoÛßla%+I÷b¨Kinclude 6 1
Kêeª[ ØJ>ÙÕ°ÊÔ;zmk 6 0
ªSiÌÌeWñ¦µÀÚF£zephyr 1 0
­ºòµ´-ÔykæqÜ#*H	.github 1 1
¦¼73a!êµÐ¡±[v\C;¹workflows 1 0
OæùE5HÎ/HoE
#åÛû·LÁ0AHÔÕ÷ò¶]
```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/FETCH_HEAD

```text
4a204a6ed4f0223c846b7a9fc5372483715d87f5		branch 'master' of github.com:segodimor2d2/zmkpromicro

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/config

```text
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "segodimor2d2"]
	url = git@github.com:segodimor2d2/zmkpromicro
	fetch = +refs/heads/*:refs/remotes/segodimor2d2/*
[branch "master"]
	remote = segodimor2d2
	merge = refs/heads/master

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/HEAD

```text
ref: refs/heads/master

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/description

```text
Unnamed repository; edit this file 'description' to name the repository.

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/ORIG_HEAD

```text
4a204a6ed4f0223c846b7a9fc5372483715d87f5

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/objects/pack/pack-b7a77e8e4ff22c7ab2714ee62af3df0214483413.pack

```text
## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/objects/pack/pack-b7a77e8e4ff22c7ab2714ee62af3df0214483413.pack (latin-1)

```text
PACK     
xËAÂ @Ñ=§à(1À½ËÚ¤¡4ÆÛÛ+¸ùüÑsGDPÖ"NMXK.ztÄz~
IBFö½M.rÒz
U*l)ïHÐ>­ËGÛ»¼SÍò²å¹ñRÛm®´¬çÔêUjt`Ð åI¥Ä¡u#ÿ·!?GNßºBxÍAÂ Fá=§h 0´$Æx÷.§ð·b(ÆëëÜ¾äËë
  Ç­Æ8àq)Ì.úf7/ê%
{§4NK0±1²Y´Y|bñ,Â6ò4)y÷gmô¨ïFw) Ëµ¦\êm-·s¬åJfôÃo=iG'mµV¿Zrïø_ª£¶\ò.ô¶ç}=Ô{ÛH/xË;n! ÐSÌb
e@¬ ½ËÉ,f]øôÉÜ>é­)a3Å
m5$ÆD4NgÉ)ahjÒêÁSö÷)zU¹uÍh«ólJÑL¡VÎVñ±ncÂe~¹|?å:JëãçÚ¹ÝOyô3hò:ÚÍº_hÕ¿ö¶|>UÇSàê±ç6vÞËÇl]ÚdxÉ[ýùJüxÎA
1@Ñ}O(i¦i§ â	Ü»if,X+cçþz·ü±ÁÝ#&ÃR¦!yåçH)
e&I»·löÀKV[|V2bU.EÅ4$,SBFÉ³ìãÑ7¸õ}«4ÓÇÖ^jëµI}µ·3ø}&SNîW[ÃþîiåPì¾¯P_uÀo »/ªD
xËMÂ @á=§à5ÐIñî]ò3Ô&EJïo¯àöå{£3KBgí µUÎøL¨£CJµ.ºÌ>¡àQì¡ówH¤¬rÂÉ:â(«5¼ÉÎñi]¾ÛÙå+T÷×ÚK
ëvK­>$8 ïä¤Râªuÿ?ÅàcÈcßÖ1ÅÅ"AæxËi1ïâ%°F}q¾û´èÓov`µ2Éñ[)øRÐÕÔè e²!bK³)iwÊ0,Ìyk9#~bÇkö¼³ÛU°µ*oFñô®lì9Y¬CÄ9­Ów¾b½_8Z9kû<j<o¹ÕRÞ)¯ÒnRK)­çø)®z5±{m¿Xîý<VEO[Aø_iORxÁ
0 ÿÂP9q©ª:Aÿ}l(i*ûú½Ó]ÛÌ@³¤$ÄrbAÁGH&ûÄÛÕ¼î+}Ee
FÏ¤¨­çX!L£½ë¯zlðbpÛm®ºú,ëe¬å>±OÑSdè0"º¥5û¿tÍöfpJXM;µáÝåDxÁ
Â0ÿ®â
 t¶ÉKQçË%XÂ1J¢Ã-ðÛíH[UpCVfì"ïº^U¢YçÄYO!yñ¢s¶c·UO[éâH*Ò÷-1zÃ[}îe[àÆYá¼êTËuÊ)ùöDÉaÑ4S­ú¿iª®ôÝ^î M^éÉyùû)0n³¤2³ùNL¨x;nÃ0{b/à?k)À|÷.ÔCÀôeøøÑÒL1À3:@nYmD:óì×¤è¬-âB³cÎ©`áà"_éx
*p¢/k>YJö'\Rql×hd?Úé®{§4ÐeÃCÚôúhR_EÛ79Ü9ùD'¬5muü¿4Û =ëÁ×Ñëþ)u5Ý7Ð[*BYêGÍevNÄxÎMjÃ0@á½N1hYcYRzî»Ôü$1D +9}l|ðF7¢\-£pÑlÈZp&MòéRËSxÔnûU±DI'3b"ÌÓÊ(+MBy"!õ9nÞáÏ~k3ø:ìêº5ÿ¹¶ºÝ?ÅÛ7Ä%Çy%,ÃYÛ6½/Ã°cHßê®»¿ìu>{øiYGÏxAÂ  ï¼b? Z¶mb/ðîqÛJ¶AÐÄ×Û/xÉL-Ì°µhìÔ«ÇÄ=vÈ»·^mT8W0Ö¡áÎkmm½A²¨GÂl?ô_hVÔê]
Ü¤¸Rb8½x\ÖDñyôÎ`4ÝþpºÓZí4ÅZùÿRm%&àÍ_XZöQ2ÁGÊ´Ô¸iKxËÍ
Â0@á{¦ð ;?n+!ÄÜ9:S*5éþtÞñ^ßUÁc ÏÁYGÉQH9³¨KÊÌ:b=Z2_Ùuë0rÀdÑÈ©Ê2¦ayÈÎEïcsd2rôwÝáURnMÖRKõsk¹
Lxæ=\Ð!SËÚ»þ(M¡kë
M·¥MÍg;DþxËË
! Ð;ULA>#1VàÝã ÃJ"²aYë×¼¾äÍ!gNXåÄ'XJÑ8òBbö9bN­<ä=!!æäÍì5m
kOQtä­ÄÄDñ>}À£ïîÜ.,=×ÖoKãú:¦Þ® É£óÆY4ê§­Î)ÿO5ePßë>!ú¡¾#6FUxKÂ  ÷â]@óÊD'pïÊðyÔ&¥4ÞßzWL2ÞÁÑ9=¨]ÒCdc¢ò*jJûàX¬¾ñÒ!kVÙG1 FÊRiç¤Ì2[JCôxÉCÒÂïýS¼êÞàéÃuã±¦©ÔÇXü4c-wdP*CÊÂ	«8lzçÿKÑyë0-ëÞß×Ú~á(¾x/GxËAnÃ  À;¯Ø4Ú°Ø°RUõ½ç¸À caüÿæ¹4s¨bjcLDÉ²eââ[(+J	nÉ¨Ù2tP/.N!úLká`)Ò=RY&¬5rÍWðè×?i
ß§>{®­ÿ>Ôízû»_{Zá	Ñ¼µÕ9õói¢
SÏ	u?®	z¼tÈ­_§R_JxÎAÂ Fá=§h(ÐÂ$Æx÷.§åGJ]xz{·/ù×*@cÀ0Ilë&Ãì=3ÎzVo©x5ê­u)È`ÍÈÐÖÅ´Ø àÝ®7líQ*ÝÊVé*tZq/qÎårÏ2/Ç©ä3u¾gÏÚCmµV{Ískø_ªQVÐ7?	ýt¥$Ë2Ç¢~ÜFÄxËA
Â0@Ñ}N1PÔd: âÆèJÝÉ¤#izõ.ÿßªxÃÑ9÷õûÎFIÑ°OaÍôPo®òjàX$½8×;²ñA1PÿË,Cöa¢â¥=K[Y*9lgJsÙÇiJÞAGh5ÂJwZ«¯æ±5ùÿTMæ÷Ó×Ãù§©¨DôxKÂ0÷9/ Ê·­%8{ÆqJ¤ 4åüä
,ßhFz½ ²OèæèãÂ&-m$k<É;4Qjòî<M´ØÙ
Z¢StCôzÒýsLd¢£¿jG=Ü©\vYkÌ¥ÞÖBy;s-W0sÀÉ-óäá¤ÖjÐ{ÿKÕeïÐ%GÎãm£
m[Uý ÓHjxAÂ E÷\Á
ÐLñî]t¨$¥z~Ñø?y/¯­ÌèÁY"£¼Fó´ÑSdoµâE+/M²ÁÈCç)LcH^#@àÐhA{{ÖU>ê¾Ê;§:æRoS¡<b-W©Üp¶èóò@ô·äÖøR4Þzßû[9ç­ñÒ%æ¹Ä¥FxA0 ï}Å~@³K[hc|wË²&¨ÿø3i»*°N:~Ðh9¢sê¸O!á8
H¤#&óæ]·¨ÏRQ£¤ØMV)%%»1õÉö$áO[ê¯úÙáÉEávè\§\êc.×«Ôr|ô1"\Ð"ÓÜþ¦GSXóÖt;ÿð®×%OÕ|É?JèxËAn! À;¯ðZa0Eª¢< ê=G&E*8"l}}ó\G5ER¬TÒVó]_HÐî.JqXsñ ;Oæ8ÕL¼9ïBÚ·RBÀ*T#,GK.ác}ë«¾¸|<ä¦¥u½Ü:·÷¬ýx
ÑÇ@ðf½µæ©½­%¯OÓõxÔcä¦GQ
p­K¿ògþ¢8KxÌAn1Fá}Ná1'B= bÑ]WñüC#ç/WèöIß ÁÁPÃ:1kò9ó´FF8«­sÅ»vü
£Él,Sò²XFÀuöâ£®ÊÓmü´N_mëtÑ
:>qkK©íãVµÜ÷ÖêÄböS¢gïÝ»Ö2þ/Ý³T^6íã»ÃP^ïÏ'ÎîÍGÅxË;nÃ0EÑ«
$ $þ/Àp.åól6EC¢²þhinqÓWòÈ*)Ø\tÁ¹ÀYføÌÎ©GÌ[V,æ IÀaôÞæÛd­Þf/c1f&#{´~Ú¾ÒU*èkÃ½i©í|¯R^¹Õ
Ñóà'?1}ØÉZsÜZzÇÿ¥éØ:=gú&ÐÊ_{Ñ¥Qm¿8²o0´RJ*xA
Â0 ïyÅ~@I³Ý4 ¼yÌf·µ`´©ï·_ð2i*Dr<R9jÎrÏHÞrç{Ü[;Pr¹Ñ|Ò¢ï$¨yd-3aðC ô.Z´$äLÚÚ³.ð¨Û·TN«NUæR/SIóëk9C7P®wÃ^Z³Û2·¦ÿ&@©Ûª;¿
ûp+(ÜÍÈE¶xËKnÃ  Ð=§$ÂØRTõÝgñl¢`*êõÛ+tû¤7º ¡&L1¸i§S¾­"Ù$¿1[çò¢¾}cæDlCf´ÌÖj"NÖÑ.±Ðª
¥°j·(?ÇÞ:<Úìðå«Àý­¥RÛçV}y_c«@|[Ø²Dõ§µ!ÿÊ¿æ9¦ïãyþ÷ç.PäyÄÒ¯~0I¾xAÃ ï¼b>°Ã¥Uä¾ÇÉàÿ/_È­U¥ztØ_-²ÖÐ eÑ¸m¨#y³HÊèVT'w9:¤`R.JÀ0y6ÖÙMûL!LKhS|wëð×®O®¿yµTj{¼*ý[½Ãâ¬!=?zÕZMZËò}©>ç^
òuÄÒ°Äùºó§ôr¾eNõöL[xËM
Â0@á}N1PfòÓI@ÄtïJÒd¢cJÁãëÜ¼ÅotK8#±hÍ|¤4»â]ÊÅ½Úb× QE	íB´x?Ù(M!ú_T|Gëpmïs¬§]î-¯µ]î5®ÏcjõÄÎºÐi8 AT?­ëòÿ©dßm.ýÊúÔ¨¾É_D]xËMÂ0@á}Ná4[	à,FÌb®ãþhF!½ÿp¶OßkUü$yìê1)th@æØ8Å1*»'W}4@¥ebÊ£WÌ½3#SÃ(Á«ã½­Vá×ö
W.
§.·bç¥ðv?/ðÔÇ)ÅìÝ»­5ýüt²ªü½ögµfbwË÷ÍýRÝGoxÉ
Â0 ÿ®b ­Ïu$¨?/´Ø18õøf¤éMlà`lÎ:#çLµv7ò16Þ©77yuH'Ñm¢5Ö9ÁY
DÙQF­xí÷ÚàR×g.E¦çROSáù¹OµAwIZDµÑ2÷.ÿjY@¾Ûh]`Óàq-ËôQ?$F
xËAÂ @Ñ=§à
Mñî]ÚD¤Az{7ñ?ºÆÈ³A+%ç
ÙÎ^b9Y0blj]>C#{Á%;d½óG(¸8d'ÊL¨â>^­ëGÛ»¾Ç*úò¥åµ¶ÛRãú>s«WÞYõ	:´®cÈÿ§ïfh´{éO õm$Bí
xA
Â0 ïyE> d³Ä=zðæI6É¶LSÚôÿöfÚ"¢	#ö}ìÉGBÈRØº(ÎÛÙ©ÆÌH<:O9w1pÎ		r@c!)ÞÚ§.úU·E?¸>¯2Ô<z
ßcªå¢!8rádõÁìµÛ2¶&ÿjzÞyÊ·uFû6 ~BxËKÂ  Ð=§à>&Æx÷®Ì C%
ÆëëÜ¾äYÂÄ0+Ýì4x;¥Ä.SlªÉÅèÄVnCÉycBHH´2Î2{8`\´öñè«¼õ}Wª,O/=Ú/K¥ò:Æ^ÏRO ½±(Ê*%~ZËüÿ|ß>eÄÌ{¥7j©/ØFxËÁ
! À?Ulp!1FðaôásEÇa8®mÁï$3:3 SÞÉhi'£Lì¼ÆÈÙD1¦dmLâCçÊRÁí-:ã0{É³%­4'³B-I#Aëxµ¶v¸Pe8,ül©ÔvzV*Ó6¶zÖhe¼T°ZJñÓZÆàÿ§8AÊü±¸¯7´°øAÄFxËMÂ @á=§h¦åg 1Æ¸w9ÀTT ÷·Wp÷òo40"4gk}spM.x«]Ô,at,´¬6nò°ØÅOÁx=9r¤£#?XJÌPÒÌ¬x¯ÚàQ÷w..Ï×RoÏÂëûj¹ÂDÖ`èN¨ÕqË:ü/Õè¶&½Ãwç.êû`Db
xËM
1@á}OÑ(ýM; â	Ü»LÚd°VjçþÎ\=øàÍÁ¬ÁDSYçI ãQ¼dJ"A_)"©~O]ÕIrL+9»$ò (V³Qá>}èGß¾cc}ùòÚëÖúmm¸½Î¥·«¶)³¤h½>o:´msòÿ§µ±ú«dA0xËAnÃ @Ñ=§4	 UQNÐ}À.ªa,7=}Ò#tùôç`®ëTÈ_(Å5]ãìiÔÈ:âà>Á®1êd)xJµ-WrnáÂyA.FÖ%Ïù-røáóÉPmrßZ¬û%K»vvEï=| ATomuNþÿ©æsÂÎºÀoû9´üe9{®Ò£z[WKxKÂ  ÷â]@Ã·@b'pïòÁ{hc)Òû[àv2ÌèÌ`Ïqbo"Z§¢¶c´×ÅXí)5ñÁÎë mSYk*Çè~r.UlÒJ¸Wëðh{;VËÆÏFsm·gÅy9çV¯ ¼³Ò4¤R´Îcðÿ¥X -óúÁÛÀÇ	aÇ>ÄzZI,
xËA! À;¯è4PX
1¾À»Ç.-ºAöÿú¯Ìª!iÎ«xâÂâc!¡¸hõU1ÄXyóÐ×VÉÂ9ùJBXÈ"\8%æD«á}>ú[ß\¹)>zï²µ~¹7ÞÇÒÛ-ÁZõÖ¶mNý0?vÓ|§±AúxÌMÂ @á=§h 0ü$Æx÷.g`ZH1Þß^ÁíK¾7ºÚÈÉ0Â9gbNN´ÏÓÄqÈÕºl
icmÙqãÄ^{Óìi7®`BEÇx·¯vtxR¸í²´²ÖöX*­knõ& Máx¸h«µ:k]Çÿ¥²ÚJ"|,pPêÀ×EExËMNÃ0Ð½O1 ÍÔÿª8{_IkÇqXpzz¶Ozs¨õqq	öâuHl< nÝDBæ¡Ç¤9´ÌÅnÀ;MÂ%»K18ç½úìç 4¥·o½õµ¶þ~k¨ûkéíJ½Íþbé-³yj«sêÿ§91&Ý±Ô½N¬ú£ttúm_ôlºãX»ù_LÕxËK
Ã  Ð½§4ø©
]uÓ]]S!fÀû7WèöÁëR¶âUjkCôyÌÉaÄ=¢&Y åGÿr
^¡ÜvZ8Ê÷¥²ë
­ñÊ«ÑÀE)Å©µôNÿOñÜJ/a÷~îo¹,øÛÍ7w 
x31 ½ôÌÒ$e{ÌÅ_m½°PtctY3õNC3 WG_W½ÜvÆ¹.-Ó¸ª.üLíöÿã÷ù&`còRBOnOr[âa,[mu'·Õì¢äQ¨)I¥9)z¹9î*ûî&Hù©0Û;äºW@IÎÏKËLg´ëäÓõÊÏ§´ù-ñuè}j·¢ *µ £²aí®O['l¨{¥2»¡ëYáe-N ¾bRæOx6 ÉÿÐÐTN¤´!$Ù^ZÏ
ñþöh3ÿ(ZQ
 2dýH¯![ßæEx6 ÉÿÐÐT»vQwG¿L÷B¼Ä®oê±h3HÔücîÃæ¯{è3DßÕ¯!»¤x31 òü¢ì´üòbÿg?]M=Îõé{ÈÍÎwåR~zã7 ëU#¥x340031QH*ÍÌIÑ«ÌÍa(M¬jù,¥·Z<XÆZ¸Î",A Ù¤¼	x5ÌKÂ á9«¸hÁ8dd7 1
´P°¼äDWokÒÙ?8çÂ+çjÝ·ë´Í¾¬Hî©¢é Uç¬^Uaé Å¼hÛ0YL¢æAÈ3Jä@nÎ røúeÙÚÎ¶*Ù û_úuû1mgúñîô>Ð#ùàÕ7¾"x»NA{âO°ÀDÙÞñ¢`²^m6Ç ;ë\ø0ÆÂhË#ìy"Q)vþýþË´³qs.-ÕïõgIÔÚÅ9cáLýÊ³@°S/­LºdÅ+i8$ò±P!Ë}×ì ÈÀjbò´§Ô.ïi±óSØÆ±rAb½ôâp3<QÍÈ!pÚ(ôãØJdô4åS
ºñ!¢"OÒÌøNÖ!ÝZÑ ÑùÇÎÖ³þ\ôÏFGã,x³­ª!q"&õo:Æcln£txOw×7@¨ YdÏp(H´aÁOÝV«ÝÆUý
õªÇÒ¥"ò÷I+tFUý)Äß³2$Å´1XÜ¯É´Tó2:§¾Ðï9[ÿï­çþ°wrXô/óüptQìF½üº8ä/ºëþÅjº/Çoçcx[Çòe?²²Br~nAfNbIf~BIjq	¾¾rjQQ~"¹yºy:;ú¹ø+»*¸n2@\gß OG:%. ª¢x31 âÌÔb#²Ò©îUþ!f.þ->ÑÈn ¹¬@¤x340031QÐKÏ,ÉNM-`x6÷ÑìM¯9{wk®+ºqèIOðD PHÎ/ÊKeÛí÷ýVäÕ¿¿³;6wüâ	ÉÜ Ö%â0x    §x340031QHÎ/ÊKÕK))ÎdØ¹½Á¿øâµ£óÎØí½ë¿U´dÕ%CªìÔÊÜÄø¢Ä¼â´ü¢\Íhõg!ç#&ú·ù/Ò\2Çæ
ßN ôÒ#±±xSÎÌKÎ)MIUPÊN­ÌM,/)JÌ+NË/ÊÕK))ÎTâ Ð³xUÐË
Pá¹O!Ú»`ù*aauR,Þ½ßCn\7ëÛ3M_IÊªG(í­-/×CÝ~ÝÍ¾My;îÎUºIGÏpÿÊXåIl·õýJoíEþwáüÝMNtËøßÍQbÄIFædAdEÈ@
D @"(D9­ôÔT!
QB¢Ä Æi£gÙÄ 1Câ8Ä9íô|iÿ6ï<áû i¥I«·6xËnÛ@E÷ú
Â^Ö A6ÐE iP¤Y4]4E Q3´DTÌÃ­ÿ¾ÔÃvd¥ÈËËË3ZÃSÇ¶Ü´d)`¢©#¸ãô57ðE'v6Â)ð¿b
·.@äÁËDã0ø ±cê
h74lqØ 3
ÜdvÔ/ch¸-£îã¶b>¸@âeSpýlÃÖðMÆÃì+ÅmYU³Õ}6TÎSHûøå2h´}t#Mj=àRÚxÒXyÂ¥ÇVpÌ4ç#¾:ZöR=öÇcÉw{¡37$ûtb!ñuRÉ4ÊcäV²ÀXcbÛfÌ{\N>'Ü º'4CY¬%Ü¾ß°²¬©²h]µ»\ÁËèÔÔ.XªzÚ¦ÕVóWà¶K³r¡$  ¦±ª@»ËóòëES·+AÄm{õñÝ§`«Y	1eÃN¯UÊÂnªusýøýöþ®z~øVýxúysÿøy¿èÎhò#T9uÕ¼@(*¥#W÷*`g÷Ë'ÜÅRó"^â;x{ÎÖÂ¾ÁYZA¡8/³  µÄJ¡*7[·´8I7'?==3/kr Ädf!¶¢Ìô. ¨Üø x340031QHÎ/ÊKÕËN­ÌM,`xúü¬E»÷©sÌÞUO¢î1DRV¢ÆvÞËìïí«¾"ZÖÓ¬å5Ë>b*Í/K-ÊI¬d&^<ã@è&Éj«È=÷/~ó×JÕEéPßµ<²ðÓÁ÷g¿K Ä9uµ0£v0¼:;½l¶ÍåH.©ÌÏ¹M@!3/9§4%AÄCêxêªh^vR7¯n8uÅ¢¢¸(á[à¬üÛ÷sUµù<¿'­ðZWZ\¢WÃÐqì Ióê72øÕ\ûõ3 tw}¾æ	x6 ÉÿÀÀmiQ¼*XZfÑÃ¢®S1/ÀªªG:½ þýJÝ-ªÏ»B¨wòÜd«É´³¤x­W[oÓH~Ï¯QIR »KÙJnâ4ÙÚ±Âò9ÎÐZMlËvíßsqìôªU9ùÎeÎw^¶ÄKÑO³<>¿(ÅhOìw÷»"¸âs
¢¤ÌãÅUæ¨¢¶ï>vÉ¤Æx)2þËü½pÆÈ;­Öó¥ü'0w§ãI0ÌÖÐÙÁÜYó3Ó½ýnWNGt»/ñûMKöß	ZÑë8VWK)>ÄIvUv²<dQ¯eÕ~Èìâ&ï,Kc'Ë89/:¼þòb0¢t)×õuy^Çw!Ö¡~¬/;²¹r[~)o¶°·5Ò«¢Ø¡¥1d;9ØX~¾@V«½^_Ï)Æù*.JÈ\üô&]âoñ¡ý#ÎæßoæE®@i_ôÅQD(¢<]­î?[°{""	6Â2NC~ÏÒ²> IúAItIµ×Ò(Sc~7LÊ¥±.Pó]·«u±~Þ@ýàÂ¥\7Je£Àü9¬õµòçA#;=f?áðËÜÈd§ÚÉÞÁÑamµ:`ôªzR¦Ñ©,Ì!þYÄÅû:QSAµ(]g²ÅJBAÉ½Ò`FfÆ2L"ùì¬ :þVáB®PÛ5=k,ìo©<WçÁ-YQj!o
}`0ííËLØÖ0× ^1ß
$=bÑ¥,ßëÉoòØ3û§Vðä½ãÓ@Ge/Ü±kíÕ²äPäoÄú
ax}Æp;¬MÜèMë0Û «_j3¡ÇW«rgÛJµÅ¼ÕõºiaáX~%8ýÈÃ',Z|#Tì5:3ÖkÈêKdûnLÛþh È3yðyTºCfÿ¡úHÓHüÃ:§#òm=ñ-üB7ËcÛýÀd~áá3
â1ã¸êM#á¨ESÇøüÁT6ômpY?á"¾ï×yIjÀ0ìP
Ù°=(âÅ~¤@Ìu*z¤³}XÃÚ
¤ß2à1á»fßzíÛ¦*èU	P¼-´~Sa8¸)=ê\èã 3ý&ó_­ëÀÄü%p±ÍÉÌ9¶¼ù_
êOò<RÒ?ª%UÐßÑÔáÓ1íÂ«I¢gú¶&\¿Ñ®Ý#¼Ø>ÖjywËÃVSáÃl*w<Iá5!èõ È+z0ýnnhtrCÑ. Cõ~ÆÃpü:ÅZÊ!¨¨­¶XIá!ÉRv
)¦Ùµ
­ò§¤Ê5%Fa¦ñdæß_õ¤x+K¬Ý*Pe¥¡­BR¿×èåq!µ\áFÝKª2v*´ÇÔdhJ©a]{¦ú©ëõ'X¤õ¹O}#	fmÖÞ¦$yu-¯{1¡Í&X?0áÒ éÈôUØ¶fºóÁøl<PMìÄ3Ï¬§;`}ÁçY5!\å GÁzæOáÍTë»£tÀºp4Mf%Ï"«5OS4B|Mî¬e\døNÂ5=5­§HófWme÷Àùbç¼¡#Ò}RÍz°­*jZu¢)Ú¦Â[5B/#lèpjÖÃnQóññØªÝñbCÿéf£YYul´zëW×¨ô7%&loûüWg^Ð'ÆÎetç67hÇ1g°Z)c/@A_àºíkZ·}MsÛ×nû
ªÃ§mTã²êôm~]µò½¡v
iÀÜ¯3W×BvåhôçgS.aÜk¦(L¢Y@÷5ÊèÃÈô¼©zÖ>æâiº4Ü{µkwî× ª¦æöjºaÊ¬AWßÕ¯õ |'±"ÌàïrZXlEx;¬2QyÃgöÍK9æq %`M·qxT¹nÛ@íõ«q iXPäJ",q%iÀnµ±ðPHIý;©\¤JV?Rw-QEíÌ¼yóæÂ¼ÜÔ
T,25p¸?ö&òn~-îùçO¬'ýuÎãáÓ4×©çJÁ."ÝLvNè$U¾øzõ	Nc[Dv/ÀVUõîW	÷eîÜþÐCLxöLOBaé0!â ®ðnäB>cV1è±¨0yYFó$zKùÀt^fkõf ©`ÊÐ3´ÎßÀoÁz¯>/Æ2¸`¨Ñó½F@°`ÄËDÃ¤},ÑÃ´×û Îþÿ¥!kv;â¶èºøFÿ~í;¨¥j ;QSt¤Ën<aU¶sÝ%ã:ÒvææãÞ=ÜÈ:AJ'Zõ²ç{ÎwGZt¥Ï8
£ÁBðybÌ)> Ã±Ï"9c7lf]öQÇÆ+!\?æ¦ã» pî«ç&Ï|WLZ½ïª½N·	ïþ,7Y;øÅî÷Ve¯27ºæ0rAåµUàI
C Z½nÝ)ó®[7Qõji4w8ü7×&-m¿x¢õtÀÃ!à5ú¹IkUÖðvÓäÜöí!;¢Ñèø6kð­Ötðöü FLju4Ì¦F÷aU£uo´]_ëÍ¢NëµÊX*HÕf
ªØ½Té}	ËîÔêñ©;4&;`¬²t
§dY¥x!á9ÿqÖ@}¬ÉÔRïµöô%sËºAÛ)_Ý§edg'5ìþ®ÓVt­j±yÐÎ1 ^?¡kg4µK>i²HrR&K­º¬Tm²¶+ïQ'Å#*À÷4kÄT[U¬ËtmÃ¹íp|Y§NÇùjdØ7ecF]^þçjxÎ÷sÂõÉXU6þ}Â,áìïçæéåëàãïäãj[©À B%*ç14x}R=kÛP%¶ªÐ¥´)Â-	¸ÎÅKzuLlËè£Cñl=G¥'UO¸ÿB~	²º:i*ýû3ºöJrkk©¡§sß¹ç{?ºòå¡«¨pýðæhýõöè¤S÷NÝg«úQA2`2å9K Tø¸CËé(o"¶äkkp>6Ùtsö~<ò.§ÞÔtmâYdnZÎ`­ìÁ9Â³
ÅÏÎÛÇ[d+XÎëï/tøOglÓÂ22
ØÐvÓu<<ÙægÝQ°§>eR&Rd9§	à«öÑäiCýÌûÖÅLø|
(DV¦QÈ%¯ÖÉkôØ
V°¤2RA¾áM,åÐ,ÂròeJj'º¡ÃPVË-\ÑP§ddÍmRÚý¨²´ÉhD,ÏrCäP{)j±í½ë`Â¿zÇP]åx6Ç¦¦A<çÜ"C£5=$nÊÉ2ÛÍoó hQfÉeÊB	qÂò.©LþK¨i;Ý3RÄh~ùI=äÏáÇ~ÍôªÚ«dÏ'ãF:z®µÁFæßÄNÍxÉ#A>TBù-åA³9~µlgÍMçôiE¼ýî7ö­íxxÛÀ·oC%ãÄ}b{e$ýýÜ<ÝãCâ]ã}m+¹6ïc,b Sn
ï¼x½UÛNÛ@}ç+Fy@bâØNH"¡RTMÚ¾Y{ +l¯»ks)åúý±Î®³	Ð"Eª{öìÌÙ3]Ïy25 §d²pÃ/Y»5DÃ®¤(ó®eÐÆ\a¢àìºø>mL/Æáø[Ü6ô7Ú&ÚÏü¢6öøcõJI æsæÃâó	êó$âÖÉÅ-J36Mð%úúëFã«*XQjÑZâÝ·ª=Q)%f£rÄXÚíö<×­©æ¸z¥r6OØ¢k!@KëKÑÄ®óÝjCËàfÚ©I&«úU4iÎ
NGÔ¼¯r.¨ÉkDzeè't­zMãM¬ë7p|~z¾~9
ONOö Ó¢
 Ã
iC,¸ÑkSÚ[Â¦hFG,KUÃÎ÷¡q@ô´ë]§¹Ë
If !¿A¹ÁeE\dL'óìlA4
3Ë9üH¯Û²Ì)ÎØ
RGÊQò|%áÜlÂ"Ê¸m¯âe!9yÅûq¶:UJ1×|¸R¤¦, e9Rj³BKg¶BÌ%òB×*b»æßb¼WMß áßYêÆ\Äèh¿QAt"xRÜ¨(¥ø^"Pu2°)ãwÄúPHÕO{T6Ó2þ`²àv¹xCØ°ftö~V%t>ÂÉù«s¦.8o°²XÕCÐû·KEÒæþê$VöÐ[ÙCe;+{¼ÁÃâdú"¤vÍÔ¥iÝJNcxCSUýô´Åê,ÝÔNûuRifÌ}2Ûý5¢¡8ïoQ3øý+£¹@³Î¶·MA;n¾õõðzàõÁÛj
o¸°ê»àwÁ÷À÷ÁÀï-®öÁß þîÂjàAàC U{ÐG}0æÙzq0Ö">JóÉI÷cÂçi¦õt\£ÜáY^t5Þ)ôØ$³~|b>»moéZÃËEÑµ`RahBÕDéYØ¨ñ·x
èhf½RêzÁéXx[#üQÈP_KÁøýþGÍóóÒ2ÓKBBR
2óòòòrsrSóJR´ô¹68p ÉíFxû(´EkC!g=¾rf^rNiJª~vjeR~bQ^JIq¦>ª
Òúù¹©úÅ©éù)¹ùúU¹ÙEù¹ÉEùúÉùyié¨æ;M ¡VZ\Y\Z¤P
W  TqIbIi±­R~vb¥5ÔÒZ0 Ä>2âxÛ"ÒÆºÉÉR93/9§4%UAIOO?)?±(¥X¿8#35H'çå¥êg§Væ&Ä%æ§ååê¥g*q í>hMxkc½Ê²Ñ0	 
pgx»Ê2e4 QFæpxÎ7oÂ>f.eÉXU&þåüEl²ãÎÄ&ßd´¸Ol²&¤²³¿§{|h°S¼³s¼£³¯m%PÛæ(¦½, [¹ÉgCxkc=Ã²Á	 
Z®x31 ªÜlUÁgÎÌ%*ÕþqÙÖ·Ü ¤ ø§x340031Q(M,*ÏÍ/K¥Å©ñ9©i%z¿µgÛçsªûâøù×vOþ.W5Ä®£(3=¤åÒÎKµÏ~v×?èæþiñíã d-Åå%É0æqvy»=kó¤Þúö²£'¬1U
Á¢fxÏ¦s¾Ý<µó^çWÞc	7CWåfC]R\XÔÄ¸pêÎGkuïï|k¹½ø¸} Çjë?xûÎøqÂcm{§e]ûjaï\3C£ò% ÊP
úf(xûÎxqÂ! 
Âèx;ÄøQÑÄ RËRóJÎwÜ«nRÙzRJhß«bÿ¿yL8 -_9é3x{ÌøQÑÄ RËRóJÒÄDzûåN´\:,ðß«=ÈÿÑ1æ 1ê3x{ÌØÅ4AC!'5%>%5©4]/A¹KK¾Oã'ïöè/)ÌM.MT< ;Ää6xëbÚÍ4Á_«¸ '³$>7¿´85¾8µ¨,39U/A(»Â¶ÆME£¡¤iýþ&©óÏü'z ^Yh@xÛÍ4i£¢# ðG¸xMÁjÃ0Dïþ\\(5¤BKOÍ¡Cÿ@ÈÒà,VFZâOËµ?V9ÒÓ2³3oÙÝí-%qèv,.Tú(êÇÂËéó¹`>]ópFÜWÝ0Ð·°cxi:¾ºKbOÞxu2,¬ýê=½ßó?\Ü¥I~o9Qã_° <êc`9Ùª¶{}eÑ7£äR}¦U¾îööjbÙèGìàQBÛÏj#Dñh¿>HE­¢ÿ ÙYZ¾·xmAK1ïýaç¢ìÜDTö ìmÞØfB6­â7#(rÈû!|-3x¶¡9û7Êk/ôLu¿þÚëÔÄß°ó,¦ââhy¶9´º¡³PaØ=îàÝÄÎ/ÆLãh`#¿z!c	¨]L­lúÃé¨ hN°ÄR0ì·¥'ÈkB6EõCná»hj¦=îeþ29_úM\ÒY`t(xõÓâË»øøNý	º¥hS¹xmÁ
Â0Dïû½(½
¿b²4¡É¦l6býz#ô`Á9Ì{Ì°²ÅÂ È.5Ox{ÓVg¦t÷_ç1DÿY±YQËzµJFâô ØÓõÅ(ú×i7×Ý¬NJJæ/Üm£¦Z¸Âñ
Lé;¥à}xÛÉ¸qB0sNjÚÄð$&.. 0Úó¿
xm1Â0F÷ü.
ÅYPq©­.GM.æ &\èß7Çï=x_Ã6²p?õxÝ¼ÜÃ¡ÃN5s ?F5´/`ÅpÛý²G~ªJ(cÌvùUü(N¥ú5
¤8µð:úæ¼åLf¹©[õ
Õ;Pmx[Ï¸qBsNjÚÄc "\â¯!x340031QpöMÌNõÉ,.)Ö+©(aàÔ.ß¯Ï°vÆñËj?$æ?ùnQ¢Ìpö]¢ÅÅ95%/~ëuÝèÓû-9ª
¨ >%5©4¨lHödÍÅ&nAÛd[EËMi*ËÍ/-N/.ÈÉ,O-KÍ+*	þÛöüýÕÊ	3Ón÷ÌÝÁ(UQÑTTT»<¥ðLDmå£$½#O¥¾ïïª-I-.*ªlå¹^*8Í­~3BñI¾ÿZ}ª,M,©,K*ÏIM¹£æ#[É­U§úæªýxèªú5þ8te¦g´L©¿soå÷M7581%ÄäÃlIQjrjfYj0üÀVý;±ÁgUëÊ×3<÷O¶;Xùó{Î&d+àêaä/O_1sÚË	^¢òZÚ+ÿ¼RDÖP\Y7Õ7sqå·ö	A%ÏÿÌh9jáå{.Û¹Âêõ»ª;ç^¸¬Ø
 -àæxÏÒÊ2AÌú·øÉ¹é3tc|þlû¹ÒÐÀÀÌÄD!'5%>%5©4]/áÊ[«ß&^©¹Éæ õV	¾èsËüSóJs*òøóY»¼'¿¼üÖáæWÆ*{£=ÎA
*.ÈÉ,ÏÍ/-N/N-*ËLNj(?Ì¹Çvùè¿%SÙ.\Æ¨0YQ|²0£ÈWG¬?4ÓæÃ­I{Ü¼¼È¸ ò§MäBxt ÿÖolÁ5>%`¸9x@â]ãjÎ*.¸central.c î:Çº:IkRÃªW±ý¸¸[±,Y/ðq"¼¹bâQoVg§Ög|P¡*«ÄÌG¾ Æ2´¹bx­Án@ï<ÅJä ç,êT(Nla§^FÃJKw7iGê©ëÂÚ2Q[²H=3ÿÎ?ÿ|CÈÒ¦`\h¤·_Z(Ã8²
sÚ?°­5¾#ôU)-ÐDW/_ïn!ÙÜß¤_¯Oñ´"¹[Þ® yÈ²Õýv,YÁ§4{½^,.O!ÙjY¡ê®fÁºÕÈ&o?yë	êtaÍämË¶Yúe¹_]½¼o´Nw{×¦VA0­xÄÅd½D»ÒÖÅA úÙwÛuºl³¶#Ùy²å:¶,±ïê\²Hæ\14ß:Ô\õß&]OùîrM`³GqD
Îøó]PQÍÔêàRu	'"ua:~òìCøhRÂµÐÐÙGù°/xè6l@zÎþa¯LÎ
ãxû×¤8@i0r¼mQ¶Ârý
úÄiQVó¡17VM1t
·TóÓfÿ
ÛÔþ`ÇG4¾ òºç3Îª,½NÀq@Os8;iúã1ØØß¹Çq]`1k¸ýéÅÁoêûòãCx[É³s:Óäã,RÂÅ9%ñ¹ù¥Å©ñÉ©y%E9XâsRS&2kL^Å¤5yóÅÅ©EeÉ©`5ÏX´&»²
sir¥æ¥d¦ihr $&#ç_x[Ä¹sÂNFåÉy2@ò=£ìÄ"ÆdF&eÍ:eÌ üe¸MxÅR]oÓ0}Ï¯¸´BJYµ¶L ÑzUDÖT%í/V¸ÕÔS©cû=üþ÷&4ÛÐ¨à(¿Ï=÷·¥³2pq»Ýô2ðD¬Êôôæ½Ó~8ùÍÞô±±xþÈÈ0E/Í¥~é4*íáHçLøu0^øÏÙÄû²¹ÛTïÂ(^yþåú'¤ÏÌï§×A*+Òÿ¬:8]Vs§µTP|ÌC |ùù.	ìwÂ¼)¢`pôQÔòÈD´UøZÊB,a&^Ç)lde±VÂ2¶P¯rm,
Ýi@ÓJZö:ðÍ¡jw0fKoÄ8J°Ð=¦N	$×à¾¨¹,¸Q²wéfç@C(2Íçnk2óXiºT¡Ï[U¯ïëäÏ¥âØÊZ¦¥}·¶Ïv8y°g_BoÉ~16Wa¿ÔïÉÊXoÅïZSd2]%½ÞôÊmQßËóVF¼I«)Pfcä*jÃóÈRônOà
·X£T¶´<{ëDdÑoAÙwwð^¶êYùHh¯îïÜ]#ÖEa 1éþZ/NON
)cfE¸ÁÎ2!r·ió!ÞcHóþÄqÿÄmJu¥uÏ;²â õºy¬¿J$|¼êõÞù	*°w^æ2x»Áy{Ã
z.}}GsZ<ó23s2«/?¼8_!±´$?÷ðÂÌäD¼|¤üü®âD _!3¯D!'5%>%5©4=>3/³$¾¼(±  µH#9?¯¸D¡¸¤¨4¹D!%µ,39UA«4¯´85E«KÜãCýB]]4u k°ªPÑ¢ÔÒ¢<k®Z.®àÈàxO?Ï
ìÖë(8øx:;xúûé(8ûû¹yºÇ#5ÇyúyDm  ÄGZ3¸x­WÛnÛF}×W$ TÙ¢äK¸
 ÈKDYNA.WÖÂ)KCJã§>ô;>ôCücY^´¢'hË]¸3³s;gvùÇáÇÏ|9_G­[Ü?¿®=-/ùáÍnZø]¹.×KÓÊ®ªë'\¡·_&ÕÖ#å7DXj»V4g·-{¶ÇÝ¤ì'.%N$íExÇñ#¹íóÚ§6_ØïÇç×Ã=\XWÓÁÄ¾ id<ã7¡?½µ.ì_Þ¿³Ig8ø0ÖÏjµV®¯­óq8"'%ÄrÎÞâ¿BhwN÷]!/ <9²e­Z,)Ä2JWÚI"<¥Aw#æÑ`\-B·ø¼Ú´±m¬)Éæjfbøì¥óâôøäð¨Ý¹Jä·sÕîðó÷¥J£,ó}îxt¾á9ãs§/N;íÇ|é´·3_0µç"fXµh
?ÀUâÆ,.¥9¸2{Ô@¶iÙ`éÿÙnJ-Î7ÈõÊ/Òr÷ßwv b¶#â+ÇÖ~èxàé= JjË­Ú¦6læ& &}~¥[ÕÄ?ÕêPi*¾ÓnK¸
ªuSõlû=÷yP¯ý¦ºJÌÀØ£eøòÞÃpRtü¸L¢õ¢7ÚbËFM­ÑõàLY¸¯©¯t»<7
7AÈ0&a#Â8AeHi_:,ÉÔùÕü{]0Wfç_yÆ[MzºiU®:YoJ}ÎÅÖ©PY¬³-ú¾ÂÛÖ+Åpëm±£L,ÏHµ!1òéU
ªøÍðVMðÖMÈ}(~áûÌAâ@.%öt}Üb÷KóÀh7áÄÌ%/&ÐÊ­.°#<ØaÊÐáî£RmÎtVgIÀþ"(¬´±JØÀè"hÐçw¢,l^æT~o!vÐ±2ÇMèdÚ.?OFÆ-)¯ ßo
3xÎ=07`&W¢é/ø"æÒÈà&]|æáÌÈ ®ÉVÕôj:¾,ÀYÀk/Ll±Ìlï¿¦IÕç£v1h±®OY£·¥ÀJM¢âiÂÜ	<wÍÕ³Õ&P"÷_§ïòv¤TU&´£7-IIü ãlZCéÞL¼)Çö¥KÚ9·õû}{4Zo?~KÕÎbÛ
§[ûh.]¤ùñ¡7¼äGûíxÂË'zÐ\§d|Ô<Í%ðy$êÇ|Jva;#ò"F%ííid¨-S´¥ª¡$s½°ÞôìÕQZsÕi¿+@÷ÀýkÓé«Ö3HRm¬Í&{[&Sî$ª{£±î3[9bz¨ÿ+VÉ*@o&.tv¼S]ï||äe*y7'·Ìëç¹tÖMkJKÄ9*q¥÷$Èoõt£´Ëú4#rõQ©ÖNÎ §¦Ù®Õáéø(6J)÷îCO9C[Wýñ:ýÔôúxÂËÕÏ#%7%ÿåóNÚýâÁÉd2xøãá÷1L½á+Õ³RÈDDà;'ñ2 Óðð7]DúPèî%|µ'«ç·WÙ
éÎ²<òÖ@Äì¢³3èGáI`x4¾"gÞ9N	ôhjõµ)¹9¡tßgð<oDêÈ²z<­;6³ôñàMþàw!ÝÍhâÞ««xß¬Ýc¸­ ïvN"ÃÅÃxÚ	ñf .^}µmõ`²«¥]È<Øcv¤¢áñ|ÛÅ,èï¦j«Wê2XuU4¡wy9´ú½©57Zí]z¼Xã5ý{üÅ°ÿÆàfx[¡°^q#¾ÂänFSf} }QRLGÁ "%D&%HËD.}ýÉÅ¤*Ì-@B¦f ÒØD!I9@¡Ô4"`Ò@£@B¨fhZsMîbTìÀ¤*ÖÖÖl©ÃÔ**aPaa03&Æ ÒÈ.	dÒÀN;:)")´l9Ø:S°6/bjã ¼RA4³xUmoHþÎ¯)RS°ã$vs©äb¢óKäz½
-Ëb¯¬Ïn¯?æt*Ýßðë,Ø>äÒ¢dììÌ3Ï<;ñFyÀàÏl1_§æ=KÌßhG"1ñdfâïër½`Zy¼Õr&ss÷dýª9#R>ßÙ"âÒE1/céS¦¼Là¢_Ä/`~^ ÕzÃ¯?ìN{7rnÜñÄéHKj=\»7Þïý_=åßsî^íRÓÌc
a:u»Po´^ù\Í3)bXÇæÞ(pPS[îÝüìH²¤Ä$ÃÿD²dN ä+±
A x	DvMí(`!O¼x*·7¾í¹¬b:v¼±3ºsmÇ»ëôà
ðÚy!BÏØÃ®£[«zÃ°V§M4gçh.ZhÚâ£¡±Ý¬<¸¬ÑçÉ|&`hB«
l·3éüi£§hÎÏÐ´.ÐXm4¾J`wÊ2 T@Áx*Q¨ªh¬fHN!iN%øÒËsxH[Ù½ª´E¸ª0ì°
èüJ¶ÉEëìü´YoL{=£ð}S1ÉB¿mÞè«Äõsp"É°X!¨OÚ­ó³æi£þF½ê¼ÅbÃ$)|ÊÞÅ",9IA7¯x, a¿,+uÛLåý¶çÔf·Õä<-OVÅ¸9ûÐ°>'
Æêìª3sÓLÔV°ºÝK»ë\»çÑ)Ýµ¢ð½¹ýÎèýnþ¢r¦ËéPÐV3´b#VhÏñÐR<<C¼?S.¼DH®Õ¼û]gÔ±q\àÌpíj}SNþ§ñ¥þ7²quºð×A
|7NÜë÷?ãÖõÏzTÿ¡´¬mØÑ±eÛzéº{³Or ´x÷ÛÈ85­p'oÐ9I@`Á"9IÕ^²íaJùl.õB (*JÖu*LÂN6ÇYcÿ±¤¦})ÚÂCÐñÞ@Æ?3VäQVÒU2§	¼rÜNÊË"Ä×R	1ébýx¿erª¢ h¶â(æ½8¢ÿtÂ¨ä}'U^JáJÍõó¶õäVå¹¤'èfíd¯¢FÑ XQY¯ÀÚUßCu©¯ ñäÞ[`.ü²ëuV¦VÑiËÆ¨^j_µïÓe^ä
Cx,pZp=³AEJ*LJ%EÌ-@S3il"
Ò`õ©i 29D&&ÔY8¨º4­'¿gÒlÍÊ9y=³D'XOrX§%Ø&sÇÌDH#C°!v[
ØmI·Ym1Ûb
v±Ñfn ¢+5 ¿5x}RßOÂ0~ß_q3ñÉ!áÇ$Æ!Å_AËX(+é:²aüß½ûÐ^ïûî®wýjQ¼à)ep¿gÛU.Ý51ãÍU×ªC\aú<Ã7kwÑªÅt+¢X%U(
¤"±c¸¥	#-fYþdDÆáÌ÷ÈÐø½©g#ßÁäùáqD>ÇODS|ïÝómËÂôpÌFßQ@3J3?ÉB
ÎIÅd,d3O1Yò Lr¸&
ø²,ÀåºðÂÂ H¶RAÈÅ<à@àJ¢dºPEJIkØ×æìá©?[·f*õTðh_©VàÏMw.hÞ¤$Ã4k_r
å ÓÂÆº^
i¥ù/;ñ²S+^¼ØR7³{öÚwû¾×((ú3%+sIÐ¬ÌGh)û#ûjÖ¾AÁ -B§N±_½ïýe¨i·ÓÊê­Û]½WN¸\ZCZ<'ÕäbâYþ©õÑ¶¾­6ªÞèx»Ï¶mÂÕúøÔ´Ì¼ø
.\ ¦¦°âä¢üx"Tj@â³¸¤v³
ãFa°¢¢ÔÒ¢<eÍUË ¬.d´fxTÍnÓ@¾û)F $¢¤!!
H¡5UDÒTmAÀÅÚÚÓdõ®µ?¦)ê·à8pâ¸æMxf×vëñÌìxæoæ.p9Â³+,gÝç²t¶>{³ÑÝÛö9jb«I¨éËiÞ[í9V<CoÚ[ÌûiªB:ÁTóéÌÞ
ÑºÜf³µË­PX¡¤XL²)ê?C³é×¿1¥à6
*ò~~}ùR£è¬£¢Ñä0OÞô Ù
Nøªwarôjx~¿N½Ë(y:{T_\"g'Ãwéþdt
»Wjïÿ:y?§ÇÓáÙprkõ±½Üû7n?Ø;QDY¾rrù}ùMs\p¦¡dÊÊË®``1/`98Çs7Uf\I&:±Ìò*Ås0(ótØqi¤B*íGHéSDð@èSÓ:´mµÊ¾V;ììÕhk4&\§eüpðùç`L>AÌàp×Êý [áR.±¸ÃxAôP+ðáC
®!.QórÚcDSE¸:Ã$9µt j}ÃÔ
ùæ%³Ë
/uªG½Ç½ÅêGn
ámªÇ
îùe7Tçáùóiÿàd2­HÿÃõ¯¿n¹pî¬UÒtàSõ?xyßÙ:ÁO!¿|~/|áÏ&¥ iÓóú&&wnFhÐÕîêâJ"]ØAT3°jRæU¿¢öCÄÌìöÞÑÃs*ª½_Ò÷f;zùÂk6 íµ¾×´V«­vÃÚäOÆFªm×ëz?ËkÊ($~¹Á¸^nÔË¯4oLRiëyìïN{éñ{VÒÑYz2&1V~9y!6iÁSà2§YÑ`\Fóªy×KäÍÃ/zTÜ¸0uÕúØíÂn_£uZÂÎ^tý3xëx{Â3cÂ¼=]¸¸3ósJSRlªr³õr2KâsóKSãSÊ2Sõ2ì¸ôõPÕå¤¦Ä§¤&¦e'«2MÎa¾$ÏÌË,ÑÐ´lÁÒW_Wb_¢PXm«`«PÍ¥ F:pTµfJ6ÁJ,ÅÉEù99ñ¸¤|rHf%äçùµÖ\`ÙÓyù%iPÇê(gV¥æ§Áø?°Kü_XRZ§a¨£`d`09M £vm2ècxÉñ}ãfAF9ÆÍnL{ÅÌ4­¹¸ (µ¤´(OÁÀ« ÜÁ
2æ3xûÇÞÂ1a³¾¾ÂÄ} j3ã& Z5±ÞxµÛrÚFô¯Ø©GØ*'M3v6²ÃC8©ÃÐYZ@,]HÆÓé§äÇzÎ^tC8îC5KìÙs¿î6öIl
Å{ÐÀ/¢ºE~%ð+üñOBçnå:3Ç2m¬ÌÀ$½¦ñ|rçÇ!#ûÊsÇ³ÜØfäÍ7¶ZlÍîÕoK@r
È¸tã9å%<æâ¸þ|îxó¼ð»eyöÊ©ÃmÐÂ±·Ù=ó"zgzæÛ`n±ð«Yi¯¬ÕowKÊ
CÃÈµ¦7gÀ¦Z©ôôjÐ¹îth\tGcc¨8@'¸±g|4z´Û?¯W*}rÝ0,Ú©;±|/H±%PA}INHÇøØ=3hgL/±¯þ côÚ§FónÖ$ý±³òC A¸þ>÷«ÍfÇñqL/ÓA{Ø!Íu³Uy\
®G \ÔÓx6c85sÏá&­WÓc¥ 	B@Ñ9([¯1ºÌËnAãh(ðÌ) íÂí!ÜÊ#Â÷{%V"	X´Y±c±î9¾'÷à>IG á>
9ð¿
,±,ß-¬ÌNdÉ6éÏRvÒzö:ÝÕr=³ZïºôQ``À·qù¹æ<aÊþAT ±ðp\?ôÅ¹ãfÜf	cB\÷ÇôÃµqmÐQ÷3äB÷âÝ¼8¬\Ò«ÑÅÚ1Î»}CdLÆpþE¸\ôù3m§kk:¼ltòRÅû"`¦
®5­%ÊxIÇïF»CGãöÙeN¾Gño5Ì?)ÆF5ñMm32æÞwlQme°ñý¬qà¾©ñq«>¬Zå;ÈÚlúèô¯ÇeDkÕ2¡Õ7g¶É¾ÈA'{\"\ÒóÁ¼3D!=|D¥#ßS²C¢dyX&ôl8JÐg++&ôØÅºÈyk¹}¸W°l¨CZé!¹Ë#(é,G´Dê¹pXfOâõí(cRÄIã!©ö /á:Eßu{
ëBGÞ$`a[º½)îÚìR¹]Ø«wceeÈ/°«yýY]Ù}}	-ë$öÐZ"vØ-ïÏW2íîÈ,wâúðîdÆnClª}­j`÷¡SÐ=ÌrlÿüÒ<\Wué!$ö§p|¨<ðÂwfºî-VÞªÓÆ¦¾u+ã¾´mCsWUÀë* ªÙXÂDíá½îCßíhéÖ|àY7sf>w¦­qâ{N :¼%Ílú:3¢Z/ô^²·G,ò¾Öívv;ä/íWÀøÂgÞ¢AªÉÒ µ"Ù2ÉÉsp0ðª#Â 	þ5C­z*ÆæÌU@»eéÙ~µèÎíÉ«g×Ä¡àøþ89!E­½xI´@×\5-îG¶¥¢½:&¤Ñ v{:ÁàN N'P*§YáDü2ï¦¿´è.Qx
|²¯·ä°×Ó½ND©¹QNÁÑ8d?k»&Ùs+LA÷?þvy"7×2Ó`jM~GsáÃ&.gR#ìÛ¤£BnÄ|+È­bkæ-:!)Ò­ÛÌü§q Ö:×ºpæCØÁAª¢büuÂeêÀôPõdÔÄ%¥êHêm­û´sâæ3¥_âjIÖ«ánHqK~Öªù¾¤¤Ã·G0yÝ»àÿ#bröüÉÐÞüN2üNMU¤ØÑ¼±åpPj°]ÖåHcrX 4à»¡ìäv¿xt·Ø²J¼,`dÔ.Ev*®ºPRxNxbÀuF-µÜn¥$òFà"ïÖQ «á¬¹¨.òzæq|Ãvû·­ÈjäTW<Kmø«Áp&^"ÈSÄ*~Ê)¢? ÚÝq¡æbø!1(ve:oßüüêÀy«/F5¸/2·;xAâ¤hIáÉ~Q²ù<mùÛ1÷SüÀ¦F3Tì¸¡\^À´µ×:xr%{ãùhfÀÊ'`ª8ð{¤|¢s/Ô&Mf?
N§.Î\jÜÔIÿº×þH¨kÊ<óÖeDØÃBg©EL·ÎµOö|'[³5úçm·V^¸¹À<ä![ÌÐB©ÜÿRÞ¿ë¤gÛ4*ù6ô\®iUN>ïc'¸Mó=ëËÃ>$]Ù)
7ávXÐ¤± ÑÍ¤é¥+r÷±	y´ß¿ïuÏÚãî ¯³Aÿ¼{A3k}?ìÝñ
ðùmÿ]@âBSx]=LAÇsÄãø
x §äC	øEac£ '¹Ìí¾Ýegö<ÔÎÊÆ SX¨¡0h,1±5WÙiLLH4ÑÆÊÆØXß,çIÜd³³óæýß{¿÷æÛÀµ¾ÀmýCë×o\_×¥ÇbíZÄ.÷¦ÙR(Dà	G
" 0@Oa~ËL»(]+!Ò9p° úôÑøÙî«Ì$ÒÇÙb²Ã¥ééù,É7§?7sçaò«
%%)nAÈ=5S9ÊpQeÏÌOý5MhKéÍøT&í³ -S%Ü(r\&ùèÑG¡åP``+!ïÓ_â»ú|MB¬íÕ¼öNÖå{úáj ,APäM-pÇ°Ù^®{IÂ¾üoK}(Z¸"¤}ÅÜ|yËÍÀ"ËsµÈ\FÌpAß8Ð¥wÝ1Ô¿Ø2HÞbàGØ¤¾Y?§_×?8bí1@ nqæ¿Î5uêlRÑ	ÒUX~VÞ$Î&5jsBD/
E
¸ %*ãý6ÙqS/«V° )¦¿'ï\ Ýi)¹õÖ)?§IPÜtªB+CË÷ÌPÑÌ[Õv»õÝºØ0ê×Ò5ÑVÃÜÈøT`(«ÌLOW&ä}¶êf¡0¼õ«dWg|÷å§ßó¢ñHê¿]êæõûÆÍòÁ
TÅwP	ê.Ð8/5Ý½Dgf¯\ÓöjåÍ-SÀTy°ä´sz#æåÜh÷¥¦£¤k-KÂ^MeòáRïðHi/7^ý?®×RúkªVÿlÞ8d*¬$»¿Æí{-¥µ¡7¥¯µþÑh:·ïêÍ=úX[+l?lû ¡Ê¨ðÛ,s=óB(Hcqo*Ã¥1ØæêÒ5ê¸ß>ûðpvåu}x­UKLÔP
:Cá£xQÀ©~p !Xå#0qlNç
4óéØ¾"vº2ÜÑ\»0Æ¨ÃD£K7&.\¸0.|óv¦6i;ïÞûÎ==÷¾;;·;]G¥D6°µ%lÈ)Ø¨Ûj§/^âk5eÅ1XM'»XhZ_ÂôaxãÓR\I½×JËma^<Xg±99f%¢§¤gh*Ò2ÙrV7Ñ êvÀËY¬§«ÌNGY&1,b
¢äðÎµKI!EGvzaPZ1ieu(QFDIÇ^?NèhPm©(ÎÒõâùYY§gå9qN¯_Qo7)O]¹0#ÏOAûVª¹p#Lmë`Qx"!æF.ÏÊEsPá`³LàØ*eí5lI
¬Äå¸Bð÷òù¸ÌWËÃU¬p¯üÏÁ>ßdåº´ïÙèïReX],,ÌáørÙÖ+öuÌ"DÏðf_+$+6+X5MÀWJRaÙhÑ2Dø­Í/hCy½£
3àªôDJ¿	/ª¦ú]º¬8f~A[;Sd÷ êqÒÈN;z\ý5mõ.È-I¯-O[¿k· ÚìÑ)JV²XÆé½"EwÅõ[UÕðÃ3Ûçä!Ø¿µ@C¦Z¯Þ+uÁçíýâÃ!Ô::çAm8[Ú qïAxç
¸eþîì-Õ¤Üõ5ÃXuàÖ6fÇ-ÄO¾6ª¥©¿Þñ?$KûÆòNà+_³£à}×}vB=0ÃhHâ°ª§Ð =%\âZs¾¬MÇþhfÆÓ[5Ep[¡÷z|!FNÞG|SÁ¼xËßù£tÛØË¬»1ðÔbóç?ëÏyBy[éøHÖ¶¹ß´?¹;ôTú$8Ø±7
óAØÌqð¾º¾Ö6{÷Âµ¡p(ïÏáÀ<£v?pÈAz;Ðä°|(K¬.òjâ)BxeRMhAeìn²ùëcµjI¥±5¡R	QB\&»³tè&wgCÚzÒhù.?=z#xöàÅ«¢·bï7êæsz¼yÌûæ½ïSþMáÉtÆeÍ¶ÅL¦`ÝnbÖâóßÉ4|ç÷u¸ªbÚ¡-nÃZ.y¦I|ór¹4p*p~`NáC2ßÃw°«;¶ei[E8ÿ^vá~ð0I«9¼Â,'n.Î©p)ôTp9Ñ7ákÈÈT6J¾¤íØ:u]Òì+{Uá
w¨Ö´=BK<·)Ð--f|Fc$FÆCýÇLÔ"ì*ìx(@%x-Q8^/iS·M[ú_a:#àÈsyuíªV*g§àGäx¬Eá­ü©°íhC/bUýè¡¡gµ^õz­áqn·ÜzMß ú¦ë5ë ÇÎÂK)* Å>&oÝö=ýÚõ»X³ÙòHîÕ{ZÝÄOøKB1Wú
Q¤}Ñ»d	& ¯,LPî*8<Ng@¼W¦à±2%HÈ)GÑE¸§KáEì¶DkxfmrðMáhVSNû¶×á°mªÓ6·KãÏ wlf@"íýJÀÓ·þÖçxÛ 3YgÄF«lõØd'ÏcgÛ,Á.Á d)åGx{¨ýF{C8#~jYj^I±þæÆ^ ]ïÐè!x{£½Qs$þÄ9º#C'lÊ('kS­_XT_
$JSã2Ó3Jô2ì6W2.gb-ÍÌ+±ØlÆÂÈ¬Ì¥°êÒ (;¹]dr¼ Ûä¿ì·²Ùå|_°AÙ¼%9Àâ¼`ÍzI¥%%ùyÅÿ°)sÀ,Ø|C D#:û²Ux}SÁRÛ0½û+¶a±©-í¡:ibNÂÊ´½h­88GC¡ð1=qê©ÓK¯þ±®+10Eh­}Ú·ïi³ÅE17,]«½9S¥»³Cgëq*IÂEböGùÅï]/höôüÍèKõ4SP¥I~Åu4#)jpÂñ1ûÃô^Ø.b}èGGcòmxB$.Ð;p½=è³)$òï)	HÉ´4B^PXP­ø
¤åïGÜDÐ7ûé9[±©Ã`Ø=¾Þ8<Ã|ÅÐ£iT¤¢ü%b1HIPÈPWÒUòÊ7å6¥L·'Á×a÷Ïçñh×Äì<`|	®IzÃ¦E9_`U^¹¦ß
U9û7}¸2L±<g±?Àe)½f
u¿FçÌ9j;cI¡¨(ïiØk
4Â»(.9/ïË?,.åÏÇ4·×ø´x··ÚÄ
)ÁfW&·5K¥ ¦¢Ð\¶ÑÑÙ+gpoù°öé YE1](¯Áè¢®SwÎZæÛ}Ôië¢Ôgß ¶!"×kUDpÜZrÉñ½E;6èTÌ2¸ÕÐiRYkñjÂãïnuè¯Û±|Æ¼5ÔÚôÀ£K8jp=Û±÷ÔÿS»ò.ÂÇlõÛit²k'e¥`sÞpÖ¬ækºÈ0='Ef¾;®·ÝY;FÔ®pÌäÙæÜz÷Wýùë¡^©3fõ?»­Æ¶ó¦UÐ9Ü9ÃEªÛ`&lÝµYuiø­*lAZ¥æ¬aøæ)M-]wR{Ûsçüî«vå#x1JÄ@Q¶´z²!l­Ö1ÆØ¤ÑwgÂÌÄñêè5´ÜhiíAÌÅ×<xðýïÿÞ§ÇºQr2ª)ÝéøÊf×keWBº)5C¤ÀüÑA±`ÛÀaJÍe) ÂÄ¥b¨åÑïàì~g-¿Ð~"bTs¬Î>ÃÆ^zmÞ·ï5ÑðwtÝÀ¾g D-	koùÉ1:MÒ0¥ùÈ;rãÀGir~æù(J<7²~è¬d«Â¨Õlöòü?³«°5ìb¢$@û¹^c©ùô`
¦§O­®Ó|ô.V;L2]K¾XCãÖøÙè¯¸@x}RÑnÓ0}ÏW\RUJ ZÅxAÊR¯DKªé&àÅÊKc5íth||H;KiX~Éµï9¾ç§ÇÊEQgï¾aßÁ
EÅQ~nõ¶
¾\²ri¾OúëæÝ¯ÓêðüótÃ¸8ìÔ©PTÞ1µÈ©`Ë\Bp¥K¦/©T©BºÈÓrF
rL3qhxÜ²t·Bpö½nÈ,¼2!!@ùö.Ì6ÇÓ0ò±ÁÙVè8^GIù3âh=M.Ãý<¾¢¹§ÕËð+Æþ|~¤A%ðúøÏ±Á_OcJ§qÎÃxâ~çÁ.8¦váå_ìWà¦Û¸¬Ëí¯íO_k,7,m-Â¿£UÁ\DÄb¥nÚ­ëÂÀØZ÷ßR¢ÝF÷àó*RbæÂwô27Ç±
gÿ÷§ã1<©D½P c¤Ïn,éÛçu$y-ØNØ]M¹?'4øàOF&ñõ, ú9?ò:Lsµ&¶ê;î]Ùé*¶FÍ]Wº½¢ueötÊqA­©@#W¤L"}ÞÓøÒ1ùk#Çî¼ô%¤
~æA_ç|v¾ÏÖiu¡NtmïÕz÷`7¥
'`,0h{°{oïÓHnèª¥ùZÖoÚIY²xmP»nÄ0Ûón>ûpÝ¼õú­Äjý¥$¸ûú:MÚ¡í$B"HÉfÅ '»Dá4\©dëMÝ}ày½B¶	
<ÓÇD-m¶á×`iñ:Zî· RÙh=eT®$ý~WïIº_"2¸ÅR¦<ÃXló¬9Æ>ÝÂRR'xg3XÐCÀ`6ñT~CüyÁÇê5<Zmå¨Òfý¢îê¦=®KÕ[ïA§³$ÅËIæ.ù
ÿä?sõü×¥Z°õðP´ÿÈ§C¬Z	f=Ñ<|²Êt¦x340031QÈÍO)ÍIÕ«ÌÍa9´9L¹GvRVÓ;Áz§9cì×H õí
äµxK*ÍÌI±âRP(N-)ÉÌK/±òRâòóK¬ô¸ âå¢x31 âÌÔb1Çÿõï
þöøâ­ðùv±ë¾ ê² ¤x340031QÐKÏ,ÉNM-`x6÷ÑìM¯9{wk®+ºqèIOðD PHÎ/ÊKe*Ða<¨>¯Ã«âÇý­6ïú'XìÜ ¸@¡x340031QÈN­ÌM,/)JÌ+NË/ÊÕK))ÎdÐVr>b¢ÿ"Í%sl®ðí «¦ï¢x31 âÌÔb«)öØÞ1éh9ÛÁÜh±8 Ø.ø¤x340031QÐKÏ,ÉNM-`x6÷ÑìM¯9{wk®+ºqèIOðD þ]o x340031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VÌI]|NjZ^r~^CÚy/³¾·¯úhYOS°×,û`©4¿,µ('±A!öÅ3#¾®®p·ËåUä¨¾gê¢Ìô¨ÉïZLYxéàÉû³ß¥HOPâ:ZÑî+8Ø}NöÌúðê
÷Ù7> Bf^rNiJ*ÃN¡Ça·æ
}¯~º¸âµóQMN{ *:ùRÅµ.:ºò$·]À^üPëÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  'bà
x;Àti£øà×+-ç\û·üJ¥Jíw)¿GFeU âx
gù%x[#|UpÃU 
\3îxUMJÃ`¡)´de×n»(Úf¾¤DâJcòAiRãB)ÞÀÍWp'H/à<x
yÃ¼ó/Ì|÷~Þ_ZfÛºèØl|óiIGç·Î"óc½öRâ ,õ0ý0mÏzÚ+Ò°X|½%Ñ2Ô9Îp¨Ü]VÅ*XsÎÙ¿®p@@æ¦0y¹å ÒpE!.â!ÇcdLö£ Ê5q÷°êäÎ<w½«ªÉøÈ·7>môyÜE4×I-*V7'Y^ëEp¿L³ò~p¹ùõÏê¼?ëSãsx{/pR0B93/9§4%UA);µ2)?±(E/¥¤8SK__!±$³,Q!_!'³¸$5/µK­$µ¸$ÆU¨æR âÄÒb[¥üìÄJ%k®Zk.®
ùL\\ ®iÍlgx;)øI`bÄùÍjÙ%h®x31 ªÜlW±l;¸Bwì´z5+{ï¥"&Û>ý §ü
¯x340031QÈÍ/-N/.ÈÉ,O-KÍ+ÑË`-ÎÒÆ{ÕÛÆ§¾ç÷z^Ý u_¿xmÏJ1Æï}À^ôâ\ ëüsñà¥tgB§lÛ4]Å§ò|1;ã^V7Bòû¾¬2[-PP©OC¨#ÂÕ;æiÏÝ9a¸®ÿ£@ÎùäæúÇmoÄD¬C±*ÂuhÐDªMÉÁYð¡ ÅÌ~ÚYt¬mÌ´aï¬|±'È-T åbju$x}¸[vù$mÍ¸ÓGíþ¨-SfwjxPÖÃtSE(­>µRíé_úÇgsÛ¯ïoú³okõ©^w'l]x»ÏÔÍ4Ádb÷ÄË=  S¶Rx}TmnÚ@ýïSLS52â~HU%¤J "?úgµ±'°Áì:»kSUê!z¨?zô$µ±
YXöÌ{óvæ LËæ*3Èô²yÏ,Føpé4×ÁµÄ¤9m?%j2rÐ}'>¸@IÌ\ò	ê'Â&HV(ÉåY4år±K÷£;u/!½þùE8ö·å6àx4<é÷ØÓÏÌ¥Â«pPky^ÀVVY*øóýÌ Õê­ÛÕXÃá&«_«
¤Ç
"­yÒô´qíº³Àu¼±¾ô£è{f!^6¶ó­Gi$lïË50[]gÖ*i¼µú.F`§UàG3WW¹ªçëèU"$ÂBâÇâeûúíIJpÝa×5ëq^¯þJF/á|B@»
¯ßÕà^-ONZ;Y9e¹¤Í(Q;lI^#¦DU¶^ç-ï÷O»y Û­Q+,ÜÏg¬´:N+­eÐXEeNÕ¡mA=¥ºÜ0G³?Å'ÒR¤¸ÿYZUpÖh3-ÁY+¼¢+^°Îe§3KaËTë»³H_¶+	
8t38¤æS³n·ÓóÆ¡X`\®%kIÃ>zAÍéÿ
£¯äóã)sØ0ò]Åq)Å]_CÊ5Á5|êw×E4¦JÛB
q~¼Í´´o°¶&íHhÌêAÕ~	0«ß¤)ófök{×¦TÞp]rWuÿõz\¬¶[þá£õg; DÝØc!¢wÐóËÎùñ¸vÑ
w¾ð§B4+´óäx[ÆõmB³yn~iqj|qANfI|jYj^^rf^rNiJªMUn¶~ibQI|n~Yj<DqNjZÉÄkÌë¹@__áÑVgÿ  ×Ä¢D(_o2c=S=] .Äâx añöMHÎÏ+.Q(.)*M.QÀªLA+µLÁÝi¸¼Fj¦5Ø°Ì4
ÅÔ²ÉÌÆ;uxRËtíR*t@ôäÌqY¤QXf`Ø4 eãPx{ÍÖÃ8QDmb W¯w¼k«_H¼§oÆäxFQfMk. Àd	î®Px áÿÐÐ MkÍtTâÀ=Ïû;ïo%¬å¼M¯!ÒO¢çï>x7 Èÿ|ÊPÀoíüÎMG³Â.&±^}·¼¥½<±Ä0Õ5:ñëuÀ±â#¾UÃæâex[¡°X~ÂÑ'<Y7°%2n®`÷c|ÃÑvr³ØdNµÉîú\ÉÉÉñy)9©/pLVäâJÍK	ÉrÕOÏ%>y'¹@­BjNqªB5Lfã¶eªåÍ!¿9û#Óæh¾³ 	-%>åÖKx,Ð.0áøÆS;Ùc'0O`b¼]N(3MA£(YÁÖVÁ@S¡KAAaòMveZ.S¡(µ¤´(O¡(Ù« ßZî±x»ÀxqÂlûÉsr&rñ¥ÅÌSÚ_W·w×ç¢ëÏv
Êî,x áÿÐÐ¾bGwvÒÐß@ô6÷J¯!á0í=x;ÀtiÂ+£¾Ãò¼._tÝìÄ.'w±ÖÄ ²>{çÍçÕYP"êç´þhòdF 3xíIx= ÂÿÀÀê2ÌãVÚ÷{å£xëCÅ$²B¼40000 src iAý¾×q§ÌkY¾)¦ý\O$·ïöXxO °ÿù4zn¡bÇ$MÔÉüA6éPn c½¬ýÙF³<Q~À0'§MÒ{©_ëVúõùxCLOÐ}«a¾B-$ê^x uÿùÂ¨íh Í¸KÝeXÉ°9Ã*iOcentral.c #Ï4m¤0Db¨àæhBïs100644 split_mouse_service.c ¹=¥Öî½;VMjìÖQòÏÚ½-ï ´ásûZÕ>ë;¾»ß<*ëòkx[É³c:Óäã,R&n^À,Á8Yuò3­É®¬Â\\©y)i\ .Oã8xÛÆñc/{rj^IQbÎä&åØ6W01NÁ,5Y½8µ¨,39(§7ù+³# ÝOóà"x[,¿P~×dE®¥sÝa 3B$mExkhØðÑbòkv "ª®x31 ªÜl»ëXÒØkißZðøÍgÁVqãF ¢ãçïqx{Í¶m9ãäJFMäÄâÉqb¬©Ö0®f ¤­	õo,x[Å¶mC#SbñæÆc *%³x­ÍnÓ@ïy¸Øà6?´P@²h
Qó§&EÀeµµ§ÉÿDëuåÈ[pãÀð}YÇq\C%bEõÌì|3ãÝÙG"p¼ØExy³ÉRVE0Õz<¼®<ÚÕ»8þE¥$Þ¯¢ÐÛQùÓ*Î1PÌç£,ªc.nr&Lñd7¬ÌCT0BÉ·¢ÑZºÌÅ«xL*j~}û
¶+)Ô¾ò Ð\¼´°k.ÚØ~gõÆFü©{ÎÎ[»ö
úÃö¨Ýï2¼±À	==7áqnõ0´Ò¬T(¸³8¸ûq÷=/'¸0ëyìsPèx¼)®óP¸@©»lK#:a
`ö¿Tí"áÇW¸Îl£JÆh6!)Õ@bQ¸LÖOy3£Q3÷xÍ½(qI¡§îõ¶Ê§¿uÉ7ÉîÜe± ~GH£¢x4wwaA6]fU(CG}an)gÂÚ»ÌåC2¼Jmõs8ç^9Q&®yCËä«õtÕ¬D$¸N3ÏÞ*|«ã¨[÷ëõJý¿ÚÒ+áÓçþSÏô;£2Ì-£4¸¸ »Z>Zú,ªín¼F2¦;Êuôÿ4^× Ù4`Ðs+aGµ¹nöwÝºÙ¬VyN­ø')q¥¨
²;Î¶hö\IäÓfT/54(Úè Õî½·;å¸§çî×ëw[ÝrÜÆ]ï7^ÊyÇ7ÞÏ~k·{å¸g7ÙîÌ¾ìÊqÏ5îóptðØSå¤Mþ'i6ÛaÒ°Ó~RÜý¤[ôg^hæz¬¢6öX5!_®¡ÅÙÑÝ\²ÔD55èf"<#¹Q¶Îx±][p@'@·N¥ ?S·¢Æ¿Y¹¹2êµZ`Í9½»hÙ§ì´uÖîµB´L¸TZãÈ*fbAï²ÓÉQ~Äø
70­×áÖox{Âs{Ã	¦Í9Ìa²,f C\Ììx;È½g:£µ¾¾rf^rNiJªMUn¶~NjJ|JjRiº^PúÑVÇÌäÌü¼TÔâT¨úÍªÕ,Î õI9yÙñ%%©Ey:
FÖ\
@PZ	5ÔZÈ/J-)-ÊS0°æªå ¼+îx[ÀscÂ¼=¸¸&k1JMNb4bÉÌ+QüYt²óNÁÔøÔ¤ÒôøÌ¼Ì
MëÍ9&ßeäR ¢ÔÒ¢<k®Z. ülî¿x»ÀxqÂlµÝËU>Æ/3J?ÕÄ¦î¬®;q½" ÄÇà`x;Àti£HnDõöÿ/¶ìÌ8!ª³ÎóÓÍÉ2* ÙÏ
_¼jxTÛRÛ0}ÏWl2äÚ@;ic M :½£QmhâH©$¦ÓéC§ýüXW¶cãÀúÁÏ]íÙ]i?ßÙl¼P	SÛãW¥uSÀæÜg3¥+×3.×ÓI%¢Ê}Ã?&_¥66âÁYsxÑþ@Þöº¨Õ3øÓYt¼gÍ>é÷ía»wî(yS_.8víÂfÁ{ktK¥J#±üµü)FßxÈ©UÛu4¥`Ò6Ôpæ È-s@Ä®~âoKÏ}EO£HËr,QsÈÆlúiÍ¥ ±ûLuÈØÌÙ«ºÿ8¢¡#bÀÍcÁîbñ}®}
º^°Ñf\H`zÆüå÷eA÷	AJ&|&1MsõhÍ:"é7_ÅBÐ(Û·F;,°iÁ8«ptU7æÛç5´¼÷í·i
É7tðsÞkyÝæ¯ëØiªº9ùåSäé|Î³$Â5Q8×ÅL¤DJ´nV9ÁìGü:R,¦s½'ývô.ýËaÚ¬ÌG3³Î®¥¬+Yö­þÃ7éëplØ¦
+4Ñ"$d11É±àª5èÚåH¶v4øT< yI©ÓÞfu¿?(	x¤ÿúóö<p[ÅÂìÜmM¢a/1öC«ÖSúqÖÊðAÐ)zZ°DxW@wj	ÚI´¤ãq3æ!'>Ê÷¤õGÕ~¡­­û¬´òg+JaÎuDÃ)ÁW\­¤Yþ/²à]I(ã
W[Ý(Ííí Zsåo»<p®ù©ÎûÂ¯¶n!.° ÕÕü­l÷­Én:£¶w¨QéêÌá.©Ô^xÍiyÇísÏYLÂlnµ¾[^Ù2_v»Å÷ähüHÊúîÆx áÿÐÐ
Y)Ñh3IÖ¡°	1Ç¯!Â½¤íJx;ÀtiÂ+#Û.«>X}Ú+îmÃ¥__þgt71 â¢dÄXEµL½+ñ	­
êbÃgÎZ6YQ -ó®x31 ªÜl:÷£-«RZÖË-2¼Äßn 5
ç'xg ÿù¨A^ ÙQ	õ"n·P³d¯|9ÊQÂ	¦¤ßÌ/4zÿ®ç;Í lì½pßc!`uÐÉQÖQË<PAëà³Cí-uXú#,;¾tH.çêvxz ÿ¨¨âñ1Bªj{¥ü¡lqAßJ°*@SýfçïÕpyfÛ¼X100644 split_mouse_rx.c h)ÌÀc]O&ÕüÞ-[ËÈUªËQù¼jLók?¶Cþ(£½ê¾F9åx[Éó{ÂNFåÉe¤!¬LUnv|n~iqj|qIbIj|rFb^zj^2²ÂdÆß³Hmvf*e,ÀÆºù3# N YäRx{Ä}{ÂÎ»¥'0ÊLgfç-ÈÉ,O-KÍ+ÑKæÚ,Àx Û×îÊ!x áÿÐÐ¸&¡ÄÏêZú?9?ùTLãÉM¯!êñþàixp ÿÀÀ?`§)ãa^û×!ç«i*SFÆ=S³éat¡s¾DoÑy7çÀ*2ÆD«÷r¬ÀÐ<ë,I"&:40000 src ¼ß%·°e°_ ÏØËòô$\9/^®x31 ªÜlo³&¤P[<Ã}iÑÚÐÃ;ÍMì «f3¯x340031QÈÍ/-N/.ÈÉ,O-KÍ+ÑË`øô1EÇçÁY/E¯UmåÅgM éB¶xSÎÌKÎ)MIU°©ÊÍÖO-KÍ+)ÖÏÍ/-N/.ÈÉ,éeØqqék)¸¤¦eæ¥*ä+EóÒsòsrìT-}®(_ïx×0W¿xW7O?W
 ñiZs ·¦)PîÍx áÿÐÐÜ2SFÎ©UÚó%Ê®v
ÿçØ¯!Ò=î.x áÿÐÐÕú¼¸Az#<äàéê¸ÄqªÁ¯!ÿW4î,x áÿÐÐ§¹/×ÿK¿Mi|Õå¼Óú÷¯!é×î,x»ÀxqÂlr­E_îXnÞ-÷uB'Û/ãëÑü
`àbxp ÿÀÀ?~Q?B^:CéQÈdøNKcUÕ¼SFÑ³vØ&»åsê²x-8tgÀ*2) È éâ|C§ä>5C®cákÛ40000 src 'åvÄ@Ï·$=Mà¡ÌÆÅiF$÷×1_âxR ­ÿÀÀ?`§)ãa^û×!ç«i*SFÆ=S³éat¡s¾DoÑy7çÀHA1ÓTe­/¼å6PàTà(S­ãN$Y#Âí`x;ÀtiÂ+£c.«¿­9ÀsAÊFdÎkO%5+ P(.Jf`{à¯á~ÿBOãÏÕ/fíàz{e²£
 ·È¥(x340031QpöMÌNõÉ,.)Ö+©(awqË·iË~·óª¸oÎaÈ­2¨LIM*MOÊIO-KÍ+)ÏÑKføþ¶ÉÌ HsõC.m¡OÞm_Øüü.õE@õzú¬âóì´ãß=v¯ÕBÕçæ§Æç 
R[óên|öÇ'f¬ª®q÷D¶W,TmqANfI<DGQPíÙF7{gÜgOfkRL(½Ð}2ÚÚOëtÒ=o/³÷¶¦lß¶ÛMPµ%©Å0¥ ßàû{Uíá4Åm]ß1O{þS%È­)¬OE$7­¬ª´Jôþçc]÷¬ *K@*ËRa§¦|÷­ÍäÖªS}sÕþÎ<tU}Ï:2Ó3@ZÖß8)×¨; I_.åóO9ÈZRS3ËR`Vý;±ÁgUëÊ×3<÷O¶;Xùó{Î&¬êaä/O_1sÚË	^¢òZÚ+ÿ¼RDÖP\Y7Õ7sqå·ö	A%ÏÿÌh9jáå{.Û¹Âêõ»ª;ç^¸¬Ø
 o/ç	Mx hÿ´A^ ÙQ	õ"n·P³d¯|9Ê*xC¾,E(" kAÉç gï8ÛÖ100644 mouse_split_event.c Â	¦¤ßÌ/4zÿ®ç;¶D²8(²Jy	[¸BÈVÎÈ´¥Ë<PAëà³Cí-uXú#,Ç¾¤A¿rxUÛjÛ@}×WÉºq)R
q¢ß°ìÐeÙHc{ñzWì®r+ù>ôú	ù±ÎÊvpÇqÁfç3³gGûBe²Ì>Ýc1¹3õ)òíäs°¿z<jìÿ}|uÁlZÇkTÍ¸âc4kùË°­[TVV=½¸¨ÐV8¡³;dÙ«1æÎQ#8évÎsö­}ÁÒ^+¼@VHáXF4\Vx¥]ÜGQ´ºç¬Ý=¶bÖÏt÷Ã¯Ê1»X[åó+[ñeÜÒCjBhúÉvÒm¥pØxzí.â¯íãëuÓdt;¡Ñ75È´ ô÷üýB ^SÌ$7üñ÷ã/
aa´{üãD¡£àZJn³7ÂefÅ¬¾]F'.,rmù@À5¸ÒZBaÐZ_jNÀË[!7P' ºö÷åó2ß=AÅLû³)Þ½ÈÁÏ èÚ"qÙ8SbtD«IMÏ+£Íç¦Ê²EØxGrwFqi+HBLµtÑeM¤È¹DÆ¥ÛÓÒ>(ë5AàÄVaòS58êõûyH äùÌUÃ½ì¿6¤/CîtÎÂ=øÞlÅp7ç? ­ð Âigæ{Ö< RÙ«ôÒ6!
/äöu!½2TÈ°@ÞYØ+gsÂ÷^a¶Â'po·ì'»zl¨¦Jß¨»+ð	~î	®4ªñ%ýâÎ5M8ò¨Ô >êÒmA
ëP¡±tRuF'yÃÕòª³:¢­=w1©¨Æä°ô^5§­[²HÔMæ§Ë®ÌÛÍPñzhúC²¸sLm;
×¿¬ß¥ù}Bí·¢ÿ(`ÎÑÈañøjwVªìVx[Ï·oB&ibQI|qyfIrF|NjÚÄj©N'ÞUÌÎ¸]__¡,?3erP¾d²ää­Ì@Îä*&?0})³³óäx6ÏÉËÙ: 1$ Ý¾^xTÛnÚ@}ç+& F6¥©ªDÄ¬p¨íËÊµXá[w×Zõ¡ßÒOÉuÖHRÅ²VÞÙ3gfÎºÄc?ÌÎ×¢º@cøqÞ,¢E+y±7CñÊ±¬Je"X¾{î4çÁscæ	ÅäWþ8}!,÷%ÒIÜyªU(¡â	=÷ÎÈ½v;­þÕ Æ8ãÉãúÐÛÎ 7t»­«ö+
¥ §<Fèµ&#÷ëºc¨íÌßz·ìÖùÚk
Ùp0v'î oä¡~Ú`éoÊÑïÁÒv¡ §¸Ë@ýØ×VÆcõ)ÈQ¶íWèÙïäQzÊºË[%2´äLuJÉØyøE2DL­³Ýx3àÔeHã$T/ý.ìJâq¨»ó=IBàr3Ôó¨òÏÏ¨¨4Û¢ªLÄ`	NÁªgpqçuÛK¨åÐÈyÏô Y°
Ö¨Ø´­¬ö¾×»nLY°K´Ùú'r×V××#¯5yfO§ek|lBÚ×æõ!ws/Bd2
¹2}!5ÄRé×ÜÍç[®æPÒD}ãCD¸¢y2
Ì'ÀPN)¯'Ùë.|
ÖIºÍ°×­fç^§?aí»v»ëªø,N¹Åð#Cÿ& õBNJä=%;Ö@ú¡¹%i¿N¢¸Â<-ÝTKòI>ó" ^FÄ÷9o¦«V|>5SÕ¾~öUàTëæÓ0ÝÁ
»jßXÅúÈÔî|~¦J¾|Gb\ÓZ¤+dii¡Ú/ý,ãXÑ¤ô»øß(¨$mïºãÓwFÖK1ÊN\{ÿVÕ!ã»ö¸3rùê8Lkæ(æÑ³äÊ¿8x}R]o0}çWt%¸¸ùºÄéÚ3?öÒ0¸
±VÓ¢[öß×R4~ 
á¶÷{z{ÚfÆb'Þ~`îyg}IûVó¢å2cK/ðõª0IÖÀoÀ¢³ÞäØÒL2¥¸dg&!vG)mÃ1|¾k£Aà¿\ò5þ îá9öZ]ËÊDyÄ5µOa!m©¡ÐW"Q²k-÷gKó
¥¤6YæUö;rÃ¥w2Y¬ù(XBç*{°cEHÝSÕ>AÚB¿¥äyl8W¾(vz(¤¶V×´»@öe=8È3¤­ÂsõaJãxØüYeÐ6×nCV@r£d×{Lgúpåd^æ+_Ô´Ñ>ö¡Ï}å¾{Ö®*¬Òþ¾×ÝìÍÚ.4ïÙ£¬)_~þÕ+$4ðvÍ+y]:9A8úÿvy­ÓJáÌ0Ûë¬ex;,´Â×ÍzÛ's³:±ÈäV0ýJ§±ékl¾+;æ¼LsOå\Çq røï
AxÛÃ?Â¢G½sRÓ&0^Óïý@ôf¦P&NCMk}ýÂÉl÷³HD@"å@åÉÌ¬2 cH*XÄ"b)LfDJÀ"w jÌ@"@{ÏÄ+òd&§²ÉD,@"@ÍKØ$*p®x31 ªÜl¯Â·}]ÝUøÚÖéøÿ	¡YR ½
î;x{Ä=cÂ³
'§1+MþÈT¼x3ãdyf¶Éé¬Õ ¾ì+xÏ±sÂöÉ²3JMü$5ñ÷ägLRç1³Mg2ÑµJy*ãsóKSãsòÓÓ'?dVÊOöb<U,¥Ì¥  É¦¡É þ³áïcxO °ÿ«	´	!#J#î# û86$Êç{¿mouse1$Î¨
)
endif()
ÚYá	]xÛÂù{7ÓäkR|Å9%ñ¹ù¥Å©ñEX4'0ió¤ÃDsÊB)©I¥éñI9©ñ©e©y%Å`aÍÍºL½ÅYd¸4LægQÁT_4ù<£"u% ëT&3±l g+2¥±SxS]oÚ0}Ï¯¸-/IÇÊC5­£LZ
"lÚ¦ÈK.Kc·¶C¡Sö[ö°Ò?¶!¥tªÛ÷c{¯y ¼½Ãët©ü*ü8=sÛP>óqÂD9ì'ªgÂÚ×(´T]=¥Yòt³`ÊDú63qqî¡YD.çHBcr|¨Tpx@ãS|zÝ«ó!}èß4)½á`\vÏ%îÐq	N30èNÆÁç¨7¼á¤]m\Dý/î(
Ã`¯\%oKî[Î=8zÄ~nôGf²æ2KòD3\ºE&ÌÈUÙ,¬Ú/hÔ³ ³¼àÌ¬Vç6Á¨½É÷H¡ÖLYú,Ê5G¼vÛ-¯óbÁ)ãÚ*`(¹Ù+vïTèÚ2pê&ãB R­ÖäìÓ³UPÓåã¦N% ý½¦£Ý K"ÇdSpìæF¶
M¡´:ÕNïvÚ^Ç÷6t¿R©¢­&ÑåZ}UdA÷°¼>É'½(a}k}?3^`ù=é<¢,_@i¯MP{)ËèÁ´þHÀE¦
	 ¸¶û²æ°¿é½mmwbndÑ\ÏèÀ51Ëé 	©TÙñ-xùxj^¶6Èªc%9àÒD¡Y"á^"ßû/oQçÕ Pþ(¡ÞWS:bÝ¨WÐMWlëO.ßìeNúWý±»ÎÍ,ªæ¾®%~|öÆÁÈ¾ñ]ÚnGçÛÇ¤¿¼Gx}SÛnÛ0}÷Wè=xuÒnÃ°tÔMºqËö"¨qdÃx[}Ä¾p_2ÊI
']gE<RÎSiØ*+52³=O3©´Wß1_TE°ÄBaz¾øòÒfó¹Ts»øWË ×¨(3W|Å+näFfiÃ
²dÁÕ;QÜg÷ñõ4
Ù(ìÆpäÓõ¡o}öíþYx~
#¯ã8A ¡J2*&¶¾¨@*MlS¶ÌÀ¡ºc«Ë`©T
?Ö9ØÊ%ÛG2Q>8üVüpçRlá3¸åámçÔ_ù«¿@Sì~uíü´ØóT÷òP>¦DoVªÄÒj&ái
*¨²6\kÕ¨Ôã¡oÝÙ:âHeùo3ÚebDbÿVpMMìÀö9×YY$H6«ÃC<Lñ'ÝIÈz·Ýa?dãx:ê$R¯ùH©$6ÌºäiJ`éÏÐÈRUNÈ%+s»gs4îôDgÁ®4ÃKY ÔGþüú
¯ô'5Ì²bÃAÇj7>âÈÎ³Âì$³éØëCrqíäsëçé'Ð++!ÎÄ¤@.há¦Mï	i®èÒÌ }8µ6íÝÚðæ Üf!ép»m¯¡ÍåßûðöÒë<l¥SÄÜm·Z­½ýxß±Éí(ì^³ëðf0OnÞ Âvëâß¤åÃpEÇ_*Û¢
9sþìÒu½í!DxÁJÃ@E	î?ÀåÝÈ`Ó.
]¸ ®BL^!4)ÉdlàNÍÒßâè'ÿàÖi*®ªoóf.Ü÷îyß|dwúþjÐl[îV"E©Pª¢JRÒYBØ1½	­ÛæÃzítPB4Neá~@Bg1&RgJ¢ <V»Íxã¥f0	edå±öfNèmZ©¨ ©,-·Í&ÃãÓaþQtÎÎ8Fq^Ç :8	ü3?p¼ÕÄìvN®ëV[VI"Æ4·»]ÇCmBÇx»y é6~~Ê³T¶ÈÿÉÝãè·1Ï~5¯ÅR¯`.ÌÃ<í?Y¾ÒEÙ[}MU¸[°O?x¦¢æ!$xÍ5wÂ
åÌ¼äÒT¥ªÜl} ÏÍ/-N/.I,IOÎHÌKOMÑËPÚ¸1èëO®a¶gS3XdAÌKÌÚPYÌ¼¢ÔøÉUÌ<H@ez}}¸â4
°b[[55J0OS¡¦ªKJKp¸U!µLÁªôR¦+¤TèÀD5 Â áJµ@»ôòsr@üI<Id©¡/©´¤$?¯¨ÊB(©µæ³£|½ã]Ã\ýBâ=]5RË4­'b©wTxÔ6I¡¸49µ¸8êsX Ô*¤æ§"©y)ñÙ©F:
FÖ á°©EEùp\°hSðñw÷ôs·&Ð=q §´(OÁÀ© R»ïLxÃ{Â/
Y¸ôõ&K1JÕéâÄÌdäü¼â §¨4¹D!%µ,39UAH+Ø*¸¸y:»Æ»Ä»»Ä;úEjTåfÇgæÄCTjZsnKH}¼³°«¦@AFú'¤)ä+¤dägdÙù
¹ù¥Å©
`
,+Çn}¼´¿«£«À:4571>gfÒ×,Áªo´ôR*Æ¤Tèp)@\¢$Q$>¹U
¤}ÚÍª"
T\k¤Yõ+V¹ÉB,b¥Ùò'³°©
q%RKJò¬¹j¹ Ñ=èÕ[xÛÀw{Â·L6ó2®ftö÷sótòõðñwòqµ­TPà 5
Në6x»À=gÃVg.g?7O÷xO¿Ðx_×ø WGÛJ.9 _YE±k«H mÞEã=xÌ³oÂ
&e7î³ ©ÉÛYÍ@Ô[Vµz.eÇÌ²D|âÒ¤âÌâÔÜDTÌ¼ÒôÔ¼Ã+2óRò¢R2*¸ýýÜ<Ýã=ýBCl+¹M(ÈÉ,QH²R2ËRªr³uÀé¥J¡£|½ã|<£A&`Ä;ù¸¢KíHClÕð/HÎÌÏKÌÑQÈM,V8¼«$3G¡ ±äü¤ÒtÍÉ«%'Ë1		£1 UÉXëØMxûÎ¹kÃwg.g?7O÷xO¿Ðx_×ø WGÛJ.9 _YE±k«H «µî?xÛÅugÂu&e×9XÔäû,¦ JU­KYÁ±$³,Q!_¡¸4©8³¸$57Q!%U!3¯ ´D!=5ïðÊ¢Ìä||¨ÔÊ".e.g?7O÷xO¿ÐÛJ.d3
r2KR¬¢Ì²Ô"ªÜl°Qº`)Ö(_ïøà ÏÏD'`au$6¬ j¾Arf~^bBnb±Âá]%9
E §&¦kL^Ì¤!b+P7 YÓQ¨ )x340031QpöMÌNõÉ,.)Ö+©(aH:á­¶ù¾CÊºôßýò²&³
!*sóKSã*âsªSóRô>=oÞª5¿¶W9¾Æ4ý1çã?Q$¤"ëX²ag¬æ\Õ«ìÔ64]Yé¢£$µ¸$¾85/lÁ4Ýu÷ìxè*ó­ºÖ§ÿ)gªr÷h0-;ûúèf¯Î]!Ös$;ôÔ ÊÁææ¤¦ ýrÖü\7OÃßÝlúxªwgÖ{?deEé ug#Ný-.¸ÿiöL!cµ¹Û?¤ª+M,*ÏÍ/K p\ó­ÍäÖªS}sÕþÎ<tU}Ï÷ÐuÀ,áN³È_úÖùÍ·Ó¡WZ/°#[RYZ³Bìß
>«ZW¾á¹²ÝÁÊßs6aU³ yúÓ^®HèôM×Ò^ùç"²âòÌä¸ñ¬¾+¿µOj,yþgFãÈéXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV¨òªÜlhà@RArFb^zj
0\o)g&)O°­­/L>¤å²ù Íe)ìSx sÿÜO7KãKÓÅ?3uÖWgãÁY;r.§½d\²½VX100644 test_mouse.c ¯ì¿;w
ÚkxåpÏ2Õ8Q(ú ]ßÊ4
ë­zê³UußáÚU¸¹Ä~-+§ü/µø\
<Åîx^ ¡ÿÜõ<bµ«Ck1bD &ó100644 test_mouse.c ³vv¸Îtúò`½Ôê&õ¥tQ¯Øm2PSdó¸I¸lé¾Ý(S²HxS]oÚ0}çW\©
RTZ4mè&U%hF+ ÓºËJîc#ÛÒ_³ýþ±^;TÓEùð¹ç	Ê2C¸~ÆE¾6-¡¥«ùçÆÙ1áR¤øÈ|£Q( bÞÂ%*Ç
®øÍ)\rã]	æÌYh5Z-èêåÏËo
¼|Rpn8 Zúï²àà0¼aw"¥XTã:*r£W1ì~R-ð«tÕ»ZQ;¬ÚG!Bcp¦Äf¢Í½AkVÜü9+¬D\DíËfçß+þäÒTq¢¥{³Ú&?Í
òH&Öa5<)H³EµõX¡KK¡3ò <PÄ'³Å\¨ùe/Cè¼ÊD®vºTl*26InïFÝIÔn­=Näèî+j£RÁAo	Õ,i: 
Þ6÷¥9W3Ì(>Õ:R¿.²'Z¾ºO5ëÎ¡ÄcO4¬ éÈ)¤Ô^4
?¾ê¹ôËoÉhÊÆ7ýIáòhÚpZÁ6þ%#:	1ôG÷Ù÷Ø®67ëÝ©Þ¸Ùù"1
,wX¢^cê"]Ã]ÌÞÿTêýÎgÁU ?àÍÖe·4#0X£1`Ó/ãä¦ËºI¯?J¢yDæl¿OÃèa8<|~Óx7¿ôîb£©x340031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VÌI]|NjZ^r~^Ã,æ¹{®¯{yáC@GTìÙ/»¶~ÄT_ZXÉðz}ï~Ï³UüïþÝÆõùÆü³¿§£¨.ÊLÏüíIÞÇkÌo_Ön¸¿ÞïÖ!ÃM±¨m¥k%zPbÛk_w{Më{ìa»ÓÄ 2ósJSRü÷¼¨Ôì(þyw·BÇì&[6e¨@'å'¥è¥g2D=ñÚðÏlölu~óå,ÞQW4d!F%3Hîþ¿%g£;^\¨Ïýû¶o¡Æ§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  yª®x31 ªÜl"&Ë[}SXzN óâ` 
úéä>x»Ïti<GIeAj±^ÝD^õ!ê<%%©ñÉyé©)[ü\Cü­@ÊRRÓRòRËRóJróÓS&^®çGÖ£iÍ ± 
àZx;ÏtiÂ#}}Ì¼øâä¢üø
k. À¯Oæetbââ ½yê·&xÁNÃ0ï{P$NL×ªx Þ e7Y¤qdgâ©x^$]×ô0	«Äþ¿[«¯!ÞbxGçOA.©÷ÚuÖzQÏOív®
a.mbéZ«kõÆØ2)tØ(RyDÌØÁU@.Ãâ\p¤è¨÷:àÞBVûÇ¬ZoU3Ö÷ã<¡(OÃ\Ä·æ09ÕçÝæ8Y]Ð¤`8N*Ó#yª<Ì®ÛÒOÖX ¸Y^¸[`´` Ã)ý»Ê èØaªmZYl4çuÅõÐ lõçêvvÜæFÚ3uøýa¤»	>~¼f²
¹Mx}SËnÛ0¼ë+¶	(=ÖµÖQ£~vR½´´Ó¤@Q¢_ÓOéu)JÕZîpvw8¼Ne(áó;fI¥»ÔÅC2ô®SBÅq*ã.­Gùí¦;m¹ä1êÓôûvÃ¶ªÈådaÂeÑ)e©Tü4¤gð×TVí°¡¸6tº]Pgu'PÉµÒ[GÊó&óg6?¾Mö&_O-w`4=ÙÏé7f!à{0¹í{Ñ¸+n ãÑÜp
µ*R´×³ã¦!ÐDn£_¤¹A+É
Xî0¹_Ðç¹ÑEè0gT$üÀsvAfø¨iËG§kð?à®­@;öÓh
-¡×·7È¿ M)0iFÿyF!	fOî·#µÒgOþÕÔ^±;ý	¢rpu ªê%µ°*!	½ò¦÷ñÇU§&·ì»ûaTvÜZ¹µ¥:LC¶7îÆîYc¦´X¨v ºÓºÒ¶ä°ÆF
ú®YõõØtÖnÖÈ.å·\x?\©¨zXéÚº7B¿.vªPÕYT;oÃÕÿÃØò¶QÊvàzl6£XÇ'(W;³},§zIÚAt¨ï1ê73^¾³`áï»¶õ~çÒ IíáåÛ×åh1~yÏg.øþ jï/x»ÉùsB2RUn¶~jYj^I±þäóâÌzJÂY »
õå+x{À¹mBòÄuRg±(UåfOÌÌÇh¨X\X¬W¢_ZKOÎHÌKOMÜÅY¯ i
©e
Õ\
Pàãïä§¡äZW4¥ìðÂÌ|%Mk¸¢¢ÔÒ¢<H-L§§/ÈFÜü²T
[ÕJ ©¤£Z¦kR¡YS*Nfev\Ì,ÌX19Y×¢¤lîd-FÉ±,b8¼1Å ¦INØî6xeÁNÂ@C41á¦7'11m²J!¨ôP#ÁP8¨fmGØ@[ì¶c¼#õ¼zõæ3ø¼NQÆ9l²óÿ;óï÷¸ø±0µÛMã ½Ðr¹ÇÛ^×GO«/¹ÄiÂmvä\D¤p}©ÈÂ/QÒ[?hS»·5¸Vê²#zêæìW×=Ä¾Z±L£X¯L5«iyeJ2:ûñÅµá\Á.èã÷äÎÎ`KËC:
Ç0¹»Ù(¥?õ¡¢R¾(«yÐ0
%«dìkú+«pdôlýÿ Z«Zý{n3÷ë3^cFgÒG0cÛHLì·g"&$i4­- p2Äo'ÏÇ!r¡'¨ïQbÜñãÙ'¦µgå£f¹^¥§l¼\£ü¥§è\xûÏÞÃ<!k£ádm¦É[­j¹j¹¸¸ôõ<srRsSóJòRË|Ä"/'3/;µ+Ê×;Þ5ÌÕ/$ÞÓ7ÀGcr8³¦5 ªQeïx»ÀxqB)çêEñ·KÆ.¹\Âá*pôJ¡($çç¥e¦30Yü×Iq®ix,tÂÇï¥Ýë'®W (×ä x340031QHÎ/ÊKÕËN­ÌM,`HnXImÝâb¥kþçÁ>VÌI]|NjZ^r~^CE~ç¹DNuõOÅ*¢NM_ÒwSi~YjQNb%C××cµS8>Ù¢{¯ÁáÐ2¿÷sS6 ¨.ÊLÏ¼0ÇtïÔ2U}µ 3]1ïx,jaFÿa¿`å-¶çÿåKEL01 Ì¼äÒT}yLÏcf]»ÈÄðèhCTïòÉÚÅEÉÖkÓ­¦^Éb¸h),ÿ $ËØ9×j]yjq^enCÇ±&Í«gÞÈàW{Vvpí×Ï|f t'}àxp ÿÀÀ?G¡;çÊFÂ#:
¸(¨xVH SFS£iªO°OÐº;Ó3AuÀ*2_gðõZ¹Ý8h&V¦r@] 40000 src Eo_ïó*UÙÐ4±­SnrûÖ$^×/&çx7 ÈÿÀÀÈWDéHÚ½ÃÑîV3C¨Aá¼Ìb2Ü,p/nÌÞAqþ¢|øeãjÑÏ7$r®x31 ªÜl2z³9öo}ÎÝ÷æt#Ç³Ù»º¤ZÙ¸<xR]Oã0|Ï¯X@	*¡â	QÔªK[/îÅ2ñ6Hä8QSÄÇ¸¤pw ]bïîxvÖÝTFY)ÎÖøÔê(Ëã81­~rîìvõåÓV(5[rÉcTÊ½õò-ó²@Vh®E	1
?é}â(¹2yáBÎ¯Ùt~yì2¸Ç7kHûp1]M®ÙïéOF0xBoè8©Ô@]ç,ÕìQ³ÈS<c
#L+t£\J;a×¼EºFe(=çÅó¥pM;£¦/ÜB«2jÉÿ2ç5Çè¨B]*	Ádö0&J¶m¿æ#²Xß¡=où¿Á"Ñ¶_¬LLÝÏÅªÿ.Ýu¯·òE¤ò,cÝ©MâOLÇ`1Û<¥ÖæÞØ¸ey6B°òäÂx©qÁîÓ¶6û£ì-fwìf<¹
\¬È41d2»r{S²#´ÌUÊáGÀ-åÄj´'@ÔôßhßÚ7U+x4Xí
õºñ©Qnn³YêfÙ°l-Àòlä}ò¿þ¿LÖ}¡óê¼m:ç@x;Á~}~jYj^I±þäFñ	Ì f5´>xuSÍÚ0¾ç)F¬ZmÄOµ½¥°6Ä²­Ô&³Á"ØÔvÐBÅÓôÐÙë8!h¡]2Î|cÏÌ7¯¸Hò"E¸Ýãf¹Sí*ykùÙ¹ºre\dm²øzÕÆ-
ÃÖ±3Tgpc¿^±µ,42mb,YÆ"Ã´µl8N8½céè1ôÙÈ¹ïR¸Ãi4îØ÷É=³!¡ÿÕ=Çi·a\?/¿%¤1¥Â8BÊõ&V1H
ÔAmPfw¶§ÕYU]ënÂ/h=I.8ô¡Û#sÛd¯¯ë¦*o4F%ÐéêBmW+}&÷Ê,Ë:wÿqêDÉ<g6¾sì©KèGaú9cu2b.<áqÎ÷1HXq¨ kú1|#i«âUI<Åm«
oìR÷¶÷jæo°pztN}5³à[ÙÀ¤ÍL?¥µÓ§ÁG6¾[+º!« »ÕVU2¨kL?AúÜzîÈ4<i Ù½¾©sÄÛít:ÍI¨7H2êÆ¬a)ê¨¬²s(Å8Â'.NJ´É¹g/s0"]Èw«ðJxSÝÎï_Qz=áÙ÷ÔwÝ¿}ßüÌfa0,iTçÍ©GjÊùZl(Yçx{Âþ}B:~jYj^I±þd[FñÕÌ lIT±Nx}S]nÛ0~÷)¸+Á«ûÜ.Ô-¹IbØ0Í:Âl)d#éÃìqçèÅ&ÙI/M ÅäG<e<ÎáË.æ+ég"MO­<_;§=ÿåc\r¢<bV¾¹\
ÒT#ç§Å+äJHRi Úª¬Á÷äax;rô£Qàýáà.¼'ß¾§ ê\9ÍÏb`\CMH/IÆFÒW,Ùº,
pÞßSE\cÞ(ÈàKèUäÀ5ñ®ªpìÜXv*Åº,ãàÉüÁô¦½^ÚàûÐBClúéGB¡ì¥î	¤È_ÿJC7dé'«Êwö¦·Ç$TSh)ÝMÁö4+Ð>¯¥WË¬½
´þªu¢át$ÒÎºÏ(öbX!Ý÷+éxMñÆÿâ°XXÆjÛE±éëÊ¦
c/VîÙnáí¿x[¶-n&õc1ËX¼×.W¡|ýÈKfÈ -´Èí¤ÒÜÌ+¨EÆt=/õØ	ÝãÀÝñÚ¦°3îÜ;0ùvi¡û1deÿU,EåÞ½zinÄIÓD{Ú¾Û -mcZ]ÙRyo®×Smh8`ä¬¤w¸¥&®õO{ãþ(|ÃÁ[~GÐxÿøót´PxTÍnÓ@¾û)öâ"7'¤R¥È"M¢8E-ÕÖÔVÖ»ÁÞu¢^y Þ qèäMxfí8MiX¾xöo¾ùfÖÞÞá2^eÍfE#~ï>¥&(5K¹ä×=?^à*åËçñ+y¨§wé¥ÊäÈrÍ5²0æò£F|ðGUÃ3ÍòD18×¶sá<gÝÙÔ¿`ýñ0vÇq,WB¡r#Q®I¤~Ã4dêÆú#Tâ¾:@Ïn<I°zl)·Ì ¤:3xtRÂIw.n§µüÁüeû­lÒ	!yq±ñF$¹F*k°¦USÐðãºê0'ayÁXÂðxÎö8ï_ÕàÖ¸Ô"4àË(	ùúaýSÁ`E*RA­°´&û
Z5wKÖñ S]À¯oß¡ìC4B¹¡6ÏgÙà½ÑõÎ{½á RFV=ál{Ð®8»ÅúH¢öoDgK
ý`6
¦îËÞ{{fBnÙìà¼ô§þdæG{öxN¹{||§*[?p0im]H4}kòRÚ¢êý¶bíÝÉ´Yºvák×ÿ±e^¹Õö[CÑ-íFÛÛ¢­(ÐÙ	äa¦`×z¶èÝðÑ6ö1zOÚJÔí.5UwJÃEJ;%¦¿ý´ëw£Øe)6m84¿à2`þÈU t'¡ßïÚxÐNýl'V¦°ÉÔOýÙ%ÿ&béfxkáZÄ5¡C?µ,5¯¤XòFñ½»7»1­ddÎK-ü¹* Ê×;Þ5ÌÕ/$>ÈÑ3ØU(Z¦iÍ¥ Å©y)ñÙ©Æ:
ÆÖ
úú
ÎùyiE¹
¥©
ù
`³óÒò32Sò'¯b â¥(ë¼cxTÝnÓ0¾ÏS6!RèÖ1q`LÚJ6EËÚ©ÝpcyÉYkÍ±+ÛÉZOÃÂq'c£PEõÏùý¾s7ÊeU ì}ÁÅ|e×hÊíù~´ù§HêÙL¨ÙÖ?äåõ kT\ñuñ5®J¾X¿¿Ä9¯~À¢âÆ1{#\>gFÌæîñÆòº²È¬ãY>çjÅö|#²ñ1;¿¿Èö>f$&õ>Ç££ô}>=a^%K>$Yïmmx%ÂéÁù$ýÈãl
/wo¯½þIòéôà§éy:ÅFßô!×²±ß÷àù=ë{a/8ªÔÏ?¿kàÕRHÁ
,¸áªöûªäà0<ò@DµXT#ÒâJ(÷9hv&ð×èw&+ÊJz2¾nsì3öÞ6esfÐÚÆ´qïîÿíìKÛx#gÈ->àî[Ôá! *åL
ëP¡!zuà«:ÇÁs÷ 
BKiçAçJ~
ï[öH+Ää/ÀW?ÁºóîÞò»Û]¢°|]Ñç¨4B"ç¡hµ°
BohÐUFïä}Éè^fIE¸½ùÁ©º t­¡©©cJÐJ´%-5ªÑü¬Â"ð|íbIg¬·öeÿ6¿íbÕÝ®îÜÚÜh)YgÑ×5:ëVã®ËÊ9ªZë¾=ßhZØÖ\9æ7´#¶ ¯DÁ>"XÙRXëG¢âÓ²¨õ¼NÒiè~NÛéZuÔ[Ìnzvúð*T÷yÖüà§££x#ñÒ-(Ý0´£¹»ÂÁÖ>ËwO(Vþ¿£íÎ¾¹¿t®6~³é3m+ÖU¿Y;÷N­¬%´úFóÝµ·µCmhÒE¡#ê:O[NÏQ2×æ­¿>ÈÛL/§ÃIzÖ<kØ=2]dý_âçzxÛÃsgÂýÔ²Ô¼býÉÅ7^Èa o	¹xSÎÌKÎ)MIU°©J-È¨,ÒÏN-ÊKÍÑË°ãRFHåfë§¥æÄç&æ%¦§¡H+UåfÇçæ§Æ$¤Æ'g$æ¥§¦èe(qqEùzÇ»¹úÄ{úøhàPªiÍ =0ÇåkxëdÂ8ÁC?µ,5¯¤Xb¾øÄh= LC#i xÂØË8Ác¢¿+ ¬!î7x áÿÐÐûT2Ì³Ø¿H¯`×æÇK ¯!ÛÓÁî-x áÿÐÐÜ³8v¥ÖúÁÍö0Æ4~Õ¿1ZF¯!ð.à·ix  ßÿ°}Lï(Cò æx²jÆóÖçÑx{Â³e¢ÛÄ&Éjsí&_`f¼YHk1ßdN D½¾¾cAj^b±BfnAQfnªB~±BJb
,JMNMÊ²¸ÀÇß=ÞÓÏMCÉ7¿´8U!Ô1(®ÂJ!¥ÂV5EG!¥L'åçäÄ£p 
JKJòóm
*T
*t&÷±ÈT"ÁUL` <=@«g¾x»À½{ÃbV ¯âéxÎ7kÂu!g?7O÷ø(_ïøà ÏÛÊÉX$'bÚøYIÚÉÇÕ¶R
(+§*f§) Lfg9 òâf®x31 ªÜl;/Ü]&Ô¦|C;CA£uc £¢x340031Q(M,*ÏÍ/K¥Å©ñ9©i%zÉ_?øX>ºÞleónvíi9á|Øue¦g´´uíÐü^¯ÝµfËöw[/?*°CÖR\Y³`g·Û³9Oê­o/;:yÂSÕ,ªaWùl1çÛÍÓQ;ïu~å=PxCñ8 É8RäxT «ÿÂ÷Q5îâèhã5#f1xoSÇZþå6e]5100644 zmk_mouse_state_changed.h ùw{Þ³íZWbâµdÜgwóV$ fcxûÎxqÂ! 
Âèx;ÄøQÑÄ RËRóJlÞW7jdli½É)wzéßþBÍè_³' -:¥x340031Q¨ÊÍÏÍ/-N/.I,IOÎHÌKOMÑË``\8õgÉ£µºwÎw¾µÜ^|Ü¾Î Éû±xmNQ
Â0ýï)ûQöWPORj·±¶m*«×ñ(^ÌÊDB^Þ{<fºó(ÍËáxÇ©/Qº]úµü(ûÁ¾E!%;,%¨m192ÚcàÊÒóA0Þ+ ëÈÊÓ
ëÈ	7vná»VÀJ}ìd"9§Jû'Ìë©úërI]23uuºK5¶Ð´=HS+îLx»Ï´q¦$WqIQirBne|n~iqj|QjA~QBõÄËRÆFñ%
I¥%%ùyÅÖ\µ
ññÉÙ©)Ö\ ÝÍ¸¢)x340031QpöMÌNõÉ,.)Ö+©(a¨gäú®þúéãÕ%ó5&îý;û¯!Den~iqj|QE|Puj^j^2ÃY[÷]}w:gúÖ¯å×^=»Áj°EyqIbI*²e·Ë¹^9¥sNÙ¾¶+e
±wQt¤Ä§æ¥-XT³¡²á×yî &÷°«/ªÅ=æÿü5ÇJ`Ý¿×A:ók|ªyo9CÍÍIM+:»@x÷Î¢/òÙØ¿ø¾P±kâ\deEé uÝ±óí_ï*ó¯:O0Oa"s/T]ibQI|n~Y* Ôäïß-Íl3¾þ[z>4ôgÔ|dE©É©e©E0õjuÌÞq
oÉ3×mð¿5ëÓ­7ó°ª9ieÚ5K£¾ºÖñuÿß}`I±&²âòÌäñb¬¾+¿µOj,yþgFãÈéXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV¨òªÜl¨O!Q$Ñ}KÙÞ)xpÌPù HÓQwA!2N½ÀYòh­îóo-··¯ó Mî1íTxí ÿÝo£/&ðý8Ú2ëì&[Eöê*òçµ*}_|5gã	ÇùY¤°¹])m%ÕYÂ'¥UÔ©O-®Þ>ÄH-#VªÑV/òlº;$nÖ0!gÚñSDBcK|u©100644 test_left.c édmìåWîÙñÊ¾	jïNÍXÊýspßø3&·ñpgÈ8Üãó¿,¼P»xÔªd &	sf	\Ë~Ô[:9aZm¯FõË¬ÓÍóDÎk
èÜPxÏñ}ÂöÉ²3JMü$5±qr63÷äÜ1iLÁh3Iir<áäyÌlµâR'0íß`¶ÌÎ¤2y	³ &Wj^Jf& Hùîcx{È~}3ÓäKRÙ&Ç0	M¶bR¬Êd8¹iT}ò	fþÉL*Óm¹4¹RóR2Ó44¹ ksjãhx]ÁNÂ@I|IÉ x1Ô*âÉË¸Ð©ÝXZÒÝö!¾Äoàø&<ø&v'ç0É?ß|ó³÷¾ûÚïXËùÎL*-4á,ñ#ùG¡U­Éxe>ÁejªE$use¤DMEi.g´þ8Y¾Ôd Îù°såòv=vÞßp2v;ôF.Ç1÷q{×®BQ2Öò N5.(R¡¢Øg,+g¨¡nSÞ %¬N¹m_l9Á)°ÔcË¡)wÔCgØes)ü LÌ-8lo¾vÎ7ûöI¯"EÿÖ¹ç1«+¢PH'Ê)Ö[Zi]2AëÀ·­yêOmU­/È`3¨¼ýmÍu»à9xÅþmCãæåáY§ 4ºâx{Ìöu~jYj^I±þDOé½
úú
n¥y^¯­¯Y\Z4q,s|rÒÄÛóíJRóròÓòÀFå+¤¤*äæ§r) ¿{¼§+ªää¶-¬&eR´¢hÌªÉ$viZs¬*.ÎÌÊBì(¬Âl ïDªî°Px»ÀxqÂlXG½=µöÍçy|Þ	Ý°(]ubçìëÊ
ôí°.x;ÀtiÂ+£Oîÿt.M¶··Úµè£çLï«w­M@¡¸(¡ðJÂ6Sï¥þÚLhswùÚ#¾£h²£
 pX®x31 ªÜl)jO¸]Îúöï© ïÔºk·" ­÷
î±lx áÿÐÐ»zóå¬2ß¥çzXEÐ6X¶¯!÷î-x áÿÐÐ½Óõ±Ã
ñ´AR£q¯!ÒT
âJxR ­ÿÀÀ?ÞæhÅ@'¤lz-áU74 SFÇLëLYêÅ{1è7
PÎ»ÀH¢Å^ Ó_;+sj.®¦¿-$°»#0âaxR ­ÿÀÀ?xoÎa	'¯äcyBZÊ¤ÐSF¡l5¦
v%/,H&R6-K_HÀHö5zÂË¸#I°âr]5¸jøõ9$W³!·è
2x¨ WÿÌ(¬Ââ¦»vÀ0ë'¦f*ûÅZvrÍÚ	î âPÛjÛY|;l6a¡cTöèÁ-@ó×#(ÇÁ100644 test_left.c Ð¼ÞÜB÷åXeÏL»$ßÍX>G±dJÁ­ÔCù8ðÜ/ß#&ÃÄîh'0÷2ËÇÑMá7x ~ÿhL
ÞçÛ5òHöz¹1³H*Øµ¾ÖîËlµõwÖêæØ0¸Y£Ê?§ê	§Uß@>ZËýðuPò>*Ù;;tÔ«¡vr·8©fÖ92t~à®ÿ»À¤s)ËÇý?ï)x{È~}CÓä&¾Ée&'0³Ma<éÔä)Ì&Ó'_b³O>Á,	 Ôã<x»Ï~}Óä4&©É	Ì¬£^BÙ@Zaòdf ×öH±UxÛN1ï÷)FpÁ.ÊmªJiXPDNJ j{cÝ!ëÆkÂ¡êÓô¢Roûy±7R¤F"lvlÏÿþg_¨Lúáý#NS Q(_¢ýç%©Çc¡Æuúÿ¬^Nê8CåXÉ£Ù-Oð¡äÓÝ÷×XðÐÿØá¹qÌÞ	Lâ£½P¯EÙüO.ÆH6*Ú¨A¦s´²IÖc9a¥öuÜ!Ë
®ÆÃ¢¨Ó?gÝþéU'e§i«Ó¦1­¯A«ß;k³¯ÝtÒOi'iDÑ~7B!tÃögÖêwFðæxý:¬¿H¿t6èÚí~/6ú®	Äá9Ã­Ý¯ Å$ÈÚWó_ó¸¿RpSnxe}ÉÁa&yfZäCå¼Ç^(wÂT
W?ªÆß# Ï&N+J/Àu-±ÎxL´ÄZ[í$V"Nãã#*ÞzTÔy¾I£B[jVfh`%ö{ßpi«æÔ`¹ÅÝîÑmP|Ég$fO½]H-åLQ@ãT¨Yó·A[q©ÉuHÓJ~ñL\Ó5UüY®Ô­ñÕàíÎ>¨JtôfõdYKAm"T3_B5HÞrI1Þ¿bP"È\µ2MQØ.°ìr¦èÂAQupÅ&[/(SÙü7Li -¥§¨ôq¹R5ãra÷pÅ%ª³\hxåTêÚ¥#:³DÐ~ä\?1Ü¾FU0è¼QpÔXâÒ¯üõ×63bêVQ5°íÑeÚKñr½	XÐ,¥£«£Ö°=¨ucùK°«ðxíÑ+"áöèO,ýËæ<x»ÈukÂTF¥$D·ûÆ?>L<:
Ö
úú
ê9Cÿ2 zd¶UxSÛnÚ@}÷WØ)*iª¨T(q"ªíµ±'ö6ë]²r©ú5}¨Ô×~?ÖÙåT$`í9çÌ].sá
÷8©tóµDñºúí>	U\Mú¯o8Ei³IV¢ÞßàCÍ&Ûï¯°bS®þqÃ1m3sÇm^e¥ËÐlAùìOÁK%]÷ê«Í:nÂõXßdµr3cÅ,¯,±ðÅ¢¨78ÍúãË^§^{ÆßÎàü¤{}íe>¥~J{I+v¼æ¡ß¾u?gAooW¯}þYú¥ßfÃÁ¸{ÑÇZÝ5 W"ØØß¸ý
bL¢¨89û5û©¹{.8Ó0atv5¹`gÂs*^²È{ì¸´GÐpù>ëz^;áÕÂ®06ÀjI²	ÍP£1á*)hâ$><  á­CÉ3þ@*¨¡î+Yahÿ»ù5&t§#Èn·~lJµ®"ØÐì(¾³-EC%VäÑ8¹.Ô¬ýÍ LPDÛûi¥JâX®t¡hu0àÜÎÝj 
x;gÏí^-¢|oA¢Ç©­$©HMRPh®°KÞ2A
1Þ¿'XZ&3l²ü&iD¾Ð|[-ìcµ®Ã­ãäª|ö&´JüS|L,QM¯»qÒËY/	¼Çz"TãÁÕ»ÊÍ­\¨'
7§Ó
Öi	­b#,(
xÉ»2¹æËÂÊvÇéy:CÅ`qröºJ$­³Ï_~wFÝaØÕõüäþ'øÊY­øùÑ0ZýláÍSà=x»ÆukÂF¥%6þ	bâ4Ñ´VÐ×WP/ÚÎü Ãê
ßgá+x»ÀýkC9+ 
÷	g¢%xÂõsÃK æ.ïaxÅþe¢BHibQI|n~Y*(-NÏIM+Øi*T\X¬W¢ (xq©èë+¸æe&*ä+¤¥æ é¢ÔäÔ¤Ì « ±(£êÂRf¾Æä,&iùJ N]»âä¢üø
/©´¤$?¯XÓk2³¹HQE|NfqIj^jÌ	ýU&0« ×*Béîyx{¨=O{ãä`FÉêÊó²mÌáÇ s$KîÄ|x»ÀxqÂllO
¹ôôÄ¤£{6îåe8wáìÄõ ½
ìbx;ÀtiÂ+Cnî<·øª7´ÎYùjMZÎ'&@ P\Ì03ë@á¶%?äWW%ßÛd3YQ i®x31 ªÜl(k§©¯·¬[j/.ÆÆf,  f	XàÓx;Ï4iüDKÿÇt&Þ±)ÍÌ+±/QH*-)ÉÏ+¶æªµæâÒ×WðML.ÊW(H,JT(JMÏ,.)J,RÈWH-KÍ+ÉWÈËWòõ¬Ä¨ ½èïnxO °ÿÐ¨Nó1dT`Ò8ÑYölåNDY9ðÇñ	ó¥9r_S^ryãÒ3$Ë~TæpÁÏ^ÕkÐÇ?½¿©%¸áx[ÄyIYa¢BÙd}FÉù×pir¥æ¥d¦ihr ¥k	[à/x»ÌüEAYÁ3/9§4S!%³(µäðæ¢ÌübTÔÄÔ¢b®LeÊ
nùy%©
Éù¹¥¹
Å©¹E©
 }×¦$jrM#;ñ<on~Yj|n~iqª^2×ÄRuqeçÔ¼¢ÄÄ|ÔâÂÒÔ¢É>  Ûü/¼áxûÅòeÂ´ÉÌ'OfTäÊÍ/KÏÍ/-N¼qHH!_Q¢Ì¥  É¦¡É Q¶ í
DxûÁrmÂ4e·ü¼TäüÜÒ\âÔÜ¢TÌ¼äÒÃkS5¹JÒSKâóKS5
<ÃC\¹&[0ÉHUåfÇçæ§Æ$¤Æ'g$æ¥§¦è%sMÜ89{²£ÖdÆxdU9Å%©y©EYJRK&71^1â2Ó3JÚ4¹RóR2Ó44¹ 2=PàæMx«=W{Âê§%&.PØøx Bóã2xmRßkÓP&i×6Ý¦kË`ê¼lsf³®SØv«âd{t?º,Ä,¹icÓ¤äGMÿa`9à
ÊÞ|û,}ÚÐÿ`°w|U4´©NæË=ç|çïÞïN<µÔjMSUeÕDSDªnÏ
6Ò
T5£lsElùS¢fJª^Êzçdy!:¢êæÈÍ=¨V²XkWmÊª|2è¦-T:ÚD©ÊÍglóhÖMÊKÃu¬Ûìs½WEÁ&º_ÛäòÒ`r¾?á] LYihÐÈÁ@*ã{n.-ÓgÚvlÛÐEK|°éìZR5ýá´¼gÃ@ðyeRÞ¥V®g ÿ½3,ÎÂ&Bd  ÚÍ'åFÛw¼îÅþsÛ1¸Á^(ðq1ü
¡Ù[Ñ¼ôÃa¢â¾»©hÆ}øJ=ôð4|òÍÂX/ÞÍÙò\Äåó<g7jçd×Û
ë0»ÆëHañTÆRÅrª¼×"(úú#ÌíµUvxC­ÞXÔß¿Ò`±o7¨*&áØ|}¸xÍ¯õTÙ@,vkóSî¹©Ë.2±äãÃ(|¦pHáÖNÜ%Î÷Ì#¶3zã°ÈÒ]1; äÓÉ®ÇS_2p7Áu5=m;J{¦ln
óý
Íð9ØÝDXj
ö'©õâº°¼º¼ÁÂa*RúÊoSÜïWx¦5Q{£xUnv|n~iqj|qIbIj|rFb^zjÊfmÆ'¬õ
Õ\
H ¸¤¨4¹DÔ2[4  RO-KÍ+Ñk
è`QU®ªR²âä¢üx âÉMìêÜ0>ÐÉ+ØÕ£õJKJòóÑÌ¢WkÂ-JÌz	ç4RË&?dÇÁ· Wp^	îÚx»ÉÙË8Am¢­ W¯w¼k«_H¼§oÆäý,R G	QîÑ?x áÿÐÐ <!¨²ÅïÖÛßTª}ñ(ð¯!Ü÷ôå'xU ªÿÀÀ?)ºyZX0Ü
².ssµºðS2Íìp(2á×cÐ«(GotMÓð40000 src 4P% n&Þ«áKõ§o$èß"%oðrx»À½}ódQæÊÉe *½®x31 ªÜlgöVß,kÓO^`É}urí ?Ò»xMÛ
Â0ïûÝ¨íV>ImÜ
k;Òtl>½ÙA49üùòb¤¶ó-Ä`P.![[bëWýýO{ãØ/T[rRªsK pf¤ &Ä²a°89pY!-Cu-âËg# mAhp5Óäº+£P.R+nä«f%eÇ}PRN¸v ì\Â·]JÇÅaÐ¿ý!,%äCyffùüÜ¨rº]îä?xd ÿÍúE+dÞm!kPBÌ@ûYýñ9MB8>'move_mouse_right.c °âêî^p¯¼ýÔ%«ÏËj!jM7weÈýÙPn£
{ÓÁË]¤ý-XµSx}SmoÚ0þ_q£ªPFÛºiI´¸¬ZZ$FQ·E!1`âÈqtê×ýýÄýó
-?Äï9?wÏÝuH\!5ßPü$1u[,eÓº©°ÐÂÅ#;a®¨iÐ\~ziòéyô¸I°
±©¾X°p¡ögöõÊ<Â4{8pný{8}re÷FDG\
ï®oÎ÷Û/ØdBl££i'>³Ñïþ+kkµµXºyàñ0Kx²l §Ð>Ü\!×Ø±ÛÝ°OìÞ%±u³EbÖæÌÖ44tð9DT°hI@ä
8xQ¿¨7åñrèhùà`XÛÇ]y=ÁÀÙ>¿@DßÌ)1?~iÍAåè°ØÔõwz«QàÔRÑH¯Ý÷FãBKH½jsT&"×Dé2Éî´t«âÿx?ÍLêlMQWkÛëuò7Lø.%¤¥ eÉ:)D²+5éF	\BÛ
ªç\¿­xÞZvåí¥²²¿;fßó?Wö\ÞN,¶·¤Þ*NÖ³uÐôá#a¶øÛj6Ï
Uò}qJ'$#sªöÀð®ÕÁí¢ç¸í¨tüÙMcbÓñ1¶däz\Òöàq+}Ã}¤|®ã#Æ´?">Oä^·4rN£ ý?¸	°Y`e!Q7ÈW­×¿èµÛt|F7ÏcøûûØäz¹úü#NE÷ÔÇPß¬@Õñ:ÎdØ=µÚÛZ£ÌF-5Njªª&§¼¦yoc]´ÑçëæÚBx6 ÉÿÐÐ3hËÎòÚ¼Â7ê:éBÑJjFGT·¦ó º9DÐòZ×üóbù,Ig¯!¦Õà§Bxp ÿÀÀ?Z¦.a÷ÙË7ý:6Ø9Wü6SF÷zhÆHï±`u¨¤·'¹À*2ït­Ï¼ìþ±ÉÇVºÊRMI40000 src ),Ì[çë°´ãà-q$º¥46ä»xÂ5mb\ÏdfÆç10Næ`> K Ðï!xÅöMMYÁ7¿´8U!5/1)'ËÙßÏÍÓ=>Ê×;>ÀßÓ/ÄÓÏÝ¶kC$H,4Ø)ÞÇßÝ"Uwqusõ	÷q
sõ±5ìÏt Y!á^xûÆvuÂüó*¹6ç0r1 CÐ ®x31 ªÜl*Í3Çî,ÊÛñöo¸àgÏÖe©SÝ µ
Sªx340031Q(M,*ÏÍ/K¥Å©z5Âgn[[©ìþçZì}NSÏ4DR\\YVT=³ËÛíYË'õÖ·<a©jÕEé åU>fÌùvótÔÎ{_y%ÞP< ä;(µxS.(JLÏMTÈÏKNåRÎÌKÎ)MIU°©J-È¨,ÒÏN-ÊKÍÑË°ãâÊÌ+Q(M,*ÏÍ/-Ne©@1ø
³RG¡ÊN*-)ÉÏ+Ö´æ '#¥x340031QpöMÌNõÉ,.)Ö+©(aX8;àÓÃuWÌÏnþÉ²qÛ5¾½ò¥E%ñ¹ùe©@¢´8U/ájv¸ø^ûÉWÖè	o¼#øYqQjrjfYjQ|NjZ	P½í½ÿb^îÚÒr`þ÷'b{ò±ª/ÊLÏ i¸|àAÈYÖ]$x&øßÿ£'d`¬¡¸<³$9f¼«oæâÊoíKÿÑ8#%r:Õ0ÃË5>÷]¶sÕëwUwÎ½pY± äskæ[x6 Éÿs¹m%%ÕLp*r¿G=aÀ@ªJ(a3ÁÍ¯¦"uågjÕâÐ¸]/Pº5xuRÛnÓ@}ß¯µ*²#¤DiL¨pTQTx±{ê¬jï½T6¨Ã7 ¾ ?ÆLâ´¥}Ø¹9³ûRå/^}ÇÕ²5+4
«þòµØèªtYJUòûÀ__
²x¢*VZ*g»|f\Zëk¤Ë[ä 1èõô V×2_¹eÊiÐòJ~ó¿I y:Uf2ÐSÉª>ào®¡h`¶Òy¶­£4 l4\@ðôpô2 ;ìßÏhÿñå¿ïVfë6g2Dq¡Ýú7ZÒ]J¬°y	0
/]#²,d>#³EQaxËÞ óFÁ°ës´VGÖ¿
YjnÆhÌ§él>9Oât$Çgq@Gp2ÿøît~}H9$?ÇIx$m:ýIÉÍÂ^¤`g¶øÎîfá :Ö; &)í½+cp¥©æB[ÛÆóéïtïªEw¾"m§æ÷¡¡vÜk~9iCî}û½RKæ_4'ÛÆå<òvì}ê>M-Çuá»£56ÃÑ÷!tïÖÙÀQaG®[=GâFüå;ãîcx»ÀxqÂl7-[ÑCu½Ñêâµ=ÛrâzE ·Í&àIx;Àti£È}¹d~	§}Ê¿vÝê>ÿf¾îdF ÊÂ÷¾òxWénÛFþ¯§ !Ål,;ASÄq
Æ¦SÁäHrTP¹´¢H"%ÐÃýQ ¯áëÌIKnQÂ0¹»síÌ7ÈsÃo|1]'G3D<|>}ÛxZ?òùRx|÷Q"<Ir7ÉvHÔæ3IÎÒ¯"ó¦,äÁ>y¼älç©TÞ8:[»?eO#ÍÜLxàÅQA%¹é#xFöÀ\8:ç»²÷Î°¯nïÂ¹¶ß9×M¢h·Z§
;8EfàKeqã©Ïqp>
Ùóù]Ïî_@{Õ>®|èÝÀON¤ÌÈòÄ-ÉÒ>&Å³¾7-Qö®ôîzÁOÕ~$âHÓ hÃÄ_ÚÞxq¸û`ð4åþöp3¾Þ.wªÓ¦ú«-)4Û%vÚ6ÆMò,Ãðly6 Ã©66§
ü#ÿ¿Ë'ä´{|qÿ×ý±ïVV0z5>5Û¨&yÀ(pgÐ®ìóÕ{÷[:$%",Å%-BIbÎ'§;do[
:¿9ðâ¤qÅ>ÞdÎe§ëHÀè ÎÓ»/¤âæø¶,	ÔB-xi 7M¸ëÃÂE¨,ØÃ¸F_*Qûð¾c_°ÁÐ>¿ªXÈ÷f·OHÎmÇeJ¶úf¾¹ÊÓ7ZY¡k)"°ïBþi,cáC«RXSn?s-Póáµß%fwxA©@µ¯Srh·J¸1r$»ãYó ¤Ry÷@fWì²×ÇèôÉs$U: )ioó§,ÝsÓj¿.ØIT¨KP*æyèf\Ö¢fHÌçlÖ#ÇrëÄ«×¸aÊ+òð¤Ñ<DÉ¬tïâN²ôì¸Ì.,K®}£ª§¿²ô-ôz]]ë<Ý­Ý³¦m²çnNª$K Ïã(sïøP×3tnqåM;K6Vu*,øÄ¬A©^M2bFÙÔ<L¼v"fQ-°\ÀÁxð¿V¶]&¤Ë¢yr~
X5xºà¤uÆ±Ú	O¸a"ôq
ic,:ÆT"@1v /öðþo!Ã³m~ÊîÜ¦±ÖëÇÚNêVëóÑ1j?«t®:%T+?Ê»l{<Ê°Gôññ<iÔâjÊ½YÏÇI$hAµKþÕþj<ò×ct§lÿ¢X²Ä<E±+ë¥«E´¼ÿ#%ò"ÚÕk«RQØkd#Jæg1 _îâ¼ 'OT¼P$¸fU_÷PuímÕ¿±ôâÔþâëME"ü wë¢Ù~?#F;*í§t[Ú¢Ë,.ÄR¹êïÒSÜZ³nÞ	²yó.BT¥³oWkïíCè«ïPj¸¦Ë`¶ÐbôÒ[æÀ
õH)É£ÛRs/Éß¶Ì/M÷âQ:Ó8É/k´¥¬÷CS	öç¢´Ù4	43i|³ßxÓEjûo¡tFë;?¸G5z:XäOÝûÕîËÓ9y/þöc¯Ôß¶ÝæQúÃèLO"<Q?EHeZË!±UÎãÏH¥ªìZ"ùÂ<ÝBYÑïX³[j>ñpÐêÞ^_ëÆ\p&+Æ#wr¥PØ~ÌÃvq=TF@-Uµ¦ÞÞ¥s%Eëá,CFèKÊÄÊÿJ>=¯,hÓ<·:D¯TÎ¤àÂßé:}èó*vò3:ø<`ng¨.ó@¤öÍÍuçÜvz]Î{ÝËÎ{VÚÌì¦ßéõ;ÃÏ¨ázåbÆå5x['·NnCãä>¦ÔÍa?3Yó  WôZîx áÿÐÐã8[Yö³jÝ|û£­Ú¶¯!ÞzOàzx;Àti£÷I'ióþ­ÐøÂÝ\®×g¹¶{²£
 Ï\æ
x6 Éÿs,ùneÙX=Á"&[§Ìgv>Q­Øý/Ä1þApap¡mj¸]iù¿³ëxWÍnÛF¾ë)Æ6lP	aKnqBh°")í6uE®¬­háb§ð¡RôPôÐSA/Ö]"%ÚEyXR»³ó?ßöïx©ËáõÎï££|îÎß6ö6\¾¯?ÄGñÑM('	R;Jj	/êâûø(,6o?Ä³HÜÌ%ÆÑìñ(
"ØÝÁçÒ§f·3è
ab1±V¿áýìßÌ~§7$ºÝÆËgÂçÐ7zl0ìÐ³X§ov&ÇÝV³'v"p?N N¢ÔI,f.jrÞÀÙÈ2¼:]vfXZÎOÔqó¤QËJùUÈ¦g\]|~ç;£¯E«I|ÐÖí	ÎØzW­»Nçú/¹°ä>ä×WQðùúÊ	<\æÜYÄéíu.>E·~Ã¦³«×'ù6îÒõh)1i¤
¡ÝÚ_¸oG eR~#³DÆ%Ó~m >¹¨µf'}Ô²º4ìSámµÕ_Ðneâc%? ý`Æ¥1°ØûãÂ`ó'©çìÝäì=ë§æÀÐJzÞÆ7tÅÌ´3z=S^dq$¶³ É<â¶«Ô
£Àáq\xI©D¡Ü
(×P)ëû±Ñé±ÕéçÊa2±xêð²}Ü,¢)·` ¢SÌµYBmO=áçtÜ}fë >¦ùÓl¨ÕO¾%Önf!¥G&FÈ)2O)ô6O	'ü\¿ú{É½âÞB:ÝðD;ØÂü¡Ã9;Ñáãf¦=Ó ðÐ¯èUYlôpUð3ö®Õ.ÝPè¡íª
ÙAÛwõ}·ù³¿«¾Ý}îÂ+ØsÛ1ÇcÅ3ÿÄ´ll±.Õ DÜáSá¯jýÖñ/­"Ïv<*ºMUqB2Æâ6õì+<ÔêF3ÐÙkhÃ[¶Ñ@H; %!;Xe_þ³å´QPúc¥ßh+{õçê Ü Ë ^¢l(|óÑV;ÀìÖ¡]b¾`±Çy¨Q]­ÝøøôýVFñÐx(YÖt¨3Õjáßyé¤1dÑå%TWµd$¿LV¢äpàð¶êptLçÉ]¦÷QØa{2*Á*ðÓÀ7j3|hC"ü×Æ?ãôüù5¦SN°ª·!ÇöõI-!fFFqü&LFñÕcyá(²ñ;ìÇ	B`¾¤çG©ËGÕd*ÈèâºtÑ¦èÉK¤¨já/W¿{;0.ÁÕ¾æzGÖNÎ^¯x²%°Ò7Ëtr9uú'aTú¡jû£
 ål]ÝsõmJxí3r\«mú¿ù 3¶â50}º©ìi5eÅ<N9v`½jiÜFÐÅ ÊØIÄ«b]wË1#{Æ\7Ìx¤,Pøê;¸¯5T­1z

ÖÆgÙás$"ì(Èb"¸sO#ÅaDI³lun-Aqq~@­o y%£°A¤c&­®bÎÍÄMñ5ºÊ1xxa.,f:]Ë¼4òþU«YT«l«ÿG5Åä }bíyS£X×Ô¤8=zý~Æ°¸Ý15§WºeÊçspM¸4·<éPÝ6f;§ëÙ®¹]ôloJ½ÊZ{ïkljåÏ4®8råLÖ[Ü@yrÝi°¨fþÛÎ°Ìü§AÐL'&~ÓÒêYêÐúø÷Ì2ÿ
NÍ3VÚÙhlÇ¦õ%ü%k0èBxÛ,Û+<ÁbÎÄÝ2Ü¡A!
)©eÉ©ËM5SRRËRóJò4Ks¬ÄDÄ¢D xfIbBAjQJb±æäsLòLÆFß3µÕsyÇx¹:ºÄ8:{Ç»¸ºyú¹j&Ä$&gë(hZsy%É
Å%E¥É%
Ùñ%E©)
`v|JbI¢5WY~&Tì¨¬XX+QGÂH1&ÿgv\ÁÌ® °:Lfeï¼ÝL\A__!µèèD¤ÊTÌ¼ÌäÌÄÍ¯Ù£'gsóL>Ì)5ù5;çä_ë&åÒg´Ç-9y!·ïäÁÉ'xjÅÐ]§v×äH^90£WáÒÉx'sñ­ ÛA}/ë7xë¾*¼á"£cinj^Ij¦B¢BZfN¢BAbQ¢BqiA~QIbBnbf±BjPE~±Bqj®BAjQJâæÿé²úú
®Å@>PO~\QÄÉ±ÌÅ/2Ï`U ªKI-NN4=9¿$U!3¯ìðÂÌüÍl*Ì ì2Ôî¦1x»ÀxqÂl¦~éÇ+zì&:püÈ»ÔýaÃÄëÕe4å¦x;ÀtiHæÅ ~FfB®n)ª(Ë©²¨qÈèpö,Ùu²glm$ÖÚÉh BqQ2Cà2;×OIyãÄ÷æü¡©ü~yeU v $±ÑxÅVërÚFýÏSl&n06NÚ´¹LZ`Y¶ã^²­1·
Ñ§oÔ§èõ|g%:ãÎdºÃýnûíî·{X·j[ãÉm]]'êqïªìVvªóÖ!\£$º³dO*ÑS;+ÙQ/MÃR³è2
ãïT«éÃ_.E£Þ`ÖÕ«nxüaìN?For~RêF£~4ºÿÞoÂÛéÎõ}ÝDü²z_Ph0&©"Þx8	¨;ÕkµOuÈÖKÆKH?¼fäbÜqn¨ø²Õ`ð«ù qH+Î8¹@%®®0PËÊÕ¯³h

«XÍJÂÞ Pÿ5z±¦I¯'¼(cÉúf±ÌZDß|Ã²µMQÚ=_EbW«Ý>U+ ùR¾QîX	-¢Kôâ{K©UBi`ÕsLu§s¾kKA·G¬u¢D4(ý sR±/_Cçô¾8§ãhOU¢D´)µtÎ§TveAËQsC»SõNAö©äÆjËÜ®ÇÂ6µË²­ÞÕ"nÒ1ñh]"ªÌþ-5`Ô85£Î´ ÒZjË$Ìf¹E2¨{Äñz³oQm	Fµ³iïY­&]Þ1þ-Òä¬»ÄÓuF4'Älkmj(»G­^MíÈ§åÀ³õô8
ÅA¶¿8«=ðÃDÁ)»²ÀSÑ`CÄ¢åÈª
J¥¤ÍTéãßÃxþgÛð©XVZ¦Ùob¸O|F|NÄ%S_Súøø-qW0Ï²ªoÚ.Lþ8ü
qøø(l2§vÚ½ã Ý:¹D¯Tcds$àìK¸Ùº÷QéÄ«ÓÖÿJ1Þ6jÌ&wªR/T|¡ ðõOGát.^ègvi±à.p"ª¨EÏ²b
nõBÁE^(ûyEE6X86jG89ptÒ¹Íz$FÓ´[fkæ¥"|5¾4a.±¶ÿ+õ¼éìX=I¾ðd|Ûå§åá´_[VàÃààýgdÇ÷ÄGÄÏ_¿P*·Oó¼Ï^WÔé>"ÂWbÄkâÄ?ßIåÇõã)/8ô+â{âÁ­»-YÌYJô«-{[Å¾þ¶jëÃy¯ßV¹Öióâ6
ÃÓNÍR"ÂqM¼ãúvX/ñïR²Cq3aÎsÄ¥nÆ«Ub¬2F¶Æ¬­f»£gë¸cèÅÚÕC¹æÈê$B5{)ë®qb-S{5÷ªTÙ²ÒI;ínßÆìz{UAzRH"8MGøM»ÆI¹ì ñú­ÎæKF_¦îæBÛÃÙÍ®¿¶ÿûxþ9kSx(µ@bÂîÍkS¹âx[ ±@bÃ?fÜ|C5 i¤ ] àèìª  f¹i`7Ë5Øy² äd;±Í±,w'ïcklËÖ¸Ùý ë®x31 ªÜlËØ7	_TXSÆÏÅgºðWd8 
Ýf®xëb¨ %î·.xN ±ÿÍè®$éT.ù°þÄ1n2£¦«-EÝ«±4ÉØD¬i;¿¯n?Õ¼]Ææ>u~Jà¡v@ð]9\#ùæ	xë¾"<¡9'5mc3£cinj^Ij¦B¢BZfN¢BAbQ¢BqiA~QIbBnbf±BjPE~±Bqj®BAjQJâæÿé²úú
®Å@>PO~\QÄÉ±Ì ;6¿b®gU ªMI-NN
´!9¿$U!3¯ìðÂÌüÍl*Ì ,m6xî³x»ÀxqÂlUû:û4Ü¶Ú7~1û¶£üvåÄõ ÕÑm x340031QHÎ/ÊKÕËN­ÌM,`xå£×9ýmqEÂåZß/ºx¾t!ºøÔ´½äü¼4o*üÕ-%ËwJÌºÝÌ©4¿,µ('±Áo«í¦ÿw"Êfþ½iò±îBC¼wê¢Ìô¨ÉW
É¾JÿÕ·ùðõ¬ém/bQ3º2ÜôÌì	5Ïì	H¹sè4sÐDQ PÈÌKÎ)MIe¸ç"=Eö@ì[	¡µvò%ÅEÉI9ùë~ð+fOuØ±û`Çß{PëÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  ÿTtá´xÅÖÈ:¡rbS%×f7Æ+ 6¿æ|x[#¼cC 3>èkMeEpj­A®Zk®ÉÒ_qHMÞÀ!ÇË !ã2è
?x[Ê±}ÃT¦É"E¸ Ö¸ôµÔSóJ&_b¶ª1s¬´ôA2µP§¦P
äüâÔ<!¨ÊÍÖ)*ÍÓMJÍH,ËÌ/R°46&f¤§É.f  ª +*¨x340031QpöMÌNõÉ,.)Ö+©(aXÇ¢ò2Dx*^÷OÙ¹þ1ÌhQYXT_YZV¢Ì?ßàFØ¥eMBÓ;Ä¦½Àª¾(3=¤!o« Ó½ÀÍ·ëqíîqÀ±ã ²âòÌäñG§iÌ¸½ý¾ÉË
iµªXTÃ/×øÜs tÙÎV¯ßUÝ9÷2ÀeÅV v[ùí %xÛ,ûCfÂ)Ô´½;®Í<çX¼Í÷X¯r  «Õî¸x áÿÐÐ½ý¼fÍâR±(gàòä´
¯!ö«& x340031QHÎ/ÊKÕKÎÏKcøóLaó_6Ëé·!ÞëøÂ×Ue§Væ&0¼òÑëþ¶¸"aÇr­ï]<_ºÎ	Y]|NjZ^~YjQNb%Ã¼Ý±,.÷¾`Îá}®©zóðª¯&@ SÊuöÑÖµ?«Mó_^8çziG'DEqQ2C ó¿©n/êf83Á¬íbx¡&Ô¶òÔâ½ÊÜcMWÏ¼Á¯ö¬ìàÚ¯ùÌ ^Ëa0îSx{ÀøqÂ
ÑëS¢dªö¸oéüko×§#7q
 Çç¹fxÅöyB£òd7F¹Éû?O´W|É f¤n$xûÂüyCãDGÅÉkÝ/£ãxûÄ|eBõÄ*Ù¾2FQ¾ÞñÞ®NþA.ñA®þA!¶\Ê
Îþ~nîñ i_ÿÐ`W\×Æ®F úGæx»*x£^_¡K3òSó Ð×RNU(,Í,N-RHÎÏ+ÎÏIU(ËLTu
QH;¼¶839QAAK®£*µ £²H¦ÖVA­4±¨ÄÀÙÌÄ¢D$ã¼æ;)8»8+8:û"Ti`rJr|brn<Ä`òZk. âÚ Ãd§VZõEqIbIi1PR~vb¥Ô(FX¡r'±HÙ@íLIÖ
ë:aÊILJÍtp<ÐÁñPI&K1UOÞÄÉ$  d!j_x»ÉqcC$ íèlx»Íñuã)¦É5Ì÷%n®x31 ªÜl_×ýö¿\ãÏÀ°ø¦ëÎ÷÷&´} ºV©x340031Q(M,*/.Ï,IÎÐË`£!u²Û"Æ+OLe¶øõé3'iø[x[Ï¸qBùÄZ# h¢¬
x340031QpöMÌNõÉ,.)Ö+©(aÈ
ÜÙ_»õ£à¦ï\¼²vï|öÜ¢2
¨0¾¸<³$9#>3/³D/a¸SpÂI=î÷IÜDø³^Æ@U&Ä¥&§f¥v>ë¶»rx÷tÆvgýôÈæ²RÁ@Mu\©fÑMÞA=\±zwTÇÚ  KUD÷ëó	x[É³qr>£ìÄkRXX'Ë³pLfd³0²±ê%sirMh+
 ìØá6x[ÆxqB!³òDi´ÄìÔøâòÌäøÌ¼Ìy ·°7x¥Ëj@÷>Ån¤)tR¹´ÔcY
SÄ!:cgÆ¦ôiº(]ç|±&J(Äsù¿9çüWÅY¸Û"}ÎF²ëôÞ¸:MQFÕI"_;%
É7ªâ´NQ*Nàµ$°Á$ÍËà°/\T;	H²*YÂ¥±á4#!¤³[ðaþÖHfæÍýi0eu&wÜº§)bº6tlP¢$º¬­ð¤%ÌëZÌþ%Î$9Ëé\Èéüã]ÈñÚÏæT3Î¡CûÅc=ÃÞ 
#?­ÛÐD+¹ÞýÇÉl'öÿÖ½K·jâ¨dÕwõÅA¨v¼)g8Ó~Ð¡<Ñ«]BW°ÂùKõ[TXÑX÷ª¿ÖjFU
n÷0jHVTªfÊåéé÷PëPLqF·¸©2æ9ò?2Oy6ôf³ßïEþ4°AÛrä? £XÓf¡?
ýh¡7ðX ¡½çxWÍnÛF¾ë)ÆlP	aKnqi°*)6uE®ì­(áb'ðÃ==ôÔGðufK :PÂrv~¿ùfôD^û^}æñÍ]r¸àIÈ7­'ÍW>_	oOÒÃëXD_ÈÝ$Û* B±ýEzÆ³EãÞrqHÚXúIdÞ
½l=ñù\úö	Ol82«ïX#à~§ÝJ37xQffIîe@.3ÕÄÜ×p6r¯NFvÙSCë3¥tÚ>nmU¥OÉ-Tsb¿sz6)"øE.õ­ì¾A6é9<ëEk<}	[Ëººä+f,»ùÕe}ººô¢ 7Ü[¤ùòJÏ1/ß±fùüòÅÕ±>ÆS:bq¢eÆ¦³<q!vñá&K÷3Ý¤­HÚG2)2±ð¥øÑ¦Ö×ÎÑËúz|ÜºW¶OE°aÖÍþn§0*ûºf¿³SööÂ¾°ÙÄùÕFéÖ9ûiröØ§ÎÀydÊ£ezýÑT|æÑÜØFÛ6ð¼¨Ã$s½pÈnîú*Kqy<MË,)7Q(©§a
þ8¶­6Z½sí!â¼	/ºGh¤_áÜHNýd¾¹±U$|Â""Ôr<}ê ~Ìô¯ÝR%ÚµÊ.ª¤~º£Û.JJg?¡O z|Ì9äK
	füw|ÆQøðÏRÝ[0J8»æ±_AªÂ¾,	çìt8Æ*)Ãt>³(
 N0«²Ù¤èÁUð{ÛéVn¨ö7vUì¥`ìùæßþ-Ü5KMßÃîîÂKØó»)Ç×J=SÿDX¢7ÊÀÛÄ,Æn¥!á	?z~X>ö:G¿4¾^Ñ0<~ÍÍ°´ù
OÊÔ´	'âùT´ÆR±Ì7ãÆ¶@Êè+9¤ætªu&·t°vDàFØ,¤;{ØÕ¤n3V±q¿®&ñµõë2úÂsþzø3?* TF)é6!Ky´kì#ÌMèV/XpÔévÏèv$Qêm¿ß)îß·Ðµ¢ÍdÈTz3£Fù§ñ[÷PòDvî%Mw^½w¤¾¹G8Âö=
 ÞÔ±®QÜwavôÎn 1UfU5âö÷Áê ËjcÈDó5z+u 	Phzöì
A¤§Ä5Ì¼hjÖÁÊ²Ë©
HcgÎ<}kADq!qô¶Y!ñÍcº©çñ[Ìr¡~¨¶âç _> ôpÚÔ|¥ Ë;Ò
EÍ,PºEÊöáêá Ù`Æ^ J0æTLA'´Mìø¦ë1úÕ§1­ÖÏ²â§}N#'£AJCMººþè$Àä}©]$éûVknJªÂm¾S%ÇgíÕ}£,4pÂÐë Ìq5¨] ºÓ%Î¿>]Cö³åLÛ²c¾VN¹`a»6­V¦;ÀÙçcydí(0R£PìVkFtÌUsS1ç<QCXzø÷V #6êu/ÃTµæ(:´C3Zå¨×LDùØQÅD*yçöÙ8J²v5j
^¢âãÂëßax p@äI¨ §Ü)y17×yÂ×ì,÷ááÅtt1eÎÀêMw6*alõXr«g4ÁÿkÒ$]|d3\¨XI×4Fähª©éáV4¸è÷XËÉ-Ã]wp)¬×«ó0G8ciUW1S.aÅ×Xòh!R!Ô×Þìê-z_Ýâ{µg
ýt>ßÐ¡JC¼H·.±L$a¦-~¤¼´RÈèÂS«H ùS8!jB¥÷,¿3U[÷J¬Ñ¨ïô¬©3ÐN3V9ÙhìÇÎô=Zøy'Y<lxxû+óNf'ëæVUN $B`³@x}ÝnÓ0ÇïóTV7S?@e
Uµ~LMËMN[«§£>OÁaÇÉV6i¹pó?¿qZ&ý#æÛêìP	L/¶¼ÖS)
y?Ñ³;d,n_áí¹TÏ)M{®ã­½ébLgÑí4¢£èj:\FäíB¸ZÌ?OÆôûìZitMçu:p[ Ä2SÖ=*¾æ?J£%ï¡ßKøm¼ÒÀJaKaæeþþ	ÓÁ
áµ\s`K^GßfÃz³ø2ù:YÌmÎÐe#\è÷ï¨¬9¨j¦±ÕÏ3*MI)ÓXÅ]R
U2Ä~ VR¦.LøåyPÁ ÞöÌ¶8ä²àKa¤;6ÌlºXBC¡Uk0i³"ºâØÀëæ2¨tGnPÓªÆ2MyòTÆð¡
»[¯¼ª35£X»]b´\.¡)Ä4v¶ÀÐÍicêR	xMæwÃ©³\¡¸G³wj6ÝEÒµ^µ[ÙÏP6×ðQÕ<ÃB³,7¤w´Ìí·ÅBçtj&7EMÇÆë?¼\ìåz¤=tý~õÖÝtÒèÓøg?´x$ÕvbhÕaðüêêC|)²Ï`¬¨k¢5Móêy'ï®¢GÑì "xUAKAÇ±.²®Aúc»fHÑIQ,Ã$ºÅcg´¡uVfwÊèÐ=?A'O¤ØK§>S3K+õ.o÷ßïÍCöËzú¸ßç}!	>dü>äÊãp}/0¤Pxñ| \Ýðä¨bg7M:Ö&3Ãz¯Û:;otÚ'znY¥ä¹gñdÂåðt#ZS¡PÆi+ÿªhxÖô;³¾
Ûþ·¦½{oAðA¤HÆ3*EH 6ü@Ä³ør?{Q>ýDZ{LÛÿxÜ¦aSíÎÁy³Ûµs-9&O3\òëÄ
_¡aÕ<K>¡{®Å*1Øn¶NëíÅèÎ¾eD6¹ên,]¬ôýH2PÛpçKÌ6òÌAµ¶ðÂ"/,ÃhSBBù\.äÒ¤¿»ü.¡[Åº³~ Äþî×^x áÿÐÐ$È×	hÓOAî×äåWÛíâ9¯!äOÑ®x340031QpöMÌNõÉ,.)Ö+©(aØa¯whÿ7çöÍu³^åîÇ{úãYgCÊÒÄ¢ø¢ÔäÔÌ²Ô"½dí­ÿ{ÖÜÞtSÄ§XöÈ\÷U·g$g ~1,JmÛÞ¤Ô{göÆí)×>Í \_4ëîÙx áÿÐÐíecÿñã!ÏXåÉ\ h#±¯!æô·î	x áÿàà¨]½"È§ãRË}¨N)ø]W^kä¼$æMÂ®x340031QpöMÌNõÉ,.)Ö+©(aØa¯whÿ7çöÍu³^åîÇ{úãYgCÊÒÄ¢ø¢ÔäÔÌ²Ô"½d«ÜyVö7©¶ozð¡÷õÆU¿g$g ~1,JmÛÞ¤Ô{göÆí)×>Í V5÷á0"xuÏKAÇ	bÕ´§Vb,O%ÙU+Åí<¤Jª^Tq÷%²Iwfml)^{´ÌàÁ  àÑàß ýzèMtv³Qãa`æÍ¼ù|ß¼÷®
Çoöÿ¼Î¿£Ìã áÓ÷f£T§Áïóa!¤>ÄÉí¸º1«.rÉìBÈ(ö%4<MI$½HX*÷ýZøV§!BÑ6àG²:{4°ø¾ç	KÞçåJy½\1UñO¹YõÀØ³¶R	¬¶e­0ËÒV!·
ÉèÜÀ]ë_¹iðvÔ½ÐScæèeþ ô§æ4©ÉZ¥5²4r	8´xÈ¾ÆIWûGöÖ+«;È¤;tU]«=eÍ´¦ÈölÒìøyr·f×Õ¼6|Oh´
Å»àºizîçÞf«®©§kê¥+fhåëÁÑÚJrF9ÓÐAhû?COKY=R²¢ôjá¡|VE]
Á*mñ¤(©Z²>guôi:*:=T£;{HsU<4q$_Ú¹eT>ê4ËÛp^]æn aðDã4VxmRÍnÓ@VH$_CN 4M*).qÒJÈqP$$¬ÍzÒ¬êØÆ»NS@¢OÀü9 UªúÏÐçà
u~TKìÁ³ëýf¾ïËâuéû¹½-|îÅ.B÷ãô¸>fÇèÈ¡øäáä1ÔëÐÝÛ×b{rI	QpRç÷ãÏåsÂôAF§
e¤brô ÎÐW:
õÒèKaà_8
Fñø]+ùûÖ¥rbPHÎàEÿïO!d< Ò³« ?W¿ B#Ú_Ü»åæ*ôe¤Hâ4¨zÁBTª¬y¯gÀr1TÝ		¶
ìì -;EÕàÓ¨|%ü;FÒ(³¼k%¿óµ\#¹ÎÜ×öìÔKsØY'OøçK¯Èû²ÐEì3#C7
M¤D²n´R+[a$O7ï$g·7:m¨H¨V\³âÖÞûesøÊ/õ¶m(ÐC&®I¬©Yk]£ôeÑÕ7½Ááºm"©XÍ·ÿ
#£v%¼YC3el.ãþØ2Iú±æÈcuÄ)<ÐSAÑ(E=¸1 LÇRaueeíX2éôÆ:½V-ù»yw·E0âK+DÉÎ4oU2Ù-Zå /8>ùctñ¹ð(ÿø÷Úîx».ºMtÂ>¾ÒÄ¢øâòÌä½»oW³Ê¸@f^BQj­Hjóv6 ÌÇËçG=x}S¿oÓ@[±ôBÕâTV ?¢ê¢ªÐ6¿@%sµ/ÉÑÄvísKª0ð1 !UêÊ¿12²±sþ¶iRn°}÷Þ½ï}ßçw|{ùë!³tb¨*¥Ê=¨å^*J½·±I5ºkãzÍ±vê5Ýj×Ù¡ïÎÍêRÇ£ÀFüÚÃ&r ¸eD?G§à!jQ5x%_1é¾;Æ(s¼Á]÷¢È±»¤=hï3äs¾60eà1C^úH]©hÅªZUµòÒgËÚÃòý¢¶ ..­¨ÒF;nsKìa«!â¡ù-gäÑUe¸	Û,S¤oÚr02Â~mÇÒ±ëéöÉlâêüÔê;?VdïÇnÆ
ôÞÀg§EÚ¤<û3~ñy ÀÁëôMÀ.Å/Äµ-³÷e·kþÚjML¥!Ú3ÁFemqµÄ	|Fl=vUÈ2;b»ìC,w)HËr¯ä1Ë]â©ìgLS&Ä,
cÇV÷³.ìuüúÈ ÌãºaÃ/ÿ->Å~ÇggTéSÜ>¹k¾À¾ºüWêX@Lè¨÷©÷ÑÃcñ¿Jëa ØØåAL¢ÔfWÎ½ëéÌGõÉu/oxZ¾.gñî£ðQaÎ(
ßìÖÂûq`ïÏ¤¹MôÉD
>,¤Rd¿íýßþUí±²TÉ@zØ÷xên0yz5¦
yÚÈVö©ymÁ,9>x6±.üJüþ~ñkIîèx áÿÐÐO!éNÍvÜzïÜ¡ðOÿ=§6³¯!çÊ¢î®x áÿàà¨àrÉô¢çIîJÈ;ÞóF§¼$ýu®x340031QpöMÌNõÉ,.)Ö+©(aØa¯whÿ7çöÍu³^åîÇ{úãYgCÊÒÄ¢ø¢ÔäÔÌ²Ô"½dV·â§QÓì>~êÖÑ[Ó[¶0q"+-.Ï,IÎ *übXÚ¶½I©7öÎì'ÛS®} j¼5
æébx6 ÉÿÐÐ3Åx<USen÷a}§ GTZÉ(^ÐST¡¨w9>¯!FwäÚ1x[Ç2eÔDF®EJ@b98¯$¾¶¥*$¦d&gæç¥*dç[qqM^ÌØ
 ®¥ðì°9x{ÀøqBÑÁÉêbµ>³Ó"ø,$ï\HZ|Óû_(%3\þºµ¡åio¢ÀiO§I\sÊØfOÜ£ A®x31 ªÜl´[mÿðþV(
éó¯*nã\  ©x340031QHKÌN/.Ï,IÎÐË`hà:ëãù»ùõ7æ¥l§Ú³´­2 $Í>ï«wx[É¸Q@93-/%5M!Ê×;ÞÍÑÛu¢Ö²dIKÌNî(¦ ¯÷qö÷à T)¬
x340031QpöMÌNõÉ,.)Ö+©(aðm¿þíKôêökkó£Ýï^j÷{eQT_\Y¡Ì 4ïìÅ#[^½Ö;¾:ûe_ËOiLñy%@Õ*Jâ	kÝÏ¿ÿ{[¿Û¤gá3¨êÒÄ¢ø¢ÔäÔÌ²Ô" Ò¿Å²7«¯ÜùtçËw»ï=û ÒýJ=ãx3 Ìÿ¬¬HôEÖà^%|²ýÏç¿ÕNÔ*nù¤4oV¶4:;Ñ­¼ZßÉrgç mx[É³qr>£ìÄkRÜiÙ©ñÅå%ÉåEøñy%zÉ\\å&Ú ©á<x[Éxq9ibQI|QjrjfYj^òD)]Få2jslÍ	càFxkæhá+Ì¥Sª`S­:±þÞÊhËfM^Æ Æì­!xûÀ6uKZbvêD7WÝo.	¢ãË3K3â3sKsKR5u'ÞWWÂ)©£Sªi=ù'£4²²ÌC#ìÔÉNL5`»&bÊ0í ù®1/îOx áÿÐÐ£ß¦ÛÿÚlÆZªù×¯!ï7îyx áÿàà¨wþíó4Hh÷ =þcÙ{ØÃ¼$ùuÀî)x áÿÐÐñwÉkm7ì·(uþº$ô$Â)¯!æ±ÛâSx{À¸qBDqQ2C¯(ç¬;sãåJ¸Ë+=¶ú¬¶¸G æ¶
¥x340031QpöMÌNõÉ,.)Ö+©(a¨>:OyÝ½ob>Z<fþJæR¥!DeibQI|QjrjfYj^2ÃßâÙÕWî|:Áóå»Ý÷ý Ç&h°x[Æè9ÁI Cýîvx áÿÐÐXüCEùç<¢N*|º´bó¯!ã¼Fî-x áÿÐÐS¸a	d}É	¤øcåÅËÇÅR¯!ÜÔ{îyxÛÇ¸qBÈíÿ7>ËO­±åeºÞóµ6é´ºµßÄ' æ@a®x340031QHÎ/ÊKÕKÎÏKcXË¾o­Ç÷o¿mJ
üôæT!²ªìÔÊÜÄW>zÓßW$ìX®õýâ¡çK×9!«ÏIM+ÑË/K-ÊI¬d¸}âÿÆgù©5¶¼L×{¾Ö&V·ö31 â¢d¾s;qkô¦±öÆæÌ?P³ÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  q¢PK¥x340031QpöMÌNõÉ,.)Ö+©(a¨>:OyÝ½ob>Z<fþJæR¥!DeibQI|QjrjfYj^2¹·nØäå¡aÓäó13OÏ3 l~ éxÛ*<×A9µ¨(¿HA),µ(3-391/%_¡8U¡4±¨$¾(595³,µH/Y!µ¸äðB H:9?· 3'1%_QkÂe}}]< òââÃ2ó
#ã=ý<C44'ÍlÉè1y#£Ìæ3['{°)Lîfód/J-)-Ê³,Ê	coÞÀnÌ(]ËÅ45¼(±  µÕ¸É|Êù%$4¹ª¹À1È=>Ô/4ØÕE#%µLÓz²§9P·sFbn¢B¢BZiÞáåç+$&gò2ó23s2«! Og¤æ&NNæ Ò:_çxË{w¢ÃÔ7dô3ósJSRlªR2*ô+õ2óJ²õ2ìôõ
 B?çpp$d&+lg`*ÕP
u
Q(JMNÍ,KM±RPWMVWÐ0¨P50ªÐÉSÒQH"MëÉyÌEÕ\
P Óíãê¢Zª_4'1¥¨KÓ®²(µ¤´(Â¯ü9Ò	Ó°H0f³;ãä©¬ÊÜeù)\`'/`Ä&2Ù- ewXwágx»À¸qÒD÷FÅ¶õyþq*÷y{å¥×G®¸^ Í¨î.x[Í¸qBÈ:Òa'
¥3&õWµ-OØ¥ ¼h 
x340031QHÎ/ÊKÕKÎÏKcX¬¦À¦ºrkªú¯LËy±ÓeÝUe§Væ&0Hæ÷½º³ß«ÕDeNWÙZþbyÕÅç¤¦èå¥å$V2Ytíaözû²ZÙoô=ÏØ¼ªº<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 â>èx[À¸qB(%3<~Å÷'}m~ðú?^´èÜ´ßkT Né ­x340031QÈMÌÌÓKfâ-·;r·ÁcëB¥7W­¶fBT&Ä¥&§f¥ûu·ïYq+÷#Á­%Kï&¶d[ Rj·Gx}TÑnÚ0}ÏWÜÑP­öql¤,jÐµ&¹&¹ÇF¶CG§~Íö!ý±Ù ªÒùÅVÎñ½ç_%8õàzrµQl¾0à§M¸h_´aº@ø1¼²0ÍJ#¶TÇN®ûwg1KQh<2åÕFSwÂDÊËáã#®,Q	ä­Åç×Pk[ê?QxÖhs½?8Ökó¹EÝîñx@ãþMI8i8ñå{èGÑXÓÄqâð[7;®`QBÂQ÷KöýZ?J®ãî÷æaÏbdL¯8Ý¼ÔÌ×ó­Ë=/ )§>ÿ}þ#!£b{¾éN¦ÀÇÂK-T¢0E¶FÕJ=üel¨Ày	&ñ×eN¼mÓÍXÊ¤°E´FqJ Â «ë¾ LøÍ{çRd×)8	Äqz'T	!4*e©Zr¦AH(ècÖ:&£	Ý@No5öÖäªm%~{`<]ú[ä©,tó÷î§h¼ýI8F£AÒ¬JÔc@t9Ó½SÐyqI3÷±ã@'OG-lØþ¾åÔrkÉádâoS©o»Å(gÔØØ+ó5ve*+AÌQE°Dv´ïÿûî¤÷\ènëß¾õ­TKªd)2È¥¤Ã®}-]bÅ{XXEàzákb¨^GU»vkI4G\ùWd=ÿ¼ÝÜ{©CÜîqUý]¡)íÀ¶;Þ÷2gá7x»À¸qÒD÷î¬V'æo¹~íG:¹×þ¸^ Îwüî.x[Í¸qBHæ*³¾U
w5ã¶Að{ïß»ÔîPx áÿ  hØÉ	-®£\Ðþ 93ßïY|$Óæ
þî-x[À¸qBHÝóÚãï®^ÓIRúèûÙåÈW5* ÙcàÅx»Éñm¤DUjAFeNr~^q~Nª­ZibQõDq½úÌ
úúóU7ÞÎ ª×ï=x{ÎömäDcµ¢¥E%Ö
Zú\\
P ¯5±[u¢¨ØÄJ¾«÷0 Sm
ÜáYx! ÞÿÐ«"GT5ÖÄ,MC­ÈþüµËø¶;DÓ¯! Æî0x[Í¸qBH÷¥F"î<¨ü±qÖ¾ï»Ò& 
x340031QHÎ/ÊKÕKÎÏKcL7v¨=év÷c QyøÍÆØ_Ï6DVZXÀ ß÷êVÎ~¯V9]ekùWMäEVV¢_ZXÉ¸G+"*­þâaEë
õÌ\µ
ªº<µ¸D¯27¡ãØAæÕ3odð«=+;¸öëg>3 t4@ mÿx»À]41Nw2/£þÄb "Ä¡ªx340031QHÎ/ÊKÕKÎÏKc³ûsáÍëW_m8>ûä+k!ªÊSKô*ss:4i^=óF¿Ú³²k¿~æ3c  lD .±xSV(-QHÎÏKËL/-J,ÉÌÏSÈ/ QÅ
©E©\ Éî·§~Oò,z²qNæ*óßH4
```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/objects/pack/pack-b7a77e8e4ff22c7ab2714ee62af3df0214483413.idx

```text
## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/objects/pack/pack-b7a77e8e4ff22c7ab2714ee62af3df0214483413.idx (latin-1)

```text
ÿtOc                     	   
   
                                       "   '   )   +   +   -   /   1   3   4   5   7   8   :   ;   =   B   B   C   E   I   L   L   M   N   O   P   P   P   P   Q   Q   R   S   T   W   W   X   Y   [   \   ^   ^   ^   _   a   a   a   b   b   c   f   h   h   i   j   j   k   m   q   q   t   t   w   y   z   z   {   ~                                                               ¡   £   ¨   ª   «   ¬   ¬   ­   ®   ®   ²   µ   ·   º   »   ¾   ¾   Á   Ä   Æ   È   É   É   Ê   Ì   Ï   Ñ   Ò   Ô   ×   Ù   Ù   Ú   Ü   Ý   ß   à   ã   ã   æ   è   ë   í   î   ð   ñ   ó   ÷   ù   þ   þ   þ              	    
                                 #  #  $  %  '  *  *  +  -  /  /  0  1  2  3  4  6  7  8  ;  ?  B  C  D  E  F  I  L  P  P  P  Q  S  T  V  Y  Y  [  ^  _  a  b  d  g  i  j  j  j  m  o  q  q  s  t  u  v  x  |  |  ~                       <!¨²ÅïÖÛßTª}ñ(ð c½¬ýÙF³<Q~À0'§M  â»Ã<))9÷D_®
øEÐíÜ¶»q±&-õï=©¿ôføÈj¤uÔDDN²lüèB#l¡Ð	tâ­-ÜÏí9·sÇ?~J9Tÿ,`C|ãÈLNé>¸±¯`§)ãa^û×!ç«i*FsåZ »ÇÊÚøØµg´	àO*hGßÐù«À!Ñj¸
íÔI«¢_pÛç]¥ÓtEÅÔqbµ«Ck1bD &ófðµ=ü
û uTOzrx½©÷"×/Æ­ÚøÑÆ{ç	¿Ð.@éK¸MÇ!
Y)Ñh3IÖ¡°	1ÇÁÚ{a±Á;nyê¬flÌä+w¿/ ­¶(ÇÓ&ùaøaoä÷f<o¥íLìöËUÔ3Ðj<BömN8ÄR§|ÿ_ØáR+
ýx(ôw.9­ÐñÐÝ¦#ØZ (±nPlAéÏÓáÿáY+5óaÂ}Lï(Cò æx²jÆFÙ
Ä'àË­ §o)Â MkÍtTâÀ=Ïû;ïo%¬å¼M4P% n&Þ«áKõ§oV< bÝAj&©Û'ÇCÏª«jx=|F$(t¯¿ÏæOp,Á'Jxøßµ<î8¹¿Ü³8v¥ÖúÁÍö0Æ4~Õ¿1ZFKêeª[ ØJ>ÙÕ°ÊÔ;SýfçïÕpyfÛ¼XØ¶Ó%à«ËJ^íb Òúôÿ÷G5¬Çlç(ShÉáë`pZú=N¤´!$Ù^ZÏ
ñþö«ËWù_©å£ëñs
7«¾¤0CáÜpàÆ1#ÁÅG×pYZÁ'G´ý?>,Mi£yöRtçüdYþÈ°Lª©ëI¿>Áyù÷l²ZÉ(^ÐST¡¨w9>¤Së©9Öþ§Ê$y$}÷Nâ2oêÚl¿J4$v­©
»ùo´l±&
.ULßß=í*Ù;;tÔ«¡vr·É1NýÙ/$1êþàlË@>4@ßnÆËyá¨#C©ÛÍPÒ²2wª@æ¡$òàçz~ÕÎ´u{G([pÜbâÜ!Â³V#jÌÜS.Ë	\?¬ðNy/¾èA Êw¸Î×1G»N÷Ü*YÕýûSk³úTiºÂ	¦¤ßÌ/4zÿ®ç;¹=¥Öî½;VMjì ]èæLÄàõ«xG>m
!y¼!d¦"»Õªø¯æ=ì»%Ã!ò«üJb2[ÝUäù
B"ÍÑÄ´êë.ÉXg«kéù#"ÐZÙOøÛAPd²Íû#*p(ù
è[ôd³ÓV$8"`­GÏï\ý×/4¡æ$nÖ0!gÚñSDBcK|u©$½7m®tSl}v^óBî$fü$¾0nç\ÖÑ âÅZ§+$È×	hÓOAî×äåWÛíâ9&~K^ ì¦S~°OÚòÚì'Ñt¿pGtB}F&×á1Ûh'åvÄ@Ï·$=Mà¡ÌÆÅiF(¦ÍëÅ³JÑT;	.&(a3ÁÍ¯¦"uågjÕâÐ(ùú:®þëR,|L{
ÚC(ú ]ßÊ4
ë­zê³Uu),Ì[çë°´ãà-q) È éâ|C§ä>5C®cákÛ)ºyZX0Ü
².ssµºð+hH*ÿ¼¬Û²ÙLsÄ¼mGªÛ,ùneÙX=Á"&[§Ìgv>-¼®ª %ì¼f,!6ºÝ.¢ÁLªTLæËAM¼>ë&äQ2£¦«-EÝ«±4ÉØD¬i;4zn¡bÇ$MÔÉüA6é5{H£$ºÊJ6æXZªçMñ6¦#Ý
Ýw)ÁNunþy¢T7weÈýÙPn£
{ÓÁ7K-V§UVoqæS7ùö%QÄucíxøm/µå9ÅÌhÒ[¸ß4éx@­1%:½ þýJÝ-ªÏ»B¨wò;j-:Á¶´Öõ»JãH=¹;­g;BÔj Ñ9àTj3CmG<ï{(h´Ù	Ë¥ýq)[ú=½9þ\é¹´À÷ä¼oq=£F5d
­[zÝÃ {sD@QFS#1]ÿjãÞfnµ±`@!A1ÓTe­/¼å6PàTà(S­ãNAè~þ¦ç9¤Qø3'/4'ÜñcDj»æ¸Óà½TÓ}·úF*=|Â°,S¦ì-eDJ·k9G¡;çÊFÂ#:
¸(¨xVH G¨LÈËIjðÿ¨GØðGä/YXAF7Ýå´Pã¸$8ôHã¨>@ønÒkð HôEÖà^%|²ýÏç¿ÕNÔJ JnÔð"<kzÅ7$q]õKM¶üJ+ãÔá)í!üþãnM_×öô[«Ö­o[AGÝÒNêNº=²ÿÜXvýÙ4ñ~Ð_KNç-U-õÆSk=up¶®3ºO!éNÍvÜzïÜ¡ðOÿ=§6³O7KãKÓÅ?3uÖWgãÁO½ÉÑ"AóK H=#OæùE5HÎ/HoE
#åÛûQ­Øý/Ä1þApap¡mjQâyUÛÉå_ÂW¦ÄÍQô(¹¯dìBìÏÂNnS£iªO°OÐº;Ó3AuSª4ø¦2¹à4Ýð£NKáR¨S¸a	d}É	¤øcåÅËÇÅRT¦¨'.)àý4Á@`)KÙÀõTª]Û~ö×rïì ï1ÐÑ{UÉ¶gF¤H3{:Üm6ÑÅWDéHÚ½ÃÑîV3C¨Aá¼Ìb2X)['æTÏXOO¢)¤<Ô¹XüCEùç<¢N*|º´bóXæ?A:ö9}fÉÐmêÉ­À Yg3@}ÉFÝñQ2wWÙ]ØôÃZ
w>ÅTÝH®E¡"`lìÕ:µhZ¦.a÷ÙË7ý:6Ø9Wü6ZäJ°þ6'7§KZÔ)R[K´·ø+`k÷;FÕ\>ç}ÇîÕÖ,cR"ñMóDÄõ T\aZÍâµh­ù{5oéÐÎEÒ¸]>uc°Í;0»SÜ[Ób0]R]A.x¼}?ÏLîØ8uªÈ¹]½"È§ãRË}¨N)ø]W^kä^}·¼¥½<±Ä0Õ5:ñëuÀ_J\ïÂâ\ÅÝÊìG
7
­t_gðõZ¹Ý8h&V¦r@] `PÇ±#¿jQ#ïöT¤ú=µ«a]!&i.Ô_`üp~ \cW¦a­UéölpG-ïÖ¦÷ÿ
blo®øw!h3CP¸£ÁýÞbrkMü|ë/²Ø¤WYö»rf%·bÈA[&³ß@d®lg`û4c¯Ò&¬>£Áu­åËþOÐ?]cõðL9â×:<îx=ËÈxdå2²©zPªßóÆÞ:fÈÒÃÿJROâàfÏJ6èMÛÕM*; ;)vð5h)ÌÀc]O&ÕüÞ-[ËÈUªËhL
ÞçÛ5òHöz¹1³HhËÎòÚ¼Â7ê:éBÑJjFiQ¼*XZfÑÃ¢®S1/Àªªiª6ÐMz±1¸ÄÛ0Sÿ?KûiÑPLÁ26ÂTÕ´wxvhTz9kI(dggabÅ£±½
 ÎÐÍkb¡áæg^KJptNB¯Åcl6a¡cTöèÁ-@ó×#(ÇÁmQ¹}µò²÷DJj»¹æçm~{·ÿè´¹oÈU,®IòÙnoKéÓí@Ùèê3$½[HÎnµÞQ³³·,6
»A¿ÁoVg§Ög|P¡*«ÄÌolÁ5>%`¸9x@â]ãjÎo0ØVÒ¦1PYáfíXo£/&ðý8Ú2ëì&[Eöêo§g¨é¨`Ja*+©üê!p»¹r`Èéå<?è÷¡!Op/nÌÞAqþ¢|øeãjÑÏ7qÔ`¶5K¥ Pý<GDõ¸rr9þµMd¡,èØ~ t&»Qw$ñ_¦2gÊ'C'&]uazYTó.«S;~8V`w*¢ôÜ9³»nõIú3Pw(óÀU¦¹¨:ëîzÜÎéPD¨µwÃ	¼=§À[ýtÅ¡¥hf Pwþíó4Hh÷ =þcÙ{ØÃxÄî¢
úè|ïLÌÝ^uÍxZ;Bë´¨u?WW V3xoÎa	'¯äcyBZÊ¤ÐyW5Ìã)Ì¼PdÜÂËRyjàhö¹?õ¡¥NgÌz)ÌÆÜ¢n¸íÊMWóI¦eFzKÒ2âX ßràyø±¬÷	zL²öÙËZ¹Þõ
Æ`qØ!Ç{Å#>Þöñ8çæ7êø"y|ÌÅ¶^­y#GùÖ]Ô¾BÍÉ|êÝ_kñäòª{}ÝÈk
]|ñ4ÚªÊ&ýQÂÕ'¼¬O~GÅ«rdb¯¢1Ò_?~Q?B^:CéQÈdøNKcUÕ¼~ÙãêÎò3¨	w3/SáA¼öÐ
÷'ëåã«t!(½þm]ýî:Çº:IkRÃªWòÏÚ½-ï ´ásûZÕ>ë
ÍLIû§×`F¥Êj+:hLdKûÒ=hõþ¥ÏUUêIZ!ù@=nO^$ß
ÃY¨5îâèhã5#f1xoSÇZþå6~
e6[KRýââ¨«»Z­PEo_ïó*UÙÐ4±­SnrûÖ×uF³ sÄQMþÆõ%yË×Qx¾"$ì»*±#Ï4m¤0Db¨àæhBïsPÒRÑ>+æ¨×Çó;D¿¼ù©¸)÷'k¬´î´Óâp>D
z2Ðùd@fÿñ÷ý¸¸[±,Y/ðq"¼¹bÆÁ4«Øh&ævÁ­õó6 dä^u¢Å©É>P½Hoéæ>ÔÃ»ø»kõòâ<Ä0|ÊPÀoíüÎMG³Â.&Àó}Ê! ÿñú§©7n~LÛ	õÆ}òÌ´-Þ@Â¦Nïd°A^ ÙQ	õ"n·P³d¯|9Ê]?ëºvO}n !~M	Ü±m_twyH·L®?øýeÒÛ¢ Ì6ÑWj1)Ã
DãèrÛBZ^Ò}TæpÁÏ^ÕkÐÇ?½Þý98-ÍPKi~Ç=âíáÚU¸¹Ä~-+§ü/µø»vQwG¿L÷B¼Ä®oê±¢Å^ Ó_;+sj.®¦¿-ºÉå¯#QæN¡TM@å>«Æ=S³éat¡s¾DoÑy7ç&äûRÓjöþø5
~ÖÚXÜÞ©÷²Ø(	æ`_plsc±,pVÈqsh{Í=u_b]+õÉìÃK5`±dé´ u¢ÁßHÔücîÃæ¯{è3DßÕsÀU²{:Y¼ã¿§çÙú©-®Þ>ÄH-#VªÑV/òlRqb@s+v"òõ`'Sß@ûÎh0£Ä}¾«ù¤4oV¶4:;Ñ­¼ZßÉiAý¾×q§ÌkY¾)¦ý\Ol
òq¶¤ø2q«{2cÞ²<-¸&¡ÄÏêZú?9?ùTLãÉM¼×®çYÐðZZ]Íôºµñ
dV
ÕK<Jû¯
»R 
±Í$&þ Æß(f2J}CÉÚ!LßCZQ,nTXÉ8\K
n$×5ÖÄ,MC­ÈþüµËø¶;DÓ»ÐCq¼)¯#«ÕÇÉ°É©|Ì6îKD9·Í½BÄbLK$ßÍX>G±dJÁ­ÔCù	KFæä;Û¦Å¬5%TØÉ	-®£\Ðþ 93ßïY©_ëVúõùxCLOÐ}«»]DÞ¡èo
ç)%ÙÚªõÑ´ìF¦û
$G³[l iUy¡l5¦
v%/,H&R6-K_H¡PòáÈ~Ô7Í³ùT±¶Ö½¡ù¹	1Ëîy«[öì0L ì:¢z\°y úÏR8GVÕã§££ß¦ÛÿÚlÆZªù×¤r.§½d\²½VX¤°¹])m%ÕYÂ'¥UÔ©O¥8¹­ÛÌÊ»TàlÕ[¸÷[e¦¼73a!êµÐ¡±[v\C;¹§dqü}\9âb.ÄåôÇ§¹/×ÿK¿Mi|Õå¼Óú÷¨)çØ=-Ê&½ÁÐÏwÔ«øj¨Nó1dT`Ò8ÑYölåND©MÓmÂ+ÉO(­ò(³iü©fÖ92t~à®ÿ»À¤s)ªSiÌÌeWñ¦µÀÚF£ªc& /e©µe,'úi9]Fª¾ sR(Fµ?ô6ÿV¸wÛy¬ÁÂgé:Dä¦øð½pë­W¾­¼GÉí÷6²eQòìÊx­ºòµ´-ÔykæqÜ#*H	®$éT.ù°þÄ1n®k)£4FR¶wÅ¯n?Õ¼]Ææ>u~Jà¡v@¯Øm2PSdó¸I¸l¯ì¿;w
ÚkxåpÏ2Õ°âêî^p¯¼ýÔ%«ÏËj!± ~ý4 !Åf'j)Rè,z¥²8(²Jy	[¸BÈVÎÈ´³vv¸Îtúò`½Ôê&õ¥t¶Ø®%PÏz
øëZI|.,ÞØ¶á6jÍ­ê¡ðm612wp¤·¦ó º9DÐòZ×üóbù,Ig¸?.Â¿ìÎ¾F;ªGN
ËñÍC¹m%%ÕLp*r¿G=aÀ@ªJ¹·OsÑÖÅÌ>¹ÝOµtªÒ¹çªÅ4Úa®ú{áº½N¼­~»zóå¬2ß¥çzXEÐ6X¶¼ß%·°e°_ ÏØËòô½ý¼fÍâR±(gàòä´
½Óõ±Ã
ñ´AR£q¾bGwvÒÐß@ô6÷J¾B~`É.ïbÀ`jé_0¾,E(" kAÉç gï8ÛÖÀåºvÿÎÙ wÄV=è¸«Á'}LfX8ÜÐb£ÙKþ`Á¼â³þ¬M¹aOåäýÏÂOdÂ¨`xGFDi§MÎ\äM^cÂ¨íh Í¸KÝeXÉ°9ÃÄ eGzO9T6òÅ£û2>Åx<USen÷a}§ ÆD«÷r¬ÀÐ<ë,I"&:ÇLëLYêÅ{1è7
PÎ»ÈýÕ&ò1,!¶ñîíWåÉ£·sDË©v¾Ôv]ÝÉî¬xa(24BCX*lw
GiñÊ?§ê	§Uß@>ZËýðuPò>Ë<PAëà³Cí-uXú#,Ì(¬Ââ¦»vÀ0ë'¦fÌãVÚ÷{å£xëCÅ$²B¼Ì¢Æák¯?v}±ì/IÌÊ³³ÍXÊýspßø3&·ñpgÈÍ lì½pßc!`uÐÉQÍìp(2á×cÐ«(GotMÓðÍîa8Ñ|tóÑöE±ClöccÎç½vBÏµ9¬²7n;ÈÁpôÎÒßêÎ£®|QðmZeªSÅÎúÝæs°ÄSt¥Ý`Uk;Ï5Á½'4yeÉ¾ÈÕÿöHÐ¼ÞÜB÷åXeÏL»Ñ³vØ&»åsê²x-8tgÒ¹Ò}æù3àù8öðAüLRÓÀ²Ï¢q|vj5¡æJYWÓÀð0TÍTºOßü.09Óõ¡Ö5aËIB
vÔqp¢îZgú·Ã×jÓqÑÔ[:9aZm¯FõË¬ÓÍóÔð=:¨öÒY)²<Á;µ[ÎÕdÐ¼=ÙhÅ^7Ìm[^ÕkW°\ßcIÔ¬.±Ú\ìÕú¼¸Az#<äàéê¸ÄqªÁÕòF!©%²æ`ðâ;±ªúØµ¾ÖîËlµõwÖêæØ0¸Ù\8aÇþºSöãÑè*W>]®õÙ§zFbj "ÛJð©57¡èáÚ#j1b#=}qcÂ%jInd³ÖÛrøwrGu+?¸Ö$Jk(ÙÛÈÿ±æoe|=
×õ}bË';NÜ$Ò÷.»mí²{<f¯îEÜ2SFÎ©UÚó%Ê®v
ÿçØÜãó¿,¼P»xÔªd &	sf	\ÞDkÀ~Ì=<­>t)ÞæhÅ@'¤lz-áU74 ßd`tcOB¾#úºÚÏì-ßUì@%ZÈùýgÇ·ræ#¢Æßcl

rf\"¿~~½º
óràrÉô¢çIîJÈ;ÞóF§á.XJó,¿*° ëòCá.¿¶UçìËæTºâñ1Bªj{¥ü¡lqAßJ°ã8[Yö³jÝ|û£­Ú¶ãêüg­oS¯éññÖR¢Îûä=mÎLM
 Iå:wFÛ²ùBätê3ÿ¿F´1Ô|÷Q'É¾RåÉ¹ä¯ö}~"w¡'_uÍóØåÉÕgv<ÓY
$çP3åçê8d"KÊÎKzä[ ÞÌæâ²ÑÖCK)®wZØÂäSédmìåWîÙñÊ¾	jïNéEÕ4Ëeé]Ù´ÆÎ=´¿é»~fç(+Ú ãìó3êL.ísx`¸§*÷ÑÂÑÏu®Bê]¸
U¸¹:êk½Ò¸4¶òùë&oyþGIüôj-Ñ§úÃë¯¿IÍzîþÙ
óØø÷gíecÿñã!ÏXåÉ\ h#±í½Îíèh¯DObwyîà¡ÌÁÉßîd"	ït­Ï¼ìþ±ÉÇVºÊRMIðÜ/ß#&ÃÄîh'0÷2ñ	ó¥9r_S^ryãÒ3$ñwÉkm7ì·(uþº$ô$Â)òGþ,Ò??_:·j¢ñIKÕÝ;ò®,gIØÂ\½Â+)¶Ûòçµ*}_|5gã	Çùòñj,LàÍôrë#%=aô1tZe·"]Üä·dÖòôãúÆÀ°@IîÕÊõÔõÚâõ«^Zqë=BÇÿ©`Ujõ$â8À«Â<ðÀ*¼FJÀèõøH1gg;ä|iÌªÊçÂªö5zÂË¸#I°âr]5¸jøõ9öPg÷&£G¥r­UÃ¹74>öÐ#S`2xOq'9w¹Û
öänñÖíé}°ß¯NÚø1À±÷zhÆHï±`u¨¤·'¹÷Æªn)«Ò^®NVæª,÷í60r)«¬ÂDUäî·¡çÖùw{Þ³íZWbâµdÜgwù¼jLók?¶Cþ(£½úE+dÞm!kPBÌ@ûYýñ9MBú×N¿é¬O  £ÙE¹ïÞTòûT2Ì³Ø¿H¯`×æÇK ûÉlXg-\2M¡ùù©û+?mÆD-èÇÏë>äbý¡_%ûÅZvrÍÚ	î âPÛjÛüÐ2Z@kfªÿÓø¥cäüFfoÛßla%+I÷b¨KüMùÈÃÓo#³?d
ì:,"üæ ´´úÀ°Îl°_JÇ¡¹ÖýsxÑáS'©¹åIéî»Þæüÿ(ZQ
 2dýH~V»éi¼1µ7õIõ>Û¯»_¶
è ®jmÝùÂ±swu°Ïtú~'êl¿¨`­TÎiQ!¼^QEÕ;Öí3ç³ÞîúõôÎèhF_ÿzDkßÿæ¢ËËcÜÿuµµï_«<kHyÈZ"îeÏ)9ÔÆßIúJ<aA e¨¹d=¶£2ÐKLbðáA·ïYV:~BO¨TAñIÌüî	ò p¦.~I÷zðõùâhPÅðmÓÝÃ¢úÃ®¹~JÑ!ö+SÜK´õ2ûª^!iSD÷E)Ú8¦7Ï>	´Z×ok"g
<ÝÁ<Vªv·p/~³ÓO\|^Ò»0ýOøDµpíj@Hñ«lÌ"Eî§Ð¾¥~lmíìÛÀEñÁ.¹QpØNqÌaÁ,¢]$»ÌÆUãU±¹ãÿZx<õq1Tì jG&îà¶¼{¥Q*ÏNj¤c±7$3©Ç¯_vnÃj¦¾Õ;-3 ð¨ÀÍyò$@±j9º UògnÞÎ|üî]¦Û@fû }øµé
 Æ¡ Xä+b
å}]e²­ifZN µ³UûëEØOzÏDU©ÍÌ/LZuûäÀÌfçTACObJÕYhêÃ¹	·©Ktõµ¼³~Iúeëµd÷?<÷Äè92ËnäYµàUÄh¹K"¡£ä¥8ç!Ó¥3`3§ïü·DÀ#QÓ¶ CÙËíõm©p¢¬Ä[æ)UB>ë3GnO/czÂ¶tK÷8-§ÚÓøÐëH74$é|Z¸îåì0¥þü3(7{Ü¿Apù2c}Z«Êq»½/N+·ÌÙKeð=, ú0únNbÌ£ZNºY­nu[$6ëFß`Çðå¸;Rj_µWîË¢Þ)ªA²Åi$
d¥g×¡ø1YÚo[Æ$W#ùµÎs/=Y"5NhlXûL)Ç{+È¿añ¿8ÁGÓÔ=Á|TJ´h¸_¥µ°P÷º[²w»¦ÿ²õJ­pÏ¤	7>º(±O~Rö9-£Q§³ÁèL^¡'Z*×üëµ2tËKîfËÄ2g%HreÊOÛB*:'+'þúi<-YïÍ~§®ôòíßHDßA µþù`!´þê qÉEan##^gURÄ»BB¶H]ÒÞèY8!äB°¬-rSèãêö«ãçy#¨ÉUóµ¹xGí»/Xô@­Z#û¡ñ­»+ÀÀÞB`ß÷¯³ã+¶¨>:iwÓL×T9EëPhàÇùÄÏÀv·»]	¶è¡ÉÜJà@¶!Ç±Ã£B'î)Y0Ý?0cVÇ	ÊÅWÝ­;[=]¡ây´i ¼?±4ãb)ÇAÚ#Å´&(¼¥µY5*]M3¥ôÇW©ÕwÖµwBPQ& ÕQ·ÝØFá¸?ûiAPwýßþ"À¾§¬YÖãQ~/=tZû-Z6Õ­ÔÇ¬¥·ñªÎ§Àotâ¬Õ~ìÑÀ®pï¯ç¼ÌÜÕ/
^óy9&ÓÇC~~ò@Ö5Ý6·Tüðum­W26cë[¥&Ç/AÕS|NZ¾Ü;ìAÁ'úýÐÇå£Éu:ã¼oqq¤6Ú8E÷ó¡-
÷ÜðOyÐÑSÂËS/æR.ßð® 	y«­nv )PÝ[Õ3"M?Êðgs¤DäÁgp8Pp=^ðhÉFïØ~É[e'fÁ««RrvÿÓw7Tòúë/nó>×qZ0J=jÚmL]ä®õ<WbX¿Ø~Ë7ÃhQUbÆü¯bláÜBüá¾èZß^¸¨_¼üÞã+Àp¡\~¾
vý3¦u;ôÓBkËMe,Ç5âÀ.ImÍÉêgOTðý  Ð  v  ¶  è  À   "  ¨{  ,* :  Þ  è   
¾  Q  r  }Ñ  Ê  ;&   Ú  àU  ¸  Ô  ¶f    jJ  Ñl  "  63  i´  §ü  3a  qÂ  ~  '  i9  :  µ@  ô  d¢  a& 
N  9á  è§  ¡  È ô  .  Ç  X  i
  Â  ¡  Ð  u¤  lí    
 {  º  5n ²  ¾É °  ·m  ñ  _  #  <  ­  Ì£  ¾¬  4  ×¦  Ô  Ðw  ÷&  Ú$  }£    í÷  u Ô q  ÌÁ Þ  Þ  aÿ  3O  1´  »Ï  ¸Í  ßÙ  ö  g   ²  ¿  Ù÷    1ú 
  èE O     Ïæ   ð n 	!  &  û  ¦  ç  
è  í  +ö  
E       ið  .\  ' Å  ·  '  Õ¬   ±  î n  ô  w  ¿¢ Ë  rß    ¨À A  ~¸  ¿w  ð  Ð  û  #/  ¹
  
  m+  ."  pò  Â°  _  2ë   í  ÉÎ  t  ½s  õe  8C  @  à  Qd  =H  ñ?  ½.  ak  ¯;  Î  ¹û  4H  zg  Õ  È  eÅ  G 2 
t  ¸'  ·  ïØ    Õð þ  7 .  Öj  T  Lú  4³  ø  Ôi  ¼Ë  Ff  PN 
ñ  Kh 
  ¹°  ÿW  ¶7  v(  !  u  À  Ð¸  Â  J×  gé  r  ý  re  9  k  @  ²" 
Ð  ô  u¼  Ï¼ à  ¦F    Á-  kT  )  ¸  yY   ßû  "ê  2Ù  ¬è  s[  ¦§   ty  Ê  ð  »  nA  î  À@  ôz ¬ ÿ  {  ÅÆ  8+ 1  yá  ô	  æ  ·  Ë(  '  ªÊ 
G  ¤  £ì   y  uã  h   ¨  Ë÷ y  Q  5\  ò  î²  É£  ò·  hÜ  Êù  =u  æ\    ¤ê  Ñß  qñ    ©  Ó   |  Ô®  õ/  [Ó  ü  Z  Àl  ~B  òh  ÀÍ  sÐ  õ  ¾  !£ 
  s/  ÙÌ  uI  I 
  o  ÈÂ  N  ¡½  ½  Å  ML  Ât  m  ó  µ  nX  Ð  z  Ø  I Ö    ÂØ    7  í  XÖ Ñ  Õ-  µ«  ?§  j  ×ë  é w  ¨ç  ie  z;  µË  5  óô  k  Ì  aJ  íb  È°  ÖË ¤  s 	N  /  3    à( Ó  y 	Ë  ñh  2  (ô    ±¡  ð  4æ  ìú  5  õ  l   µÞ  2ü  ÕÉ  É|  Ï 
¡  ¿ì  ¼  ª§  md  ý5  ý  4p  Q1  Ö  Áä  4  ï»  Ã  ÕN    Z  Ê>  y;  Ë³  ôG  ¦ô  <é  7  ÈÔ  k  :£  	£  òÏ H  !á·§~Oò,z²qNæ*óßH4¸ÍYI;¿|1tÆ\W½Cï
```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/objects/pack/pack-b7a77e8e4ff22c7ab2714ee62af3df0214483413.rev

```text
## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/objects/pack/pack-b7a77e8e4ff22c7ab2714ee62af3df0214483413.rev (latin-1)

```text
RIDX         h  	  @  o      /   V  d     ?   ÷      Í  "  }     u   r   w  _      9   "        C           5   1   ]   8   $    V   x   ;   
      ¶   Ë  k  T     p   ­      Ï   ß  /  i   4  !   {   
  *     ç     h   â   t         z   Y   d  g   è     s   X     `   «  ~     ¾  l  n  
   <     E     ¹   ù       *          ¤    K   ¡   Â   °   Ð   Å   ½  7   Ã     £    G      B   (  X   §   W   '   ¯   Ñ     2   #  Q      y  L      á     Ö  p   7  9     {   ñ  <            Ò   Ô     ,   ê  ]  '      í   Q  .   Ì   6   Û        Ê     ä   û  R   ¬  >   N      !  $      ×  a   3   ï  1  B   5   Õ   ^     a  N     ®   _   	   O    )       3   J      n      ý   ¼  y      H     c   ð   ¿    D   ©   ,   D    W   o          4         Þ   ë             P  z     é   E   ¨  j   Ø  ;   %  J  S  r      É      ´   þ   @   }   ³   ã      [      Ç   ª   Z   Á   ¦      G   >        x      ó  #  &   à    8     C  6   ø   -  Z  2    u             î     ÿ    
   F   T  v   Ü   i       K  =   Î        À    I       t   ·   »  [   I  M  -   b   M   \   æ  b      ¢     q      f   +  m     Y  F   s   P   ò       µ   k      ¥  f   A  %        :  U   ü        ô   &       (   L   Ó  |   È   0   Ú   S  q        ì     O   .   m  ^  e  0   )  +      Ä   ±  H   j   g   :   =   e     ²  w   Ù   º      l   v   |    A   U   `   Ý   Æ   å  c        ?         ú     \   R   ¸   ~   õ   ö·§~Oò,z²qNæ*óßH4Ìèü]j98¿û}®ol9¸
```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/info/exclude

```text
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/logs/HEAD

```text
0000000000000000000000000000000000000000 4a204a6ed4f0223c846b7a9fc5372483715d87f5 Your Name <segodimo@gmail.com> 1762860195 -0300	checkout: moving from init_placeholder to refs/heads/manifest-rev
4a204a6ed4f0223c846b7a9fc5372483715d87f5 4a204a6ed4f0223c846b7a9fc5372483715d87f5 Your Name <segodimo@gmail.com> 1762860219 -0300	checkout: moving from 4a204a6ed4f0223c846b7a9fc5372483715d87f5 to master

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/logs/refs/heads/master

```text
0000000000000000000000000000000000000000 4a204a6ed4f0223c846b7a9fc5372483715d87f5 Your Name <segodimo@gmail.com> 1762860219 -0300	branch: Created from HEAD

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/logs/refs/heads/manifest-rev

```text
0000000000000000000000000000000000000000 4a204a6ed4f0223c846b7a9fc5372483715d87f5 Your Name <segodimo@gmail.com> 1762860195 -0300	west update: moving to 4a204a6ed4f0223c846b7a9fc5372483715d87f5

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/logs/refs/remotes/segodimor2d2/master

```text
0000000000000000000000000000000000000000 4a204a6ed4f0223c846b7a9fc5372483715d87f5 Your Name <segodimo@gmail.com> 1762860231 -0300	pull: storing head

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/logs/refs/remotes/segodimor2d2/HEAD

```text
0000000000000000000000000000000000000000 4a204a6ed4f0223c846b7a9fc5372483715d87f5 Your Name <segodimo@gmail.com> 1762860231 -0300	fetch

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/pre-merge-commit.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/pre-rebase.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/update.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/applypatch-msg.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/commit-msg.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/prepare-commit-msg.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/pre-applypatch.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/pre-push.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/sendemail-validate.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/pre-commit.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/fsmonitor-watchman.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/post-update.sample

```text
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/pre-receive.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/hooks/push-to-checkout.sample

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


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/refs/heads/master

```text
4a204a6ed4f0223c846b7a9fc5372483715d87f5

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/refs/heads/manifest-rev

```text
4a204a6ed4f0223c846b7a9fc5372483715d87f5

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/refs/remotes/segodimor2d2/master

```text
4a204a6ed4f0223c846b7a9fc5372483715d87f5

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.git/refs/remotes/segodimor2d2/HEAD

```text
ref: refs/remotes/segodimor2d2/master

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/.github/workflows/build.yml

```text
name: Build ZMK firmware
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    uses: zmkfirmware/zmk/.github/workflows/build-user-config.yml@v0.2

```


## arquivo: /home/segodimo/zmk-ws/zmkpromicro/zephyr/module.yml

```text
build:
  settings:
    board_root: .

```


