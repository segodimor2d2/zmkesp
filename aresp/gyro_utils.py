import time
from mpu6050 import MPU6050

class GyroReader:
    def __init__(self, i2c, samples=10):
        self.sensor = MPU6050(i2c)
        self.samples = samples

    def read_average_gyro(self):
        x_values, y_values, z_values = [], [], []
        for _ in range(self.samples):
            gyro = self.sensor.get_gyro()
            x_values.append(gyro['x'])
            y_values.append(gyro['y'])
            z_values.append(gyro['z'])
            time.sleep(0.01)
        return {
            'x': sum(x_values) / self.samples,
            'y': sum(y_values) / self.samples,
            'z': sum(z_values) / self.samples,
        }

    def read_raw_gyro(self):
        return self.sensor.get_gyro()
