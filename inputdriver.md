
# Projeto da pasta: /home/segodimo/zmkxrepos/cirque-input-module/

## arquivo: /home/segodimo/zmkxrepos/cirque-input-module/CMakeLists.txt

```text

add_subdirectory(drivers)

```


## arquivo: /home/segodimo/zmkxrepos/cirque-input-module/drivers/CMakeLists.txt

```text

add_subdirectory_ifdef(CONFIG_INPUT input)

```


## arquivo: /home/segodimo/zmkxrepos/cirque-input-module/drivers/input/CMakeLists.txt

```text
# Copyright (c) 2024 The ZMK Contributors
# SPDX-License-Identifier: MIT

zephyr_library_amend()

zephyr_library_sources_ifdef(CONFIG_INPUT_PINNACLE input_pinnacle.c)

target_sources_ifdef(CONFIG_ZMK_INPUT_PINNACLE_IDLE_SLEEPER app PRIVATE zmk_pinnacle_idle_sleeper.c)

```


## arquivo: /home/segodimo/zmkxrepos/cirque-input-module/drivers/input/zmk_pinnacle_idle_sleeper.c

```c


#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zmk/event_manager.h>
#include <zmk/events/activity_state_changed.h>
#include "input_pinnacle.h"

#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(pinnacle_sleeper, CONFIG_INPUT_LOG_LEVEL);

#define GET_PINNACLE(node_id) DEVICE_DT_GET(node_id),

static const struct device *pinnacle_devs[] = {
    DT_FOREACH_STATUS_OKAY(cirque_pinnacle, GET_PINNACLE)
};

static int on_activity_state(const zmk_event_t *eh) {
    struct zmk_activity_state_changed *state_ev = as_zmk_activity_state_changed(eh);

    if (!state_ev) {
        LOG_WRN("NO EVENT, leaving early");
        return 0;
    }

    bool sleep = state_ev->state == ZMK_ACTIVITY_ACTIVE ? 0 : 1;
    for (size_t i = 0; i < ARRAY_SIZE(pinnacle_devs); i++) {
        pinnacle_set_sleep(pinnacle_devs[i], sleep);
    }

    return 0;
}

ZMK_LISTENER(zmk_pinnacle_idle_sleeper, on_activity_state);
ZMK_SUBSCRIPTION(zmk_pinnacle_idle_sleeper, zmk_activity_state_changed);
```


## arquivo: /home/segodimo/zmkxrepos/cirque-input-module/drivers/input/input_pinnacle.h

```c
#pragma once

#include <zephyr/device.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/drivers/spi.h>

#define PINNACLE_READ 0xA0
#define PINNACLE_WRITE 0x80

#define PINNACLE_AUTOINC 0xFC
#define PINNACLE_FILLER 0xFB

// Registers
#define PINNACLE_FW_ID 0x00   // ASIC ID.
#define PINNACLE_FW_VER 0x01  // Firmware Version Firmware revision number.
#define PINNACLE_STATUS1 0x02 // Contains status flags about the state of Pinnacle.
#define PINNACLE_STATUS1_SW_DR BIT(2)
#define PINNACLE_STATUS1_SW_CC BIT(3)
#define PINNACLE_SYS_CFG 0x03 // Contains system operation and configuration bits.
#define PINNACLE_SYS_CFG_EN_SLEEP_BIT 2
#define PINNACLE_SYS_CFG_EN_SLEEP BIT(2)
#define PINNACLE_SYS_CFG_SHUTDOWN BIT(1)
#define PINNACLE_SYS_CFG_RESET BIT(0)

#define PINNACLE_FEED_CFG1 0x04 // Contains feed operation and configuration bits.
#define PINNACLE_FEED_CFG1_EN_FEED BIT(0)
#define PINNACLE_FEED_CFG1_ABS_MODE BIT(1)
#define PINNACLE_FEED_CFG1_DIS_FILT BIT(2)
#define PINNACLE_FEED_CFG1_DIS_X BIT(3)
#define PINNACLE_FEED_CFG1_DIS_Y BIT(4)
#define PINNACLE_FEED_CFG1_INV_X BIT(6)
#define PINNACLE_FEED_CFG1_INV_Y BIT(7)
#define PINNACLE_FEED_CFG2 0x05               // Contains feed operation and configuration bits.
#define PINNACLE_FEED_CFG2_EN_IM BIT(0)       // Intellimouse
#define PINNACLE_FEED_CFG2_DIS_TAP BIT(1)     // Disable all taps
#define PINNACLE_FEED_CFG2_DIS_SEC BIT(2)     // Disable secondary tap
#define PINNACLE_FEED_CFG2_DIS_SCRL BIT(3)    // Disable scroll
#define PINNACLE_FEED_CFG2_DIS_GE BIT(4)      // Disable GlideExtend
#define PINNACLE_FEED_CFG2_EN_BTN_SCRL BIT(6) // Enable Button Scroll
#define PINNACLE_FEED_CFG2_ROTATE_90 BIT(7)   // Swap X & Y
#define PINNACLE_CAL_CFG 0x07                 // Contains calibration configuration bits.
#define PINNACLE_PS2_AUX 0x08                 // Contains Data register for PS/2 Aux Control.
#define PINNACLE_SAMPLE 0x09                  // Sample Rate Number of samples generated per second.
#define PINNACLE_Z_IDLE 0x0A         // Number of Z=0 packets sent when Z goes from >0 to 0.
#define PINNACLE_Z_SCALER 0x0B       // Contains the pen Z_On threshold.
#define PINNACLE_SLEEP_INTERVAL 0x0C // Sleep Interval
#define PINNACLE_SLEEP_TIMER 0x0D    // Sleep Timer
#define PINNACLE_AG_PACKET0 0x10     // trackpad Data (Pinnacle AG)
#define PINNACLE_2_2_PACKET0 0x12    // trackpad Data
#define PINNACLE_REG_COUNT 0x18

#define PINNACLE_REG_ERA_VALUE 0x1B
#define PINNACLE_REG_ERA_HIGH_BYTE 0x1C
#define PINNACLE_REG_ERA_LOW_BYTE 0x1D
#define PINNACLE_REG_ERA_CONTROL 0x1E

#define PINNACLE_ERA_CONTROL_READ 0x01
#define PINNACLE_ERA_CONTROL_WRITE 0x02

#define PINNACLE_ERA_REG_X_AXIS_WIDE_Z_MIN 0x0149
#define PINNACLE_ERA_REG_Y_AXIS_WIDE_Z_MIN 0x0168
#define PINNACLE_ERA_REG_TRACKING_ADC_CONFIG 0x0187

#define PINNACLE_TRACKING_ADC_CONFIG_1X 0x00
#define PINNACLE_TRACKING_ADC_CONFIG_2X 0x40
#define PINNACLE_TRACKING_ADC_CONFIG_3X 0x80
#define PINNACLE_TRACKING_ADC_CONFIG_4X 0xC0

#define PINNACLE_PACKET0_BTN_PRIM BIT(0) // Primary button
#define PINNACLE_PACKET0_BTN_SEC BIT(1)  // Secondary button
#define PINNACLE_PACKET0_BTN_AUX BIT(2)  // Auxiliary (middle?) button
#define PINNACLE_PACKET0_X_SIGN BIT(4)   // X delta sign
#define PINNACLE_PACKET0_Y_SIGN BIT(5)   // Y delta sign

struct pinnacle_data {
    uint8_t btn_cache;
    bool in_int;
    const struct device *dev;
    struct gpio_callback gpio_cb;
    struct k_work work;
};

enum pinnacle_sensitivity {
    PINNACLE_SENSITIVITY_1X,
    PINNACLE_SENSITIVITY_2X,
    PINNACLE_SENSITIVITY_3X,
    PINNACLE_SENSITIVITY_4X,
};

typedef int (*pinnacle_seq_read_t)(const struct device *dev, const uint8_t addr, uint8_t *buf,
                                   const uint8_t len);
typedef int (*pinnacle_write_t)(const struct device *dev, const uint8_t addr, const uint8_t val);

struct pinnacle_config {
    union {
        struct i2c_dt_spec i2c;
        struct spi_dt_spec spi;
    } bus;

    pinnacle_seq_read_t seq_read;
    pinnacle_write_t write;

    bool rotate_90, sleep_en, no_taps, no_secondary_tap, x_invert, y_invert;
    enum pinnacle_sensitivity sensitivity;
    uint8_t x_axis_z_min, y_axis_z_min;
    const struct gpio_dt_spec dr;
};

int pinnacle_set_sleep(const struct device *dev, bool enabled);

```


## arquivo: /home/segodimo/zmkxrepos/cirque-input-module/drivers/input/input_pinnacle.c

```c
#define DT_DRV_COMPAT cirque_pinnacle

#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/init.h>
#include <zephyr/input/input.h>
#include <zephyr/pm/device.h>

#include <zephyr/logging/log.h>

#include "input_pinnacle.h"

LOG_MODULE_REGISTER(pinnacle, CONFIG_INPUT_LOG_LEVEL);

static int pinnacle_seq_read(const struct device *dev, const uint8_t addr, uint8_t *buf,
                             const uint8_t len) {
    const struct pinnacle_config *config = dev->config;
    return config->seq_read(dev, addr, buf, len);
}
static int pinnacle_write(const struct device *dev, const uint8_t addr, const uint8_t val) {
    const struct pinnacle_config *config = dev->config;
    return config->write(dev, addr, val);
}

#if DT_ANY_INST_ON_BUS_STATUS_OKAY(i2c)

static int pinnacle_i2c_seq_read(const struct device *dev, const uint8_t addr, uint8_t *buf,
                                 const uint8_t len) {
    const struct pinnacle_config *config = dev->config;
    return i2c_burst_read_dt(&config->bus.i2c, PINNACLE_READ | addr, buf, len);
}

static int pinnacle_i2c_write(const struct device *dev, const uint8_t addr, const uint8_t val) {
    const struct pinnacle_config *config = dev->config;
    return i2c_reg_write_byte_dt(&config->bus.i2c, PINNACLE_WRITE | addr, val);
}

#endif // DT_ANY_INST_ON_BUS_STATUS_OKAY(i2c)

#if DT_ANY_INST_ON_BUS_STATUS_OKAY(spi)

static int pinnacle_spi_seq_read(const struct device *dev, const uint8_t addr, uint8_t *buf,
                                 const uint8_t len) {
    const struct pinnacle_config *config = dev->config;
    uint8_t tx_buffer[len + 3], rx_dummy[3];
    tx_buffer[0] = PINNACLE_READ | addr;
    memset(&tx_buffer[1], PINNACLE_AUTOINC, len + 2);

    const struct spi_buf tx_buf[2] = {
        {
            .buf = tx_buffer,
            .len = len + 3,
        },
    };
    const struct spi_buf_set tx = {
        .buffers = tx_buf,
        .count = 1,
    };
    struct spi_buf rx_buf[2] = {
        {
            .buf = rx_dummy,
            .len = 3,
        },
        {
            .buf = buf,
            .len = len,
        },
    };
    const struct spi_buf_set rx = {
        .buffers = rx_buf,
        .count = 2,
    };
    int ret = spi_transceive_dt(&config->bus.spi, &tx, &rx);

    return ret;
}

static int pinnacle_spi_write(const struct device *dev, const uint8_t addr, const uint8_t val) {
    const struct pinnacle_config *config = dev->config;
    uint8_t tx_buffer[2] = {PINNACLE_WRITE | addr, val};
    uint8_t rx_buffer[2];

    const struct spi_buf tx_buf = {
        .buf = tx_buffer,
        .len = 2,
    };
    const struct spi_buf_set tx = {
        .buffers = &tx_buf,
        .count = 1,
    };

    const struct spi_buf rx_buf = {
        .buf = rx_buffer,
        .len = 2,
    };
    const struct spi_buf_set rx = {
        .buffers = &rx_buf,
        .count = 1,
    };

    const int ret = spi_transceive_dt(&config->bus.spi, &tx, &rx);

    if (ret < 0) {
        LOG_ERR("spi ret: %d", ret);
    }

    if (rx_buffer[1] != PINNACLE_FILLER) {
        LOG_ERR("bad ret val %d - %d", rx_buffer[0], rx_buffer[1]);
        return -EIO;
    }

    k_usleep(50);

    return ret;
}
#endif // DT_ANY_INST_ON_BUS_STATUS_OKAY(spi)

static int set_int(const struct device *dev, const bool en) {
    const struct pinnacle_config *config = dev->config;
    int ret = gpio_pin_interrupt_configure_dt(&config->dr,
                                              en ? GPIO_INT_EDGE_TO_ACTIVE : GPIO_INT_DISABLE);
    if (ret < 0) {
        LOG_ERR("can't set interrupt");
    }

    return ret;
}

static int pinnacle_clear_status(const struct device *dev) {
    int ret = pinnacle_write(dev, PINNACLE_STATUS1, 0);
    if (ret < 0) {
        LOG_ERR("Failed to clear STATUS1 register: %d", ret);
    }

    return ret;
}

static int pinnacle_era_read(const struct device *dev, const uint16_t addr, uint8_t *val) {
    int ret;

    set_int(dev, false);

    ret = pinnacle_write(dev, PINNACLE_REG_ERA_HIGH_BYTE, (uint8_t)(addr >> 8));
    if (ret < 0) {
        LOG_ERR("Failed to write ERA high byte (%d)", ret);
        return -EIO;
    }

    ret = pinnacle_write(dev, PINNACLE_REG_ERA_LOW_BYTE, (uint8_t)(addr & 0x00FF));
    if (ret < 0) {
        LOG_ERR("Failed to write ERA low byte (%d)", ret);
        return -EIO;
    }

    ret = pinnacle_write(dev, PINNACLE_REG_ERA_CONTROL, PINNACLE_ERA_CONTROL_READ);
    if (ret < 0) {
        LOG_ERR("Failed to write ERA control (%d)", ret);
        return -EIO;
    }

    uint8_t control_val;
    do {

        ret = pinnacle_seq_read(dev, PINNACLE_REG_ERA_CONTROL, &control_val, 1);
        if (ret < 0) {
            LOG_ERR("Failed to read ERA control (%d)", ret);
            return -EIO;
        }

    } while (control_val != 0x00);

    ret = pinnacle_seq_read(dev, PINNACLE_REG_ERA_VALUE, val, 1);

    if (ret < 0) {
        LOG_ERR("Failed to read ERA value (%d)", ret);
        return -EIO;
    }

    ret = pinnacle_clear_status(dev);

    set_int(dev, true);

    return ret;
}

static int pinnacle_era_write(const struct device *dev, const uint16_t addr, uint8_t val) {
    int ret;

    set_int(dev, false);

    ret = pinnacle_write(dev, PINNACLE_REG_ERA_VALUE, val);
    if (ret < 0) {
        LOG_ERR("Failed to write ERA value (%d)", ret);
        return -EIO;
    }

    ret = pinnacle_write(dev, PINNACLE_REG_ERA_HIGH_BYTE, (uint8_t)(addr >> 8));
    if (ret < 0) {
        LOG_ERR("Failed to write ERA high byte (%d)", ret);
        return -EIO;
    }

    ret = pinnacle_write(dev, PINNACLE_REG_ERA_LOW_BYTE, (uint8_t)(addr & 0x00FF));
    if (ret < 0) {
        LOG_ERR("Failed to write ERA low byte (%d)", ret);
        return -EIO;
    }

    ret = pinnacle_write(dev, PINNACLE_REG_ERA_CONTROL, PINNACLE_ERA_CONTROL_WRITE);
    if (ret < 0) {
        LOG_ERR("Failed to write ERA control (%d)", ret);
        return -EIO;
    }

    uint8_t control_val;
    do {

        ret = pinnacle_seq_read(dev, PINNACLE_REG_ERA_CONTROL, &control_val, 1);
        if (ret < 0) {
            LOG_ERR("Failed to read ERA control (%d)", ret);
            return -EIO;
        }

    } while (control_val != 0x00);

    ret = pinnacle_clear_status(dev);

    set_int(dev, true);

    return ret;
}

static void pinnacle_report_data(const struct device *dev) {
    const struct pinnacle_config *config = dev->config;
    uint8_t packet[3];
    int ret;
    ret = pinnacle_seq_read(dev, PINNACLE_STATUS1, packet, 1);
    if (ret < 0) {
        LOG_ERR("read status: %d", ret);
        return;
    }

    LOG_HEXDUMP_DBG(packet, 1, "Pinnacle Status1");

    // Ignore 0xFF packets that indicate communcation failure, or if SW_DR isn't asserted
    if (packet[0] == 0xFF || !(packet[0] & PINNACLE_STATUS1_SW_DR)) {
        return;
    }
    ret = pinnacle_seq_read(dev, PINNACLE_2_2_PACKET0, packet, 3);
    if (ret < 0) {
        LOG_ERR("read packet: %d", ret);
        return;
    }

    LOG_HEXDUMP_DBG(packet, 3, "Pinnacle Packets");

    struct pinnacle_data *data = dev->data;
    uint8_t btn = packet[0] &
                  (PINNACLE_PACKET0_BTN_PRIM | PINNACLE_PACKET0_BTN_SEC | PINNACLE_PACKET0_BTN_AUX);

    int8_t dx = (int8_t)packet[1];
    int8_t dy = (int8_t)packet[2];

    if (packet[0] & PINNACLE_PACKET0_X_SIGN) {
        WRITE_BIT(dx, 7, 1);
    }
    if (packet[0] & PINNACLE_PACKET0_Y_SIGN) {
        WRITE_BIT(dy, 7, 1);
    }

    if (data->in_int) {
        LOG_DBG("Clearing status bit");
        ret = pinnacle_clear_status(dev);
        data->in_int = true;
    }

    if (!config->no_taps && (btn || data->btn_cache)) {
        for (int i = 0; i < 3; i++) {
            uint8_t btn_val = btn & BIT(i);
            if (btn_val != (data->btn_cache & BIT(i))) {
                input_report_key(dev, INPUT_BTN_0 + i, btn_val ? 1 : 0, false, K_FOREVER);
            }
        }
    }

    data->btn_cache = btn;

    input_report_rel(dev, INPUT_REL_X, dx, false, K_FOREVER);
    input_report_rel(dev, INPUT_REL_Y, dy, true, K_FOREVER);

    return;
}

static void pinnacle_work_cb(struct k_work *work) {
    struct pinnacle_data *data = CONTAINER_OF(work, struct pinnacle_data, work);
    pinnacle_report_data(data->dev);
}

static void pinnacle_gpio_cb(const struct device *port, struct gpio_callback *cb, uint32_t pins) {
    struct pinnacle_data *data = CONTAINER_OF(cb, struct pinnacle_data, gpio_cb);

    LOG_DBG("HW DR asserted");
    data->in_int = true;
    k_work_submit(&data->work);
}

static int pinnacle_adc_sensitivity_reg_value(enum pinnacle_sensitivity sensitivity) {
    switch (sensitivity) {
    case PINNACLE_SENSITIVITY_1X:
        return PINNACLE_TRACKING_ADC_CONFIG_1X;
    case PINNACLE_SENSITIVITY_2X:
        return PINNACLE_TRACKING_ADC_CONFIG_2X;
    case PINNACLE_SENSITIVITY_3X:
        return PINNACLE_TRACKING_ADC_CONFIG_3X;
    case PINNACLE_SENSITIVITY_4X:
        return PINNACLE_TRACKING_ADC_CONFIG_4X;
    default:
        return PINNACLE_TRACKING_ADC_CONFIG_1X;
    }
}

static int pinnacle_tune_edge_sensitivity(const struct device *dev) {
    const struct pinnacle_config *config = dev->config;
    int ret;

    uint8_t x_val;
    ret = pinnacle_era_read(dev, PINNACLE_ERA_REG_X_AXIS_WIDE_Z_MIN, &x_val);
    if (ret < 0) {
        LOG_WRN("Failed to read X val");
        return ret;
    }

    LOG_WRN("X val: %d", x_val);

    uint8_t y_val;
    ret = pinnacle_era_read(dev, PINNACLE_ERA_REG_Y_AXIS_WIDE_Z_MIN, &y_val);
    if (ret < 0) {
        LOG_WRN("Failed to read Y val");
        return ret;
    }

    LOG_WRN("Y val: %d", y_val);

    ret = pinnacle_era_write(dev, PINNACLE_ERA_REG_X_AXIS_WIDE_Z_MIN, config->x_axis_z_min);
    if (ret < 0) {
        LOG_ERR("Failed to set X-Axis Min-Z %d", ret);
        return ret;
    }
    ret = pinnacle_era_write(dev, PINNACLE_ERA_REG_Y_AXIS_WIDE_Z_MIN, config->y_axis_z_min);
    if (ret < 0) {
        LOG_ERR("Failed to set Y-Axis Min-Z %d", ret);
        return ret;
    }
    return 0;
}

static int pinnacle_set_adc_tracking_sensitivity(const struct device *dev) {
    const struct pinnacle_config *config = dev->config;

    uint8_t val;
    int ret = pinnacle_era_read(dev, PINNACLE_ERA_REG_TRACKING_ADC_CONFIG, &val);
    if (ret < 0) {
        LOG_ERR("Failed to get ADC sensitivity %d", ret);
    }

    val &= 0x3F;
    val |= pinnacle_adc_sensitivity_reg_value(config->sensitivity);

    ret = pinnacle_era_write(dev, PINNACLE_ERA_REG_TRACKING_ADC_CONFIG, val);
    if (ret < 0) {
        LOG_ERR("Failed to set ADC sensitivity %d", ret);
    }
    ret = pinnacle_era_read(dev, PINNACLE_ERA_REG_TRACKING_ADC_CONFIG, &val);
    if (ret < 0) {
        LOG_ERR("Failed to get ADC sensitivity %d", ret);
    }

    return ret;
}

static int pinnacle_force_recalibrate(const struct device *dev) {
    uint8_t val;
    int ret = pinnacle_seq_read(dev, PINNACLE_CAL_CFG, &val, 1);
    if (ret < 0) {
        LOG_ERR("Failed to get cal config %d", ret);
    }

    val |= 0x01;
    ret = pinnacle_write(dev, PINNACLE_CAL_CFG, val);
    if (ret < 0) {
        LOG_ERR("Failed to force calibration %d", ret);
    }

    do {
        pinnacle_seq_read(dev, PINNACLE_CAL_CFG, &val, 1);
    } while (val & 0x01);

    return ret;
}

int pinnacle_set_sleep(const struct device *dev, bool enabled) {
    uint8_t sys_cfg;
    int ret = pinnacle_seq_read(dev, PINNACLE_SYS_CFG, &sys_cfg, 1);
    if (ret < 0) {
        LOG_ERR("can't read sys config %d", ret);
        return ret;
    }

    if (((sys_cfg & PINNACLE_SYS_CFG_EN_SLEEP) != 0) == enabled) {
        return 0;
    }

    LOG_DBG("Setting sleep: %s", (enabled ? "on" : "off"));
    WRITE_BIT(sys_cfg, PINNACLE_SYS_CFG_EN_SLEEP_BIT, enabled ? 1 : 0);

    ret = pinnacle_write(dev, PINNACLE_SYS_CFG, sys_cfg);
    if (ret < 0) {
        LOG_ERR("can't write sleep config %d", ret);
        return ret;
    }

    return ret;
}

static int pinnacle_init(const struct device *dev) {
    struct pinnacle_data *data = dev->data;
    const struct pinnacle_config *config = dev->config;
    int ret;

    uint8_t fw_id[2];
    ret = pinnacle_seq_read(dev, PINNACLE_FW_ID, fw_id, 2);
    if (ret < 0) {
        LOG_ERR("Failed to get the FW ID %d", ret);
    }

    LOG_DBG("Found device with FW ID: 0x%02x, Version: 0x%02x", fw_id[0], fw_id[1]);

    data->in_int = false;
    k_msleep(10);
    ret = pinnacle_write(dev, PINNACLE_STATUS1, 0); // Clear CC
    if (ret < 0) {
        LOG_ERR("can't write %d", ret);
        return ret;
    }
    k_usleep(50);
    ret = pinnacle_write(dev, PINNACLE_SYS_CFG, PINNACLE_SYS_CFG_RESET);
    if (ret < 0) {
        LOG_ERR("can't reset %d", ret);
        return ret;
    }
    k_msleep(20);
    ret = pinnacle_write(dev, PINNACLE_Z_IDLE, 0x05); // No Z-Idle packets
    if (ret < 0) {
        LOG_ERR("can't write %d", ret);
        return ret;
    }

    ret = pinnacle_set_adc_tracking_sensitivity(dev);
    if (ret < 0) {
        LOG_ERR("Failed to set ADC sensitivity %d", ret);
        return ret;
    }

    ret = pinnacle_tune_edge_sensitivity(dev);
    if (ret < 0) {
        LOG_ERR("Failed to tune edge sensitivity %d", ret);
        return ret;
    }
    ret = pinnacle_force_recalibrate(dev);
    if (ret < 0) {
        LOG_ERR("Failed to force recalibration %d", ret);
        return ret;
    }

    if (config->sleep_en) {
        ret = pinnacle_set_sleep(dev, true);
        if (ret < 0) {
            return ret;
        }
    }

    uint8_t packet[1];
    ret = pinnacle_seq_read(dev, PINNACLE_SLEEP_INTERVAL, packet, 1);

    if (ret >= 0) {
        LOG_DBG("Default sleep interval %d", packet[0]);
    }

    ret = pinnacle_write(dev, PINNACLE_SLEEP_INTERVAL, 255);
    if (ret <= 0) {
        LOG_DBG("Failed to update sleep interaval %d", ret);
    }

    uint8_t feed_cfg2 = PINNACLE_FEED_CFG2_EN_IM | PINNACLE_FEED_CFG2_EN_BTN_SCRL;
    if (config->no_taps) {
        feed_cfg2 |= PINNACLE_FEED_CFG2_DIS_TAP;
    }

    if (config->no_secondary_tap) {
        feed_cfg2 |= PINNACLE_FEED_CFG2_DIS_SEC;
    }

    if (config->rotate_90) {
        feed_cfg2 |= PINNACLE_FEED_CFG2_ROTATE_90;
    }
    ret = pinnacle_write(dev, PINNACLE_FEED_CFG2, feed_cfg2);
    if (ret < 0) {
        LOG_ERR("can't write %d", ret);
        return ret;
    }
    uint8_t feed_cfg1 = PINNACLE_FEED_CFG1_EN_FEED;
    if (config->x_invert) {
        feed_cfg1 |= PINNACLE_FEED_CFG1_INV_X;
    }

    if (config->y_invert) {
        feed_cfg1 |= PINNACLE_FEED_CFG1_INV_Y;
    }
    if (feed_cfg1) {
        ret = pinnacle_write(dev, PINNACLE_FEED_CFG1, feed_cfg1);
    }
    if (ret < 0) {
        LOG_ERR("can't write %d", ret);
        return ret;
    }

    data->dev = dev;

    pinnacle_clear_status(dev);

    gpio_pin_configure_dt(&config->dr, GPIO_INPUT);
    gpio_init_callback(&data->gpio_cb, pinnacle_gpio_cb, BIT(config->dr.pin));
    ret = gpio_add_callback(config->dr.port, &data->gpio_cb);
    if (ret < 0) {
        LOG_ERR("Failed to set DR callback: %d", ret);
        return -EIO;
    }

    k_work_init(&data->work, pinnacle_work_cb);

    pinnacle_write(dev, PINNACLE_FEED_CFG1, feed_cfg1);

    set_int(dev, true);

    return 0;
}

#if IS_ENABLED(CONFIG_PM_DEVICE)

static int pinnacle_pm_action(const struct device *dev, enum pm_device_action action) {
    switch (action) {
    case PM_DEVICE_ACTION_SUSPEND:
        return set_int(dev, false);
    case PM_DEVICE_ACTION_RESUME:
        return set_int(dev, true);
    default:
        return -ENOTSUP;
    }
}

#endif // IS_ENABLED(CONFIG_PM_DEVICE)

#define PINNACLE_INST(n)                                                                           \
    static struct pinnacle_data pinnacle_data_##n;                                                 \
    static const struct pinnacle_config pinnacle_config_##n = {                                    \
        COND_CODE_1(DT_INST_ON_BUS(n, i2c),                                                        \
                    (.bus = {.i2c = I2C_DT_SPEC_INST_GET(n)}, .seq_read = pinnacle_i2c_seq_read,   \
                     .write = pinnacle_i2c_write),                                                 \
                    (.bus = {.spi = SPI_DT_SPEC_INST_GET(n,                                        \
                                                         SPI_OP_MODE_MASTER | SPI_WORD_SET(8) |    \
                                                             SPI_TRANSFER_MSB | SPI_MODE_CPHA,     \
                                                         0)},                                      \
                     .seq_read = pinnacle_spi_seq_read, .write = pinnacle_spi_write)),             \
        .rotate_90 = DT_INST_PROP(n, rotate_90),                                                   \
        .x_invert = DT_INST_PROP(n, x_invert),                                                     \
        .y_invert = DT_INST_PROP(n, y_invert),                                                     \
        .sleep_en = DT_INST_PROP(n, sleep),                                                        \
        .no_taps = DT_INST_PROP(n, no_taps),                                                       \
        .no_secondary_tap = DT_INST_PROP(n, no_secondary_tap),                                     \
        .x_axis_z_min = DT_INST_PROP_OR(n, x_axis_z_min, 5),                                       \
        .y_axis_z_min = DT_INST_PROP_OR(n, y_axis_z_min, 4),                                       \
        .sensitivity = DT_INST_ENUM_IDX_OR(n, sensitivity, PINNACLE_SENSITIVITY_1X),               \
        .dr = GPIO_DT_SPEC_GET_OR(DT_DRV_INST(n), dr_gpios, {}),                                   \
    };                                                                                             \
    PM_DEVICE_DT_INST_DEFINE(n, pinnacle_pm_action);                                               \
    DEVICE_DT_INST_DEFINE(n, pinnacle_init, PM_DEVICE_DT_INST_GET(n), &pinnacle_data_##n,          \
                          &pinnacle_config_##n, POST_KERNEL, CONFIG_INPUT_PINNACLE_INIT_PRIORITY,  \
                          NULL);

DT_INST_FOREACH_STATUS_OKAY(PINNACLE_INST)

```


## arquivo: /home/segodimo/zmkxrepos/cirque-input-module/dts/bindings/vendor-prefixes.txt

```text
cirque	Cirque Corporation

```
input_report_rel
## arquivo: /home/segodimo/zmk/zephyr/subsys/input/input.c


```c
/*
 * Copyright 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_INPUT_H_
#define ZEPHYR_INCLUDE_INPUT_H_

/**
 * @brief Input Interface
 * @defgroup input_interface Input Interface
 * @ingroup io_interfaces
 * @{
 */

#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Input event structure.
 *
 * This structure represents a single input event, for example a key or button
 * press for a single button, or an absolute or relative coordinate for a
 * single axis.
 */
struct input_event {
	/** Device generating the event or NULL. */
	const struct device *dev;
	/** Sync flag. */
	uint8_t sync;
	/** Event type (see @ref INPUT_EV_CODES). */
	uint8_t type;
	/**
	 * Event code (see @ref INPUT_KEY_CODES, @ref INPUT_BTN_CODES,
	 * @ref INPUT_ABS_CODES, @ref INPUT_REL_CODES, @ref INPUT_MSC_CODES).
	 */
	uint16_t code;
	/** Event value. */
	int32_t value;
};

/**
 * @brief Report a new input event.
 *
 * This causes all the listeners for the specified device to be triggered,
 * either synchronously or through the input thread if utilized.
 *
 * @param dev Device generating the event or NULL.
 * @param type Event type (see @ref INPUT_EV_CODES).
 * @param code Event code (see @ref INPUT_KEY_CODES, @ref INPUT_BTN_CODES,
 *        @ref INPUT_ABS_CODES, @ref INPUT_REL_CODES, @ref INPUT_MSC_CODES).
 * @param value Event value.
 * @param sync Set the synchronization bit for the event.
 * @param timeout Timeout for reporting the event, ignored if
 *                @kconfig{CONFIG_INPUT_MODE_SYNCHRONOUS} is used.
 * @retval 0 if the message has been processed.
 * @retval negative if @kconfig{CONFIG_INPUT_MODE_THREAD} is enabled and the
 *         message failed to be enqueued.
 */
int input_report(const struct device *dev,
		 uint8_t type, uint16_t code, int32_t value, bool sync,
		 k_timeout_t timeout);

/**
 * @brief Report a new @ref INPUT_EV_KEY input event, note that value is
 * converted to either 0 or 1.
 *
 * @see input_report() for more details.
 */
static inline int input_report_key(const struct device *dev,
				   uint16_t code, int32_t value, bool sync,
				   k_timeout_t timeout)
{
	return input_report(dev, INPUT_EV_KEY, code, !!value, sync, timeout);
}

/**
 * @brief Report a new @ref INPUT_EV_REL input event.
 *
 * @see input_report() for more details.
 */
static inline int input_report_rel(const struct device *dev,
				   uint16_t code, int32_t value, bool sync,
				   k_timeout_t timeout)
{
	return input_report(dev, INPUT_EV_REL, code, value, sync, timeout);
}

/**
 * @brief Report a new @ref INPUT_EV_ABS input event.
 *
 * @see input_report() for more details.
 */
static inline int input_report_abs(const struct device *dev,
				   uint16_t code, int32_t value, bool sync,
				   k_timeout_t timeout)
{
	return input_report(dev, INPUT_EV_ABS, code, value, sync, timeout);
}

/**
 * @brief Returns true if the input queue is empty.
 *
 * This can be used to batch input event processing until the whole queue has
 * been emptied. Always returns true if @kconfig{CONFIG_INPUT_MODE_SYNCHRONOUS}
 * is enabled.
 */
bool input_queue_empty(void);

/**
 * @brief Input listener callback structure.
 */
struct input_listener {
	/** @ref device pointer or NULL. */
	const struct device *dev;
	/** The callback function. */
	void (*callback)(struct input_event *evt);
};

/**
 * @brief Register a callback structure for input events.
 *
 * The @p _dev field can be used to only invoke callback for events generated
 * by a specific device. Setting dev to NULL causes callback to be invoked for
 * every event.
 *
 * @param _dev @ref device pointer or NULL.
 * @param _callback The callback function.
 */
#define INPUT_CALLBACK_DEFINE(_dev, _callback)                                 \
	static const STRUCT_SECTION_ITERABLE(input_listener,                   \
					     _input_listener__##_callback) = { \
		.dev = _dev,                                                   \
		.callback = _callback,                                         \
	}

#ifdef __cplusplus
}
#endif

/** @} */

#endif /* ZEPHYR_INCLUDE_INPUT_H_ */
```

```c
/*
 * Copyright 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/input/input.h>
#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/iterable_sections.h>

LOG_MODULE_REGISTER(input, CONFIG_INPUT_LOG_LEVEL);

#ifdef CONFIG_INPUT_MODE_THREAD

K_MSGQ_DEFINE(input_msgq, sizeof(struct input_event),
	      CONFIG_INPUT_QUEUE_MAX_MSGS, 4);

#endif

static void input_process(struct input_event *evt)
{
	STRUCT_SECTION_FOREACH(input_listener, listener) {
		if (listener->dev == NULL || listener->dev == evt->dev) {
			listener->callback(evt);
		}
	}
}

bool input_queue_empty(void)
{
#ifdef CONFIG_INPUT_MODE_THREAD
	if (k_msgq_num_used_get(&input_msgq) > 0) {
		return false;
	}
#endif
	return true;
}

int input_report(const struct device *dev,
		 uint8_t type, uint16_t code, int32_t value, bool sync,
		 k_timeout_t timeout)
{
	struct input_event evt = {
		.dev = dev,
		.sync = sync,
		.type = type,
		.code = code,
		.value = value,
	};

#ifdef CONFIG_INPUT_MODE_THREAD
	return k_msgq_put(&input_msgq, &evt, timeout);
#else
	input_process(&evt);
	return 0;
#endif
}

#ifdef CONFIG_INPUT_MODE_THREAD

static void input_thread(void)
{
	struct input_event evt;
	int ret;

	while (true) {
		ret = k_msgq_get(&input_msgq, &evt, K_FOREVER);
		if (ret) {
			LOG_ERR("k_msgq_get error: %d", ret);
			continue;
		}

		input_process(&evt);
	}
}

#define INPUT_THREAD_PRIORITY \
	COND_CODE_1(CONFIG_INPUT_THREAD_PRIORITY_OVERRIDE, \
		    (CONFIG_INPUT_THREAD_PRIORITY), (K_LOWEST_APPLICATION_THREAD_PRIO))

K_THREAD_DEFINE(input,
		CONFIG_INPUT_THREAD_STACK_SIZE,
		input_thread,
		NULL, NULL, NULL,
		INPUT_THREAD_PRIORITY, 0, 0);

#endif /* CONFIG_INPUT_MODE_THREAD */
```
