# Projeto da pasta: /home/segodimo/zmk/app/include/zmk/events

## arquivo: /home/segodimo/zmk/app/include/zmk/events/split_peripheral_status_changed.h

```c
/*
 * Copyright (c) 2022 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>

struct zmk_split_peripheral_status_changed {
    bool connected;
};

ZMK_EVENT_DECLARE(zmk_split_peripheral_status_changed);

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/position_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>

#define ZMK_POSITION_STATE_CHANGE_SOURCE_LOCAL UINT8_MAX

struct zmk_position_state_changed {
    uint8_t source;
    uint32_t position;
    bool state;
    int64_t timestamp;
};

ZMK_EVENT_DECLARE(zmk_position_state_changed);

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/hid_indicators_changed.h

```c
/*
 * Copyright (c) 2022 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zmk/hid_indicators_types.h>
#include <zmk/event_manager.h>

struct zmk_hid_indicators_changed {
    zmk_hid_indicators_t indicators;
};

ZMK_EVENT_DECLARE(zmk_hid_indicators_changed);

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/layer_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>

struct zmk_layer_state_changed {
    uint8_t layer;
    bool state;
    int64_t timestamp;
};

ZMK_EVENT_DECLARE(zmk_layer_state_changed);

static inline int raise_layer_state_changed(uint8_t layer, bool state) {
    return raise_zmk_layer_state_changed((struct zmk_layer_state_changed){
        .layer = layer, .state = state, .timestamp = k_uptime_get()});
}

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/usb_conn_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zephyr/usb/usb_device.h>

#include <zmk/event_manager.h>
#include <zmk/usb.h>

struct zmk_usb_conn_state_changed {
    enum zmk_usb_conn_state conn_state;
};

ZMK_EVENT_DECLARE(zmk_usb_conn_state_changed);
```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/endpoint_changed.h

```c
/*
 * Copyright (c) 2021 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>

#include <zmk/endpoints_types.h>
#include <zmk/event_manager.h>

struct zmk_endpoint_changed {
    struct zmk_endpoint_instance endpoint;
};

ZMK_EVENT_DECLARE(zmk_endpoint_changed);

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/ble_active_profile_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>
#include <zephyr/device.h>

#include <zmk/ble/profile.h>

struct zmk_ble_active_profile_changed {
    uint8_t index;
    struct zmk_ble_profile *profile;
};

ZMK_EVENT_DECLARE(zmk_ble_active_profile_changed);

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/battery_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>

struct zmk_battery_state_changed {
    // TODO: Other battery channels
    uint8_t state_of_charge;
};

ZMK_EVENT_DECLARE(zmk_battery_state_changed);

struct zmk_peripheral_battery_state_changed {
    uint8_t source;
    // TODO: Other battery channels
    uint8_t state_of_charge;
};

ZMK_EVENT_DECLARE(zmk_peripheral_battery_state_changed);
```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/sensor_event.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>

#include <zmk/event_manager.h>
#include <zmk/sensors.h>

// TODO: Move to Kconfig when we need more than one channel
#define ZMK_SENSOR_EVENT_MAX_CHANNELS 1

struct zmk_sensor_event {
    size_t channel_data_size;
    struct zmk_sensor_channel_data channel_data[ZMK_SENSOR_EVENT_MAX_CHANNELS];

    int64_t timestamp;

    uint8_t sensor_index;
};

ZMK_EVENT_DECLARE(zmk_sensor_event);
```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/activity_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>
#include <zmk/activity.h>

struct zmk_activity_state_changed {
    enum zmk_activity_state state;
};

ZMK_EVENT_DECLARE(zmk_activity_state_changed);
```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/keycode_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>
#include <zmk/keys.h>

struct zmk_keycode_state_changed {
    uint16_t usage_page;
    uint32_t keycode;
    uint8_t implicit_modifiers;
    uint8_t explicit_modifiers;
    bool state;
    int64_t timestamp;
};

ZMK_EVENT_DECLARE(zmk_keycode_state_changed);

static inline struct zmk_keycode_state_changed
zmk_keycode_state_changed_from_encoded(uint32_t encoded, bool pressed, int64_t timestamp) {
    uint16_t page = ZMK_HID_USAGE_PAGE(encoded);
    uint16_t id = ZMK_HID_USAGE_ID(encoded);
    uint8_t implicit_modifiers = 0x00;
    uint8_t explicit_modifiers = 0x00;

    if (!page) {
        page = HID_USAGE_KEY;
    }

    if (is_mod(page, id)) {
        explicit_modifiers = SELECT_MODS(encoded);
    } else {
        implicit_modifiers = SELECT_MODS(encoded);
    }

    return (struct zmk_keycode_state_changed){.usage_page = page,
                                              .keycode = id,
                                              .implicit_modifiers = implicit_modifiers,
                                              .explicit_modifiers = explicit_modifiers,
                                              .state = pressed,
                                              .timestamp = timestamp};
}

static inline int raise_zmk_keycode_state_changed_from_encoded(uint32_t encoded, bool pressed,
                                                               int64_t timestamp) {
    return raise_zmk_keycode_state_changed(
        zmk_keycode_state_changed_from_encoded(encoded, pressed, timestamp));
}

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/modifiers_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/keys.h>
#include <zmk/event_manager.h>

struct zmk_modifiers_state_changed {
    zmk_mod_flags_t modifiers;
    bool state;
};

ZMK_EVENT_DECLARE(zmk_modifiers_state_changed);
```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/wpm_state_changed.h

```c
/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zephyr/kernel.h>
#include <zmk/event_manager.h>
#include <zmk/wpm.h>

struct zmk_wpm_state_changed {
    int state;
};

ZMK_EVENT_DECLARE(zmk_wpm_state_changed);

```


## arquivo: /home/segodimo/zmk/app/include/zmk/events/mouse_button_state_changed.h

```c

/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#pragma once

#include <zmk/hid.h>
#include <zmk/event_manager.h>
#include <zmk/pointing.h>

struct zmk_mouse_button_state_changed {
    zmk_mouse_button_t buttons;
    bool state;
    int64_t timestamp;
};

ZMK_EVENT_DECLARE(zmk_mouse_button_state_changed);

static inline int raise_zmk_mouse_button_state_changed_from_encoded(uint32_t encoded, bool pressed,
                                                                    int64_t timestamp) {
    return raise_zmk_mouse_button_state_changed((struct zmk_mouse_button_state_changed){
        .buttons = ZMK_HID_USAGE_ID(encoded), .state = pressed, .timestamp = timestamp});
}

```


