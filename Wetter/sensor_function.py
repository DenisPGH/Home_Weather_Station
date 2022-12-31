
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280



class Sensor:
    def __init__(self):
        self.bus = SMBus(1) # buss
        self.bme280 = BME280(i2c_dev=self.bus)
    def reading(self):
        """
        get the values from the sensor and return it in array [temp,humm,pressure]
        :return:
        """
        temperature = self.bme280.get_temperature()
        pressure = self.bme280.get_pressure()
        humidity = self.bme280.get_humidity()

        return [temperature,humidity,pressure]




