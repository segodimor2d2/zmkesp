import time

class MPR121:
    REG_TOUCH_STATUS_L = 0x00
    REG_TOUCH_STATUS_H = 0x01
    REG_ECR            = 0x5E
    REG_DEBOUNCE       = 0x5B
    REG_SOFTRESET      = 0x80
    REG_TOUCH_THR_BASE = 0x41
    REG_RELEASE_THR_BASE = 0x42

    def __init__(self, i2c, addr=0x5A, electrodes=12,
                 touch_thr=12, release_thr=6,
                 debounce_press=1, debounce_release=1):
        print("iniciando mpr121")
        self.i2c = i2c
        self.addr = addr
        self.electrodes = min(max(electrodes, 1), 12)

        # Reset do chip
        self._write8(self.REG_SOFTRESET, 0x63)
        time.sleep_ms(1)

        # Desliga todos os eletrodos
        self._write8(self.REG_ECR, 0x00)

        # Configura debounce
        debounce_val = ((debounce_press & 0x0F) << 4) | (debounce_release & 0x0F)
        self._write8(self.REG_DEBOUNCE, debounce_val)

        # Configura thresholds por eletrodo
        for i in range(self.electrodes):
            self._write8(self.REG_TOUCH_THR_BASE + 2*i, touch_thr)
            self._write8(self.REG_RELEASE_THR_BASE + 2*i, release_thr)

        # Ativa os eletrodos + modo automático
        enable_val = 0x80 | (self.electrodes & 0x0F)
        self._write8(self.REG_ECR, enable_val)

    def _write8(self, reg, val):
        self.i2c.writeto(self.addr, bytes([reg, val & 0xFF]))

    def _read16(self, reg):
        self.i2c.writeto(self.addr, bytes([reg]))
        data = self.i2c.readfrom(self.addr, 2)
        return data[0] | (data[1] << 8)

    def get_touched_mask(self):
        return self._read16(self.REG_TOUCH_STATUS_L) & 0x0FFF

    def is_touched(self, electrode):
        if electrode < 0 or electrode >= self.electrodes:
            return False
        return bool(self.get_touched_mask() & (1 << electrode))
