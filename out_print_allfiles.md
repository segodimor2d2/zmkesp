# Projeto da pasta: /home/segodimo/zmk-ws/zmk-config

## arquivo: /home/segodimo/zmk-ws/zmk-config/.gitignore

```text
build/
zmk/
modules/
tools/
.west/

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/build.yaml

```text
---
include:
#  - board: rec_corne_left
#    shield: nice_view
#    #snippet: zmk-usb-logging    # Uncomment to log over USB.
  - board: rec_corne_right
    shield: nice_view
    #snippet: zmk-usb-logging
  - board: rec_corne_left
    shield: nice_view
    snippet: studio-rpc-usb-uart
    cmake-args: -DCONFIG_ZMK_STUDIO=y -DCONFIG_ZMK_STUDIO_LOCKING=n
    artifact-name: rec_corne_studio_left
  - board: rec_corne_left
    shield: settings_reset
    #snippet: zmk-usb-logging
 

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/config/rec_corne.json

```json
{
  "id": "rec_corne",
  "name": "Rec Corne",
  "layouts": {
    "default_layout": {
      "name": "default_layout",
      "layout": [
        { "row": 0, "col":  0, "x":     0, "y": 0.37 },
        { "row": 0, "col":  1, "x":     1, "y": 0.37 },
        { "row": 0, "col":  2, "x":     2, "y": 0.12 },
        { "row": 0, "col":  3, "x":     3, "y":    0 },
        { "row": 0, "col":  4, "x":     4, "y": 0.12 },
        { "row": 0, "col":  5, "x":     5, "y": 0.24 },
        { "row": 0, "col":  9, "x":  9.25, "y": 0.24, "label":    "5-way up" },
        { "row": 0, "col": 11, "x":  11.5, "y": 0.24 },
        { "row": 0, "col": 12, "x":  12.5, "y": 0.12 },
        { "row": 0, "col": 13, "x":  13.5, "y":    0 },
        { "row": 0, "col": 14, "x":  14.5, "y": 0.12 },
        { "row": 0, "col": 15, "x":  15.5, "y": 0.37 },
        { "row": 0, "col": 16, "x":  16.5, "y": 0.37 },

        { "row": 1, "col":  0, "x":     0, "y": 1.37 },
        { "row": 1, "col":  1, "x":     1, "y": 1.37 },
        { "row": 1, "col":  2, "x":     2, "y": 1.12 },
        { "row": 1, "col":  3, "x":     3, "y":    1 },
        { "row": 1, "col":  4, "x":     4, "y": 1.12 },
        { "row": 1, "col":  5, "x":     5, "y": 1.24 },
        { "row": 1, "col":  8, "x":  8.25, "y": 1.24, "label":  "5-way left" },
        { "row": 1, "col":  9, "x":  9.25, "y": 1.24, "label": "5-way press" },
        { "row": 1, "col": 10, "x": 10.25, "y": 1.24, "label": "5-way right" },
        { "row": 1, "col": 11, "x":  11.5, "y": 1.24 },
        { "row": 1, "col": 12, "x":  12.5, "y": 1.12 },
        { "row": 1, "col": 13, "x":  13.5, "y":    1 },
        { "row": 1, "col": 14, "x":  14.5, "y": 1.12 },
        { "row": 1, "col": 15, "x":  15.5, "y": 1.37 },
        { "row": 1, "col": 16, "x":  16.5, "y": 1.37 },

        { "row": 2, "col":  0, "x":     0, "y": 2.37 },
        { "row": 2, "col":  1, "x":     1, "y": 2.37 },
        { "row": 2, "col":  2, "x":     2, "y": 2.12 },
        { "row": 2, "col":  3, "x":     3, "y":    2 },
        { "row": 2, "col":  4, "x":     4, "y": 2.12 },
        { "row": 2, "col":  5, "x":     5, "y": 2.24 },
        { "row": 2, "col":  6, "x":  6.25, "y": 2.24, "label":        "4\n2" },
        { "row": 2, "col":  9, "x":  9.25, "y": 2.24, "label":  "5-way down" },
        { "row": 2, "col": 11, "x":  11.5, "y": 2.24 },
        { "row": 2, "col": 12, "x":  12.5, "y": 2.12 },
        { "row": 2, "col": 13, "x":  13.5, "y":    2 },
        { "row": 2, "col": 14, "x":  14.5, "y": 2.12 },
        { "row": 2, "col": 15, "x":  15.5, "y": 2.37 },
        { "row": 2, "col": 16, "x":  16.5, "y": 2.37 },

        { "row": 3, "col":  3, "x":   3.5, "y": 3.12 },
        { "row": 3, "col":  4, "x":   4.5, "y": 3.12,                         "r":  12, "rx":  4.5, "ry": 4.12 },
        { "row": 3, "col":  5, "x":   5.5, "y": 3.12,                         "r":  24, "rx": 5.15, "ry": 4.33 },
        { "row": 3, "col": 11, "x":    11, "y": 3.12,                         "r": -24, "rx": 12.3, "ry": 4.33 },
        { "row": 3, "col": 12, "x":    12, "y": 3.12,                         "r": -12, "rx":   13, "ry": 4.12 },
        { "row": 3, "col": 13, "x":    13, "y": 3.12 }
      ]
    }
  },
  "sensors": [
    {
      "ref": "left_encoder",
      "name": "encoder_left",
      "identifier": "encoder_left",
      "compatible": "alps,ec11",
      "label": "LEFT_ENCODER",
      "enabled": true
    }
  ]
}

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/config/rec_corne.keymap

```text
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
        td0: td0 {
            compatible = "zmk,behavior-tap-dance";
            display-name = "Shift/Caps Lock Tap Dance";
            #binding-cells = <0>;
            bindings = <&kp LEFT_SHIFT>, <&kp CAPS>;
        };

        parenthesis: parenthesis {
            compatible = "zmk,behavior-tap-dance";
            label = "PARENTHESIS";
            #binding-cells = <0>;
            bindings = <&kp RIGHT_PARENTHESIS>, <&kp LEFT_PARENTHESIS>;
        };

        bracket: bracket {
            compatible = "zmk,behavior-tap-dance";
            label = "BRACKET";
            #binding-cells = <0>;
            bindings = <&kp BSLH>, <&kp RIGHT_BRACKET>;
        };

        brace: brace {
            compatible = "zmk,behavior-tap-dance";
            label = "BRACE";
            #binding-cells = <0>;
            bindings = <&kp PIPE>, <&kp RIGHT_BRACE>;
        };
    };

    rgb_encoder: rgb_encoder {
        compatible = "zmk,behavior-sensor-rotate";
        #sensor-binding-cells = <0>;
        bindings = <&rgb_ug RGB_BRI>, <&rgb_ug RGB_BRD>;
    };

    scroll_encoder: scroll_encoder {
        compatible = "zmk,behavior-sensor-rotate";
        #sensor-binding-cells = <0>;
        bindings = <&msc SCRL_DOWN>, <&msc SCRL_UP>;

        tap-ms = <100>;
    };

    combos {
        compatible = "zmk,combos";

        device1 {
            bindings = <&bt BT_SEL 0>;
            key-positions = <4 44>;
            layers = <3>;
        };

        device2 {
            bindings = <&bt BT_SEL 1>;
            key-positions = <3 44>;
            layers = <3>;
        };

        device3 {
            bindings = <&bt BT_SEL 2>;
            key-positions = <2 44>;
            layers = <3>;
        };

        device4 {
            bindings = <&bt BT_SEL 3>;
            key-positions = <17 44>;
            layers = <3>;
        };

        device5 {
            bindings = <&bt BT_SEL 4>;
            key-positions = <16 44>;
            layers = <3>;
        };

        lsysreset {
            bindings = <&sys_reset>;
            key-positions = <44 28>;
        };

        rsysreset {
            bindings = <&sys_reset>;
            key-positions = <45 41>;
        };

        lbootloader {
            bindings = <&bootloader>;
            key-positions = <44 13>;
        };

        rbootloader {
            bindings = <&bootloader>;
            key-positions = <27 45>;
        };

        sutudiounlock {
            bindings = <&studio_unlock>;
            key-positions = <44 0>;
        };

        outble {
            bindings = <&out OUT_BLE>;
            key-positions = <44 14>;
            layers = <3>;
        };

        outusb {
            bindings = <&out OUT_USB>;
            key-positions = <44 29>;
            layers = <3>;
        };
    };

    keymap {
        compatible = "zmk,keymap";

        default_layer {
            display-name = "QWERTY";
            bindings = <
&kp ESC    &kp Q  &kp W  &kp E     &kp R  &kp T                                 &mmv MOVE_UP                     &kp Y        &kp U  &kp I            &kp O    &kp P     &kp BSPC
&kp LSHFT  &kp A  &kp S  &kp D     &kp F  &kp G                 &mmv MOVE_LEFT  &mkp LCLK       &mmv MOVE_RIGHT  &kp H        &kp J  &kp K            &kp L    &kp SEMI  &kp ESC
&kp LCTRL  &kp Z  &kp X  &kp C     &kp V  &kp B        &none                    &mmv MOVE_DOWN                   &kp N        &kp M  &kp COMMA        &kp DOT  &kp FSLH  &kp RSHIFT
                         &kp LALT  &mo 2  &lt 4 SPACE                                                            &lt 3 ENTER  &mo 1  &kp RIGHT_SHIFT
            >;
        };

        lower_numer {
            display-name = "NUMBER";
            bindings = <
&kp TAB    &none      &kp N9  &kp N8  &kp N7  &none                          &kp HOME            &kp LS(LEFT_BRACE)  &kp PG_DN       &kp PG_UP     &kp NON_US_BACKSLASH  &kp EXCL       &kp LBKT
&kp LSHFT  &kp EQUAL  &kp N6  &kp N5  &kp N4  &kp N0                 &kp N0  &kp ESC   &kp DLLR  &mmv MOVE_LEFT      &mmv MOVE_DOWN  &mmv MOVE_UP  &mmv MOVE_RIGHT       &kp RA(W)      &kp SQT
&kp LCTRL  &none      &kp N3  &kp N2  &kp N1  &kp N0        &none            &kp END             &kp LEFT            &kp DOWN        &kp UP        &kp RIGHT             &kp KP_DIVIDE  &kp MINUS
                              &none   &none   &kp LEFT_ALT                                       &kp SPACE           &none           &mkp LCLK
            >;
        };

        raise_symbol {
            display-name = "SYMBOL";
            bindings = <
&kp LA(TAB)  &trans  &kp LC(HOME)  &kp HOME  &kp END  &kp LC(END)                    &kp HOME            &kp RA(UNDERSCORE)  &kp MINUS  &kp PLUS  &kp PRCNT  &parenthesis  &kp DELETE
&kp LSHFT    &trans  &trans        &trans    &trans   &trans                 &kp N0  &trans    &kp DLLR  &kp N0              &kp STAR   &kp HASH  &kp DLLR   &bracket      &kp GRAVE
&kp LCTRL    &trans  &trans        &trans    &trans   &trans       &trans            &kp END             &kp EQUAL           &kp AT     &kp EXCL  &kp RA(W)  &brace        &kp AMPS
                                   &trans    &none    &trans                                             &kp RET             &trans     &trans
            >;
        };

        fn_layer {
            display-name = "FN";
            bindings = <
&none  &kp F10  &kp F9  &kp F8  &kp F7  &none                            &rgb_ug RGB_BRI                   &none     &none      &none     &none      &none  &none
&none  &kp F11  &kp F6  &kp F5  &kp F4  &none           &rgb_ug RGB_EFR  &rgb_ug RGB_TOG  &rgb_ug RGB_EFF  &none     &none      &none     &none      &none  &none
&none  &kp F12  &kp F3  &kp F2  &kp F1  &none  &none                     &rgb_ug RGB_BRD                   &kp LEFT  &kp DOWN   &kp UP    &kp RIGHT  &none  &none
                        &none   &none   &none                                                              &none     &kp SPACE  &kp RALT
            >;
        };

        rec_layer {
            display-name = "REC";
            bindings = <
&trans  &trans  &trans      &trans        &trans        &trans                    &kp C_VOL_UP          &msc SCRL_LEFT  &msc SCRL_DOWN  &msc SCRL_UP  &msc SCRL_RIGHT  &trans  &trans
&trans  &trans  &mkp MCLK   &mkp RCLK     &mkp LCLK     &none             &trans  &kp C_MUTE    &trans  &mmv MOVE_LEFT  &mmv MOVE_DOWN  &mmv MOVE_UP  &mmv MOVE_RIGHT  &trans  &kp PG_UP
&none   &trans  &kp C_MUTE  &kp C_VOL_DN  &kp C_VOL_UP  &trans  &trans            &kp C_VOL_DN          &kp LEFT_ARROW  &kp DOWN        &kp UP        &kp RIGHT        &trans  &kp PG_DN
                            &trans        &trans        &none                                           &trans          &trans          &trans
            >;
        };

    };
};

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/config/rec_corne.conf

```text
#
# Copyright (c) 2024 The ZMK Contributors
# SPDX-License-Identifier: MIT
#
# go to sleep after one hour (1*60*60*1000ms)

CONFIG_ZMK_IDLE_SLEEP_TIMEOUT=3600000

CONFIG_ZMK_SLEEP=y

CONFIG_WS2812_STRIP=y
CONFIG_ZMK_RGB_UNDERGLOW=y
CONFIG_ZMK_RGB_UNDERGLOW_ON_START=y

CONFIG_ZMK_RGB_UNDERGLOW_AUTO_OFF_IDLE=y
CONFIG_ZMK_RGB_UNDERGLOW_HUE_START=160
CONFIG_ZMK_RGB_UNDERGLOW_EFF_START=3

# Uncomment the following line to enable NKRO
CONFIG_ZMK_HID_REPORT_TYPE_NKRO=y

# Some operating systems have problems with full support for consumer keycodes.
# Uncomment the following line if keycodes labeled "consumer" like C_AC_SEARCH don't work
#CONFIG_ZMK_HID_CONSUMER_REPORT_USAGES_BASIC=y

#EC11 enable
CONFIG_EC11=y
CONFIG_EC11_TRIGGER_GLOBAL_THREAD=y

# Mouse enable
CONFIG_ZMK_POINTING=y

CONFIG_ZMK_BACKLIGHT=y
CONFIG_ZMK_BACKLIGHT_BRT_START=100
CONFIG_ZMK_POINTING_SMOOTH_SCROLLING=y
# Uncomment the following line to increase the keyboard's wireless range
CONFIG_BT_CTLR_TX_PWR_PLUS_8=y

CONFIG_ZMK_KSCAN_DEBOUNCE_PRESS_MS=8
CONFIG_ZMK_KSCAN_DEBOUNCE_RELEASE_MS=8

# CONFIG_ZMK_UNICODE_ENABLE=y


```


## arquivo: /home/segodimo/zmk-ws/zmk-config/config/west.yml

```text
manifest:
  remotes:
    - name: zmkfirmware
      url-base: https://github.com/zmkfirmware
      # Additional modules containing boards/shields/custom code can be listed here as well.
      # See:
      # - https://zmk.dev/docs/features/modules
      # - https://docs.zephyrproject.org/3.5.0/develop/west/manifest.html#projects
  projects:
    - name: rec_corne
      url: https://github.com/a741725193/zmk-new_corne
      revision: main
    - name: zmk
      remote: zmkfirmware
      revision: main
      import: app/west.yml
  self:
    path: config

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne_left.dts

```text
/*
*
* Copyright (c) 2024 The ZMK Contributors
* SPDX-License-Identifier: MIT
*
*/

#include "rec_corne.dtsi"

&left_encoder {
    status = "okay";
};

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/board.cmake

```text
# Copyright (c) 2024 The ZMK Contributors
# SPDX-License-Identifier: MIT

board_runner_args(nrfjprog "--nrf-family=NRF52" "--softreset")

include(${ZEPHYR_BASE}/boards/common/uf2.board.cmake)
include(${ZEPHYR_BASE}/boards/common/blackmagicprobe.board.cmake)
include(${ZEPHYR_BASE}/boards/common/nrfjprog.board.cmake)

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne_right.dts

```text
/*
*
* Copyright (c) 2024 The ZMK Contributors
* SPDX-License-Identifier: MIT
*
*/

#include "rec_corne.dtsi"

&default_transform {
    col-offset = <7>;
};

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne.keymap

```text
#include <behaviors.dtsi>
#include <dt-bindings/zmk/bt.h>
#include <dt-bindings/zmk/keys.h>
#include <dt-bindings/zmk/mouse.h>
#include <dt-bindings/zmk/outputs.h>
#include <dt-bindings/zmk/rgb.h>

/ {
    behaviors {
        td0: td0 {
            compatible = "zmk,behavior-tap-dance";
            #binding-cells = <0>;
            bindings = <&kp LEFT_SHIFT>, <&kp CAPS>;
        };
    };

    rgb_encoder: rgb_encoder {
        compatible = "zmk,behavior-sensor-rotate";
        #sensor-binding-cells = <0>;
        bindings = <&rgb_ug RGB_BRI>, <&rgb_ug RGB_BRD>;
    };

    keymap {
        compatible = "zmk,keymap";

        default_layer {
            display-name = "QWERTY";

            bindings = <
&kp TAB    &kp Q  &kp W      &kp E     &kp R  &kp T                              &kp UP                &kp Y        &kp U  &kp I      &kp O    &kp P     &kp BSPC
&td0       &kp A  &kp S      &kp D     &kp F  &kp G                    &kp LEFT  &kp ENTER  &kp RIGHT  &kp H        &kp J  &kp K      &kp L    &kp SEMI  &kp SQT
&kp LCTRL  &kp Z  &kp X      &kp C     &kp V  &kp B       &kp SPACE              &kp DOWN              &kp N        &kp M  &kp COMMA  &kp DOT  &kp FSLH  &kp ESC
                             &kp LGUI  &mo 1  &lt 3 SPACE                                              &lt 3 ENTER  &mo 2  &kp RALT
            >;

            sensor-bindings = <&inc_dec_kp C_VOLUME_UP C_VOLUME_DOWN>;
        };

        lower_layer {
            display-name = "NUMBER";
            bindings = <
&trans  &kp N1           &kp N2          &kp N3        &kp N4        &kp N5                                &trans            &kp N6           &kp N7           &kp N8           &kp N9           &kp N0    &kp BSPC
&trans  &bt BT_CLR_ALL   &bt BT_SEL 0    &bt BT_SEL 1  &bt BT_SEL 2  &bt BT_SEL 3                  &trans  &mkp LCLK  &trans &kp LEFT         &kp DOWN         &kp UP           &kp RIGHT        &kp HOME  &kp PG_UP
&trans  &rgb_ug RGB_OFF  &rgb_ug RGB_ON  &trans        &trans        &rgb_ug RGB_EFF &kp C_MUTE            &trans            &rgb_ug RGB_EFR  &rgb_ug RGB_SPI  &rgb_ug RGB_BRI  &rgb_ug RGB_BRD  &kp END   &kp PG_DN
                                         &trans        &trans        &trans                                                  &kp INS          &kp DEL          &trans
            >;

            sensor-bindings = <&inc_dec_kp PG_UP PG_DN>;
        };

        raise_layer {
            display-name = "SYMBOL";
            bindings = <
&trans  &kp EXCL      &kp AT        &kp HASH   &kp DLLR   &kp PRCNT                       &trans            &kp CARET  &kp AMPS   &kp ASTRK  &kp LPAR  &kp RPAR  &kp BSPC
&trans  &bt BT_CLR    &mkp LCLK     &mkp MCLK  &mkp RCLK  &mkp MB4                &trans  &mkp LCLK  &trans &kp MINUS  &kp EQUAL  &kp LBKT   &kp RBKT  &kp BSLH  &kp GRAVE
&trans  &out OUT_USB  &out OUT_BLE  &none      &none      &mkp MB5  &kp C_MUTE            &trans            &kp UNDER  &kp PLUS   &kp LBRC   &kp RBRC  &kp PIPE  &kp TILDE
                                    &trans     &trans     &kp SPACE                                         &kp RET    &trans     &trans
            >;

            sensor-bindings = <&inc_dec_kp PG_UP PG_DN>;
        };

        layer_3 {
            display-name = "Fn";
            bindings = <
&trans  &kp F1      &kp F2      &kp F3       &kp F4     &kp F5                         &trans            &kp F6       &kp F7     &kp F8       &kp F9      &kp F10          &kp F11
&trans  &trans      &mkp LCLK   &mkp MCLK    &mkp RCLK  &mkp MB4               &trans  &mkp LCLK  &trans &bootloader  &mkp LCLK  &mkp MCLK    &mkp RCLK   &kp PRINTSCREEN  &kp F12
&trans  &sys_reset  &trans      &bootloader  &trans     &mkp MB5 &kp C_MUTE            &trans            &trans       &trans     &bootloader  &sys_reset  &kp SCROLLLOCK   &kp PAUSE_BREAK
                                &trans      &trans      &trans                                           &trans       &trans     &trans
            >;

            sensor-bindings = <&rgb_encoder>;
        };
    };
};

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/Kconfig.defconfig

```text
#
# Copyright (c) 2024 The ZMK Contributors
# SPDX-License-Identifier: MIT
#

if BOARD_REC_CORNE_LEFT

config ZMK_KEYBOARD_NAME
    default "REC_Corne"

config ZMK_SPLIT_ROLE_CENTRAL
    default y

endif # BOARD_REC_CORNE_LEFT

if BOARD_REC_CORNE_LEFT || BOARD_REC_CORNE_RIGHT

config BOARD
    default "rec_corne"

config BOARD_ENABLE_DCDC
    bool "Enable DCDC mode"
    select SOC_DCDC_NRF52X
    default y

config BOARD_ENABLE_DCDC_HV
    bool "Enable High Voltage DCDC converter"
    default y
    select SOC_DCDC_NRF52X_HV
    depends on (BOARD_REC_CORNE_LEFT || BOARD_REC_CORNE_RIGHT)

config ZMK_SLEEP
    default y

config ZMK_SPLIT
    default y

config BT_CTLR
    default BT

if USB

config USB_NRFX
    default y

config USB_DEVICE_STACK
    default y

endif # USB

if ZMK_BACKLIGHT

config PWM
    default y

config LED_PWM
    default y

endif # ZMK_BACKLIGHT

endif # BOARD_REC_CORNE_LEFT || BOARD_REC_CORNE_RIGHT

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne.yaml

```text
identifier: rec_corne
name: Rec Corne
url: https://github.com/segodimor2d2/zmk-config
type: mcu
arch: arm
toolchain:
  - zephyr
  - gnuarmemb
  - xtools
supported:
  - adc
  - usb_device
  - ble
  - ieee802154
  - pwm
  - watchdog
  - gpio
  - spi

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne-layouts.dtsi

```text
/*
*
* Copyright (c) 2024 The ZMK Contributors
* SPDX-License-Identifier: MIT
*
*/

#include <physical_layouts.dtsi>

/ {
    default_layout: default_layout {
        compatible = "zmk,physical-layout";
        display-name = "Layout";

        transform = <&default_transform>;

        keys  //                     w   h    x    y     rot    rx    r
            = <&key_physical_attrs 100 100    0   37       0     0     0>
            , <&key_physical_attrs 100 100  100   37       0     0     0>
            , <&key_physical_attrs 100 100  200   12       0     0     0>
            , <&key_physical_attrs 100 100  300    0       0     0     0>
            , <&key_physical_attrs 100 100  400   12       0     0     0>
            , <&key_physical_attrs 100 100  500   24       0     0     0>
            , <&key_physical_attrs 100 100  925   24       0     0     0>
            , <&key_physical_attrs 100 100 1150   24       0     0     0>
            , <&key_physical_attrs 100 100 1250   12       0     0     0>
            , <&key_physical_attrs 100 100 1350    0       0     0     0>
            , <&key_physical_attrs 100 100 1450   12       0     0     0>
            , <&key_physical_attrs 100 100 1550   37       0     0     0>
            , <&key_physical_attrs 100 100 1650   37       0     0     0>
            , <&key_physical_attrs 100 100    0  137       0     0     0>
            , <&key_physical_attrs 100 100  100  137       0     0     0>
            , <&key_physical_attrs 100 100  200  112       0     0     0>
            , <&key_physical_attrs 100 100  300  100       0     0     0>
            , <&key_physical_attrs 100 100  400  112       0     0     0>
            , <&key_physical_attrs 100 100  500  124       0     0     0>
            , <&key_physical_attrs 100 100  825  124       0     0     0>
            , <&key_physical_attrs 100 100  925  124       0     0     0>
            , <&key_physical_attrs 100 100 1025  124       0     0     0>
            , <&key_physical_attrs 100 100 1150  124       0     0     0>
            , <&key_physical_attrs 100 100 1250  112       0     0     0>
            , <&key_physical_attrs 100 100 1350  100       0     0     0>
            , <&key_physical_attrs 100 100 1450  112       0     0     0>
            , <&key_physical_attrs 100 100 1550  137       0     0     0>
            , <&key_physical_attrs 100 100 1650  137       0     0     0>
            , <&key_physical_attrs 100 100    0  237       0     0     0>
            , <&key_physical_attrs 100 100  100  237       0     0     0>
            , <&key_physical_attrs 100 100  200  212       0     0     0>
            , <&key_physical_attrs 100 100  300  200       0     0     0>
            , <&key_physical_attrs 100 100  400  212       0     0     0>
            , <&key_physical_attrs 100 100  500  224       0     0     0>
            , <&key_physical_attrs 100 100  625  224       0     0     0>
            , <&key_physical_attrs 100 100  925  224       0     0     0>
            , <&key_physical_attrs 100 100 1150  224       0     0     0>
            , <&key_physical_attrs 100 100 1250  212       0     0     0>
            , <&key_physical_attrs 100 100 1350  200       0     0     0>
            , <&key_physical_attrs 100 100 1450  212       0     0     0>
            , <&key_physical_attrs 100 100 1550  237       0     0     0>
            , <&key_physical_attrs 100 100 1650  237       0     0     0>
            , <&key_physical_attrs 100 100  350  312       0     0     0>
            , <&key_physical_attrs 100 100  450  312    1200   450   412>
            , <&key_physical_attrs 100 100  550  312    2400   515   433>
            , <&key_physical_attrs 100 100 1100  312 (-2400)  1230   433>
            , <&key_physical_attrs 100 100 1200  312 (-1200)  1300   412>
            , <&key_physical_attrs 100 100 1300  312       0     0     0>
            ;
    };
};

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne_right_defconfig

```text
#
# Copyright (c) 2024 The ZMK Contributors
# SPDX-License-Identifier: MIT
#


CONFIG_SOC_SERIES_NRF52X=y
CONFIG_SOC_NRF52840_QIAA=y
CONFIG_BOARD_REC_CORNE_RIGHT=y

# Enable 32kHz crystal
CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL=y
CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM=y

# Enable MPU
CONFIG_ARM_MPU=y

# enable pinctrl
CONFIG_PINCTRL=y

# enable GPIO
CONFIG_GPIO=y

# Enable SPI
CONFIG_SPI=y

# Enable writing to flash
CONFIG_USE_DT_CODE_PARTITION=y
CONFIG_BUILD_OUTPUT_UF2=y
CONFIG_MPU_ALLOW_FLASH_WRITE=y
CONFIG_NVS=y
CONFIG_SETTINGS_NVS=y
CONFIG_FLASH=y
CONFIG_FLASH_PAGE_LAYOUT=y
CONFIG_FLASH_MAP=y

CONFIG_ZMK_USB=n
CONFIG_ZMK_BLE=y

#EXT POWER
CONFIG_ZMK_EXT_POWER=y

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne_left_defconfig

```text
#
# Copyright (c) 2024 The ZMK Contributors
# SPDX-License-Identifier: MIT
#

CONFIG_SOC_SERIES_NRF52X=y
CONFIG_SOC_NRF52840_QIAA=y
CONFIG_BOARD_REC_CORNE_LEFT=y

# Enable 32kHz crystal
CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL=y
CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM=y

# Enable MPU
CONFIG_ARM_MPU=y

# enable pinctrl
CONFIG_PINCTRL=y

# enable GPIO
CONFIG_GPIO=y

# Enable SPI
CONFIG_SPI=y

# Enable writing to flash
CONFIG_USE_DT_CODE_PARTITION=y
CONFIG_BUILD_OUTPUT_UF2=y
CONFIG_MPU_ALLOW_FLASH_WRITE=y
CONFIG_NVS=y
CONFIG_SETTINGS_NVS=y
CONFIG_FLASH=y
CONFIG_FLASH_PAGE_LAYOUT=y
CONFIG_FLASH_MAP=y

CONFIG_ZMK_USB=y
CONFIG_ZMK_BLE=y

#EXT POWER
CONFIG_ZMK_EXT_POWER=y

#EC11 enable
CONFIG_EC11=y
CONFIG_EC11_TRIGGER_GLOBAL_THREAD=y

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne.dtsi

```text
/*
*
* Copyright (c) 2024 The ZMK Contributors
* SPDX-License-Identifier: MIT
*
*/

/dts-v1/;
#include <nordic/nrf52840_qiaa.dtsi>
#include <dt-bindings/led/led.h>
#include <dt-bindings/zmk/matrix_transform.h>

#include "rec_corne-layouts.dtsi"

/ {
    model = "rec_corne";
    compatible = "recperipherals,rec_corne";

    chosen {
        zephyr,code-partition = &code_partition;
        zephyr,sram = &sram0;
        zephyr,flash = &flash0;
        zmk,kscan = &kscan0;
        zmk,battery = &vbatt;
        zmk,underglow = &led_strip;
        zmk,physical-layout = &default_layout;
        zmk,backlight = &backlight;
    };

    vbatt: vbatt {
        compatible = "zmk,battery-nrf-vddh";
    };

    EXT_POWER {
        compatible = "zmk,ext-power-generic";
        control-gpios = <&gpio0 13 GPIO_ACTIVE_HIGH>;
        init-delay-ms = <50>;
    };

    left_encoder: encoder_left {
        compatible = "alps,ec11";
        a-gpios = <&gpio1 10 (GPIO_ACTIVE_HIGH | GPIO_PULL_UP)>;
        b-gpios = <&gpio1 14 (GPIO_ACTIVE_HIGH | GPIO_PULL_UP)>;
        steps = <30>;
        status = "disabled";
    };

    sensors {
        compatible = "zmk,keymap-sensors";
        triggers-per-rotation = <15>;
        sensors = <&left_encoder>;
    };

    kscan0: kscan {
        compatible = "zmk,kscan-gpio-matrix";
        wakeup-source;
        diode-direction = "col2row";
        row-gpios
            = <&gpio0 19 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            , <&gpio0 8 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            , <&gpio0 12 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            , <&gpio0 11 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            , <&gpio1 9 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
            ;
        col-gpios
            = <&gpio0 3 GPIO_ACTIVE_HIGH>
            , <&gpio0 28 GPIO_ACTIVE_HIGH>
            , <&gpio0 30 GPIO_ACTIVE_HIGH>
            , <&gpio0 21 GPIO_ACTIVE_HIGH>
            , <&gpio0 23 GPIO_ACTIVE_HIGH>
            , <&gpio0 22 GPIO_ACTIVE_HIGH>
            , <&gpio0 29 GPIO_ACTIVE_HIGH>
            ;
    };

    default_transform: keymap_transform_0 {
        compatible = "zmk,matrix-transform";
        columns = <14>;
        rows = <5>;
                    map = <
            RC(0,0) RC(0,1) RC(0,2) RC(0,3) RC(0,4) RC(0,5)                      RC(0,12)           RC(0,13) RC(0,7) RC(0,8) RC(0,9) RC(0,10) RC(0,11)
            RC(1,0) RC(1,1) RC(1,2) RC(1,3) RC(1,4) RC(1,5)             RC(2,12) RC(4,12) RC(3,12)  RC(1,13) RC(1,7) RC(1,8) RC(1,9) RC(1,10) RC(1,11)
            RC(2,0) RC(2,1) RC(2,2) RC(2,3) RC(2,4) RC(2,5) RC(3,2)              RC(1,12)           RC(2,13) RC(2,7) RC(2,8) RC(2,9) RC(2,10) RC(2,11)
                                    RC(3,3) RC(3,4) RC(3,5)                                         RC(3,13) RC(3,7) RC(3,8)
        >;
    };

    backlight: pwmleds {
        compatible = "pwm-leds";
        pwm_led_0 {
            pwms = <&pwm0 0 PWM_MSEC(1) PWM_POLARITY_NORMAL>;
        };
    };
};

&adc {
    status = "okay";
};

&gpiote {
    status = "okay";
};

&gpio0 {
    status = "okay";
};

&gpio1 {
    status = "okay";
};

zephyr_udc0: &usbd {
    status = "okay";
};

&flash0 {
    /*
     * For more information, see:
     * http://docs.zephyrproject.org/latest/devices/dts/flash_partitions.html
     */
    partitions {
        compatible = "fixed-partitions";
        #address-cells = <1>;
        #size-cells = <1>;

        sd_partition: partition@0 {
            reg = <0x00000000 0x00026000>;
        };

        code_partition: partition@26000 {
            reg = <0x00026000 0x000c6000>;
        };

        /*
         * The flash starting at 0x000ec000 and ending at
         * 0x000f3fff is reserved for use by the application.
         *
         * Storage partition will be used by FCB/LittleFS/NVS
         * if enabled.
         */
        storage_partition: partition@ec000 {
            reg = <0x000ec000 0x00008000>;
        };

        boot_partition: partition@f4000 {
            reg = <0x000f4000 0x0000c000>;
        };
    };
};

&pinctrl {
    spi0_default: spi0_default {
        group1 {
            psels = <NRF_PSEL(SPIM_SCK, 0, 20)>,
                <NRF_PSEL(SPIM_MOSI, 0, 17)>,
                <NRF_PSEL(SPIM_MISO, 0, 25)>;
        };
    };

    spi0_sleep: spi0_sleep {
        group1 {
            psels = <NRF_PSEL(SPIM_SCK, 0, 20)>,
                <NRF_PSEL(SPIM_MOSI, 0, 17)>,
                <NRF_PSEL(SPIM_MISO, 0, 25)>;
            low-power-enable;
        };
    };

    pwm0_default: pwm0_default {
        group1 {
            psels = <NRF_PSEL(PWM_OUT0, 1, 13)>;
        };
    };
    pwm0_sleep: pwm0_sleep {
        group1 {
            psels = <NRF_PSEL(PWM_OUT0, 1, 13)>;
            low-power-enable;
        };
    };

    spi3_default: spi3_default {
        group1 {
            psels = <NRF_PSEL(SPIM_MOSI, 1, 12)>; // WS2812_VEXT_DATA
        };
    };

    spi3_sleep: spi3_sleep {
        group1 {
            psels = <NRF_PSEL(SPIM_MOSI, 1, 12)>;
            low-power-enable;
        };
    };
};

nice_view_spi: &spi0 {
    compatible = "nordic,nrf-spim";
    pinctrl-0 = <&spi0_default>;
    pinctrl-1 = <&spi0_sleep>;
    pinctrl-names = "default", "sleep";
    cs-gpios = <&gpio0 6 GPIO_ACTIVE_HIGH>;
};

&pwm0 {
    status = "okay";
    pinctrl-0 = <&pwm0_default>;
    pinctrl-1 = <&pwm0_sleep>;
    pinctrl-names = "default", "sleep";
};

&spi3 {
    status = "okay";

    compatible = "nordic,nrf-spim";
    pinctrl-0 = <&spi3_default>;
    pinctrl-1 = <&spi3_sleep>;
    pinctrl-names = "default", "sleep";

    led_strip: ws2812@0 {
        compatible = "worldsemi,ws2812-spi";

        /* SPI */
        reg = <0>; /* ignored, but necessary for SPI bindings */
        spi-max-frequency = <4000000>;

        /* WS2812 */
        chain-length = <21>;
        spi-one-frame = <0x70>;
        spi-zero-frame = <0x40>;

        color-mapping = <LED_COLOR_ID_GREEN LED_COLOR_ID_RED LED_COLOR_ID_BLUE>;
    };
};

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/Kconfig.board

```text
#
# Copyright (c) 2024 The ZMK Contributors
# SPDX-License-Identifier: MIT
#

config BOARD_REC_CORNE_LEFT
    bool "rec_corne left"
    depends on SOC_NRF52840_QIAA

config BOARD_REC_CORNE_RIGHT
    bool "rec_corne right"
    depends on SOC_NRF52840_QIAA

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/boards/arm/rec_corne/rec_corne.zmk.yml

```text
file_format: "1"
id: rec_corne
name: Rec Corne
url: https://github.com/segodimor2d2/zmk-config
type: board
arch: arm
features:
  - keys
  - display
  - underglow
  - encoder
outputs:
  - usb
  - ble
siblings:
  - rec_corne_left
  - rec_corne_right

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/index

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/index (latin-1)

```text
DIRC      iAX"l"iAX"l" DsB  ¤  è  è   mâa mÔìíäX6ñ\x+ .github/workflows/build.yml       iAXf	iAXf	 Ds  ¤  è  è   #*"ýfôXò`ey]6¯½ 
.gitignore        iAX(b	æiAX(b	æ Dt  ¤  è  è   ÿÜBèP¶Ä¯ÒF&Ñ³bÜ "boards/arm/rec_corne/Kconfig.board        iAX(b	æiAX(b	æ Dt	  ¤  è  è  ¢ftJQ¯ñ}V¢ ð
øOXÒ &boards/arm/rec_corne/Kconfig.defconfig    iAX'ÉqÓiAX'ÉqÓ Dt  ¤  è  è  =·IgËÍü«6"rÖ§õó}ñK¦  boards/arm/rec_corne/board.cmake  iAX'ÉqÓiAX'ÉqÓ Dt  ¤  è  è  X1f0£ä÷o-A©(ÔîÌ¥­6¯ +boards/arm/rec_corne/rec_corne-layouts.dtsi       iAX(b	æiAX(b	æ Dt  ¤  è  è  S. ùê#ÈHäôå(_Mä,´Ö #boards/arm/rec_corne/rec_corne.dtsi       iAX*ØiAX*Ø Due  ¤  è  è  ÜýxÅªqÙl|÷çNÓc61Â %boards/arm/rec_corne/rec_corne.keymap     iAX(b	æiAX(b	æ Dt
  ¤  è  è   ø°lÇðüW0ÌR<ÆzÖÔz #boards/arm/rec_corne/rec_corne.yaml       iAX(b	æiAX(b	æ Dt  ¤  è  è   øv\ç´XQæs8=Vÿ:7¾x*% &boards/arm/rec_corne/rec_corne.zmk.yml    iAX(b	æiAX(b	æ Duc  ¤  è  è   `x9a¥»ZÓ.[+Äwcý* 'boards/arm/rec_corne/rec_corne_left.dts   iAX(b	æiAX(b	æ Dt
  ¤  è  è  ÜÂ}æþÕ°UëÉÓ6KåêÁÐ -boards/arm/rec_corne/rec_corne_left_defconfig     iAX(b	æiAX(b	æ Dud  ¤  è  è   ¼#C}`s,+DÂ?LùíO (boards/arm/rec_corne/rec_corne_right.dts  iAX(b	æiAX(b	æ Dt  ¤  è  è  ¤Dv#ÂUÝ'N_g;)Jl .boards/arm/rec_corne/rec_corne_right_defconfig    iAX!mÆWiAX!mÆW Ds  ¤  è  è  àÒIèà%þBÌN³,ðÙC½c 
build.yaml        iAX!ÓiAX!Ó Ds$  ¤  è  è  JDÏ¢s1ó9¬¯èÏÙåÔb config/rec_corne.conf     iAX!ÓiAX!Ó Ds"  ¤  è  è  
j-(hj5ud0Ég)@ config/rec_corne.json     iAX!ÓiAX!Ó Ds#  ¤  è  è  ¾oJ
îÜdþÞã`CÃTÄ¬É config/rec_corne.keymap   iAX!ÓiAX!Ó Ds%  ¤  è  è  *ºµfè_sc2gå¶Þ¼ config/west.yml   iAX!ÓiAX!Ó Ds-  ¤  è  è   &[b6WÒ.5ÔÅ)`áÖåâÉæ zephyr/module.yml TREE   ú 20 4
Ù.ËõWrqªÊô¾ÕbÎòÂÕùboards 12 1
T<ýÄi4¢Øõ¸ãàî]arm 12 1
d@t,]Å(*ù§õýkÂBXnrec_corne 12 0
nÒ'X1³Z2ÊGL5þconfig 4 0
oô^'u#F_ª%!J[M	zephyr 1 0
#íïSq#ýf¤¯³°1Ò.github 1 1
áÅÓ}ÁdH5=ðY	þ$workflows 1 0
q«^~T±U²WÑì^¯KfÐsIõÈyM¿rô¬Ôï
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/FETCH_HEAD

```text
aef6aacb7aaf29665d1600d63ea3af6f605f5005		branch 'master' of github.com:segodimor2d2/zmk-config

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/COMMIT_EDITMSG

```text
tst51

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/config

```text
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github.com:segodimor2d2/zmk-config.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[gui]
	wmstate = normal
	geometry = 1916x998+0+22 162 234

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/HEAD

```text
ref: refs/heads/master

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/description

```text
Unnamed repository; edit this file 'description' to name the repository.

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/ORIG_HEAD

```text
aef6aacb7aaf29665d1600d63ea3af6f605f5005

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2a/22fd6617f458f202609465795d18360507afbd

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2a/22fd6617f458f202609465795d18360507afbd (latin-1)

```text
xKÊÉOR06eH*ÍÌIÑçªÊÍÖçÊÍO)ÍI-Öç*ÉÏÏRzå©Å%ú\ 0`
Â
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c9/24cc751e9b9cc1e986ebaa3175b06f9bc27360

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c9/24cc751e9b9cc1e986ebaa3175b06f9bc27360 (latin-1)

```text
xKÊÉOR0·°4gPNIMËÌKUòõð÷ôñôswqusõ	÷õssôQ0420PPÐ×W030àÂ«%Ø9È¬ÅÈT¬ÃÐK93/9§4%UÁ&3¯ ´D¿ (?9µ¸8¿¨X/¥¤8ÓIAUjAFe~JnRf^Jf^z±>DÔM-KÍ+ÑMÎOI-ÖË@ÖXÍDd£ªr³õJPu¢Ëg§V¢®"¿´¤ ´¢üÌ¼Ì¼tü¥'p©åæÅ½Y\Z¤P­ ÐE­ZUfA|Ee|qrbNj¡µB­5Znq2	F'åçä`7F¡KAAA!1995'µ(±$3?O7µ¢ ?/5¯äS;k<8~
ÀJK2sSuKòus+tRSStsÁ*
`jAÉÇØ ¢<%5'±ª¡ b&Ô×W0àx+·ê\X,;§ì¬Á
J2ÓÓStR2óa44³³ÛX\BÀBC¨i8­3*ÀnÔ6.}¨5ð´åB $ÅÀJ¡$Å I$[Xª`« T­Ó¬[X ªñ*H9§dB;/1¬)8#3­Dß9± XÁ'?9[!$±@Á>ehÔMNÍÉG&ÌW SAª ,§] àãêìáéb§£`qvH(>A4$¥æd¤g[) q(÷pNbRj(x\ýB<\=PÃt¿yº{Ä#ó"ØÓÈâ½TZb¥ ePÑNAÎÞ®!{Ñ)ØÇæ+w¡&ãAOR!J¥²w\)öLg+¦g\Q½J°H*JOOÍÕ,EV
H$áÉ|Å©yÅùEºEù%%ÈP*Í*ØóT@V¦+¹;Å;y½"äõÌÝÐrîtT>½][¬ n¸øû	
°³æÂ `V*Â^zÃ¼_×é%JH¦¤e&§"éY´I%
N!ñÁ®>
è%Yvj¥nA~q&¨¦G¡4¤AæpNbejXÖIæh
s¬ialn0Õ[  L¬sºñXÝîPbÝ`BäE¬n@0bÝ`JL"ÍÑvCNqeqQjq*¬=2QReqeq<XñØÂÁ9M"§¼"êÚdª`;ÖÙ
9Iùù%9ù) ¶+<£cø¡"§dËÆàb¸Yfd®`b¤Ù²âÒÒÌüÒ¼P	Ò8ùQã¬.¢É0Blñ¬-Ì/-5ñðØ_Z¢àïä\§á²Ç9Î@§ÝüÒÒâ$|asBh°^5²DSÓ	 ÷Á#;µ27± Éu0D	jUXS¶I/È`ôÖp`¸kPH$Zs9N¹@íX×`gf3PADC(W0X "ÀGºz
àuh Vu ã#a2 N(ÄhOûÃs@BNÁÎ`û{¸@ô9B¨`åÒv±DÀ,L \jÜ*(¨å÷Î>ÞPEyp3bTl´D¦,rb»úzBÔ¸CìäP
ò`SÃ N C@X-/?/Ä@Ç!è²
cü`â ÷øBÄý}}Å]ü¡èìãQîá o0`d£H_n¾ZNBp£3$µUN1Vpõq%µÜ|C¨{À=LG!e7XnY_ZWQJ£g
¿P_'× BY#Ä _øÃ×â8?(m® 3º@Î(óð÷E	#©>Á dê¸jBÔ¸Ç»Àâ¤&À=@<?¿øÐàx'Ggï`Ç`h¼¹F8Ô>NÞ!è9Å50ÔýÌ 6ùBi(m q-	¶Ò "
)(@".>>àxÊ-dv ÐS'òÍ\`M 5Â5Á<pnºq|=ý@1 Rìgq(f(øASÜýÑÒæê) Ö@@¸"
R¯@|Ë²È.GzÄ»xyº¸B;w6ë¹N
"Ð(8"@®CÏ{0ã`záspd ¢ÄÌâÔøâÊÜ¤üKp¤¯¿¡äã¨âèJÙ%EyÅÐñqÖ ehv	GÈO>Î®~.Ðô óICt@ø $ä¨êçâììËIàX
É¾ AÎ~ òyXæ\\}\C\³ÌÕPdBSQ 'AR%B$Í> O±- ÙàÇ h>ögp5Ð¸Dvj	Bµ{cÔÑ¼pÂRrÎ3PåA<9% Å %	T¾¶X\XÐL
v4¼.I8ú£$G¸Y¨á©!ªdc+Ä0eHÆ@(ÎÁ;Òòjv¹ùáÍä(7ChÉê­QÜ 5áEAA
eè¥õ%¨¸ùd²MRØ¡	J<4!h±0Å&!ñïf-Ý u´nqÕ-/C]êrW7PMäwt Æ`³ öÙp !P	Dõ
´ZqV3n0>ÈHàV"3PcµÂ¨Å<$* |0	D!@ ¨ðÀ$H`> ûÚAIÈi	UoªÀøY²H¬F^)Ø G×áÈfE©ÉDå³ Wg¼
ZfCò7¢Xù&b£Ê ó * $ÈgÎñaþ>°X47Ä*P4aNÐ\
á
põíéÙA6zÏ3*à&e(8Çû[pÑ\ÔÆ(»Cs0WÃä!®ñÐ]]  n Âr¢ÊD²p -6-Àa
&ê@ºÀB lo&ùC{ª'CTtÌEð N
À¬8ÜÅ%EBÔ HXhADÐx¢ "EªÃ0­yç fÂZðd 2K
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c9/c4cd134937018968ac5d67219d40a53e0ef8fc

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c9/c4cd134937018968ac5d67219d40a53e0ef8fc (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`°x +¢æ«Ç[Ïh¿Û?E--ª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ Î_Bb
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c9/d5c54e77e12d78eff87b822d1471b01cd337d4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c9/d5c54e77e12d78eff87b822d1471b01cd337d4 (latin-1)

```text
x+)JMU04²`040031QHÎ/ÊKÍ,Î¯JÍÓKÎÏKcXôð÷3iæU¯ãÿ/þü¼wû«ôÉØg§Væ&0\5p}}ìç1¸;¼·L½÷(Tô@§èUææ0t;hÒ¼zæ~µge×~ýÌgÆ  Ì8
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/66/de2eb978290a1f564ca630b1ab1b886594d435

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/66/de2eb978290a1f564ca630b1ab1b886594d435 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó:Ên:^üN¢êà.Së¢B<U©EÊoß²+ÿe&¸dýæ
¦Ï  3©Tû
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/64/3d0f56e0ad44108f6a20bfcecfd86420bd8770

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/64/3d0f56e0ad44108f6a20bfcecfd86420bd8770 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó*x6;]¸õ\J¸3Éawùý}ÞG!
ªR2*ß¾.dWþË<9MpÉúÍ/M ?U
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/64/40742c5dc586282af9a79486f5fd6bc242586e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/64/40742c5dc586282af9a79486f5fd6bc242586e (latin-1)

```text
x+)JMU06c01 ¢Ôäøäü¢¼T¼Kê<9fÈEI
ró1ý 'Y
Æ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/64/53f6ecaa8f0f025d25f1ecf950c0ee161ca2c6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/64/53f6ecaa8f0f025d25f1ecf950c0ee161ca2c6 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó´/²­j±ªmÛwFÚvEòþ)\U©EÊoß²+ÿe&¸dýæ
¦Ï  T
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/21/d650a11f81ba71b9fb9c533eaa1859b6929a67

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/21/d650a11f81ba71b9fb9c533eaa1859b6929a67 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`¨<ûå­£LÀG¥¯	§SoHÓ]ôª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo 
C¤
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/21/6d66fb3644cd0d55d57529151372499dbf79ec

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/21/6d66fb3644cd0d55d57529151372499dbf79ec (latin-1)

```text
x½XmoÛ8¾ÏùÂ
7`YuëÝu»Nb·¹:g;í¶/h­Q¿ÁvºuÃý÷#õbKi^¶[1£L¤REwgrÒ;éýv´¢¢À§þxzLËÛ~0]Á¥aþ^ntz­½*ÞÐµÊWiô{­ÖQ.ãõ7Q¯«n^dKZYQ>_UeôVøJóû¢»ª:(]EéuÙå:ì·CïhZuÙÏoT½½	ï¢mUS_Ûî¢Ò57çoéýíMl]ò,J+À¿±âz­vÜÌÅ Ê¦´ ß÷¹ù¼iòàË}P.Ã^þÛ×äß×h¢\þrYdq¼ÝùÖÍ#árIa°²´C¿äY
ÁG¸${ #zL´Ú©²N~é9¥«NR2É^OÊbúCú âÆá½i¸MþË,s·;g×"¯p9Î"º¾¦E'§EÕ O@×êêd4BªV½SüQXÈ^fIZÄÜ}ùõL*wª0ï¬ÂtIpp(Ï**st?
¦äÝDªî0ÌKbgË[â9mÑ;'¢»³èJ·¹]BäayrÛ´üÀ;[þÛg9À'bJè´TÎÃ¶÷QyJâçÃ1<áSÿÜôÆÞFLþ§oAé¡;>;÷u¢¾êî¢·´:%âåÝ¸ÆðÂôÚEwpQomüîóéÍC'(÷>²'æ#øáåö ºjB9hå½8%
¡¸´çÀ4;¥SdUX©îHLì=?ÚÙÁ¥××Ä=wÌ°k¬pA&(¦5tþÕèá" ìÍ®¦|Í;¼>òX¡:ÍøÒ%¸(Dü&À=zx.éQf"\ÇU å
/°úeïÝéú@'å£îBé
q_ßñá&SA¾Ë¾´±{Ä[°¦fîlBsäsn{,y8"&_¸d
<gÈ ÛÞ¹`gðÁãÃYA¾Åg¡ý4±xXâöÐ¾RÍ<+tÜÎ¹4¶ÿá<©À¦oã¾xæüÁ7(Æ¦Ë1}ùïùÀ¢Ïø1¨×ª0-%¥
FL@uF¼ã25Xl6@ÈøüÑLÒòlp§sOË©ÀF±
E.î´ã¼$cyÆhÒ?@ c10d¤Ïñðû]²*½ÈÕSqöAºNé|20ÝCçÃ7`CÚb+êãûÇ7ýS:¡þ!©ÍgÏ
¯N%ÇWæÛÌãyj(¬D·î
ìap_JJß"µ1#ÛÆ*Po	Ww	WÒ®¤6áB$³`î@|,Cña´À§ÁÇi.ëùàlÔ`Máº3QØÔ3óM©BJ`å&ä"8GÓ:Í%Ä*Ê3+À(âhfÛ:ªÊ
CÚ¬4Z4m
È£PQIò>Ydñ»Âû0ÌìCgz$8ODuh^4#FäÁ1 Þx6;(1Á"ÄÃçØòÍÛ#¨1mµwfæ7|5ÙÜ6
iGc7­îJ|süA"ÑoðÒ/Ç3×¸4[mpîm«)ËÕyT¶%ºùnÿJÀ×4 DWóýPÜ=°W°!eóBÄ8{>ÜRifÿ\cj¶Wg~O>J¿«ï±¦{ó¸¬Ö«(ÖißeQ|Ô6»Ü
¯£ªa«×m­Õ!á°à®`#Ü l7ÕWÒP§½È²*ÎBhÜý¡ ¯PPRGEiZXßØþ'aZ¢©²Ð$Ââf±ú"Å
ÞV»¼/´âk×2RVúìaªñÞT¨w Ç*
î]Ü1VOWËJÝ§¤Êajöwóêeä5x».ºÜzjôeô%¨ü¸àap9³áªo\mºÙD<JÏ<@­ýD¶ö¬Ñw5Jiûuï8òÉÜg-mm÷ÑÛ:Ñ¶¯7N^¥
OS¬iJ>êüNHÙ	=ªÛ(	oÿ¸éävzó8htý?2×*÷|ãÒ0ÀßàÝó	
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/21/a5008ddc06668407dda8d389b62659611367d9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/21/a5008ddc06668407dda8d389b62659611367d9 (latin-1)

```text
xÎAÂ @Q×h¦@Iñî]SJïo¯àö'/ùÜj]¶f:^ÎaÌ"ä8ËL`Í(1O"r&Û¢¾ÔËgh69I ÄäãìQ$ï¢}¼Z×Ï¶wý Zôu+KËkm÷¥Òú¾p«7m3­Å¨Ï ê¨Çß(ÿK5¶aúzCØ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/00/46ed8a25956780e12f9d1351a33132793a1044

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/00/46ed8a25956780e12f9d1351a33132793a1044 (latin-1)

```text
xÎAÂ @Q×h2%1Æ¸w9eÚDÄ´ôþö
nò[­K·à©¯ªV Ë ÈF
ÐÄÓªy$ªo¾¼ê§[Å	 'O¨à,ÀO))OÂÁðÞ_mµÏ¶¯öÁUíuÓ¹ÉRÛ}®¼¼/¹ÕH)Köì¼sæ¨Ç_×ÿ¥é[Çh~0Cq
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/00/d8f2415b6ffc801886ad01c51009d899c9db67

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/00/d8f2415b6ffc801886ad01c51009d899c9db67 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹l×É+|S[PoÊÅönû¾¦Ó jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  ©I?
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/00/f05577fd7258c3255a9e2fe066acb46f223544

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/00/f05577fd7258c3255a9e2fe066acb46f223544 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgøäp¯ïs½ð¢r¾òWöxJL¸QPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú ¼)VÈ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/57/f1263df157be46c7a1d53346201050d5f11db6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/57/f1263df157be46c7a1d53346201050d5f11db6 (latin-1)

```text
x½XYsÛ6î³~&ÑSINì¶I¢lÕ(s¼p(	±9æ5$åÆÉô¿w	Ð\·òÀ.öøÜ]@Z'ù~:ÚÒ¯qFÉùE¸tg`¶8'öÔ\9A8w¯ìðÊtÈèx8$d0 §Ãaï oyS9>!Lc4ìõâlì¶¼³bW2ßÐªÊËêÕ¶®âÀwZÜÜmm¬ãlg×Õë°·AïhV|K«W7ªÞÞDwñcUSßÓÛÁ-½ïèv%ò]
(*ò8«£kª¼^£@¯¦w!!Lâª¦-ÉÂcjwüFÞ÷¿ÇEøí>¬6QBÇdôáùó¨6Ï0QmÊ<I7C~ôàãh³¡à#ªã<3è·"Ï`sºd|ñ!­ãun¤Ñ7£*(ÝiÅ$C)éñÒ·4îH+Àmò7³ÌÃJï}NNÐÉ9Î2¾¾¦¥QÐ2Î§ ¾ÂQ,FHõvø_
Ù<-`Ö	p_@þ¼ÊFÆ6Ê6ôâølãªÀð³(eJþMüµXQQ'ßÜ *Èä½#ñ|í®Û%DËÛ8ö4ýóÙ4øð28¹ôÅ^¡-6B64Ãê)ßPb>oE3(Y£Ìë¨Vc>ákÐÑõîxgãpìÍv5!à7Cü"è:ý£:$¬ÍMÜ¾á¬AFØ JhºP
yÀn<äjB¯vIBvaÿhø¨ßÍºË¶|m\úz/¶oáN/ùð6SA¾Ç´±Ä&GØ±Z>*æ>Ë$VÜöLòpD¾+'Ü²ÆþÒbÿ|
`gòÁçÃYAþ3ÎC{µ±v@,qÇr.T»îÍÎÎsimÿÎmK¶|g8ñí9Ä3{ØÇl ó>ñí>ã_qÆ¸ñUQVIJ[ê£Ä\8sçsØ2þ â§¾A2ÑÙbåk9#Ø"é°Ëáp"ý¤&o¿4-1ô3´óïMs2âxØgà=NC¥7¹f)Éÿ eíÒ'ëc±mï`}/Ðï¸½?sx_d¸3_%ÕqõÜôLÂuiWÊ¦»«°I²ÉT4Û³Tx0"Ð7>^ÒØÃàJJ7?ikMBSíÒ¿¬~í:vR
ky6¢
gµ<]dÆ²?åk1P6¸ê& nä±ÃÓô<Wt<µp½AÆêB N`°OdµØÑH­?¡&	Ôyú¸·@M\ÇÑvuUºýÒ.\[Y´
Çz)£¸¢au®óäÅÿ<»Îs
F¢+F&±wG~;Å@T
ð.¡ï°jB9¶,¾KGÎLhQðàº³T·9ü,_CËTwä«âûD¬	s@TD%ÎxEq´x§{¦uaæ|æWv[ðë¸« \ùpVô%5v ÿö3¸Â«flC´ÈÑïcua_®à>(¡ì£ýÉgØåÜôà ÄuVEµä3gbk¹×úÔgS3"¢ç$èÎÃmb4j öÀ×ìoÝ¦¦ÙÁÄ¯êÝ6ÎÃ]àmÌÚ>qÊ[>ÅùÐ¥HÓkÏ«¯\}S»6	
æCöqFÀIÊÃâ¬bóÒ?8cÔ$0¬r¹á6Çöó¹¤Þr×Ï1TàÂ¥MeØS¼Ì­ó¼Nò~· Ñ^ÙØt.noð81,=ø7îé¶
muü0¨ê¾
KZÑdÚHt
_LQ¹=Qaìñ«©.¢ÙPÝ·ËÃòà¨p\ï,JsåÛÐ/lóBKwÝF)¾ô Û85ùBö¡!ÝS%Ý<ZúOÎ÷nåÈ¡¢ºÁáZáë´7Ñ-<Ew¥u¾Ð$¡kFÌlÁà£ÍsDLõt£	á|ð.,wå_ÞÐ¤6îGÝìÞôýCJâXðlsúÏ÷ºõ¦Ït4(]o¥[Ø!ÝÄ×è$ZÓÿeòlK9mÚÿp`öSÙW
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/57/fd52f85cf79115d5d2b5960b150dfe840a07f9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/57/fd52f85cf79115d5d2b5960b150dfe840a07f9 (latin-1)

```text
xKÊÉOR0731bPNIMËÌKUòõð÷ôñôswqusõ	÷õssôQ0420PPÐ×W030àÂ«%Ø9È¬ÅÈT¬ÃÐK93/9§4%UÁ&3¯ ´D¿ (?9µ¸8¿¨X/¥¤8ÓIAUjAFe~JnRf^Jf^z±>DÔM-KÍ+ÑMÎOI-ÖË@ÖXÍDd£ªr³õJPu¢Ëg§V¢®"¿´¤ ´¢üÌ¼Ì¼tü¥'p©åæÅ½Y\Z¤P­ ÐE­ZUfA|Ee|qrbNj¡µB­5Znq2	F'åçä`7F¡KAAA!1995'µ(±$3?O7µ¢ ?/5¯ä  a VZª[¯X¡[\¢[Rij``g
V
NÆå)©9P%Pu`J__Áâ­Ü2¨{ðZv>e¦§§é¤eæÃihfg
¶Kj<1Aù ¤X)¤ 	ósK2rRlªr³u`uKtSóS¬ÁvpJfqÈûy¹`MÁi%úÎÅ
>ùÉÙ
!
.Xô)CsnrjN8t
ìPM* Ë©e(ø¸ºÄ{xºØé(ØD4ä$.H,JÍ+ÉH-Î,¶R@âPîáÄ¤ÔPð8¹úx¸{+¡ºt¿yº{Ä#ó"ØÓÈâ½TZb¥ ePÑNAÎÞ®!{Ñ)ØÇæ+w¡&ãAOR!J¥²w\)öLg+¦g\Q½J°H*JOOÍõEV
H$áÉ|Å©yÅùEºEù%%ÈP*Í*ØóT@V¦+¹;Å;y½"äõÌÝÐîtT>½][¬ ®]üÃýÀØYsÁK&Pi)³
Ae6Xæ¥äüÜ¤üb¼N(QB20%µ,39ÕI(vQ6©DÁ)$>ØÕG½$ËN­Ô-È/ÎU=àh01Q0´4ÈÎI¬L-Ë#ÉÀ
Rqqn0D2¤ÐëcâÜn<V7 ;X7çäÀÄèF¬Ls	Z0cCs4EÝS\Y\ZZÏÅÅñ`EhÆcsrDNyEÔµÉTÁw¬#²ròóKròS@IpE'£æB¸*"<l:-+¢¶eFæ
&¦H.B¶¬¸´¤4%3¿4/Ô`´VAþa¿ÕÅC"R->5²ù¥% &òKKüCCâ|ë4\ö"ÇHá´_ZRZ/áÂìDW,ÑátÈ}°ÀÈN­ÌM,@rfQZ¤%æÄm@Ò2½5îÖÜ@S.P;Ö5Ø¤ÄTP QáÊ$ð ¾¸«UÈøH
1Ú&¢Aâþ0ÄSp3ØÅ>Án!}*B¹4]ìp ·

j¹ Æ½³7TBÜLãíi KçbÁ®¾5®ÁP;ù@¢ T<ØÔ0ÈVËËÏK1Ð1Â fº¬Ä?8È=¾1g__Gdqh ºûx@Ô{8(åLçãèÒ¯`¤  S¢`¢àèI-`U¤ c\ýB\AI-7_ÁêpÏÓQHÙ
@æä§ÅçæbÒèYÃ/Ô×É5PÖqÇÈ×>¡Á°Àµ8ÎÏJ+(à.³ Ê<ü}QÂdªO°(Æ:#®uîñ.°ø©	pf&ÏÏß/>48ÞÉÑÙ;ØÇ1o®Îàäu¡wzNq
u¦A?3M~¦PÚJ@\D­4HC

8rË ä&ôÔàüàA3XÈÄ GpM0¡îGd_O?PûCäJÙ
~ÐÔâw?Ft´¹úAÊ5#.Ô!ç+är,²Ë¢Þñ.a.®cÁÅÀú`nÓ 4Ê Î_`%ëÐóÌ8^xâ¨(1³85¾¸27)?@åéëäïC(ù8j8:RvIQb^1$t|5@$]  bBÄÁò³«4=À<¡AÒ>9jú¹¸;ûÁr8 FC²/Ha@³¨üB§9W×Wäl£  s5ÙEbÁBÀI T@³(åÂS,DH68Ä1=à¢EA
4.ZPíäu4$¯ °¤Á³àTyAG	Å`1HI¯#¤m E 4S
¯Ë@¾Á(Én*á@xªF¡*ÅÃÙä
q L1&spä´<¢]n~xs¤b9ÊÍZ²ºAk7hâF¸FQPPC:Ai@A}	4äê	 XLB¢ÕÍZ´ºA«7háª2 >Zê W7PäÂwt 6Ü¨¥ ÃLæ°ª¡´RpñA.Ö2£!jõ Q'H%bA«R+XÐjBIM $X»!.y"I	3cÐê ì.GàHÖE©ÉD¥ë Wg¼	ZFBò¢ù
&b£Ê ó * $ÈÎñaþ>°X49Æ|;yP!x°hBq&ÌepÔðôÀUgÞS@:ØQ (] àïní!ÌEm,!B0WÃä!®ñÐ]]  nÂò ¢B²p $6æL(
s>$ù@¤&Ò
èxÇ  hÏâd
<È\êd¨ Ô2pË%EBÔ HXhADÐxÐ,#L¢êÆLgyç fµàÙ, J¶N¿
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/db/791a1894a9c4954b377df77f2896aef2924147

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/db/791a1894a9c4954b377df77f2896aef2924147 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`èãwË»u¥uÝ¤Ý»æ2îíäËû²ª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo ãTBÖ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/db/aba39dffa5cdf8a0272d3f990c470937a51d2e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/db/aba39dffa5cdf8a0272d3f990c470937a51d2e (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Óê~Þª¸~kc&SÄúÝ^þ2åìU©EÊoß²+ÿe&¸dýæ
¦Ï  ÇT 
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/87/e28a7cad08c7a384ac8d4aa44194371de673e0

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/87/e28a7cad08c7a384ac8d4aa44194371de673e0 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`8Ç)âwtoùöü¿ÒW7¥ÿe­ª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ Û°B²
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/87/6f4a0d8aeedc641dfedee36043c3549ac4acc9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/87/6f4a0d8aeedc641dfedee36043c3549ac4acc9 (latin-1)

```text
x½YëoÛ6ßgÿDP/¶ã¤[»ðCJ¼È²+Ééº/l³Y2$9kZìßÝ(Ù±Ýf!y¼Çïw|¨ó(³WíîOÏücsö÷øÚNF¶7²/ý¡aöfç'7Ó³X»Ój1vzÊ.Z­Æ^wàX$Ò9g$Ñn5ÏÃxmýÆëM~ºNÏ²$Í~YæYøVcøÌ×wéé2oÎÃxÆ·Ù©¡¿MþÀã¼¹H<ûåNó»à!Ü¥QWõyu:Ï«õù{þXÓ]çH69xqiqø÷KoçÈÐ8Y­|rÑÂ,ç1OÙ&|.£Åþ`¿|×þ§G?[0uXûíöïT-¾BE¶H(Ú­}iÀâ±`±à`#ÈÃ$nòOë$à#4I?È±æá7ó¤¹
>5³5çËæ*CÎóVKñbúAú àGÁ£d)Nñ4·VÏ^#ix{ËÓæ§a¢@¶/Þ¾i ­Si¨H&9FHù²õÿh$$/Õ48¸ûòë¥næÁº¹âöl#;þa¶F÷ã`EBî]ø1?ëYÉâyÁ
wÈ=ÑU(ººfU2'÷kf¦ç»W#Ó{û2(ÞÔÕÐi±uÂòÞñ,Ì^ëïw8
æ<ÂðL{a{W;rk1ùzßÑåçkä´N/c¤»;OÅ=Ï_3ÙùnöÞàÚð¾ÛÅ¾k])¯»Ró+páÿÁîßíÌt45¶1ª®`.ªE­Ñç1nõék¦
4Ïö_Æc8_i¹^ÏåÄÞZªÔÞÜ2ç²ï÷¹P!
¥
·ÜXèÕñÿFgòpòÞ&ðe6äEùãn%öì6îÙDW.AçI¶º`,).ùC¸àmM
W·ÚyÎú°ASp7×IâÑC[]u»Z® ì¡<¥É3mFaF¡s8Ô
ì(¼áìÛ!¡sBçÛ!t rgÚ¯¾Ãùqê½µíoÁeYÊ3ïC<>1Znu~Õô¼K¬¥sÖÕS·Í$ 6É}^\âËnµõÐ¥¥c¬¹t®!Òe|³MáèK¥4+HF|¾`Ô=å¾ÕèáV·¸=Mfß·ôcë);ízÞ¯ÀÀ&aæöpµó[éIè
Û
® e ¶YÁò¬²Û6QîM×/¼ïÞ÷¤qRýô5màUÕp8Ýw¢y/Dî§t<ÙâóÑkv6ÝÉÚ>¨Ìê¢aôê=Hê»Ó!¶Ü+° ­'W4CÒtS. ÿ)âý¸VÀm
¬kÉTÎÓMP¨¹RPõ¦h
éö°ãcp{Zxà90¤¿Eóh(òD¿~a)W èm	oúì£±´5!\âôáDÑû¯àqèSÉ%A-Y=âÀD9ë2wÚl©p?@5gÞ,¦Ú*amÛ ´rSÕÆ¢äúñfµµK×KÃûs¨4¼­ÇI¹Üß8ûWÙ¾¶dÙå5]MÆQ,ÝôÂ÷ñ³P7ïBjýÆ²ÈøÄög®ßkõ\¹nÆ_J?°Mjû×^½Rw3øÀDÓöláÓéìÊ¾=Õ~4
dlÅF½¡eÑ:©b¥¢õì,ÇèC9ÅEÖP£Ó{ñüÇÝw¿,2º8k	.Ç2[ìÿÖr aýA¢%rAE>½®p\ne8Ò2×S8º
ai<²gîÓeDr
cÑ%Õ¹·ESõÚSê`±ÁUà<Q@ifÜÏá8\ÜãþÄ:TAVïfvðÂ èXX2ßE] +´@ØèË|P§wU$ÐÌ;8J3­09µfò:÷/í3`ázÙ ]¡­ÄPÔ|ÁX+²Ë§ ü²| Wfléëõ ¸Hôª(p!ÂNÔGbÇX\:½	ZÔJi¬4Üå¨èê<éF	P¿«fäN¢Ø¯!U"´¡°,j]e8ÑOUPWMí ÌÄtðA1@Å¬©Ýcªãc|ÔµË´÷VðAm¹³òD1åb>Q`y*_GFÊ3­-·²§TÛD¢4$] [«)S&jM¤Iaâ¡!ô&pÓ	w´BEÙÛK$¶*ByòP0ÕËXV´àPWÔwªÇàÅ(C{òhÀ®8°§.±J6éFõVçùÊ¾Rîy.8H*@Úôùâ¨¼vÁÞÄÅªJKµèÞß?ÒG'þÍÄR ÄÿÚäºc±:å¼¸r(nµL
¬hñ=0ï::õ6(Rb+§

z<óè¶WPB­.O
µï¼(j@9]U
¡ÁfËÀáM²êÿ»Ã]Ü?a¥ÅµÄq&òeø7¤ð¡]ÉHÝ<ö· ×F[¯KWÇUéºn5®ÀÙQ ð¼ÿÛøH-
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/87/ba59c8cc282ac08e91a7826e797e77ad5e6930

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/87/ba59c8cc282ac08e91a7826e797e77ad5e6930 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓòMÏ9µb¦PÒûÇg>W.õRQ¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô ]¨V4
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ca/ce0eb336a0056f4cba5eab0b6fc0a1f0d2ab06

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ca/ce0eb336a0056f4cba5eab0b6fc0a1f0d2ab06 (latin-1)

```text
xÎAÂ @Q×hÂã	Ü»2ÓÚDÄ´ôþö
nò_Z­K·èÂ©¯ªV³
±Ã ä5p LLÊ:ºüÑ|yÕO·"Z2ÅÉ%(4B"%AÍÀeÂ`xï¯¶ÚgÛWûàªöºéÜd©í>W^ÞÒêÍº!Ä#Ù3x sÔã¯ëÿÒô­d~¤zBõ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ca/b4901ddab86acf376f64d4307ee56f246a842c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ca/b4901ddab86acf376f64d4307ee56f246a842c (latin-1)

```text
xÎÁ
Â0@QÎ"»vZ	!&àÎÑMRÔ¦ûÓ¸~éK/ÕRæ1t§¶yÌ1æ)"÷YÃl ¢iì$#wûêjæ³ª b
,D{´§úPÆÈÓ½½êêu_ýCùëfsRïsÑå}IµÜ|L£ø3;êáköÿéÚÖç¶AK
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4a/30761f7c264a9a8ce357f36c891405aa7b34e5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4a/30761f7c264a9a8ce357f36c891405aa7b34e5 (latin-1)

```text
xR]OÛ@ìs~Å
JTv¨ªÄí¶éî\h_VNrI,_tv@ù÷ÝK
¨é^nonvgf'ë:îÓÁ)z½5õbÙÃùôÎð;È¥ßéÚÞÔM¯MGHQ.zªÚN]Æ3Õöõ¼Væ¤±Xª^C×(µjÞ+ºU°Ôçî×kÇ×qUw1yvH}0%EÂX2NY^ÊÛ«kÂ9ÎØq»}­Ýá;D!y\Pù>Ùñ0Éï?xÂ<£ïG¬v 7ÿÑ+eùÝÝnÎØ¢dìèÜkç¿ó #ª=ìj@®íT¯Vä&ôäû\7~®Û45G~ª¶4
²1Ï9£x9(í»A9é½V¦ê-O·ízµê`Y=)XMdt{®û%Ì7MÝf½Ö¦§Î¦ºí6+
îQm§z¦ºo
XÏ_±ÐTÕ¨hNHÄ£ ½ óxÁL·g=<kó88=JÌª¡«(SÆ²JáL ï8Ø)cë¾ØqpÂþFboHëÄBÙû^2âÌíIõ¦SïlÞEg2ÎB:Ê÷q]Ñ'ó_§]=Q¤y.#ÏdßáóÄëvjTEÚ $&º2³3!»LÕ.Ô¡/1	GùÅ=Ç")Þ¼S2áùyÎÀTÜÞH¬ï@%Ìl;Æù,ò~Æ9udYæù	£~ ~GWä
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4a/3645dcb7af94fd6e9c356aa8ae19526ef9bc64

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4a/3645dcb7af94fd6e9c356aa8ae19526ef9bc64 (latin-1)

```text
xÎAÂ @Q×hÊ41Æ¸w9ÚDÄ´ôþö
nò/­Ö¥[ïðÔWUK£ à@2B³@â$Ò=	 ×2ùòªnÐ»5OJ 0÷TDsL13¼÷W[í³í«}pU{Ýtny©í>W^Þiõf]1öÀõøëú¿4}ëàÌCn
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/83/2500965e3c37cf47fc7d9ead87c77bdaf8b7be

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/83/2500965e3c37cf47fc7d9ead87c77bdaf8b7be (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Óßã:÷¦;°éªÄ±Ìg¯+ 
ªR2*ß¾.dWþË<9MpÉúÍ/M TUõ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/9a/a4b6e6b73f92ca56a4e9ea4bd5bdfbe9029c45

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/9a/a4b6e6b73f92ca56a4e9ea4bd5bdfbe9029c45 (latin-1)

```text
x½XYsHÞgý©¸JOQ$Û¹6É¦
!dk
d'y¡4±)s oìÔþ÷í¬+Gí<hz>¾é-¢tA^½yûæ£ý&|±.|{6zé?2ÆÚÜô|kveøWIOBú}òz0èìTquÇd*'¯Ó8t:Ga²Ö+J>I¶.ûY.iQ¤yñbUáGEàf·yUöa²
¢ÏuØoÞÓ¤ì-Ó-^ÜªzzÜ,ª¦ã»þ¢lj¶ßÑí¶Dº.!=BY&%àßí,¿Y @§Ç÷>ÑÂ¢¤	ÍÉwÂc®wüE>tÃÌÿöàË ¡rüñ=ù÷=(?`¢Xæim6C¾wàðH°\Rðaôè·,M`óºd2bÀDË0¦½2íÅÁ·^QºêÅ¤,¦Ï)¤*®h<ZÛä¿Ì2+¾x¶9yNö"æ8óðææ½æaZ|
êè«/UÉ$Ö©\
ÞáÂBö23Ø ED!Üg_Ï¥r¯²Þ*Hôâ8VaaøI3%÷6üZöõ +.ïdd´AïHTDN%b»+Ãæv	%Ãòä.#¦1ö|÷|2ö>>Ì®Ù®Ø+T ÅÄfÈF&X]ù;¢,wÄ[ÐJº§ePª1;á7 £ëõ
qÎþÐ0ì
ÖHgøE.WÐëÿ=Ô!a×àhv=eà+ÎÜä2ÂÆQÊ¤qpÅ¼QøéÆsH®Ê ÜåÁ:*}È.¼?*>ê·³îòÚp¼Ï åPO¡ùb¸:>CòO×|2
òÎð¤m3^qu¹½Q}Op1ç'HpH
][gPM÷| §ñÉåÓé#ÌgÜ`ý[CÃ¡MÝ¼"õsgrv.K}´ü7·,câc$\Ã2¦áp¬ºç 2¿ðéØn3þg+/e$\Õs
Ó­æW:©ø¸°«eÍDLc×°Ðd:w¹QDELÍd{B"Ý¨$/kk:ÏôÁ´rÊ÷	LÆ)9æ®pÕ £Zo^1ìrìÂK¿¢K êþÕÌ[©WÑ¬<ëü	Òhî'ëxoMçÖÐpv8¸n{ÆsyÃã¾óè}ë¨Ïz[	µDúëæ
djïÈ0;ódFð/hxÓCùékéÍ5ØCªº ¤¼0xf×1úz%k²Ý]$ÖS±6ÂoO*h;u[ÍqfâTEÑG}f¸¨¹'¹½àEÑÈu¬fÄ¯æ¿2Íd
¥]|ËQÆH_³	fÕBË° ~ñ/ÒhOÃr?[ÃyP¥A@Æ'ÝÀüx5¸¨øÀ`Ï5/o$G¦	ý¶£O+1!Ýê$¨O²) uÍ1ðVR³lÜTFº½IÓÖDÇt/Ñòx÷Ã¢$CÏ×°V+bÉbNMZÃM0UÊÊjBç{z·>Çd\ÎáÃC^H¤#9fÙ*ÎíÊ¨«
¾ÈlîùszWW®&ôn¥Jb·µø½(Óº	[Ô¯"æÓ!6×61ßÁ¶ÎI¤ìò&æÈØZpmüjßè0s¬.²M·Áo+½¯ÉAïãdgÉåz¦þ:ðÓmèîVlÌîW¸GãSFOVÆÇß3êÓßQzcÙUè¬0	Í
¶ÑÇÊ=ÇÇUõ4ÔbT*¼`ï¨E°UGph9.Ò´Ò ¾Å^¼Û³PmþÁoÃ7>ÑÉÓÂÏiAKQr­áPáWåuß{_ñê·Uhmscø`f¦iÎt|µF ¶6w
ø,4´Õ¶9Vùò¼fÞí ó·oo¶¾óp"B	°=77G>Ý¸í?¶nKWgÂT9*åª¹UYj@¢­TÚ1?i?õZ¹hKÈ¾ÍUäX?¶nK·wTnK{Vô6m§kE=Ü¼ÞöQ° þcæºÒ_êÿ£úÄp
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/9a/691e5b5b82c4fdbb4502ccdcfa6930bc94c176

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/9a/691e5b5b82c4fdbb4502ccdcfa6930bc94c176 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹mwK¯KºrÒRÿMbÓÌ©çwîª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ 7A«
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/a66077eb594479a0b4bdef267b53d8a38bb205

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/a66077eb594479a0b4bdef267b53d8a38bb205 (latin-1)

```text
xÕXYsÛ¶î³FñÄÒ\d7êfêÚJª©li,'éí"!	5E2 dYIï¿ç  	Êã¤}¹ô8Ëw6lÓ¬ãW'/ð^ìÁ9/Ê
gó$Ïúá¹YPòçåï0KÎ¦+YpñÅî%4Ô¤4lÆ(ïËÁ
òöö¼T
÷.ð~Ú{Æò$[¥æOYâå|vùÑGÇ@Ç^[D©t§,OY>^FSü;\ì"ø´¼õ1@»$s1+ø©yº¡Y,QRðºY¼)VR(­@I>ïxEJ3ò3iSw~RI±,cÉ¦µ(JÊY¹ <ÎÓRLkQù¨ã-î$ Ê-c.dE÷ñKTÑ:-Áã%aë?¡q8¬:öøòÖ¹I¬T¨ÎÖà4ò
òÞaß
¬«<¥|kD¼\¶iÀÁ83^EÊÎâU&#íç6ù4Nn3_@X¿hÿ¯)$=¢Ëwí@ÔÞdrïÒtabUÉéÿqGú×
¡÷Ò-5åîæÐÄHAï'òEæÎKV0ít{>	ºäíx0ÎÎoïûÑo·¿½nìd9.äR¼qëØ7£²ÎdDs:éDøu'Ô8+!É °àÅ[Àøäù62ò·;~7FïÆÒéCGß$@HZ*»è6!c¹ÂÏj&5 +û¡(Ì";ÅàÞÒÍ2.]CjY
98S.\(? K×ÐiplV©À ÙîÞ.ÑUòYU­¼]ï
Öò«gÒ:¾¥+ÀZ¬xBDHÖyÊ8MÆNRd!/Ö/¼é(ÔºQ¿k¯¾Ñ«×-n§ÎÔÂÿ;ø~î|ÕãÁËúôå»ÃáÉÃJßAÚõLO'ý¬áÓ¥¾ú
©öeU¯Õ^¯¯P0ª<7ò­f]2n-À* Öj«Y$8²*
CÏÖ7,êÙË¤ëóç¾ãÕ¦
MÛ5íi*QíV3WóèOFÀi_6¨5Û°+p4¬ÀÑ°GK

+p¶`êÐ	4ñQÕéª	ò*VàhX£a°BT(#B+4°B+DX ®ã­Gch}Õ5¬ÐÑ°B+4°@¡-X-ñÖR¯¥v
¬î¶·,ò]Åo¼Õ5°º «ÕÖÚPoOz¤\/aÛ½`Á¸VZÃ'XÑÓV] $ø®Òz:>ñÉøÃet9éC$T<]nþ]®/ÏVòC5¢ h°.÷ã41%×¬·Åm¼j·*~¤ªÛÝBÇdèm´J¿GöWb>Fmv¨ÎhyAÞößãö]-éö*eÏóÒ"ZgÉ¿`a=,øÜËbIôRzçOí-µ8\Èef¤yª­·Û»ã:c÷4mvêv|ÅiÊ©nB³LÏ^V¬	ö¶´n0W¤
,H­êðK	åøÇé'8ÿÞ7QÝðGxµTa°+ö1Â®¸ß+j[W
GT!C/ÔÑP> {à4ÏI,5J Jç)loñ 5JàTfÝÙlF Kåw4%|²L7DÂ±3.Ë¸y:´¸­.Àq4ÓÆdÍ²L)ÊIQÐó_½!2£o&ÞÕûÍÍf OíPmù:=ÐD¡¥9^ÚÄÏ<`°]ªÇuøNvÇlZòË
fGèÃÝ
ô¸Vîn'â¯æÎßgUiÌÌÞ#Âz³Íy±*«ÒGYøê\¿º~'ýáóÉxpMÎwïÀ}ÁÁk§åd:m_&E¼|
õ`2Ò²í¢«ÜW6ÒÒØ£úÿ7Ö )pÌ6çPÚ@c¤iÍ¸n4Ñ³ß¾Ý^\|Fïn tüv¿ìaT®Ô7ýU!ªy² àÝÆ	öÛ·cR)¬³½çð$£÷xpqvsVçõÃÜëFMîþ¿£VùTß`=ä°Fw®#p¬Éð¿DÚW(ú*ÎÁÛ YvtÆ©ÂõÕ+?é¥"eýÖp/).3ÑtÒQtFO"¶.|òãÃCÙË`Ê>Ø§ o*L´][¨4è&·¾EgvwQÑú.×©¼§v±Iª­áÇÐ*0¸ÿTwv=²Í­=FêºàY*è9sBU§ W¾÷ºèp|ªµËåasÈ':nINa&b¸YÄùªû\[ h»{wÆéÇÜá=ä)®yz-«t]6s²Yî|.ñîó4wJ.àªw÷¥xc¨öòã(/l#$¨uÂ©´à®ÔRÛ°aÿ":
G×Ñà"z{Ýï_Ö§ëþEûÃ¯Ãw}	R~ÿA°
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/d92ecbf5577271aacaf4be9fd562cef2c2d5f9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/d92ecbf5577271aacaf4be9fd562cef2c2d5f9 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgÈÿ§^ª<­Ý-~Uª¢s´´/'DAUjAFeòÛ÷ÁìÊ'§	.Y¿yá¥é3 "S
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/2d28686a3582750504648e30c967299840999b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/2d28686a3582750504648e30c967299840999b (latin-1)

```text
xWÁÚ0í¯°rf#&	ÛÝ½né©j¥Uoí
`Z¤l Vü{gØ½60¶ß<gæ=;ÞÔíFäE^|z	ì·ÉH:Y­«¶kd2§Î¦|Ôý"+ñl»ëòÜGó¶rWëa=~ájEWHø5õñËhOd1IÕÖØRÍÔÀui8Í?äÆÎÕ8jÇâ2£ö,Ä3µ	GKá
£v,ßá¨=â²"Ä÷¨qiÆqØ]©rÕ[ÞÊ³8@<0yHy¼Îä2æL!7¸<É3·HÃ|&Ï°d¸ þà^çîop·§,~ xð	áL!0Ô&AÄàL!§¾Ä0>SÄ1Á³ðg
8-ø>SÄi¡Aê<ã{Ðx°'vÁOr¯ånpÅsè*ÞîÐÉ¾ÅÚÔh£w}S¼nÿçop}NCFä	!#êâ3dHNCÆð0CFèÜiH»5$eãCf>C2iæúÁB0Cf>C2>!Ý'Ã¹Ãg
ÁùÉøÌÎxoO8nH¤øÝdn±x.C^Ç´mOM(Ó@Ïå4PD}
ÕÍi >S7f ]:
¤q·"5N²Â´Gvî4ÃYaÚ#póQï¤£·.UNYovt&5Âö1J¼qóÜyÚg´bÃeÓA+`¼³¸]S¼hFrÎ´-©DÅ2²¬
¥ÙØ¬Zã3ÒR5£¸L²yU¿ôO½Ô'½lú¶£[Æx7ï¸tr	ÓkÙTíVvêº¢6}eÖê4×¼åÈfØïöÀî9Uûv(ý¦VW²>ôsYX
ýÂ|[}ý¹^}þñeõbeS"®SCwæ¡^gÙÇ.ÙW
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/f5994db4aefa0e20a7c43d0535e03e63251314

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/f5994db4aefa0e20a7c43d0535e03e63251314 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Óïy¹údÉñÚ²¤êWñæÿ(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} Q¬
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/7d038241c39637fa9c105d4cb63a906c9a88b6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/7d038241c39637fa9c105d4cb63a906c9a88b6 (latin-1)

```text
xK
1]ç}¥ó8W.Ý»ìîtÆc$Æû;W·)

´Z×ÎÍ»ÑU!&¥9aRë&ñêµdÉqbÌ8côâó¦®¯RX(	ÉìxN6úPJÔÀRÒÑÐw<Z{ûv¸QU8}tiy­í²TZiõö8¥ù#ìÑ#Ínÿþ_ëhyÛ¤õ®Ëº¡ùÄJz
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/adceeebcd34d1342b05ed346d1efd189a9faf2

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/adceeebcd34d1342b05ed346d1efd189a9faf2 (latin-1)

```text
x½YëOÛH¿Ïù+VEB­Ô4´ÐCrr8lÚûb9É,Û²®´ºÿýföa¯g):ewggg~3;³;6S?ÓV«ùÇÁ~óJþ\;ãQh÷NWïiÃv£[Ý¹ÕÒhÖëÔjä¤^¯l]buL-i¶¢Q¯T¼`æ/ç|öhÖ¢8Ñ$	ãäÃ<M¼áãÚ<­N½`î÷I¯a¿UúD´:ç4ùð ®Ò÷É['QõcñX¦ÅåùGú\]æ)X±)
½ üÛÅ÷Sd¨.O3Ññ½$¥ÉOÂmÎ½Eþ$xóýÙIf®LMÒ¸8'ÿ£dö"Yúþz1äg6¸³nêA~Â P%{ "ê5õ´Õû½DÎ«9ëuÉásáçÔwKÎÀeò_&µxx¶*Ùã½û{W#{¡Ù8¹8¯ ®P#¤t^?ÃäY¸ÀAS¹o ¾ÞËÅÕÔªs7Ñ7çL7²ã3÷ÍÜ[d=xßÒZÇb³Gb»é®Yw 2¢
»â3ïë
eÊ°8y¡÷lÇºê÷ì÷9@éhcKYFsPDnÛû@/9S¿o°ïN©îk¦>´¯t«o|òBÛÒB³ye;êDî#ÕÜiìÎizFDçÍlZçZ·ÛD³}m¡½÷Çú»
FPn}eKôW°ÃìÈíA#6`üÉãÐ¡ïñQI[.¡Ü)Õ8LÝTMº1±5
¹ª÷Ä¼l;m³Ï°H]aÄ-Ózqü£°{¸;º2ðe2äYÊã	ÅÏéÓ.M?OÃd+tÎá	Ó'oFÊ*ÜÝk§)iÃ¡¤DjD|àâ­FaâáuÃ·iµXA87iÌ&98æ~à"Ë°ãâG/p´æ.ÍChíAuåZ/4N_áx?å^ÙÆÉK0øÉsÓ¦ÛP ÃvmE«E&5îâ×ÕtLZjpªüi¦~èÂ!¹ÍªKA¼v{Á¬ª²8ó:ÊKÇ
"UY²Ls/\>ÖA?©Y8DÆçpFEØ&óÔ£FU<Vn[4Ml§m¨×Ö&=rï>¯@Á2îabµ÷0µù©Ä´!é¶²3wÄê5ËYÞNûoîÒO¦AYËEîÍnÚ_a5NÊGÝÓ
§ºÕÁ9ìÞðæ7:[tl)cc¯T½ÁNÆkPÚW9	Ý4l>.ImkÜa
ëªX¦ñÆâMIAz.AýÉb¡\à6:Æµ`ÊçYQËÅ\I	(ú/NØÒ
ìaÇÒ`ö ðÖM¹cÀÄ¿yó7Ì÷~Ë	íLW ï~r ¶9D¬5ÔÑG-¡k4ÃøôîH¸±g`#LöêR¹µÈchó\oÂäÐOIXc­Ãã¥À½ÿ ÅqÌEH{µX¥$Ì'TæÿÐØ	sºÃÉ ­»ÃÖ`?ùN éÃOÖð£hO³éU[qÁfeÑ6d¾Âñ¾þÈýc>8Ò<¬üCå3à¥rÆ.Ôo\7<áCø(ÄÆ­lâò>3	QPº)%³LÜ<îòyDdâÈ¼Lu³éW;ÄpB@bïÀhd°l
ðåÒ8FNc6(¹ãü@ÂÀ(ØÙÓþpbmLé¬r+%lmvÏBy)Íq¬ }C´Ç®P'y·Ç]`}´GÆ®p7^øw°
" vµ«¦"þuAojo'Ã®nZ©£éfÞqÍÎPKú;UAwËÛ®nè¶þ.x°¤ÏÁ¢4]2oÔ°s97×..·{<SØj0ðìÂg.MíVÎõx×½~3/Åù5p<ØåþÃ Ýë±Óíßö»p1öÁxs¤sI2D¤®Âcl~vc,ÞÝ'Ø¿{=½áÖ g6 ¦^£Îìïòæ#o>)G¡[j%àª_yäÁ Î³;ï®ô¡ÂÉ[£iñæ7'ª8¦T¢÷ðÌV°Ù#(TÞÃ²(C÷ÖÅ4k
Ø(FGR"µäJÛT.µmw
ôDuD~xcÜlÙrµ£r¨F«<¿ÔÏíB¢Þaö=¬élm rk¥¡*Y³c¤;ÎíÈpòde_§äÝ®~¿RçùÝ.gåÝ^r!+ª¼¨f}SØÅr[òçx%£LlV(eÔß¬H$jp	Ô\±ëÜµªÚÜqXå#æ)I´»³7¨èhG3Íx½RwÏ·GÅEª	V,ÎË\9ïIo­eÙ_^µ~\;Jróù¨U
ãì?¦ÞQf¨ÚQ4ð÷5,o
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/2e5d91a0d0bb87e6ff7cd5e9b78a7e854ed3b4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/85/2e5d91a0d0bb87e6ff7cd5e9b78a7e854ed3b4 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹Û¶è2ÙX_{uG-1ês£h¿Tmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ Ò>
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/42/952c2c8a762edf95a478732d6e7aa07de29e4f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/42/952c2c8a762edf95a478732d6e7aa07de29e4f (latin-1)

```text
x+)JMU0µ0b040031QðNÎÏKËL×KÊO,JaPÌÿ)£e÷ÍyÿÃ>¬Ye¾w«+ÂÔ4¥·.Ú¬±µBeþ)/j|çSu Á¦é%ç&f§2to÷L?}væÕfJE×ý\ûÑ{TYjejNbqF|r~Q^ªnNbe~iI±^JIq&aÁâ'¾çë:²¯Ô¸òîÌÒµfë±é¨n]Pþ:Ò¥rÁ½ïÕªo,îÞÄUuvjenbìß£²«
ûnæÔ|îw9ÙÌpÎ!¬ê+ss6õnõ¯®åèÁ¨+»òÇßêÝUuUn¶^%PÃ4-ÿÅGÄgçìßoþÒ÷Ò/R³°iÏIM+ùáyË¼·wL3yê¯ømj­[þ2§xDX±üÙ5ãÐûî&nÑÀ¸YåYíXõe¦g@¬Ú¾å¶ðüé;^YúíBêt·,+aÜZìz¿h:bä¡ßNóÍ¾ö¹ig×Z õü
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/48e7259643fd9f7ca4e967904c93509a3bf3b4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/48e7259643fd9f7ca4e967904c93509a3bf3b4 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹³l{¶Ý~Ò©°%/_y_Ýûû%ÓW¨ÚòÔâ½ÊÜi»¦mM{ÏQl$ÅþtÛ½=<< [éC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/0ea62383f12159220a9bc4686198d090065f52

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/0ea62383f12159220a9bc4686198d090065f52 (latin-1)

```text
xAÂ E]s
. `*ã	Ü»¡61Þßz¿z//ùÜj]¶£èm²)aöQqÊÌÅÀ!DïÁ¥T<§¬>Ôå=4 ÉK QÀñvGòämQ´gëúÑ¶®ïTE_V[^j»Í×[½jã'sþ
õÚéþoÈÿ¥ë°A})Cq
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/7fbf051def1e3cff6ce9fcfcfa8214d98d2f3c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/7fbf051def1e3cff6ce9fcfcfa8214d98d2f3c (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Óv[ä¨õ½yÇ49îÑïÛgÞpþ
QPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú `VN
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/93593a42344d9db1461d0fb746b2f8f2d94e02

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3b/93593a42344d9db1461d0fb746b2f8f2d94e02 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹½»¾¾qÀÝ3åøsn5/¡jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  °A
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f0/e1673393cb2da2edec9566defa8cd65f0a9c34

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f0/e1673393cb2da2edec9566defa8cd65f0a9c34 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`8&ûæê×Äz¾UK¾Ùq=ºÊ|»/Wª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo øªC

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f4/7155f87abbf70104070ecc61b7c43ce1c5c637

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f4/7155f87abbf70104070ecc61b7c43ce1c5c637 (latin-1)

```text
xµ1nÃ0E;ûÚ,"P½GÐA¢¨Æh2=äöqçÎ}ã{ÃÇç¶®Gô¢]Ä9CÍ9¥¤#!ÚBP¸zïÂ¯ÃºÜÕC
³©TGÉ#HL2È½µn¾å±¦íUÊ¢­_sÓOóF6zB?]þÆc¾÷Öeûy_Þ<r[ßÅ`CiÌNÓWTþudÐ]­ïÊc.
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7e/f9da78d7cf0ab1690258afbb4a4f1c01770761

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7e/f9da78d7cf0ab1690258afbb4a4f1c01770761 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹/öô¸Å>T>ï·ìãfÛË+îÜøðª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo Y¿Cf
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7e/1c66d37db037ae42c4e81521776cc794af8f99

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7e/1c66d37db037ae42c4e81521776cc794af8f99 (latin-1)

```text
x½XÝsÛ6ß³ÿ
^sç§º¶Ó¤ÛÚ®wþ/òG$9iû¢m6ÑE_'ÉYÞþ÷$!í,Ûn|0 $ò*LVìôäôä§£
ÿÄ}^xùdæNfgÞØ0KËõ¦ó+Ã»X¬Üë1Öí²w½^ë 3²-ar|ÊE¿×jñ:Ün8ûÄé¶è¦Y²æydùMj
<½}Èº¢³
âMßä]i#~;üÇEglxþæ¶n·â·þ}°ËcÝÕct×½ã
Û¦F²- å3JiÄàÓa4]e7+Thµ£èÞKðÂ /xÌ3öÉ5U»Á~cÛAê}ðòµÒ1ëúÀþü.òõ\äë,	ÃÝnØó×ksøEÄþ=MbØ\ÄS'ÞªEñNt"ÿ{'O9ßt¢\höz¤áñÂ
7<ôJ¥ }Ê_áY.+ºWxöMr<XâÌuRI	òã\]5Q,GHÅ¦÷j"¯(
Zû
âç5w
?ílüxÍ_Ip¨mä).?ö#aäÜßîÈOsf%ë;æú)ï°;RßS	ÅîÒ²¥_Æ(%DÜ¥Ì2L×sÎ'¦ûé5DHF£ö
`Ñ
Ñèñ³'{ÏjLmÍÖóR¶%_Ô×|¤Â× ãÔÛf
½¡=Ø5ÑX-Ïñ«X.¡ëüÿò27_ÏøR²\ racÔÒD;
¨BÄLDT~ºñR«tµÚßÑõ££}3ê.¯
ÛýÖ8H­~
-Ãáv/%¹Ä&(·¥À%û)9&îåb§ºûB#È,¥ï	É¢|NéECg1-çÜ0(HâH2^PnJÁh?DÌP@ÝYJ«·'gçjsr¾¾É@¡ÜÂvc
ëÁ1s
[b¹6( ð«$%»/äWR0,ç*2?Î«Ó
#`}DõqRÌTM6NaËdCùx®Vh:,R¨NfKG2U¬%v.ËµÃ0g1ÉÑ´_À ·rÇÀi°¾Ä#AÖ8
^äÊ¡0ùg^¼ÍÙr:4ìù¡N Ý¤¸½?Kx³_h¸3³_kR=8e$á8ù%ÝÃ|s6ê2ñbÏZdð"Ði¢	øï#*¤ðò#ÒjlYXÊl§ù)ûeXVãX
*®X3¯¬ÕrÃØUdÌ úd(ßªþ´ÁQÇ âª¡L\Û«WO&/¼P¨Õ$0ØÇdvtRc52£@s~î-pã¹eé¶u¾:
òÏZ
KÃ±'_2?È¹?D«$|æBq¾Lsë%	Cè²Z!#ìMZ_uq!O²dÏ±D6¡ÆKÜÇE½(h8n-ê[yÐihC¸$âTª_ô8Û$jL¹N"É¥aOfDoº¡=]ª8Ù+£J	ø:aó¥ë-¸+ÚÄ
-¨¿íð0UI«¥Ñ
*ä8ï®¼0.ðÅ
5jûh|©;ìr:°áÄqEW¸klh±WÍ©÷SIÑKnÎÆmÜ #»=	ð-þ[¯)3>øy±Ý·C|à1¡LaC&^HUªÁfY¥Aã·­½µÒ©tF]N&]NB¨î&Ñï«ºcöûe`Ñ¼µm,ë~]¶[(¬ëX
ïxwï±ºÀ0ñ¶J"L|ø$fWJg(ûrÇOÁç¹ñòÁ)J´üÖ±mùº¬F±§£O·2Ó¢S÷[qäTH!Z©ýæI5d{ò&ãë£a4ÎS@Tò:G:DñÜGÞÕÜª0Ô´9Ì7GKs9PÆé¿lúVÐ¿7¥±-­/¼éÒE¤ÿòEnÝºÜ1|®èûá¢UöºnùÐùÏ÷ºMïéhqºÝ>N÷°/b¯ñ¡¿â!þ	d£ÚePýÅ½¿ `0Fî
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7e/3fa33244f3b5b180ad3cd527b11d131eb5ff73

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7e/3fa33244f3b5b180ad3cd527b11d131eb5ff73 (latin-1)

```text
x½XëoÛ6ßgÿDP×NÓf]Úm)ñ"Û$§/l³½ ÉYÓbÿûîøHÅvÒ5º'w¼#©,ãlIo~9XÓ/QJÉçéyàÌ'32;
Æ¦e,l?Î/ÍàÒ°ÉáËÁ~l½&ÞÈµÉË×Y:(]Å5%ï¢4ßTý¼ÈV´,³¢|±®Êè½¢ðæ×wE]õQºÒ«²ÏmØoÞÒ´ê­²5-_\«vKzÞFÛ<ª®¾%7ýe¥[¶å7ô®å»­m*â¥<Ò
ðï¬¸Z¢B§$·1£²¢)-ÈwÂcn²Eþ$ïºß¢<øz«0¥äðý[òÏ[tQ®~ÀE¹*²8Þî|ïÀâpµ¢0GXEYÚ£_ó,ä#=P¦ZE	íUY/	¿öÊÒu/)æ` u±| |ÐpMãðN¨4
Ü'ÿeyXÉ­À³k×8É9Î"ºº¢E/§EÕ Áçêêb4BªÖüQXÈ^eI	ZÆÂ}õõ\÷ª0ï­ÃtEqp¨Ï:*s?
fä]G_ªþ(ÌKbg«â9o±;ÑUYveØÜ/!²eXÜäÄ6-?ðÎ&ÿþ9TpFã\¡-ó°å½¦eTøùãpIcLc¸æÌ?3½×ÊÉMq(#t'§g~ 
ì«á.puC«"^0Ì¡kÎMÿ§CtçõÂ¹Æ¯³ãßv,@y$ôã0 
w$Ç6~u&ÙC­DØâ_PÂÚÓr%MáTéYVjÛÁÞÒº§Þ\÷tÝ	Ã¯±Æb)dIí´®Óÿ7z8
;Çó3¾æ,@^7=îQÊNÍø2$8ØøYkt?ñ\J¤v×pWlpxÕ|´oo|L×ÿÖ(º
Ü²Lo2|½àÃ>Ìù.gøÒÇîÏYÂ®5g«ºû$%H,¸ïäáü¹|á~5ôl{gAÁcæùg2öÓ@ÄíÔP·Gö¹Ðjäl«ã~Î¤ôýçI&B¾oøâSß`;6]yä» ÌÏ|øÈ}Æ¿äa=WUi))ul0bªñÓÔ|$¦b²ùt
)ãòÇsHË³!H¦:-<­f¤QÅ6l¹îG¤WäñcÄ+FÓþýñÓ$#?qØ1«¡Ú±YÇÙß´ÒMò`ÌÓ¡éîí±ÝöéýÃ½1bffHª=¢ôÌðêJB¹ô+u÷Óm)$IîC²%ÍrÖ÷FúJÀÇïö0øÇ#ãÂÇôÁ­Æ¶BÝír~Ùý¼,9î
¥4sÔ;EÎÂÙ]TÆª?åx¿×6(õ|7òØýÍpÝ¹ØñÔfByõ@-&1`Ë&k°£­N9,2¼¬üÌ-8Ïm[G¨ÚµßÕpðæ¬<Ì£ik8vôKF%
Ê»dÅ(Þ§épn?¦a$ªm`mwY!ÜMí
ëÙPZ$2(è^û ïÜ	<µjLqïâ	ulùæOì1lM]õÒÍrÎøÜ$ómTjwºVL
Hl²(=	G3ÃÅ­=°Eá#d\ù¢<ñGÙ(Ã<ü.ÝhºÆ¥ÙéJäÎ9O{V5
¤¥Î67¸
Ú Ï¼XÀ+¤g <Lðq$·©áÂÉÈ0S&*ÆÔÙsª0Í}°tt¼Dd®ÉQjAsgé/é£®ZVº·+Êj³²`ÆøZ§_Æ8-qXp0zçAÂS¥ÝµÛÈ	sr¨`=ÛÖïtYVÅY_|¶ó¯]iáù 0ü9ÜÅTi;uíß­M7è:Ýò®
ZÒzÏ#Â#!z"Aê ºü©ÊCôÖFÖ¦ktZ}éÞ8µËÕ6ÝGó¤ÓP
Ì®£®¶V»þÍÐ·Eë¡m£Ú¡àúË¹Ý\@¥C¨ï§ÛÒÚv_'ðöïÊÛ¿þ-À¨©IÔr&D}L>»õÖÜ¼iÉÜºÎ^@ôü©¸$*]Õ­¯.Oëf6ýMG³ÒívQº]Ó.|®ÿuæ#eOtøûÎðÑ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/e696b3f24fc409f6817109a04ddceef478945e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/e696b3f24fc409f6817109a04ddceef478945e (latin-1)

```text
x½XYoÛ8Þgÿ
¢òT×NÒtwÛnÙ7òÉNA¶ÙD.Hr¶i±ÿ}gHDÊG,°z9Ã9¾¡f´Qºdçç§g¿­ù·0áìëøÊMGùhráì¡µpæþxzcû7ÃNN»]Æ:ö¦ÛmTñú®#TNÏÐ8é¶ZGa²6kÎÞI¶);Y®xQ¤yñj]áMàÏîóÎºl/Ãd&·EGêw?ð¤l¯Ò5/^ÝézK~<»,ê¦~Ä÷{þØÐmJ¤P>!¥aR>FÓT~»DÖq?ø"?
'<g?©Þ
ö{ü#Ìüï~±
":e'Þ±Þ¡bõÅ*O£h·ö³«A¦IÏÒ61 KñÀï
Ñ2y»LÛqð½]d¯Ûq!$»]Åô8ô@Å5G%RHò-,Ë°âgstò$b3ooyÞÎx¦È7 ¾:ÊQ,FHåºû_Ù«4Î`p_@þ¼$åvdíu¬ø	ÅñYEá'A,¼»ð[ÙéYÁtuÏæAÆ;ôTÆ·á«Dbw)li1*	'÷sìáÜ÷.GÃù9Àé[3Oí*AÐj#d£Ï¬ü-Ó-æñ<mçizÌGjá |:ºÞÜ2÷¢ç÷ÜÀn°*üf_årÝ¤ÿoôPL´¹ÁôÓD¯8 6&V&Æ§.CÈBDáí"\AèÕÁ&*}È.ìõYwýÉvç_@éÑ¿BóÅöú¸Ók9|-TïJÆlì±É1qf,f;¥ÐÜZAb!m#ò§4vÕóf}Ùñ. y<9ä%ãB0W
kÄbwúÎª×ÝÑÅ¥rsI&ÐöGiÄòáÄ³ÇÎìÉÜv%æþÜd~Ãg9ÝüÉèU¾Ê<H
¢ô±Æ	¨¯¨9º©øH³éx[&ä¦*Â¡ç@Bt4YxFÎQÄ±±s)Nì8*ÙkæÍ¬¾ÌCúÚ9;FãH<â3Èg 2\µ¥óÜO6ñõ1Y{¶{°>Ô8n¸½¿Kx?(FÜÉD5G\½´¼*pììaº¹
D}Rh±g-RØèk/iâðßE£àÂÍlH­ã`S¨ªüSõË´¬×±ÔVX³¿êu8Ùaì*3&}ò(ÏÔ|«lpÕ[¸~'OËu§ªãéÅë2Q
µrË}@EVcG#U2Öþ%¨ËôóqoLÇDØÔÕéúk]¸¶h°h;=õaÁýâ1^¦Ñ÷eÜ:Ï)Bk°7G
~=Å@¶ªxW3ßsD5¡Ä[ÜÇC3Z<¸îÌô­E<KèkC¸$¢£\Uo´8ÙW$jMJ¥"*ÉÐp&+J¢Å;]ÏµúW¶jÎ®uc×%¿NØt1÷ÇDõè¿Ç	\áÁU5Ö¡Q5rô»«.ìëüâÃ%´}´?÷Õv=¶\8 q]TÂí9ó3°Ü«}3ÂTè9'	ºsqÄCfSÄøüÒmjLü¢Ü¬ÃÔß$^ðÅÆ¡Má²U©êSmDªN,X[¯ºÖ}ÉÆ©(xÄN)A¨CJÌO´Æ!'U¦ym_¡C8ò¾$¦cuu+ÉïÉÐ=!Q¯Óé°LÓ2Jø¥!<íT9sáÿ¸Û64fÍév4Åcáç¼à%Èhõa8Ôøè{Ü¯£	ÓÎlE§!¡ªÇS8@àTp¦}¼jb43káÙÐlëÊÈlÍQsªù20øM¥_¥
#!§Ä=ÅóÕÎê3¦¨A£KÜ]T3 ÜÌ¾3uêÛ¢Òº\¨ÒäªóI
ú¬3(ª¨
t¥	Wþx1vå?ÞÂÈ÷£®vï<æþ!E¸k^­nK©rKréæj¥.L#8z(]kÿÜ´Ð´O´ß £`É#ü'ÉµûÚRÿO³ÓO3
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/cfc63f00d74744735a04b0b8c0ab4ba9a71d30

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/cfc63f00d74744735a04b0b8c0ab4ba9a71d30 (latin-1)

```text
x½XëoÛ8¿Ïù+È§eIöº]·à$N«ó¨í´Û¾N¢µFýíôÖ÷¿©%7I×ÛpFaIýHÒU­Èwý×¿mè×(¥äËô,XÌ'32;	FöØZ:~0_ØÁåþË^n¼íõZU¼¡ë0oÓè÷Z­£(]ÇÛ
%¢4ßVÝ¼ÈÖ´,³¢|±©Êè£&ðæ×wEwSuVQºÒ«²ËuØ»CoiZuÖÙ/®u½½o£]uSßî
½kè6%²m(Ê³(­ 	£iª¸Z¡@«$·s!£²¢)-È=á>ÕÑ íïQ|»ÊuÐKÒÿøüóMë'(×EÇ»Íûl	×k
kU¥ú-ÏR.bÀ%Ù;Þc¢UÐNuð[§Ì)ÝtIözRÓã¤*nhÞ	ZÛäof»Ü
<ûy<ã,¢«+ZtrZDùÔq­®XH% RµéãKc!{%9hSp÷äÏs©Ü©Â¼³	Ó5}ÆÁ¡8>¨ÌÑý4Lw}­ºÃ0/­oæd´CïHd|v%fÑns»È`yrÇûw:ûCæ gh-<+TB§¥r°½×´Êc¢?ïp®háYX®=óOmoâ5bò}ÓJÝÉÉ©èuôuwWE¸¾¡Õ1¿ÐÍk
Ïlÿç]©sñÛðDß?h#M±íÇD#4§$jISèµ"«ÂJOÖ#1q0ïÃ¥·WÄ=wÂ¶Ä`r#DRÐMúÿF
°ói4¿1ð³\ rU*XÙZc|é	ð½~x.é¡dà
·q@[ÀÆ¯ø¸ÇÍvq~i»þgÐ£¾-,tÛ"?ÏùpÉÙïòÁg/<;ì¸Ìg9ÄÛHÈËnYo1dït`gñÁãÃYAþ3NÃxÕ±éXâÎÐ9Rõ<kÜÎ©4¶ÿâ<©À¦ïà~xöüÁ/hb¶Ë1}ùøÀ¢Ïø1PkUEÒÇ#& >#¾qÅGb*O§2þ 4{8ÉD'³¥gäT`#8Ã"Á­´ã¼&ÞÂò1¤@ W<b`4ÉHãá}N*³É©©8ûAºM­Ùr:°Ýõ!v Ý1¼¿sx³wÒGÌìI5G=µ<I8/íJÙÃts$ûLeI³µ¤Â¾ðñvÍÿ­¤äÈ¸pe6¸ÖÈq°)¨jëËêçiYÏc7¨)­°'êµ;ËÅaì"3f}üa(_ïe³oâúA»õX®;O/&WÈX]Ôbì#Yd5v4¢±^O¨ÉDu~Æ¨ÑÜqLM]®wCÚû¦ö0¶càØS/E4(ïU?r x§¹óè
­IìÍQ_¢#ªxgÀsX5¡Ä[ãÂ_´(xÚú
iç'Ü#_$*¦«²^råÈgÅ-ÎöæX;_¼H[^15Ë'®ua×å ?)É|éKÎ¶¤ôÞv
¿»@Sµcqãª»jÂ>_ÂÏt|PBÆ>íOCq~O-?g·X\hâl#ë©/H ý¤3sm¾Ç°xÓWÄÔÿþÐ=jLù²Ún¢,Ø¦1þ&SH$"Ä9gÅÎ
Fï=%X¤ÚÆUØ¸H2#}-çÔj¤æüV{eUpíç+4Å¤8Æp"0ûÆY c²ÇØü5þ.Z:ÃØ¸½º¹Z®ÑµÚå]´¤wõ."ýý!Î/åDôA6pùQFúh­¬I+tF~Ö8µÏÔ.ÙæI£
 =É^ÐõÎl74ýmÐ¦k»¨¦+¸?ÃàbîÔç<(?øaº9«ÔùDÝhÙÕÞW{ó¢Ï¨©¨åJú,.}v¥UÜ¼ïðö£VÃÛ?D%±ë²ê^òËc]¯f~hQ¦Þ>Ê´°/coÐê¿I®=Ô:8üþÆEa¿|®
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/14bd570ecbf2162e643a1a51fc9b1bd575612a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/14bd570ecbf2162e643a1a51fc9b1bd575612a (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`à{©ùtâµuñGâyóÜXáhÑU[Z\¢WÃ0m×´­i/â9¤XÒn»· î$Bì
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391 (latin-1)

```text
xKÊÉOR0`  	°ð
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/f3d6fd51d41c4b364e10545cd0613b99eabda5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/f3d6fd51d41c4b364e10545cd0613b99eabda5 (latin-1)

```text
xÎM
Â0@a×9Å\@ü' â	Ü»N¦µ`¤éýíÜ>øàq«u`´;.&$ödÍ)!rd(âØ2G>ge*Q}©Ëg@ò± MÆi¶9Ø8Sf¾8¥3¥4EûxµÏ¶wxP¸n²´²Öv_*­ï·zZïOpF¨zü
ù_ª±
çÕg2Bj
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/488c9d1dfea6b139ec0a3946d6bab420fd0bc7

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/488c9d1dfea6b139ec0a3946d6bab420fd0bc7 (latin-1)

```text
xRËnÛ0ìÙ_±Hi
¤ÂHä #Ö$¤½,d¶È¢AÉ
ü÷]ÚqêmðÂåpvgf§ë|}:C 7;S/W=|]ÂÐ~¹Rð+ÐSÛzºíµé)ðá*©gªíÔU<Wm_/je~@Ë¥Zjè5tR¨½2 [+½5ðÙý2rìqÇYwAgwqÔã0a(Æ
qÊòRÞ^ç8¯`{Äíî¥v/7îäqAåBùXf!ãQß¿óyFß=.OXí@¯þ£WÊó»»ýï±K±§sGÎçAFTØõ\+Û^¯ÉMèÉ÷nýT·Khj2üTm5mdrã9+r.Qþ,Úw+rÒkz£LÕ[n×õjÝÁªú­`c4Ñí©îW°Ø6
tÛÍF:é¶Û®)¸Gµé¹ê¾~4`½xÁBSMU£æpv¤9#
ôÌãÁæº½èáIÇÁùIbV
]E2~U
/b}OÄÁ^\÷Ù£¶ô7{CZ("ÊÞ÷cÎ¼ðàLª·zÃ`ó.ò8qYÔÉP¾L8ÛõøW}2ÿ9pÚÕÈEçr"ày:|xÝÎªhR»ÄTWf~a33äo×©Ú¥:öó%2á(°¸çX$¥À7J&"ð2YÀ°àLLÅíÍÄºðÄYÂ<Á°S\ÅA2dç'ÌvúÿvV
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/9e4c6b289b06a389470630b9db01a2e937b9f9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/9e4c6b289b06a389470630b9db01a2e937b9f9 (latin-1)

```text
xÎI
1@Q×9E. TÊ "À½ËJRitúþöÜ~xðsomR+{Yºjs%f	1A%o$¨d/¾æ¨MòâK?S¢*±8Î.gÐ¡r²)¸5i]ª
cöÄöùêC>û>äËëÆK/kë÷¥Ñú¾äÞnRyTÐEg0 â¨Çßäÿ¥ÛÔ ~5D>
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/84b86e5c46ee0902990c7fd44eb2857ea7e963

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e7/84b86e5c46ee0902990c7fd44eb2857ea7e963 (latin-1)

```text
x±
Â0EßW<"
µ*v±8éR´ ØA\J¼Ú`H$yøïÆ{Æs¸­q-n²l.!G÷½~ös¹Àíz»Ãª'|ç¨,{Ýì|åízº'-ÉJ
Eu§Éï±,ªÿU
0ÕVA
É4¡¯¥óV 3C×d¥Säñ¸á!à{5£ÈáÃÂ1ë
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/93/79cb07d7b95fc3a4d14730c585349d7787ea8b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/93/79cb07d7b95fc3a4d14730c585349d7787ea8b (latin-1)

```text
x½XYoÛFî³Å"ôTE²§ÍÑ DÙª©Ã¤ä/%mlÂ<rãýï=¸KKråvgvo3»K-|ÉÎÎÞ¾þåxÍ¿Åg_Çál:ÌGópà7ÇÓk7¼v<vrÚí2Öé°7ÝîÑA ï{¤rzÆHã¤{ttg«d»æìCm¶UgSä+^yQ¾\WeüÑøÁ7·Eg]µq¶³²#tè·ÍïyVµWù/oM½%¿îã]MS?Ò»Îhè6%òm(ÚäqV>FÓTq³D£VÞBÄeÅ3^°LÄTgýÁ>´~ÄðûCX®¢NÙÉÇ÷ìï÷h¢\=ÃD¹*ò$Ùmý<Ã¢Õ¨ó¬Í¿oòÐ%=ðÆ»$ZÅ)oWy;¾·Ë
çëvZd·«d±<^Ay â'Ñ©MñKEXé½Ä³ÏÉ:y±ÀYÄ77¼hoxçäPG_éH¤Rµî¾ÃìUn AËC¸/ ~~UÊí*Ú´×Q¶â/8Çg?RR
nãoU§mJæå«;66l°CïXV|ÞJBÙUa»© :¹Û0ÏÎÃàb4ü*8}gÈ\¡-¡Ca÷ïA1·ä´l»È«¨2c>á[ÐÑõöùç½°ç»ÅÈð!~YËºMÿßè¡msé§	×Ådb´õ*`J¡D#¢ðãÄ(.möêhT!TîúÍª»úäúó/ ê1ßÂÖôq
§Wbø$TïÆ\ÙØ?â&ÇèÌXÌvJ¡¹/j°=<äLqag½`Ö'°^p1ÈsÄa@úÈ
Æ¹0hþÖà°k@,q¯ï]J¡zÝ_H7ÊÚþSØ
Èñp';pæNæ®/Ðöç> ó«>2NükÁèi/Ue¥¢Ì±FEg®È9ºÑ|$ÆÒÙt<ÉLeTÃÀÀHh4YVX¦QÄs<ÊVGk%{ÍÓõaI?@;¯D®Àh³Çg{/ÓKIþ/Âl>ÙÅ¸çúÛ@&½Õ1£¿	\ßUpç·Ú7âY-ö}ÐxÓÊ¹2hÓ62µ}UÌÊïRx4bL¯eLxA£bz£(5>öÕ`6åA©öW -j¶^Ç¤ÔÑo³óP'¬ö¿HÏ
T<Ð+9odZÉI<ÐStÄ:¾?û¢)n4\ê'J¨¶¬B#ºk@6`
ª7»7R©ç9°ÿG2ÑÂñ×³ÀíéÁ"Ké2O8/ãÞÔ{N
H6ZE5G~=Å@.@oàÒ pØ(0ÆíOävæ©Û<¸îÍÌt#GEBÚ¶
­	RÑBVþ¢Å	¾\­õÕªÌ	rE`$ëyX8¥JíùNÿÒûü¹ï\»uëÀg
.æá"§¥¨[y+»?ÚQ£d` É£X{µES¹ûò¼;>Z:H3y×*<Ãº5UéÒ#h?óLB>æÉFKa[öÿ·ì_]ÂÙÁ¢/«í:ÎÃmàwåe¡C±¡!Ö¡ÜÍìàð_oâÄÚùSï´õfe	!µÿÇ<4U'òà£ù±qÆ®5e^½!²V_¸èî5G	>ßá)äÑÉ)±"uÒ¨³dçUGð¡ÚZzc
uæÃßp±w]Ø±ED§#*Ê°à%¯@ÆèË¡ÁGßã¼%4ØÇùÎS¡yÀ)¨mplÞ´wV0sß\®siU¹á¨95´JÏ¡;°`îiÆ¯vv£ýµ#ñ*wÍQ@VÜ]T3(ñF¯§^}gÛÂStSZ«]~JNXW¢iÐg]áRÝ¥AkMP¼Ôu¨¹:Lu¨Çº>wßÝ¬äîG
¾û!f/EvþR¸*
ÞÕ×)´QéæªVV¥Õ^l+6ejí7uvÓ(|N¢%Oð)ßí'LýwÌþÊ[\
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3f/4a2be91d29fc3b5c8f0396c594eb1951a6bae5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3f/4a2be91d29fc3b5c8f0396c594eb1951a6bae5 (latin-1)

```text
xÎAÂ @Q×hf)%1Æ¸w9L§µ¡ôþö
nò/µµ[áÔªDã .+eÇSb½Ixyo¾ÜôÓ-3 ó9º%(1æ8Ï>bR 	
ïýU}Ö½Ùµ×M:­¥ÞÂëû"µÜ,FÂ0{`züuý_¾uæÅC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5b/b359eafbb3bb04fff4fbea581c058ab255e93e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5b/b359eafbb3bb04fff4fbea581c058ab255e93e (latin-1)

```text
xµ;nÃ0Sëì
üïa¤Ø%¶Ë¨UáÛG}ê¼r¦¼Üee¾¤3+§ÉúLn2£&((yÇ5ÖÙl=Vìü©VÀHÖO©êÕ!òTs)j&O±XÜåÙºúáÏëË,­ß©É·ºI&ïNåmß¸oã»u^_ñ1Ës§1·åªÌÎ'­NúØpÐãð¿FÙD_ÚäcL
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5b/f355c2a7ca5d17fb48de945656be2db7a30bbb

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5b/f355c2a7ca5d17fb48de945656be2db7a30bbb (latin-1)

```text
x½YëOÛH¿Ïù+VEB­Ô4O @ÉIÈá<°hûÅr,Û²®´ºÿýföa¯ó>ÎBÙÝÙÙßÌÎìÍÄ'ä¤qÚøã`Fï½ïýkg4ì
ìÞàÒéè]mlØNx«;·AjõjJW«¥­K¬¶i°%õ#ÂVÔª¥ÒLýÅ/^-ÒJS$a|¥w¡0ü¤ÑãK\¥åÌ¼à!©ð5ì·Li§á&Õuúè>{ë$ª¢~Î*´¸ryþ¾,É^æ)X±)
½ üÛÅd(ÎçÏ3Ññ½$¥É/ÂmÎ½Eþ$_zóãÅI¦®LuR»8'ÿ£dúD$Ó8ôýõbÈ¯lq§S
:ÜÔ2ý81 Jö@DTkêÍi9
Ës÷G9(ç	rU«Ã§ágÔw_KÎÀeò_&5x¶*Ùã½#{¡Y;¾8/¡®P#¤tV=Ãäi8ÀA¹ï ¾>ÊÅåÔÊ37ÒwçL7²ã3óÍÜ9[d=z÷i¥íF	1Âé±ÝtÖ¬;Q]ñwÁuÉ2eX<EÄÐ»¶c]õºöÅG ´µ¥,B£9(B"7í}¤©ß7Øw'ÔG÷4SØWºÕ³|òJÛÒB³wye;êDî#ÕÜIìNhzFDç
ÍlZûZ·ÛD³um¡½õFú
FPn}cKô7°ÃlËíA#6`üÉãÐ¡ïñQI[.¡Ü)å8LÝTMº1±5
¹ªÄ¼l9-³Ç°HaÄ-Ózqü£°{¸3¼0ðe<äYÊã	ÅÏéÓ.M?OÂd+tÎá	ÑgoJkÊ*ÜÝk')iÁ¡¤DjD|àâ-GaâáuÃ·&i6XA87iÌ&ÊÄB}?peØqñ
Æë!4öPß¡þzÍý ¨®\ëÚÉë1íay£Wv¢vü~òÄ4¡é6Àã0¦][ÑlúgI»øm5¦ª&©ºpHn³*çR¯Ý^0«¦Æª,ÎÅ¼²:ÄÒHU,ÒÅÌuÐ¯Bjñ9Q¶É<õ¨QB%ÛMÀAcÛiêµµIOm9wW `Lö0¶Z{Z?]bÚÎtCÙ;bõå,ï
§ý½»ðSiPÖ¢àå"÷æN7ío°'å£îi	ËSÝjãvoxsÇ-AºÉ	¶±±ÅW*ÂÞ`Ç£µL(íÁÁîI¶HÊ¤5j3ÄuÕ,HÓxcñ¦Ã¤ ½Ë	 þä±P®9pmãZ0åó¬¨åb®¤ý§Él
éö°cé}0{Pxë&Ü¶M`@âwÞ|å
ó=£ßrB+ÓÀ»¨mk
uFôQKFÇA_èöûà0þ ½3nìZØ$½º"F®`-òÁ<Â09ôSÒ$ÖHkóx)pï?@1
î09IMàa¯« ùÊüðo;Áb¾rN/'Ç`Üoéæ®ä°5ØC¾húàÃ|íI6½j+.¸Ò¬,zÑýÌW8Á×¹_b,ÒGú5¨¼1ra¼°ÓØú-ÃëÇa Ø¸M3Q\2Âg&a"J JÇ00å³d©"Ç]>hóLù)²n6 mpµ'$ö¾LFËÖ _þ cä4f8Î$	½ÉIq8Ýï
ÆÖÆ$ÎZn¥­-ÓÎâY(_JsÇ+hßí±ë%ÔI^à­ÁßqXßú­¡±+Üá"þl¨]íª©]ÐÚûñ £V{hê¨AºwGÆXâ#³=ÇþµÍNUÐÂÝò¾£º­Èì)çs°(EÌ5ìÅ\ÎÍµ ËíÃÏ¶¼»ðÁKS»Õ_s=ÞuA¯ßáKqþ b
v¹ÿ°'Àa÷zätz·½A½?Úé\©«ðÛ¦]ç$"w÷	öû`¯¢§;ØäÌÄÔ­UýÝÞ|æÍ©rJ¸Kíaá³\õ+¼0Ä½¡6êT8×ßäÍoWÐ¨Êõ.Ò
{JÐ»X©ú#uª¦ÎõPbÔ(.^1ªò©\\³ªr	:Uí³ÙWtTeÊg/®Çb}-Sg©E¤Jì©v!Ä¶s;4üBYÙÇ&yU«£Ôy~UËYyUàeDÈjä>¯Yßõr±zü9^Iá¨ûcÕ=õ7\%Ôx$"8w­ª6wÖZù9DJ­b@æî¬BÃÍ*:ÚÑLs(ÞÔZçóíÁQ±Þê`Õ~ë] ÞâÃ¥Oíï^quî(¹Ïà@éQgÿX0õ¶rÒBB ¿ï%Ë
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5b/657b5265ba1511942529d15a13ceb896dd1fc3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5b/657b5265ba1511942529d15a13ceb896dd1fc3 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹®vÇ½oiIõ=<7Û a9Tmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ |>S
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a6/550e976ccaa8991262efe3ccf379a09ae92127

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a6/550e976ccaa8991262efe3ccf379a09ae92127 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹[7<zÓ(&<ÀyÊ_f¾ÄòÕ²Pµå©Å%z¹9ÓvMÛö"£8ÙH%ýé¶{{xx ¯Ó?
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ab/f6d0a403724378cc0c1d7caaab00cb880090fc

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ab/f6d0a403724378cc0c1d7caaab00cb880090fc (latin-1)

```text
x½YëOÛH¿Ïù+VEBTj'ÐBÉIlÈá<°hïå$X8¶e;\iuÿûÍìÃ^ò(Eg¡ìîììÌofgf×fDSrÜ>ný±7§·~HÉßKw<êþðÜíé61w0ºÖÝkÍ$f½NH­FêõÊÆ%v×2Ùæ!a+õJeÏgÁrNÉ?Y-N¢MÓ(I?Î³Ô?S~Ðøþ)©Í³êÔç~xÖøö[¥4Ìª³hNÓ÷êº)½÷ý$ª¢~,jÓ¬¼ruþ>­È^åX±)ü0ü%wSd¨ì/.3Ñ
ü4£!MÈOÂm.¼Eþ$_öø±ûýÉMg^ LMÒ8;%ÿ¢tö"ÒYÁËbÈÏ
lñf3
:¼ÌÂ*ýG!81 Jö@DÔkæ/h5ªï{5)W)rÖëÃ§áç4ðKÁÀeò_&µxx6*ÙãLü»;TcøÙ8:;­ ®P#¤l^?ÁäY´ÁAÓ¹ï ¾>ÈÅÕÌ«s/Ñw§L7²ã3÷ÓÍ½[dßû·Y­ëÅ)1£Ùq¼ô^X·'2¢
»0ïëJeÊ°8y©k_ô
çìDPºÚØV¡Ñ!±ÀöÞÓÔOOÔÁïxS {Æ¥ÝîÛ+>y¥m@i¡Õ?¿p\u¢ðjî4ñf4;!¢ófv,­{©;¿m¢Õ¹Ì7ÎÔÆý±þ~Íæ¡ÛBßØý
ì°ºr{Ð²
rc º4Äòe ´!áRÂRM¢ÌËÔ¤Ûó§;¨zyG¬óÛ±ú{Ô&HÜ¢æÐËãÿ=Ã½ÑÍÏ)1 ÏS+¯Ó
¬Ó.M?O£t#tÎáÓGFÊ*ÜÝk§é@QÒM"5">pðVã(õñ¸aå­MÚm%Vê&MØdKChî²;.~¡õz­Ý 4·Ah¾B{7ª+_ôBãøõwÃ°ºÑÏv¢qôAú&4¥Ù&Àã2¦m[Ñnæ'I»äm5¶ª¦`EYyP$7YUp)_Ü^0«¡Æª,)Ä¼²&ÄÒ¡HU.³åÜa÷ ¥Ô,ñ¹Q¶Î<µÔ¨
á&7·
&Û1ÕckÆjo¯W `Nw0±;;Úü¼Â´!é¶kgáçÇ,gyWªö·Þ2È\¦AYW/¹W7ºå|Õ8)uO+x=Õí.Îa÷77¼ÑÙ¤[àHk[|¥"ì
v2~	¥}38pÑ}IÃé#ÙárÔ±Ç]Ø´/À476ozL
Ò
N8gõ§@uàZ ·Ù5/S1Ï.µ\Ì¢ÿâ4¹M!ÝÄvl} æ`.ÞºÅ!wø7o¾òùÑ¯9¡ë
áÝOÔ¶w
uFôQKNÇÁ@è
à0þ ½7n4llDÅ^]J#W°yLÍdàMìi{¬uy¼¸w wÈ\D¤!ð°Wç ùÊè¸árñ¬N¯&Çp2èèÖ¶äp4¶û|/ÐøágløI´ÇÐ®Ý*Xp1<Ã¼¬L=Ýzq<ï?rÇÄX$LûÀ×dæìú×.61ÄÉRb(hJø2¢mÑÂ§¥üa@(Ì@JÏ41ïóù"3_1=vpÃ±3ö +RBÛà0¬¬a	úg¼´i&§03ÁqQp$`ìc·×¿î÷`Ëp~ÐNìõÙ»LºN¶ÑÆ`¡-ô¯Îc®ô¯	üÄóSê¦Oðl9ìoÎÈÜùðòÁû¶%¼lmø/4;¯ÈÁlÑowG¤£ywlND=[Ý!Vå3	gp=ÝÔý½÷0÷ËXQ7/±Ë±/æTËßv4ÈD¾ìËOlN[Úµ®»Ãæ õ9iúÕ>Ò4p<lìdd0óÓqÆIç0c¦eëS®sHYÀ»»Dúm¸ÓåÇnð¢ê
,/àCTvCTvcSeÏM(}£èK²Ò%¡èåu4I/º¬©ÈkBhjnjn`5/Ö3¥û
 ÝÀ
®ÜTnàM)Qô6[¡(Ù(á#ráë\âg;V¹¤s^Üqþ@O\{È«9-¼(¢IU*Í\mU_ìKQ `ëÃµk§³ãº|_)¸Ò"X%¶TÓb×½nq0¬üã<õÕÏ[ê<?õå¬<õKð*YÞâ{ÀïÜìþmÉûwù6^øT"Î%0ÔÃnV9õ7ï*5Ùd,#<w-wW[8onÅ9DJ­¯òå÷=Ü,Ðv5Ë·/õnóÅöà¨|oê8ðÞpmà#é-je´6G9÷êoyõªl9.ÁûKiÿ£ÂÒ»JÅK=*þþ·0u
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/55/eb2c073b6481f81f07363551f8c54b8ca6d2c4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/55/eb2c073b6481f81f07363551f8c54b8ca6d2c4 (latin-1)

```text
xAÂ  =ó
> aY²1¾À»G Km"b(ý¿ý×I&3¹ÕºmÁFÑ&ûÄCÄÂd=¡°#
ÖLh3ê»|Æâ¢MÂ0[.åP²ÏÄN0Aô)
©¸WëúÙö®±¾n²´y­í¾Ô¸¾/¹ÕÀyöõÙ!uÐãoÈÿ¦Û0Aý ³ûA
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/55/ec78b82e1e201f1e99e3fd6f467009fe080630

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/55/ec78b82e1e201f1e99e3fd6f467009fe080630 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹áÕl?ïs;¾ðª±@ÀÕ²Û jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  Ôà@B
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/55/c9b61f671246a448331d7b3adc6d8536d119c5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/55/c9b61f671246a448331d7b3adc6d8536d119c5 (latin-1)

```text
x+)JMU06a01 âÌÔb«)öØÞ1éh9ÛÁÜh±8 0)/
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f2/51ba7badd8f3e32b846fa526348b583ca39fe3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f2/51ba7badd8f3e32b846fa526348b583ca39fe3 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`¸zIìà£Y·>;©·~½S{È¹÷ jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  KFDì
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f2/dcecbcec7c608e8eddf1d1e4cbeb4d638b1a2f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f2/dcecbcec7c608e8eddf1d1e4cbeb4d638b1a2f (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgHz­3iÀõ;nÇWòWZß
QPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú ¢V;
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f2/40de8ef37f13a2e91e4d391fd4bc491bf160df

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f2/40de8ef37f13a2e91e4d391fd4bc491bf160df (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`¨eµ_ÎG_æWó³[¥yçn@Õ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá ^A"
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e1/907268d00f0620ca31b879a232bdea05658084

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e1/907268d00f0620ca31b879a232bdea05658084 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó&lÈ[RÀ7¹?$Ç¡¥ó­¤}¤DAUjAFeòÛ÷ÁìÊ'§	.Y¿yá¥é3 üS´
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e1/a932c5fe0b898960f5438e6d624575c9e7af2e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e1/a932c5fe0b898960f5438e6d624575c9e7af2e (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgøð0ÝxòiÝEoßLM»÷«çZ<×ªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  ø/X
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/28/cf19946aa0f01ef28057a0a8cfa0f430955d2f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/28/cf19946aa0f01ef28057a0a8cfa0f430955d2f (latin-1)

```text
xKn!D³æ}X4?RùÞgÙôôqcsÿp¬Tª*=®¥äÆÅÑD}¼2bBz!½imt
Î	³!¯äÔ¼lÞÛÙÉ&·Æó£çäMÑxëãQüÔ³ÁÀW½®¹ÔÛ^(®åðê³>µÕZÍtú
ùÿRÑóìC:ðùÈ¯yÔêNð6ý þPV®O´
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/28/5602dbba2073e365dc2ea2c3e933b7b47476cf

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/28/5602dbba2073e365dc2ea2c3e933b7b47476cf (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`¸Q|4ªiçäb·§Îæ¨ûÔY
U[Z\¢WÃ0m×´­i/â9¤XÒn»· õ×C"
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/45/84452432f3219b42f24551b9e4a1da21199bc3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/45/84452432f3219b42f24551b9e4a1da21199bc3 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcð2(¯QóÕó8üsN§ëªj§*³óóZu52²LJYYRúN¦kÎp9CevjenbÃÙ²CF-ÛZüqVn.9øÅO<%ª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo vb?¢
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/56/27d338f869fa25cdfa1d710a2167415ea18e57

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/56/27d338f869fa25cdfa1d710a2167415ea18e57 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹u2ik7¯s:òBT±<çøõý3¡jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  Þv@
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/56/b0fbc8cad27ddaf8dc79771d90dcf4425f8dc8

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/56/b0fbc8cad27ddaf8dc79771d90dcf4425f8dc8 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓåB¹¾´½M²N÷Ò¿ÿå"Á+¯- 
ªR2*ß¾.dWþË<9MpÉúÍ/M ÇT×
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1d/fd78c51daa718ed96c7cf7e74ed36336319cc2

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1d/fd78c51daa718ed96c7cf7e74ed36336319cc2 (latin-1)

```text
x­WmoÛ6Þçü
¡ü©n¦í¶® ÉòËB½D/I³/lk©[2,yE:ì¿ïH7v\`BÝ=¼;ÞùòtYNwçÎ:]³åv¦ùìïE¹©ÞÌëjquÒÌëþtQÌÅCuömõx6­ß|94þ?U-Vå¶ÊÛz½­_³y"ÊÉñÏAO[ÔÕóóø§@gåjÕé27~7^QY¯ç~­ûó¬å¯~ãQaçTv¡?ËËÜ>_éM0Ö{\ÌÆi4ã«×±Í Rþþôâ3Q=i^ÌÊy¾ùh(û¼«¼¨ÊMSÖY­æ~*¦¯¥©·F8²R+ðÜ5h Khò¦_eëY
êhÛÒyþW¶]Öé2{Ê7/Z=_TkÂûE¶âëssçñ½ê
+5çô;6-àoÄëºV
s`ï?DIÝa ÷
ÈMD°Àø!gHVØ'=ìÂÎÌFQ¸û¡Isíql,aâx±#ë	'£±DÇÿ×ãî!DKsé&æ-dv2ý)^;?0¿c¼ÝM¬À´Eþ×\AqE0Ûw]Ù/FjÙíÖÑãI
Fl Ui\ÐkYFô}ZÏº+ pl:KÁÞBÅZDM×Æ°é<¥Þú,q¶U+£?úÐ\_óÍQüð×rBâRÅ=êMVT¢Ó>|5¨Àæáú¥¦½Ó´÷¶ïÝSuã<æNçêý¼ü²üºpþ $¬iZVÚ,LMF×è	 r!<:û¢Ó°°ÖVÝMÛÔÒ[awÙH$!d!h(­hv $> Æ¾K¬hcÐ)!RN\A?¡¥5]µuÈáíÔMb zÄÑýp®(F¸¥ t7ìta.ÇÃY&xÚ¶ùîù¯§tHÛàiL<yÎbÀöFûy´,Ú|í°}dÞd*?ÌÑ½kùìX2;mY	Ê2éÜ´±á&àõ2FË)$´½ÖLZ7/½ã@ál¡#dÓ
ÐI>Wà°ÀÄf!)l¥=å1;6!4WpbØ®Õ=ðÃÓdø<#ÝP~ÈÄ¹ILy1ëóü¸Éj¯QhÞ:ñèÓÓð8M"ºÞzf1Ð´(§¡¼ FÄ=gdxæææÞÌ
qËT!B
&<#â	8ÚFÙ|ÿ¿éug¢ýØÈ3ÁêëqxH-ÿ1üÃ0½|áÓpXË¡¼öPÑN~^äK!óVÅã6ûo:¥£ªosÅqoq½q±¹Ø¸"/5._4E Ý>ìVMPD\?*]ÈéEÂ4©>ÃiYÖË2£_2¼à:>j­N¼8²CÇÁî]¼íR®ªtWyMcjúÚLÝ`>âMç«ÍÐÓ&P³ À­Ïóm|c¦ÀL"~Ù8æµ¶åRj/­ev×ö)¢QËã&á?õ¯GÌO¿Ëèï?"OÉ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1d/b05cff346ef3103d0a327baa344d22ccae4a4b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1d/b05cff346ef3103d0a327baa344d22ccae4a4b (latin-1)

```text
x½XYsÛ6î³&ÑSÉN¶I¢lÕ(s¼p(	±9æ5$åÆÉô¿wZëv¦| °=¾wVi±"gg¯O:ÞÐ¯INÉÙe´ð¦óp:?ÆÎÄZºa4ó®èÚrÉÉépHÈ`@ÞGUÛwÊéa'Ã££ã$_§Û
%ï¼Ü6²*Ö´®ª~¹iêä&ð·Õ`ÓôWI¾IòzÀuØ»OïiÞô×ÅÖ/ou½½ï]uSß³»Á}èèv%m(*$o 	£kªºY¡ÀQ/Ëî#B&uCsZÇÔîù¼ï}OÊèÛCT¯ãNÉÉwä¯wh¢^?ÃD½®4Ýmü8Câõ¸I¼O¿EÐ%{àhd´ßý,þÖ¯KJ7ý¬fÃ¡ÅôxéÆB¤à6ùYæae÷Ï>'gèäIÄgÜÜÐª_Ò*)È7 ¾ÂJA#¤f3|/ìu°A«B¸/ ~Êý&.û8_Óã³IêÃÏã)·É×f`ÇeMÜb}GÂ¸$ãzÇ"ãûðUR¶»2lnY,OîJâ:0
.¦ðÃÏ9À±­E ö
 h1°²1¢9VOõhóxkCÉö«¢=æc±p¾]oo>Fþa7Xc~3Ä/rYA7éÿ=Ô!amnì}3ð³\ racheb|
èBä/D~¼ñ\K^oÓ&ìÂþ¡ø¨ßÍº«~m\þ0_ÀÆ5^ñá#¦|3BicÿM°3c¹Ø)æ>Ë$Üöóãá'ÜÎFÁÂf`Ýàb0gñ!àÃé#ÂçÜ þnÁaÕXâ®í^
¡vÝ_7ÒÚþÛ
Èqq'3pæÌCÇçhíÐd~áÃ'>°gükÎ)/Mçµ¤ô±EI§¯9ºQ|$fÂ7Í{"ªIàB`Lh:_F¦QÄµ\¶[E¤6ä5	ÍóÃ~v^ñ½£YAN8pÌ^¦ÒâOZEù6{²æËÙÈñØô^wÄýãÿ*cûü¤º#®^XJ¾.-KéÃtwöG6¹fz$Àk ÞÆØÃx#)92.\ñ¤
®5ö\×ÂúW-ÈBçÙØ®cá·VIóH56 åâ0zsH=þ0¯ÄüQµàj"býA.;)-ß÷D{Ó«×6V·pË~,««EFTJêq.w!fIáþ1¹«]}´´$×{xKÑfÓq
${ê¦FõC¶*Ò'Îàólä¹Ï)ÉD+©î¨Áo§ÈêîZ?È¡À[.\9³ Euw¡ÔàçG§º¼úH&u,Zï¯±*ÀdlÃÙØu1CqÊÒrä[ö¥#zó¹o];mQÀOâ-ÃhÀ!ÑÔÈöÛËá¾väØot¶»2«%üÀÓweO¶8»®fG5äSwì×º4gÐóÎtèã>hYØ=Éÿ5ÿG§Éü`Ò×ÍvÑ6Oñ.Ïöem¡ÞªëDô).ÆW½±ö¾zÚ8°ÄÉfæd3gXð°©<³!,6?ÑÚg¨öåwbÖÚ«»5ÍÄ­>#8Ä6tü¶çz~tYLt~èÁUMg8¸ÂÞª(´á
O»g/|øû.æ­Çuú8®ú¡*ZÓd´1j|ô=ÁÓE|ÝAcäó;iGÆ0¢f¼:Dp!Á9ìz6Þ<1®µøåäXFÞwé¤æËÅàë
ÿnnÓ>5Àî)Ò®wV©ùËE| é¡;rð»êÛjG×ÛÞR@Ä´ðÝVê|A¥¢S#æ/#ôÙf»¤d½)ÐJ/£Ù2ä
YîÊ¼­I3lÜZíÞÌýCJâXxMVÝ©0RáVÊ¦»«J/&-âhê¢t­ýsÓB×¾¤
8øÆ+âK¾ck'Oû×
ÌþëOT
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/aa/0123b7297c4e5a1b711ff3945ae05eec05d0c1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/aa/0123b7297c4e5a1b711ff3945ae05eec05d0c1 (latin-1)

```text
xµ½Ã0¯öS¨1ZýYòá]k##¯¼ý©¿ú¦øf¹®ë"Ê¤ô%YåÈY£çD`ars()o0Kdál!GÃß¢|§>1îDÚR\!FaÖ>"ßË,xÈ³6õÃ·3çEj»SouI]=ý
oÇÎmßµñöúEs]¯
&.@¤Nºkè´_þ×AvÑáÝ*cB
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/aa/a8421d5edb07f38ac390c66228fce4ad575d81

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/aa/a8421d5edb07f38ac390c66228fce4ad575d81 (latin-1)

```text
xÍ;
1@Që¬âmÀ!_ÁÊÆÎÂòå7&ó Ù¿ÙíÃ
Tké 8õ(i¼¸p=G½4\Do¥r)cè¬·U`xô/5øÐÑà5ÁuOÅRé¾T,ë¨Þ@X#´ÊX8sÅ9uüzú_²çVzÁÞûÐÚrY&ö¢:d
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/d52593efbe31242b6d28e98a6a3d5ef723d6a5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/d52593efbe31242b6d28e98a6a3d5ef723d6a5 (latin-1)

```text
xK
Â0@]ç¹2æ3OàÞå$3Ô1¦÷·Wpûà=^iµ®Ã:ô§ÑU­sB @.§"2/Ncg5_îú6Ï¬
Â£¨Ï¨hÂòQ(ÞÇ«uûl{·®j¯.MÖÚîKåõ})­Þ,¦ ¹Ùa0=þþo±
$óëâC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/1b58bd375426fd8f2cfcc3e80616f627a02678

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/1b58bd375426fd8f2cfcc3e80616f627a02678 (latin-1)

```text
xµ1Â0E{ì*n:â!1.TPR¥îÀíéÎÌß>iÕtD;­"&bN82w±Kl£$]/H(é¤'g9Uy«<BCÄó¬·h¹ìpàÞaV}jòÒ|Û¨¥^rÑ«9DOèÝþW×EêÒ¾Kùõiï£>ÖÜrN0le Gfo·5Ý®¨ü5Òè¢¾¨aÞ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/a600620a2f0315633c582e17dd389026b759a3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/a600620a2f0315633c582e17dd389026b759a3 (latin-1)

```text
xAÂ  =ó
> a
mb/ðîqYÚDÄPúù¹L2Ép-eëÁzÑÇA`of%¥	Äqè·sÂ¬¾Ôä3ÂÙ2ØLÙ-|~òeÃ$¬èè¯Úô³M?¨¾î²Ö´z_mï×rÓ&KôÙXcÔ°ã¯Ëÿ¥ê{·Ný sD
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/e2e272ff68b340e756e90fed7eac44ed870c58

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fa/e2e272ff68b340e756e90fed7eac44ed870c58 (latin-1)

```text
x½XYoÛ8Þgÿ
¢.P×NÓf·i·lK7òINA¶ÙD.Hr¶i±ÿ}gxH¤b9ésòÑpHe¥+òêõë£ß6ôsPòizî/æ7úcÓ2¶çOç¦iØäðÅ`@H¿OÎ^wäØÌäÅ+Â,ÎA¬£í·amË~§kZi^<ßEøNQøJ³ë»¼¿){«0ÙÉUÑç6ì·GoiRöÖéÏ¯U»½nÃ]UW_ãþ
½kØ65Òm	(PÊÒ0)£é*¿Z¡B§Ç·>ÁÂ¢¤	ÍÉ7Âcª³Aþ"o»_ÃÌÿrçë ¥äðÝòïtQ¬¿ÃE±ÎÓ(Úí|ëÀË!ÁzMa Ó¤G¿diÉE¸${àjÆ´W¦½8øÒ+2J7½¸`ÔÅò8ò@Ã
;¡R+püyæaÅ·OÛ"¯psyxuEó^Fó0­@9®ÕUÅ"hTn'ø£°½Nã´(ûêç4îAÖÛÉ>áàPMXd~ÄÌÈ½?ýQÄN×7Ä22Þaw *¾o%bÙas¿È-Áêä&#¶iy¾{6±¼wÏ r32®ÈaÐÒ8rx½×´¢?p¬héY9óÎLwâ6rò±)eÎäôÌóUA}5ÜU¬ohyBÄä9tÑ¹éýtÎð¼zqñtvü{Ë«Ã(þâ8Ì_3/Ç6.&³ZÐ}`ÏOB(aíÙrMàÔèåiê¶;½;HÛ=¸ôö8§CèL~5¯Bh§tþ¿ÑÃQ@ØI;¿1ðg¹ äÕ¦Ç¥tjÆ!ÁAC+âg¾£ûç*P"C¸.Û¨ô¡ÁáVñÑ¾Ùø.Þ÷¬Q(õ-t°eîe8½àÃ{>ÌùgxÒGûç,a×åb§ºû(%H,¹ïäáü¹p?Èºl»gAÁcæùg2öSCÄö
j1¨Û#û\hÕrÖê¸3é}ÿÍyÒoã'®9xpíØt8æç2?ñáXöÿ3ÕZe$¤Ô±Æ¨JÄ©øHLÅbóéRÆäç"kCLu2[ºZÍH6¢mØ,s)ÜH7*ÉKâ.¯Mû;ôsÄ3Nãr<üÄaÇ¬ª¥YGé?4÷müàþ-§CÓÙ»?Äè6GLïÞìO#fföZRÍ¥g[UÊ¥_©»nJ!I²ÉR4ËYGÜèK¿ØÃàKJÒ·Û66j·ËõåîçeYË±Ô²±§~Õ)êpýØEeÌ úøÃPù½mR×3 qý ÝßÇ§n&WÈØ¾¨Å" ìc¹ÉjìèD«ÓzÍ:/+?sÎÆsÛÖªvÍyý6¼9+óhÚýaAýâ.^¥Ñûq:ÛÙ0UÎDÛ6*Àë)po¿ ï|á»6ÛG¨1ÅfÅ3¸°åÌØcèE]õÍÌOø¾$ó¥çmTjníº3\yÖ¶) ¦(½: ñDºòzÌÔQpêf§+A.]8îLà[qÈ±.y©ÊÇ_BÅDy±-H
:<Lða$Nª©áÀ1Ç@âzìAcºØsDHM®þj
×sL°4C}LNua²½µ]ÛMúÛ$ÂÏÈ
D8-q(Xp(0ºõ8à¹Ñî¼ÚH$99TJ­ZmgZ;ÝUQÀý¯ÐTC¢õ[Ðú­éwL¦]^axs¸Q©Ó7-ërsµ&]£ët»ÂÏiAKê=[D*½!/õDÔA6tøeP'è­¬IWè´úÒ½qªÍÕ.ÝGó¤ÓP
L[C§ëÕ®ßüñ6h=´]T3|?#ÿrn×:¨TqõýtSZsAû¥ ïð¼Ãë7zFM¥L¢+!êsºôà(¨ÑÖW»ØhÉlG]e¯zþT\«Ä®êV½ÔkÚé´N)æ\ Uô£n·R­Úçº¦IkpÔ/lt\ýÌ1GJmÂ ÿ6ÚÜ³
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/84/8bd08cee62d8bc3534c9d0f9a6fd8c5887d71e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/84/8bd08cee62d8bc3534c9d0f9a6fd8c5887d71e (latin-1)

```text
xµ½Ã0¯öS¨1úõz!¼G¸BZ­sqdäu·?õWß0Õ|ÃP]×EEüÆ¬ØDtBafqÒ%x7ó'ëBX,[lüå³íµXAÎÝÉ{(h0ÁeC¦ø!ò¬MýðgÛó"µÝSouA3{ïNáíØ¹íã»6Þ^ñ±ÈóH#ÕõªLCê¤»ö+Âÿ:2È.Aÿ <b
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/84/a9a7bb7d937fb3b982517fb3a94d6df43d4c33

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/84/a9a7bb7d937fb3b982517fb3a94d6df43d4c33 (latin-1)

```text
x½XYoÛ8Þgÿ
¢òT×NÒ¤ÛcÈ²x#Éd§Ç Ûl"D!ÉÙ¦Åþ÷á!²£8h±z0ÃáÌ7äq¶ §oOßüq°¢ß¢¯Îe0ÝÙØ=ÖÈÛ³À\[Áµa£ã~^õûÖ-¾éÙlËñ)a;úÎA.ãÍQºÞ½u-iQdyñjUÑGEà]ß>ä½UÙ]Dé*JoßÃ~»ô¦ew­hñêVÝ· ·á}´K£ªêGr×[úÎæú}hènJd¼xBhEi	øÛå7è&É}À\â¨(iJsòpëÓ"?¢uðý!(aBÇäèã{òï{TQ,¡¢XæYïVC~vàòH¸\R°Qvé÷uÂá#4É>-£vË¬ß»ÅÒU7)d¿/e1|N |pãÆá©¸NþË4s·{ç1#§häIÄgÝÜÐ¼»¦yU Ï`;Úê	CU09B*Wýwø£°½Ì5Ð"¦àî¯rs·×ÝU.éÅñYEÅÝOÃmòo£oeÏ×±³åk2Ü±ï@dDn%f§+Ýæz	)ÃâänMlk4üñhöñ%DpLcê³ÂMà´ØÑÐ³+Gâs¿M!¥»yV¥êóXh¯AGÓâ7fØ5ÖP¸wøE,WÐõùÿò°28|rø3rac(i¢]T¡â'"
o<àªB-7q@taý¨ø¸¿uW,oövã¢|Ô[è`¼X¾kH^ñá,¶ùgÌ¤ÇF,quùt§*û"Wp2çÇ	Hp
H
ü©É ÚþÅ@ ÏàÏ!Ûügsõo

3¶MûRÔëÞøüB¹ûQóß\³Øð-<@ÊrgÇ±3ùùÀNñ¯9cPYÁÚ³ã©±a¸í #-:ÂÔÄqÄA
'Â§o[LhìÎ}-64Õ(b6;«9KòøSÃä¡Iï=A-'ü@e#ÆS5P»^bXq<`E@5ë=w¬ B¯¢YzÖñ/	ª³h¤äÉ4rçÎÀòZÓ¨ÌÃ´ ?ÄúÙÓdàºoªUý©ÍÞÊÙc-¹æÕztÛüÐ[¬3qH
-»#c¥ºÉ`[_Ëe6Ã7Eö°JòårUAöMÓ­
²ñ\Ñ©©Y>q  Øô¢§öSiHùÆ|ðåA(³9ÍÀÏv&O
¬%ÅY¯7<o"
´*êë@Àð°c¹X&q	üºZ²)@·Iý~3Pçî¬ZÛzöá ¼±e]<È­kØ÷)úëx·@jIÈÃ¨ Añ,²øÖêq{¯ YMÖ+øéPRùÎ^>¶$¶
ßgºÖ:`ê[×@¡ixÖo 
gÊHæACÒ¢·ûWhy¼ÛÊ¶(É`X£i²ê°ÊH¯&ÁkÌV¢ñ'º¯ýc²®æðÊ!.%R³ljçqmÕ)ßqd2sºì¡
lLø>v8JÄ÷gõJtÕúðÕT$ÓÜZâp§6:"à{øÞ I¤¦ã©¨@³±=´´èV´j¤N%AÛ¯vh#Èº¥qR÷ÛRï[º×í(mM¹¢Ü¬¢,Ø¤1~d±£úÇ<âÕ'â0Ù+#«F¥¶6©o¿%õF²Ç1­¼å3Rö{6íÑGJå£*¥}å6ÔdT2¼ÆnÉEÐU{°o]dYg!|5
<y3Ì£Úÿà+É²D¯o{T<ANZb%Ö4
¿JO<¢_é§µÎÃ*8Ì,ÓØ¶=1ñ# L¹oÁ¬e\jy!ïkÇ¨8©VíØ·7«Ýó·¥oïà»¾HõMá¡ØÁCÉÒÉm×9¶ø¼ySº2ËªrÕØÈ¬9 ¡V[>o5Âç½®jêZÇ¢¨ÂçÍÒÍÇÒ}»Éæí¹²-î·}.hÿíy©ôú3 þ¶®H
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/99/c7396cf96cff1d424be9954ef5ab21bc6ebda1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/99/c7396cf96cff1d424be9954ef5ab21bc6ebda1 (latin-1)

```text
xÎAÂ @Q×h```ã	Ü»ÂPJïo¯àö'/ù©Õº
ÖFÑ³áÄ9(ÞEFfLÄ%ã½XÂd'@}¹Ëgh¦¡`)ó¦às#)f2÷ñj]?ÛÞõ«èë&KËkm÷¥òú¾¤VoÚF$OÁê³qÆ¨£CþjlÃú«áBã
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c0/bde767eca51d4c7f6278d3295cfc05d470aca9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c0/bde767eca51d4c7f6278d3295cfc05d470aca9 (latin-1)

```text
xµ½nÃ0;û)´5túõE÷2è¤sc4ù<øí£½s¹¹®ë"Ê ~HcVÅ¥äèÃHÃä"6"D:[jüõÜPföÆ[ÃÆë\KÝigr>B¢!ò¨Mýò¹¦íË"µÝ¨Ê]}!L£³¿ðzìÜöñUoÏsüYäqÐëú­ zÖ EuÑ]COûádÞrFa¸
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4c/a616bb42581752d7ac5b77e1871b4a32810518

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4c/a616bb42581752d7ac5b77e1871b4a32810518 (latin-1)

```text
x½XmsÚ8¾Ïü
M3Ã§£@ríõí:c!\lpl¾|ñPOÀöØ&×´sÿývW²-Bèõæ<´Zï«´ÏJÎb.ØþëW¿¬ø8áì³sº³É4LÇáÐs;Ù^6ëözu»ìe¯×:¨âM*§/iô{­ÖI,×Ûgïâ$ÛÝ,O¼(Ò¼x¾*ø½"ðg7÷ywUvq²ë¢+tè·ÃïxRvéÏoT½¿îâ}USß6·ÝE©kî¾¿å÷;¶w%Òm	Y<!¥qRBüå×hµ7»R×qQòçì;97«Åþ`ïÚßâ,üzËh
B§¬ÿþ-ûû-(?`¢Xæéz½ßûÞÍcÑrÉÁGTÆiÒá_³4ÅÇÐ%=P=-ã
ïig}íç«Î¦ É^¯Åò9òAÅ_G÷R¤6Å/Yimîd<9yNXÄÇ××<ïd<Ó:È ¾ºÒQ]Lr!«ÞüQXÈ^¦h±æî3¨¯_+åNeU,ù3ã³ÓO¢
)ù7ñ²kFYÁìtyË(cÃ=z'Ø5­n¶°ËXªÛÙÖ(ýóÉ(xÿ+TpLÃõåZ¡$-¡C ºò7L(9È·à	@º§eTª9ÈÃ×BG×ÛkæáÀPìk(SÀ=Ãøe-×¡ëóÿ;zÀ!£68}Rð5gîBä2¢ÀDÛ
èB¨D~¸ðB«6½<Ú®ËªûGÍGýÝª»ü`yÁ'ÐÆÕ£îBë%0øÉK1|E*È÷#¨l<2¢èÜÝ}ÜODµà!g$B©ï­6±3/!½@Ù`¥¨>  DÈXÓÀÙxñ¹äW*(ü§¼<RG	ßr j¢.Z<Û<[°>á£LRGÑ+Á E®
¹)Ä*6VSÍ 
Ô,8ÒüÌqärg2oC"(dù¦¶çM°ÇsLd²>ë1ÿaHÚ¾Ð¬Ö¬
ÿaZ *$ÈÞ/¨Óµá®ø2øÌðjfÏ+rªiÂ0T;©Ú_§ñü(LçÎÀò¤Ì£¤YMa­ê6Ò­i³ß´Þ{ð¢Àè^öLd|½Tã÷]Æ«]Æë]%Úd®
Ð´½Ð°¡¸Y[0|ËfB£cù43ÜþfV¯ê¶ÎMbrÕhÚmPUî
<¨´áj8A¶PÈÚBç3 ;ªÖ"UNÙ;Ê èUÒT3EÖ"e°oÎ<Ø·¯Ó/ñWõm°O)|!«0àÜÜe@OÄ­)6GìpZ£¤ñôu0Y-õGü ÃL¡W2Pcõ#¢Ñ¢ßm$ûú~5÷4ª6<~Tð?9}l°>2LÇÖ,>4§mÃö-òÌi-&¥µ¡ÁVæ4
Ïçá¸¸ªäß<¶k`AåÕÔ#°GËm
4s¦Dz
éê>G5Ñþ ÂÉt1ctÖå¾FEÈ\H¤õ)7ö+«2|²±Ù<ç>µíj6°ö	|×Pt):lÌzÝI)ÿ$fÁÈ|:¬n®Èð=¼ðDÊ¸²{hiÅ­úUi%:kÿæÐV-Ëè°rl .H-¸ÿyts
Ï¸»+Êí*NÃm²ÆÏ)ZÙ<qGpaFH)'¢VÄÜÔòäª¬SÈêü¥<{îWÚ*Ä~¿.c¬º* BFXÀ æëò=4-×ißÒ8s,Úÿ*Á÷eáÞ?}Qq_9/x	2J©i~N4ø3jcóc58ðÉÌlÛx1Á \cî[ð©j,ªýÚ3*IêÕöèÍ:ì@ógÑ1Áñ	ÿ A¢ù
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f9/2b2bdaa4d79ec445dccf188c8897703bbf7cbd

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f9/2b2bdaa4d79ec445dccf188c8897703bbf7cbd (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg°­1nrZ¸G/mqmï¯I]	(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} V
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f9/56984799dd4c26d2d7b69005aac4df7d44b677

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f9/56984799dd4c26d2d7b69005aac4df7d44b677 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`x"gº<üÆ*÷Ð®¥S&]MìÑÓü¿ª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo áBÍ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6d/92e2610094896dd4ec17ede41f5836f15c782b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6d/92e2610094896dd4ec17ede41f5836f15c782b (latin-1)

```text
x5ÌKÂ aÇ¬â. -q FÆ©q5¦
\ÑÕÛtöÎù
§óÁs'\±ô÷(\åIà<bAÝ@,ÖI¾ÄÜ@
iQ6Ôa2yõWÈØ- 
JdðuË.Òµi7¬ ;ôi×ujÇà»³Ç'?`Æ:
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6d/e30f3fd645f6023dc00af159d367e441b8fb33

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6d/e30f3fd645f6023dc00af159d367e441b8fb33 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`ø[<­¢vÆÙ;ñ74Ó&¶mª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ èB·
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/38/ffe5ff42e94c6ac7e24a963046b21d43fce83f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/38/ffe5ff42e94c6ac7e24a963046b21d43fce83f (latin-1)

```text
xAÂ  =óýfwÊ&Æøï.µAúû¯3dr«uÀDÑU§<¼w)I¡`ÑÎ"Åí*GWHÉ|b×÷ P£gl!&'Ì%å³$Ì(ÞÇ&nãÙ:<ÚÖá«Âå«K×ÚnKëë[½M¼cG´f§ûßÐÿKÃÁü S@f
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/98/197649df2f773fdfea25de8e3cec7975a5f668

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/98/197649df2f773fdfea25de8e3cec7975a5f668 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó\[\U>+Îvúä¸óÉÂ[³CT¥dT1(¿}\È®üyràõ7^> oTÁ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a7/de0ac5526eec8b5182e62518c6698c3ce6eb78

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a7/de0ac5526eec8b5182e62518c6698c3ce6eb78 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcØ°£µ²ÊïvÆ©Ç·?äEËMÁPUÇÐª«eÚTÊÊÒgp2]sÃÌÙ*³S+sÎ2jÙÖzä³rsÉÁ/~â)éPµå©Å%z¹9ÓvMÛö"£8ÙH%ýé¶{{xx HA
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a7/8a475b660f3fe2fb0e3ee54bfbeee896226b6a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a7/8a475b660f3fe2fb0e3ee54bfbeee896226b6a (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`2cõû;"m"û.w½_Û¤
U[Z\¢WÃ0m×´­i/â9¤XÒn»· øºC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a8/0cb0119d9d6bc103e30e085b3a4fbf4c765f78

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a8/0cb0119d9d6bc103e30e085b3a4fbf4c765f78 (latin-1)

```text
xµO1Â0cî+²#ª\s×´Bü1$+­ ¤JÓ¡¿'#3Ëlsç)+£Í!'å
@; ¹¦È;+¤´aÀhSµ¸$ï¬Ä7¬­ñ-v0Ý¢¢ÐwìÚÐ0VnËcLê)ûì)Çtó1ßÕ¹{æø^·UÒZ¿cåµ×)¯9Î -¢&uÔUqË,-©¾W«?sîbà
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a8/4d68b17c020248a4dd672d9105cd2e6628f911

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a8/4d68b17c020248a4dd672d9105cd2e6628f911 (latin-1)

```text
x½XYsÛ8Þgÿ
N3ã§º¶Ó&»Ûv;#ÛRì|D¶/ÙfMt$§M;ûßà!òvÛY=@ d²Ò9;?íÿv²¡ÂÓK1Ì¼ÉìÂ±´=:¿6ýkÃ&ýÓ^n÷z­£*îÐ±Êéaý^«u&ëh»¡ämdÛ²åéE/6e¾S¾Òìî1ïnÊÎ*L6ar[t¹ûíÐuº¡Å;UoEïpEÕÔ×ø¾{OºMt[Ê'²4LJÀ§ÃhÊoW(ÐjÇñÏ\ð£°(iBsòpêh¿ÈÛö×0ó¿<úÅ:@èôß½!ÿ¼AÅúLë<¢ýfÈ·	Ök
{e&ú%K.bÀ-Ù'Þc¢eÓNvâàK§È(ÝtâIözRÓã%¤*nh<
ZÛä¿Ì2w+~xmr<ãÌÃÛ[w2iòÔq¯®Ø¨JA#¤rÓ{?
Ùë4Î @«»Ï KåNdM¬é3ÅñÛEî'AÌÜ»ðSÙYAìt}O¼ #£=z'"ã;p*®tÛ%DËûØ¦åùîxbyïCæ gh,\+TB§¥rB?ûûk¢R?ïr¬h7þÀ×¹ÓËtoa8æÌîÄN:±ç«õÇªãP>M°_ä¯B(.9á&Ð¤:yZ¥zÊ'báèi[oos1ðÎ9¢±FâÐäê­ ëôÿ:a}4¿1ðg¹ äUaI(A;
è»1dþ·Jx7ð\ò¦Û)ØF¥õ³âã7ëìêÆt¼ -3GõZX!¦;D>N¯øpÃÙïðÁc£?ØÖ	»%½¸Í¹ÄÛHÈË	·¬»2È¶;¶ ò>¸|1+È·8ã1´"vAÜÚBª^geÅí¥	´ý7çI¶|g8qÍ)ø3¨TÓáÈüÈ÷|`ÑgükÎT{yRÇ#& º"æ¸MÅGb*6O§2þ!4´\d¢ÙÒÕrF*°ElÃfKá:&í¨$¯»0<c4é ÐÎK10§¤ÏñðîÆººê@[ÒÏ4÷müd}ÌÓÙìÊz}h7GïïÞìé#Ffö§¤#®
·Ê$\v¥ìqº¹
A}H¦²¤YÌZRagD ¯||²Á?ÞºÒ×Ù66ªÚåþ²úyZÖëØ
jJ)¬Å_uÚåâ8v3È>þ1/Å|§lpÕõ@\ÈcÏÃqæ¢ã©Åë2VµØûHYhyZïYGáeéçclÁØhnÛ:BU¯9¯OCÀÁò1¦­á8P/yÔ/ãU=q¡¸¦¹}ôBiD+Lbo
üzìT
ð.¾k³jB)¶,Ç-g´(øÚÅ=±ám¤ÛäwÉ¯BfD¬ñýQR¤bíÎxE±T`i9pá¥)óc\uIÀßcd¾ôü¥wE[Rúo;?ZÐk9ÖÅ ã­b_]WKø?D&ãSóýPÜaWSÃ×+¸¬ý#ÇØ#SË½zO}&1U#hÿÐMÛ9&öI3@ð©â@|J¾ë5e%G¿(·0õ·IÒTíR"B¸1,¸1}ð®àÎhbíÄ½åFúJÞU»5[£½JÓ2JxükáªÔ¤¸,¸HíFh+LjJexsxn©ÓÏ0«{/(_£kµÇÂÏiAKîê."·u
6þ/åDÔA6pøKQ]Fúhí)¤:-¿tk:djìwó¤ÑP
ÌdÏézo¶ß³§n&µBÁpëTÓ<¡=·ëÛ~ÇBÓbÞÙA2øX·Çæéáß|ý¹Ï¨©\¨+Ã xéOïlÒîO¾z¤6F]Eßzü¸$V]­^'¿<ÖõnúLGsÒõQºfFHºø]ý+Æ1J¯ÿ/³¨|C
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/54/c6c071ede2dfe7a467d208a22c45a3ea3e768f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/54/c6c071ede2dfe7a467d208a22c45a3ea3e768f (latin-1)

```text
x½XëoÛFßgÿð§º¶ÓÇ¶´+ ÛrâE~TÓµ_Ù¾&Bô$gMýï#ï¥;ùf
&¾#äýHñxTVq¶"ozýÓ_N6ôKRòyz,æ?#{l-?Î¯ìàÊrHÿ´×#¤Û^ë¨7t¦rú0~¯Õ:Òu¼ÝPò.JómÕÍlMË2+ÊªÞkßh~s_t7Ug¥(½.»\ývèM«Î:ÛÐòÅ®·¢7á]´Ï¢nê[rÛ½¥÷
Ý¦D¶­ åBy¥à3a4M×+hµä.`.qTV4¥ùN¸Ou4Èä]û[_ïrÆ tJúïßÞ¢rýåºÈâx¿ò½/ë5=Â*ÊÒýg)1àì7Þc¢UÐNuðk§Ì)ÝtIözRÓã%¤*nhÞZÛä¿Ì2w+¹xmò7y1ÇYD××´èä´2ò
¨ã^]±JA#¤jÓ;Ãìuä ULÁÝg?Ï¥r§
óÎ&L×ôâøl¢2G÷Ó0aJÞMô¥êÃ¼$N¶¾%~Ñ½ñx+1®tÛ%D	'·9qì±x±ÿþ9dpÖÂ±B%tZ*ça¯÷QyF4âçÃ1<ËµgþíM¼FLþ£oAé¡;9¿ð}¡¾îîª×·´:#bòn\kxiûOã¢0fº'kòE¢CûEØ+ûé|²w=²ÍÌÔêd@S¬ëÅÑÍ¿#'±¤)\&"«ÂJ?'báèÁ2n½½&îù ¸æÁ	d¦*« ôÿnÂ.àÑüãWå«Z¥K+à/]û1
õ]	ï@®(è"Âm\P÷ðfS||ÇÍzøá£íú@[&4ú[ha%³½!òqúù`#ñ]>øqô¯_Âºåb¯ nóI® ±ä¶'#òçrÂí kà-²ã]ò,>x|1+ÈsÆ9c?5D¬ê ¸3t.T½Î* ·s!M í?9O*°%ä;8ÃgOÁA¶]yè» ÌÏ|ø,úÅµWUi))}¬1bê+bÛ(>S±Ù|:ñù£¹äØsÀI&:-=#g¤QÄ±¹Ú&Ò+òxkÈ3Æ~v^òÑ$#}_Dìö5PEN-ÅÙß´Òmòàù-§Û=z>Äh7Gï¯Þì7é#Ffö»¤#®^XÊ$\v¥ìqº¹
AuH¦²¤YÌZRagD ¯|ü|`ÿFRrd\ø&6¸ÖÈq°(¨Ó.÷§§e½Õ ¦´µ8T¥¨ÝY.c1ìãCùRÌw
®z¾ëy¬­³\w.*~p]!cçB À2`ÉCVcG#*ëýL$Pçé`lÍÇDØÔÕéúmH»ÐPk³h;ç¥£å}²Êâ.ïÓt0ws`$ºB+d{sÔà×StdçÔ o°¨\ÖtåÑò|Ê2*9Ð¹ò«fü¯ÀH	Æ,¹r¬q
gN båìKø¸ç¸M]6E°U|Ï]ëÊ®¾É|éKn¶¤TÚv
hIµ?»pq}'`9Ù"LÑ
.ÞJ¨äp³Åd»ÂÌ8#ÛH-ÞûH jD¹(|ÑìfàSÄüþþP³4NæuYm7QlÓ¿,U5çX\c¸}ð*àÎý®Ñÿpo¹¾aj·F
`´WYVÅY½½.¥ EÙCÙg ßÖ0ÙcLáÏ¡ÒöXtYã>ä½ 4~®Õ.ïË  %­¸«;ºTùñ)Ø@Ê»ÒØÀå ¾.ôÑÚCH:#¿Lk:djìó¤ÑPÌd/èzo¶]ÿþ®í£®àûWs§¾ÌADù!ÄÓÍU¥ÎêØDý»+ûw³gÔT®IÔr'D}L>ë[÷'ÞaÔ*bØBñÓqIT».«'u½93Ñ£L½CiáPÆ4ß ÕÿÄ\{¨UpøÈÆMa¿ãûá6
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/24/d0b2ade6453daa1aa8afe95f81ac95256d580b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/24/d0b2ade6453daa1aa8afe95f81ac95256d580b (latin-1)

```text
x½XYsÛ8Þgÿ
N3ã§ª¶¦ÝÛÙoä#´}ÑÈ6h¢k$9Û¤³ÿ}©ØN3»³|0	 ?@ Èdg+rrüîýoGú=J)ù6=óÉÌÌN±eKÇ¦óK+¸42xÝïÒë·ý~ç 7r¦òú0A¿Ó9Òu¼ÝPò)JómÕËlMË2+ÊWª>+4¿¹/zÊXEé&J¯Ë×a¿½£ie¬³
-_Ý¨z+zÞE»,ª¦ÛÞ-½oé¶%²m(Ê³(­ £mª¸^¡@§$ws!£²¢)-ÈOÂ}j¢Aþ ºQü¸ÊuÐk2øüüýMëg(×EÇ»Íø8$\¯)VQôG¥\ÄG²_¼ÏD«(¡FIøÃ(sJ7FR2É~_ÊbzCz âÆá½i¸MþË,s·;gß!'xÈ9Î"º¾¦Ó"ÊjoAÏêêd4Bª6ýø£°½Î´)¸ûòç¥T6ª076aº¦/88Ç±ÊÝOÃ)y7Ñ÷ª7
ó8ÙúøaNÆ;ôDÆðUb]é6·K,	'·9q,Û¼³í~	¹ðD¬P	!bõB(>ð·¤)¬QdUX©>ð5èxôö¸§Ã`èNv5.à7Cü"kè:ý£:$¬ÍçW3¾æ,AFØ JhºPyÀ@rÕ¡WÛ¸
 »°Ô|ÔogÝÅåú_A7åP¿BóÅòF¸Ë>]ñÉb*Èw9Ã6öÏØä»3Rhî«ÜAbÉmO$gäÏåÛAÖÐ[dÇ;³òL>y|3+È·9ã1´"Ö% îs!Õì»Ó3qÌ4¶ÿä¶¥ÛB¾+\xÖüÁ5ó-cù. ó¾ðEñ/9cXUaZJJêXã15©8l>BÈø@þx.<´=d¢ÙÒÓrF*°EÓaËàr"Ý¸"o·0G<c4éghçG&p<ì3ð§¡Ò\½gÑ"H·Éõ1[N{°>Äè¶gï;oö»ô#3{/©ö»g¦WgîK»Rö0ÝÞ É>$SYÒ,f©ðhF o||¤±Áà¿^~Ò×;6ºÚåù²úyZ6ûØ
J)¬ÅiPwÆåâ0v3È>>Êc±~T6¸ëù& nòØåiºî\t<µp¿FÆêB À6`Ë"k°£:óL$Pçé`lÏGGØÖUéækH»ðlQ³h9=õRQIò>Yeñ÷u:;Ï)®PÄÞøÍyT5À;_Ãª	%¦Ø²x\Ð¢`à¾³PC~È¯¡eÄÅAHª=ó]ñgûDì	s@TD%î®xEq´ø¦ºæèÜÍùÔ5/­¦$à¯2_úÁÒ»¢+©¡ý·ÂªçÆ5éAÏÝUÖÅþâÃJ­/#q]LM.@ÜgUpYûG?qÆ{ÍúJbªgDôs1LlH3@ð¥bO|Oé5e§¿¬¶(¶iüº]JDÓ7
7£÷ÞÜíA¬=¸·ÜÈ@É»ú´Vb`tWYVÅY-\µ÷
÷©Ý]eã 0ü9<·Teg=À½ÂoÐuºå}´¤wõ."·
· C
ý_Ê ©
lèò¢º/ÐÚSHktZ~éÖ8µÏÔ.Ù_æI£- =É^ÐõÎl×ÿ,xÂÝµ]TÛü>£àrî4·=Ô~ñÃt{·VçM{l£Ç¾+øúsQS¹'QËõy0]ú¼³I»ÿòÕ#Í°y?ê:bøÆÐã§âX%vU¶~üç±nNÓW:C®·Ò-ìËvâkt®hÿ¹q­ÒÁÿÀêÜÔ<1
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e5/5d33756c4dccc6c699bb81f8107006de2bd5dc

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e5/5d33756c4dccc6c699bb81f8107006de2bd5dc (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹/VrÐßeÕ¹"®âÉöçy¡jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  Éî?ë
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7f/a4aaa65430d2742c0040ce01ddf121bf659b25

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7f/a4aaa65430d2742c0040ce01ddf121bf659b25 (latin-1)

```text
xKÂ @]s
. O!1Æ¸w9µ¡ôþr·ïå%k)[×hÜ©7ísÌ&8±±Å§óÐlô£· ¾Ôä3ÂÐd4Ë,8Z±9YØe^0sþªM?ëÑôèë.k]¶Rïk¡í}áZnÚLÞøR } ]þ/Uß;¢úK?BO
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/311f1570b5566b84de9a8d202fc6004a699f37

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/311f1570b5566b84de9a8d202fc6004a699f37 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,``sÈá0ÔN]!{s±Ý²C»ï,ª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ pV@Ü
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/db4c7c78aafc9e2790db9b1e941294be82b7d8

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/db4c7c78aafc9e2790db9b1e941294be82b7d8 (latin-1)

```text
xKÂ0Yç¹ Èn'`Ï2qÜR¦÷'W`û43z\KÙºN½hÃÙq³ÅÇq+Ècâ0ùLFÔ76ùtËdðD, G;ìì,nIGÕ¦õhúèë.kÍ[©÷µÄí}áZnACàõf 5Öñ¯Ëÿ¦ê{ ~æ;BÅ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/46186c0a10312b65a81dd9a33ef076c2bbdca5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/46186c0a10312b65a81dd9a33ef076c2bbdca5 (latin-1)

```text
x½YmOÛH¾Ïù«"¡Vj´ÐCrr8N°hïå$[°plËv¸ÒêþûÍì½ä¥²»³³3ÏÌÎÌ®Í4§ä¸s|ðÇÞ~"Jþ^zãÑÀrÖ¹××
mbºÞpt­{×IZífF5µKm²%íCÂV´µÚ^ÍÂåÏA,óFÆ3eq}çYp¦0ü ÉÝcÚçõiÍè6kð5ì·Nh×gñfîÔuSzç?ÏITEýXÜ7¦yuåêü=}\½Ê/s°bSQø7+Ko§ÈPÛ_,<f¢YN#Û\züI>ïÿïû£ÍüÚ¤uvJþ=EÙìDd³4ÃçÅ5Ø<âÏftøyGuú=#p>b@ìh2Ö<XÐz×þ÷zP:¯/2ä<l6%/Ï.ÓÐ,%ÉdnÖâAàÙ¨d+b3
noiZOhÄdëèì´ºBQLbòyógñ"MC
æ¾øz/×s?©ÏýhFß2ÝÈÏ<È4?òls|Ë=?ÉÏîë'¤ÿÌº=uØy\W,SÅÉ}BLÝp=çb`¸gï!rÒÓÆ²æ Iü¶÷fAv¢~ßàÐÒÝ3ÖlÝr/tgà¬øä¶)¥öàüÂõÔÒGª¹ÓÔÝÓüÎ+ÙµµÞ¥îþ¶v÷²Ø8S{;õwk6 ÜúÊè¯`ÝÛFTmÀøåÐ£÷ô(Å¤
	ÑÎzç~®&ÝØ?ÜAÕË[bw½®=`Ø+¤¾0AâÅ´^ÿßèá  ìîn,¾ LÆ¼Hy¬P¼N·°N3º4	ü<³Ð9G!pNm)«pw+®æ¤EI7Ô,øÀÁ[Oâ,Àã·étXA¨4eÊÄB{7pØqñ/p°ö6íCèìAuå³^h¿ÃánV7úÉN´^!Ì³f4ßx<Æ´m+:Òþ¨0©q¾®¦CÒQSÕNã8cä&«J.ñ³ÛfµÔP¥¥×QÖX:T©Ê²e¾ñ2
ñô³"1>3*ÂÖ§U!Üäñæ¶ApÑÄõº¦zl­ÓÓZ
ãíõ
,³é.&NwSÛVÖB@#¤3 Ýpí,ñôå,o*Õþ¿siPÖ¢àÕKîÕn»_a5NÊGÝÓ^Ou§sØ½âÍ
ot¶é6'¸RÆÚ_©{eBi_å&\ô@Ò°EúHv¸$uq!6° MãÃ>tÎAý)âE¸ÀmöÌKÁTÎ³K-s!% è¿8M.`SH7±G9Ø·nsÈ=×$þÍ/¼a¾gôkNèº"x÷µ-!â]C}ÔRÐq0ºFÃ!8?Hï
Çd³WJÄÈ¬ES3çbx&ûaN:Äk=/îÝ(æ;d.bÒxØ«ÅSPJÂÉ|BeaüM½h¹xR§WÃ»º½-9\íÇ>ß4ÞúÄYE{íÚ­£aÅ3ÌÎ[^4Þ!dáûÜ11	#[{;±úº]°ë_z,ÚÄjUIí@	_PÕ-|Z*6Ò¤ôMó¾Èh/2Ãyðó¸)Ùðot®Ú¹`EJ(`8a`EXl62èÏxi	Ò8LNaf(9ã²0áHÀ,Ù/Ç^p=èÃáüp`MõÙP¸LºN¶ÑÆ`¡-ô¯Îc®Uô¯	üÔ2êeðn9¯ÃîÈÜùðòÁû¶§>¼lmø/4§¨ÈÁlñìôF¶¤£ywlND=Û=+ò³ ¸¾nê®þN{ûe¬¨ÅXÉåØsªeÈï¸dÍÍC"_Böå§
¶'ÎmíZWÝaJsJ ú4ýjËi¸6Í
öD22ÅéÂ¸ãM¤sEÊ1Ó²õ)×9$É¬HàÝ]"ý[´ÓåÇ°6FxYup!*»!*»±©²&T¾Q$YiËPöºË¤]ÖÔä µD!4D57D57°ëÒ}n`WînD*A7ð¦T({­PlCpC¹ðu¡EqÎÈ]»ZÒ9/n8 '®=HäÕÅ^ªÊ*Ñ¤*f®¶*Ï/ö¥(@ °ÄuáÚµÓÙ³q]½¯Ë\i¬L[Fªi±ç]L¯<AVññJúêç-uúrVúx5¬hñÎ=äwnvÿ¶åý»z/}*êáÄe7«úwÃl2^¸;«-7·rÄ"%VÂWùûnhDG{mÄÛz·Çùr{pT½·HuxßZøDzZ­ÍQÎ½ú[]½*[+pàþRÿ¨°õR±áRÊ ¿ÿ °j0u
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/e10e16c512d38a7dc16448353df05909fe2491

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/e10e16c512d38a7dc16448353df05909fe2491 (latin-1)

```text
x+)JMU06c01 òü¢ì´üòbÂÕìqSëÄB6m
¾ø&n½7 >ò
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/d6a21f2014f626ae607f350a06eeb7be82cbb0

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/06/d6a21f2014f626ae607f350a06eeb7be82cbb0 (latin-1)

```text
x½XmoÛFÞgÿCP×NÓf[Úm)ñ"Û$§/_Ù¾&BôIÎûï#ïEºSl']	Oä¼<òxÊ2ÎäxðúÍ/kú%J)ù<=ùdæOf§ÁØ´íÓù¥\69|5ÒïÎ ³WÅ¹6Syõ0ÃA§s¥«x³¦ä]æªÙeV/×U½W¾Ñüú®è¯«Þ2J×QzUö¹ûíÑ[V½U¶¦åËkUoI¯ÃÛhEÕÔ·ä¦CïZºmlSÊò,J+À§Ãh*®(Ðé&ÉmÀ\â¨¬hJòph?É»î·(¾Þå*Aè9|ÿüóM«0Q®,·!ß;°9$\­(¬VQöè×<K!¸dìøVQB{UÖKÂ¯½2§tÝKJ&9HYL#HT\Ó8¼" ·ÉeîVr+ðìZä
.ò b³®®hÑËie5ÈcPÇµúb¡:Yªõà²WYC1wAþ¼Ê½*Ì{ë0]Ñgã³ÊÝOÃ)y×Ñª?
óØÙêøaNÆ[ôDÆ÷`Wb]é6·K,	'79±MË¼³å¿áx"V¨NKå<,`{¯i'D!~Þá8\ÒÃã®9óÏLoâµbò}SJÝÉé¨MôUwE¸º¡Õ	/OèæÐ5Fç¦ÿÓ.ºÃózã\ãùìø×[.Pî	}b?Ì'ðÂÉÍ±çÎÄ1[~¨b@S<À¢[{J®¤)t^Ua¥ÝØ[AZõàÒ+â¡;aø5ÖXlL)qÖÐuúÿF­°N;1ð5gá òºèñRNjÆ.A#Là(â½ ÷è~à¹¤Hm®á&®8à°Õ|Ôo|L×ÿÚ8)u:xdÞçðõø`2ä»áK»Gì³][ÎV)4÷IÎ ±à¶'#òçòÛAÖÐsF²íY y<>ä[qÊÚOoK@ÜÙçBªgG·s&M í¿8O*°)äÛø/9ð
cÓåG¾ÈüÌ|`ÑgüKÎÖkUERÇ#& :#ÞqÄT,6N!düAþx.iy68ÉD'³§åT`#ØÍ"Áýtã¼&cxÆhÒ?@ #10däãáµY
ÕÃ:Îþ¦Enëc¶Mwo}è¶GïoÞìwé#Ffö¤Ú#Î^I8/íJÙýt{$Ï!Êf1ëH{#}-àãw{ücIÉqáãCÚàZcÛÆC¡®v¹¾¬~Í<
¥sÔ'EãÎÂÙ]dÆ²?åx¿W68ëù nä±ûáºsqâ©Åó52VµX¦ûXYhyÚ¬ÙDáeé`lÁØxnÛ:BU¯ýÞì7gåaM[Ã±£^0*iPÞ%Ë,~ ¡x¦Ã¹ý¨
vI´ÝeEpc6mvn4îgCiH§Ð£{å¼s'ðlVV(1Å³Ô±å?±Çp4uÕK79o(ð¹Iæ?Ú(Ô®t-X>
dzÂm 2Ãm­uÙvðs¤HÌÆ¿FVà·èFúÔ5.ÍNWb^xÐ-ä:íQhÕ(2ÛæØ<àÛV*æÅþ!%8ýáA¤æÇhkSÃÈ0S6/D©³§0É}°ô9ixÿÈ\£ÔæÆS_ÒG]²¬to=ÕfeÁ&ñÓ³¿ô	qZ¢XÐH½³ðPi÷díÞ$bÂ*	X¯¶5¹;ÝeUqÂ7_¡- E»° ]0ûZ£è*L;ÂðçpS¦%ngÖ!~{µ6Ý ëtË»2(hI+îê=]D*Í!Úr"@ê ºü©Î#h­¬M×è´üÒ­qj©m²æI£- ]M®¶f»þµÐö·Eë®m£Ú®àþË¹Ý\@¤öCï§Û³µ:Ø}À{¿+ïýúW £¦rN¢+!êó`ºðÙ}·æþäeHænÔuÄðê¡ÇOÅ%QIìªl}iyòX7«éo:}®·Ò-ìÊvâktýO3×)'8|ã¢0Àß¿Ýäõ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/15/2784b773682b04a64a1dacc65c6045f8be72c9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/15/2784b773682b04a64a1dacc65c6045f8be72c9 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgxuk&£F`ªÕÒM.3·.+{èt¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô £Vi
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/76/5ce792b45851e673383d56ff3a37be782a8a25

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/76/5ce792b45851e673383d56ff3a37be782a8a25 (latin-1)

```text
xEKj1D³îS4Þ;C,¶¹A.0èÓÒKê¡Õ"LN#½«W(WØáúùõs¡-²T«/ÈÁ ß<K#h¶Áòø=yH1¸«Ý,KÊº÷î¹.\YÖ°.õvõÜbN çqß;¶Àß
Z©Éêê¯x£³Or?=§-¤Â¿¨y¾3ðÐcèc7º¡+=»[z$Ïÿ[¡¨³ô²$§]áKSË
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fb/4a667914669b9d2fa857a30cdb99f9c9800a69

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fb/4a667914669b9d2fa857a30cdb99f9c9800a69 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹\ïÒe^öy¾ùÒÜ¯{¥^,U[Z\¢WÃ0m×´­i/â9¤XÒn»· #	B
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5f/88cc16687c13efe5992b214a2e9a0385428530

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5f/88cc16687c13efe5992b214a2e9a0385428530 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓÚ+ÊEd6V^Ð<w>LéÉþâzU©EÊoß²+ÿe&¸dýæ
¦Ï  1TÄ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b0/6c8590c7f09afc579330cc523cc6987ad6d47a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b0/6c8590c7f09afc579330cc523cc6987ad6d47a (latin-1)

```text
x%QrB!EûÍ*²}í;ãðëÜ!BÆaÔêêkñëÞssâ7ñ°¨t¾2©%¼ h!S\&gB8MºYH½×f%rOÃïQòÒ(Jà,ºuyæÛ¥\9þ¨¯ÿÃ8ÅdÁi6]dÃä¸X°'ÕôÐYc/²ôû/6ÓF­¢Â[wçu4	ôÃHýöN&¢ãçúõ}s½çw×1be¥U6
Pc
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b0/ad6e332f437a5a9b5c8af60044e185728190c2

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b0/ad6e332f437a5a9b5c8af60044e185728190c2 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg¨.¾,+ØÀ½¿G¼øâ×N»_·k'CT¥dT1(¿}\È®üyràõ7^> ÝUü
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b0/b885797a4edb5e4628cae3dbf06e5b31171e94

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b0/b885797a4edb5e4628cae3dbf06e5b31171e94 (latin-1)

```text
xR]oÚ@ì3¿bTJe
¡Jy°ÍÅXøKwg%íËÊÀVM#þ}÷ ¤$jé^nonvgfgµë_ú½>z»7ÕjÝÁÕüÎà;Èµ_ÉÎT³]§MKHoâj®VÝDÕtÕ²Ræ$ìYªNC[+µrÙ)ºQ°Ö;Wî×¡cë8Î¦½îõ,½B¤>c"f,G%,+äÝípóv@Üí_kb0r($r*òÐÇ"3ÆÙÃO¥ôÝãòÕôæ?zÌ0»¿?ÌùÛ¤ :wèüwdDuÝöÈµ¢ëÍÜ|_êºÖÏU³º"óÈOÕ³ZA:åÙ9ç$#gyÆ%Ê9CûnePNz£@o);ËÓîÛNmZX¿l&2º=WÝ»ºv·ÝjÓQgsÝ´»
÷¤ös½Pí·Ï¬¯X¨ËªÕ.N4$âIA^y<ÀB7<kóÔë%fÕÐU	ã'YðB&Ð÷D±Àu_ì89aK#±7¤uCb¡ì}/F9áÌIô®UïlÞy¥2JC:Ê÷i»ÿ*£Oæ¿N»z9¢H²LNP<ãcÏ¯¹Q%MjéÒ,.mfüm[0e³R§~¾Ä@Æå#æó¸8z§d*/Å1ó³"
æ	¸H¬ï@ÅÌìûQqMÄ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/20/617916a668ef3d4aef615ab38031ad1caad193

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/20/617916a668ef3d4aef615ab38031ad1caad193 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg¸])%1eå©Þæµßë5¦­û4ÉÑ¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô |V<
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/20/757414ebeea84f06b9c6550b29afed64db8244

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/20/757414ebeea84f06b9c6550b29afed64db8244 (latin-1)

```text
xµ;nÃ0DSëì
ËÏ\ rÃE®l!)P«Â·7]§ÎóÁÃäº®(Cô!Y1;
ÞùÀÛ`Md ôyNèµ>å4aKïáTö±ÛÅeÌ1Ä:È!r¯MýðsMÛË"µ]¦*WõI:v¨³§¿á÷±sÛÇGm¼ý>ÇÛ"÷cs]¿¨Ñ¤NÐ5t·_þWÈ »hûgÄ`É
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/91/d4aa93ed1c75686b01859b7b6e2b1cb7e2ab07

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/91/d4aa93ed1c75686b01859b7b6e2b1cb7e2ab07 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgÐcº½K¡øqê½E_oßRRv¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô ®VÒ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4f/77204541b7c5a3d79a966b46d74e52e9eb8ede

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4f/77204541b7c5a3d79a966b46d74e52e9eb8ede (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgµoÇcÛ^V7È]ÿWlnQPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú µV
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/43/197b6a2c789235770c720df9f598fee2a206bb

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/43/197b6a2c789235770c720df9f598fee2a206bb (latin-1)

```text
x+)JMU051c040031QðNÎÏKËL×KÊO,Ja¸ãô"`Ûõ¬ÜÕ.rlîMyGMaJjDÃr¯ÈÝE~ê{%Â.{6úïú 
U6M/971;¡{»gúé³3ÿ¬6S*º¶üëçÚÞË ÊRãóòRus+óKKõRJ3Ó?ð=_×}¥Æwg®5[®¢RoAïÏWÊÌ'<|yªïûDgKç5Ù©¹²+Ê®*ì»Sóý¹ßåd3Ã90ÔV&ææ0lÈipüÃ¬?á
ÎÙQuíJÊªÜl½J â²ç¶D>+¶°
ûoe¾¯B«K]q|NjZ	ÈÅ	KvGñ]ÖÖ>R<ù¯VÕñp>Tûì_÷Õ
¡S_¼læýtÖ«0ôe¦g@¬Ø£,â\ W¬£í"xÈÞççÛÉþØ#Ù±ÄeJò!)P»ê~ñéÖ"^9 	Þ6
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/43/c070367e5b1fd6187a695f93001422e8d5f542

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/43/c070367e5b1fd6187a695f93001422e8d5f542 (latin-1)

```text
xÎA
Â0@Q×9E. Ì¤OàÞå$Ô1¦÷·WpûáÁÏ­ÖuXt]ÕÊ&
	c0d.D,]>GÌ¥4_éúVÐM]äLê#2Eò¢àU3ø2ÙÇ«uûl{·©j¯.m^k»/UÖ÷%·z³È)'°g ÌQ¿¡ÿK3¶l~PBW
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c6/1decd5f5617f0eaaa4f63e0ae2d503db8e6d1c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c6/1decd5f5617f0eaaa4f63e0ae2d503db8e6d1c (latin-1)

```text
x½Y[oâÈ>ÏüÖÍJËë¸Ø	'Æ0¶Éììe '±bldìdFç¿oUu·Ý6l´(¢»«ëòUuU_È<JæìÍùÛwÿy¹ä_Ã³?ÇWþt2²½}á
³7³<<¹6üëÅÚV±ÓSöºÕjìqE"sFíV£ñ2ÑfÉÙïa¼Þä§ë4Yð,KÒì·e5ï|}û.óæ<a|
únò{çÍE²äÙo·ºÜß÷á.ºªï«»Óy^¬Ïßñî:G²ÉÁLë$sÀ¿ßXz3GÆÉjuï~f9yÊ~0ás-ö_öûÉ÷pí{ð³ESµ?~`ÿÿ*²ÅO¨ÈiE»Õ°
X<,lyÄMþmÄ|Ä&éÑ"Ö<\ñf4WÁ·f¶æ|Ù\eÈyÞj)^L3H\ò(x,%Ð)¾I³pku/ñì5r±À77<m®y&
dûõÇ
´u*
É$Ç)_¶ÞãFBò"Y­!@ó»/ ¿~UÂÍ<X7A¼à/>mdÇÏ2ÌÖè~¬HÈ½
¿æ§`1+YÜ1/X³á¹²"°*EBWÑ¬JòänÍ,Ãô|÷rdzÌÊ 7u5!tZbl¤°¼·<³÷úà;sax¦=Ç°½KÃ¹µ<Ñ7M¡òÐ]\z¾>QÆHww;¿g²ónöÞàÊðþ±NÿªX8«÷j:¿<²xè¾ðgöÄx?Zt¢êæZØ}ãö¾gÚ@siOÁe<3¥&yëE÷RNì­Jí éÍ
s.ú~ßö
i(]P¸åfZ@¯ÿmôp0:Ï6/(³) /Jw(±O·q&ºr	â<O²½Ð¤G¡pÉïÃokR¸ºÐÎsÖMÉ°²,ø·¹N²ÚÞº¬ÛÕry`ßä)Mi3
3rã ÀAV`Gá-gOpvÎ!§CèAåÎ(´ß<Ãùqê½µí×OÁeYÊ3ïC<>1ZnuÞjLzÞ¥ÏkéuõäÔ-Eó$É£$MrW%xçò[m=tci©æyu Î5Dº±loa²#¼ý¨feÉÏ²ÇÜÓ·Ý Üäñæ¶Çp°ÉÌóû~l=f§]OãÃûØdóc ÌÜþ®vÞÕN¨`@¹­àÚYbû,/*»ý×`å>YÐdQqýûé³áx_@'ÕG_Ó^O
wsØý$Ï¢1Hé xJÇ£->©½`gÓL¨íÁÁL¨)¶H¨Ð¤¾;bË½4Òz¢qE3$-H7áúW/êÀµnk`]I¦r.µBÍ¥Òªÿ'hJ¦na;®1w°¡ÓHúS4"OôkAèbxù©Þ ñ¦¡ÏÈ>Z)è8K[ñÂ%>HNdM×äÐÃ¥/JZä±zÅ-w0;rÖeî´7ÙRá>~jÎ¼SLµUÂÚ=,¶Aiå¦ª	EÉ_<õãÍjk®=÷
çPix=Zr-0 ö;Î~+Û7Ð,»¼F±ËÉ¸#¥ûÞøz1~ê¦ð[Z?ä±,&9½W3{h8î`â(	ã%X&¥ð©×ñi?)Ñ´ýZ¶ðc²Û]ÙÂ¯MµM[±M`ohY´JªÔE!¡h=7Ë1zPdi¡pé3øº$zY4edqÖ>\6&e¦Øú­¥@6Ã{0#DKÜ|zMá¸ÜÆpTâ.%®¦þpt=ÂÚ"ËxdÏÜÇäÂ¢9Jª,qo¦êU§Ô)Ábk«Ày¤tÒ Ì¸=À$:p¬¸_Æýu¨vàñå9§¼-(:ÖàÌtQè
-vú2#¢Åé]5´«"hÉ©5§ÃÔØ¸si?º¡a¡ÐjÙJÅHÍU°"7±tJ	À/Kze¾Þ¹^
D/{®Ü;Q?;ÆâÂé]KÐ¢RJc¥Qä.GE¯èTçI7Jú]#wÅF|=©¡}aM°¤	tqáDo<=TB]6UÿÌÄtð  bÖÔî1Õñ5>êÂeÚ{«Bx Ì¶ÜUMyò,1%ÖÊï"#åÖ[AÙÓÎ¨m"Q.ÊÕÇ)µ&Ò¤È0ñpÐz¸éÃÄÛY¡¢ìí%[¡<Ly$jÈe¬+Zp¨«ê;ÕÃAðbÄ=y0`W	ØSWDÍX%t£ÊÍz«óüd_©w<$ mú|±3¯«oYªpT`õþþîBø×K]lhÿ"~BQ/Æ"öå¼¸L(nµ
¬hñ?÷|:uç/Ib+c

z<óèWPB­®E
µï¼j@9]ôT¡ÁfËÀá
±êÿ»Ã]Ü+a¥Å¥Ãq&òÅ÷·ð¡]É7Ý<ö· ×F[¯KWÇUéºn5®Àô¯8Æ@Û±á)¦ ¿¿<¨@!
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7b/73d31d11800bbf880c1773d1f5893efadb7d93

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7b/73d31d11800bbf880c1773d1f5893efadb7d93 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`h]{îÝË¾ÂNâ.»]|±så¯OPµå©Å%z¹9ÓvMÛö"£8ÙH%ýé¶{{xx PEC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1f/2b44e38e44506018167c9c763e417fb10c1099

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1f/2b44e38e44506018167c9c763e417fb10c1099 (latin-1)

```text
xÎAÂ @Q×h:%1Æ¸w9ÀPJïo¯àö'/ù©ÕºÆFÑD¬
8!RfÅ%$
Ivyr30«/wùmÁ(þ22£wm¡Dd£x¯Öõ³í]?¸¾n²´¼Öv_*¯ïKjõ¦
yãm 4ú@õøò¿TcÔ÷BÙ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/97/af87d473202e3e2c7118437bc5bdd628e7cb79

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/97/af87d473202e3e2c7118437bc5bdd628e7cb79 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓfeÊEG7ù»ÛéÌ_{¦,(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} TV
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e0/4c98f9b8c896439d7f3297c8bdfffb45635393

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e0/4c98f9b8c896439d7f3297c8bdfffb45635393 (latin-1)

```text
xu?kÃ0Å;ëSxVÉÅ¥	
&m<¤^ºY¾È"úc$9%ýôUdèÐFÛq½ß½§^»Ö«Õ¥(+ô<`M* 
½ã~¨o¨ypÞ"Óxw 
uÒ­È®
¿u¬&5|COµRYySAg3mè )à®è¡;½<"Ó+9Æ$?bf×²lc
Cå¨D2s¿"¿ å^ènÛ_=û|?°ÓG·kÚÍíÑ½µÛCsÜol¼ÔH-7ø·ç¼Ô],æ_1¦ªóÆL)þò¹Q¦
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e0/cd45e8ab8520284dbca281a9dc624692bae3e6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e0/cd45e8ab8520284dbca281a9dc624692bae3e6 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó¦É[M*PÔø4÷RòüEÞe§6BT¥dT1(¿}\È®üyràõ7^>  "T@
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e0/282c7bd8bfa5c3c89c6eb3adca03c451b9edaa

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e0/282c7bd8bfa5c3c89c6eb3adca03c451b9edaa (latin-1)

```text
xA
1E]÷¹6Í'pï²ÓÆqÀZétîo¯àæÃ{ðà§ZÊÚÁYèMqbÌÖ97g§YP<¦M9%ÎÁ|cÓOLäýìZ	)ª0RSO/bâÞ_µÁ£î
î±(\6]j^K½-%®ïSªå
6°
(Í°ã_×ÿKÓ·NÎü ¿]A
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/80/ba21b32645f93ef7df329c1efc91e33eb3cbf4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/80/ba21b32645f93ef7df329c1efc91e33eb3cbf4 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`ø,ÇÿGÀþL­ì=øWûXoÞª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ ©¯AÇ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/48/35971973633f7e6906c8abf1db88d8509816b1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/48/35971973633f7e6906c8abf1db88d8509816b1 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgèY÷xÊæ+ÿ,¸©ü2ÿöNªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  àW¥
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/48/71d8c2d58f3d60e608efc5285f1d482c73e77d

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/48/71d8c2d58f3d60e608efc5285f1d482c73e77d (latin-1)

```text
xK!]s
. éæ×ã	Ü»Ä¦'1s¹·¨T%[­ëÐÝatKa-;ÇRñÎÄÏò2êº|Æ(b¦qÖ	ìÐ evYTÚÇ«uýh{×÷TE_6YZ^k»-5­ï·zÕH½Cú@M:ÿ
ù¿TcHê¶A½
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d3/344b2ce10ac03ae85037e85d55c033c857f488

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d3/344b2ce10ac03ae85037e85d55c033c857f488 (latin-1)

```text
xÎM
1@a×=E/ $ýI; â	Ü»LÓÌ8`­ÌÔûëÜ>øàIomÖa8MÕbt)§ì
¦ÀXY¢8ç¢ÉÉdÞ¼ékØªUü\
¦28Bö¢!S©¡¢áÏxôÍÞûg³7njÏ».½®­_Æëó$½],¦D.D´Gð æWCÿfìÃ£ùÕBµ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/47/49f6ed132f8a2972e0fbc27449a9611f955587

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/47/49f6ed132f8a2972e0fbc27449a9611f955587 (latin-1)

```text
xOoÔ@Å9ï§°vl*µê"q@T-(PâÌxÉÌhþ,,gí¶B3ö{~þ9q¼º<±û#ìØôd)`¢i ¸áô>wðV%v6Â)ð¯³Õ®]È£Eç0hx	q`2;¶X[@­'£+Éy0´'³ÈÐjq[¤âvb>º@âeSpf¶a«yÏ:ãQû×â¶jÙ*5µàóÒá¾º
- r¤©U#þ 
CO½â"V£p1Øy.ó¼ä(Ñ·ÐFËÞSj§ú´,Âùá tæd/+¶ïP¥Êâ(¦ö¹,0½LcbÛgÌs\N>'Üj '4C½ÚH¸¾o°¶¬¨±h]³¿XÃ÷G¢¥¨\°ÔÚ¥õÖóWà~HsçBI, :vÚ¾ní/??T*°Ü®iælûËóÿV­fd5Ä5»*xUåØUYØ--§SÕP]½»ût}{Ó<|üÐ|¾ÿru{÷æ°ô=£]ËtdÐüä44ó ¡XUÕêÀý@îÐü&+P¾Õ?êèêä=
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/47/74b741cacf8fa57c767f49cb226580f1e11888

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/47/74b741cacf8fa57c767f49cb226580f1e11888 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó®Ì|üOG¿ÃÉÕò¼L0¿î#ªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  õ÷S~
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/783961a510bb5a0ed32e1c5b2bc4776393fd2a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/783961a510bb5a0ed32e1c5b2bc4776393fd2a (latin-1)

```text
x±
Â0EßW<"
µ¶ÔÅâ¤KÑ`q)mòj%äu(â¿ïÏá¶m1Ù%³x
<Ú÷äô³g\Ê¦Û4Ãª'|ç ;ÝlåízºG-Éx
Eu§Éí±,ªÿU0×F£"d-­3´Qìµ XÔqMFZE?a=PØW3¾9ü â¤06
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/0975d096c80329d790a14255ade17af73b316f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/0975d096c80329d790a14255ade17af73b316f (latin-1)

```text
x½XmsÚ8¾Ïü
M3Ã§£@Òôzm¯3ÆÂÅbôåÇxblmrM;÷ßoW/¶d!wó´Zï®ödqº$çoÞÿr²¦_£/Îe0M¦þd:ÖÈXØ~àÌ®­àÚ°Iÿ´×#¤Û%¯{½ÖAÏtmærzNG¿×jDÉ*Þ®)y%Ù¶ìfyº¢EæÅËuYDï4»}È»ë²³uÜ]îÃ~;ô&eg®iñòVõ[ÒÛð>ÚQ
õ}s×]ºgóý}hÄnZ¤Û²xÂ(K£¤üËohÐjo6÷K1£¢¤	ÍÉÂs®güAÞ·¿GYðí!(VaF§¤ÿáùû(VÏQ¬ò4÷!?Z°x$\­(Qtè·,M`òÉ¨3-£
íig~ë¥ëÎ¦`½´Åò9òAÇ5ÃaRðüEæimîÇ9ÇADÌqæÑÍ
Í;Í£´ùÜq¬®¨*&ÑGHåº÷ªWé&	ZÆÒ}õõ«tîaÖYÉ¾ààÐuTd~nw}-»fÄNWwÄ32Üãw"ÑUÙìÊ´y\B$eXÜeÄ¶F~à]LFþ_¡r@csOÌ:AÒ¢a-Tc@dWþ(%çù4Jwò´K5çñâ |
:½½!îxÜ	Ã®©"\3Ä/j¹®÷ÿoôÀCÂ¶Ááìã¯49 g6Bm)`Ú@p"¢ñîÄs(®* ìåá6.¨.Ü?*=ú7«îê£åúÁ_ÊG]ÖoðW¼ùÈ¹ Þå
_Æx¤EÓÅ¼ùµ¥ðh®CÍE¸3Jon¶ÚHÆÚÌàFoìÚ¸b,Lõ
$ÜÆúÈÆ/öBº ñÜòë;(x¨tå³É³Mßµ¹êo>ñÆdîhzÍl«@sÃäÓËÌ¤«©R0T*ì8"üÌqÄtg"gC"hdy¦¶æZL4°ÇLd>4qI^oæ¶¯gDÎ)D;åã»ík TJ` }»`].Á®g×3{áXTS%3ªÕµ,7§Ñü(JLÎÀrR¢ÌÃ¤àyLavª-$(Ö?Óz¯´Þ{ðj@ØMl>,ëµ)~k*Þ4¿7Nè,ø%r]dà¦í
åLÚ\áY6áu¦îá×½j6Ôa«Ü7X¦-øE(sWÉME«1ÚD¡BxsT\Ì Jó1l&"YåpïP@6i(B	7ÑSl-æñÍÀYø
:ó*9-þÕ±­îLÊ ÞIª(à¤l*`Ä­)n"ÙáT#_=Úé`²Zê{©Bx)lßòAÅj¬z8
ý1[~7ªnyô¨MÂûìfö±õÉ`:lÆüÁÞááÙÂò´mX^¾D®9­ÌµÖÔÐÊ¼¶Á¦áZbç79Î*ßó] öÜÀÉ­¤GhÛ1YÏa4e¢[Î Úç¢í3îL¦Àè¬«|rÈK(
ªsmì×VMdøH#³,<8\Û²7°ö	|É0t):ÜõºçÂþIÎBÅt(ïsð]<÷9|QOæbò'öÐÒ[WtªÑþÍ1­Fè°r@¬	ÎE
ÜOc»«gOÜVGÉAÆåv¥Á6ñÍìHÏ8Ë#80#Ï(:¼Vþ¹®åÌÉEå§0åùË:âìer_^c%Ä~¿*cV]
!#,àTÄðUùËÆeqÂ¡Î
ÌÚÿàÈ²ðÀÄIïîfT<ANZRjÚ¾b'ü/jóÀÀ*8Ù¶=3ñb æÆÂ³àãÔ2.5ZÈõÚÓ*Iê«öø­:<ó§±7;ù¾¯MýCRd(>Õîf,=äçõÖU½ñUiJ»§Z¢^ÆÉ{,¿êÕ<Ä¤îÉ[®6aÏÆ'Ñìâ¦Åá~ómsþdÔf+ýmÓn·/=äýý%Kãr®e*gGýHÿ º¥°
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/4baee5c1096ea6de4b878ce53500cd84411d87

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/4baee5c1096ea6de4b878ce53500cd84411d87 (latin-1)

```text
xI! =ó
> aiè&1Æx÷ÈÒù¿ó¯ª¤romÒh8ÍÁ,#[  ²`ç¨CÀZ Q¬*qôèRß8ø3%êBÙGÕ¯Ø~ÍÎ«º û|õ!}òËëÆK/kë÷¥Åõ}É½Ý¤F§)(ÏÊ*%züMþ¿sÄÈeC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/04622ca3d551012d93af67d898e8ae0f6533cf

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/04622ca3d551012d93af67d898e8ae0f6533cf (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó\[èíq÷Ðy6ó1,M^¡QPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú W\U·
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/0812883f3fc11a0c0e105075e9bb930b493812

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/60/0812883f3fc11a0c0e105075e9bb930b493812 (latin-1)

```text
xI
1 =çý¥Î
"¾À»Ç&éÆH&óç^*¨Ü[['mOsG´ÞÌTÓ¨MIÄÕSÈÕ;¢\Õ|&ÔB²Ì8Í%T-¬cJ6	ïóÕ<û>àÁMàºÉÒËÚú}i¼¾/¹·èà´Ñg$DuÐãoÊÿ¥Û4¤~ËC?
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/389e3aad54d336f2686a00f5ad2621e9ab87a2

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/389e3aad54d336f2686a00f5ad2621e9ab87a2 (latin-1)

```text
x½XmoÛ8¾ÏùÂ
°,ÉºínÝnØm®ÎKm§ÝöÅp­5êØítëûïGJ¢-§yÙÎ(""©)ÑGÉ½ê¼îþq´äÂ³£s:½áøÔ1³=4¹4ýKÃfÝçcí6èt{UÜ¾cç/Ðèv£0^Dë%goÃ8]í4K<Ï,¶,òð&ð§7÷Y{Y´æa¼ãë¼-uÄoßñ¸h-%ÏÝèzs~ÜÛ,ê¦¾®nÛó¢®¹9Ëï7loJ$ë¼8 &a\ þýe×sh4W«;_¸èGa^ðgì>WÑb³·Í¯aê¹÷óEÐsÖ}÷ýûMä0/²$¶aß°y,X,8¬a·ø4!ødDGá·¤µ
¾´òóekÉNd1}!}PqÉ£à^TÒ¦ü¥[«;g×"/q%Î,¼¾æY+åY _:®ÕVÉ¤hT,;'ø£±½HV)hqp÷ä×SRnAÚZñ?àPe§è~¬{~*Úý Í,n¤l°EïHUDv%Ñ%·¥]Æ¨dDÜ¦Ì6-ÏwÏ÷î)dpúÆÔU±B%tÓ í½áy0øu£`Î#ÏÔpÌ±wfºCw#&?éf<t§g¯OTÑ×ÝgÁâ'L½üF7{Ñ?7½_vÑég§Ã©ùdÇæ¡\úÂ³'æoðÃéÓö uô<ãÐç1ïÙ	ÓÍ¥=óîVA¡ÝØ[?µÚÁ¥××Ì9íù=g(°×Xå%:LKèuúÿF÷ð`r5àKÎl
ÈËÇJ;§\kp¼	p^@z¡ÖQáÃñXÉGýÍcïâÊt¼ ôè»ÐÀËtû8¯r¸)TïHG6vxË2ÑÔÌ¦[¥ÐÜAb&m#ò'ô"í «çNû²íY y\9ä[q*µ
"Þ ¶q»o+©j^tÒÎ@ÛÿH))äÛø/®9ð
cÓûÈü(÷rÑüKÉèkYçDécPQï¸LÉGb¤F2ù 0Q´\¢ÃñÌ­å)ElÃK ;bÍ¨`/;5ú2cjÒ?@ c10ºJXWâ÷¸dk¨ê\9%yæÇëÕÁúÏF=Ó9TÒT[Qß×ßø/rC3þ¨ÍgÏ·L%ÇR$DË­æ±*JKMó}OnËãiù¤A@·#¥ãxòDÑ(¸ðYR«l²Ò	9U>!'Z"'JCî^@I$ÓS6= úXIOQÒRÖõZ="HØ²3QÇ^A8_\H)¸Ò`¯ ã2ïªUÔAB-j>Æ¨ÁÄ¶ëÀ(k²C¬4XævÄpÜQ"YæÜÏïWó$:p¸F½}¨F`y(K¹r×¨£ïå¼ó©ïÚ¢lPb
¿MoHzOý  àMfß³áÚk_Á»¸« Øæ*GTâU>á,Ö¤~XãÄ©c\&!¹ÛNÍh¦Õel¶%¾y14àk¢öÄ«<Aé¨äÍ.YÒ£é+AÝ D¡$3ûG±º)1UÛ:ÒL­Êvdõ§ø»º"k¼7ób½Gø¥ø0QæëÁ'i«¯¢ð²ª¨2¶zÝ¬µºµÖGÉc8,¸IÄ÷Õ}cuµ4TáiÎ¤ Úza¿9JóP8ó5
ØêÑQùlo­Î0-ÕrYháÃå"FuÙX]%I·ÑÌïs?ã9/:Ùë³©ÊxÓ¡öÙ'Ö$VÕrXpÇìêÎ±ºÈ <%ÞZVÖ­ITSÛ´¿GË£(eÛ«áÛQ5_l-úwrP8´¹jVb'Ùí`ûþåÄ»¿¨j,~¬%ªÁªZmÈ±óQç/¾¥}ÔýÈG3Ot¼äå¯¶DP©~¨Ì´*°åbeðÐè×C©Ã#y-À5Mâ£üg[£:ø}}¶õ¨n£ÞþqÓÉíôf9Ôèò_hÙ×.øXÇ¥a¿ÿ ¡÷
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/187b08391e6144a76704900e6c593ea36493ed

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/187b08391e6144a76704900e6c593ea36493ed (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgP«`ºà/ç¿«áêÁ­¢tëm(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} ÍVV
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/270edaf8f47371b9dfe685138e30cfbc229124

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/270edaf8f47371b9dfe685138e30cfbc229124 (latin-1)

```text
xK
1D]ç¹O§g"À½ËN¦{0F2û+¸)ª\KÙºvN½1kaB B4a]`rdÈOêK?]ûY8òÄ(¢7É
ÓKæÙ¢£¿jÓÏz4ý ÂúºóZ­ÔûZh{_r-7m§1À8ÔgãQ£ÿ:ÿoª¾wÕjzB
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/039ab60f1e4c2f1cfa6a1403e67cda756eced8

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/7d/039ab60f1e4c2f1cfa6a1403e67cda756eced8 (latin-1)

```text
x½XmoÛ6Þgÿ
¢¨k»i³-é
È¶x_"ÉIÛ/l³Y$9kZì¿ï/"éÄv²<Þ;ÞÇÌlN:G¿,é8¥äóè<Nã`8>
¶cÍÜ M.íðÒrI÷M§CH»
2ÆN¿ï¹LäÍ;Â$ºFã NÉzIÉû8Í×U;/²-Ë¬(_/«2þ 1|£ùÍ}Ñ^V­y.ãôºlsöÛ¢w4­ZlIË×7ºÜÞDwñcuUßV·íyeJnÎßÒû
ÝÙº+ö0åYV÷bÅõÍÕê.d&I\V4¥ùN¸ÍÊ[äOò¾ù-ÎÃ¯÷a¹`zCºNÈ?'¨¢\<CE¹(²$y\
ùÞÍ#ÑbAa¨³´E¿æY
ÎG¸$û ":µW´Ue­UôµUæ.[«9ßu:ÃçÂ4îbà:ù/ÓÌÍZÝ	<;Ùã,âëkZ´rZÄÙ=úpÒÀµÚb¡:Ä!UËÎ1þh$$/²U'Ì}ñõJ
·ª(o-£tA_°µ¿e\æh~­©Úý(/-nIådðÜÈìJÂ¼®34Ëaqr×vÐ?:ÁW9@é[S_B£9(Bò¨í½¡e\ë78æ4A÷L-Ïg¶?ô7|òmÓJ½áéYêÊGº¹ó"ZÜÒêÎO4³çYýs;øa½Þy½q®õët8µ_nÙ<4r[èO¶Äþ	vx}¹=hiÆÜ8Câñ^m ´#áJÂÒ*²*ªô¤;;óÇÈ\z}M¼Ó^Øó»A$nqÖÐÍñÿ.ÂîáÁäjÌÀ×Ù×)'?§»xN3º4	®ÁDßkæç,5Ñ:©B8Þð«é¸ÇÇÞÅí@'å§ïB,Ûïãv/xsÅ Ýã@êØÞâ-KXQ3>Êê>ÉÌ¸î¡¤aôìp=HêùÓ>ìúgAÅ7¦é'2ñ£ âá
l+`wûî¹àRóì ãzÎ¤
Ôý§I6t{ØñíØ=8mcî0 ñ3o>òyÑ/9¡W¯UQZÊÞ*úèã25#±Ød4ñép¤ã»`$<vA#%X<®å2×ePfR·ÄZ}2÷3¨ç»®2ÒØóyÊÕìoZézµ7AÆ³QÏöö%H`Á4Å^ ñã?8®ñï¢ýMÍo3åÎ,¿#ä:¥òLám 7NE&mr¦VOp .\gOvä#Þlüöáò:1<F¤<¸.u~ËäùÎQÍ#j5©$K¶±?öÝ-ùÂc0ôºÆ?°¦ X T}(ËÁrõ¬Á±:¬p$À
vvñKu8=g~mr¦n%ªÍ¶fxB¡`Ï)¼49Ç4PlI"K÷«yì¹0üO£ÞÄÝP(AJ¼8&nkÈE
x@;¾ËÒ¤ö4ßý©;g¼''bð.Ø®Ø/Mx=É,{.GÛ0mÒ0¡nküF- a$ÂM=,,l5¸§ui+x3_?Wäù²§5a>ëöÅþ"±³X{õëìßF×Mw5×(ÑxNd{Øz6¤62µO	æ/é*g¼3Ëj½³p&øT!2¯Hs¶Ën55ÂG£q«ÑM£5Ê!îpðêÀV\%¸Z®¶pOseUEPº3
Òù²åj5 xÆ+ØxíS u¶¼;@ù¤lGUªFØâ:qÄõâtÑU2HÞF³¼/Ã´(%HJ<æÈäQ@OÚóx-h0pÌâqÄ½â{Æé"AâªñQijÓGRÓvt©gôå U³dzê@¦ùÐ¶¢^DºCSNzÌÖMf?¼¸¡ºcACý\eþ Òçy!geaÀRå,þ 9V÷#YÝ³Zß3FZåoÚÃf+jk½?X Iä
J½ÙÔÈz;kBÓ:<)§¯xëj«¢ÃCËó&â÷RHÅêÔ¹aÚmÔ3
øö©Aí´àó$ý%lõ¿É<»¯]ð ÇYhàï_wpë-
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/71/ab075e94817e1654b15516b25713d1ec5eaf4b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/71/ab075e94817e1654b15516b25713d1ec5eaf4b (latin-1)

```text
x+)JMU06g040031QH*ÍÌIÑ«ÌÍaÈô(aJgî7âoÈG}©Ð VH+
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/71/0c96be7ce275407364ccc7a688089b240e723b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/71/0c96be7ce275407364ccc7a688089b240e723b (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹K,º}6P*nx7©Ð9ª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo ~u>U
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/71/a54bf647c06c30b90a22ad32c35b404fc13f3e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/71/a54bf647c06c30b90a22ad32c35b404fc13f3e (latin-1)

```text
x½YmOÛH¾Ïù«"¡Vjm¡ä$6äp`;ÐÞËI°plËv¸ÒêþûÍì½ä¥²ÞÙÙgfgÆc3
ã)ùØ9<øcoNo¿Þx4°ÜuæõuC®7]éÞfV»Ù$¤Ñ GÍfmã§glKû°­f­¶D³p9§äK%Ë¼¤ñfYfæy*?hr÷6æy}Dó ºÍ|û­ÓåõY<§Ù;ußÞùÁsUQ?÷i^Ý¹º~OWd¯rÄË¬ØÂÄAþÍÊÒÛ)2ÔöèAÓ¦ä'á6Þ"/û?Äûþèe3?¦6iOPD6ûÙ,Ãðy1äg
ø³~ÄQ~OâP%» "5´Çõÿ½%Îë9MÉás áç4ôKÉÀeò_&µxx6*ÙãLÛ[Ö±Ù::=©¡®PT#¤|Þ<ÆäY¼HÀAÓ¹o ¾ÞËÍõÜOês?Ñ7'L7²ã5²ÍüÛäÜ7y£ç'1ãÙ=qýôÙ·'2¢§2ïë*eÊ°8¹O©®ç÷ô=DPzÚØQ6¡Ñ!ÂñÞÑ,ÈÕÉïúS¢{Æ­[î¹î¼Ð6E ´Ð»ºPúH5wú³{qófvm­w¡»¿m¢Ý½(ÎÔÞcýÝÃC#(·¾²%ú+Øa÷äñ U0þäÁ@9ôhå==&ÊD1iCÂe4gJ=s?WnO,lÌJî êå-±Ïº^×0ìR_ qbZ@¯Îÿoôð  ì9Ü][|AyòX¡xnaftiøyg¡sBà>3ÚRváéV\;ÍIn©Yðo=³ 7¬¼uH§£Ä
ò@Ý¤)[<PV$fäàÚ»AY7?pðr»AhoÐ~9ÎnTW>ëÖÇc8Ü
ÃêA?9ÖÑK0ÙcÒæP Ç¶E§CÚ&5îÒ×ÕtH:jpªÂiçaìCÜdUÉ¥ ~öxÁ¬ª²´ó:ÊÚK
"UY¶Ìó ^F!öA?+©Y)"ãó8£"lyj©QB'ÛMÀAF×ëêckÖjo¯W `Mw0qº;Úþ¼Â´!é¶¶³tÄÓÇ,gyS©ö7þ2Ì=¦AÙWÜËkÝv¿Án\z¦5lOu§kx{Ék>èlÒmNp¥µ#¾Rö;?ËÒ¾ÉL¸è¤áô¼árÔuÆ=ØtÎ
À4úL
Ò
N8cõ§D:p-Ûì©\gM-s.% è¿8Mn`KH7ño}æà4ÞºÍ!÷\ø7¾òùÑ¯8¡[èàÝONÔ±½º"îQKAÇÉPè
à0~!½?n4lDÍ^]*#w°yLÍdáMì9ég¬õx¼T¸w î0¹IKàa¯OA)	'ó	ñ?4õ¢åâI^Mk2ìêö¶äp5vûü,Ðxë3f}ãG×l8
+atÞð¢ñ!ã|ßä¹H ÙÚÛÕ×í]ÿÚcÑ&v£¨Jb(hJø2¢¬áÓRq± f ¥o÷EFË|Î¯\GÀåLÉÍ sÕÎ¥ +RB{À9,++bÀª`°A·xÆKKÆar
3CÉ	gfÉ~1öú«A×kâ¬ÏÂeÒur6 m¡%ps­¢Mà§~Q/{pËcÁù6ìÌm/¿üpnûyêÃ»ÁÖñ©©ÿ\sêÌæ2qÊ|ÌWÆæDò±Ý³°È(_H8àêë¦îêïÔµ_ºYh\¾{±&BVÇÕ Ü($rn²/?h0~\8³µ+]-ý»#ÝB§P_Q~9ÅìÂ©­°
w"ûÂâqÂ¸ãM¤KE\Ê9Ó²õ)×9$EXq»KTßD;5:µ1Ë
c´°WQÅ
QÅMU\º_ù1de,Ó¿¼+jh.\Ü²¡&'¬%!*·!*·»ÜÏªt«µÐA÷£t»¢BDy·ÈØªEy6D¹6ä_Zç<Üµ«åóâñg
Ü¼r³°Â¦ ª¬MªRiæê¨òüâ½ h}®]5=×ÕÞ\fßÊ`«¸i¦{ÞÕÈôÊ È*>TÉ'¼ú)K]çOx¹*ðx5¥±¿òþõÚ¶ìµ«wéS¸ÀP'.ë¢
êoö%5æk2^¸;«-]Z9cÄ(á«|EoGÑÑfÛ#ñ¦¥öñ¸^Îª=TÇ÷­µ@¤·8¨ÙÚåÜ«¿ÕÝ«²å¼zÊ¼ø§­÷

<*þþõq-
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3e/a01f0f577de819bc0929e8254ab3fe9b0fb2a1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3e/a01f0f577de819bc0929e8254ab3fe9b0fb2a1 (latin-1)

```text
xAÂ E]s
. )¥@b'pïÚDÄPz¹ù»÷_>ÕR¶®'O½1k$ÙÈBF¢T>ObH}cãO×Ñ%@9ä%aÞ&çaÉ-VWñè¯Úô³M?ba}Ýy­y+õ¾¸½/TËM£³hM@pú@vüëüÿRõ½CP?ÌsDV
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b3/51116f1515a22f5ba7e504507fd3c11dc43dc5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b3/51116f1515a22f5ba7e504507fd3c11dc43dc5 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó&l°v½±îÅãNeïÏî¹+¹S¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô `V-
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e8/bc8c465c55e123cf4ea6f1b33dd3a8dcd8f0fc

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e8/bc8c465c55e123cf4ea6f1b33dd3a8dcd8f0fc (latin-1)

```text
x½XmoÛFÞgÿC+P×Nv[Úm)ñ"Û$§í¾²}Mè
5-ößGÞt§ø%]»	Oä¼<òxÊ2Îäõàää§£5ý¥ü9½ùdæOfgÁØ´íÓù\69~1ÒïÎ ³WÅ¹6Syñ0ãA§s¥«x³¦ämæªÙeVÏ×U½S¾Ðüæ¾è¯«Þ2J×Qz]ö¹ûíÑ;V½U¶¦åóUoIoÂ»hEÕÔä¶¿¬tÍöü-½oÙnKd
¼8 gQZþý×Kètä.`.qTV4¥ùJ¸ÏM´Èïäm÷KïrÆ ô¿{Cþ~&ÊÕ7(WEÇÛÍ¯Ø<®VÖ«(K{ôs¥|ÄK²2bÀD«(¡½*ë%áç^Sºî%%¤,¦ÏKHT\Ó8¼" ·ÉeîVr'ðìZä.r1ÇYD××´èå´²äkPÇµúb¡:ªõà²WYC1w@~=Ê½*Ì{ë0]Ñ'ã³ÊÝOÃ)y7Ñ§ª?
óØÙêøaNÆ[ôDEô`Wb]é6·K,'·9±MË¼óå¿{áx"V¨NKå<,`{oh§D!¾ßá8\ÒÃã®9óÏMoâµbò/}SJÝÉÙ¹¨MôUwE¸º¥Õ)/?ÐÍ¡k.Lÿ»]tõÆÙÆÏÎÄ1îØ<tr_èöÄü~¸#¹=èîp4Åã½8%
¡¸´§àJBOéYVjÑ½õ£Õ.½¹&îÙ0º]c2¡ÄaZC×éÿ=4Âúðxþ~ÆÀ×ÈëÇJ9§_ºm0wÜ£ç"µA¸L¸
àxÃVóQ¿}ì]¾7]ÿ#hã¤|Ô]èàez#Ã×K>¼çÉTïr/mì±Ëv©Y8[¥ÐÜG9ÄÛHÈËnYCÏ1È¶wnä|ðø0fVoqÆch?
D<¼A,q{d_©ftÜÎ¹4¶ÿà<©À¦oã¾xæüÁ78Mcù. óO>|à>ã_qÆ°^«*Â´:61ÕñËÔ|$¦b±ùt
!ãòÇsHË³ÁI&:-<-g¤QÄ6l¹nG¤Wäx1â£Iv^òÑ$#Çï7¬Éj¨ôC®³¿h¤ä`}ÌÓ¡éªß
é­¨GïoßìWé$fö¤Ú#Î^J8WJ~Èd4ßØfë©¡djj°:Ýv¸¯\ül`{")92.|ÔÆXRmOº¼%\Yî®¤9\IµáB$³`á@üR $ãÃiOÓ\Öó
ÀÙ<¨Á.iëÎÅÁ¦ÖÎ7GR+7!Á	@<ÕiÖ,ñP'VA½ñÜ¶uPm]KJf¯ÄÊÃL¶dG)aTÒ ¼OY| Wx§Ã¹}¨àåðÐHõ¸¬È®Â¦ÍÂ"n(Íézô 0wáÍ
%¦x,ñ:¶|ó'öN®zfAç½¾#É|áC´bihC	%¡PÍ@f»CÌ	{@dlüÃ7^I°¿7Òg®qevºóÂÛvîh-Az$lìC	\|[yø0à`Í#Ñ±.§ía¦l^SgO«`ßRß="2×ä(Rã4}L]|Ju²f{ë¡¬6ë(6iß5qZ¢EXÐ"½³9ðPiW`íJ$âÁ+	X¯¶5¹;ÝeUqÂu¯ÐC¢1XÐ}­%tL¦=@aøs¸`©Ó/ë¿½ZnÐuºå}´¤wõ."
ÁÀ#Ñ¬!¤*°¡Ëïê¼4ÖÚÈÚtNË/Ý§vÚ&ûh4ÚªÙÕèjk¶ëm[´îÚ6ªí
îÏ(¸ÛÐæ¹ÚÁÚO·gÛÞËù#^é§òJÏ.ø®F)×}ÝzºðÙU¶¶û_]{êd¸ë áö®P&õÀjßÛO·gpñÇÝ~ôhn£$´ýcÊvºþ]ÿOÌ5GÊ9_ß¸4ð÷Ëë?
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e8/0915912708da95c4a5549e8e68eb8e1c9a822b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e8/0915912708da95c4a5549e8e68eb8e1c9a822b (latin-1)

```text
xÎM
Â0@a×9E. $3ü'pïrÚLjÁIÓûÛ+¸}ðÁ[­ëÐ`Ýit©PJ.O¥°0fÙ@­S_îòºp& R&A&!Jì3I	Ù3)ÞÇ«uýl{×®¢¯,-¯µÝÊëû2·zÓ6¥hb }6h:êñ7ä©Æ6lT?>B­
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e8/d269108ca2261622ca37b3423f2fab93ff983b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e8/d269108ca2261622ca37b3423f2fab93ff983b (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓÆæø9vlæîÆl÷´¯Þ(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} _³V<
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c8/f11bb5a2b328b578249fca1cf450260ecf652c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c8/f11bb5a2b328b578249fca1cf450260ecf652c (latin-1)

```text
xRMo@íyÅD/z01¦MÓÞ`Y+qEÔj/>V%¡¬lbâï`_r"ûfÞ{ófüXùðòÜh6PµÝ§ÑzC'èÂ ?xw#ás2F(ÉÓÈßå*Í°Òd²g2É£U$ÓW.i­@j¶!ØqÍ	:µ-&8º*YEëVÙòXgiF ¿P®¼]CíeìeTNÙjt93nºÂr&(³\[ãÖ=!2	ÑBû;áp¸Úho£_û¥ïnK- i¹JÂÒt4lP]¾R1Nx~,¡x/â Ee3¥e½°ìáÓ`ÑÃ!«/èÅh~©0Â½Â\Å¹·®ä°ý[¦¹Luðû;jæPn1áTJþbÏwSìÜWàpÆf7¦+ñbß7pÝÔåvÕqK¸ßwG?Éàâ­Ø`s2á¸7èþÜSIÔ+ëxã$fóÆjGâ
Zé]ýü¯hÉTÍ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c8/4e5a4e9dee4399f70ad69ef057bc2ec1dead34

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c8/4e5a4e9dee4399f70ad69ef057bc2ec1dead34 (latin-1)

```text
xAÂ  =óý¶@Ä_àÝã²lkÓÒÿÛ/xÌ$#­Ö¥:ê«*¨âg
h|ÉÂHS>&Ì¬FóåU?+©D(rØf)RBF,§ÂY¬÷þj+<Û¾Â«ÂuÓ¹¥¶û\yy_¤Õ¸1¸@ÑS³¬5=þºþ_¾u´æ\¡D

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4b/d41078c237ee2cb94c4ce8054209297bb2b084

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4b/d41078c237ee2cb94c4ce8054209297bb2b084 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹!Ç¾}tÿùôKt\¿²+ëª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ 4B$
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/ba96b566e85f087363321a0467e5b6debc0c0c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/ba96b566e85f087363321a0467e5b6debc0c0c (latin-1)

```text
xmMNÃ0Y÷#e]ÒFì8@=
þfFíéqZÑGöñ{ß´>µP×§ ¢ës³ )#Ï%À¢
ØÀ9|wÂ¤/÷ #ùm«¸¼Ùn¤ì]¶c+t
ò¿¼wc\v)*!Ñ#N1+]ì¡MK¶}9õÈ9"0ZEh¼ã,bÐ{±z©àq1PÓWKÅ0x&iª<²\¿ÿmþÓÏ:qÆÁh ô:D½ÜZ<Ë2}äT@É+1asðÕ*æ2òZÞó#Ô:Q¼¡÷z=ì^_êÝÛ~f¸8Ýµ
ÂíàfCk evö À!Qn@
K4q
¾LbôÝaPÙ6ó®:×o~ Q³,
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/d5cad2f6327af5dd58ee66a802e15d7f88e5a3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/d5cad2f6327af5dd58ee66a802e15d7f88e5a3 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹o;H5WtYðãòZ¡«Úÿ¦¾ª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ *[B;
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/721f3b1692702128f2980dd2639fa24b76cab1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/721f3b1692702128f2980dd2639fa24b76cab1 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹¿=*ú±ÙáyØKþ·uk\Þ¶óD@Õ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá HBn
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/0e9da60efd8f30c338c0292e4d912c93bfeff4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/0e9da60efd8f30c338c0292e4d912c93bfeff4 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó²®<(9A÷>ËÅ\³áIKÜ!
ªR2*ß¾.dWþË<9MpÉúÍ/M ßûS2
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/2a4fa3c4179b576cbfbf37e94dd2fcf4c0656a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/2a4fa3c4179b576cbfbf37e94dd2fcf4c0656a (latin-1)

```text
xUMjÃ0»Ö)ìSã´i¨¶¥ç0#{l$3Ó'(^´»÷Ãûà9ÎN_ç·90
sjáÐL,ÐFÅcD&a$¿¯~ZV-xÕµØ®[úêÞÇ;¼|öÓ¹ÿþèîñzLtÛ!º­OË(A½hfB­BÅ#\i+ML¡¬[Ó5M$ç[sÆüô&W]«î»Z\+)ÁqHËÞü;20Íú¢üý7HX¼<Y
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/bcf37566d0bf152477dc375f5958f2a3c012a4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/96/bcf37566d0bf152477dc375f5958f2a3c012a4 (latin-1)

```text
x½XëoÛ6ßgÿDP×v[Úm)ñ"Û$§/l³½ ÉYÓbÿûîøHÅvÒ5º'w¼#©¬âlE^Þ¼úåhC¿D)%gg³Îýéü$±´ý`¶¸0Ã&Ãç!ý>Ø:M¼±k3ç¯³:£(]ÇÛ
%ï¢4ßVý¼ÈÖ´,³¢|¶©Êè½¢ðæW·ESõVQºÒË²ÏmØoÞÐ´ê­³
-]©v+zÞD»<ª®¾%×ýU¥[¶å×ô¶å»­m+â¥<Ò
ð¬¸\¡B§$71£²¢)-ÈwÂcn²Eþ$ïºß¢<øzë0¥çdøþ-ùç-º(×?à¢\YïvC¾w`ñH¸^S#¬¢,íÑ¯yBòNÉ¨S­¢öª¬_{eNé¦Ls0ºX>/ |ÐpCãðV¨4
Ü'ÿeyXÉÀ³oW8É½9Î"º¼¤E/§EÕ _9ÎÕÕÅ$hTmÇø£°½Î´)ûêë©4îUaÞÛé>áàPMTæ~&ÌÈ»¾TýqÄÎÖ×Äs2Ùaw$:¢«³ìÊ°¹_BdË°:¹ÎmZ~àN-ÿýS¨à
Ç¹B#ZçaË{EË¨<&
ñóÇáÆÇpÍ¹jzS¯ÿâPFèNONý@4ÙWÃ]áúVÇD¼<b#×þOèÎês¦¹gá0 Êã ù1¸c¹4¶ñ+ñZ°4Åí½8&
¡u áJÂÒ+²*¬Ô¦;ý£õN½½$îÉ(¹S_cMD² ÄfZC×éÿ=ÃÅ9_s ¯[w(ef|	lDü$À5ºx®%R;ËD¸« ¶7<Àj>Ú··½ó¦ëkÊG]nX¦7F¾óáLf|3|écÿ§,a¥³SÝ}$Ü÷TòpDþB¾p?ÈyÎA¶½SÀ ÏàÇ	ó|3NCûi âæ
j	¨ÛcûLh5r¶Ñq?§Òúþó¤!ßÆ7|ñÌÄo°.Ç<ö]P@æg>|äË>ã_pÆ¨«*Â´:6± UxÇij>31Ùb6ñùH¤åÙ$SÎV3Ò¨b6Ë\·#Ò+òx1æ£iÿ ~^ðÓ$#C7ìÕPé\-³¿i¤ÛäÞþ/g#Ó=ØbºíÓûÃÿ.cÄÌÌÿT{Dé©áÕréWê¦ÛRHÜd)Kå¬#
îô¥_ìað_KJ&Ò·Ø6n
u·Ëùe÷ó²lä¸4ÒXÎIPïM8Kç0vQs¨>þ0/Äû¶A©ç¸yÇnoë.Ä§6Êkd¬/j1	ûD6YÔÅØÌ'Ìd!9/¿ sÔdaÛ:Â¶­J7«!ýÂ½YyGÓÖpìé"J·É*ï9P¼O³ÑÂ~HÃHTÛÀ$Úîª"#¸/6Û7
×³¡´HdPÑöÞx6k+ÔáÞÅêØòÍÚØºêå(ð±IK?Ù¨$¨5Ø>
%JOh9.k]l9xËY£)
³¯QøºÑ>q³Órö(¬jHK]2&|»ZÅ<_Â)¤»?<Ôü8ÇÚùÌpáLd)cæ8Oæ!XºL:><"2×ä(µ ¹³ôÅôA,+=ØeµÝDY°Mcüð¬Ó/cB8H,8H½÷á©ÒîÉÚ½Iä9*XÏÖ*jî*Ëª8áÏÐVCâ¸°à¸`þµ¢«`2-<¿[Ê0-q;³ØøíÙÚt®Ó-oË  %­x¨wl©8,8RèM©'¤*°Ë/ª\8¢·6²6]£ÓêK÷Æ©}®vé>'¶j`öt½³Úõ¯v¼-ZmÕ×g\,ìæ *uBý0ÝÖæ\°ÿ"÷~WÞûõ¯ FÍ¤L¢3!ê³`¶ôÙ}·æþäeHKæ~ÔuÆðê¡çOÅ%QIìªn}iyô\7³éo:Cn·Ò=ì«váktý/3×+;8|ã¤0Àß¿<ïØ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/dd/ec986f17042d27e98a5d8ddc74d2e9220acf24

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/dd/ec986f17042d27e98a5d8ddc74d2e9220acf24 (latin-1)

```text
xµ1nÃ0E;ûÚ¢EQ¹GÐAèÄh2=äöõÞ¹o|oøø¹.Ë¬fñKÁH >)ÌüxØóÄ¹[S·	+4!#;BëÑçb	Ç(Kò]ÚõYùÏÖ³Yk»sÕos0bèNãmß¤mý»6Y_þ1ësç>×åj uä0Fs²Ýa+*ÿ:Òé¦H¿Åb

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e4/d6a4614b48ddc2f09e3c319ec600a563a6582d

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e4/d6a4614b48ddc2f09e3c319ec600a563a6582d (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹"7ïÈUúðÀØ/ü1s±¦á_¨ÚòÔâ½ÊÜi»¦mM{ÏQl$ÅþtÛ½=<<  >²
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e4/1e35a757d8aa47558aa59492d5618c2e29ffbf

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e4/1e35a757d8aa47558aa59492d5618c2e29ffbf (latin-1)

```text
x½YmoÛ8¾ÏùÂ
°¬I¶[»§ÍÕy©í´Û}1Dk:v`;½uÃý÷#EÉÓ¼­-Î("¢È)Ñî8Æì¤~|øÇÞ÷CÎþî]ºÃA·ïtûçnÛè4F¦ãö×{Ý0YµV©0vpÀ+ÒÆ%vË2ÅÚ+ªRiÏ'ÁbÊÙg?/ÒyMxDqòa&þá'ß=ÆÓ´<öÃ©Þ&´FüùÓò$òäÃ¾nÌï¼D]ÔÏÙýÁ8-®\¿çK²9¢E
VlaG~þÍÊâÛ12ög³Wè~òÇì#so±?ÙçýþÜýñè&/ ¦«~9cÿ¡dò"IÁj1ìW	6y	^êGaÿG!81 Jñ@DTkêÏx9Ê3ïG9s>-Ïä<ªT/Ï!.òÀ{,9É¤_!Ì=H<lEL8cÿöÇå9ýH¬9+¡®©(&9FHé´r?	Éh6æ¾øz¯So^zá¿9º©ÌÑüÐEöÿ==hyóÑä9ÞµW¬ÛQ]	wÁuÉ*eDÜÏit×¾èv/ï!rÒjmmM {1lïOüäT¼ÜàÀó Ý3lXFß¹0ì®½ägÚ¦	TZÝóÇÕ'réæcorÏÓS&;¯hfÓj´.
çÅ&ZÍËlãÌÆÛawh¼[³yh'[ø+[b¼VKmQ´ãOm.ñxO6ÐLÚp	áN)ÇQê¥zÒíÉùSÈT½¸eÖyÓmZ]½@jKnyfÐãÿ=\LÜÃíÁM_Ï(£! ÏRO(:§«xNº2	ü<ÐÂ#8åþWµU¸»×SÖCÉ0Ò,øÀÅ[G×8Þê¬^×byàÜä±<Ôffä µÝ ÀEaÇÅO >ÂánjÛ Ô¡¾Ý+½P=y>£Ý0,oô¨?C<&1Oxº	ð¸iÛVÔë¬öQcÒã.~]MG¬®§®)GQD¬Ê¹4Ä+·Ìªê1 +s1¯£¬±t¤!Ò%t1õ£E`ô«C$|.1jÂÖ§5ºB¨ä±rÛ 	8Ø`ä¸MS¿¶Öé©.ñöó
,ñ.FvsSkÖB@#3 ÝfPvæxzÍËÂiÿÝ[©+4hkQðr{ucXÎ7XêÑ÷´å©a·p»WÔÜPc%H·à(k[|¥bâ
v4\ÉÒ¾©HtWÑ°Eú@uHö°%öE° ­AMM[HAzç ÿä±P®p-óR2åó¢¨%1JþhjBº=ìØFÌÁÞE[Hü¯Ôßú5®ÞýÔ@osXkè3²Z2:zR× ×Ñôö@º±c`#,ñêRµB´Èc6Lá¹ÞÙ~²:³ÅK{÷9$ÌYÄªxµx
JK8O¨,þá±.fOÎéåäèzMÃÚNöc6­ï"dý²=ví^ÁA¯àáBû­	oï3ðHmËÂÕx;ê·
Ën
,Ö ÍøÚ' 4=9$díK¤ðyHëÐ.#ðÁ)@JÛ41ù³´VI£Ò"0GÐùH¦VÜDÛW0¥R,pKã
ÁÐ/àCßÁFR(D#¨DA=YpP8Ê¡æ+.n»{ÝmÃî!K¯ÛÙë3¤O[jc+@8 6ç1ñ
 ÖdAìù	wGx¶Üö·^s`nKxLÀÈKc^¶¶OMEü
;;JCØ¼"¶§izhäá>´Z}<v´o&ÄàÚi8Æ»BlÅ¨lÉ±"cÒJ/s@ÎåÜ4k;
Èa
Bh	ÛWß9Ä"8·×~#ÀÊ]ªør (PªÏH3®Fðý8Ö ×Á#¦ÅÉ=fvÕîÞpc¤k¨UÌg.Ëõ®ï	åAR\}ÔÝ%Ò¿;UBþÆ6 ¦Nµ"\ÔùDÍGjN²ÔV`´ûoÝ'óà±,¡óÞJ¢M­Jh©9¢¦®É ­:£Ç·Í@M¤ÖJ/ÆV#4ÔÈ &Á¹üeÇèPVñæÀ¾ÈkzòGÐ.B	®Bìd:hÖÊlëä",¢]Oj>YÀÅ*}Í	è´¬Ù2ÒmA-÷z`ºù-²²OVê×?jéótÍ«YU)`²¬ÅJ»G¶¨º-UukðÜ§
q&A îQNeÔ'UØh(S.w-9ÔæÃr-	ìWà±Íù²"ORÑÑnÃ²òë7%àíþê87
FYöKæ-Mquî(µæp P)³OXFK;¡G!ÐÀßÇ`0g
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0d/6a245d96d0e81fbf0304a584a3bcf97e47801c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0d/6a245d96d0e81fbf0304a584a3bcf97e47801c (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹>ËÄv;E]_]þ°]ÚË¨Uª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo zN>4
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/32/d712ea64d4b69f5dd9420f2159fac3d9542fa4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/32/d712ea64d4b69f5dd9420f2159fac3d9542fa4 (latin-1)

```text
x½YëoÛ8¿Ïù+6`Yí¶vWÀI6WçQÛi·ûb8ÚulÃvzëûßÔÃó^W\PDE?R$E§S?ÍOÍ?æôÎ(ù{påGý¡Ý^8]½§MÛntçF3H½Q«R­Z­´sÕ1
¶¥qLØz­T:ò¿SòÅ¢eZâpF$ó4ñÎ4zx«ó´2õ¹Ü'U¾}Wè
ÒÊ,ÓäÃºoJÜ'oDUÔÅcuw®®?ÒçÙ«á2+ö0E¡¤·²ø~¥òbñä0ßKRÐü$ÜæÜ[äOò¥üÃïÏN2s}`júùù÷E$³_ÌâÐ÷7!?KpxÄÍ(èpS/*ô{à|Ä*Ù"¢ÆXSoA+iXY¸ß+IDé¼²Hó¸V¼>MÜ8§¾û,Xr.3ÉÜ¬ÅÀ³SÉ^ÄgìÝßÓ¸ÑØ%ÈúÉùY	uU¢,Ä!¥óÚ)~)$$ÏÂEúÌ}ñõ^n®¤nT»Á¾9cº?s/ÐüÀ]°MÖwV;n#=ÛHwÃ¾#8y\W,SÅÉcD½g;Öe¿g¿ÈJG[Ê&4"$rc8ÞxÉ©:ù}}wJ}tÏX3õ¡}©[}kÅ'/´M(-4û¶£.ä>RÍÆîì¦§D<¼¢mSë\éöoh¶¯²3´·ãþX·åðÐÊm¡¯lþ
vy<hDÑ?y0P`yO2QLÚp	
àN©Äaê¦jÒùSÈT½¼'æEÛi}½@ê
$nQL3èÅùÿ.ÂîáîèvÈÀgÉg)×é:ÖiF&§a²:gðÈÎé7£uenÁµÓ´¡(é?pñV¢0ñðºaå­EZ-%Vê&ÙbSYCh.²;n^Ð|9æaû 4^¡uÕ½PÿørÇaX=èµ¨¼<'1Mhºð8ißQ´Z¤ñIaRã.~]MÇ¤¥§ªÉaê.É]Vå\
âÇfÕÕPÅ¹×QÖX:V©Êeº{á2ð±úYHÍBIÃaÛÌSKª:yìÜvh2ØNÛP¯­mzê«a¼¿^e2=ÂÄj`jãó
ÓVht¤ÛÚÎÜë×,gyS¨öwîÒO¦AÙWÜë[Ý´¿Án\õLKØêV×ðñ·|ÐÙ¤`K[G|¥"ì
v2ÞÈÒ¾ÉL¸è¾¤áô|àrÔ¶ÆØ°.{i,>t¤÷8áÔ¯!6êÀµ n£c\	¦|5µ\Ì¥¢ÿâ4¹-!ÝÀ'|°ôOÐxë&Ü±M`@âß|øÊæ{F¿áv¦+w?9QÇ"öêxF-'¡k4ÃøéÝpcÏ2ÀF$ìÕ¥1rÇÐæ¹ÞIÙOIXc­Ãã¥À}øÅ4¹Ã@æ"$u½Z¬RNæ*óÃhìËÅZ^MádÐÖÍ}Éakpe~húð35ü$ÆÙòº­¸áR³²èAF
2_á|¿þÈós>8Ó<¬ü²òÆÈðÂR*§±ý[÷
O8Ã~bóV¶ÌDqyÈ?3	QPº)%³LÜ<îòuDÏdâÈ¼Lu½i«b8! qöE`42X¶øòÒ8FNc6(¹ó¼ áL`ììMNÃåA8±¶&tÖê(%ìvÏBùJã:&XAûh]/¡Nòo
þ»Àú6h}áo¼ñïàD@í×MEü¾ÍJ;_æ]~Ôcc"j÷ØìE5Ò¿vX1áÜo»º¡Ûú»<ÎQï>lr=ÇÒXPÉtQ£]¬	¥"ÄrkðçÛt5vºý~W.LíF¼Í07¸~=ß>
\%ro!S{{g?Jm0ÞÎ\<pë¨Û/¦Rgüñ@¾jhzÃ,Êôþa@.~r(t%bÚÃª£¸zp+J=/¦¬<D8`
 ôVb=¦F%è=Ñìô°À#*Qð{pJ+ªâ_@%¶eàòDÛT.©¡Å¼'{½D$U¶Q}P92~áW¥EÙÈòåÀKg#µØUË\Ú2rÀJ¢ ¡8[5	ÙqnF_c°'ûI^ÐêPê:¿ åª¼ ð²â%d#vÈÙ!³~Ù,Ìî¹hG=Ø¬ÛÉåÉ6B¢óÃÚ
PAã4ËXÎ\)ÊÝUÑ*4É;=çÍú2<"Í4GâIíÀq=?»"ðî°Pså Hp½)f<_Tö½ÏEy«òå¼ Â<ûw©w­7jþþ.Í#
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/32/5b16049d4db2501db7238efaf935da87b75a3c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/32/5b16049d4db2501db7238efaf935da87b75a3c (latin-1)

```text
x+)JMU047d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe"DER~bQJ1CèÉmòéBnK<e«­îä¶]<jh``fb¢T¢WÃàîùí­°~fÑßJ<W&ÊO
mÎpòêQ¿òºïT7én¹l~¢ *µ £²aí®O['l¨{¥2»¡ëYáe-N 
ËF
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8b/b74967cbcd99fcab362272d6a7f5f37df14ba6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8b/b74967cbcd99fcab362272d6a7f5f37df14ba6 (latin-1)

```text
xAO1=÷W¼,veeÕxPÀ@ CrÙ´Ý×¥°mÉk÷@ÿÄ7ãm2o2#/ávðpÕ¡?ÈÔ»©Ê ¸)î`³CØ.f]ä"ÙFOõ`½½ó¹Qèòi.ma1Ý0&½ ª¤Ö9¤RPRGz$_CÂy§¹Ö4§§·Õë}|ÁëH0&cÆ©¦­0½þÜUùò¼åÚ+o­wy«þÅé++ýP+j£º9ÿÑðså7z×ynÞ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4d/2898af9cb19ed9edcac441bc50717a73d1c1f4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/4d/2898af9cb19ed9edcac441bc50717a73d1c1f4 (latin-1)

```text
xµ;nÃ0DSëìäòïa¸Ø±Ë¨U¡Û[½kO9ë²Ì¢ ç/iÌ
Gäsrä·Ù1@6B® BÒÁënÅÆOQÁK:¢×GÔ>Pt">ÖN|»ÜkSÿ|,¸~ó4KmWªrS?Ù$£³ý;¼ì·mxÖÆëãþf¹ï4uùU&ðÆAÕë3ÝÙW?*éd_
bS
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/dc/42e850b6c4af05d2460326d108b38d6299dc19

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/dc/42e850b6c4af05d2460326d108b38d6299dc19 (latin-1)

```text
xÍ
@E[ÏS|è¦B´3Jò§FÑfÀñSdFÆiÑÛ'­ºÛs9pÚIµàÁÆ&6Dj~i1¶|ëùÐâ²"i´hFée}Ö×øîä£\ÐÉ:Fôõ¬!6!\É^p¬B3D,ªh°<IëZ¥&°4rÆöÆúgÝJB]E¬¤iàí}Ý²0üé¥Ùéü]üÉùÃüá}N
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/31/6630a3e490f76f2d4107a928d4eecca5ad36af

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/31/6630a3e490f76f2d4107a928d4eecca5ad36af (latin-1)

```text
x­Ko@»æWR©JªPÒ¼êM»HEÕ1®GÁ`ÁX-­úß;÷^LvQ!±áúãÌãEÕ,TraÎ_D¯ÿQïmßÚok§ebªûu©¾Þ}ôj×ÚÅÎ5mç#?úð%¼µEYwex³,kgW¶l/ÕÝÍ=¡¢ xië¢Ú-Ku½]÷-òj^å}³sÝ¥ëì,"õ+P¾,ËU¾«Üpùò¯ó!f³Í]T¥z§~nN÷èPÐGWd¨í¶¾1¬ó
Gßò½}ÀáÚ¼îVM»ñ°ëW{cëìIèCÙwJEÿ)ß}ËZPÕS¥ÚÆñ7µã-©næyó½ôyî\Û)Ç|øØÉ[õNÆzötú!1$Ã$mXË¨Ïâi&
½:Â4eLò]Ê#~a2Ï ´ÎHd;0	0w:iÊÈ}"ùyós§Ä $Î`
X3X¬òåláhâÖlQçÁ{¤c&q&vÄÜ« Ö¸
D»
"ïÄU$I5s]ÅÀ\E¶WhbW1W9£ØU$ñ½ 1ââU ^ ÑÄ^ÈñIñN,AäïÄÍYªÍ´=Ó@2²9Ï4mÓ$DÒü0 ÒqH z '´ÏLâ	:G$yÚ;ùÛÐ;±âÇúyïäô÷Uà¿ qc}
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/31/3ce3c3c546619ec100bb5e52dd6e4713368c9c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/31/3ce3c3c546619ec100bb5e52dd6e4713368c9c (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLghÔU³ãøâ5½^K§Ë>+~ QPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú »iVÎ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/30/b24cb3715e60b9de8b843eeaf55fa232c24e92

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/30/b24cb3715e60b9de8b843eeaf55fa232c24e92 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó6®[P«sSùéìCyIZ§+ßë¶](¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} a V2
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/30/a3370e84e47cb236ff92995e4fabeb562ae341

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/30/a3370e84e47cb236ff92995e4fabeb562ae341 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`¨µgµ6ä²Ù§,¯kÕ_®n_U[Z\¢WÃ0m×´­i/â9¤XÒn»· È¥BO
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cd/76c23284b685c4fa1443238374c1f44e176467

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cd/76c23284b685c4fa1443238374c1f44e176467 (latin-1)

```text
x½XmoÛ8¾ÏùÂ
°,I»uwÝnØm®NâÙN»íá$ZkÔo°Þºáþûz±¥4M¶[oFI=¤(Qî"Îä¸÷úð·ý¥|Îl<õÇÓÓ`dZÆÜöÉìÂ.ô{=Bº]°éµvxC×f&¯³è÷Z­(]Æë%o£4_WÝ¼È´,³¢|±ªÊè¢ðæ×wEwUuQºÒ«²ËmØoÞÒ´ê,³-_\«vzÞFÛ<ª®¾&7ÝE¥[nßÐ»
ßÙº(ö(åYV÷dÅÕZí$¹
XAMiA¾s-ò'yÛþåÁ» \1(þ»7ä7è¢\þrYdq¼Ý
ùÖÅ#árIa°²´C¿äY
ÉG8%{ "zLµÚ©²N~é9¥«NR2Í^OêbùAù áÆáPi¸OþË<ó°[ç¡I^á${sEtuENN(«A9ÎÕÕÅ$xT­z'ø£P¼Ì´)ûêë¹4îTaÞYé>áàPUTæ~&ÌÈ»>WÝaÄÎ7Äs2Úbw vDV%fÙas¿È-Ãêä&'¶iùw6¶üwÏ¡r@24Oä
0hi,ï5-£ò(ÌÏczÃ5§þé½üÇØ2Bw|zæê@}5ÜE.ohuBÄË#9pá¹éÿtîà¼^8ÛxêóÙAP}äHÌGÃÊåÁ ôÔ:ã0 )ïÅ	Q%¤®¤)ôNUa¥nº1°sÿh{§^_÷tÜ1Ã®F"YPâ0­¡ëü¯F°><]NøZ2w y½åñRÎi&!ALà â ×è~â¹
Gí.á:®8Þ°Õr´ß<öÞ_®ÿ¬qP>ê*´ðÀ2½!áë{N.91	Ê].ð¥)vYÂ.5sg«ºû(Gsßc)Cò|á~P4ð!l{gAÁÇÉyA¹Å§L ý4ñðµÔí¡}.´qvÐq?gÒúþË¤B¹oøâßà06]yè» ÂO|àeÉ/¸`PÏUaZJN¥
F,@uD¼ã4µl6@ÊøòÑL$Òòl©§sO«iÀ(ªØÍ2Áí´ã¼$cyÅhÚ?À #1pd¤Ïñð~Ã¬J?äê¡8ûAºNöîé|20Ý}ûÃ7`AÚb)jùýãþ.ÄÔL_KnâèáÕ¥ãx¥ä',FÉómÆq?5,M
VK¢Û÷XÀÅÏö0¸/%')Â·HíÅÈ¶ñ¨··+·»+yWrp!Îi0wö >¡ÈøÃ°AYàÓàã<×õ|p6Z°Káº3q°©{Ç£
9»à  Më2k¦oª*¯¬ ³£më¨î+éGîñèÑ´5 l"JwÉ"÷ô
ïãd0³÷í¸#ÁvxÐ$ª}TFÑPÌÈ½m ²s'ðl¶=PcOcË7lÄÓVïÏ,Ë¼;À#Íý``â>pr\7}¨øñAbk"Â7¾SR[Þ|9§®qa¶ÚåÜÛv¶hú~ C-Dù~ÿRÀ9jñj~d{OY¶a-JÊt1qv4 ¦)S·I¥Ýa¹&ÇÕ³³Ø¿§¶?§ßu²¦;kº¬Ö«(Öiß÷fQ|à6kt
­©áê¢Øu[»Øj¡é° o0
ÝQÑ]¬¾R"=íEUqÂ%yØ\És÷
P8ì×æQQõ
l)U`Zâe¡K]QÑe¬>¦HVr·Õ.ïÊ  %­:©³AõÑý\	¼©P.¿j
«¸`XÐ_vÑo¬>
$¯Vº7ÎIýÜ6ëïÕÓÈN5x5ºÜºkô9Ò§hxVnã¸¬ùÅ
m_þ?÷@b«)^ó'òÏ.ý®Æ) _mÉOæ>k=µôÑ¯Bu¡m_'o·z=ãð$8%Á¥£Í¯¹)+¡gu'áí¦Anç7·Æ×ÿ/sÍ¡ÒàË§ÿVõB
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/33/e29db8b7f602187dc0ccd06829c3dd7361a021

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/33/e29db8b7f602187dc0ccd06829c3dd7361a021 (latin-1)

```text
x½YëoÛ8¿Ïù+
(6`YM»­Û
ÈÃisuµv»/h­QÇl§·n¸ÿýHQ²å¼×gDQäIIÙ$&ì]ã¤ñÇËÿæýÝ¿tGÃÞÀé
ÎÝÑmMÇí¯
÷ºi²Z½Ze¬Ra§Õjiç»mbIýµj©ôÒ§ÁrÆÙ'?\,ÓÊ"¦<I¢8y;Kÿ³Æð/îãÊ,-Oüpæ·IÖ¿eþÀÃ´<f<y{§¯ð;ïÁß$Qõc~_¤Å«ó÷üqEö*G´LÁ=LÈSÀ¿[Y|;AÒÑ|þà
ÝÀORòýddsî-ö'ûtôÃ_¸ßÝdêÀTgµÏÙ¿QD2ýÉ4`³ö³Ç¼é/õ£°Ì¿/¢P¥ø "ª5õç¼Få¹÷½,8ç	rT«ÃçÂÎxà=JdÒ_!Ì?H<;ìEL8cÿöÇåýH¬~þXB]©(&9FHé¬z4§Ñ|Ì}ñõF-.§Þ¢<óÂ)ñQèFvüf~²@óCo.Ùwþ·´Òö	3£é=s¼ëlX÷RfDv%Þ×$«qr¿`¦Ñu\û¢×u>¿ÈJ»9²µEh4bláÅ°½w<ñ3}ðûÞèQÓ2Îa÷ì<Ñ6M ²Ðê_8®>ûH7w{Ó{1ÙyF3[V³}i8¿m¢ÕºÌ6Îl¾õFÆë-Fp²?³%Æ3ØaµÕö E0þÔÆ@9tyå=>cÚ@3iGÂ%<3¥G©êI÷RNìÌBî êå-³Î[nËê	ìRG pËbA/ÿoôp0qw7>£G<Ky¬PT§kX§]~DÉNèÄá	ñÊkÚ*ÜÝk')kAQ2L¦4"~pðQâãq#Ê[5Z¬ ÔMÉcmFaFP?dv\¼áøéPß¡þtÃ è®ÜèÚ»§c89ÃêF¯íDíô)ä1yÂÓ](ÇLû¶¢Ñ`õ÷wñój:a
=8uMÁ$Ò ò Hî²*çÒoÜ^0«¦Ç®,ÎÅ<²:ÄÒHW,ÓåÌa÷ Ô,Dð¹Ä¨	Ûf^jtpÇÛMÀÁcÇmú±µMOm5÷×+P°L&@Û­L­XaÚ
PÎtÃµ3wÄú1K,/
Õþ·RWhÐÖ¢àÕKîÕa9_a5NªOßÓ^O
»sØ½¢æC,AºEGÉØÚâìx´	¥}U38è¢aô¡ê$µìQ[ 6í.`AZô.ÎAÿ#Ä:pÍÛl)Zs¡$ è¿¦)¤ØÃmôÁìÁÅÛ°rÛ±Sóá{A¿&B+ÓÂÛO
ô6w
}FöQKFÇA_êöûà0úÞJ7vmlD%.Q+D<fÓà%Ì5=j¶)^
ÜPÌ19dÎ#VxÄÓbp*PYýÃc7\Î×êôjrÆýaíK§IûqDÖ>²Á{Ù¾vë^Á¦bD!Ã~æ.à µer,3GÆ"W³#íÑHÂLx³è¡ààÒÁ)ñà§!1n@»VLÀMùR:¦¥´Jâ}ù<ÎG*}ÔS°XûJ¥PJc 1®°A0(`Áv 1ÿpÁ$õ$Áq^p$aJvñ¤SâpºßííÙ (¤/W[%dg+ ØúW6ç1Ù
 ¶D~ìù	wGxA{Îûk¿54÷>¼~!ú_iìÁã`o»n*âßýVóÕxÐ1,»=´Ô <MÝ9}dµ²D_Ú¢ÂrË«añºù{A*cr°(M4äËàs97ÍÊ¸ËíÃ-èÀÀ°?9·×~ ù@§*>¦n{ãj¿ç*nóàÃ.ù{v/Gn§wÝë@-ìýÑÎ`×`«°Ï+ÞÞÚ
Â¤¸4©{H°º u;\Øºµª°¿û÷Ô|È²[]k
?QÀ±¿ö©Â ¾Ë³;ï®õ¡DdÂV#4
jN¨9ÕÅ	¥:£[Ãæá*¤.^2Dyo#QN¦­Nh$D9:V24©+~Ñ¡´,ítËøÐvyâ@Oq$RýÆÕî¶l¹ÞÑ9t£u_êçv!y÷-Ö|º1ó-%¡jY³g¤ÛîõÐtóCde¿T©^ÿ-K§^Íª¾ ³¤e-^°ûtÁmK]¶WoÅãUBÝ;âÆQó^¢P:¸|G2¬s×êjsÇá--	(I²ÕÈÜÝíp³v5O­_¹£(u¼3(ÔË\9õ·6²ì_]µy\;JqÓ|ÜU
ãì%,£­f¸Á£hàß±-Â
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a2/b34081a82026ec2099509746133240e19d68b8

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a2/b34081a82026ec2099509746133240e19d68b8 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`PÌMûmær7ôj©¦¨pçÜýo jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  º@ý
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a2/e1fbe63c1b03aa09eb5fffa3f3e78db7ea6793

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a2/e1fbe63c1b03aa09eb5fffa3f3e78db7ea6793 (latin-1)

```text
xM½
Â0 ó]TR:uQcöGh»¸Æ(Ô¤´ÉàÛpÓqßwÝ`;ÄÉa[8yPjDûpj5
Oë'¬ãmBÄÒ÷¼!§²¸.ïùUsÆd1vµÈYÙÔé>	3J	PûÉ«õËèZÓcVýËm¯:¯a½½Ø¿©2+9O?äæ4Ú
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d8/73c55a82bc09937346a8cacdcb087ef289715b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d8/73c55a82bc09937346a8cacdcb087ef289715b (latin-1)

```text
x½XëoÚH¿Ïü«FB­T
äyô"0	óm¶_,Ä±-ÛäV÷¿ßÌ>ì]B½Vç¬wv¿Ý3ã9>:iý¶· wADÉá7Fî`táõÌ¾1µ\o8¾1½Ã"íýVf·ZµJ§k[Ldÿ0v«VÛ¢y¸ZPò1UÞLÒxN³,N³<Îo4yxN¼1¢EÝgM.Ã~ôFyc/höáAÑÿ)Ø¤QUõmùØåºäúú#}^Ó½Î¯rðbSQø«¥÷3d¨ÕË'¹èAÓ¦ä;á>Ñ"õoAâ}}ö²¹Ó>iÎPE6ÿÙ<Ãp³ò½Güù
?â¨A¿&qÁGh=-ÆKÚÈãÆÒÿÚÈJeG­äÅô9ôAÁ
ýgÁR2püiæn-J#[sipOÓFBÓ  ÛÇçg5´Õds/Z§ø£<	hRp÷
ä×{)ÜÈý¤±ð£9}sÆl#;> KÐýÈ_2!ç!¸Ë]?ÉÏë'¤·AnOìJÈ¢¡Ó4Ë#Ãòä1!Ùw=çrÐwÏßCæ ¥kLEæ Iü¶÷fAvªN~ÞáÐÑÃ31lsä^ÎÀYÉôMQ(=´®§.1RÝ¥þüæ§D¼üB7;¶Ñ½2ÝvÑî\go'ùîÍC'(÷þbOÌ_àÝÛNè>`þÉëÐ£^ïé)Q&K.£ÔFç~®º=±Py~´³¦W÷Ä¾èx{À°k¤pAâi]ÿßè¡V{ãÛ_P¦@^y¼¡ø=ÝÆ{Ñ¥KçYUBç,Â}
æ´­Háîj¡å¤iiYðÂÛHâ,ÀrÃ®·Ã#rxBõtY³µ¿-¨X`­MÙ¹_»ÙÚWTØRÙ^Ú:ÜÍ
¸ÂVûDÁôÒØÑnÆÔ¨2å×ñcb`#ìñÊÛ÷býåqæ,o´¬ºóWaîAÑÄ¶¨EÅëÅôúÖ´ÝÏ òQ°eÐtº¸¯×|¸åÉDns+u¼>bïFX«<läBuå
N¦\÷@ÒpDúX¾p=Hê8.l9} 4zLÒûpÁÚO	[`[»Õµ®W¹ÎÊ'×s)U î¿8M
°%¤[ø/9ð
J¼isÌ]×$~áÃ'>°è3ú
't
[yêÃéßðñZÛÄ f
:Ú
cãáBÆ¤÷Æ"}Ç'd³.IK)ÁFä±.¦ÔÃgbtyÊhÜ?0A=<d t¶ ÄÚ¨ô£U ã¿iêE«åÖ2;¦½í¸ìH]ì:?úãý.Ærý¥»(qi8E!Ô&¹gßrËÄ\¡unRWúSÁö¨VðÉöXoP6?|i^¬Àg­äeáÑ/Î´<0òóä+×o9ÇG6ÌYà\¿õÛaRa E4djÐ× åR%§á\="8/o&	õR.£©S¤\)F¯õ±`¨|aöY^s¶z®ãIÓì¿õ©dÔË¡S	·Ôçó°3¶¶¥=tÙùï Îºs¯Íäâxû@»xÅÎDc¾ãk*®òÝ«ÉüÔÅ«GãmÏ´L×|W«Ã_d<u½×ÎkÖé%FT§'RDÊ5ÎthøÊ*²mH½°³7uÔëC^#[Fæ¦,7¯§ðg>hÓPW-$ÚÆÛ[Ø¿µWc8©Hh®F¢ù(È·þ0{&Tn¢cjwIæ»h§§?ªLâ,_-Ø[E!þP¦ôj}^W8X×¾|´EH¡ó}¬8úÐz!(må&á¨Ïâ8c¾óìbÜ
SEeöñÆV`ºcèTÙ½Q+Â¡BÂÄW&A¯VÏ3/¥ÍÔGòn¹ö«BëØ¼Ó8FQ	ú¢2ô¡RH¬Hv|Zéúø¬¢bÜÄ»3MÞrv
w¼Àé|cÒë
»²0²Ñ¹ª{»ÙÌ®w3¶¼²6BP/eY÷Õoiu×}¹*ë¾«lN ÄVØeÎr[)í¹îG>º¬ó,õÉE"óÝ:PAW6hy_Q¸xð°}ÓC©Ârå¼EãÁ«Û3l{,>Å~¤Q`±²ò$è Öfââ)oÓ5;-%ùº	úm^üCj]åz/?áí_vh¤
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d8/ed0a5e9b13174c6f98652ad23bb322ed31d83a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d8/ed0a5e9b13174c6f98652ad23bb322ed31d83a (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó¢S«Rw
NQÕ¼%|nÇ´»ò!
ªR2*ß¾.dWþË<9MpÉúÍ/M ÷bT
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b7/b4db139f9739b862e8cca5f6d06597466a3a13

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b7/b4db139f9739b862e8cca5f6d06597466a3a13 (latin-1)

```text
x±
Â0Eó
¢B­-¢`ÕE¢ÁâRÚäÅb"ÉëPÄ7Þ3Ãmµm!]§£dÎp´ïÁ©gG0å3ÈÙ
ªáQ2äTÛu>·ëé_Gã1.RR¡ÛBYTÿ«±±2\÷!Âuã»[gp!È«±@ÙôjrñÒº|q«c+¥G=ì6}sö4%
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/04/2e511ee39f80394e02fa0e70b42e45c9a7a72f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/04/2e511ee39f80394e02fa0e70b42e45c9a7a72f (latin-1)

```text
xÎM
Â0@a×9Å\@Éÿ¤ â	Ü»N&µ`¤éýíÜ>øàq«u`?.ÉÙ õ8vÈÅcaÌPNÈs¦fE}©Ëg±Y;õ!óÌÑÅhC0!OÑEÑ>^­Ã³íT®,-¯µÝJëûÂ­ÞÀ`0Ñ'LÎÚi­zü
ù_ª±
ê·dBØ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/36/a6838982efe509744cdcd18a32baf78a644842

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/36/a6838982efe509744cdcd18a32baf78a644842 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`(i¼:ÛïÓ¼¾÷¦cXe|m9gTmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ ñ3Bì
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/36/029754b521895d02f0a1a092d9e451f935191f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/36/029754b521895d02f0a1a092d9e451f935191f (latin-1)

```text
x½XmoÛ8¾ÏùÂ
°,ÉÞn×î
8Ýæê¼ÔvÚm_'ÑZ£mØNoÝpÿýHI´å4MÚÛpFE=¤Hî<Jæì}çÃ»ßüksöetæO'Ã±7øÓ2f¶ç&¦aØ¬ûºÓa¬Ý5ÆÎ%nß±Å×ïXÑí4a¼ÖKÎ>qº.Úi,x'YþjYäá±&ð§×wY{Y´æa¼ã«¼-×ß¿åqÑZ$K¿ºÖ×ÍùupnÓ¨«ú¾ºiÏúÊÍù~·¡{S"Y`Å¡4	ãðïÞ,»£@£¹ZÝúÂD?
óÇ<c?´¹òû}l~SÿÛ/^³îñûçUä'¨ÈYEÛÕ°
8<,ö0[ü[Äà|Ä["¢#DpÅ[EÒZßZyÊù²µÊQò]§C²>o |páGÁ©¤Nù+4K³V·
ÏÎMö"8³ðêg­gaB »ï¸W[mT¢R±ìâÆBö"Y¥à yÄÁÜg_/iq«ÒÖ2üÙØÅñYyæÇÁJ,r¯Ã¯E»¤9³Å
ó
¶¬;PÑSwÁu5Í2"NnRfç»§CË;~	¾1uµEh´ÅXdp¼×<óCøy£`Î#tÏÔpÌ±wjºCwÃ'ÿÑ6M!YèON=_¨|¤;ÏÅ
/zùfö£fz?m¢Ó;+Î6OSóÅFpiÿÅ¿À§OÇFÔmÀø£rèóË{vÈ4B3iGÂå<;¥%EPèIw &væO-wpëõsNz~Ï
ì5Ö@@¸U1-¡×éÿ=\LÜÃÉåX/9³) /S+¬Ó]¬ÓO&Á5¸Bô£¾ïx)áQÊ@3¬£ÂòXÉÇ3Þ,{ç¦ã}Õ8I~

,X¦ÛÇ9|=Ã¥L±ùdx¤ãáoY&Ùt«ªûL3HÌ¤î!ñpDþ^¤dõÜi_@¶ÝSÀ Ï+Ð|K2N£öSAÄâ
b+·ûöªæE¡zNIêþKòhB¾oøâ#°ß ÄÜ÷@æ9|ð¾à_HF¯Ü«È8'J+úzÇmJ>#µÙd4Éùr¤åÚ`¤gn-fhQÄ6lá¹º#Ö
ö¹S£/#¦&ýõ¼¥«u%yßK¶ª^äÊ©(ùg~¼^íÍñlÔ3}ùáp MuåþýCâ #Ñ5ãßÚqöÔpËPÂyÒG²»éÍYbúxòXLÛôÌR^Ê1¾WÈñB<ù[¢h\ø,¡µrÕÀ¶± NiD/C²ÇJPQZR¹çDRçôÄM÷~#EÇròð Hð© JZÊºP«G8Id½ä!­gÒUáBJÁ­Äãùåô`\Æ]µz#H4V:dàùàÙÇ<¥a£,à<&d
ÉÉaÎýün5O¢=·ûyÔØû²º&HpHydîCã}Ñ{¼³©ïÚ"aPbeI9Þ¦7
!­µ"«Lødç÷l(PÁÚäW0qóñCY æÔÉ ¥B®²	ßdÊ°&uÂB'NãÂl4	áÌÝVk6kÏ]Gº-äÍóüÜÓY§ÕdRX64
éÑtÇe n "WÝ£ØÝªã5RÍc¢úkü¨~Èïæ¼X/ÃÄ_Ç~#ÞyÁzð±gÚâÒ«(¼¦*jwR7kMn­éQ^BwXpn1ªÆêja¨ÜÓ'I%4ôB9sê5 Pí5
kõè(M½Û@S¥3LK5[ªDøp­Q]3V]DARám4ó»ÜÏxÎd6Æúì~ª²Þt¨=Gv5U5Ü.»ºm¬.2O·um¢%û©m«Í£mÊQ¤ò#ï¾Ø6õ/e:"*7!whsÕ¬ÄN²Û-A÷ý
·~%ÿ_UÔRM-Ñ²¥ Z¬ªØ{þõüâÀ©QÚ÷@Ý|4óD¯KVVí
!Z3DÈêÊH«[nV:o -~Ý:<×\[I|\°}Ãq&êÛï)MQü®H;ºW·Qo÷¸iävº®ú÷9*/ÿyæ}íÏtþþ	ûñ-
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d9/655ef0620e03df29cb07910c70e8af9e7c9b0e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d9/655ef0620e03df29cb07910c70e8af9e7c9b0e (latin-1)

```text
xÎAÂ @Q×h(Hñî]2ÃPJïo¯àö'/ùÜj]¶0FÑS	'tÖXqbÂäØSÎ³
LÕ7uùM<{@&©d@¤(.
)RTÚÇ«uýl{×TE_7YZ^k»/5­ï·zÓüÁX}6ÎuÔãoÈÿRmS?:öC÷
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d9/e4744a68bf4b9c322934be7708851552ad0bac

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d9/e4744a68bf4b9c322934be7708851552ad0bac (latin-1)

```text
x½XYsÛ6î³~&ñSIN¦I¢lÕÔaRr%!6Ç¼¤Ü8þ÷îâ"@®_Ê»Øã[pwiä+r~Þ÷ÛÉ~3J¾M®Âùl<]§áÐÙKoNf7nxc{¤ÖëÒí·½^ç¨JàøS9;'L£ßëtNâll7|³b[w2_ÓªÊËêÕ¦®âOÀOZÜ=ÝMm­âlg·Uë°·EhV[ë|C«WwºÞÞEñ>º©é}÷>¶tÛù¶OyÕÏÑ6UÞ®P s¦!!Lâª¦-É/ÂcjvüI>þðÇcX­£ÎHÿÓòÏ4Q­a¢Zyì7C~uàãh½¦à#ªã<³è"Ï`sºd|ñ­ãZun¥Ñ«*(ÝXiÅ${=)éñÒ74H#Àmò7³ÌÃJCNÎÑÉ9Î2¾½¥¥UÐ2ÎÈ· ¾ºÂJA#¤zÓ{/ìu°A«B¸/ ^Je«
kekúCq|6qU`øY2¥à.þ^w¨¨¯ïÉ"*ÈpÞÈx¾JÂvWÍí"KåÉ}A<w´Ëñhñé%dp{½B%ZlliÕS¾'¡Å|$ÞfP²V×Q­Ç|"Â7 £ëí-ñ/áÀ3ìk(BÀoøE.+è&ý£:$¬Í
g§¼â,çAFØ ZºP
yÀw7@r)Ð«£mR]Ø?õÛYwýÙõ_Aå£æ8¸Ók>|æËTïsÆBÚ8<b#ìÌXÎ÷J¡¹¯r%·=æ<äÌpng`î0°^p9È³ùðaÈô?ânP7à°j@,qÏñ®P³î/.KimÿÅmäx¸À@8s§×çhÈüÆ/|`;Îø71P^ê2Ê*IécN_st£øHL³Ùd"6k8QcBãé202Ä0"í±ÝÊá("§IMÞ`n;<?éghç5ß+0æ¤ÏñøàÌcö2µäÓ2Ì¶ée0]N®´Ä¦¶GÜÑß9®é;Ûç?$ÕqõÒTÚðuiYJ§Û«°?²áÈÌ4ËÔTØ17" ¼±ðVRrd\¸âI\kèyPý0W-ÈBçÙØ¬cá7VIóP5& åü8zSH=þ0¯Å|§Zp5XØ³Ôà°Òöýhoz¡ÂÆÊBàn\ú¡¬®=Q)Ùø3Ñ1Ä,	CÜ_ð5y^c[[§o"-Ã-E{M×3¨2+Vé*O8?¯ÁÌ{NáHtzØÛ£¿b {ª¸¼c5-oäÜ[ÀðæúÞ"­êæ^%,\9òUñFÓÃ"VAE2â3QU8ei9ðmçÊ½ùÂ·oÜ¦(à§-á2CâTRÚïi÷uô#Ç¦vk`´hë^/áVø¸ûÅg×õÄöáÈ3Ð²æÅØºFâiÖ©¤FÐ~æ9}Ü'-ÛÀp ù¿gÿéâ4Ê&}Uo7qn³ïòl_FÐ¦* 8â­
±Dâ2Ðáa|Õkï«é¡Mg2!ÙÆG<l*O+FÃÍûZãà¾Ê5i^~!f­¹$±ûÒDÜá3ó<<iì°%Gï[«<¯<'¨­¤9f¡Î}øË.ã®íGt¶QõX%­h
2Z5>úà+¡A',{o;Múi¢oAcócø`à|ðfÞ3ÀÜ^.üNrí+#Ë5Gí©¤éXÔVz}Üó@1t½·Í_(¯t×9dÉÝGµâ_ôfæ5·1-<E·¥:_Pé'åÔyÅ}6.)Y]
´ÒÅ+»SaÏ»{5øvBÜ1¼ûÄ%Q)ð¬º;a¤­<N·W:_02­ñÜöbZ1)]ëð¼­³6à@ât­h"ù®£0Í_40ûÊMO
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8e/0f466edad485ae92bbba9d0255bd890e6ef4a5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8e/0f466edad485ae92bbba9d0255bd890e6ef4a5 (latin-1)

```text
x½YëOÛH¿Ïù+VEB­Ô4m¡ä$6äpØ´÷År,Û²®´ºÿýföa¯ó.Eg¡ìîììÌofggÇfDò±ÕøüÇÁÞù!%÷¯ÜÑ°7pz·«ÚØtÜþðFwo44õ:!µ9©×+[ØËdKÇ­hÔ+?%_ü0^dµ8¦4M£$ý0ËRÿ\aøAãç¤6Ëª?ùá}ZãkØo>Ñ0«N£M?<¨ë&ôÁ{ò×ITEý?Ö&Yyåòü#}^½Ì-2°bSùaø·+Kî'ÈP9Ï\f¢øiFCÛ\xüI¾þðc÷û³N½ ¤q~Fþ=CéôD¤Ó$
õbÈÏ
lñ¦S
:¼ÌÂ*ýG!81 Jö@DÔkæÏi5ªsï{5)Uç)r×ëÃçÂÎhà=Ëä¿L27kþ$ðlU²1Çø÷÷4©Æ4ñ#	²qr~VA]5¡(&1FHÙ¬~?
	ÉÓh&sß@|½«Wg^8¥oÎndÇgæ§1zs¶È~ðï²ZÇSbFÓGâx1é®Yw NDv%`Þ×$Ë#Ãâä1&¦n8®}Ù3ó÷9@éh#[YFsPÄ^Ûû@S?=U¿opàMhîi>p.u»g/ùä¶)¥VïâÒqÕÂGª¹Ä>ÒìÎ+Ù¶´Îîü¶Vû*ß8S{;êôw6 ÜúÊè¯`ÕÛFmÀøéÐ¥!¦÷ä(Å¤-.¥!Ü)Õ$Ê¼L=tbbëù)T½¸'ÖEÛm[=½Dê
$nLsèåñÿ.ÂîáîðvÀÀçñçG3ÏÓ
ÌÓ.M?O¢t+tÎáÑ'JÊ*ÜÝk'iCRÒM"5">pñVã(õñºaé­EZ-%Vò&MØä2#1#ÐÜ\d9v\¼áèåöÐÜ¡ùr­ý ¨®\ëÆÇc8ÞÃòF¯ìDãä%ô9MhJ³m(ÇeL»¶¢Õ"ÍO
wÉëj:&-58UMÁ$² ò In³ªàR¯Ý^0«¡Æª,)Ä¼²&ÄÒ±HU.²ÅÌauÐÏÒÑ,%ñ¹Q¶É<5Õ¨
¡ÇÊm&à Ã±ã¶MõÚÚ¤§±Æ»ó(X¤} íö¦6?/1mFHgÀqCÙY8bõå,oJÙþÎ[Ë4(kQðr{}«[Î7XòQ÷´å©nwp»×¼¹åÎ ÝâGÊØØâ+ao°ãÑZ&öMÎà`ÌE÷$
[¤eËARÛubÓ¾4 Ò4ÞØ¼é2)H78áÔ!êÀ5n³c^	¦bµ\Ì¥¢ÿâ4¹M!ÝÄvl½æ`
oÝâ;Hü7_yÃ|Ïè7ÐÎuðî'j[@ÄZC}ÔÓqÐºý>8?Hï
Ûd±WRÄÈ¬ES3ç"x&AFZÄi/%îý(æ;dÎ#ÒxØ«Å*(åÀÉóÊè¸áb¾§Ç`ÜoëÖ®Ãáh°|'ÐôÁgkðI´óéU[qÁ¥fçÑ6ìç¾Âñ¾þÈýcq|p¤xX3ùÊ#fÂKå0K<¨ßr,¸npÂðQ[ù4Åå!#|f&¢ tM|~åQÇ]1h<8ò%/Wd_o@zÄÕ0Øû20lG|Å4Ó
ÊÙÀqp$0
vö&'Åát¿7ÛtÖr+%lmvÏBùÒ1Çy<`%í¢=ñüºé3¼5;îû[¿=4w;¼ñBÄ¿mµ«]5ñ¯zK{;tuËî-5H7óîÈ$>²:ô¯UAwËÛ®nêþ®x°¤/À¢4]òÜ¨a/æ
n®]]aöøIa«ÁÀ[°¹°´ýe8×ã]ôúõ¾*ÖÀyð`û{v¯Fn·wÓëB
bìýÑæHçd,H]ÇØ6ü0í:Ç$Y	¼»O°ß{=Æ`kT¾»XWÛÃÒg	¸êW´ÙÀ[qSpsJ£H¸,TD"Ù£ÉU© t³µÊBá£tCD^J\
\f]Å/¿J,ËÁDÛR.²¡	ßD$U¾Pí¨9¿Êð«}iQÞÏ¬}³2®Ôrå-ÕR@ã±c¤ì¸7CÓ-®:¸ú¡Jç¸x	^Î$BV=÷yõÌú¬¤Ëuµä/ðJ
GÝ;¬"Ê©¿YzHÔà(®Æ#Ë¹kUµã°
+FÌ!RhrwçµnPÑÑ®fYCñ¥Vé8_lÊT¬*,%ÆB9ïIo­ñ3³¼dã¸,Y2Kp ()ó9XzGÉÁP£Vhàï?¡)

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8e/ba3d1387078981b01b683c40bde4fc05124dfa

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8e/ba3d1387078981b01b683c40bde4fc05124dfa (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹y.MO^¤È©æctcöéESîìª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ â±@¾
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/29/bd25016ae5d23003d4c5c880689e051a7f096d

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/29/bd25016ae5d23003d4c5c880689e051a7f096d (latin-1)

```text
xÎAÂ @Q×hf` mb'pïr:µ¡ôþö
nò/µµ[têMÕ&£×G%àÇÙgLyÌA½©ùrÓO·')çx¬3y7@BN¢!²á½¿j³Ïº7ûà¢öºéRÓZê})¼¾/RËÍâ0Ð@1Ú3x sÔã¯ëÿÒô­#1Cª
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/01/12186e2be5b2a51da59a1c7b3c4c940affa8c3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/01/12186e2be5b2a51da59a1c7b3c4c940affa8c3 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓÖk~z³puÅfÖºùG~L^ö5×¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô |W0
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/01/1e550af486ed623b674a2fefbfe9a211d4eb38

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/01/1e550af486ed623b674a2fefbfe9a211d4eb38 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹+|36Ö01y,¹®;õ¬^ÆOA¨ÚòÔâ½ÊÜi»¦mM{ÏQl$ÅþtÛ½=<< ¨>
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cf/be0afceac0ab4cdb2b89e01634ff6e4bcf9560

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cf/be0afceac0ab4cdb2b89e01634ff6e4bcf9560 (latin-1)

```text
x;Â0©}½ ÈöÆâôþ¬H#Ç¹?á¯ÍH/µZ×ñ4:3L
9E-bqlIÚäC,*Gï³7¼²QOèü@Må·CôÈL\LZÅd9æ DØÇÒ:<ÛÞá*Ãuã¹åµ¶û\Ãúº¤Vo !o=ÁY¢â Ç¿Áÿ"äiôlËZÔA_£#HÛ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cf/920df522a9cfeb43270d1adce61c4c40ad411a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cf/920df522a9cfeb43270d1adce61c4c40ad411a (latin-1)

```text
xÎM
Â0@a×9E. Lñî]N&3µ`´éýíÜ>øàQomz2Ói¬ÌºøH´$½Êd)¢³1I}qåÏÐr©«k'L|òlÄ¦ÀlE¢`
÷ñê«~ö}Õl¬¯Ï½.­ßçËûB½Ý´ÞxD} zü
þ_ªy{©¯ÜC/
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fe/a7d4fdc16ee5a660d03293bf9b2d8cb77ac9bd

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fe/a7d4fdc16ee5a660d03293bf9b2d8cb77ac9bd (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó¬'GZ9øÎÝè&Ë¿ÝmÓO7ý 
ªR2*ß¾.dWþË<9MpÉúÍ/M ðÎSÚ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/62/e76b2c92b610d7dc46c681a90f793bdf505a9b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/62/e76b2c92b610d7dc46c681a90f793bdf505a9b (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`Ð¶mw}ßvÕÙëË3M4Ù_Z\¢WÃ0m×´­i/â9¤XÒn»· ÂAÜ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fc/fc00c1e968dbaca59c4dd86b429a582ef9123a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fc/fc00c1e968dbaca59c4dd86b429a582ef9123a (latin-1)

```text
xµ;nÃ0Sëì\rùY |#Å\ÅB,S Voõ©óÊbðJ[×E#zÓ.b ï s¶*Y®Fæg+±ØHIxØ¸ËSM°\ §j+¥X}ÍÖ°ÔB,>ôÞºù×ÊÛ»ÔE[¿MM¿ÌAFJè/åõØ¥ïã³uÙ¯ñ{Ñû1¥­R =7ô¼¢ò¯Awû)!a
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/27/596f9fe4026884bbd99eff56f0acaa37bdb545

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/27/596f9fe4026884bbd99eff56f0acaa37bdb545 (latin-1)

```text
x=0Eû+^`ÑFãVù"º4Ð´¦ÔÁ/q×x×ssO.ïo5ØÄ_=^Z´i5ÏõPv·Ã~DÒhÁFéal§àâ¤¢B9 Ô(hê
ØTJ6¢mFó×0¥EÌü,?,
£À®T¾°¿«=6ÆúÐ(ë"óÙ1Þzá²sBéÏý<ÙÅß{ÞWLTU
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/27/71b20ea2cceaf64fe103bf1f8ccf9e10d1a46a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/27/71b20ea2cceaf64fe103bf1f8ccf9e10d1a46a (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹bG#_uÿ©4ÚÁoQ¸øBÔæ9Pµå©Å%z¹9ÓvMÛö"£8ÙH%ýé¶{{xx Ø[@|
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ee/497646b9063729528e0056cfa56700336acaf7

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ee/497646b9063729528e0056cfa56700336acaf7 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓÂÔ/[üÈü¥zöl!bºcÜÂ¾pªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  	TH
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ee/ff179129806aeab3f921ef96595fc98c692dcf

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ee/ff179129806aeab3f921ef96595fc98c692dcf (latin-1)

```text
xmMNÃ0Y÷#e]R" ;ÎÀObÿä4jOÓ¤Ð®<²ßßû¦u±º~}ð*Ø
@Fi.¶ÇNþ»·ÙO*ãù`ÌnÛ**o9Q#å`Ù­è¢ÿå¼kmÙÆ ø¨G]¬l°a6ª¬I±èÊÙÄÑFèTÁYbÔ`0#(	«
>Ã U1}±T|©cG²GÅcFë÷¿ÍúY'NÌ1§¿°có ÷¢²B
(y!&{W­b*#/å-?<¢Sd>»ÃÁ»ðÔËóîå©Þ½ígÛÓM[Æ¥Â±_ØC\mi
µ,ñÞÞî´XbæTZâ£we¡ëI±iæ}õvØü H´á
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/94/98abefdcc0593c598e5132d38952efad822c6b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/94/98abefdcc0593c598e5132d38952efad822c6b (latin-1)

```text
x½YëoÛ8¿Ïþ+Z`½±'}íðCN|ìt»_Ùf!²dHr®iqÿûÍ(Ç¯Ë'&9Îüf8CYÏÄ»æÅÅ?^/ä÷ â¯Áµ7õþðÒëZ½ÖÔxÑåÝ´lQoÔjBZ­²wÛqlZÒ8´¢^«T^Ñ<\/¤ø#VëìtÄs¦qþ¾ÈÒà³ÁðS®îÓEVÑ"nÓS^C¿Uù £¬:2ýýÎ\7wþC°M¢)êçòþtWnÎßËÇ
Ùñ:+0­â Ê ÿ~eÉí*'ËåG&zaf2ø%ØæÂ[ââÁÊûñè¥s?¦¨þ$þó	E¤óÿAD:Oâ0Ü.FüªÀæ	> ÃÏ8ªÊ«8ç#TIDDX³`)«Y\]ú?ªéJÊEu"çy­¦y1|Î |páBþ£b)X&ÿd6kù ðìUr1ãLÛ[TW2	b
²~ñùSu*Ey0©1BÊµøc<+pÐ,`î+¯ßôâjæ¯ª?ËWH7²ã³ÒùKZäÞß³Ó¿JÏïÅÄ_îu¯UFTaWBò.¸®$Y§ÅÉýJØVoâ¹WýÞäóo9@é´Æ®±fPB¬ü¶÷N¦AúÑü}C&CtÏ¸åXÃÉåöÝ
<Ó6C ¶Ðé_^M<s¢ðiî,ñç÷2û(TçÍl;­Îµ5ùÛ&:íë|ãìÖql½Ý±yhd[ä[b½NGoQ¶ãOoðxO>
c`´'áRÁRMâÌÏÌ¤{­&öæO)wPõúV8m¯íô	{ÔU&hÜê0Í¡Çÿoôpº»£¯CS¦c@§<P|N×ñ&º6	ü<Ó½ÐÂ#¸Á\ÖU¸»%×Î2ÑCÉ²Ö,øÀÅ[]Åi×
oMÑl±<pnÊ&Ï9Bã8påØqñgÏpvÆ!çChÁtåV/Ôß=Ãùq67úÉNÔ/!LÓD¦2Ûx<b:´Í¦h¼7Ì¸K^VÓ¹hÁij
gq±ä>«
.ñÖí³êfÊBÌË(k@,Leé:[/xXý*¥féIÏcFCØ.óÌ£ÆT<Vn{4M'^Û6¯­]zêa|ø¼ëtv©Û>ÂÔÆ
¦ÐíH·%#^³ÌòªtÚ÷×aæc-
Þ,r¿|µÉ7Xú1÷´å©åvp»_¸ùÊEKî0a¢eìlñJÐìt¼	¥}Ó38²è¾¦aôî°$µÝqÛîU° ­ÅËM¤ ½ÇK"?B,Ôk	ÜvÇ¾VLÅ<µ,æJK@Ñÿb^@SH·±×9ØÂÛrrgâ ÿâæOnÈ÷D¿aB;×Á»mk
sFõQKNÇÁ@é
à0~Þ)7ö\lDC¯.¥Ñ+¨E»eçbx'a&Â·:/%îã(æ2±¨+<ôjñp:PYÿ[&^´^>9§7c8´-çPrLZ¼'¼hýð#¾Wí;hwî,¸
J®!7·ÞL]Ëq;#ÇzKÃ7 ½kÈcDäs÷
¯&oÉ£H°þìPÄæaÒL
	ç
)|¢qsbN)HéÚ6&Ö4¨3'qc],rZo¾2~Bá~Q95´bÂq"8Æ¶*%|ä
f°úDr¨L$k|ÁqqHáHA-Ø¯Ç^·ÓïÂîáü ?º»3Tl¶ÕÞPçlZ& æ^	ÃDHü ^ú/ákÂý6hìC /Ã°'YâÃ»ÂÁV£.ZÄÕróÓgÈìr2Îæé±=UçûØéñä1>0ëZ¶5±Þrà FmK#²å«4 ü8g>ß´ I6D^"Nô§ZNëÆ2/Xy¤K5_ÀPf}Â'äâAZ\MÓá=3¿m{0Þìjö¹Ë
½»{¤ÜbHË°»ÇDú÷è¨b¨7ÜádbêÕkä¢ÞnÞsó.Ïn
öI{Rú\%À§Hè¢gÈ-ªGM­Îh.¸9ç¦iÈ`&«'¸m2²È$X=,ò+¬èm%ªijJØæ5À,ØºáJÛ)äÊØU®AOU=è>À)°N(é*ÅN®²f7¨|Á¡N!a¨:{RËùÖ .ê;NDgdÍiBìx7#[W4ÿÐàïXº<Öc}Íë1_óz¤¯ùÌF·Xl¸Ø¦ÂÛÑw¹/|ªçõ`:¡*§æÅF­_C4j=Þ^hÔ ª.ÖkÙY¬¶pkÅDkIªÕðM¾¼ÈI\½ãÔk
oÞçÇ!r­wÛcDÁò¨Qýù@S^½)[Kp P)óÿP8VÇ8¡GÝÐÀßº×0Ê
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/de/dc3fbb60e7b9020b4a4c1083ce961a6bd810d1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/de/dc3fbb60e7b9020b4a4c1083ce961a6bd810d1 (latin-1)

```text
xÎI
1@Q×9E. T*C% â	Ü»ÌPitúþöÜ~xðsom9ÍÁ,)PÅ}@ÎY°H
Ð´×Ú"oü
pÕWCT
¥²óViÏrM1(4"îóÕ|ö}ÈGl,¯/½¬­ß×÷%÷v¬rÖy
 züMþ_¹M
âÓAA
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/73/02877877141cb179d029cecf5622e4bf73f92e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/73/02877877141cb179d029cecf5622e4bf73f92e (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹uö\>oÝØ°ÖæªúFYa¹­ÿ¡jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  ÑO@6
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/73/fdfcb15791890c85159c555d46a6f0f8b7fe4f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/73/fdfcb15791890c85159c555d46a6f0f8b7fe4f (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`0º.ô*åÊ¶ù±7ø#¾¢¿ª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo ÜRB
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/61/5a4d34b2b767ee3a93507b0708e4bd6c4a4a51

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/61/5a4d34b2b767ee3a93507b0708e4bd6c4a4a51 (latin-1)

```text
x+)JMU01`01 ÔÊÔÄâøäü¢¼T§©::]ez÷§.©(ÖÍ«ZPûh?  
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/70/f1d41dfe52532e250cd1b64a532042c66571ab

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/70/f1d41dfe52532e250cd1b64a532042c66571ab (latin-1)

```text
xAÂ  =ó
> YØJb/ðîqmm"b(ý¿ý×I&3¹Õºm
FÑ|NzÂf²SÆHP$§¾Üå3tæDL)&ÏyÆàgOó³%ÏÙ¬x¯Öõ³í]?¸¾n²´²Öv_*¯ïKnõ¦ÍQ6HNÔA¿!ÿjlúKBF
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/74/81d59b4ef29eb1514dde95c600aa33d6a70970

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/74/81d59b4ef29eb1514dde95c600aa33d6a70970 (latin-1)

```text
x½XmoÛ8¾ÏùÂ
°,Éºõní®Øm®ÎKm§ÝöÅp­5êØíôÖ
÷ßD[NóÒÞ3È¢Hê!ERt§Q2eG­£¿Ìù×0æìËàÂúC¯?<ó{¦eLlÏ®LÿÊ°Yûm«ÅX³	2­ÚN·ëØBäí{&$Ú­Zí gÑjÎÙÇ0^®òæ2Mf<Ë4{3Ï³ðTcøÎ·is7¦a<ã¬)eÄoßó8oÌ9ÏÞÜêrS~Ü4êª¾/îÓ¼*¹¾~ÇÖt¯s$«¬ØÃ´LÂ8ü»7Ko¦ÈP«/÷¾0ÑÂ,ç1OÙ&m.½ÅþdëßÃ¥ÿíÁÏfALoYûôýs*²Ù3Td³4¢ÍjØf3{yÄ
þmÄà|Ä["¢%XópÁyÒXßÙóyc!çûVx1|!|PpÎ£àA±R§ü¥Y{gç&{KixsÃÓÆ§aB ÛG§'5Ü«©6*IÍR>oãFBò,Y,ÁAÓ¹/ ¾^p#yÏø±7²ã3³%!äÞ_óf7XfÌNfwÌ¬·Aî@eDN%Þ×U4SÊ8¹[2Û´<ß=ï[Þék t±«	¡ÑcË ã½åYë78
¦<B÷
Çzç¦Ûw×|òmÓNÿìÜóõÒGº¹Ó4Ýñü©_hfÇ1º¦÷Ó&:âàlãå¸?6_m9<4K[ø/¶Äüv8]:4¢jÆCÇXÞÓc¦M4v$\Æc¸Si¹tjagþTr·^Ý0ç¬ãw¾À^!õ	[Ózuþ£{¸7º
ðe2äEÊcuºuZÐÉ$¸P~Ì/Y <
h&UûPÞð+èxÆëeïòÚt¼Ï ôè§PÃeº]\Ã×K9\ËÁ"Hw$Á#ÛG¼ehj&ã\¨î3­àd"u÷#ÒGô"õ ©ã»²í[ i\9ô¤[p&"o`[ »Ýµ/W¹.
ÔsN*P÷_Fb	é6¾ákÀ|bl:s×s_äðIÂû~%	b¯<
âfúXbÄ ÔWÔ;nSÐq2Pp|Þ)GZ®
F
ÖþpâVbÄ,¶aÏ%Ð±z³wÌ]1îgLPÏ¡ô(]$¬-ñÈûF\²TÕ"W,EÉß<õãÕbo~'éìËÏ©«£@ã$®ájü½\ßf.ÊnFÈG:If÷|}U×§.<=Ó6=óU­`¥úH¡¯1÷A­Ï=ÛÆBPd8¥e¼År+@9ÓÉ½à:Çgþd¼ð¡db! òÔü
<¸ë ³|sD¦KÎõ¬ÁyY¬p¦ ìñòúU¸7,b­ÜE½ÇÖÇG;wÉDºH×1+(¶$C÷³Å4öÜîçAgdïËè !ÀEp¼m#Á.G4àQ2 íbì»¶Hä`RN·éBGk¥%à*Â¾Ùhâù
Ò6Xëô*¼­ÑÀpM>S[i¾ÉTauê|;.9ÆY«Â«×ª1{FÚ]¾)ÜÍË	üKÜÓÙ&^MQ/H!-ÚZÒ(¸ãÅ_*ÝÔìÅî¦ÄTÈÈyJTÔÿXÃÑå«yø«8ÂoÂÇ2ÍY>îL[\råëP9+a£ÕõJS[ir?ºÃÂGu£Xê±ÚZSî©O$ x¡a=i.Õk@±Þ°¡¸Ò´°Èk°½4Q:Á´Tse¡J­®K]1V]DARâ­Õ³ÌOyÆsxÖÆêêþYi	¼éP;ì+³ºM,u»Xê¶±ÚH <ÞJTVµÉìm~2¶)FÊO¼ølcÚT¿é¨ØÜ¡­«;ñn¶£¤ë_l¸íKüü¢VæÔJÐ\¶4£V¢«l"6!Ç@=¾èøÊLëÿ«öHä'z[²²lkùó B¨TTDZéØb³Ây=hé«®Ôá¿æà$ÑQaûãÔ·Þs¢*ø]ÝvU¯n¼ÝãºçtÕ¿ÇQyñÏ2Çìj|ã*ð÷/g^ï/
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b5/b0e695d9325c57504394fd030e61a91f7b091d

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b5/b0e695d9325c57504394fd030e61a91f7b091d (latin-1)

```text
x½XYsÛ8Þgÿ
N3ã§ª¶{d»m·3²-%nä#/ÙfMt$gdö¿/ÀC"Ûi¶;Ëð´Wq¶"oo;ÚÐïQJÉ·éY°Ofþdv-Û\:~0_XÁéÁË~^÷û"ÞÈuÈË7IúÎQ®ãíQo«^^dkZYQ¾ØTeôQa¸£ùÕmÑÛTÆ*J7QzYö¸ûô¦±Î6´|q¥Ê­èUxíÒ¨ªºK®{×ô¶%ÛæÈ¶ |)Ï¢´|:¶ªârnÜÌ Ê¦´ ÷ÛÔxüI>tï¢<øqë0¦dðñ=ùû=ª(×OPQ®,w«!÷8®×ö«(K
ú#ÏRp.bÀ-Yï3Ö*J¨QeFþ0ÊÒ³ß¼¯ <PpCãðV°4\'ÿ2ÍÜ¬äFàÙ·ÉÜäQÄg]^ÒÂÈie5ÈcÇ½zb£:XÄ!Uþ;ü($$¯³$­b
æ>øy.*ÌM®é3Ù±m¢2GóÓ0aBÞUô½êÂ¼$N¶¾&~ñ¹#ñJÌ¼+Íæz	)Áâä:'eûw:±ýÏ!r22ð
¡ÑR88Þ+ZFå;¢L~Ýà8\ÑÝ³0]kæZÞÄkùä_Ú¦(ºS?Pï¹ªÕ|M±Xï2Q,>p¼%M¡BEVzÄGbáàii'[o/{2î¢ÆâÄäiÔ­¡ëóÿ=ÂªúxþyÆÀ×å×ù Tí( è&ö÷5óCÇs®¦pW$ËgÜN²óÏëiîØ«§ÐÁô°¼ÒqxÎ»Ï¼³Ìè.ï|F8øÁNØ¹\ìdÄm¾Ê,¹î¤aô¹p=Hzìx§6AÉ;wc¦é6'0öi b© ¶Øs&¸uV\Ï©Tº?q`KHwpÏ=8Ô·\yä»ÀÄo¼ûÂ;æ}F¿àa½WUi)gjß`Ä TWÄ·©é8ÍæÓ)¸7¤çÂ¶çu2[zZÌHÖ#c:ÌsÜÅ¤Wä5ñæGÆý	êyÅ=J8^ÝXI×Pí©éqö-t<³åth¹óC@·Ý£{çðfo¥èÙrÖîqõÔôêHÂu©Wò·WÁI²ÉPsæ³xÐ#Ð×>¾IYcðåLö
]©KBírý<,u¬ÍLI¬ÅIPWÆåâ0v3>ÞÊWbü mpÕóM@Ü4¤±·éºsQñÔdÂõËZlË},¬ÁJ´8möl¼Èð²ðÐ· l<w¡*×7§!àà+MiL£åh8öäKF%
ÊÛdÅ\(Þ×épî<%a$ºB)d{»Wà7C4äAÖ ílxË&äbÉâ~\8rdBÖUßuü.i¥5[U"·x$jÎ+¾a¶/IÄP3i8âÅBåÐ5Gg(Î'®ya5)?ÆÈ|éKî®
¨¿Ý~±ÀVuß$ÃCä¸ï®¼°ÎðrH?ÂÐú2wØùÔtáÄõ.+ÿHñ'ÎØÒb)Ûñê¤tàv.º5©&|¨Ø ßÓzMÙéÁÀ/«í&Êmãï:$"ÄiÃÍ÷ÞÜíA¬=¸µ\É@»z·AÛé®²¬³ÿ»j1)îîR»º
&ËÆ+@!øsxn©ËÏ0{{'(Þ ëtËÛ2(hI+nêYD*nnê¿äR;ØÐå/Eu]( ¶ÇÖè´øÒµñÙ>U»x&¶j`ö{A×;£]ÿYðýºi»fmSð|FÁÅÜin{`©íìçíÕZ/4å±ø®|àëÏ}6Ê5Zî¨ÏéÒçMêýÅWTÃúý¨káC÷KbØUÞúuòûºÙMéhÍt¹}3]Ã¾i¾6¯ÿq­RÁÿE`ô}I
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b5/2d05719ae137c1e2f663df59fee5f73021f24b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b5/2d05719ae137c1e2f663df59fee5f73021f24b (latin-1)

```text
x½XÝoÛ8¿çüÂ
äiYÒvÝ]·Ý ÇqÚ\ÚI÷ñb8ÖuìÀvzëûß¤$[r>ÚáóCDRù£Dvæq:ggççç¿-ù×(áìËð*£é`tô¾5s§Áp|ã7ËO:ÆÚmö¦Ói\âÛKKNÎ­8î4GQ²7KÎÞGÉzS´×Yºàyfù«eG4ï|}÷µEk%Ë(¹ÍÛb
ý¶øOÖ"]òüÕ¾nÎïÂhEÝÔ÷Õ}{^+ëó÷ü±f»®n
â	¥u%à?ì,»£B£¹Z=bGyÁ±LÄ\íû½o~ÖÁ·Ç _1(°ãïØ?ïÐD¾ø	ù"Kãx·ö£ÇÂÅ°Ò¤Å¿­Ó61 Kz #:¤ZD+Þ*ÒÖ*üÖÊ×/[«4;¥és
é<¥J¥ l_²,ÂZ=H<û¡'Yt{Ë³ÖgQZ|ËÑW[:*Iò©XvÞâ&Bñ"]­aæ1p_@~½T[E¸n-ÃdÁ_p¨Ï2Ê×~®h}-Úv¸Î.îÙ4\³ÞuG²"Zp*1í®
[ØeLåÉý¹NøþôÃKÈØÖÄ{ h9ÐÙð«+{Ë4Fù@¼9O ¤[YZó8ß®7·Ì»è]o@Ø
QOgøe.ÐMþÿFuÈèì?|)M 9AFØ ZG·Ð
ò@"*oo¼Pä*
Â]nâ"ìÂû£ãúzÖ]t¼égXêÑO¡ùâø6Î!y-bph	Ê=!*F¼æuÙdü¬æ	û!CÉI$
¤ºþÄ&À®Ù((³Äà¡GëQÞaÐü­ bíâ
¸¶{UªUÞàâRººTÓhÿ/a_.AÓHøÎâ@ÊMO ¶§( ð>vä7BÐ-½Yä3Ç
¦9'9tUÎ 3ÇÃ¡Ü´ÞXFÖ÷]£odaU\Ë¥=K¡-±f\°×ÌX¶ÈCû'´u*ö¯Rv,0yàÐ¤ú0¯º4ð2,ù" Àvp3vgC't,i*Ûª.Ô%æâôoÉfõdyfÃ®ã,/yÍúaÖt\¿£{|ûCÐ;WÜÎ±J½5Ç¶\Ö0ó&:ë9nC	óu§ízåb¨	¢ympøÞHÍ½Qêî¥Ûå	"¥¦ê³¨V
¢@ª¸?§±Q¦u¤qï] åEð!OÅCTÆ2®&ª±²·ÉõxËóÆp1@WG¯å©##(wÃ(¤
ÈÊ]ãÀË>þÃ@#¸·ÕÓÄ÷.íÙ÷9o¾Èw4«xF9òÇÕ<h¡þçawì>«Æ!"çM}@¥x0ÚKËÇdÏu¡£9ñìQ©&µkC%å1×4ÈmyÞÌ`ßNpgô§t)$Ý%û¸.Q&zªÌªÑ¾YwÄ
©IéUä°ûõË§Â«Ø4*A 3Äî#p9×3ø$°»W
­G¤À­ZÖgÝ8UÅÂwÏ¦ÁÌNÚT\×þÔLàãF ÔIìþÃ.ÞHfMõ[ÖkOÍÒ¸f£#7yâb02=*x]$&
¨éÀí9ÏªL
¡N_Ñ	æÀR×"
x¿¬¿&Ïzí`^lQl?­hKûòRÆúâJ&ò¶D
ILïú­2à`öU7#»¢¥©ú91²}¬Ý{Bp\æ³¢^ZUBLÉêÃÞê°äWßyqÂ÷¢t!ô÷¹¹íÁ¿Lð}ä8²IöO¶cÊó ã9/À°oCM^ª¦¬öG«÷WjeõkVí]×ÛøÒç4±f¾¯ueT¥NÈ5F#ëK~7Li 
 ¿¬3xÓÞõ=j~jÊMWê#ªD&¹k4M9-ï¸LÔ& Ë@ãáBÐ8q'h¸4î¬L\å´k·£0*ìå¢Ú6¯ZQjÁÂá·Wr&üìÇ\¥¾BËv%xmZÊ¶$uÉé°äÜ,}Ó$Ñi¤®¼ÞZPÞQ/8óÿô[ëIÕl@ýßb¹Î
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b5/9660f73cf5eea5f1c9c0c3bcb27a437963a1ec

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b5/9660f73cf5eea5f1c9c0c3bcb27a437963a1ec (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓBßTìÐSùøo¾[ç?6ªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  äyS1
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/df/a139cfe486c43c8807964c4a7121838ca746f1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/df/a139cfe486c43c8807964c4a7121838ca746f1 (latin-1)

```text
x½XYoÛHÞgÿA[ ®ÞvÈ¶x#äôxd{ÑINûßK3ªÁ
Gär8Ê2ÎäEïå«?ÖôSRòqrÌgã©?C{d-?Ì.íàÒrÈñ^ntz­½*ÞÀuÊçi÷Z­£(]Å5%o¢4ßTÝ¼ÈV´,³¢|¼®Êè­&ðæ×wEw]uQºÒ«²ËuØoÞÒ´ê¬²5-_ëzKzÞFÛ,ê¦¾&7Ýeej6çoè]ÃvS"ÛTàÅ¡<Ò
ðï_¬¸Z¢@«$·s1£²¢)-È7Â}®£Eþ&oÚ_£<ør«0¡'äøíkòïk4Q®~ÂD¹*²8Þn|kÁæpµ¢°FXEYÚ¡_ò,à#\==&ZE	íTY'	¿tÊÒu')d¯'e1}Bú âÆá©¸MþË,s·[g×"Ïq9Î"ºº¢E'§E)/@×êT2	!UëÞ	þh,d¯²$ -c
î>üz$;UwÖaº¢88Çg9º	Sò®£OUwæ%q²Õ
ñÃ·èèÀ®Ä,ºÒmnY2,OnrâØ#?ðÎÆ#ÿí#Èà¬¹'bJè´TÎÃ¶÷QyB4â÷Ã%1<sËµ§þí½FL~Ñ7Í ôÐù>QG_wwY«Zñrnö]kpnû¿í¢Û?WçXÎÇsûáÍC'(÷Þ³'ö=øáäö ¦zÂqÐ÷âhæÒ+i
=¥SdUXéEw$&öÖQ;¸ôæ¸§ý ïv5.È©nÒÿ7zhõááìÝWÅ«ÇJ;§_ºm0wÜ£ïÏE =A¸L¸
àxÃ¦ø¨ß<ö.ÞÙ®ÿ´qR>ú.´ðÀ²½ÎáëÞñÁf*Èw9Ã6vØe	»Ô,æ[¥ÐÜ9ÄÛKÈÉnY}o>`ïl`gñÁãÃYAþ3NÃø©!âá
b	;ç\HÕóì ãvÎ¤	´ýçI6|ßðÅ³'à¾Áal»óÀwA ùð,úÉ}µVUi))}¬1bê3âQ|$&b±Ùd!ãò3ÈçLt<]xFÎH6¢c9,rÜH;®È3âÍ­ÏCú'´óG&9æxx¿aMÖ@erj*Î>Ó"H7ÉÁú.&}Û=T¾Ò[¡Fï_ßôtC3})©æ³g§R	ç¥=)»nÎBäA$sYÒ,h-¥ _ÔH_üøÁÿ¤äÈ¸ðq"u¹ÖÐqðXPõ.ÈúçYÏãyPSZiÍOuVÔþ,æÀ?å0¦üa0!eð©¡rËz¾ë5ØÎrÝ8ôôzÂyÍMà4Ê:«Á£õzBM¦nËÀ Ôpæ8&Â¦®N7}lãÕY{EÛ1pì("JwÉ2ôïÃ¤?sÕÜ¥ lRËôáÊl;ìè¨),ö2<N¡GßðÎçç°ÂB	_< sG¾ùcg§S[¿u³óßd¶ð¾Br#¡JÑ(HÈúA SÜVaÞ#jFÌ	{@Ä¬ý«a~®¥O]ëÒnµ%æ·í|Rë¢^âÅækDH²ÙøG>HYÐ Ä«ý~ :ÛÅÄr¡-2ÌÍk2ßÓRäÏÆwÒµ9J#|¡©OéÝ³FÓ½õPVu4ÆoOµÒ_Ä9­d­Ñ;qU6®N"ÌÈ±jµFR`´YVÅY|¦ýbýÙ7:E[Ãd°5h1aÄmtß\­I×èZíò®
ZÒ»ú."ÍaÍG¢^CHt`}ß!õyi­55iÎÈ/Ó§vÚ&ûÃ<i´Ô ³«	ÐÕÖl7?þ6hÓµmTÓÜAp9sê[ (?ø~º9«ÔùºIH95âÕ"¯þìCÀ5(í³ÀôQÏ®¼µ=yûùµÛÌÝ¨UÄðêaÆOÇ%QÕ¯eÕ¥åÞc]¯f¾höQ¦Þ.Ê´°+coÐê¿f®=ÐNpø>ÇEa¿ÿ @cï
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/69/ea8909e125c3e3efdcd65b10bb1abd063c242c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/69/ea8909e125c3e3efdcd65b10bb1abd063c242c (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLghØ¥¸YÍõ§Ý÷ûFsäþL|l·ùôªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  ØWÅ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ac/aede984b5e2f5393b112b372874faeba280650

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ac/aede984b5e2f5393b112b372874faeba280650 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg8yä¬°§9cgÆØtÅ¹Kíø~ü(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} ywUe
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/72/af29f2eca1ab78d083057e9fc4f893a6f56d44

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/72/af29f2eca1ab78d083057e9fc4f893a6f56d44 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹-+ï®\¿ygS`ýæ¾¹_l}¡jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  ¾A
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/65311b09fddbfd177b9e39b58cafce0fefe1cb

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/65311b09fddbfd177b9e39b58cafce0fefe1cb (latin-1)

```text
xÎM
Â0@a×9E. dÉx÷.gi-#iz{·>xS«uÚFÑ!±Â9&
ÁìNa N)øW_êò9 >" °%Mà<ï
ÛL³ET´WëúÙö®TE_7YZYk»/Ö÷ejõ¦!zðR}6ÎuÔãoÈÿRmS?QàBV
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/a5003fb4dc6bd6264a67346d68a29f42118bfa

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/a5003fb4dc6bd6264a67346d68a29f42118bfa (latin-1)

```text
x½XmoÛ8¾ÏùÂ
;`YÒuëÝºÝ '±Û\Äµîåá$ZkÔo°Þºáþûz±%7I×m8£L¤R$%wgKr<¼þí`M?G)%¦ç3ÌüÉì4±°ý`:¿4KÃ&/Bú}ÔéìUñF®ÍT^¼"LãpÐéDé*Þ¬)y¥ù¦êçE¶¢eåóuUFï¯4¿¾+úëª·Òu^}®Ã~{ô¦Uo­iùüZÕ[Òëð6ÚfQ5õ5¹éßÐ»n["ÛTò¡<Ò
ðé0Ú¦«%
tºIr08*+Ò|#Ü§&ä/ò¶û5Ê/wA¹
czAß½!ÿ¾Aåê&ÊUÅñv3ä[6«5Â*ÊÒýg)1àì0Ñ*Jh¯ÊzIø¥Wæ®{IÉ$)éqékwB¤à6ù/³ÌÝJn]¼ÂEDÌqÑÕ-z9-¢¬yê¸V_,T' RµàÂBö*KrÐ2¦àîÈgR¹Wyo¦+úCq|ÖQ£ûi0%ï:ú\õGa^;[Ý?ÌÉxÞÈøìJÌ¢+Ýæv	%Áòä&'¶iùw6±üwÏ s32OÄ
Ði©lï5-£ò(ÄÏ;KcxÃ5gþéM¼VL~Ð7Å ôÐù:ÑD_uwY«ZñòÝºÆèÜôÚEwx^ok<ÿ¾cëÐÊ=¡¿ØóxáäæØÆSgâ-?ÔLÐxqBBqkOÉ4S£WdUX©ew &öVV=¸ôæ¸§Ã`èN~5[!SJ´ÓºNÿßèá( ì¤ÏßÏø³p y]ôØ£NÍøÒ%8hEü,À=ºx.)RëB¸« a5õÛïâ½éúA'å£îB[ép_/øð&SA¾Ë¾´±{Äs°kËÂÙ*æ>Ê$ÜöDòpDþ\¾p;ÈzÎA¶½3À ÏàÇ1³|3NCûi bû±Äí}.¤yÖê¸3imÿÍyRM!ßÆ7|ñÌ)øoÐMcù. ó>ðEñ/9cX¯UaZJJêxÇej>S±Ø|:ñùã¹¤åÙà$Ì3R(b6\÷#Ò+òx1â£I?@;G<b`4ÉÈ!ÇÃOvÌj¨v4ë8ûAºI¬Ùb:4Ý½õ!v Û1¼px³?¥ÙkIµG=3¼:p^Ú²ûéö,Iö!Êf1ëH{#})àãw{ücIÉqáãCÚàZcÛÆ¦PW»\_V?OËf»AC)åu§hÜY8û±ÌAöñ¡<ï÷Êg=ß ÄÍ<v3\w.:ZL8_#cu!PE`°e5ØÑ§ÍM^~Æç¶­#TõÚïÍn8xsVfÑ´5;ê¥£å]²Ìâïãt8·S0]¡42½=*ðWtä^Õ ïÜ	<UJL±eñ8:¶|ó'ö:RW½k³Pós¤UÒ?×í*1'%Ò°qßx5®¼*3q8uK³)ø0&ó,<8#ºÚèe
_ WMÈ8sø¦·Õy±6H	Z<<(l~³ëbj¸pð1¨¸{PÄ:{
)	£Sæ1®æ\c®¶ü=9ÿ9ý®îÍõ²Ú¬£,Ø¤1~VnuÌâ¶v<ÚX»2#JºÕalå3çwºË,«â,û>_¡- ÄQ`ÁQÀìk@WÁdZØõ?Ê0-qó²±I·WkÓ
ºN·¼+´â®ÞÓE¤¢ñ[ÐøRhùRNHT`C_Õyaä­µµé_º5Ní2µMö»yÒh¨fW§«­Ù®	´ýmÑºkÛ¨¶+¸?£àrn7<Ô~ñýt{¶VçMgl¡ewzWÞéõ>£¦rN¢+!êó`ºð¡§6h«Ë]t4x»Q×Ãk?Ä*±«²õDA/åÚz:­S:Ð2MZÄQ×ÛG©Z»ßumûÖà¨_Üh¸þkÞ8üýX×Þ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/2314437d601e732c2b4411c23f4cf9ed934f08

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/2314437d601e732c2b4411c23f4cf9ed934f08 (latin-1)

```text
xÁ
Â0=ïW,DZ-JÁª½{/¥M66Ù¤ÿÝúæ8Ãkkp±ÊÉzpï^oÖ6àXL0§K,[ÂûùØ+X7]pìûòz9Üâd=Å$´ÒÄk<åÿ*j+L'	#&Q	Çf2x$©º3¡
\[¯?ñØO8;¥<Üâ&ÛåðÍá'2y
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/774a59bb724e2741bd1856d349814fbc12f015

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bc/774a59bb724e2741bd1856d349814fbc12f015 (latin-1)

```text
xRMo@íyÅD/ö`ÒX{ho°¬¸¢jm/>V%¡¬lbâï j»ZÙyïÍ{¦*ÇûáMtªí>OÖzÑ-îCð7Þ§,ee»RåvzskÙçI$³BöíXfe²JdþSÛ']B3ÃµË¨ 3×a³OH¤²U²® Å½5=1eðå*Ø¥%tØ^¦A±AÖ<mÊsÛî3Aã»×F÷È,Fúnep8\
¸öóø[r­Uãêä2.±Ù9-jÑz"T*Å­² L%T¯ð¡b\¬Zº©Jðf´î;z,5"\êèÛ¼/®Æ!,TZë#Ê¼yÃy2zÿr,·èh*^C¯gÚêÜíYu¶Ç·lU×«\[ê¦/¨Ï]­jb2ågið¿r¯Í»ªl±Mð|N4¸wSC"t¥ÊÄ>®Áüuz9xÌ3KüR=ãÜéù_/üód
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6b/ea25f3b0862d750feca05616f08beb3733d8b5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6b/ea25f3b0862d750feca05616f08beb3733d8b5 (latin-1)

```text
xµ±Â0DûÙNºâ?º´6Uêü=Ý¹ñÞpïR¦Q
á EÄPpÜ² {°£ÐµÐXh©O66g´$«ÌjcÀb±Âì½Ã9Q#¸@¾âM\ÌK>/'éFÍå³>Ì%@Ðám[¥¬õ,ïOýuØbòt5@»9Û9÷T{»_QùëH¥«bûjÜaÍ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6b/ff9a6b229488f05af3aae7fcdd19fcb4b6d16f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6b/ff9a6b229488f05af3aae7fcdd19fcb4b6d16f (latin-1)

```text
xK
Â0@]çs¥I&?ñî]N&ÓZ0ÄxëÜ>x¼Ç­Öu1þ0ºlçX6¦ØÀ1(Þè<1 9Ò¬Õºl¬GW8ÎÅKbë<Q$ÑÉ/sÊìQÑg<Z{ût¸Q8¿eie­íºTZ'nõ:8Ð8NvÔN÷¿!ÿªÃö+u©¯'±¨/öGÁ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3a/49b1aab67ae2eaa544534f1c73ebbe74b13975

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3a/49b1aab67ae2eaa544534f1c73ebbe74b13975 (latin-1)

```text
xÁ
! }SÅ6 Y`I±ÿ>XôÃqý{-øI&Ü[[&ís Õ#BvlK½OäK qF¢¤³Q_ò9J²Ö3¢órb'0ùuÅbvò·ùê}pç&pYåÙËÒúíÙxyroWÐÁ#¤èàQívÿò©æ:)$õ{¬DF
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3a/04fcba98c2ef8b820b20155458515e9a776a87

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3a/04fcba98c2ef8b820b20155458515e9a776a87 (latin-1)

```text
xuRÁÚ0í9_aËö°¶íªRã'víIa{]¢¢°
©*öëw¤J½yÞ{óÞxìÕv·b_&?»×CS½lZv³þÈÂqxÏ`S²Ù¨ºmªÕïv×ìIém¼¸ÕÕº¬÷å­z*ë¶z®Êæ+Ë£ &OTÞôÒ)é1wÉ§pñípI±û1~WTd¸Q>JÍýq¹D- EËz¹Úlþ¾±usØ·Ëmo*´3êÈÁÝEâlz'p\ÿMÆÖfW1-zsî2¤òD§)^«zÝ6ó­Ê¸.=KR«LoÑ¯ì½U=GÇ+êOSµUýÂÚ{Þ.÷^Wx1Ð%c;P LNçGÒ1lX$áÀÐìÈµ6sL;r ó~(¼PyJÏvûÑÉÆò?Rä¿TÆ-Aýdô°ðÑ êHw##¹ fÍ\ºK5xOqww^j/
~]àTJ©6×S'yLw
ÚA
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0a/ef60671ce98f37cce7b3d29df5bd1ae8a09952

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0a/ef60671ce98f37cce7b3d29df5bd1ae8a09952 (latin-1)

```text
x½XYsÛ6î³&ñSIN¶I­:LJÎñÂ¡$Äæ×'ÓÿÞ] ´$×ÓâÀ.öø°Ü]PZÅÙ½év~9ÞðoQÊÙ×Ée0§ñô<:£ÞÒ]Ùµ\÷\Ö=ítk·ÙÛNçè ?ð\¡rzÆF·stt¥ëx»áìCæÛªÙeV¯6U}4~ðüö¡hoªÖ*J7QzS¶¥x¶ø=O«Ö:ÛðòÕ­©·â·á}´Ë¢iêGr×¾ã
Ý¦D¶­ åBy¥à³a4M7+8:Iû@!£²â)/ØO&ÏTGýÁ>üòàûCP®ÃNY÷ã{ö÷{4Q®a¢\Yï6Ã~ÁËaázÍÁGXEYÚâßó,à"t)¼ñ­¢·ª¬ß[eÎù¦B²Ó!YL×¨¸áqø DjiS>ey¬ä^áÙçä<Xâ,¢^´r^DùÔÑW[9ÒÉ¢hTm:ïða°½Î´9÷äÏKRnUaÞÚé¿àPÇ&*s<~&BÉ¿¾UíAÌÍÖwlæl¸CïXe|ÞJ,¢KÇv£yr3×-ÿb<Z||	Aoî«X¡ZMblxÕS¼caùÀyKBÉ¶¬
+óÌÇjã |:ºÞÞ0ï¼ô½±Àn±êøÎ¿Êe
Ý¦ÿoôPL´¹áìÓT×åÈÄ(ëU@J d!¢ðãÀKH.mzu¸« ²ûæ£~3ë®>9Þâhã&
ó-a¾8þ ÷py%§Orr
ò=ÉXý369&îå|§ûB;H,¥í1ñpFþÒ²úþ|  »þÅÀ ¯''_NCaù#É8ëQCÄÚ±ÄÝ{©¤ê}o|~¡Ü\	´ý§´M
bù.®pá;8®éÂñ$æÁÂd~Óg9èþµdôµ¯ªÓ(s®1b;jn4r6L dr 8S'ù.R§KßÊR3¸=WD.ËÄ{Ãüyo 3Æ~v^ËÑ$c]G¼Ùã,TvÓ[qö/t<YÓå¤ïxëC½æáýUÂþFgÄÈL'ª9ãîEÏ×ûddÓÍ]õ!Je¢EÌHáÑ@ß(øø&ÿ(¾üÈÔº.6]íäª_¦e½Ý ¦ÂºSÔÇYÎcW1ìC |­ÖÊwýE×yâòìyÞLu<³p_#u¡P+'°
ØTd5v4¢±ö§Ô(@]¦_±j8s]aS×¤ë·Avá³ÅÂ¢ãZ8öÔKF%ÊdÅO\(þIæ>§`]a42ÂÞ
øõò¨jw9|WTJL°eÉ8Î]Zõ EÁÀ}wn9ò.¡·aeá jÎrW=Ñât_¨=e(¨$+YQ-~Óõ½ÞàÒQÍùÜë];uIÀ¯6[.¥wÅ	Q}úïI
ðàJÏõÑè5rô»«.«%üâÃFÏu]Mz\¸/ªáöÅØ:VîÕ>íaÒ3"zÎMî<d¹´@ì)oé¿ú¥¿¬¶(¶iø"0#hS8ãH¶*±T}Jò¡
îÄET×3·n¤@ÍZXëøt#	¾ºÄº«Í¨ÛÕÙ$ÔP³Îsm²÷ò¥
EWÁd¹	AE¶Ê²*ÎBøåa9#-aÃ$ôZB?}¸|(¼²
>éH[Ög×1Ö
½ëè] ¤+ùÈÕÙcÆrÖ¥`riÁÙS_ï,ûW½Ñ=³DføM5±ãÞãFF¢FÓMÛ!.7töñûß£ïû× &´G¨µæî<ÿEVP÷£ÖÃµãgÖa%ì¦ìÞ\7Gz¶2Äåidg[ïejí_Ûö¶à@â[t®xìxÎÀhðõß&°úoh;ê
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0a/002ead6707c329f12419c7f4381a195ffac728

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0a/002ead6707c329f12419c7f4381a195ffac728 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹[uYg=4?øè[òýÈO¿(~òª-O-.Ñ«ÌÍa¶kÚÖ´ñÅÉFR,éO·ÝÛÃÃ %B"
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/12/cdc033df24c88a77a34cc636625515d964506e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/12/cdc033df24c88a77a34cc636625515d964506e (latin-1)

```text
xÎI
1@Q×9E]@ÉT@Ä¸wYI*Ú`¤Ó÷·=Û~î­-´²9!½³±T]½7µT&ÌÙGÕ¹ >4ø=!Y¥"JÊþ`ÆlsP©h¨`IÐ6}À½onÔÎ+?zYZ¿>-¯SîíÊ£r68mà(b¯ûßäÿ¥ëÔ^|Ï8C 
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6c/391f98ef774c0fb246c942aac93bc5840251f5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6c/391f98ef774c0fb246c942aac93bc5840251f5 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`ÿô#æûDÑ«¶Nãåý×ÂÅþª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo ãsB
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b6/b42d023c3bd6eacb0c26615af3814620158f12

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b6/b42d023c3bd6eacb0c26615af3814620158f12 (latin-1)

```text
x½XmoÛ6Þgÿ
¢üi®í¾mK»²-'^äHrúòEm6"K$gMý÷Ý<Tb§Y	È;Þ;WqºbozýW¿mø(áìóô,XÌ'32;	FöØZ:~0_ØÁå°þ^±ntz­*ÞÐuÊ×Lhô{­ÖQ¬ãÝ³wQíÊn§k^i^<ßEô^øÆ³«Û¼»);«(ÙDÉeÑ:âÝá7<);ëtÃçWºÞ_7Ñ}uSß¶×Ýk~ÛÐmJ¤»P> ¥QR>FÓT~¹BV{»½	A%OxÎ¾3éS
ö'{×þeÁ×Û X1½`ý÷oÙ?oÑD±~b§q|¿ö½ÃÂõÃa¥IÍÒpJñÀ÷hmy§L;Ûðk§È8ßt¶ìõHÓã%¤*nxÞ*Z@ÚoaYºµ½QxöMò'y±ÄG<ïd<Ò
äPÇ¹ºj¢*YÊMï_ÙëtAV1wAþüJÊ2Ì:0Yógã³ÝOÂ­Pò®¢/ewfsÒõ5óÃîÑ;RßUEtÉmi1Ú"O®3æØc?ðN'cÿý¯9ÀZOÅ
ÐiRÎÂ÷QqÌ4âçÃ1<Ëµgþ©íM¼FLþ£oAòÐú>PG_wwëk^3ÕyB7®5<³ý§qQî×ÌµÍ0aiÝÀ)ê¢+\zÄØû§½qîi1YØw] å¢ðx~Ì4BséÀ¶+x'G'OË°Ô·Þ8¸Sï.{2îD`7X#åáV%µnÒÿ7z88mGó3¾â,¼Ê¬SZµ|r	Ã-£ïðÝÀKHJ®á..(rxU|LÓfñ;ÿ`»þ'Ð¦ÆV_-Û"»ç²ù ÙïÊÆ/<k¸º,÷
â4h¥´=!¶ÈSGÚAÖÀ[dÇ;äY²ñd3V?Á0^5D,á ¶qgè)©z\;içL í¿$ÄòìaÇ³§àö $Û®Ä<ô]@ægÙ|¾à_HÆ «ÌÃ¤ Jokúêã4©l>BÈäüÑ\rì9à¤Ì3¤ Zq°RBäR¸#±v\²WÌ[XC1ô#´óRFLÚîK<òÔG­Ê,rÕPþÍó ÙmÜ³åt`»÷Zv³Åðþ&áÍ~'12³?j¶8zjyU&á8Ù%ÙÃtsê¥2Ñ"f-R¸Ó"ÐW
>~+GÀCµ dCjBµÛi~Úý2-ëq¬5¥m¬ÅIPUÚåâ0v3È>ù/UÿÎ¶ÁQÏ· qý OÜá,×«§o&¯}¡P«I`°hÕØÑHõ|J	Ôeú[ FsÇ16uuº^
²·gímÇÀ±g¿äaTð ¸Ý®ÒøÅû4ÌÇlBk°7[
~ÝEGîìà-Ï»	%¦X²dõ,(Qð´õû¶µ<Gh%l!L QÍVª7Î?Û·AÔ2JÃÚ-ìÉÝÄÚt]â8pâZv½àãÍ~°ôàh5p î¶ø½ª­Ý"ô
/
Õ@*&òìó%üáR?ø8Tg×ùÔráàPq>ñ ´?qF¶o4Úl	OÕö£NÎµåê¦§=Iÿ%ù¡Ô89ìE¹ÛDi°Kbü¶¬"Ä9V§ÄN	Aï=d$K°q)RaFúZ¾U³5Zò[íUqÂ_ÎÐCê,ÃY ì§@[Ãd±ìkW,aÕÕkÜÇ*Ý­I×èZíâ¶r^ðRºzGªÊ?Ê/BÍ'9 ½Ñ
\y;ÔÇ>Zk"kÒ:#¿LkÚgê>ÙæÑPÌdÏùúÞl7?þ6hÓµû¨¦+¸>ÃàbîÔ'<T~(ñÃts´Ruil z.õæ_PS#Ô4¢>¦K_\f+îOÞtxûQWÃ{?¡"ìºlu#yòX×³=Í!ÊÔÛGöeL3ñ
ºúWÌµZWç@¿Ð<à$
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b6/6c92a4e1a4301e11b0585e96a3c9ecc25cc60c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b6/6c92a4e1a4301e11b0585e96a3c9ecc25cc60c (latin-1)

```text
x½XYsÛ6î³~&ñSIN¦IJ¢lÕÔar%!6Ç<4$åÆÉô¿wÀ -ÉqÛ)ìbËÝ¨e-ÙéiïÍ/Gkþ5J9û2¹æ³ñÔOÏ¡=²LfWvpe9¬wÒí2Öé°×Ýnë 7p¡rrÊF¯ÛjEé*Þ®9{¥mÙÙäÙE/Öe}Ð¾óÍÍ}ÞYíe®£ôºèHñÛæw<-Û«lÍ7ºÞßwÑ.º©ïÉmçß7tÙ¶m²(-	£i*¿^¢@ë8Iî± §<g?ÜS
ö;{ü=ÚßîbÆ tÂzÞ±¿Þ¡bõÅ*Ïâx·ö£/«aeiÛd)1 KñÀï
Ñ2Jx»ÌÚIø­]l8_·BHv»$éñÒ×<ïH- mÊ_aYn+¹Sxö99E'"8óèúçí
Ï£¬ùÔÑWG9ªEÑ©\wßâÆBö*K6 eÌa»Ï r»7íu®ø3	ÅñYGÅ·Pòn¢¯egn
æd«[æ6Ü¡w¤2¾
o%Ñ¥mK»QI<¹Ý0Çùw>ùCæ g`Í=+TM«AO±zò·L#´=ØoÁS(Ùva©ïùH-o@G×Ûkæõ¾;Ø
ÖPmßâW¹\A7éÿ=Ô!mn8û8à+ÎbÈd	¢ñ* %²Qøaà¥$Wezu¸Ë ²ûGÅGýfÖ]~´]ÿ3hã"=ú[ha¾ØÞ ×pz)r°
ò]ÉðÉÆþgÆb¾S
Í}¦$Òöx8"FiY}o>ï|`gÉÁÃPXAþH2ÎÃø©!bíXâÎÀ¹PRõº;>;WnÎÉÚþCÚ&±|g8ñì	ìgöÔ·]yà» Ì/rø$}Á¿~å«ÌÃ´ Jkú£ÄD9M&2ù 8S;ylR§ÏÈR#8#"ÁáÄã½bÞÜÈ1¤@ 2b`4ÉXOâ¯Aö8Ùäª¥8ûçAºM­ébÒ·Ýõ¡ÞÀqsÄðþ*áMßÐ12Óßj¸znyU&á:Ù%ÙÃtsD}Rh³)<è+/iâð_E£àÂÍlH­¡ã`S¨ªüSõË´¬×±ÔVXó³ êõvóÃØUfL!ûä#P¾Tóe«oâúA8<-×©§®WÈD](ÔÊ	,ö!YTÉXûSjH .Ó/ÀØ59°©«ÓõÛ »pmÑaÑv{ê%£Å}²ÌâGïó¤?sR0.×aoüzyP5À»#ª	%&Ø²dçÍ,hQðàº3×CyÐÛ02pID5G¹ª~Ñât_¨5e(¨$·3YQ-Þéú®5¸°Us>s­+».	ø:a³,<8+ê;ÐS¸Â«j¬·F;¨£ß]ua_.àÐâh¨3ìrb¹p âº¨"+Ú?rü±3´Ü«}3ÂTè)'	ºs1Lâ!3@È©bO|Mê65J&~Qn×QlÓ/ø"0#hSø ÆlUbªúäC&ªÖcíìYÆµIiÔÇ'<bJ ÔY%æ=ÕF½^hÊ Öû)®Ò`[ûùRR=9378ÇÔeúfü\Öt=ÂKÜ2ËÊ8á{e¿íµ×Xå®Nn¦¸/¼4
>âH÷Aq1G{ßWÑÄ¾¾wáÛÍ¦i2°j65äÿ	aØÒ9ýºËùjgá_(*dä¡9JèÄÝE57y1®fN}ñ ÓÂctSºRUÎ\5â·Kßæ &´F¨+MP¼&_6YÊ¿¼1îG]E¯;fü"\°ë²ÕEé?uíÍhQ¦Þ>Ê´°/CoÐq¸ä1þäÚí0©ÿ¢ÙßywP

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1c/c2b356238c1d926a82ccdc532ecb095c3fac19

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1c/c2b356238c1d926a82ccdc532ecb095c3fac19 (latin-1)

```text
xKÊÉOR06gH*ÍÌI±âRP(N-)ÉÌK/±òRâòóK¬ô¸ >ø
°
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1c/c3214880a841d90ad3124625f86f0e6c0697ea

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/1c/c3214880a841d90ad3124625f86f0e6c0697ea (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓúvÙ
·³w6nÎ°qØûä«ï/ªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  þ1T
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/13/de4a454d76746a1e0d3f1104652f7a0d6f53fb

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/13/de4a454d76746a1e0d3f1104652f7a0d6f53fb (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹ÊüÁ®§Ý««{4{}RBå
Tmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ ¢>?
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/13/fbf37a0229c48be47ac20b76b0853259e1aa94

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/13/fbf37a0229c48be47ac20b76b0853259e1aa94 (latin-1)

```text
xWÁnâ0Ý3_aùL#¶íµKOÕ®´ÚÛn-R $Eÿ¾3N<SCkì¼yÎÌ{6³.ëµÈò<ýò1Bî·òQH}ÖeÑ¾­6uSi9Åªx×¸´ìÄ[*s}ìZXÅðìVïcÙ­úgQ®@$ÄïaF!úAfS!7u	#3üøàôì«¸ØH~g-Ç±¸ápÜãTâËÇÃ-p9Ãá8oÎp8îqiâ{°¸$å8.µ69êÍïNÅY2OQJx¼ò¬RæYQUF¸<+Ê³Ê	7KÂ|g5g¸ þÔÂæY-np·Ç,~"x5&x£B@6pÁQ! g¯ÆÃø¨cWÞÂ3pVð1|TÀY¡©dDðïÞâÞ	q0Mä^ê]ç<ç3ÐU¼!Ü¡Ñm§ðPÃJÍF÷7Äkößûó2"OtÀQ1Ctà5dé2Bç^CZÜ­!123$Ã¡f®o 23$ã1¤ÿæb8!cø¨Ìé!'xÄqCBHøÈüOú
ÄâùyopÐ¶>U¡x^E¼×@y3P¨n^ÅðQÝ"té5ÅÝÕ8È	Ó]ÙÙ Î	Ó]Ùöêðü
þê2hõz`waÁH©î²a4â5óDa1Ë¼·¡{G'6Ø6¸ÓÆ;ÇÇ5ÆfDçÇIT,#Ëª0Íª8¼#nÕ2Ë Wó¿õ²ÕU[7Øeô½AßkÀyÐèLJ¼§WºÚÔ[ÝÅ¶mVæ6·Mt;ºêö»= °ëéÁWÏlê÷CÑí×¥iòÐNõF)Ga0Èåó¯ÕòûÓoËnYW`±­ê£¦z\&ÿ!Ü¸
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c2/7de6fe8bd5b05595ebc9d3364be59aeac181d0

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c2/7de6fe8bd5b05595ebc9d3364be59aeac181d0 (latin-1)

```text
xuRÑnÚ0Ýs¾Â/ÝC%Zm´Çq{öÍ`{¹¨(T!ÓD¿~7@¨´7ßsÎ=çÄÎj»[±/ðÓ(1±{=4Õó¦e7ëÏ,÷6%ûÍªÛ¦ZýiwÍÞÆ[]­Ëz_ÞªÇ²n«§ªl¾±LA0
aòD¥è@/s<ïKê}½ãÅù@E»(Ë%j ±+ëåj[²Iø2}cëæ°oÛÞPh#f´3ºÃÙ$ôNà¸Ìÿ+­Í®b2[ôæÜeHã.O-^«zÝ6ïùVå\DEÏÔ*Ó[tç+{oUÏÑñúÛTmU?³vÇ¶Ëý¦×^bô±DË(P&§ÍóuGÒ1lX$áÀPwäZ9&û)Î9ÐùO?^¨<¥'»D{èdcyJÏÃQäG*ã ¾ýBXøhu@¤»
ÁH.Y3îRM ÁDÜÝ/µI¿nBp*M¥ÃTk©<&Í?>Ù
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d2/49e8e02517fe4285cc4eb32c7ff0d943bd1763

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d2/49e8e02517fe4285cc4eb32c7ff0d943bd1763 (latin-1)

```text
xu?kÃ0Å;ëSxVéÐ¡²4¡Á¤ÔK!ËED$'¤¾¥Py;îq¿÷îõÚõðüòô@)%Ê
=
X
Bï¸jð(pÞ"Óxw	 ê¤Y%]^çu¬G5|3BOµRYy¿© ³Â6BtpôÐ^IÑÏ+yI*ùeâ]ã/Ó~a!NrÔ"¿0q?r/C
t³n÷oÍ}}ìØá³Û4íêVÚ²÷v½köÛÍ$:r©åÿv;ÎËø>`©ÚÀ<¦1Óû'@~ H&
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/18/16c559ea8bfc7932bb680f387fc373d05ab39c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/18/16c559ea8bfc7932bb680f387fc373d05ab39c (latin-1)

```text
x½XÝsÛ6ß³ÿ
^sç§ªv¦ÛÚ®w²-'^dËä¤íN¶ÙD}$gMzûßðC",Ûnz0	  ò2Îäììôô§£5ý¥|^sg2ó'³ó`dÍíSçÚ
®Môûôzä]¿ßÙ«â
]©¦qÜït¢toÖ|Ò|Sõò"[Ñ²ÌòÍº*£OÀÍïÞº2QºÒÛ²ÇuØ¯AhZ«lMË7wªÞÞÑ6ª©§ä¾wO[ºmlSÊBy¥àÓa´M·Kètä!`.qTV4¥ùA¸OM4Èoäc÷)ÊïA¹
c:!Ç>?? rõåªÈâx»ò£/«=Â*ÊR~Ï³pKöÀï3Ñ*J¨QeF~7ÊÒµL²ß²§¨¸¦qø(Dnÿ2ËÜ­äAàÙµÉnr1ÇYD··´0rZDY
ò¨ã^=±Q,FHÕºÿ²WYC1w_Aþ¼ÊFæÆ:LWôâø¬£2G÷Ó0aJÞ]ô­ê
Ã¼$v¶º'~Ñ½#ñ¼EWºÍí"KåÉ}NlkìÞÅdìz
¡9÷D¬P	!bõïB(>ïñ·¤)¬QdUX©>½ð5è¸õæ¸ç`àNv5.à;Cü"kè:ý£:$¬Í_ss@Î #lL¥L´W](<àÂÏÏE ¹jÐ«ÃM\]Ø?j>ê·³îêÆrý/ òQßBóÅò¸Ó+>ÜðÁb*Èw9Ã6vØä;3ó­Rhî\AbÁmO89NqÂ-àlàÍ¬í]òL>x|1}ä9ãTpX5 ¸=´/P³îNÎ/Ä6ÒÚþÛ
È±q'5pfÍ|Ëåh¾ÈüÊÏ|`gükÎÔ»TERÇ&º"æ¸MÍGb*6s¦S¬#¼{68Æ&³§efElÓfÑÊà("Ý¸"o77<?4éhçÇ
&9æx\ØL£÷²z)Îþ Ene0[L»·DÐ»í#ú3Ç5ûE:Çâü«¤Ú#®^^6|]ZÒûéö*ÄG6¹fÚ
ÏFtà­p ocìa¼®xÒ×9¶mbý×-ÈBçÙØ¬cá7RIóó n
Cù~ô"-fzüa8OÅüYµàªç#bõA.;)M×uD{S«×kl¬,n±
,ú¬®=©SRÝç21KÂ ãÆdTÛ»hiI®wñ¢<Ì¦ekHvÔMF%
ÊÇdÅÎïËtàØ/)IG+©ö¨Ào¦èÈê.ïXMËâÛq Ð¢àAö\}ÿÈáçG«ºù®NI®ùªøE³Ý"VAE2â;³mcâ¥åÀ5èÍç®ym5E"ÄYøÁÂC¢+©
í·Â}íÈ±)çÀ0Âk]-à¯NWÉý<g×ÕÔtáÈÓÐ²æb,-ñëÚTBªGÐ~á9º'-s[Ã°#ù¿¥ëâ4íMú²Ú¬£,Ø¤1ÞåY\ÆÐ¦* 8æ­
±Eâ2Ðáaüº3ÖÎ®r'öLqGÒ¥9ÙÌ<l*Ï,F#ÍöÁÇuÆIûò=1k;2KQ¦ÒQñÛqÌbï;pUS­1\áHweUð¡ÄáíÃsþ¾¹eA«æ~<÷«|,´Ò
ÜPAQ{¨OT7.¿êª+{¶ßâ0´toí¡hP¦ªø?kæO5°;j³ «­Å©°D;´G_r·Qm1KÁµc7Ñ-¢ÛÒµ:_¨3PÊÕ#~¸òDÿaÔT®IÔµ&(^ÓÏû°Ê¿¼¤I3lÜº^ôø!%qI¬»*[_¥þóX7»é3Í>J×ÛEéveH;ñ5:4Æÿ\k¨8Í?60ûúµQò
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b4/a0e599c93e50f4860e9d2291c2a59cd2f4a917

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b4/a0e599c93e50f4860e9d2291c2a59cd2f4a917 (latin-1)

```text
x+)JMU06`01 Ä¢\Ä(_MÛÓßYM¨fçx²7ÇË+ åS

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b4/2c01aab141976c5c4c81bd2359aad580d5678b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b4/2c01aab141976c5c4c81bd2359aad580d5678b (latin-1)

```text
xÎAÂ @Q×hf ã	Ü»a¨MD¥÷·ÁíO^òS«uÚàt]DÓäl!IÌ¡@ã²q%è &6Ô»¼@È9	|Î²
ñA\$DK>GÅÛx¶®ïmëúÆUôy¹å¥¶ë\yyR«Þ!ÙÆë#X µ×ýoÈÿRuR_uLBE
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/78/0cb342d0dae71a13896240bb77c8d88f8e4bc5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/78/0cb342d0dae71a13896240bb77c8d88f8e4bc5 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹{2Øo¹}MÍ+Ý$7cÑ|'Áî_Pµå©Å%z¹9ÓvMÛö"£8ÙH%ýé¶{{xx Ã6?æ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/78/611bcca6982af834b0f534a0c9e246d968e53a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/78/611bcca6982af834b0f534a0c9e246d968e53a (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹7xeì÷c¤i²¯£U4h-÷¨ÚòÔâ½ÊÜi»¦mM{ÏQl$ÅþtÛ½=<< ©H?!
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6e/71c2d29763a2210929564c32d89bcba294dcbc

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6e/71c2d29763a2210929564c32d89bcba294dcbc (latin-1)

```text
x½XYsÛ6î³~&ñSIN¶IJ¢lÕÔaRr%!6Ç¼¤Ü8þ÷îX ÇÓòÀ.öøÜ]@ZEé÷z¿lø×0áìËäÊÏÆÓÅxzáíµtþdvcû7ÃzgÝ.c{Óí¶ªx×*gçLhôº­ÖI¬£í³÷amËN§k^i^¼ÜEøAøÎ³»Ç¼³)Û«0ÙÉmÑ:âÝæ<)ÛëtÃwºÞßá>º©ïñ}ç?6té¶OeiÏÑ4ß®P uÇ¾ÁÂ¢ä	ÏÙ&cªwýÉÞ~3ÿÛ£_¬ÎXïÃ;öÏ;4Q¬a¢Xçií7Ã~´àã°`½æà#(Ã4ióoYÀæ"t)øâ]!Z1oi;¾µóM;.d·K²¯ =PqÃ£àQÔÒ¦|Ë2¬øAá9ää<XâÌÃÛ[·3iò
¨£¯rT%¢R¹é¾ÅÆBö:3Ø UÄ!Ü?¿r»²ö&HÖüâølÂ"Ãð JÞ]øµì¬`Nº¾g cÃ=z'*ãÛðU"±»¶´ËÈû9öhá{ãÑâÃ¯9ÀXsOí*AÐj#d£Ï¬ü-Ó-æ#ñ<mçizÌ'já(|:ºÞÞ2÷¢ï÷Ý±Àn°*üf_årÝ¤ÿoôPL´¹áìãT¯8Ë9 6&V&Æ§.CÈBDáÝ"\AèÕÁ6*}È.ìõYwýÑvAéÑ¿BóÅö¸Ók9|-TïJÆl±É1qf,ç{¥ÐÜgZAb)m#òg4vÕ÷æÙñ.G y<9ä$ãB0W
kÄbwÎª×ÝñÅ¥rsI&Ðö_Ò6)%ä;8ÃgO ÙÓíJÌÈü"Or»/ø7Ñ¯|yDécP_QstSñ(g³É¶L>ÈÎT#Ï èxºô!1¢c9bçR8ØiT²×Ì[1ô3´óJîSÖxÄg=Î@e6¹j)Jÿæ¹lã'ëcºôm÷h}¨/pÚq{ð¦¿S¸3Ó?j¸ziyU&á:Ù%Ùãts6ú¥2ÑbÏZ¤°3"Ð×
>^ÒÄ#à¿!FÁÙZCÇÁ¦PU;ù§êiY¯c7¨)­°æ~Õ)êpóãØUfL!ûä#P¾Ró²ÁUoaâúA8<-×©§®WÈD](ÔÊ	,ö!YTÉXûSjH .ÓÏÇ½j8saSW§ë¯AváÚ¢=Â¢í8ÔK÷ÇxFO(ÞçIæ<§`]®52ÂÞ5øõÙ©ày(%\`¿8whfA×¹¾¯È	}
#]D@Ts«ê§*D­)(*	QC3YK*Þæú®5¸²U[¾p­».ø]ÂfË¿ôà8%ªï@ç=Màò~h¬ã"ø5lô»¯"ìë%üÖX´´?
ózb¹pî¡º(Ä*º>rcgh)W;4g¨ÎstçâfIÿ5ù©Ô(9ìE¹Ý©¿M"¼Ô]Ak¨ àH¶'Ä:R½IÊ@ëGð«î+X;¯ºgÖ½ÈF¨i%xÄN&A¨IÌ{Z³^cd^ÛWhÝ¼#éD]á
Bòû24e£FOçCeFHÔët"¬Ò´Ò ~@O;aÎ]øÏnã¶
ÍXFs¶MñXø9/x	2ZÆ5>úôáëhÂ´3;Ñéç&d¨jÄ©áTN!8	Ù ¯ÍÜZz64Ûº22[sÔj¾ ~SégiÃFÈ©ñ@ñå|½·úÌ&êcæ(áwÕ7sàßÌúÆ"¦§è¦t¥.ª´#¹jÄ|>ëÌ&*ª]iâ?Y.d¥]ù7/2#ÆÃ¨«Ã{¹H.ÂZ×d«FªÜÜqº¹Z©Ë#ÓÈ"¦Þ1J×:<7-4ímÀÄ7è(Xñÿ=rív¢ÔÿÍÀì_Â¸M
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6e/d22758310cb308981e5a321910ca47164c35fe

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6e/d22758310cb308981e5a321910ca47164c35fe (latin-1)

```text
x+)JMU051c040031QðNÎÏKËL×KÊO,Ja¸ãô"`Ûõ¬ÜÕ.rlîMyGMaJjDÃ.¶´¯Àõkg-ZðëÄ%¨b°izÉ¹Ù©ÝÛ=ÓOùgµRÑµå_?×~ô^UV_ªX_ZR¬RRÉ`f°øÉïùºì+5®¼;³t­Ùztzz¾Rf>áñäËSxß':[:¯a¨ÌN­ÌM,`ý[qTvUaßÍïÏý.'Î9¡¶217aCNëãfý	lp&ÈæØªkWª0TVåfëUÅ<´%"ðY±mØ+ó}Z]ªèãsRÓJ@.fH¨°L\*°;ï²L´öòäÉµ°ªGó¡Úgÿº¯núúäe3ï§³^l¼¡§(3=bÅeçÚ¹bmÁCö>?ßNöçÀ®É%.SÊIIòÜU÷O·ÑôÊ Vßã
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/14/904003b3b86d22f0e0333d0e57e303732931fd

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/14/904003b3b86d22f0e0333d0e57e303732931fd (latin-1)

```text
x½XëoÛ6ßgÿDP×v[Úm)ñ"Û$§/l³½ ÉYÓbÿûîøHÅvÒ5º'w¼#©¬âlE^Þ¼úåhC¿D)%gg³Îýéü$±´ý`¶¸0Ã&Ãç!ý>Ø:M¼±k3ç¯³:£(]ÇÛ
%ï¢4ßVý¼ÈÖ´,³¢|¶©Êè½¢ðæW·ESõVQºÒË²ÏmØoÞÐ´ê­³
-]©v+zÞD»<ª®¾%×ýU¥[¶å×ô¶å»­m+â¥<Ò
ð¬¸\¡B§$71£²¢)-ÈwÂcn²Eþ$ïºß¢<øzë0¥çdøþ-ùç-º(×?à¢\YïvC¾w`ñH¸^S#¬¢,íÑ¯yBòNÉ¨S­¢öª¬_{eNé¦Ls0ºX>/ |ÐpCãðV¨4
Ü'ÿeyXÉÀ³oW8É½9Î"º¼¤E/§EÕ _9ÎÕÕÅ$hTmÇø£°½Î´)ûêë©4îUaÞÛé>áàPMTæ~&ÌÈ»¾TýqÄÎÖ×Äs2Ùaw$:¢«³ìÊ°¹_BdË°:¹ÎmZ~àN-ÿýS¨à
Ç¹B#ZçaË{EË¨<&
ñóÇáÆÇpÍ¹jzS¯ÿâPFèNONý@4ÙWÃ]áúVÇD¼<b#×þOèÎê³_©cþ¶gñ0Êc¡ùq¸c¹<Z°4Åí½8&
¡t áJÂÒ+²*¬Ô¦;ý£õN½½$îÉ(¹S]cMD² ÄfZC×éÿ=ÃÅ9_s ¯[w(ef|	lDü$À5ºx®åQ;ËD¸« ¶7<Àj>Ú··½ó¦ëkÊG]nX¦7F¾óáLf|3|écÿ§,a¥³SÝ}$Ü÷TòpDþB¾p?ÈyÎA¶½SÀ ÏàÇ	ó|3NCûi âæ
j	¨ÛcûLh5r¶Ñq?§Òúþó¤!ßÆ7|ñÌÄo°.Ç<ö]P@æg>|äË>ã_pÆ¨«*Â´:6± UxÇij>31Ùb6ñùH¤åÙ$SÎV3Ò¨b6Ë\·#Ò+òx1æ£iÿ ~^ðÓ$#C7ìÕPé\-³¿i¤ÛäÞþ/g#Ó=ØbºíÓûÃÿ.cÄÌÌÿT{Dé©áÕréWê¦ÛRHÜd)Kå¬#
îô¥_ìað_KJ&Ò·Ø6n
u·Ëùe÷ó²lä¸4ÒXÎIPïM8Kç0vQs¨>þ0/Äû¶A©ç¸yÇnoë.Ä§6Êkd¬/j1	ûD6YÔÅØÌ'Ìd!9/¿ sÔdaÛ:Â¶­J7«!ýÂ½YyGÓÖpìé"J·É*ï9P¼O³ÑÂ~HÃHTÛÀ$Úîª"#¸/6Û7
×³¡´HdPÑöÞx6k+ÔáÞÅêØòÍÚØºêå(ð±IK?Ù¨$¨5Ø>
%JOh9.k]l9xËY£)
³¯QøºÑ>q³Órö(¬jHK]2&|»ZÅ<_Â)¤»?<Ôü8ÇÚùÌpáLd)cæ8Oæ!XºL:><"2×ä(µ ¹³ôÅôA,+=ØeµÝDY°Mcüð¬Ó/cB8H,8H½÷á©ÒîÉÚ½Iä9*XÏÖ*jî*Ëª8áÏÐVCâ¸°à¸`þµ¢«`2-<¿[Ê0-q;³ØøíÙÚt®Ó-oË  %­x¨wl©8,8RèM©'¤*°Ë/ª\8¢·6²6]£ÓêK÷Æ©}®vé>'¶j`öt½³Úõ¯v¼-ZmÕ×g\,ìæ *uBý0ÝÖæ\°ÿ"÷~WÞûõ¯ FÍ¤L¢3!ê³`¶ôÙ}·æþäeHKæ~ÔuÆðê¡çOÅ%QIìªn}iyô\7³éo:Cn·Ò=ì«váktý/3×+;8|ã¤0Àß¿÷ïØ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5c/d7c9a38ebde8ada1fe1ec06e0b481bc928d45e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/5c/d7c9a38ebde8ada1fe1ec06e0b481bc928d45e (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó
y¦í«yTêPræø²Ù*|EÖU©EÊoß²+ÿe&¸dýæ
¦Ï  ÐT2
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/89/e8c4c468c9079dc0fcf1c58bd243c30e62efb8

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/89/e8c4c468c9079dc0fcf1c58bd243c30e62efb8 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥aË§3OÚ|iã«4ñÐÒ9¾¬T¢WÃðÀgÆÏ'¦9Ï­7~bïÿß®ÉÁ!Æ$çç¥e¦3DÆ½_®ó(fQãQf÷-Öþåå¥U©EÊoß²+ÿe&¸dýæ
¦Ï  õDV±
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/89/bf9e7c9ade567aaf51a2ce85d8f07c608031ed

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/89/bf9e7c9ade567aaf51a2ce85d8f07c608031ed (latin-1)

```text
x½XëoÛ8¿Ïù+6`Y½n×í8Ýæê<j;í¶/h­QÇ6l§[7Üÿ~¤$ÚrG÷ÀEdRõ#ERtçQ2g¯;o^ýq´äÃ³O£3:½áøÄ1³=4¹0ýÃfÝçcí6¬é4ö.qû-<ÅÄn§Ñ8
ãE´^rö.ÓuÑN³dÁó<ÉògË"ßkßxz}µEkÆË0¾ÊÛrømñ[­E²äù³k}Ý_·á6ºªo«ö¼¨¯Ü¿áwº7%uVJ0. ÿþÍ²«9
4«Õ­/Lô£0/xÌ3öI+o±¿Ù»æ·0õ¿Þùù"@è9ë¾Ëþ}*òÅ¨ÈYEÛÕ°ï
8<,ö0[ükÄà|Ä["¢#DpÅ[EÒZ_[yÊù²µÊd§C²>/ |páGÁ©¤Nù+4K³V·
Ï®M^á&KYxuÅ³VÊ³0)A¾å¸W[mT¢R±ìãÆBö"Y¥à yÄÁÜG_Oiq«ÒÖ2üâø,Ã<Eóã`%¹×áç¢ÝÒÙÉâyAÊ[Ö©hÁ©DÂ»d¶ÔË¥Ù¦åùîéÐòÞ?ÈNßºÊW¸¦ÅiÁñ^ó<ÌFüºÁQ0çºgj8æØ;5Ý¡»á´MSH:ÃSÏ×'*ïëæÎ³`qÃc¦^~£=ÇèÞ/èôÎÊ³ÇÓáÔ|²ãðÐ.má¿Ùó7ØáôéxÐº
zB9ôyå=;f¡´'árÃÒÊ"(ô¤;R{ó§;¸õú9'=¿çök L RÅ´^§ÿoôp0q&c¾äÌ¦¼Ly¬PZ|2	®Á"yàÝw¼ð(B3¬£ÂòXÉÇõeïüÒt¼°'éÑO¡Ëtû8¯çr¸) ßtìñe¢©M·J¡º4ÄLêGäOèEêAVÏödÛ=µ ò9¸r-È·$ãD0j?D,Þ ¶q»o)©j^:©çT î$)äÛø/®9{ð
±éHÌ}Ïd~Ã9ïþdôÊ½,s¢ô±Â¨Ï¨wÜ¦ä#1RMF#p|?(GZ®
F
ÑáxæÖbElÃK ;bÍ¨`/;5ú2bjÒ?@ Òc t°®Ä#ïqÉÖPÕ\9%_xæÇëÕÁüÏF=Ó9ÒTGQèß¿$¾ñ2]3þ¨ÍgO
·%ÇRV
F¢åÁVóO¥¦ù¡'åñÀ´MÏ|Ò  Û¿VÈñB<ùK¢h\ø,)]¶¡ÌtBNOÈÈÒ»çDÉôÄM~¡@CÈÉGÀ Á§(i)ëz@­á$lÙÇ¨2§gÎW)Wªãñåô`\Æ]µz#H4V:dàùàÙ<%h÷Mó5$;#ÂûùÝjDn÷ã¨7±etM àòÈÜ]ã}Ñ{¼³©ïÚ"aPbeI9Þ¦7
!½¾
ð5É&3ÏïÙP vÁÚäW0qóñ®,PsR%UÈU6áLÖ¤NXãÄc\&!¹ÛjÍfíÙ ëH·¼y>1à{"ëÄ«¬ÈtTX64
éÑtÏe n "Wý£ØÝªã5RÍC¢úsü ~Èïæ¼X/ÃÄ_Ç~#ÞyÁzð±gÚâÒ«(¼¦*jR7kMn­éQ^BwXpn1ªÆêja¨ÜÓ'I%4ôB9sê5 Pí5
kõè(M½Û@S¥3LK5[ªDøp­Q]3V]DARám4ó»ÜÏxÎd6Æúìaª²Þt¨=Gv5U5Ü.»ºm¬.2O·um¢%©m«Ì£mÊQ¤òï¾Ø6õ/e:"*7!whsÕ¬ÄN²Û-A÷ý
·~%Qµ7ÔRüX3TU5ÛcÏ?¢_|85Jû¨Û#fèuÉÊ_m9 RPicËÍJç
 Å¯»RGòk+kÐá?ÛÕÁïë´¨{uEðöFn§kéª£òògÙ×.øLÇYàï?éMöé
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ae/a8b52f5ff55da3348c964dc95a726ccaa87d80

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ae/a8b52f5ff55da3348c964dc95a726ccaa87d80 (latin-1)

```text
xA
Â0 =çù²én²	øï7éªc$Mÿo¿ài```J«uvrt]Õòì"gG$(h(>¡
Ú1¯týsN4{ÌÈAÑÇä£'uRGÁÑÈ6^­Û{Ûº½IU{^õÙæ¥¶ë³Êò>V/Ö±}´G@ ³Ûýoèÿ¥ë g~ùA÷
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ae/32b444f9834226ea08e997fd4b8af0bea675bb

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ae/32b444f9834226ea08e997fd4b8af0bea675bb (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó¦]=uéQÕ×»ïÒV0=­ïxº¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô ¬ÏWÒ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ae/f6aacb7aaf29665d1600d63ea3af6f605f5005

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ae/f6aacb7aaf29665d1600d63ea3af6f605f5005 (latin-1)

```text
xKÎÏÍÍ,Q0²´d()JMUH6±LM6I4µ4KI60JKIL4ML´LINKLN3N²H66MJK3L6á*H,JÍ+Q°0JK6N5O3I4M6NI45LJ±L4KL3726N36JI4OL²L41äJ,-ÉÈ/RÈN­ÌM,ÐMMÉ,É/NÊ/U°±4´0±471ÖÆt(-N-*ÖËË/J-È©ÔKÏ,É(MÒKÎÏµS0473µ°03´4WÐ6000àx¥$¦p  ~d
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b2/8db79afe7e8c0504c5c15ad4ba6ec35fda8dbc

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b2/8db79afe7e8c0504c5c15ad4ba6ec35fda8dbc (latin-1)

```text
x-YnÃ0Cû­SÌR×N·ú
z@ËÔT´ÔqNßtÜ/µO¦yy!±Ña;zUÝÍ¤QDPÂçÁàÊ¬/Áµ«ëúÕ¤0¨å2.Ó<~Gø>EÜþOÚ'Át¡qT	¢¥äS¥ 8Á³ÛÛ5öç ætÿVQ{Î©4´Ç\YÃm¯úfñrÔþPBÄ÷·i/óX7Õ³iå°fJlj&ñÅR¶
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c4/f5f20b0bde38351d0ff54961ca5f72dc06b6e1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c4/f5f20b0bde38351d0ff54961ca5f72dc06b6e1 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg0[ÖÜÙôþ)gÏ]F»¾w¥x8AT¥dT1(¿}\È®üyràõ7^> »VÌ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c4/9ec4a596dc02fdaa5aa9dcfacf3b8c35bff1c4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c4/9ec4a596dc02fdaa5aa9dcfacf3b8c35bff1c4 (latin-1)

```text
x+)JMU02°d01000PÐKÏ,É(Mb`{È'vTèrWíÁSÛÿT&d¦çå¥2h)ýMÿñ)aJje¬+ûú½sòRzBæÛpü;2/Ó¤yÑ¯;?x5&©43'E¯217áçªâÿZÏømÖ©ÿpÓy¯x2Ääü¼´ÌtKùïË}ø7¹tZuÒúhSàWªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  }îU
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c4/e5fc1a0adcd14f00f51b69863fccb2f3a66301

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c4/e5fc1a0adcd14f00f51b69863fccb2f3a66301 (latin-1)

```text
xK
Â0@]ç¹2ÉD<{tZÆHÞß^Áíã=x¥ÕºmÐFÑQì4»0§L¢5|áÁDã S61Dõå.¡=@D#Í4Dà 8I9'lâ}¼Z×Ï¶wýà*úºÉÒ¦µ¶ûRy}_J«7Á¡'0õ@ôøò©Æ6U?A
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/67/10cffc706d3c44cc6af542880ba6d90fe74072

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/67/10cffc706d3c44cc6af542880ba6d90fe74072 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó¼¯T2§³ÓÇç«§fõ¦
-U©EÊoß²+ÿe&¸dýæ
¦Ï  T
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c5/97c11b11908a0f00b8020b644a269182f1cda4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/c5/97c11b11908a0f00b8020b644a269182f1cda4 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgÈ}ÌoÍõí®Ó8îømQPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú ¥ Vz
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2e/a08df9ea2303c848e4f4e5285f4de42cb489d6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2e/a08df9ea2303c848e4f4e5285f4de42cb489d6 (latin-1)

```text
xÕXYsÛ6î³FñÄÒ<d'êfêÚJª©li,çh_8	I¨) ËNÚÿÞ] $A9r´/¥Äß^¸¦Y1%/_?xÏvàågó$O=úá¹ZPòÇùo0KÎ¦+YpñÙwÈêRK6c÷Èùà
Ey;;^*{x?î<ay­RJó§,ñr>;üè#ã} c¯,¢TºS§,/£)þí/¶|Z^{Ë ÝFÇ¹|Ô¼§I<§nß+)Æ $w<Ë"¥ù4Õ@R,ËX²iFÍhI9+Çpj±@¬© ¹r?ÑrqÇÄ»eÌ%¬ÈAÒ.~ê/ZÅ x¼D2lý{£³,V{|yí\$V*TgcpKIùòÞ`ß
¬«<¥|kG¼Z¶iÀÁ83DÊÎâU&#íÛ6ù4N®3O@X¿h¿×Qå»¶ë!ÊAïBò¸7iº01ªäô?\EãÑûþåBè­tËbM¹;§931RÐû	¦x¹óL;ÞÅO.y3¢Ó«Á»~ôëàÍ¯¯;YÎ¤ùß¹KÅuèÑ
YFg2¢9
Ät"üºjÂ¡IXðâ
`	|òtùK¿£·ã=éô¾o $-ÝÊDt±\áçNÊDµÐýPf­Æbp¯éÝ2.]CjY
98S.\(= K×ÐqphV©À ÙîÞ.ÑUòYU­¼]ç
Öò«gÒ:¾¦+ÀZ¬xBDHÖyÊ`^0;I¼X[¼ð¦£PëFýV®½üJDÎFï/ö^µ¸:Sþ
sþ+îàû¹òV7/?èÓ/ïÿG÷+}i×4i<ô°úò+¤ÚU½V3z½BÁ¨òlVØÈ°uÉ¸µ «  X«e®fàÀª`(={Zß°4ªf,V4.Oú¿GT64m×´¦=Ü«Dµ[Í\Í£?U^G¦}iÚ ÖìmÂ
¬ÀÑ°GÃ
-5p4¬ÀÙªC'ÐÄU§«:h&È«hX£atîÃ

,P¡
¬ÐÀ

¬aº.·¡õUCÖ°BGÃ

¬ÐÀt6`µÄ[/J½Ú5°ºÞ²Èïu¿ñV×Àê¬:TkC½=ér½Ulûã.Xi
`EO[uà»Jë]èøÄ'ã÷çÑù¤ÜSýñhxr9¸ú=º]­äjDÐ`]îÆibJ®Yoëø0¨qÜªHúUªn·	¡w´Ñ*MüÙ]iúµÙ¡8c Aäy]pØssJXÛuµ¤;DPÚ«(R=ÏKDìk%/þu¿às/%ÒKé
@3<µn¶Ôb!æ©¶ÞnoëÝÒ´Ù©Ûñ}§)§B¸	Í2={Y±z"Ø'ÚÒºÁ\6° µªcÀÏU$Oà§sàü[ß<DuÃçðj©Â`W,íc-\q¿WÔ¶=®$(¨B"©£ >|@öÀi&Xj4$ÎSØÞâÁ
jÀ©Íº³Ù0
ÊohJ ød%(Þ	ÇÌ¸,38\àæißâ¶ºdÇÏxN75Ë22¥('EA¯OñLÊ¾xï&67<µCµåëô@þåxi?7òÁv©×á;Ú³iQÈ/+ ·+ÐãZº»¿+J8oKU¥Y2?2kzëÍR6çÅª¬JeáS
ªsýâòu4ôO'ãÁy49ýÍ!¾÷{¯?é¸M|>uðâ1ÔÉHË>´O.`®r_Ù 2JKcêÿo¬ASàmÎ¡:#µÆHÓ(qÝh¢g¿}»½¸øÞ^Aèøí~ÙÃ¨\©1núÿ©BTóh'@À»ì·oÇ¤RXg%z!/Ï#ï'áQFïðáìäê¤Îëû¹×Ü3ýÿF­ò±¾ÁzÈa	n]GàXá5´¯PôÕ·'@³ìè3Së«3(2W~6ÓKE4Êúá<^R\;f¢é8¤£èDl\>øäùýCÙË`ÊÞÛ§ o*L´]¨4è&7¾Egv·QÑú.×©¼§v±IªáÐ*0¸ÿTwv=²Í­=FêºàY*è9sBU§ W¼÷¸èp|ªµËåasÈ':nINa&b¸YÄùªû[[ h»[wÆéÇÜá=ä1®yz-«t]6s²Yî|.ñîó8wJ.àzw÷¥xS¨öòã(/l$¨uÂ©´à®ÔRÛ°aÿ,:
GÑà,zsÙï_Ö§ËþYûÃ/Ã·}	R~ÿîdå
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/58/e8a8ca402917ba3a89a85e78e4a0a13fce030d

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/58/e8a8ca402917ba3a89a85e78e4a0a13fce030d (latin-1)

```text
x½XYoÛ8Þgÿ
¢üT×vÓvwÓnÙ7òINA¶ÙD.Hr¶i±ÿ}gxTl§Ù+¦æä7ÃáÊ*ÎVäMïøø·£
ý¥|ùdæOf§ÁÈ[KÇ¦óK;¸´ÒÙëÒíM¯uÐÄº3yù0~¯Õ:Òu¼ÝPò.JómÕÍlMË2+ÊªÞk
ßi~}Wt7Ug¥(½*»Üývè-M«Î:ÛÐòÅµn·¢×ám´Ë£îê{rÓ½¡w
Û¦F¶­ åJy¥à3a4]W+Thµä6`!qTV4¥ùAxLu6È_ä]û{ßîrÆ ôôß¿%ÿ¼Eåú.ÊuÅñn7äGë59Â*ÊÒýg)$1àìï1Õ*Jh§Ê:Iø­Sæn:IÉ4{=©åqåwB¥Và>ù/óÌÃJn}¼ÆIDÌqÑÕ-:9-¢L|æ8WWL¤EÐ©ÚôNðGc!{%9$hS÷ÔÏsiÜ©Â¼³	Ó5}ÆÁ¡:>¨Ì1ü4Lw}­ºÃ0/­oæd´ÃîHT|V%fÙas¿È-Áêä&'=öïl2öß?ÊÎÐZx"WhAKã<,`y¯i'D#~=à8\ÑÓ³°\{æÙÞÄkää?Æ¦9ºÓ3?ÐuöõpWE¸¾¡Õ	/OæÀµç¶ÿ4!
gfxi&¢<.úÄQÙO}?"Û¬L½@¡O4Å¾^Ðâ;°KÂaÒ)²*¬ôÝx$7±©pêíqOÁÀ°ÖH +MtYÝ¤ÿoôpBv æg¼â,\õl]Zg|	t¨Jù~â¹
ÔÒ[D¸« úlkÜìm×ÿÖ² qÔW¡ÌöÈÇ×>|älÆwùà3ÆÁ<~	»Í,;qÏRÄûHÈËîYo1dïl`gñÁãÃyAþ3NÃø©!bWµÔ¡s.´j9ëÜÏt¾?p4`"ä;ø/=xð
º´írÌCßd~áÃ'>°ì3þ%gÔ\U¦¥¤ô±Æ¨KÄ;N£øHLÅdóéRÆäæ"cÏ êd¶ôlDÇrXæ2¸6v\WÄ[XC^1ö#ôsÌ3Nô9~±Ó×@e69%³¿i¤ÛäÁý1[N¶{ph7GLïïÞì#ffö§¤#JÏ,OUÊ¥_©{nJ!I²ÉR4ËYKÜè+?ØÃà¿¾I¤n5rl
j·ËùåîçeYË±Ô¶±§êu8ËÅaì¢2fP}üa(Åû½mRÏ· qý ]ë,×§o&+dl_ÔböÜd5vt¢±OÉBs^~æ¨ÑÜqLM[®WCúµö0¶càØ³_0*iPÞ%«,~à@ñ>Osç1F¢+´F&±7G
~ýÜÛ5À;_ÃvjL±eñ<.ùfA§­_ÁYªù9"WÂ¨TsäRñóÏöm!îeXo|7¶¼A3uºÖ¥]oø^&ó¥,=8#Ú8ÐwÛ)|Të°$zj <ûb	ÿÀ)?|³ëbj¹pð1¨8{PÛ8#Û¨7)mÁúQ§NçÚ|uJ3RÄ¢ÿþÔ
j,ö²Ún¢,Ø¦1~n*$âSb§£÷<Æ%Ø¸42'}­ÞÔlæüV{eUpáç34Õ¤8Æp0ÿÆ)ÐÖ0ÙclûÃÃKgØcqõ÷±K7gkÒ5ºV»¼+´â¡Þ³E¤¢ó¡ó3¤Ðó¥H>èÀ.¿êrá¤ÞÈ´BgÔéSû\íÒýitÚ jÙSì]ï¬vóS o6CÛE5CÁõs§>áAEÅ!ÔÓM©2çº56Ð²K½+/õæQS)¨åLú<.}vUÜ_¼éðö£VÃ{?D%±ëºêFòä¹®g3ßL4(ÓnezØW1ÍÂ7hõ2×j¾¼qRàï_:êåî
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e3/3c83bb1bae62d4c9392fec61829995cf63b9ba

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e3/3c83bb1bae62d4c9392fec61829995cf63b9ba (latin-1)

```text
x½XYsÛ8Þgÿ
N3ã§ª¶Ûc;#ÛRâ|DÓãE#Ûl¢®älÓÎþ÷xH¤|¤ÝY=  ¤½³yuöæío'ú-J)ù:½óÉÌÌÎ±eKÇ¦ók+¸628í÷	éõÈë~¿sTÅ¹S9}EÆ ßéDé:Þn(ù¥ù¶êåE¶¦eåMUF4¿}(zÊXEé&JoÊ×aoÞÓ´2ÖÙ/nU½½
ï£}US?»Þ}hé¶%²m(Ê³(­ £mª¸Y¡@§$÷s!£²¢)-ÈOÂ}j¢Aþ º?¢<øþë0¡S2øøüýMë'(×EÇûÍø8$\¯)ìVQô{¥\Ä[²¾xVQB*3ð»Qæn¤dý¾Åô8ô@Å
Ã!ÒpüÍ,s·{çÐ&¯pGsEtsC#§EÕ _:îÕÕÉ"hTmúïð¥°½Î´)¸ûòç¹T6ª076aº¦Ï88Çg9º	Sòn£oUoæ%q²õñÃ÷è7à«Ä,ºÒmnY,OîrâX¶xÛÿø28#sáX¡8-6B64Åê)ÞP|>âoIS(Y£Èª°R}>GákÐqëí
qÏÁÐ0ìk,\ÀoøE.×ÐuúÿFuHXÏ?Íø³\ rac(e¢}
èB	ä/DÞ
<äª
B¯·q@vaÿ¨ù¨ßÎº«Oëm\ú:/7Â5^ñá,¦|3|iãðM°3c¹Ø+æ¾È$ÜöDòpDþ\N¸d
½ÅAv¼À ÏäÇ1³|3ÎC{5±v@,qgä\
©fÝ_m.¤	´ý'·-ØòáÄ³¦àÎ¬o¹óÈwA _ùð,úÍÃz¯ªÓRRêØ`ÄTWÄ·©ùHLÅfóéBÆäçÂCÛsÀI&:-=-g¤QÄ1¹'Ò+òxsÄ3F~vÎxÄÀhÇÃ>ïq*½ÉÕKqö-t<Z³åth¹GëC|n{Äð¾áðf¿K12³·j¸zazu&áº´+eÓíUìC2%ÍbÖ
;#})àã%=þkIÉqáæ'mp­±ã`S¨«]î/«§e³Ý ¡ÂZu§hÜY.c1ìãCy&æ;e«oâæA;<M×§®×ÈX]ÔbXìcYd
v4R'c³Pê<ý-Pã¹ãèÛº*Ý|
i®-ÊÃ,Zã@½aTÒ |HVYüÈâ}çÎS
F¢+F&±·G~3EGvªxÀsX5¡Ä[ãÂ3Z<Ýò8­/Æ
~È¯¡eÄÅdë¼\9òUñF³CE"Ö9 D*6®áWKC×]Z¢9»æµÕü:!ó¥,=8+º:Ð»)\áa«zl\ÛEûî«ëj	¿øðA	GZGâ».¸^Ãeí9þÄ[Zî1c{^S=öNÜÎÅ0±GO5
à[úK·);=øeµÝDY°Mc¼àï¦
à´ÅaÃ¸ígwF»k$î-72PòNú¿ìtWYVÅY-\µ8ç
ç©]eC9©×-aÙâf°c·ªmnÐuºåC´¤wuGSÀ>H¡ÿK9 uP
]~ST×Z{iNË/Ý§Ú'ûË<i´Ts ÙºÞíúÏGü×]ÛGµ]ÁL×s§9íA¤öC§Û«µ:_hÚc=^ð]yÁ×¯ûÊ5Zî¨/éÒçMÚý·iQ×Ã;?Ä*±«²õíä?u³>ÓÑ£t½CnáPÆ´_£ãpEcüçÆµFJoþÙ?¯«<é
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/11/87e08a24475c8bd83fdf418ce90d6868a773e6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/11/87e08a24475c8bd83fdf418ce90d6868a773e6 (latin-1)

```text
xI! =ó
> ih%1Æx÷M«ù¿ó¯T¥¸·¶Lm;Ì!¢Ñ 229ïM6 ¥­ÕÑGN¬¾yÈgêRJÊà*aÁàs@¤b¢HÎ±ù±Ç
ª¼ÍWúÞ·¡o¹>¯òìuiýúlyy¸·6¢dÑè# Úéþ7åSÍu:P?zéB
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/11/e80f514a258b618161551e7ff4e3e6477dd2e4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/11/e80f514a258b618161551e7ff4e3e6477dd2e4 (latin-1)

```text
x½XmoÛ8¾ÏùÂ
°,ÉÞ¯Û
p»ÍÕI\ÛéÖ}1Dkú
¶Ó­î¿©[JÓ¤»õf¡IÔCå.âlA^÷Þ¼ýã`E¿D)%''3Oýñô(1·ý`2;33Ã&ýç½!Ý.ØôZ;M¼¡k3ç¯³è÷Z­(]Æë%ï£4_WÝ¼È´,³¢|¶ªÊè¢ðæ7EwUuQºÒ²ËmØo^Ó´ê,³-]ªvz^GÛ<ª®¾'WÝE¥[n_Ñ
ßÙº(ö(åYV÷dÅÅZí$¹XAMiA~s-òyßþåÁ· \1(='ýïÈ?ïÐE¹ü	å²Èâx»ò£GÂåÂaei~Ë³pJö@Eôj%´Se$üÖ)sJW¤d½ÔÅòyå+7B¥Qà>ù/óÌÃJ®»&yìEÌqÑÅ-:9-¢¬ùÌq®®¨.&Á#¤jÕ;ÄEâeä EL!ÜGP_O¥q§
óÎ*Lôêø¬¢2ÇðÓ0aFÞeô¥êÃ¼$v¶¼"~Ñ»±#:°*1Ë®û%DnV'W9±MË¼ã±åx
¡áx"WhAKã<,`y/iDa~=à8\ÐÓã®9õMoìmää?Æ¦8ºã£c?Pì«á.pyE«C"^0ÌkOLÿCt'õÂÙÆcgìOîX<òXèGb>@îP.¡Ç Ö!Mñx/Â(!íØp%M¡§t¬
+uÓûGÛ;8õú¸G`àvM4!Èi
]ç7zhõáÑìã¯%s×[O(åfr´Á"Þ	pn'«@yÔá2®ã*ã
X-GûÍcïô£éúç`òQW¡é
q_O9ùÈÉLPîr/}ÜM±Ëv©;[µÐÝ¹AfÎ}¥)ÊgòûAÑÀs²í[ e''#æå1öÓ@ÄÃÔP·öÐjÆÙAÇýKèûo.lå6¾ágN |ÃØt9æ¡ï
?sò}&?ãA=WUi)96± ÕñÓÔrd&b²Ùd)ãÊG3HË³!H¦:Î=­f¤£¨b6Ë\·#Ò+òx1ä£iÿ~^ðÓ$#}÷Öd5Tú!WÅÙWZé:Ù»?¦óÉÀt÷íßi¥¨)æ÷OoúV©¾Ü&ÅÑcÃ«K	ÇñJÉOYçÛã~j8Y¬D·îk?ØÃà¾¤L
ß"µ3V#ÛÆS ÞÞ®Üî®ä9\ÉmÂL8GÁÜÙø@EÆ
Êç¹®ç³yÐ]Ò×MÝ38ÞUÈ	¬Ü ñhZY3xSUyeE0Íl[GuËXH?RtG¦­¹c+aTÒ ¼IY¼§WxçÁÌÞ·àÛá	@¨öQEC1#·¶ÈNÀ³Ùö@	B<}-ßü±=gL[½?³,óî _d6÷
ûÀÉqÜô®âX8Æ)­ßøNaJmyóå¹ÆÙjKsoÛÙ¢mêÛQ @µeæéþ¥rÕâÕü4=Èö³lÃZ2é5câìh LS¦nJ7÷¡Î59º&LÄÀ2p
ÿÞë&dMwVvY­WQ¬Ó¿oÍ¢"øÌ3mÖîTÃÕ¥±5ö¶v½Õ®;BÓaA÷`z
£¢ÇX}¥(EzÚ,«â,«<ó°¹çî pä+²Í£¢4-<ñØþ®SªÀ´Ä5ËBz£¢×X}L¬ço«]ÞAAKZ	tRgê£û¹&xS¡\~7Ô8VqÍ° Ë0ì¢ëX}H<5^­*uo&û¹mÖ÷ÕÓÈN5xwµºÜºkôO9Ò§hxVnã¸¬ùÅ³
Í_þ?· @b«)^ö'ò²Ï®þ®Æ)_mÉOæ>k@µôÁ/Du¡m_'ow{=ãð$8%Á¥£Íï¹)+¡gu'áí¦Anç7·Æ×ÿ5sÍ¡Òàû§ÿ.Þö
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/11/58453ec74ae3b484654dc3970f0d550b3060a7

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/11/58453ec74ae3b484654dc3970f0d550b3060a7 (latin-1)

```text
x½XYsHÞgý©¸JOQ$Ù±³96U![k2 çx¡4±)s oÔþ÷í`É²¼Z4ÝM_ÝÓ e.ÉéÛÓ7¿­é·0¡ä«uéÏíéÌÎÎý±1Ñ¦ç[öµá_k&ôûäl0èì5quÇd&Ç§YÎQ¬¢ÍamÊ~§+Zi^¼ZEøQRøA³Û¼¿.{Ë0YÉMÑç6ì·GïiRöVé¯ne»%½
îÃ]eW?â»þ²T-Û÷ïèCËw[#ÝÅJY&%àß,¿Y¢B§Ç÷>KÑÂ¢¤	ÍÉOÂsnvüA>tÿýÁ/VAJÇdøñ=ùû=º(VÏpQ¬ò4v»!?;ððH°ZQaôè÷,M`ódTÄ©aL{eÚï½"£tÝ¦9TºX>'P>h¸¦Qð Tîÿ2Ï<­ø^ày,È)y1Ç774ïe4Óäc¬¾TàR¹¼ÃIâUg°AËBº/ ¾^VÆ½2Èzë YÑªãµÓO¹·á·²¯YAÌtuG¼ #ãvG¢#zðT"¶»UÚÜ/!UË°:¹ËiL<ß½N¼/¡r@¢ksWìAÒba+T£Oì®ü)ç=ù4îåirÎGâÆ^ø
t½¹!ÎùÈ9S]E
øÌ¿¨åºÊÿßè¡	;Çö§_Ks@Î #l,©MG§PuÀ·7«@qÕá,6QéCuáùQËÑ¾]uWÇûÖx³ºä§ÐÁz1\ï!yÅO|1	Ê.ð*­xÄ6Qó:èìKu÷<å2ØH"Á= 5rç:jº 2/._ÆÌå.8çßv(Å lêæ¥Piî;Óóä¢²GÏrÏÂ %&ÞFÂ5,È )cæÇª{( ð+_>óí6_sÁ¨gÏ«Áå¶KÔrhP¶eÛ"§kBZLi:[¸Jm(®QÅÔL¶W)!ÒJò¸sMç¡hÌ ¾Oà2NÉ£q Fn#ô®1ìpìÂK¿¦+ êþµm.,ÃÒ«iÖMýW	ºÒ¿hî'øÉ6-¬áìm£2ç1|ê÷p[W]?Q¸×
oT]MQìéµÙYãÅ~Óâ¯xv÷mÅÁÊ¬f§[e¹,ÉÈóuÓñ5{ Ë®anÐðøp¨áê}£Ö'È¡mºePA¼WÔmj8¹Ëm
³Cõ4yJÉàÁ" ßª
áø[¤k0cV£ÖÂÛÙ<
°=-Îf½æ8¶8 eUßr"CÆIçx¦4ô¶ÉVf¢cÛ¶}®áMgp¬«Û:9û!úº Þ-0|$äAXP¿xiôÄhu¿X#Û<ôL0>ëlVðÝ×àHå&{¡¹8f&LZþ}V«	mei
¦yêª8Ô5ÇÀóHÍã¦2ÒõbHs
""å^a8¤ø´Ýêut®MÆYl2ÒiHkôõë«A{h[çÇd\-àC]VHFrÌÕP;w´k£iaø#öÂó.LÙnÅLlø>v8BÄ÷kç°Zöu.x§>tä4Ób66ÄæÎMLDÀwð HÍ§sqySsl(Õ-yUH	L·ÿ:¡:¬ þæ¤îµÞ·ä 7ÚI²·år³SDøÅ¶v"Æ1nóæ¦ä	#ÃÉÀÍÓßÓzjò2¯|ì2²¸ÑCéÝu°òÓQêDÈ+xO/âÔõ{h;.Ó´Ò ¾E þêüX`^Õü×_I³7}x¼QñPø9-h	:R­)%yÝèP÷ÿý<m|î	,xm¦­ãG k×XC»Tú¢z^;V)I5°hÝÁ¢ý¿¬}sxßõEª~l+í2¬D*¹º¤Çn>ok×aùºF+½zmuÖ¨ Ö&í·:ïy¯«»Ç6µTQwT
ÄmÉóø¶v{G«mi¯Ýn²m°ÍKvìæn~oÙGÁFøßcèÒ|iþ9êJô´¬
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/50/472ce19f4bd0d976d3d8021eaed5556c79aaa4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/50/472ce19f4bd0d976d3d8021eaed5556c79aaa4 (latin-1)

```text
xI
1 =çý¥;{@Äx÷¥3#Ìÿ/x©CAAåÞÚ:A>ÍÁÕqµ^ê`ð`%DÎ^ÙT1$§rD#S¥¢Å7þLsB¢PB±)*VÈèMRQ×TuvÖTçEÜç«xö}À#6ëÆK/kë÷¥Åõ}É½Ý!£É	gTâ°ÇßäÿK1·Aü ~¯B 
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/50/0950d1222bd2e8a58084360397d21c0d5cc5d7

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/50/0950d1222bd2e8a58084360397d21c0d5cc5d7 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgPîí8tþÿJÏ¦v~ø+½áúKIªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  ó|X.
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/07/cd9e83be1665bc119f18303d99f5d9eca5f1e1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/07/cd9e83be1665bc119f18303d99f5d9eca5f1e1 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgX´Ù¡qÚÓÝÎÍØQPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú q¾U,
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f7/ef6824950824f100ec836bf09b73ca052bf1d4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f7/ef6824950824f100ec836bf09b73ca052bf1d4 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó*¥Ï,¡õÃdÃW'¹ÝÌxjQPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú `+VR
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f7/5a6996b554a6605b551d45516e99a1b4fd523b

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f7/5a6996b554a6605b551d45516e99a1b4fd523b (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgx&²7ïô'1½+©À?³¥¯&jAT¥dT1(¿}\È®üyràõ7^> htTà
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/79/3a8ae41ea53c4d79f122162187fc2b60427e54

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/79/3a8ae41ea53c4d79f122162187fc2b60427e54 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgP¼°P¾qWáÎßsíVIDn4+¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô XV+
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/79/7f2d2ce8a907665052cb090b10289c93833520

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/79/7f2d2ce8a907665052cb090b10289c93833520 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg0XlÎ×ò¤fÙÿI3ãüW¿ÓzìQPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú vV(
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/79/cdf4ed411c50f122f560cb65d81bce2dab52ff

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/79/cdf4ed411c50f122f560cb65d81bce2dab52ff (latin-1)

```text
x½YëoÛ8¿Ïù+
(6`Y4íW »ÍÕyÌvÚí¾N¢¶F;°Þºáþ÷#)ÉÓ¼ÖgEQäIÓî$'ì]óÃû?^ÎøuqöwÿÂ
{·78óºÙ[®×^ÞeËbõF­ÆØá!;©Õ*[·8Û¢-cF;êµJåeMÃå³ÏA´Xf$ò4ôí,KSá_Ü>$³¬:	¢YÝ¤býVù=²ê4ñôí­¾oÂoýû`D]ÔùÝá$+ï\]¿ã+²W9âeVì`ZÄAþíÊ	2Tæó{LôÂ ÍxÄö	o±?ÙçÁÂûþà¥S?¦«~bÿ~BéôD¤Ó$ÃõbØÏ
ó§S:ü,£*ÿ¾#p>b@tADÔ5æ¼ÅÕ¹ÿ½.8Uç)r×jÃçÂ7Îxè?HAÈ¿$Y5¿x¶*ÙXàLT<	b²~rú©º¥¢<ä!e³ÚGüÑHHÆó8hr0÷Ä×µ¹ùêÌ¦üÅ'ÒìxÍtæGþ69·ÁuvØñ)³âésýë®Ù÷RfDN%$ïëJUÊPÜ-e®ç÷L÷ô
DP:­£mB£(Æ~Ç{ËÓ ý¨O~ßàÐðÝ3jÙÆÀ=7³â'Ú¦	TÚ½³s×Ó
éæNzÇ³LÞ<£m»Õ¹0Üß6Ñn_ägµ^z#ãõÃC#¸°?³%Æ3ØawÔñ e0þÔÁ@9ôxå=ùÈ´fÒKyÏjg~¦'ÝK¹°5J¹ª7Ì>k{m»GØK¤®4AáÅ4^ÿßèáAÀè9Ü^
|N yòX¡D®c&º2	ü<Ó­ÐG.pÆï)¯k»ðtK®d¬
EÉ°Ò,xÁ·ºÓ 7TÞ¬ÙÔby nò´9Æ~àAcÇÍ =ÂÑ~» 4¡¹Ýk½P÷tÇûaX=èG'Q?y
0}Hòl
àñi×Q4¬ñ^cÒã.y^MÇ¬©§®)ÄqÆ>ÉmV\âµÇfÕõÐ%çQÖX:ÖéÊÒe¶ñ2
±úYJÍRIÏ°Mæé¥FW<vn[4]¯mé­Mzê«a¼»^e:ÙÂØiïajãÃ
ÓFhr¤ÛÚÎÂ³åE©Ú_ûË0óH¶¯6¹_®Ûý»qQ]úV°=5®áí1\Á -H·ÁU26øJÅè
v<ZËÒ¾©è¢áô¡ºrÔvFBl9ç&`AZKº$é¦ Aÿ)b£\sà¶:Öd*Ö©©bÎý ©
´tïðÆ1ú`ÞAãmØrÇµá«È÷D¿v®+w?5ÑÇ"öú¼G-9'}©kØïÃÄôîPºÑt,°I6½º"Fí y¬EáMk2gÔêx)qï?A1GÂa s³ºÄC¯Ai	§ò	ñ?<ñ¢åüQ^MÁ¸ß6ì]Éá¶è<ÄY ñØà½ßÁ¸ñ¨`Ãù°_òyÐyEïøÖb¼Fð
HòÀ\&ÎìÖ«ñ kØNgh«Æ×ØMBáÕ¥è	>!ë )GøÂ_´ Â¤t-Ó?Ol6¸© 8,æ»ÉDÂÂ+°/:_$f æ#Á1À CÌ2"%B1ÿD´­ EZÖà¼(U8+Ð;.F^·wÙëÂ9"K¿7;S$w r¤°­#a x/ØV &a	ÃHü å^ú oáçó­ßZ»RÞ!+0h³ÄcaºCüç-'/«H'»×99[,¬±,ô#»3À¤}?, ®kXk¼Ö3Ö~+â¡P;|
rMÙ£ð;nrLæ¡±¨o´	ÎìÖ¥¡?ö©Ì)  @©>'"Íø2oÉÅ´¸.Z¦wP`0/	fþØ!îþh[°£ å\YÕ´ìü!å¤5	âvH¿öêÌÁÖ/
YÇJ®1eÉ7eÉ7·üÜÒÇ"kcÕÅ]^;@³ô&ì·4TÔÕeM4e}7e}7±¾ûIéÈ0±¦kw­N0Ll¡rÅÝV"±ÊêmÊjnª9"¾ÎµhÎy¹m«»àÅãÜÉ~¢¨SlaQVV&]©2suÔy~ñ^ KöIkßÎ§kãºÜÈ«\¬L;fºi±ã]-ÕÐ"þÃC|ç^ÏçªPë¢P3ÕLàU²|Äf¼/qjÌmÕÛôÂ§
q.P÷Ç.µ\9u¥{)zZm)VWQpêÊTç®ÎjÇa;WÌÈ!%ûx¾¼	Tt´×²í¡|-ANq×ö%·_ ï6>AàHrnmÌQ±¾ú«4+úúy	ô/¥yþÛèhº}
üýÍ5r
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/9b/5abeb8e33da84ab2ab801ed7fe73373b545e6e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/9b/5abeb8e33da84ab2ab801ed7fe73373b545e6e (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`(\êýÍý@ÁN.¥µF£üÚÛAÕ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá æ@÷
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/44/cf8f13a27331f31339838dacafe8cfd9e5d462

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/44/cf8f13a27331f31339838dacafe8cfd9e5d462 (latin-1)

```text
xRËnÛ0ìÙ_±Hi
¤"pä #Ö$¤½,d¶È¢AÉ
ü÷]ÚqêmðÂåpvgf§ë|}:C 7;S/W=|]ÂÐ~¹Rð+ÐSÛzºíµé)ðá*©gªíÔU<Wm_/je~@Ë¥Zjè5tR¨½2 [+½5ðÙýrãØã:³î. Ïîâ©ÆaÂP$(ãå¥¼½¾!ã¼í·»Ú½Ü!
ÉãÊ'<ò±ÌBÆ£$¿ç	ó¾{\°Ú^ýG¯9æwwû9ßc$cOçÞ8ÿQ`×r­lgz½&7¡'ßºiôSÝ.¡©É<òSµÕ´QMx~Ê9Cä¬È¹Dù³`hß­ÊI¯è2Uoyº]×«u«ê·ÑDF·§º_ÁbÛ4Ðm7mzêl`¦Ûn»¦àÕn¦çªûúÑõâM5UÃÙæD<*ÐP0cëö¢'mç'Y5teÊøQV)¼	ô={e,pÝg;NØÒßHì
i¢X({ßKP9óÂ3©Þvê
Í»ÈãLÆYdQ'Cù^0Iâhl×ã_eôÉüçÀiWO GBiË1çIrèðqâu;3ª¢IíBPS]ùÍÌ¿]¦jêØÏÈ£|ÀâcGoLDàe2?/³aÁÛÑÄºðÄYÂ<Á0ZyeyÈe0Ûë«¼VS
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/59/5eefa72a5ce25cac3281c50347b43b4f777775

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/59/5eefa72a5ce25cac3281c50347b43b4f777775 (latin-1)

```text
x+)JMU047c040031QH­LÍI,ÎOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦aUUÇ üûsæî'U¸Ë6´E>\5«êìÔÊÜÄeb»"Ä®¯.Ø.íeÔÈ*U_Z\¢WÃðî¿øDÍ¬W*¾²'S÷< NH
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3d/00db07874b7005a48d4d29e570a012d7c4aaaf

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3d/00db07874b7005a48d4d29e570a012d7c4aaaf (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`XýíÂæ"ç3<²5«V3î`ðª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo ÌÒB8
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3d/91c06a587cf548d03d495b4e9959b7f25aa572

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/3d/91c06a587cf548d03d495b4e9959b7f25aa572 (latin-1)

```text
x½YmOÛH¾Ïù«"¡VjJm¡r8N°hïå$X8¶e;\iuÿýföÅ^¼¢³Pvw<;óÌìÌxl¦A4%Û[ìÍé­Rò÷ðÒ¦30ÏÝ¾¦w&ãG×{Ý1H³Õhrp@ÚÆ-vÏ2ØÖa;ZmÏgÁrNÉ?ÙAD3¦Q~g©¦0ü ñýSr0ÏêS?ûá]zÀ÷°ß:}¤aVEs~¸W÷Mé½÷è¯¨ú±x8fåÕûô©"»Ê-3°bSùaø7+Kî¦ÈPÛ_,]f¢øiFCÛ\xüI¾ìÿðc÷ûÎ¼ Z¤yvJþ=EéìD¤³$
ÕbÈÏñf3
:¼ÌÂ:ýG!81 JvAD4kæ/h=êï{=)×)r5ÃçÂ7Îià=	Ëä¿L27kñ(ðlT²1Çøww4©Ç4ñ#	²y|vZC]BQLb²yãgÑ"M
æ¾øz/7×3/®Ï½pFß2ÝÈ×ÜOc4?ôl}ïßf=/NÍãÅ¤¿bßÈ:JÀ¼®+I)Ãâä!&¦;®}1Ð³÷9@éuÆ¶²	æ ½÷¦~z¢.~ßàÀÒ Ý3îXé\höÀ®øä¶)¥ÖàüÂqÕTs§7{ Ù	W4³kuzóÛ&ZÝËüàÎÛñ`¬½[sxhå¶ÐW¶D{;¬<4¢lÆ<(.
±¼''DY(&mH¸ðL©'QæejÒíó§;¨zyG¬ó®Ûµ{Ô&HÜ¢æÐËëÿ=<{÷G7&S&c@§<V(^§X§]~FéFèÂ#8§þ6]xº%×N3Ò¢¤DjD¼àÁ[£ÔÇÇ
+omÒn+±<P7iÂn*w$fäàZ»AY7?pør»AhmÐz9önTW®ôBóãË1í¡zÐÏN¢yüAú&4¥Ù&Àã2¦mGÑnÖ'I»äu5¶ª¦`EYyP$7YUp)W/ÕTc@Ub^GYbéHA¤*KÙrîGË0À>èg)5KE$e|.gT­3O-5ªBèä±sÛ 	8Èhâ¸]C}l­ÓÓ¬ñöz
ét»»©­Ï¦µÐéH·´#?f9ËRµ¿õAæ2
Ê^\mr¯n4Ëù»ñ¦¼Ô3­a{ªÙ=¼Ó+>ÜðAc[nq#e¬ñ°7ØÉx%Jû&ïàbÂE$
G¤äËAR×÷bÃ¾ÐÒ:|°ùÐgR®sÂ9#¨?BlÔkÜFÏ¸LÅ}ÖÔr1RþÓävéÎpbkC0gàZ¸çXpIóá+çýº¹¦ÞüäBØi¨wÄµät\®ÑpîâÒû#áDÝ6ÀB$YìÅ¥/rÇèÌo¼ý #mb;=-%îÝ(æÀ{¡¶HSàa/ÏA)é&³	Ñ?4qÃåâY®¦9v5k[j8vûü,Ðxó3f~ãG×l¸
Ka´ß²·D|gÑÞqAcø$O
y`-RWVçíÄìkÝYröµÇBìfBáÅ¥
èc>!«Ù#|_Ê/v8ò³¾a°iÍ7Uã°X#îb%ÒwpCnÀb¼pi_	Ì"AÌÃÄ NSD«GÍäÙÏóMZNE>5kp]*\hc·?¸ôáe80'öúÉÑIrÀ6÷­* y0	KÖdDâù)uÓ'x¯¶<-ìoÃîÈØðNYA%¼2l;äñ¯JUAÎÍý>6&¢Ì­%HùzÂYú¡9ÛñI;$:.°PÈæ Øñz¡=¶Ó<añqÑ±E5åÉCöå×¶	¹Ï­ÎµÉw«á®
~íj_wÀmpáß1'ÌüÃ¸ãMdk¦eëS®qHYÀ§»Dùm¸S?¤£»(>zSB]{]{}S¹ÏM(}¶H²2]Ìòº^-ê²¡&pfzSÔC]Ôv]Ôvk{±)ÝW i:Ösà IR	ÍS.¢m$2¶2BQ¹uQÉu¹FäÂ×¹Å9Ï w­reç¼<¢¨êHäÅvee¥hRJ3«£Êós)
 ,Ñ#1\»o:[×å^¦`eD°J2mY©¦!Ä{=2dÂnâ¿:ø.áõ|Í}_ÜçÏÉ-Ûè¼DØyÎZrK¶äå½ð©DK`¨µ[95!¨e'#QËõÊ®%ÂYG&#<w-wW[8[¹bÅDìàq,øòPP²Û±¬x!ûÖ¥¼o®
|AÃù³¨Y£»ú+5Kúêu	ô.¥uþ¿Kë):}
üý-G3
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/41/ade281df119995e5a425ad67289941e2e482bb

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/41/ade281df119995e5a425ad67289941e2e482bb (latin-1)

```text
xµ;nÃ0Sëì
Ë¥H.Ãð=ü,m!)P«Â·úÔyåL1x¹-Ë,
CøÎ¬Xðè¨ Tp9ÈSáÖY5v~ªQ'K©o'tµPÅ\s6Là´«}t¸Ë³uõÃ%®g.³´~OM¾Õ%hÌé¯¼í÷m|·Îëë3>fyîiÌm¹*í­¶
XucÃA+ÂÿdmÞ¸a+
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/39/557c338242a1bc2e6006a37d8dfa92d3c6d453

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/39/557c338242a1bc2e6006a37d8dfa92d3c6d453 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcxîÑ3Wöß²o¸,Ý®íÚ¢ðû8Ê¬âü<V],Ó¦RV>é3fÎÆPZXÀ öÛÌå,oèÕRMQá"Ï¹û+ß@Õ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá Cì@X
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ad/baf2b590b4912dd4796b808ae671dc232a4809

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ad/baf2b590b4912dd4796b808ae671dc232a4809 (latin-1)

```text
x+)JMU0¶`040031QÈÍO)ÍIÕ«ÌÍa9´9L¹GvRVÓ;Áz§9cì×H Wd
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ad/b346b1990d0166177f447a612c65c970c7fff1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ad/b346b1990d0166177f447a612c65c970c7fff1 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó¸ôÖ¦³Öü¨"yüdü¯ãU©EÊoß²+ÿe&¸dýæ
¦Ï  ÍdS
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ed/89a41a83788b15cca0f8d3a87d12d52bfe95ef

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ed/89a41a83788b15cca0f8d3a87d12d52bfe95ef (latin-1)

```text
x½XëoÛ6ßgÿDP×vÙvü/ò#¶û"È6%A³¦Åþ÷Ý<Tl§Y	©{òwÇãÊ2Jì¸Ó}óÓÑcÎþûóÙxê§§þÐõ¶çOfÙ³Y÷e§ÃX»
6ÆAwàØÂäå&,ºFã(WÑvÍÙ»0N·E;ÍÏó$Ë_¬<|¯)|åéõ]Ö^­e¯Ãø*oKñÛâ·<.Z«dÍó×ºÝ_·á.º«¯ö
¿«ÙÖ5m(PJ0. 	£î*»Z¢B£¹ÙÜú"?
óÇ<cß©Êû½k~
SÿË¯^²îû·ì·è"_=ÂE¾Ê(Úí}kÀâ°`µâ0GPIÜâ_Ò$ä"R<°â¡ZÞ*Ö&øÒÊSÎ×­M.4;ÒÅòxåkwJ¥R>å¯ð,ÃÚÜ*<û&y<XâÌÂ«+µRI	òÌq®¶¨,E#¤bÝ9ÁìU²I!AËC¸Ï ~q«ÒÖ:Wüêø¬Ã<Åðã`#ÜëðsÑiÎìduÃ¼ eÃvGªâ[°*È.-ý2F[BÔÉMÊlkäùîÙxä½Aoîª\¡MÆiÁò^ó<ÌOFüxÀQ°ä¦gÞs¬©wf¹c·ÿæ"tÆ§g¯ªìëá.³`uÃ¦^0Ì¾Ó[ÞÓ¨ðòæôlïçéñ/æ"Òb,\Ä8 ëÃqúÎVi>[÷C õ®èó»xvÂ4BéÀ¾ËyGG+K Ð÷ÞÜFÆÂ©·WÌ9íû}g,°¬¡
p«ZB7éÿ=L·ÃÙ© _rs@^î|lTZ»|
	NÃ
ô#y `ÝO¼Tò(Â!ØF]Ï±öõîwñÁr¼O`BzôUh`ß²ÜÊðõBä`	ä;áý#¶LÜ]óZèîIXHßcâáü½H?Èê»ól»g# ¼\9ä$ãT0
"öpPÛº=°ÏV%ýNú9#èûOÉ#!B¾oøâZß '[Ä<ðP@æ_rø(}Á¿~9WqN>V± uzÇiJ>5Ùl2ÉùÃJäÈµ!H¡:.\£fÈ@¨bC«åM$Ö
ö¹óÞ@V¡ýý¼¾»<vÄYk 2\)¿yæÇÛÍûcºô-çàþP+Ð¬Þ_%¼éo#ffú;Qõ¥g=·¬$_Ò=L×¥° Ô¨9kÁ½¾VðñcA<þ1Q4
.|i5´ml
ån§ùi÷Ë²¬äØ
*JÛXóS¿ìU8ùaìª2¦P}ò(_©÷{Û¥®×ÄÕ<që9ÎLu<}3¡¼D&öB­&1`Ò&«°£²«ùËòó1·@
g¶m"¬Ûêtµä®ÏÚ#<Z¶cÏ~É0ç~~·Y&ÑûiÒÙÙ0.Óa¯üê¹·kw>÷][ì&Ô`ËyÛôÖOS¿pTËsVÂ¨Â$U¥TýâüÓ}DÉ; TVaáÜM¬I÷e¡S§wiU[¾ÙláùÎ&Q}ún3OH°+Ç*,B¯ð¢R¤d"ÏºXÀðAòuv]Lz|*Î'ÔöÆöÐ2ê¤õð#X?êôÀéK®.@©GjØSôãïºAâÅÛuøÛ8ÂË	!B#uJàôÞóAfÒ¸"Fá¤«Õ[9[­ %¿Ñ\&I%\øåu5©ÎÂ¿q
45LÖÛ¾ÆðfpÅÒÖH]½F]ìÒõÙêt®ÑÌïr?ã9/d¨÷l©êü#èü)ô|ÒS	ÒXß·C]®tÑ[Y.ÑõezÔ>W»t¿GNk@
0{=ã«Õn~
Ôã­Ñfh»¨z(¸>ÿrfW'<¨q(õÃt]ZKAÕkhÅ¥Þ¡K½yÅÔdfBÔçþdáËlÉýÁo?ê2cx¯0ó§ã"T]×-o$Oëj6óÍDs2íöQ¦}S/|.ÿ-æX­Ã7N
üýöàV
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bb/b9a04d53b376a7335a78958541be2e0afc3cb3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bb/b9a04d53b376a7335a78958541be2e0afc3cb3 (latin-1)

```text
xµ½Â0ûÙU.ÍIñáÚ^ 6Uzx{²3ãÁÃgY<Ï(xÂ¬Ð!
!r²£#N<õ6j4Â@ÕÐ6+^j1	] ÒI'µïHSå8«ÑûÑ¤vyæ¢^üi=ñ8I.·>Ë]¢ÃÎÙãoxÝ7.[»äÂëûÓ>&yî};äù¢ óÑEg|TG]ÕTZ¯ÿu¤M,~Ôb
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bb/386c268eecee02935ee2dc4bdb9199d84613fb

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/bb/386c268eecee02935ee2dc4bdb9199d84613fb (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹²bþä}°å2ª^eâ«tf7Tmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ >
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/51/e6b75659849d77db62315cb1e951297c08c778

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/51/e6b75659849d77db62315cb1e951297c08c778 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹÷ZÒvÄ¦}W¡bsÏr·Pµå©Å%z¹9ÓvMÛö"£8ÙH%ýé¶{{xx ëÓ@¨
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/51/d9d6ec6cc028feb4b86892a22df48dabe5c7ae

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/51/d9d6ec6cc028feb4b86892a22df48dabe5c7ae (latin-1)

```text
xµ;nÃ0DSëì
\zIîA{)øYÙB,S Voõ®=ÕàMñ0¥-Ë¬Æ1h1/ÕN>M,M!9§"eªðèb´Ãº<ÔYÏà¢¥ØLÞ#I É$P8syH»ÞZ7ò\Òz:kë?¹é¯ùd äÓëø½oÒ·ñÑº¬÷çxõ¶ç±´åË@ôàÉCs²GWTÞ*tSàðaÞ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/51/5a5c8cbdd4860011c8a24eeb81a2eabe8bd60c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/51/5a5c8cbdd4860011c8a24eeb81a2eabe8bd60c (latin-1)

```text
x+)JMU06`01 Ä¢\K¹$&5´2HbUvP"¾» ÝG
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/90/b03b45d358aee8e370093ca6efcdbcdd19b913

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/90/b03b45d358aee8e370093ca6efcdbcdd19b913 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹+O³_ßxÉEw£­&sËÛ_uCÕ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá "A
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/90/b06eaf64700e938f546c408489ee3d193f5936

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/90/b06eaf64700e938f546c408489ee3d193f5936 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹ÏÎ³g¸îîRÅ²aÇÕÞ+Ë@Õ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá Õ'@$
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/90/8a0666744a51aff17d9b56a2a0f00af84f58d2

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/90/8a0666744a51aff17d9b56a2a0f00af84f58d2 (latin-1)

```text
xRÁn@íy¿b"{01¶=´7XÖJ\Ð µ¶À¢$5+61ñã»Ø®&åDvæÍ{óÞD¹àñnxc °Ød¶ÞÐoa4ÝC¸áðîNU©(eíK!wª3ÛËÍb^ìøÀIxQfiÆå¸N²¬éÛÌ'áïFÉ8D(E­«lJÞÏt	õ%<]íóz5JÈ÷4D0§NÈü%/ôMªÁñ"QÔFy*8¯ ¾ó<ù[ëÔ¸zÇ,Ö%6ÛÏ´@Û¸FDBäÐ#Å*Ê9T¯ð!µXµðç<.!áºyþøa´ÔÔR'Ï®Æ³Éâa¢òÈËÕúD§à\\6­É?´¾Uî@Ðoèõ<;»=«®(!ó­êzkGÝ
©¯U-Êò%°Î4ê¿r¯Ë»ªl	BOµq?î¦©FWª,ÕGµ3¿ºÀS6Øìj{ãÚçY¾ þå®
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b1/97e3c0cfda436a7f6db654779d04486754eff1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b1/97e3c0cfda436a7f6db654779d04486754eff1 (latin-1)

```text
xAÂ  =ó
> aé.Ä_àÝãKm"b(ý¿ý×ÉL2©ÕºmO£è=Nl4}p3`É¶ï #Í0±aP_îòº¤I #'¦0çÙE´i¶RØïãÕº~¶½ëWÑ×M×ÚîKåõ}I­Þ4xBrõÙLÆ¨Cþ/ÕØúÏãC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b1/aea07d2cd923e59bc26e622acb6379ef2d86d5

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/b1/aea07d2cd923e59bc26e622acb6379ef2d86d5 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹	¥¦`Ö¼>a¡SèÚUß­
ó¡jËSKô*ss¦í¶5íE<Gq²KúÓm÷öðð  ÌË@-
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d1/cd2d4a446584576f16ba1c981eef4a22d7edf3

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d1/cd2d4a446584576f16ba1c981eef4a22d7edf3 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgø6Ã}æ]µK×·M`]uä~­Ë¶rªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  ×
Wx
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d1/a50b52189283c93d5a3062052345907417bb8a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d1/a50b52189283c93d5a3062052345907417bb8a (latin-1)

```text
x+)JMU06c01 ¢Ôäøäü¢¼TgÉê,I¦å<E¼?¿Îø÷hÛn 4gu
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2b/e553a23d7a843a7f1d86becc1b3da863bf940a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2b/e553a23d7a843a7f1d86becc1b3da863bf940a (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹/ø½T»Cåê¿<~æ^{é	Tmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ Àa@;
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2b/2c4f8d712e42d37c8bd8e621b0738474a5a1c1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2b/2c4f8d712e42d37c8bd8e621b0738474a5a1c1 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Óx³Tb§]x!¿eiËâ=?ëÜd 
ªR2*ß¾.dWþË<9MpÉúÍ/M ÑTA
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2b/96b6bb7f8ef487259b00af77e676c635613600

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2b/96b6bb7f8ef487259b00af77e676c635613600 (latin-1)

```text
x½XmoÛ6Þgÿ
¢¨k»i³-éÈ¶x_"ÉIÛ/l³Y$9kZì¿ï/"éØN³<Þ;ÞÇÌlN:G¿,éç8¥äÓè"Nã`8>¶cÍÜ M®ìðÊrI÷M§CH»
2Æ^¿ï¹LäÍ;Â$ºFã NÉzIÉû8Í×U;/²-Ë¬(_/«2>Õ¾Òüö¡h/«Ö<NqzS¶¹ûmÑ{V­E¶¤åë[]nNo£ûxF]Õ×Õ]{^ówôaC÷&G¶®À'ò,N+À¿±âfæju2Ã$.+Ò|#Üfå-ò'yßüçá°\D	0½!ÝÓòÏ	ª(ÏPQ.,I¶«!ß°y$Z,(¬Uq¶è<KÁùdDD±Vñ¶ª¬µ¾´ÊÒekU"ç»NGòbøBø à&Ñ`Q\'ÿe¹Y«{gï"O"æ8øæ­q&AvNO¸V[,T#¤jÙ9ÆäE¶ÊÁAó¹/ ¾^IáVå­e.è¶6²ã·ËÍO£òoãÏU»å%q³Å	¢¶ÈhÁ®$Ì»à:C³L'w9qm'ýó¡¾ÈJßúÍAGlï--ãòXü¸ÁI4§	ºgjyö88·ý¡¿áÿh¦PZè
ÏÎPP>ÒÍÑâVÇDt~¢=Ïê_ØÁèõ.ês­_§Ã©ýrÇæ¡ÛB²%öO°ÃëËíA#L0þäÆÀqÒ÷âhÍ¤=	WÒîVUQ¥'ÝØ?FîàÒëâõÂ7dØ
Ò@ qÃ´nÿoôpv&×c¾¦Ì¦¼Ny<¡ø9ÝÅsÑ¥Ip
®à úV3?v<gð¨y ÖIÂñXMÇ=Þ<ö.¯m/øÒ8)?}x`Ù~ç°{ÉkÞØLé'RÇîoYÂÙt+ªû(gp0ãº-Ò'²Ãõ ©çOû²ë; io|Þ¤;pÆÆ7°­Ýí»KÍ³ë9*P÷_&ØÒ]ìaÇ·G`öà0¶=¹xÀÄO¼ùÀæ}F¿â^½VUDi)Gz«0b ê3¢ËÔtÄbÑ\Æ?¤&ÂïHòØ}f`-ò¸Ë\AyDIEÞjõyÈÜÏ Cî2PºÊHW bÎcTæ)WN²¿i¦ëÕ	2z¶÷TìHSì?þãÿ.ÚßÔü.sQîÜòë8B>©SÊ ÏÞrãÄXdÒ&7¯}:ätá.kÔL²3ã#lüöñÚ:1¼D¤<¸.urËÌÉÎ£PÍ#d5ÒòÈ¿°á:m¾ï!çcl!~
]M>?° ¥úWXsõ|Á±:¦p$*vÏúõú%G1g~djÑ6ÛG{sÎÔLáA ñã<fbGQ\Ò°|XÍ³ä{Âÿ8êMÜ§Ò ê#ÈpF¦n5ä¢<Ê ]LCßeÙÌÓÜéSw&v9ZÍY ×ÀvíÀ~ÙhÂ»LfAØsá$Ú³k¬`ââ;_Ìqnäá¦lÂÏÒ5/cÇ3Ïº²Â¯*òpy¢5nwûrÿLÀ×´X²±.f'Êf­ÔÈ¸GÓ=ñÍî (ÕìoqÏæÔößïêÏéwU>Îxo4Õzgá:Mð5¨e^<çlÝjjç§ãNF9k7BÝáàÕ­¸Jqµ8]máæ<Ëª$ tg6ã«Õâ1¯`ã¡*¶OÖQÚñì`åN°QV9¨aÅ7ÓEWÉ QxÍò¡ZÒJ <")iò#GY=jÏãµ ÁÀ1ÛÄ·#n§«ÆkD¥©MIANÛ7Ò¥Ñ*ëé{ïºØ6æ[@ÛzémN9i­aôÃ«ª4ÔÏ%YIè*}WrVV,UDÀâcu?Õ=«õ=c¤Uþ¦=ùh°¢¶Öû5D¨ ÔMÌ¨Ñ¸¸ó°&4]©ÃrÊù·®&Ñ9°*ûåyñÊ{NA¤ÁbuêÞÜ0Aí)Øûz¦µÓRÏô8²Õÿ&óì¾vAÀg¡¿aì5
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/10/fb531e0ffc103fcc7d1dde085fd8d58e05d9df

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/10/fb531e0ffc103fcc7d1dde085fd8d58e05d9df (latin-1)

```text
x½YmoÛ8¾ÏùÂ°¬Iv[»+§ÍÕy©í´Û}1Dk:v`;½uÃý÷#EÉó¾®8c¨$"R$%eã ³õãú¯§üröwïÊº}§Û¿pÛF§12·7¸1ÜÉªµJ±ÃCvR©¶.±[)ÔXQ­J¯ýp,¦}öÃù"=ÇÑ'I'ï§iâk?øüþ)>¦å±Nýð.9¤5âo?ò0-O¢)OÞßëëÆüÞ{ô×IÔEý=ÓâÊåùþ´${#Z¤`Å¦yä)àß®,¾#Cé`6{tnà')yÌ~2²9÷û}>øáÏÝïOn2ñ`ª±êùû÷E$_Lâ(Öa?K°yÌL8èðR?
Ëüû<
ÁùU"¢"XSÆËiTyßËÉóiy çq¥¢x1| |páÞdÉH&ýÉ¬Ù£Ä³UÉNÄ3öïîx\óØÈêÉùY	uJEY0É1BJ§Sü£<fspÐ8à`î+¯wjq9õæå©Nø«3¡ÙñúÉÍ½XdßûßÒÃ7OMãÍY{Íº×2#Ê°+ð.¸® Y¥93ãÚÝsþ"(­ÆÐÖ¡Ñ±¹ÃöÞóÄONõÁïxc {
Ëè;Ýµ|òLÛ4ÊB«{qé¸úDî#ÝÜqìMxzÊdçÍlZÖáü¶Vó*Û8³ñfØo7lÁÉþÂ/`ÕRÛFmÀøSåÐå!÷øiÍ¤-	ðÎr¥^ª'Ýk9±5
¹ªwÌºhºM«+°HmiÂ-i½8þ¿ÑÃAÀÄ9ÜÜöø2ò,å±BQ®bteøy%[¡G&pÊý	¯j«pw®§¬	EÉ0Ò,øÁÁ[GÇ(ouV¯k±<P7y,&´9Bm?peØqñ
£çC8ÚBmÚó!Ô÷ »r­ªáx?Ë½²Õç`§$æ	O·¡ W0íÚzÕ>jLzÜÅ/«éÕõàÔ5ã(JÈ"¹ÍªKC¼v{Á¬ªº²8ó2ÊjKÇ"]Y²HS?ZÞ~R³PDÁç£&lyz©ÑÂMon[4·iêÇÖ&=Õå0Þ]¯@Á"ïad7÷0µöii#4B9Òm×ÎÜ«Ç,±¼*TûoÞ"H]¡A[/¹×·å|Õ8©>}OKx=5ìÎa÷[j±é%ccO*&^°£áZ&öUÍà`D¢»-ÒªCrÔ´-Ø´/;i
jljÚB
Ò;D¸ýO/êÀ5n³e^I¦|^\jIÌ¥¢ÿ"Z ¦nb;¶Ñs°oÃ"È-Ç$þMÍjïýÍLWo?5ÐÛ"Þ5ôÙG-=©kÐëÃèCz{ ÝØ±M°Ixº"F­-ò
Sx.0;RVgö°Ñ¢x)pï?@1Gä09XUâOUPZÂ©|BeAôÝp1[©ÓËÉÑõµ+9íÇmZßÿDÈúeûÚ{.v@\z»p<ÔÉ±Ì }l\Í´G#	3áÍ¢'Kû'ÄÓÄ¸í2Z1?6åHi&&~Ò*aTSôåó8©ôQO=Âbík	RB)@Æ¸ÂVA¿MH"Ûi ÄüÃEh8ÖÇyeÂ)ÙÅNÃé^·?²7g ¾\n­­  b[ê_ÚÇd+ Øù±ç'ÜMàì8ì¯½æÀÜúðúè&¦±íª©]ô[7£~Û°ìÖÀ2Pò4uæHô¡ÕêËe|i
ZÈ-oÚi8ÆÛBäï©ÉÁ¢4`ÒL/_ÎåÜ4+ã.·{´D oÁ.üpæÂjÜú9 ä=ªøH¸.îëüj¨¸Î»ä?ìIpØ½ºíîM·
µH°÷[]­Â>sZ®xsOh7âÒ¤î>Áþ-ÜëÔéo
rabêT+ÂþÎ'j>Ró!Ënv¥=(üDÇþÊ§
ø.Ïî¼»Ò	[ÐPsLM]'êPVn
3«N0:xEÊå½µD9-¶¡9¢F 0	Ö¤.ùEÒ´´Ó-ãCÛå=YÄHõ{T»u]ØÉEÐl-ØÕÉE y÷ö-Ö|²6ó
%ÑiY³c¤Û[îÍÀtóCde¿T©^ÿ-K§^Íª¾ ³¤e-^°{tÁmK]¶WoÅãUBÝ9âÆQó^¢P:¸|2¬s×êjsÇá--	(I²ÕÈÜÝíp³v5O­_¹£(u¼Ý_óò
FYöç·õ«sG©54_wÂ8û_	Ëhi¥nð(ø÷±l-Â
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/10/6cb3753639a0a0ea1822a4abc394a370b04945

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/10/6cb3753639a0a0ea1822a4abc394a370b04945 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgø¸«zíÏµ[òªtGØ,ÿ¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô Ú7Wg
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/49/6611e578ace023b2bb5158661772d764cfbe1c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/49/6611e578ace023b2bb5158661772d764cfbe1c (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg°e¸ÍÞî]Àº¤×WóiÁ¡ëGV­(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} e»U;
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/da/b63e6f8e410f514507038b3f1df8f5e3cc4ee0

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/da/b63e6f8e410f514507038b3f1df8f5e3cc4ee0 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó~{¥U¤Í«¿"|1Ïí?O6peBT¥dT1(¿}\È®üyràõ7^> -ÃU
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/77/d033926227f6840f4c27ab47f7ed4d648ae0aa

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/77/d033926227f6840f4c27ab47f7ed4d648ae0aa (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓÔ7ñ-:óêÿCæýò=çç	\\QPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú N UÓ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6f/4cfaee58b55bdf581b7310b0fa387d7fc923b7

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6f/4cfaee58b55bdf581b7310b0fa387d7fc923b7 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ón|rÎÿÓ Ñ¶ñ¨ ç'o§CT¥dT1(¿}\È®üyràõ7^> 0)U+
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6f/f45e2775239687465faa8a25214a035b1b4d09

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6f/f45e2775239687465faa8a25214a035b1b4d09 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`hÏ÷âízw'Eöß½Ç	ÎCfYsª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo BC¼
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/88/c6c13483ab99d8680f26e676c1adf5f30e3600

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/88/c6c13483ab99d8680f26e676c1adf5f30e3600 (latin-1)

```text
xmAnÄ E»SXÊz J»Ê®gè	Hp-`D3§/dªªê
Ûÿ¿!Ð om÷Mò²ô Yð^\={J=¬­êêWÁHg÷
ÉDìá¿&_âf
>¦ ®áÚs"{­g/nÔHQÿ7ðn­zÆd#%1>ù4Ã@¦XÖì<úÅ*°£I0 ÏÃ°a#
| þX°4²ºcv·}â(Ê¬_U§ZmqÅ@Yo~QNbhN1×Ïò ó+ÿûÀó3éÁäãºÅÝ#ceÙë÷Ø/ßkÉ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/88/827630e1b2ce5773ee187ac1ba353b72f1120c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/88/827630e1b2ce5773ee187ac1ba353b72f1120c (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹*6­}æj»JjÅúñk¦ªæFpCÕ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá ß'@Q
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6a/52a5a9c11997001f0ddf04d16d36701392a447

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/6a/52a5a9c11997001f0ddf04d16d36701392a447 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹Ûr&-y¸Ä@NpCDÜ´Å'ß9ÆU[Z\¢WÃ0m×´­i/â9¤XÒn»· õ@ü
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/40/9bd4e84da7d804fec40585e1f386ee3ff7fa66

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/40/9bd4e84da7d804fec40585e1f386ee3ff7fa66 (latin-1)

```text
xK!]s
. ièæã	Ü»d '1s¹·¨T%/µZ·!µ¢ÓèÌ2XàãÜ}AH>)¥SÀ¥p)$¾±ógÈEÇ 	mtÅæÅr.d òÖ¾ñ¯Öå³]>beyÝymy«í¾Ö¸½/©ÕTÎ(CÖxg@ 1éü7øÿR}(-~îC)
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/23/edef53710723fd03936611a4afb3b031d29798

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/23/edef53710723fd03936611a4afb3b031d29798 (latin-1)

```text
x+)JMU0¶`040031QÈÍO)ÍIÕ«ÌÍaN2¿¤gzå¨f{ÂÃkO§?:ù W9
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/23/8d88c2cfffa934b1e6941189f0fd1bb0d7e919

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/23/8d88c2cfffa934b1e6941189f0fd1bb0d7e919 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`0c²U±3éÃÂn>	üi*)U[Z\¢WÃ0m×´­i/â9¤XÒn»· ^Af
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/23/0f532945cb6353477b7b8dc081c6ebc91824d4

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/23/0f532945cb6353477b7b8dc081c6ebc91824d4 (latin-1)

```text
x½XYoÛ8Þgÿ
¢üT×vìnÚ-àCJÜÈG$9=^Ùf!º ÉÙ¦Åþ÷á%R±fS,áÌðápHeg+rÜëÿv´¡_£/Óó`1ÌüÉì4[ö`éøÁt~iô_özt» ÓkTñF®ÃT^¾!L£ßkµ¢to7¼Ò|[uó"[Ó²ÌòÅ¦*£÷Àw_ßÝMÕYEé&J¯Ê.×a¿zKÓª³Î6´|q­ë­èuxí²¨úÜtoè]C·)m+@ùPEiøLMSÅÕ
Zí$¹
AMiA~îS
òy×þåÁ·» \1½$ý÷oÉ?oÑD¹~r]dq¼ÛùÑÍ!ázMa°²´C¿åY
ÁE¸$k°ã=&ZE	íTY'	¿uÊÒM')d¯'e1=^Az âÆá©¸MþË,s·[gß"opsEtuENN(S A×êT²!UÞ	þh,d¯³$ ­b
î>üy.;Uw6aº¦Ï88Ç¶ÊÝOÃ)y×Ñ×ª;
ó8ÙúøaNÆ;ôDÆw`Wb]é6·K<,OnrâX¶xgÛÿ28£ÁÂ±B%tZ*çaÛ{MË¨<!ñtãpEcÏbàZ3ÿÌò&^#&ÿÑ7Í ôÐù>QG_wwUëZ1ønÝÁèÜòîâð\mcÃ¹or7è/vÂzºËÜÎºçÜ (M±'D#4ÿ¼¦pwt¬
+ýðçÈ8C¸ôö¸§CpbÂ\0Xc±%·(ª
ºIÿßèáB ì¾Ï?ÎxÅY. ¹:úX©´zÍøÒ%¸(H?ðýÀsÈ%pW9¼Ès¶Yþ.>Z®ÿ´eBc¯ïBåÃÞ}älÆwyç3ÆÁ¼m	{¼,;qÏr%·=<ì?nYCo1bïÌ0ÈðÎãÝYA¾Í§aüÔ±XâÎÈ9Rõ<+xÜÎ4¶?pT`SÈwpÏ?8¢l¹óÈwA _x÷w,úÉCµVUi))½¯1bê3bË(>S±Ø|:ñüñ\ÒöpNfKÏÈ©Àzq\¯$Ò+òx(Eàc	´óG&és<üÞa­Ê,Új*Îþ¦EnÏÇl9ZîÁó!v Ýì1¼¿sx³?¤£Ùjö8{6ðT&á¼´+eÓÍY¬C2%ÍbÖ
÷zúZÀÇ¯ÖücIÉqáDÚàZcÇÁ¢ N»\_~õ<VÒÖâ4P¢vg¹8]dÆ²7òß;68ëù@\7ä±WÜÀuç¢âé	ç2v.j±Lö±<d5v4¢±^O¨ÉDu~Æ¨ñÜqLM]®wCÚ÷³ÖEË1pì9/E4(ïU?p¡x§Ã¹ó#ÑZ!Ø½¿¢#÷N
ðÎç°ÓS,Y<GP¢ µõ75¿GäNÙ"1q jö|Vüâú³}DÌ	s@4¬ÝÂ?M¤-ÌL'NÝÁ¥Uø<&ó¥,=¸#Ú:PwÛ)|Cêk·$zj <ëb	ÿrÀN|»ëb:páâcPq=ÖPÚ8cËÈ79Ûì%Õö£n\Îµøî¦§=Iÿ5ý©Lö²Ún¢,Ø¦1~]*$â´Å-aÃ-Áè½÷¤ñ6E"ÌH_Ë7µZ#¡9¿Õ^eYg!<øù
M1)îîfß¸Ú&ËÆ²¯1ü9<±te§ÝÇ*Ý\­I×èZíò®
ZÒ»zOÊoCågH¡æK9 ½Ó
]þ:Ôç>Zk"kÒ
_¦5Ní3µKö§yÒh¨fO²t½3ÛÍO¦¿
ÚtmÕt÷g\Îúå?L7g:¨Kc-{Ô»òQo>ñ5sµ\	QÓ¥Ï³ûÄo?j1|WñÓqIT».«^$¿<ÖõjæÈDs2õöQ¦}ÓL|Vÿs­VÁáËþþòéàð
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8c/628eafdd2c50a2cb2674aded91df49c4454900

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8c/628eafdd2c50a2cb2674aded91df49c4454900 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg(þûgcøÄNVÑ9¡±nË>üØþÏ¢ *µ £²AùíûàBvå¿ÌÓ¬ß¼ÁðÒô ×zW
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8c/549f3c08fd1ec49e693483a2d8f5b8e3e0ee5d

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8c/549f3c08fd1ec49e693483a2d8f5b8e3e0ee5d (latin-1)

```text
x+)JMU06`01 Ä¢\Ø£mZ?Oiûú7ûSD ëÎ§
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8c/aee3922824b3d881a9fca0d923e95e0fdbb940

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8c/aee3922824b3d881a9fca0d923e95e0fdbb940 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`0~4wÇöoLµÎ\ÈÐ<|·8q"Tmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ ÷ÎC
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ba/1e4df57f9b343842396ca7b02825003a9b2878

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ba/1e4df57f9b343842396ca7b02825003a9b2878 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Óml[~;É0fãË@ÍãU©EÊoß²+ÿe&¸dýæ
¦Ï  2²U

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/16/1677825da305a8828824332e6c4150e17dc4de

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/16/1677825da305a8828824332e6c4150e17dc4de (latin-1)

```text
xÎM
Â0@a×9E. d&?Í'pïrÒLjÁIÓûÛ+¸}ðÁ[­ëÐî4º183b8³uhNdK¡húrÏÐ8FÈ¼xvè9	#AqSR¼WëúÙö®\E_7YZ^k»/×÷enõ¦aòà½5ôÙXcÔQ¿!ÿK5¶Aý 6ÃB 
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/16/5b623657d22e35d4c5298760e1d6e597e2c9e6

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/16/5b623657d22e35d4c5298760e1d6e597e2c9e6 (latin-1)

```text
xKÊÉOR0¶`H*ÍÌI±âRP(N-)ÉÌK/± )?±(%¾(?¿ÄJA Ió
Ñ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/26/8c5a2d398800c7ca70ee42e3df7c65990febd7

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/26/8c5a2d398800c7ca70ee42e3df7c65990febd7 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLgXÞåÆoÿè7ÝSïßï^LSÊÎ(¨J-È¨,bP~û>¸]ù/óä4Á%ë7o0¼4} ¤QVq
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/26/7c5802d04f1e4fba80d5c1b5e05a2d7fe7c584

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/26/7c5802d04f1e4fba80d5c1b5e05a2d7fe7c584 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`þzhù©Xñß÷¦íÓÝ¾{7Tmyjq^enÃ´]Ó¶¦½ç(N6bIºíÞ ó7C
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/82/fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/82/fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 (latin-1)

```text
xÎÍ
!@aÏTAþc¬À»GÖMDËöï¶àõ%_ò°·¶N	Úæ`ÑQÆRÎsµS%ç¹¹Ä7þLm,¤"2{ XÐ8c1ª)ûJ]f÷ùêC>û>ä#7×Nkë÷¥åõ}ÁÞnRoA^QJõøü¿sNìD
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cb/75fa96e2b075e4796814fd2f97614b5813a0a1

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/cb/75fa96e2b075e4796814fd2f97614b5813a0a1 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Óì=Ë+oúZû,Wzu[~¡ÙyªÔÊ"å·ïÙÿ2ON\²~óÃKÓg  ïôS
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f5/3ac38a0e3ac6129e5325cdbbc15cb5b3b92535

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/f5/3ac38a0e3ac6129e5325cdbbc15cb5b3b92535 (latin-1)

```text
xµ±nÃ0D;û+´1$2M (úA¤£udÈô¿3wî÷{ÇeYfsèÃªª¸æI$rò9ò{,*dbä}³æªsìGQìQ9§ À8õé"%Ø'ô35y·{©îGK^Ï*³z]Ý'¡;ýßû¦uk¥êúûlo³Ý÷±å²|¹©á-ãNþHs´ÇÓil³_¡ïbí
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0e/e929e591d6e17e5fc45f0d6ff8d8a75841388d

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0e/e929e591d6e17e5fc45f0d6ff8d8a75841388d (latin-1)

```text
x½XmoÛ8¾ÏùÂ
°,ÉÞn×í8Ýæê¼ÔvÚm_'ÑZ£mØN·n¸ÿ~¤$ÚrmÎ(B¢¨)ÑGÉ½î¼yõÇÑcÎ>Îüéd8öã`ZÆÌöüÑäÂô/uw:µÛ0§ÓØ;Åí;¶òü3ºFã(ÑzÉÙ»0N×E;ÍÏó$Ë-<|¯)|ãéõ]Ö^­y/Ãø*oË9â·Åoy\´ÉçÏ®õys~ÜÛ,ê¦¾­nÚó¢>ssüßmØÞÔHÖxq@)MÂ¸ üûË®æ¨Ðh®V·¾pÑÂ¼à1ÏØw&}®¢ÅþfïßÂÔÿzçç ¥ç¬ûþ-û÷-È?a"_dIm7Ã¾7`óX°XpX#(Â$nñ¯iCð.)ÈP-ÂoIk|må)çËÖ*ébú¼ôÁKwJ¥R6å¯°,ÝZÝ*<»yD,qfáÕÏZ)ÏÂ¤ù¦ãZmµPLGHÅ²s?ÅdBæwA~=¥É­"H[Ë ^ðGªã³óÝä^v?Hsf'æ)lw¤*¢»èÛÒ.cT2"OnRfç»§CË{ÿ2$}cêªXá$t&§AÛ{Íó0?fóp£`Î#ÏÔpÌ±wjºCw#&¿èf<t'§¯TÑ×ÝgÁâÇL½üF7{Ñ?3½»èôÎÊ³ÇÓáÔ|²cóÐ	.}á¿Ùó7øáôi{ÐºzÂqèó÷ìiæÒËywJ+K ÐîH
ì­ZíàÒë+æôü3Øk¢rJ¦%ô:ÿ£{x0¹ð¥d6äeÉã	¥ÓBN.Á5¸HÞ¸G÷/U =JÐLë¨ðáxÃ¬ãüÍcïüÒt¼0éÑw¡éöq_Ï%¹ÄSPîHG6vS¼ehjfÓ­Zhî# 3¶$Cò	½H;(ê¹Ó¾l»§A!+É@XA¹%'BPû© âá
j+P·ûöÒªÆÅA'í	´ýÑ1rßðÅ5Gà¾Áal:sßs@$ù ¾_HA¯\«È8'N§FL@}D½ã2¥Zl2AÈäòÁDÒrmpR¨Ç3·34APT±
[D.î5£½dîÔèË©iÿv^ÈÑUÂº¼oÄ%[CU?äÊ¡(ùÂ3?^¯ÖÇx6êÎ¡úðØ¦Úb|ÿøÆoÈIÍøOâ6)nJ8-¥<I([c=U¥&eÜÇÓ6=óI`nÇýZáÆïñÜ/#*¤ðQRÙ1°m<Ê:'ÜT÷x8Â
¡pÏUæMOüÙô ä
2¤|8H|*º®g Ðê!ÂvÍp:âôêÁñêÐBN&ÊEp ÆeÆUk¨7ÒEUd>Æ¸ÁÄ¶ë°îMÖdD÷x°mí:©!ÝQYæÜÏïVó$:p{¸G½}¨:`y('°";Duòs¯0@v6õ][jðXQÚô&z7-­¥	_l2óü
Ô!x4^Á»¸« ØÆ*GTÚU>á,Ö¤NX¨ãÀc\áÌÝvÖl=<­.c³-íÍóü\ÓºS¯æ¾º ^°!ãJÅM÷\BB¶IÉÌ~Sbª¶W~ÖªlGV¨²Æ{³9/ÖË0ñ×qß÷e^°|ì¶¸ô*¯©+a«×ÍZ[kz>Ã;DP¸YU7ÕÕÒP§9O"JhèÍM ^×Ây¯qpÀVÒ´ð¸×`{hªti©fËB.AÕEcu1DµÞF3¿Ëýç¼PèHgÖGs'ð¦Cí9²C¬)H¬ªÙ°àØÕcuQ@xJ¼µ¬¬[M9ÌmýÃ2Z¦¤XLÐÕðí¨/¶MýA¹ÊE(ÚX5*±îvO0Â}ÿbbÃÍ_iTí
5¿ÔÉ¥«brìùGÔó/ §Æißu$òÑÌ½.yùÐv
¨T7TfZØr±2xhñë¡Ôá¾àÚLãø#4s /Òv¢ÕmÁÛO7ÜÎoC/ÿyæ}íÏt\üý(S÷P
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/22/d8db100c501acd63cda7bac4d2d52a40e6980e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/22/d8db100c501acd63cda7bac4d2d52a40e6980e (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2ÓZõb'.¸°»ýÙÿ«/·wÕµú]ÞQPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú {W¿
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e9/15c8a124dd283e783510a4027a8eaeb1b83b06

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/e9/15c8a124dd283e783510a4027a8eaeb1b83b06 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥¡'d¾
Ç_¹#ó2MÝøºãñw±PcJ3sRô*ss.y¾x *þÏ©õßfú7÷'CIÎÏKËLg`3-ØÝroV¯þ1¯ÌùæU©EÊoß²+ÿe&¸dýæ
¦Ï  +	S«
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a4/bdc15d0d1f35eb2bcd0a5e22277b866f7136cf

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a4/bdc15d0d1f35eb2bcd0a5e22277b866f7136cf (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹ÏMÛüÉÿç·ÆBÎ¾wÞ}©U[Z\¢WÃ0m×´­i/â9¤XÒn»· HÁB¥
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a4/44947623c21a18550cdd274e5f673b14294a6c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a4/44947623c21a18550cdd274e5f673b14294a6c (latin-1)

```text
xuKoÂ0{Î¯°Ä¥=T}¨ã`áÄ®íÚË
h¨( ª¢¿¾Ë#
TêÍovfó®ÖSrÿà_µ¼aëÍ®ÌË\ÏnHàâyªÌ§ÕºÜ¢Óêp|+óYVl³[ñU>Ï³òÄÂy-ÏóJú"«Xn·þ]0îîÎÑA{ìøð,(mPOQá2	#¢CÅ¼LWio2+wÛj²ªTl#3Jîû`Ø¬a0vT6éÿÚÚ¾ÖñEM¬Ó:ðzÄÙqM^Ìªò·_9³oÂEOHUGìÏñVáñ}yR­É|5Ù.k_j92ä ©qÂ	àäé}÷R!CP©Ó©´4w*¥A_R;78y±ÍÅrçDá7;Wsé£iÄAÒW¬übªQª7ÃRÛëçBOîWðZ|ìV#nÎ!pÑòÇ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a4/388aa6f330261e165273851891db0d6271435f

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/a4/388aa6f330261e165273851891db0d6271435f (latin-1)

```text
x½XYsÛFî³~ÅN<£§0íØm43DÙª)Q&)çxáPÒÆæ×k'Óÿ^`rÖQ·òA»ÀØ ]jgKrvvzþÓÑ~RJ¾N¯¹3ùÙE0²ÆæÂö©sc7¦MOú}Bz=rÞïwöªxC×f*'gi÷;£(]Å5%¢4ßT½¼ÈV´,³¢|³®Êè£"ðæwOEo]Ë(]GémÙã:ì× 4­U¶¦å;UoIïÂhEÕÔ÷ä¾wOZºmlSÊBy¥àÓa´M·Kètä!`.qTV4¥ùA¸OM4ÈoäC÷{OA¹
c:!Çß?ß£rõåªÈâx»ò£/«=Â*ÊR>æY
ÁE¸%{à÷h%Ô¨2#	2§tm$%ì÷¥,¦Ç)¤*®i>	FÛä¿Ì2w+yxvmrDÌqÑí--QV<uÜ«'6ªEÐ©Z÷ßáÂBö*KrÐ2¦àî+È×RÙ¨ÂÜXé¾âàPuTæè~&LÉ»¾U½aÄÎV÷Äs2Ú¢w$2Þ·³èJ·¹]BdI°<¹ÏmýÀ»ý¯!s34ç*Ób`#dc@S¬âQÅç=þ45¬
+Õç#±°¾·ÞÜ÷bÜ	Ã®±FÂ|g_är
]§ÿoôPµ¹óiÆÀ×Å3ÈD)íU@J x!¢ðóÀsH®Ú ôêpWdöúí¬»þd¹þÐÆEù¨o¡ùbyC\Ãé5>ñÁb*Èw9Ã6vØä;3ó­Rhî\AbÁmO89NqÂ-àlàÍ¬í]òL>x|1}ä9ãTpX5 ¸=´¯P³îN..Å6ÒÚþÛ
È±q'5pfÍ|Ëåh¾ÈüÊÏ|`güÎÔ»TERÇ&º"æ¸MÍGb*6s¦S¬#¼{68Æ&³§efElÓfÑÊà("Ý¸"o77<?4éhçÇ
&9æx\ØL£÷²z)Îþ Ene0[L»·DÐ»í#ú3Ç5ûE:Çâü«¤Ú#®^^6|]ZÒûéö*ÄG6¹fÚ
ÏFtà­p ocìaKJW<ikÛ6±þëÂd¡óllÖ±ðJ©¤ùEP7Æ¡Å|?z3H=þ0§bþ¬ZpÕó±ú ¦ë:¢½©Uë56V·ØýHVWÔ)©îsI%añc2ªm]´´$×»xKQfÓ²5$;ê¦£åS²Ìâç÷e:pì¤£T{Tà7StdKõ w¬¦eñ@Îí8 LhQø {®& røÒ*o¡ åP¥¤¹¬øE³Ý¥"Vg8	s×^Y¢;_¸æÕ|gá®¤64àn
7vÜH3ÏãfÛkÃº^À'^°¹õy(N¯ë©éâ¡§Áeý9þÄYZîèÖGbªGDô²£7t1P:\æ·aGþKÿÖÝi<Û÷eµYGY°Ic¼Î³¸¡S1T pÌ»bVÅe ÃÃøu;f¬?]åZìâ¤K3s²3Î,xØT[§+3ëöå{bÖv¤"£L¥¢â:¶ãÆßwà¶¦
Zc¸Åî2Ëª8á[ÃÛ3ç.üwsËnÍý:yîWùT-i¥>¸¡¢öP¨n\~-Õ%TWöl¿"7ÅahéÞÚC%5Ð
¡LUñ:×Ì)j`wÔfAW[Sÿf wh¾än£ÚbÇnî' ¢[8D·¥ku¾Pg «Güqå7þEÂ¨©\¨kMP¼
¦÷ayOfØ¸u1¼éñCJâX%vU¶¾Mýç±nvÓg:}®·Ò-ìÊvâkt.i+¹ÖP9p?m`ö/ÙR¥
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8d/f18af5c3d8c04a0f074964f017a0ce467c81e9

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8d/f18af5c3d8c04a0f074964f017a0ce467c81e9 (latin-1)

```text
x½XmoÛFÞgÿCP×vÚfkÚm)ñ"Û$§/_Ù¾&BôIÎûï#ïE:É®ÁÀ'òHÞCGe&+r28~óËÑ~	bJ>Ï.<k1»Óù7Ñ
miºÞlq¥{WIÇ!ý>è:U±m2ã×iÎQ¯ÃíwAn~%kçI¿Øyð^øFÓû¬¿)z« ÞñuÞç:ì·Gïh\ôÖÉæ/nT½½ñï}USß¢Ûþª¨k6çoé}ÃvS"ÙàÅBiÄà?¼Xv½BN7î<æ¢yAcïû\EüIÞu¿©÷õÞË×~BÇdøþ-ùç-È×?`"_gIî7C¾w`ó¿^SXÃ/$îÑ¯iCð.ÉÈ-ö¤ù_{yJé¦åLr0²>/!}PqCCÿ^TÜ&ÿe¹[ÑÀÓ¶Èk\äAÄg\_Ó¬Ò,HJ' kõÅBe2	!Á)þ(,d¯( ­B
î>üz.{ö6~¼¦Ï88Çgä)ºûSrn/Eì§91õ-qýLöèÑ]	Yt¥ÛÜ.!òÈ°<¹M©®çO
÷ýsÈà5Ë±B%tZ*§~Û{Có ?%
ñóþK³õ¹{®;S§ÿèbPzhOÏÎ]O¨¢¯º»Êüõ--NxyB7G¶6¾ÐÝvÑ]gk¿ÎO~kÙ:trOèû¡?öXn©ýjM-½áP=cÏNB(n8r9áVéeIáê±;OPíôàÒÛkb¼=eøk¬Ø
R¢Ðëôÿ®ÂnâÉâÃ/9KkR©_ºa¥ß¸G»ç""¥Ah'ümXxPàð
+ù¨ß,|tÛýÚ8)u:X²tgsøzÉ|Ð
òmÎp¥öïYÂÚ¥µW
Í}3H,¹í©äáü|áv5r¬1l:çAÆfùg1Fí§åÄ"7ÇæªæY©ãvÎ¥	´ýçI6|ßðÅÑgà¾A9ÖmyìÚ ÌÏ|øÈ}Æ¿âQ¹Vùq.)u¬0bª3â)ùHÌÄbÙBÆäO"cLt:_:µ
lDS3YäèH7,È+âXÚgLMú´óGF	r<üÆa×l
UK±¿iæÅÛèÁó1_ÎFº}ð|è6GïïÞüé#FfþFRÍgÏ5§Ì$v¥ìaº9AuH¦²¤YÌ:RagD ¯|ü`")92.|H\kbXÊÓ.×§§e5Õ ¢eye¥¨ÜYZ±ÌCöñ¡|)Þw
Î:®«y¬Ól{!*zp¾DÆÎ@-iÀ>¬ÂFjyZ­YEáeéçalÁØdauª^ó½Ú
;gåau³£å¼d~S/¿VIøÀâ|æcD±&Ñî« ÖMRC/A/vð.,Ï1ÙQBÖ+DËoîÔ@9êª63¿Dà,®72Q¨yº[h	K¸ø·¯L8v~4ÄP"+*aÒM2Ç3[»Ò;]séÀ­ ×yhk¨T¼û~¹ÿAà+kPÙÅ«þq,®¬ËfÃ}ÇpR6/D´uà®`mp¥ÇÌÖ9²*yù<ÿ?ªi2âùÛMxÛ8ÄOÉÝ-¸¸·Ñz%ððÔúÞZ$"ÃDk¨Fw$EøÐãóù Dù7 ü3ûµÂßU0éVzá. «Rº!º-c¹¹Z®Ðuºù}îe4§wuGbo@±gH¡ÌK9 uPlÞªóÂÈ­55é]-¿êÖ8Õfjì£yÒhh
L[Q§ë½Ù^ïþþ6èºkû¨¦+¸?cïjaV:~ñÃts¶Tçíöñ¶ìãë]=£frN¢+!êo¶tYÿZr²¹©³u1l%êñSqIT»*[6!Oëjµú[Í!ª®×FÕ-´eL3ñktùO0[+>¶qQàï_é+
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8d/396a22ce150039b572768bdc2bc99dd4f84966

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/8d/396a22ce150039b572768bdc2bc99dd4f84966 (latin-1)

```text
xRËnÛ0ìY_±HI
¤"
ä É,X/ö²mÚ"%7ðßwiÇ­k4 ¹ÃÙ4zûÍýtîC¨×[S/=\N¯`à¾\*ø©Ôö¦lzm:BbøtÔSÕvê:©¶¯çµ2ß!¥c©z
]£Ôªy¯èVÁRo\zo]û{®ë®º+Ç	óì!ú`<L±e²¼÷7·sÝ`;ÄýÖÙ}¯ÏÅàÎ <.¨tDÊ£ ËlÈxäï0Ïè¹Ï¥e~ë=ú¥Ì1xØÍúÛ¨$);:ïÖ}Õvãse;Õ«9
=y?×M£_êvMM§ª­&lÌócÎQ<DÎK?
¶nePVz¥@¯©zËÓm»^­:XV¿¬&2:½Ôýæ¦n³^kÓSgSÝv÷¬¶S=SÝ¬ç°ÐTÕ¨hÎHÄ³ýóy8n/zxÑæÙ9?rÜª¡£(SÆ²JáGL`à8Ü)c¡ç½ÚqpÂ^ýÄÖ!²üå3¸w&ÕN0Ø%,ò8qYÔÑP8Ùõøß5dþkà´¯G!4ÏåEÈó$Ùwø8ñºUÑ¤v!(®ÌìÂffÈß®SµuèHeÂQ>añÈ±HJw'JÆ"ô3² /³aÁû»uáÄYÂ|Áö°ß¥ÉMç
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fd/39a90a2eca63a8eeae04cd7f1ea1877e9dc290

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fd/39a90a2eca63a8eeae04cd7f1ea1877e9dc290 (latin-1)

```text
xÎAÂ @Q×hf¦Cc<{S
µ¡ôþö
nòk)k·|ê-%Ë"<	cÔCV'Q¼dãDä]	1`¾ÚÒ§[ÉÊªê00E  ç9#á½'rF÷þªÍ>ëÞìCK²×--u^K½/E×÷%Ör³(]àG{ÀõøëéiúÖÌV_BX
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fd/7396787d98cddc095fd829669186737756b354

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/fd/7396787d98cddc095fd829669186737756b354 (latin-1)

```text
x½YëOÛH¿Ïù+VEB­Ô4m¡ä$6äpØ´÷År,Û²®´ºÿýföa¯ó.Eg¡ìîììÌofggÇfDòñèóñ3zçüÝ¿rGÃÞÀé
.Ü®nhcÓqûÃÝ½ÑLÒhÖëÔjä¤^¯l]bw,-i¶¢Q¯Tüp,f|ñÃxÕâ$Ò4ôÃ,KýsáÚ,«Nüpæ÷i¯a¿UúDÃ¬:f4ýð ®ÐïÉ_'QõcþXdåËóôyIö2G´ÈÀLqäàß®,¹ Cåp>rnà§
iB~nsá-ò'ùrøÃÝïÏn:õ`jÆùù÷E¤Ó_N(Ö!?+°yÄN)èð2?
«ô{à|Ä*ÙQg¬?§Õ,ªÎ½ïÕ4¦tV§Èy\¯K^#\8£÷,X
.ÿ2ÉÜ¬ùÀ³UÉNÄgâßßÓ¤ÓÄ$ÈÆÉùYuÕ¢<Ä!e³ú)þ($$O£yÌ}ñõ^.®f^\yá¾9cºÆh~èÍÙ"ûÁ¿Ëj/NMãÅ¤»fÝ8UØy\W,Çºá¸öeÏpÎßCä ¥£leÍA{	lïMýôTü¾Á7¡ºg¤YúÀ¹Ôí½äÚ¦Z½KÇU'
©æNoúH³S":¯hfÛÒ:WºóÛ&Zí«|ãLíí¨7ÒßmØ<4r[è+[¢¿VGnQ¶ãOn¤CÞS¢¶¸p§T(ó2õÐ­ç§tvPõâXm·mõö©+L¸E2Í¡Çÿ7z¸»»ÃÛSÆ#@yÌP<O70O3º4	ü<Ò­Ð9G.pFü)m(«pwK®d¤
II7Ô,øÀÅ[£ÔÇë¥·iµXAÈ4aGÊÄBs?påØqñ
£C8ÚBsæË!´ö ºr­_áx?Ë½²`Òç4¡)Í¶¡ 1íÚV4?)LjÜ%¯«é´ÔàT5(ÊÈ$¹ÍªKA¼v{Á¬ª²¤ó:ÊKÇ
"UYºÈ3?ZÖA?KG³DRÆçrFEØ&óÔT£*J+·-ÇÛ6ÕkkÆrïÎW `Nö0¶Û{Úü¼Ä´!ÇmegáÕk³¼)eû;od.Ó ¬EÁËEîõ­n9ß`5NÊGÝÓ
§ºÝÁ9ì^óæ7:[t)cc¯T½ÁGkPÚ791Ý4l>.Im{ÔaMûÒ ,HÓxcó¦Ë¤ ÝàFP
X¨×¸Íy%yVÔr1RþÓä6t{Ø±õ>=(¼uCî80 ñoÞ|å
ó=£ßpB;×Â»¨mk
uFôQKNÇA_èöûà0þ ½;n4llDÅ^]J#W°yLÍdàMi{¤ux¼¸÷ #î09HCàa¯« 'Ï*¢hâùJ^>q¿­[»£Á~ò@Ó9¬Á'Ñ~Ì§WmÅGr0Ú°û
Ç#øú#÷KÅñÁ>àaÍä*o\	/,Ã,ñ ~Ë±àºÁ	gÀG!6nåÓLðIÒ5M<òùaGEnwÅ<¢-FòàÈ¼\}½éW;ÀpB@bïËÀhd°
ðÒ8FNc6(gÇEBÂÀ(ØÙÓýÞ`lo<ÒYË­°µeÚY<åKÇçñ´oöÄóSê¦ÏðÖì¸ìoýöÐÜîðÆÿ¶AÔ®vÕTÄ¿.èÛ,Å°ýeÞå[=2Ç"w¬Î@d#ýk%SÎ½ñ¶«º£¿+âõîÂ&ç(<.j´9¡TXa
öø¹`,íí-ø	¹°´ýeðÖÃ\âúõ¾3}¸J¨æÞBv¯Fn·wÓëBÁ¡Ömg.In¸ÇUTmÃÓ®3LÊBÞÝ'ïÂ½
c°5EÞÝl°È¥O¥ªD,BS
ÌúØ[À[APE2eé¡"ÄPP¡TÎ ¢Ø10Á#*ð
¸ ¥UñË/ ËrpEGÑ¶K*gahD27Dr7 ÙKTHRQåÕÊó«¿Úå-øÌÚ7ãÒéÚH-WÕò,-µ T9;FËV¡/;îÍÐtäå_ä­~Rçù-gå]Bç/Ç}V³®%ëärÕ,ÙË%ïVóäÔß,.$pð
OãèÜÃÚÂuXf#æ!±Klo^ !(Ew»e
ÅËZã|±I8*eìÝA)CÊY¯iiÄÏÎÒíÃ²Uù|	¥qþ¯Kï(ùÊpT

üýyÂ$
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ea/da99012e2851653aa5d8824499b5a676e142c2

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ea/da99012e2851653aa5d8824499b5a676e142c2 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcp9ß/¼¨Øð³°esïõ/Îß|z%	CeVq~C«®FFiS)+KJÁÉtÍ3gc¨ÌN­ÌM,`èÜ?¯fÖ½°ªõÎµÞøPÐ`øª¶<µ¸D¯27aÚ®i[Ó^Äs'I±¤?Ývo %D/
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ce/0914496ec5bd77e0876ffd1bd571b267fd057a

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ce/0914496ec5bd77e0876ffd1bd571b267fd057a (latin-1)

```text
x½YëOÛH¿Ïù+VEB­Ô4m¡
9¶í}±dÇ¶l+­î¿}ØkçYÎBÙÝÙÙßÌÎÎÍÔ§äcë¤ñÇÁÞy%®ñ¨?´ûÃ§§éía;ÑæÜ´
ÒhÖëÔjä¤^¯l]buM-i¶¢Q¯T¼`æ/ç|ñhÖ¢8Ñ$	ãäÃ<M¼sáãÚ<­N½`î÷I¯a¿UúD´:ç4ùð ®Ò÷É['QõcñX¦ÅåùGú\]æ)X±)
½ üÛÅ÷Sd¨.O3Ññ½$¥ÉOÂmÎ½Eþ$_xóýÙIf®LMÒ8?#ÿ¡dö"Yúþz1äg6¸³nêA~Â P%{ "ê5õ´Õû½DÎ«9ëuÉásáçÔwKÎÀeò_&µxx¶*Ùã½û{W#{¡Ù89?« ®P#¤t^?ÅäY¸ÀAS¹o ¾ÞËÅÕÔªs7Ñ7gL7²ã3÷ÍÜ[d=xwi­ëF	1ÂÙ#±ÝôÖ¬;'¢
»â3ïë
åaqòCÓmÇºìëöù{ tÛcKYFsPDnÛû@/9U¿o°ïN©î·Mmh_jVß*ùä¶)¥fÿâÒvÔÜGª¹ÓØ=ÒôÎ+Ù1ÛÝ+ÍþmÍÎU¶qFûí¸?ÖÞmØ<4r[è+[¢½fWnQ´ãOn¤CÞãS¢¶¸p§Tã0uSõÐ­ç§pvPõò§cöö©'L¸E2Í Çÿ7z¸»{£Û!Q&c@yÌP<O70O3º4	ü<
­Ð9G&pN¼m(«pw®¦¤II3Ô,øÀÅ[ÂÄÃë¥·iµXAÈ4fGÊÄBs?peØqñ
£C8ÚBsæË!´ö ºr­_áx?å^ÙÆÉK0øÉsÓ¦ÛP ÃvmE«E&5îâ×ÕtLZjpªüi¦~èBÜfUÎ¥ ^»½`VCUYyeM¥cª,Y¦Ë¹.ë £YH"	ãs8£"lyjªQB%ÛMÀAFÛéêµµIO£Æ»ó(X&Ó} L¬Î¦6?6B@#¤3à¸- ìÌ±zÍr7lç.ýÔaµ(¸\ä^ßj¦ý
Vã¤|Ô=­`yªY]Ãî5ony£±%H79Á26¶øJEØìd¼	¥}38pÑ}IÃé#ÙárÔ±Æ]Ø°.uÀ´6o,Þô¤ëpÁêOuàZ ·Ñ5®S>ÏZ.æRJ@Ñq\À¦n`;6 s°·frÈ]Û$þÍ¯¼a¾gôNèdºx÷µÍ!b­¡Î>jÉè8]£Á Æ¤÷FÂºeH2Ù«K!bä
Ö"Ñ6çBx&~JZÄ·»<^
ÜûPÌwÈ\¤!ð°WUPÊç	ùá?4våb%OÇp2èhæ®Ãa·a?ùN éÃÏÖðh?fÓ«¶âË¶Er0Úhù
Çcøú#÷KÅñÁ6äaÍä*o\/,Ã4v¡~Ë°àºá	gÂG!6neÓLðIÒ3<òÙaGEnwù<¢ÍGòàÈ¼Lu½éW;ÄpB@bïÀhd°ì6àË¤qÆlPÎó#Q°³79)§ýáÄÚx¤³Ê­°µeÚY<å¥cóxÀ
Ú7D{ìz	ugxkðwÜÖ·Agdì
wxãÛ jW»j*â_ôfûídØÓL«;25Ô ÝÌ»cc"øØìEZÒ¾vYV-Ü-o{¡ÙÚ»<àÀ.r>ÒXtÉs£½Ë¹¹vt¹}Øã'­oÁ.|pæÂlßh/Ã¹ïº ×®'ð¥8Pqv¹ÿ°'Àa÷jìôú7ý¤ Æ>ot.IÆÔUxmÃÓ®qLEÀ»ûû]°WÑ£·yÊõæ=p.rº.rº¾-§g&¾MÀ}¿òÈì J²#¾®'§Ù\Ep0\
uÉuÉõ5üPÁ£é½=BH%h:H[aå³q
@°uÀu9FàÂÓ²T<S¹ã2Ft¸z '.èñTÎ«¢®B(e¢ #
*·*Ï/ö¥(å¯¬}ó7­éb._©E¬ÊAÚ1R-C]çfd8ù¥²²VòºW?i©óüº³òº/ÀËDÈêì¯³Yß5w±ü9^Iá¨ÕNõ7\eØd,`æZUmî8¬×òs$ZÅÌÝYTt´Ó6ÍxãRëyÏ·GÅEª	V?n{"½ÅAFO(ç.ÿWeËq/qöÏ	Së*Ù
yT
üýC·.Õ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0c/6b9721513e3d138a3f952653e9455820730040

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/0c/6b9721513e3d138a3f952653e9455820730040 (latin-1)

```text
x+)JMU02°d01 ½ôÌÒ$¶|bG.wÕLñ0µýÉùOe¢¡	XIfz^~Q*Òß4ñ/¦¤VÆJ±²¯ß1')?±(¥!0*¦gï6Áü^7.zµ¯ûÔ¤ÒÌ½ÊÄÜK/¨ÿsj=ã·Y§þÃMç½âÉcóóÒ2Ó¬=«Nsþ;¿fÉËô	>fYÞQPZQYÄ üö}p!»ò_æÉiKÖoÞ`xiú M7Uã
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2d/1f3c13f70bbf4902aa677a16566273c0cc2aec

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2d/1f3c13f70bbf4902aa677a16566273c0cc2aec (latin-1)

```text
xAÂ  =ó
> ÙB!1Æ¯,ËRÛTü¿½ø oI&ÖÞ×aâiì"§¥O>`ÖÂ#26»ÊK4íòVÀ%Çs©©4
ì9eR<U&ð<,Y*¡Ïxènß²h]»ÚëîK§õyaí7sð!Ú3x sØcoÈß¡ÙÕ|ß"D(
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2d/a21f21dbea6c83e3f9349cc9036febd26044a0

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/2d/a21f21dbea6c83e3f9349cc9036febd26044a0 (latin-1)

```text
xµ;Â0D©s
÷È¿Ø^	!î(lï"H9Û)çô4¹NÓÈB¸BÑ£-#¢s¥Ñ`R¤1ää}Ì°[b£EvY$² xÑ9ø5eÑØ.nü¬M¼è3ÅåD8rm·Tù.Î oÍñ^·ÚÚÏµÑòþô[ês.BùA
ÁùÄQîéöv¿ÂôWIÇ+kõÑd>
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ef/a2970e2159c2fbc3c196489b07ade735898aad

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/ef/a2970e2159c2fbc3c196489b07ade735898aad (latin-1)

```text
xuRÉnÂ0ì9_aK{@B.ªÄÁIL°pb×v
ôò4@TPª¢_ßÇ*õfÏÌ/óÍvN{7-§Eüín_d«uEnwÄí¸=b×)yFHåUÍ?«mQ¢Ò¨`ÒÙ"ÍË´ÍßÓ¼ÊYZ<[§å8/ãÁHÓõàÞô÷Ô{êuàSÚP¤: 6e!øRÇ4%ÎòÙ|®û1ü&b_V³Míêép$¶ZC&º®Ñ>L,MÂ¿²nG©è*&RImNu¸=Ñé©Å.ËUñ¯xì[}HÂ¢gI¨¸¬-ë+{£xÍáòú*²*ËW¤ÚåfV®k]b0PT[n¹qò|ç^ÂE 2±*±ÜÁî@cov¬¹e
¿fcµ<ñÝ.Ñã\#:Ù(2t©*êfø 1^?¿<q¨à´ØÄ%ÇL_ÂDÉÊzÈÔ
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/64d0bc3dd917926892c55e3706cc116d5b165e

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/64d0bc3dd917926892c55e3706cc116d5b165e (latin-1)

```text
x+)JMU06c040031QÐKÏ,ÉNM-`x6÷ÑìM¯9{wk®+ºqèIOðD [¨
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/3499e3fe2c2f88424539cf1c84130f3c2de248

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/3499e3fe2c2f88424539cf1c84130f3c2de248 (latin-1)

```text
x+)JMU043a040031Q(JMOÎ/ÊKÕKÎÏKcèµÌR:'Ê`¹µ¨¬ûöÉ¹W~x¦a¨Ì*ÎÏchÕÕÈÈ2m*eeIé38®9ÃaælÙ©¹Óö|.M»°_T¥üy|dÄ§Å@Õ§èUææ0LÛ5mkÚxâd#)ô§Ûîíáá üA	
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/d216c1d8c56ae1b5e6c92eafaf428754b09dde

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/d216c1d8c56ae1b5e6c92eafaf428754b09dde (latin-1)

```text
x½XmoÛ8¾ÏùÂ
°,I·õîÚ]'±Û\ÄµvÛÃI´Ö¨c¶Ó­î¿©[JóÒÞ3H¢Hê!EQTgq:#G£ÃßôKPòyt8áØÏiSÛF+3¸2lÒ=ìti·A¦ÓØ)âõ]¾'L¢Ûi4¢d¯|lU¶³<Ó¢HóâÍ¢,¢Sá;Ínòö¢lÍ¢d%7EË°ß½§IÙ§Z¼¹Uåfô6¼6iTU}_Þµg¥.¹>GÖt¯s¤«¬ØÃ¥QRþÝå73dh4ËûÄQQÒæäá6×Þ"ÍïQ|{yÓ!éNPE1b§q¼Y
ùÑÍ#á|Na°Ò¤E¿eiÎG¸$û ":µ´U¦­eø­Ud.ZË9ßw:Ãç-
.h>ëä¿L37ky/ðì\d/b3nnhÞÊh¥d÷èô¤kµÅBU01B*cüQHH§Ë4)ûâëµnaÖZÉ¾8ak#;~¨ÈÐü$\2!ï6úR¶ûaV;ß?ÌÈ`Ü8-Øy\§iGÅÉ]FlÓòï|hù§¯!rÒ7OB£9(B²0í½¥ET«78g4F÷8kýsÓzk>ù¶)
¥îðìÜÔÚGª¹³<ßÑòÎ/4³çýÓÿiÝÞEµq¶ñÒ:æ«-FPnýÅ¿À·/·ÐmÀøé0 	¦÷ü(Å¤® 	Ü)­<-ÃR=tbbçùÑÎ.½º!îY/è¹C]#
	·H¦t}ü£°{x0¹3ðeê òêÈcâyºyÑ¥Ip
.!ý¨;³@xT<PL«¸ ½áVÑq×ÓÞåµéú@'å§îBéõq»¼¹æÉDîr/uloñ%¬¨:¹PÝ'9)×=4l>®I=Ïé3È¶wn¤¼ñx3`ZnqÂ#h?5DLÞÀ¶v»o_®z%:®ç\ª@Ýs`SH·±Ï=Ødlºsßwyó7Ìû~Å	½j­2BÔ¶Æ¨Î>.SÑq0MF#pÿ>GZ
F"Ée÷4RµÈc6s]
åiÆ%yG<ÇèóÑ¸1@=o¹Ë@é2%]]8QéY®§_i$«åÞ2z¦»ïøìHSì?þãÿ!Úßëùmæ¢Ü¹áUq|R§AÞrãÄX¤unÒTê	Äë¬QñÉ|$ Âß=^^1ÇçÛÆ4PoyxäyçXÏ#êz$,ØZÄ»Üø-_wNÁÈøWã«(¨Ð7 gý¡,ÇÊi8V
ë\#U°³{_ªÃéÑp<õª`3U+Q­·Ã:wÎÜLàa Èá<@
ÅÓQAâa9Kã=÷÷iÔØûÔIp"^u·ä¢<:
@»pÏf§¤ò4ß}Çï¸ý±HYæÇ>¦\îÓ6}óU£	G2úAÏt´
Ó:½Æê¶¿ãÜÈ)Â
»Ü ìñ³BmCêk\5¼©§¦^ö´:ÌM±n^Náß	øá¸Jt¹·è/¯aÿÖºÆÈÙÖ\D'âQ:MîýaëP½1©}J0ITøXãA\«E«$ÆÇ`"³ôà5gÚìR«Gyê·ÝÔªY­º2èolÅMbÅê*«÷4giZÆi;Ó /[®V)¾éTl_
ZEiZßØþª'`Z¢ª²P5Â·%n«®ARãm4"ÈiAKRòh¤¤Î£tÚè©P{./5YÜ#¸W,qÏX]$H\^-*umêH
rÚ®*õ¾Ì%R5;LO½è|ã±ÑÊVTHw(sµ6ÙºnÂìW;¨ïXÐP½d¡¾§Ôy^EÈYYEh°êû,îY©ïj#¥ð×íáÈGSÕ´Þ¬$r@ÞÔÑNFµÂÅ%¡îJ«_óVÅ$:VEëNÄ#ï9¥©;Ïjm´VÏÔÀ·÷t
õNK	>¯ARâÈVýÌ5ûÊïqþþDêëD
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/3045ebc6f9b810162c5edc0dda354bbc20788c

```text
## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/objects/d5/3045ebc6f9b810162c5edc0dda354bbc20788c (latin-1)

```text
x½VýsÚFíÏüW§¥IÁqÖI¦ú2P $aìô
Æ 1ÜÓ¿½»ï:t¦­ìy··»··zº7ÇhÄqíôô³êÓý	#^,ðÝ4ÇODý¨^¦$ËMß(ÅµÍ«ÇAÖ$²ð&oE»åqj©ô(Æ³»I ^©ÿk'éá$KÃ7È$«ÂhFïÒêïóÛêm°L§e2ªâ}IÐ3Æi­&ì *ÏÓeýYeæ/ã»L¼å8N3?ã$
/Æñl¨g(Ã+«Õýì.þpV¢ÿuKôsQhiÏ~furÀ
ªZÄó3	nü»YÆMIa-baº %òç¨ÐXwM«©ãÊ¿üpÍ{!<Mç¡'@è = Ç®aõ©M´] Í¨»¶!îUMÃs$'i»@xl 9£	ë{Uó	<~ÅUÓm{¼â-W@x	ÔÑÕV5ar¬2Z.¯âyîE£ß¢$9pñF(cuxoÇ1¤Éúkrü\Ó7U*ß.À©lõ tD+Æk ÊÉDêÊMÄÂCÔ*éEi	r9[C4ç@bcHÜr2q»r¿ð¸V»¥§*bN~ÿÐ ^c 1ÌÉF·ÝV­]sWª½ë-òäò<5¤»¶f±°JP¤®fDõV7	³iYü[ì¥§N¿­[Î£§µ<·UÃÙ«Ï'@:Vâ¬SàKà7À#Æ¢®tÏ¹¼¼:ðøxBÈ$´b:<ïÛNêAíÈjàØ}?îÝÎû¤ªTá]U)ïÞ¢ÂÁè©xø vÛÍ(ÞLéÍ_=XE¬«ZD¼2^ªÈ_9àPÒeÄøøeeº°ÐiÞLè o&ÇÅ	÷Ä
H>f¾ô¡xpZ&E²ÄÒÕPÐgà&©ÊúGÂªõò­Ý
-4µÏß ^¥]X¯R9«<xIú¦{xö{âi°ØÝë¶Þÿ«Ø?$¾>~üÈjüVøøø±(öü%ÂRÅ*Èx
üøðGà/\`ûýtÉ!~
|üÀxpÀÍü¤q÷É¯Pöÿõ
UÞ=Ä®®P>Ö!qd4%¦æªÛÅ,FÊ°îgu®
Wyµ¶M¿<8®¹sKÚZâäÆî½ëiW»JáAÉv«ÓWw°ÕëkªS©_ðé¦­¶ØÐó;±áhVAÏ»wçT'ïiµc¿cZ«´µz1Ý¡5jG²Ø°[¶úÁáµ¤i= aN¸óØë5Y¬>à{X®Lú±ü'XTóM
```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/info/exclude

```text
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/logs/HEAD

```text
0000000000000000000000000000000000000000 aaa8421d5edb07f38ac390c66228fce4ad575d81 Your Name <segodimo@gmail.com> 1751442357 -0300	commit (initial): Initial User Config.
aaa8421d5edb07f38ac390c66228fce4ad575d81 4a3645dcb7af94fd6e9c356aa8ae19526ef9bc64 Your Name <segodimo@gmail.com> 1751445374 -0300	commit: tst01
4a3645dcb7af94fd6e9c356aa8ae19526ef9bc64 6bff9a6b229488f05af3aae7fcdd19fcb4b6d16f Your Name <segodimo@gmail.com> 1751449467 -0300	commit: rec name remplace
6bff9a6b229488f05af3aae7fcdd19fcb4b6d16f aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 Your Name <segodimo@gmail.com> 1751462555 -0300	pull: Fast-forward
aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 43c070367e5b1fd6187a695f93001422e8d5f542 Your Name <segodimo@gmail.com> 1751464540 -0300	commit: tst07
43c070367e5b1fd6187a695f93001422e8d5f542 aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 Your Name <segodimo@gmail.com> 1751468140 -0300	reset: moving to HEAD~1
aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 3f4a2be91d29fc3b5c8f0396c594eb1951a6bae5 Your Name <segodimo@gmail.com> 1751468596 -0300	commit: tst07
3f4a2be91d29fc3b5c8f0396c594eb1951a6bae5 55eb2c073b6481f81f07363551f8c54b8ca6d2c4 Your Name <segodimo@gmail.com> 1751469683 -0300	commit: tst08
55eb2c073b6481f81f07363551f8c54b8ca6d2c4 a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 Your Name <segodimo@gmail.com> 1751474608 -0300	pull: Fast-forward
a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 Your Name <segodimo@gmail.com> 1751539107 -0300	commit: tst09
3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 1f2b44e38e44506018167c9c763e417fb10c1099 Your Name <segodimo@gmail.com> 1751539721 -0300	commit: tst09
1f2b44e38e44506018167c9c763e417fb10c1099 06db4c7c78aafc9e2790db9b1e941294be82b7d8 Your Name <segodimo@gmail.com> 1751540108 -0300	commit: tst09
06db4c7c78aafc9e2790db9b1e941294be82b7d8 1f2b44e38e44506018167c9c763e417fb10c1099 Your Name <segodimo@gmail.com> 1751540558 -0300	reset: moving to HEAD~1
1f2b44e38e44506018167c9c763e417fb10c1099 3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 Your Name <segodimo@gmail.com> 1751540561 -0300	reset: moving to HEAD~1
3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 Your Name <segodimo@gmail.com> 1751540586 -0300	reset: moving to HEAD~1
a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 50472ce19f4bd0d976d3d8021eaed5556c79aaa4 Your Name <segodimo@gmail.com> 1751541792 -0300	commit: tst09
50472ce19f4bd0d976d3d8021eaed5556c79aaa4 fcfc00c1e968dbaca59c4dd86b429a582ef9123a Your Name <segodimo@gmail.com> 1751545600 -0300	pull: Fast-forward
fcfc00c1e968dbaca59c4dd86b429a582ef9123a b197e3c0cfda436a7f6db654779d04486754eff1 Your Name <segodimo@gmail.com> 1751545674 -0300	commit: tst11
b197e3c0cfda436a7f6db654779d04486754eff1 409bd4e84da7d804fec40585e1f386ee3ff7fa66 Your Name <segodimo@gmail.com> 1751546583 -0300	commit: tst12
409bd4e84da7d804fec40585e1f386ee3ff7fa66 cf920df522a9cfeb43270d1adce61c4c40ad411a Your Name <segodimo@gmail.com> 1751546807 -0300	commit: gsh
cf920df522a9cfeb43270d1adce61c4c40ad411a 29bd25016ae5d23003d4c5c880689e051a7f096d Your Name <segodimo@gmail.com> 1751547466 -0300	commit: tst11
29bd25016ae5d23003d4c5c880689e051a7f096d 20757414ebeea84f06b9c6550b29afed64db8244 Your Name <segodimo@gmail.com> 1751548073 -0300	pull: Fast-forward
20757414ebeea84f06b9c6550b29afed64db8244 bc65311b09fddbfd177b9e39b58cafce0fefe1cb Your Name <segodimo@gmail.com> 1751548871 -0300	commit: tst13
bc65311b09fddbfd177b9e39b58cafce0fefe1cb d9655ef0620e03df29cb07910c70e8af9e7c9b0e Your Name <segodimo@gmail.com> 1751549102 -0300	commit: tst13
d9655ef0620e03df29cb07910c70e8af9e7c9b0e f47155f87abbf70104070ecc61b7c43ce1c5c637 Your Name <segodimo@gmail.com> 1751550543 -0300	pull: Fast-forward
f47155f87abbf70104070ecc61b7c43ce1c5c637 fa1b58bd375426fd8f2cfcc3e80616f627a02678 Your Name <segodimo@gmail.com> 1751551451 -0300	pull: Fast-forward
fa1b58bd375426fd8f2cfcc3e80616f627a02678 41ade281df119995e5a425ad67289941e2e482bb Your Name <segodimo@gmail.com> 1751552628 -0300	pull: Fast-forward
41ade281df119995e5a425ad67289941e2e482bb 161677825da305a8828824332e6c4150e17dc4de Your Name <segodimo@gmail.com> 1751553069 -0300	commit: tst16
161677825da305a8828824332e6c4150e17dc4de 4871d8c2d58f3d60e608efc5285f1d482c73e77d Your Name <segodimo@gmail.com> 1751557517 -0300	commit: tst17
4871d8c2d58f3d60e608efc5285f1d482c73e77d 604baee5c1096ea6de4b878ce53500cd84411d87 Your Name <segodimo@gmail.com> 1751580497 -0300	commit: tst18
604baee5c1096ea6de4b878ce53500cd84411d87 fad52593efbe31242b6d28e98a6a3d5ef723d6a5 Your Name <segodimo@gmail.com> 1751580729 -0300	commit: tst18
fad52593efbe31242b6d28e98a6a3d5ef723d6a5 e80915912708da95c4a5549e8e68eb8e1c9a822b Your Name <segodimo@gmail.com> 1751580875 -0300	commit: tst18
e80915912708da95c4a5549e8e68eb8e1c9a822b 51d9d6ec6cc028feb4b86892a22df48dabe5c7ae Your Name <segodimo@gmail.com> 1751585204 -0300	pull: Fast-forward
51d9d6ec6cc028feb4b86892a22df48dabe5c7ae e79e4c6b289b06a389470630b9db01a2e937b9f9 Your Name <segodimo@gmail.com> 1751585690 -0300	commit: tst20
e79e4c6b289b06a389470630b9db01a2e937b9f9 51d9d6ec6cc028feb4b86892a22df48dabe5c7ae Your Name <segodimo@gmail.com> 1751586213 -0300	reset: moving to HEAD~1
51d9d6ec6cc028feb4b86892a22df48dabe5c7ae c84e5a4e9dee4399f70ad69ef057bc2ec1dead34 Your Name <segodimo@gmail.com> 1751586489 -0300	commit: tst20
c84e5a4e9dee4399f70ad69ef057bc2ec1dead34 2da21f21dbea6c83e3f9349cc9036febd26044a0 Your Name <segodimo@gmail.com> 1751586804 -0300	pull: Fast-forward
2da21f21dbea6c83e3f9349cc9036febd26044a0 7fa4aaa65430d2742c0040ce01ddf121bf659b25 Your Name <segodimo@gmail.com> 1751586960 -0300	commit: tst22
7fa4aaa65430d2742c0040ce01ddf121bf659b25 fd39a90a2eca63a8eeae04cd7f1ea1877e9dc290 Your Name <segodimo@gmail.com> 1751587869 -0300	commit: tst22
fd39a90a2eca63a8eeae04cd7f1ea1877e9dc290 600812883f3fc11a0c0e105075e9bb930b493812 Your Name <segodimo@gmail.com> 1751588425 -0300	commit: tst23
600812883f3fc11a0c0e105075e9bb930b493812 c4e5fc1a0adcd14f00f51b69863fccb2f3a66301 Your Name <segodimo@gmail.com> 1751630261 -0300	commit: tst24
c4e5fc1a0adcd14f00f51b69863fccb2f3a66301 21a5008ddc06668407dda8d389b62659611367d9 Your Name <segodimo@gmail.com> 1751632239 -0300	commit: tst25
21a5008ddc06668407dda8d389b62659611367d9 b42c01aab141976c5c4c81bd2359aad580d5678b Your Name <segodimo@gmail.com> 1751639027 -0300	commit: tst26
b42c01aab141976c5c4c81bd2359aad580d5678b 12cdc033df24c88a77a34cc636625515d964506e Your Name <segodimo@gmail.com> 1751648623 -0300	commit: tst27
12cdc033df24c88a77a34cc636625515d964506e 042e511ee39f80394e02fa0e70b42e45c9a7a72f Your Name <segodimo@gmail.com> 1751648786 -0300	commit: tst27
042e511ee39f80394e02fa0e70b42e45c9a7a72f 3b0ea62383f12159220a9bc4686198d090065f52 Your Name <segodimo@gmail.com> 1751651654 -0300	commit: tst28
3b0ea62383f12159220a9bc4686198d090065f52 38ffe5ff42e94c6ac7e24a963046b21d43fce83f Your Name <segodimo@gmail.com> 1751652296 -0300	commit: 28
38ffe5ff42e94c6ac7e24a963046b21d43fce83f 7d270edaf8f47371b9dfe685138e30cfbc229124 Your Name <segodimo@gmail.com> 1751654026 -0300	commit: tst29
7d270edaf8f47371b9dfe685138e30cfbc229124 dedc3fbb60e7b9020b4a4c1083ce961a6bd810d1 Your Name <segodimo@gmail.com> 1751654740 -0300	commit: tst30
dedc3fbb60e7b9020b4a4c1083ce961a6bd810d1 d3344b2ce10ac03ae85037e85d55c033c857f488 Your Name <segodimo@gmail.com> 1751662451 -0300	commit: tst31
d3344b2ce10ac03ae85037e85d55c033c857f488 e0282c7bd8bfa5c3c89c6eb3adca03c451b9edaa Your Name <segodimo@gmail.com> 1751708988 -0300	commit: tst32
e0282c7bd8bfa5c3c89c6eb3adca03c451b9edaa 2d1f3c13f70bbf4902aa677a16566273c0cc2aec Your Name <segodimo@gmail.com> 1753119550 -0300	pull: Fast-forward
2d1f3c13f70bbf4902aa677a16566273c0cc2aec faa600620a2f0315633c582e17dd389026b759a3 Your Name <segodimo@gmail.com> 1753122975 -0300	commit: tst34
faa600620a2f0315633c582e17dd389026b759a3 cab4901ddab86acf376f64d4307ee56f246a842c Your Name <segodimo@gmail.com> 1753126576 -0300	commit: tst44
cab4901ddab86acf376f64d4307ee56f246a842c 70f1d41dfe52532e250cd1b64a532042c66571ab Your Name <segodimo@gmail.com> 1753130345 -0300	commit: tst35
70f1d41dfe52532e250cd1b64a532042c66571ab c0bde767eca51d4c7f6278d3295cfc05d470aca9 Your Name <segodimo@gmail.com> 1753213105 -0300	pull: Fast-forward
c0bde767eca51d4c7f6278d3295cfc05d470aca9 f53ac38a0e3ac6129e5325cdbbc15cb5b3b92535 Your Name <segodimo@gmail.com> 1753215670 -0300	pull: Fast-forward
f53ac38a0e3ac6129e5325cdbbc15cb5b3b92535 28cf19946aa0f01ef28057a0a8cfa0f430955d2f Your Name <segodimo@gmail.com> 1758396436 -0300	commit: ajustes click l e interrogante por slash
28cf19946aa0f01ef28057a0a8cfa0f430955d2f bbb9a04d53b376a7335a78958541be2e0afc3cb3 Your Name <segodimo@gmail.com> 1758484479 -0300	pull: Fast-forward
bbb9a04d53b376a7335a78958541be2e0afc3cb3 1187e08a24475c8bd83fdf418ce90d6868a773e6 Your Name <segodimo@gmail.com> 1758485231 -0300	commit: tst40
1187e08a24475c8bd83fdf418ce90d6868a773e6 bbb9a04d53b376a7335a78958541be2e0afc3cb3 Your Name <segodimo@gmail.com> 1758485478 -0300	reset: moving to HEAD~1
bbb9a04d53b376a7335a78958541be2e0afc3cb3 aea8b52f5ff55da3348c964dc95a726ccaa87d80 Your Name <segodimo@gmail.com> 1758485803 -0300	commit: tst41
aea8b52f5ff55da3348c964dc95a726ccaa87d80 99c7396cf96cff1d424be9954ef5ab21bc6ebda1 Your Name <segodimo@gmail.com> 1758486521 -0300	commit: tst42
99c7396cf96cff1d424be9954ef5ab21bc6ebda1 cfbe0afceac0ab4cdb2b89e01634ff6e4bcf9560 Your Name <segodimo@gmail.com> 1759868399 -0300	commit: add ctrl shift mod 1 e 2
cfbe0afceac0ab4cdb2b89e01634ff6e4bcf9560 857d038241c39637fa9c105d4cb63a906c9a88b6 Your Name <segodimo@gmail.com> 1759870406 -0300	commit: Ftododos corregidos
857d038241c39637fa9c105d4cb63a906c9a88b6 e7f3d6fd51d41c4b364e10545cd0613b99eabda5 Your Name <segodimo@gmail.com> 1760354658 -0300	commit: tst45
e7f3d6fd51d41c4b364e10545cd0613b99eabda5 0046ed8a25956780e12f9d1351a33132793a1044 Your Name <segodimo@gmail.com> 1760469609 -0300	commit: tst47
0046ed8a25956780e12f9d1351a33132793a1044 e7f3d6fd51d41c4b364e10545cd0613b99eabda5 Your Name <segodimo@gmail.com> 1760469643 -0300	reset: moving to HEAD~1
e7f3d6fd51d41c4b364e10545cd0613b99eabda5 ddec986f17042d27e98a5d8ddc74d2e9220acf24 Your Name <segodimo@gmail.com> 1760469655 -0300	pull: Fast-forward
ddec986f17042d27e98a5d8ddc74d2e9220acf24 cace0eb336a0056f4cba5eab0b6fc0a1f0d2ab06 Your Name <segodimo@gmail.com> 1760469968 -0300	commit: tst47
cace0eb336a0056f4cba5eab0b6fc0a1f0d2ab06 3a49b1aab67ae2eaa544534f1c73ebbe74b13975 Your Name <segodimo@gmail.com> 1760470495 -0300	commit: tst47b
3a49b1aab67ae2eaa544534f1c73ebbe74b13975 848bd08cee62d8bc3534c9d0f9a6fd8c5887d71e Your Name <segodimo@gmail.com> 1762715299 -0300	pull: Fast-forward
848bd08cee62d8bc3534c9d0f9a6fd8c5887d71e 82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 Your Name <segodimo@gmail.com> 1764203626 -0300	commit: tst51
82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 aef6aacb7aaf29665d1600d63ea3af6f605f5005 Your Name <segodimo@gmail.com> 1765886258 -0300	pull: Fast-forward
aef6aacb7aaf29665d1600d63ea3af6f605f5005 82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 Your Name <segodimo@gmail.com> 1765888354 -0300	reset: moving to HEAD~1

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/logs/refs/heads/master

```text
0000000000000000000000000000000000000000 aaa8421d5edb07f38ac390c66228fce4ad575d81 Your Name <segodimo@gmail.com> 1751442357 -0300	commit (initial): Initial User Config.
aaa8421d5edb07f38ac390c66228fce4ad575d81 4a3645dcb7af94fd6e9c356aa8ae19526ef9bc64 Your Name <segodimo@gmail.com> 1751445374 -0300	commit: tst01
4a3645dcb7af94fd6e9c356aa8ae19526ef9bc64 6bff9a6b229488f05af3aae7fcdd19fcb4b6d16f Your Name <segodimo@gmail.com> 1751449467 -0300	commit: rec name remplace
6bff9a6b229488f05af3aae7fcdd19fcb4b6d16f aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 Your Name <segodimo@gmail.com> 1751462555 -0300	pull: Fast-forward
aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 43c070367e5b1fd6187a695f93001422e8d5f542 Your Name <segodimo@gmail.com> 1751464540 -0300	commit: tst07
43c070367e5b1fd6187a695f93001422e8d5f542 aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 Your Name <segodimo@gmail.com> 1751468140 -0300	reset: moving to HEAD~1
aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 3f4a2be91d29fc3b5c8f0396c594eb1951a6bae5 Your Name <segodimo@gmail.com> 1751468596 -0300	commit: tst07
3f4a2be91d29fc3b5c8f0396c594eb1951a6bae5 55eb2c073b6481f81f07363551f8c54b8ca6d2c4 Your Name <segodimo@gmail.com> 1751469683 -0300	commit: tst08
55eb2c073b6481f81f07363551f8c54b8ca6d2c4 a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 Your Name <segodimo@gmail.com> 1751474608 -0300	pull: Fast-forward
a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 Your Name <segodimo@gmail.com> 1751539107 -0300	commit: tst09
3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 1f2b44e38e44506018167c9c763e417fb10c1099 Your Name <segodimo@gmail.com> 1751539721 -0300	commit: tst09
1f2b44e38e44506018167c9c763e417fb10c1099 06db4c7c78aafc9e2790db9b1e941294be82b7d8 Your Name <segodimo@gmail.com> 1751540108 -0300	commit: tst09
06db4c7c78aafc9e2790db9b1e941294be82b7d8 1f2b44e38e44506018167c9c763e417fb10c1099 Your Name <segodimo@gmail.com> 1751540558 -0300	reset: moving to HEAD~1
1f2b44e38e44506018167c9c763e417fb10c1099 3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 Your Name <segodimo@gmail.com> 1751540561 -0300	reset: moving to HEAD~1
3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 Your Name <segodimo@gmail.com> 1751540586 -0300	reset: moving to HEAD~1
a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 50472ce19f4bd0d976d3d8021eaed5556c79aaa4 Your Name <segodimo@gmail.com> 1751541792 -0300	commit: tst09
50472ce19f4bd0d976d3d8021eaed5556c79aaa4 fcfc00c1e968dbaca59c4dd86b429a582ef9123a Your Name <segodimo@gmail.com> 1751545600 -0300	pull: Fast-forward
fcfc00c1e968dbaca59c4dd86b429a582ef9123a b197e3c0cfda436a7f6db654779d04486754eff1 Your Name <segodimo@gmail.com> 1751545674 -0300	commit: tst11
b197e3c0cfda436a7f6db654779d04486754eff1 409bd4e84da7d804fec40585e1f386ee3ff7fa66 Your Name <segodimo@gmail.com> 1751546583 -0300	commit: tst12
409bd4e84da7d804fec40585e1f386ee3ff7fa66 cf920df522a9cfeb43270d1adce61c4c40ad411a Your Name <segodimo@gmail.com> 1751546807 -0300	commit: gsh
cf920df522a9cfeb43270d1adce61c4c40ad411a 29bd25016ae5d23003d4c5c880689e051a7f096d Your Name <segodimo@gmail.com> 1751547466 -0300	commit: tst11
29bd25016ae5d23003d4c5c880689e051a7f096d 20757414ebeea84f06b9c6550b29afed64db8244 Your Name <segodimo@gmail.com> 1751548073 -0300	pull: Fast-forward
20757414ebeea84f06b9c6550b29afed64db8244 bc65311b09fddbfd177b9e39b58cafce0fefe1cb Your Name <segodimo@gmail.com> 1751548871 -0300	commit: tst13
bc65311b09fddbfd177b9e39b58cafce0fefe1cb d9655ef0620e03df29cb07910c70e8af9e7c9b0e Your Name <segodimo@gmail.com> 1751549102 -0300	commit: tst13
d9655ef0620e03df29cb07910c70e8af9e7c9b0e f47155f87abbf70104070ecc61b7c43ce1c5c637 Your Name <segodimo@gmail.com> 1751550543 -0300	pull: Fast-forward
f47155f87abbf70104070ecc61b7c43ce1c5c637 fa1b58bd375426fd8f2cfcc3e80616f627a02678 Your Name <segodimo@gmail.com> 1751551451 -0300	pull: Fast-forward
fa1b58bd375426fd8f2cfcc3e80616f627a02678 41ade281df119995e5a425ad67289941e2e482bb Your Name <segodimo@gmail.com> 1751552628 -0300	pull: Fast-forward
41ade281df119995e5a425ad67289941e2e482bb 161677825da305a8828824332e6c4150e17dc4de Your Name <segodimo@gmail.com> 1751553069 -0300	commit: tst16
161677825da305a8828824332e6c4150e17dc4de 4871d8c2d58f3d60e608efc5285f1d482c73e77d Your Name <segodimo@gmail.com> 1751557517 -0300	commit: tst17
4871d8c2d58f3d60e608efc5285f1d482c73e77d 604baee5c1096ea6de4b878ce53500cd84411d87 Your Name <segodimo@gmail.com> 1751580497 -0300	commit: tst18
604baee5c1096ea6de4b878ce53500cd84411d87 fad52593efbe31242b6d28e98a6a3d5ef723d6a5 Your Name <segodimo@gmail.com> 1751580729 -0300	commit: tst18
fad52593efbe31242b6d28e98a6a3d5ef723d6a5 e80915912708da95c4a5549e8e68eb8e1c9a822b Your Name <segodimo@gmail.com> 1751580875 -0300	commit: tst18
e80915912708da95c4a5549e8e68eb8e1c9a822b 51d9d6ec6cc028feb4b86892a22df48dabe5c7ae Your Name <segodimo@gmail.com> 1751585204 -0300	pull: Fast-forward
51d9d6ec6cc028feb4b86892a22df48dabe5c7ae e79e4c6b289b06a389470630b9db01a2e937b9f9 Your Name <segodimo@gmail.com> 1751585690 -0300	commit: tst20
e79e4c6b289b06a389470630b9db01a2e937b9f9 51d9d6ec6cc028feb4b86892a22df48dabe5c7ae Your Name <segodimo@gmail.com> 1751586213 -0300	reset: moving to HEAD~1
51d9d6ec6cc028feb4b86892a22df48dabe5c7ae c84e5a4e9dee4399f70ad69ef057bc2ec1dead34 Your Name <segodimo@gmail.com> 1751586489 -0300	commit: tst20
c84e5a4e9dee4399f70ad69ef057bc2ec1dead34 2da21f21dbea6c83e3f9349cc9036febd26044a0 Your Name <segodimo@gmail.com> 1751586804 -0300	pull: Fast-forward
2da21f21dbea6c83e3f9349cc9036febd26044a0 7fa4aaa65430d2742c0040ce01ddf121bf659b25 Your Name <segodimo@gmail.com> 1751586960 -0300	commit: tst22
7fa4aaa65430d2742c0040ce01ddf121bf659b25 fd39a90a2eca63a8eeae04cd7f1ea1877e9dc290 Your Name <segodimo@gmail.com> 1751587869 -0300	commit: tst22
fd39a90a2eca63a8eeae04cd7f1ea1877e9dc290 600812883f3fc11a0c0e105075e9bb930b493812 Your Name <segodimo@gmail.com> 1751588425 -0300	commit: tst23
600812883f3fc11a0c0e105075e9bb930b493812 c4e5fc1a0adcd14f00f51b69863fccb2f3a66301 Your Name <segodimo@gmail.com> 1751630261 -0300	commit: tst24
c4e5fc1a0adcd14f00f51b69863fccb2f3a66301 21a5008ddc06668407dda8d389b62659611367d9 Your Name <segodimo@gmail.com> 1751632239 -0300	commit: tst25
21a5008ddc06668407dda8d389b62659611367d9 b42c01aab141976c5c4c81bd2359aad580d5678b Your Name <segodimo@gmail.com> 1751639027 -0300	commit: tst26
b42c01aab141976c5c4c81bd2359aad580d5678b 12cdc033df24c88a77a34cc636625515d964506e Your Name <segodimo@gmail.com> 1751648623 -0300	commit: tst27
12cdc033df24c88a77a34cc636625515d964506e 042e511ee39f80394e02fa0e70b42e45c9a7a72f Your Name <segodimo@gmail.com> 1751648786 -0300	commit: tst27
042e511ee39f80394e02fa0e70b42e45c9a7a72f 3b0ea62383f12159220a9bc4686198d090065f52 Your Name <segodimo@gmail.com> 1751651654 -0300	commit: tst28
3b0ea62383f12159220a9bc4686198d090065f52 38ffe5ff42e94c6ac7e24a963046b21d43fce83f Your Name <segodimo@gmail.com> 1751652296 -0300	commit: 28
38ffe5ff42e94c6ac7e24a963046b21d43fce83f 7d270edaf8f47371b9dfe685138e30cfbc229124 Your Name <segodimo@gmail.com> 1751654026 -0300	commit: tst29
7d270edaf8f47371b9dfe685138e30cfbc229124 dedc3fbb60e7b9020b4a4c1083ce961a6bd810d1 Your Name <segodimo@gmail.com> 1751654740 -0300	commit: tst30
dedc3fbb60e7b9020b4a4c1083ce961a6bd810d1 d3344b2ce10ac03ae85037e85d55c033c857f488 Your Name <segodimo@gmail.com> 1751662451 -0300	commit: tst31
d3344b2ce10ac03ae85037e85d55c033c857f488 e0282c7bd8bfa5c3c89c6eb3adca03c451b9edaa Your Name <segodimo@gmail.com> 1751708988 -0300	commit: tst32
e0282c7bd8bfa5c3c89c6eb3adca03c451b9edaa 2d1f3c13f70bbf4902aa677a16566273c0cc2aec Your Name <segodimo@gmail.com> 1753119550 -0300	pull: Fast-forward
2d1f3c13f70bbf4902aa677a16566273c0cc2aec faa600620a2f0315633c582e17dd389026b759a3 Your Name <segodimo@gmail.com> 1753122975 -0300	commit: tst34
faa600620a2f0315633c582e17dd389026b759a3 cab4901ddab86acf376f64d4307ee56f246a842c Your Name <segodimo@gmail.com> 1753126576 -0300	commit: tst44
cab4901ddab86acf376f64d4307ee56f246a842c 70f1d41dfe52532e250cd1b64a532042c66571ab Your Name <segodimo@gmail.com> 1753130345 -0300	commit: tst35
70f1d41dfe52532e250cd1b64a532042c66571ab c0bde767eca51d4c7f6278d3295cfc05d470aca9 Your Name <segodimo@gmail.com> 1753213105 -0300	pull: Fast-forward
c0bde767eca51d4c7f6278d3295cfc05d470aca9 f53ac38a0e3ac6129e5325cdbbc15cb5b3b92535 Your Name <segodimo@gmail.com> 1753215670 -0300	pull: Fast-forward
f53ac38a0e3ac6129e5325cdbbc15cb5b3b92535 28cf19946aa0f01ef28057a0a8cfa0f430955d2f Your Name <segodimo@gmail.com> 1758396436 -0300	commit: ajustes click l e interrogante por slash
28cf19946aa0f01ef28057a0a8cfa0f430955d2f bbb9a04d53b376a7335a78958541be2e0afc3cb3 Your Name <segodimo@gmail.com> 1758484479 -0300	pull: Fast-forward
bbb9a04d53b376a7335a78958541be2e0afc3cb3 1187e08a24475c8bd83fdf418ce90d6868a773e6 Your Name <segodimo@gmail.com> 1758485231 -0300	commit: tst40
1187e08a24475c8bd83fdf418ce90d6868a773e6 bbb9a04d53b376a7335a78958541be2e0afc3cb3 Your Name <segodimo@gmail.com> 1758485478 -0300	reset: moving to HEAD~1
bbb9a04d53b376a7335a78958541be2e0afc3cb3 aea8b52f5ff55da3348c964dc95a726ccaa87d80 Your Name <segodimo@gmail.com> 1758485803 -0300	commit: tst41
aea8b52f5ff55da3348c964dc95a726ccaa87d80 99c7396cf96cff1d424be9954ef5ab21bc6ebda1 Your Name <segodimo@gmail.com> 1758486521 -0300	commit: tst42
99c7396cf96cff1d424be9954ef5ab21bc6ebda1 cfbe0afceac0ab4cdb2b89e01634ff6e4bcf9560 Your Name <segodimo@gmail.com> 1759868399 -0300	commit: add ctrl shift mod 1 e 2
cfbe0afceac0ab4cdb2b89e01634ff6e4bcf9560 857d038241c39637fa9c105d4cb63a906c9a88b6 Your Name <segodimo@gmail.com> 1759870406 -0300	commit: Ftododos corregidos
857d038241c39637fa9c105d4cb63a906c9a88b6 e7f3d6fd51d41c4b364e10545cd0613b99eabda5 Your Name <segodimo@gmail.com> 1760354658 -0300	commit: tst45
e7f3d6fd51d41c4b364e10545cd0613b99eabda5 0046ed8a25956780e12f9d1351a33132793a1044 Your Name <segodimo@gmail.com> 1760469609 -0300	commit: tst47
0046ed8a25956780e12f9d1351a33132793a1044 e7f3d6fd51d41c4b364e10545cd0613b99eabda5 Your Name <segodimo@gmail.com> 1760469643 -0300	reset: moving to HEAD~1
e7f3d6fd51d41c4b364e10545cd0613b99eabda5 ddec986f17042d27e98a5d8ddc74d2e9220acf24 Your Name <segodimo@gmail.com> 1760469655 -0300	pull: Fast-forward
ddec986f17042d27e98a5d8ddc74d2e9220acf24 cace0eb336a0056f4cba5eab0b6fc0a1f0d2ab06 Your Name <segodimo@gmail.com> 1760469968 -0300	commit: tst47
cace0eb336a0056f4cba5eab0b6fc0a1f0d2ab06 3a49b1aab67ae2eaa544534f1c73ebbe74b13975 Your Name <segodimo@gmail.com> 1760470495 -0300	commit: tst47b
3a49b1aab67ae2eaa544534f1c73ebbe74b13975 848bd08cee62d8bc3534c9d0f9a6fd8c5887d71e Your Name <segodimo@gmail.com> 1762715299 -0300	pull: Fast-forward
848bd08cee62d8bc3534c9d0f9a6fd8c5887d71e 82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 Your Name <segodimo@gmail.com> 1764203626 -0300	commit: tst51
82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 aef6aacb7aaf29665d1600d63ea3af6f605f5005 Your Name <segodimo@gmail.com> 1765886258 -0300	pull: Fast-forward
aef6aacb7aaf29665d1600d63ea3af6f605f5005 82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 Your Name <segodimo@gmail.com> 1765888354 -0300	reset: moving to HEAD~1

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/logs/refs/remotes/origin/master

```text
0000000000000000000000000000000000000000 aaa8421d5edb07f38ac390c66228fce4ad575d81 Your Name <segodimo@gmail.com> 1751442359 -0300	update by push
aaa8421d5edb07f38ac390c66228fce4ad575d81 4a3645dcb7af94fd6e9c356aa8ae19526ef9bc64 Your Name <segodimo@gmail.com> 1751445380 -0300	update by push
4a3645dcb7af94fd6e9c356aa8ae19526ef9bc64 6bff9a6b229488f05af3aae7fcdd19fcb4b6d16f Your Name <segodimo@gmail.com> 1751449471 -0300	update by push
6bff9a6b229488f05af3aae7fcdd19fcb4b6d16f aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 Your Name <segodimo@gmail.com> 1751462555 -0300	pull: fast-forward
aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 43c070367e5b1fd6187a695f93001422e8d5f542 Your Name <segodimo@gmail.com> 1751464546 -0300	update by push
43c070367e5b1fd6187a695f93001422e8d5f542 aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 Your Name <segodimo@gmail.com> 1751468148 -0300	update by push
aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 3f4a2be91d29fc3b5c8f0396c594eb1951a6bae5 Your Name <segodimo@gmail.com> 1751468603 -0300	update by push
3f4a2be91d29fc3b5c8f0396c594eb1951a6bae5 55eb2c073b6481f81f07363551f8c54b8ca6d2c4 Your Name <segodimo@gmail.com> 1751469686 -0300	update by push
55eb2c073b6481f81f07363551f8c54b8ca6d2c4 a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 Your Name <segodimo@gmail.com> 1751474608 -0300	pull: fast-forward
a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 Your Name <segodimo@gmail.com> 1751539111 -0300	update by push
3ea01f0f577de819bc0929e8254ab3fe9b0fb2a1 1f2b44e38e44506018167c9c763e417fb10c1099 Your Name <segodimo@gmail.com> 1751539725 -0300	update by push
1f2b44e38e44506018167c9c763e417fb10c1099 06db4c7c78aafc9e2790db9b1e941294be82b7d8 Your Name <segodimo@gmail.com> 1751540112 -0300	update by push
06db4c7c78aafc9e2790db9b1e941294be82b7d8 a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 Your Name <segodimo@gmail.com> 1751540649 -0300	update by push
a80cb0119d9d6bc103e30e085b3a4fbf4c765f78 50472ce19f4bd0d976d3d8021eaed5556c79aaa4 Your Name <segodimo@gmail.com> 1751541796 -0300	update by push
50472ce19f4bd0d976d3d8021eaed5556c79aaa4 fcfc00c1e968dbaca59c4dd86b429a582ef9123a Your Name <segodimo@gmail.com> 1751545600 -0300	pull: fast-forward
fcfc00c1e968dbaca59c4dd86b429a582ef9123a b197e3c0cfda436a7f6db654779d04486754eff1 Your Name <segodimo@gmail.com> 1751545681 -0300	update by push
b197e3c0cfda436a7f6db654779d04486754eff1 409bd4e84da7d804fec40585e1f386ee3ff7fa66 Your Name <segodimo@gmail.com> 1751546587 -0300	update by push
409bd4e84da7d804fec40585e1f386ee3ff7fa66 cf920df522a9cfeb43270d1adce61c4c40ad411a Your Name <segodimo@gmail.com> 1751546839 -0300	update by push
cf920df522a9cfeb43270d1adce61c4c40ad411a 29bd25016ae5d23003d4c5c880689e051a7f096d Your Name <segodimo@gmail.com> 1751547472 -0300	update by push
29bd25016ae5d23003d4c5c880689e051a7f096d 20757414ebeea84f06b9c6550b29afed64db8244 Your Name <segodimo@gmail.com> 1751548073 -0300	pull: fast-forward
20757414ebeea84f06b9c6550b29afed64db8244 bc65311b09fddbfd177b9e39b58cafce0fefe1cb Your Name <segodimo@gmail.com> 1751548875 -0300	update by push
bc65311b09fddbfd177b9e39b58cafce0fefe1cb d9655ef0620e03df29cb07910c70e8af9e7c9b0e Your Name <segodimo@gmail.com> 1751549105 -0300	update by push
d9655ef0620e03df29cb07910c70e8af9e7c9b0e f47155f87abbf70104070ecc61b7c43ce1c5c637 Your Name <segodimo@gmail.com> 1751550543 -0300	pull: fast-forward
f47155f87abbf70104070ecc61b7c43ce1c5c637 fa1b58bd375426fd8f2cfcc3e80616f627a02678 Your Name <segodimo@gmail.com> 1751551451 -0300	pull: fast-forward
fa1b58bd375426fd8f2cfcc3e80616f627a02678 41ade281df119995e5a425ad67289941e2e482bb Your Name <segodimo@gmail.com> 1751552628 -0300	pull: fast-forward
41ade281df119995e5a425ad67289941e2e482bb 161677825da305a8828824332e6c4150e17dc4de Your Name <segodimo@gmail.com> 1751553072 -0300	update by push
161677825da305a8828824332e6c4150e17dc4de 4871d8c2d58f3d60e608efc5285f1d482c73e77d Your Name <segodimo@gmail.com> 1751557521 -0300	update by push
4871d8c2d58f3d60e608efc5285f1d482c73e77d 604baee5c1096ea6de4b878ce53500cd84411d87 Your Name <segodimo@gmail.com> 1751580500 -0300	update by push
604baee5c1096ea6de4b878ce53500cd84411d87 fad52593efbe31242b6d28e98a6a3d5ef723d6a5 Your Name <segodimo@gmail.com> 1751580733 -0300	update by push
fad52593efbe31242b6d28e98a6a3d5ef723d6a5 e80915912708da95c4a5549e8e68eb8e1c9a822b Your Name <segodimo@gmail.com> 1751580879 -0300	update by push
e80915912708da95c4a5549e8e68eb8e1c9a822b 51d9d6ec6cc028feb4b86892a22df48dabe5c7ae Your Name <segodimo@gmail.com> 1751585204 -0300	pull: fast-forward
51d9d6ec6cc028feb4b86892a22df48dabe5c7ae e79e4c6b289b06a389470630b9db01a2e937b9f9 Your Name <segodimo@gmail.com> 1751585694 -0300	update by push
e79e4c6b289b06a389470630b9db01a2e937b9f9 c84e5a4e9dee4399f70ad69ef057bc2ec1dead34 Your Name <segodimo@gmail.com> 1751586517 -0300	update by push
c84e5a4e9dee4399f70ad69ef057bc2ec1dead34 2da21f21dbea6c83e3f9349cc9036febd26044a0 Your Name <segodimo@gmail.com> 1751586804 -0300	pull: fast-forward
2da21f21dbea6c83e3f9349cc9036febd26044a0 7fa4aaa65430d2742c0040ce01ddf121bf659b25 Your Name <segodimo@gmail.com> 1751586963 -0300	update by push
7fa4aaa65430d2742c0040ce01ddf121bf659b25 fd39a90a2eca63a8eeae04cd7f1ea1877e9dc290 Your Name <segodimo@gmail.com> 1751587874 -0300	update by push
fd39a90a2eca63a8eeae04cd7f1ea1877e9dc290 600812883f3fc11a0c0e105075e9bb930b493812 Your Name <segodimo@gmail.com> 1751588429 -0300	update by push
600812883f3fc11a0c0e105075e9bb930b493812 c4e5fc1a0adcd14f00f51b69863fccb2f3a66301 Your Name <segodimo@gmail.com> 1751630265 -0300	update by push
c4e5fc1a0adcd14f00f51b69863fccb2f3a66301 21a5008ddc06668407dda8d389b62659611367d9 Your Name <segodimo@gmail.com> 1751632243 -0300	update by push
21a5008ddc06668407dda8d389b62659611367d9 b42c01aab141976c5c4c81bd2359aad580d5678b Your Name <segodimo@gmail.com> 1751639032 -0300	update by push
b42c01aab141976c5c4c81bd2359aad580d5678b 12cdc033df24c88a77a34cc636625515d964506e Your Name <segodimo@gmail.com> 1751648628 -0300	update by push
12cdc033df24c88a77a34cc636625515d964506e 042e511ee39f80394e02fa0e70b42e45c9a7a72f Your Name <segodimo@gmail.com> 1751648789 -0300	update by push
042e511ee39f80394e02fa0e70b42e45c9a7a72f 3b0ea62383f12159220a9bc4686198d090065f52 Your Name <segodimo@gmail.com> 1751651657 -0300	update by push
3b0ea62383f12159220a9bc4686198d090065f52 38ffe5ff42e94c6ac7e24a963046b21d43fce83f Your Name <segodimo@gmail.com> 1751652302 -0300	update by push
38ffe5ff42e94c6ac7e24a963046b21d43fce83f 7d270edaf8f47371b9dfe685138e30cfbc229124 Your Name <segodimo@gmail.com> 1751654030 -0300	update by push
7d270edaf8f47371b9dfe685138e30cfbc229124 dedc3fbb60e7b9020b4a4c1083ce961a6bd810d1 Your Name <segodimo@gmail.com> 1751654743 -0300	update by push
dedc3fbb60e7b9020b4a4c1083ce961a6bd810d1 d3344b2ce10ac03ae85037e85d55c033c857f488 Your Name <segodimo@gmail.com> 1751662454 -0300	update by push
d3344b2ce10ac03ae85037e85d55c033c857f488 e0282c7bd8bfa5c3c89c6eb3adca03c451b9edaa Your Name <segodimo@gmail.com> 1751708991 -0300	update by push
e0282c7bd8bfa5c3c89c6eb3adca03c451b9edaa 2d1f3c13f70bbf4902aa677a16566273c0cc2aec Your Name <segodimo@gmail.com> 1753119550 -0300	pull: fast-forward
2d1f3c13f70bbf4902aa677a16566273c0cc2aec faa600620a2f0315633c582e17dd389026b759a3 Your Name <segodimo@gmail.com> 1753122983 -0300	update by push
faa600620a2f0315633c582e17dd389026b759a3 cab4901ddab86acf376f64d4307ee56f246a842c Your Name <segodimo@gmail.com> 1753126584 -0300	update by push
cab4901ddab86acf376f64d4307ee56f246a842c 70f1d41dfe52532e250cd1b64a532042c66571ab Your Name <segodimo@gmail.com> 1753130352 -0300	update by push
70f1d41dfe52532e250cd1b64a532042c66571ab c0bde767eca51d4c7f6278d3295cfc05d470aca9 Your Name <segodimo@gmail.com> 1753213105 -0300	pull: fast-forward
c0bde767eca51d4c7f6278d3295cfc05d470aca9 f53ac38a0e3ac6129e5325cdbbc15cb5b3b92535 Your Name <segodimo@gmail.com> 1753215670 -0300	pull: fast-forward
f53ac38a0e3ac6129e5325cdbbc15cb5b3b92535 28cf19946aa0f01ef28057a0a8cfa0f430955d2f Your Name <segodimo@gmail.com> 1758396439 -0300	update by push
28cf19946aa0f01ef28057a0a8cfa0f430955d2f bbb9a04d53b376a7335a78958541be2e0afc3cb3 Your Name <segodimo@gmail.com> 1758484479 -0300	pull: fast-forward
bbb9a04d53b376a7335a78958541be2e0afc3cb3 1187e08a24475c8bd83fdf418ce90d6868a773e6 Your Name <segodimo@gmail.com> 1758485235 -0300	update by push
1187e08a24475c8bd83fdf418ce90d6868a773e6 aea8b52f5ff55da3348c964dc95a726ccaa87d80 Your Name <segodimo@gmail.com> 1758485813 -0300	update by push
aea8b52f5ff55da3348c964dc95a726ccaa87d80 99c7396cf96cff1d424be9954ef5ab21bc6ebda1 Your Name <segodimo@gmail.com> 1758486524 -0300	update by push
99c7396cf96cff1d424be9954ef5ab21bc6ebda1 cfbe0afceac0ab4cdb2b89e01634ff6e4bcf9560 Your Name <segodimo@gmail.com> 1759868411 -0300	update by push
cfbe0afceac0ab4cdb2b89e01634ff6e4bcf9560 857d038241c39637fa9c105d4cb63a906c9a88b6 Your Name <segodimo@gmail.com> 1759870413 -0300	update by push
857d038241c39637fa9c105d4cb63a906c9a88b6 e7f3d6fd51d41c4b364e10545cd0613b99eabda5 Your Name <segodimo@gmail.com> 1760354662 -0300	update by push
e7f3d6fd51d41c4b364e10545cd0613b99eabda5 ddec986f17042d27e98a5d8ddc74d2e9220acf24 Your Name <segodimo@gmail.com> 1760469625 -0300	pull: fast-forward
ddec986f17042d27e98a5d8ddc74d2e9220acf24 cace0eb336a0056f4cba5eab0b6fc0a1f0d2ab06 Your Name <segodimo@gmail.com> 1760469995 -0300	update by push
cace0eb336a0056f4cba5eab0b6fc0a1f0d2ab06 3a49b1aab67ae2eaa544534f1c73ebbe74b13975 Your Name <segodimo@gmail.com> 1760470502 -0300	update by push
3a49b1aab67ae2eaa544534f1c73ebbe74b13975 848bd08cee62d8bc3534c9d0f9a6fd8c5887d71e Your Name <segodimo@gmail.com> 1762715299 -0300	pull: fast-forward
848bd08cee62d8bc3534c9d0f9a6fd8c5887d71e 82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 Your Name <segodimo@gmail.com> 1764203631 -0300	update by push
82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 aef6aacb7aaf29665d1600d63ea3af6f605f5005 Your Name <segodimo@gmail.com> 1765886258 -0300	pull: fast-forward
aef6aacb7aaf29665d1600d63ea3af6f605f5005 82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41 Your Name <segodimo@gmail.com> 1765888409 -0300	update by push

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/logs/refs/remotes/origin/HEAD

```text
0000000000000000000000000000000000000000 aa0123b7297c4e5a1b711ff3945ae05eec05d0c1 Your Name <segodimo@gmail.com> 1751462555 -0300	fetch

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/pre-merge-commit.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/pre-rebase.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/update.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/applypatch-msg.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/commit-msg.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/prepare-commit-msg.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/pre-applypatch.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/pre-push.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/sendemail-validate.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/pre-commit.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/fsmonitor-watchman.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/post-update.sample

```text
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/pre-receive.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/hooks/push-to-checkout.sample

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


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/refs/heads/master

```text
82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/refs/remotes/origin/master

```text
82fc3e7f4a5c3da51bd9a6af7233f32da7ab9a41

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.git/refs/remotes/origin/HEAD

```text
ref: refs/remotes/origin/master

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/.github/workflows/build.yml

```text
name: Build ZMK firmware
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    uses: zmkfirmware/zmk/.github/workflows/build-user-config.yml@main

```


## arquivo: /home/segodimo/zmk-ws/zmk-config/zephyr/module.yml

```text
build:
  settings:
     board_root: .

```


