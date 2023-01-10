from database_function import DataBaseWetter, TIME_DATE

# uncomment here
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280



class Sensor:
    def __init__(self):
        self.bus = SMBus(1) # buss
        self.bme280 = BME280(i2c_dev=self.bus)
        self.db=DataBaseWetter()
        self.td=TIME_DATE()
        self.first_run=0
    def reading(self):
        """
        get the values from the sensor and return it in array [temp,humm,pressure]
        :return:
        """
        # uncomment here
        temperature = int(self.bme280.get_temperature())
        humidity = int(self.bme280.get_humidity())
        pressure = int(self.bme280.get_pressure())
        # temperature=3
        # humidity=99
        # pressure=1100

        date=self.td.date()
        hh=self.td.TIME()[0]
        mm=self.td.TIME()[1]

        if mm == 00 or self.first_run == 0:  # 1:00, 2:00, 3:00 etc
            self.first_run = 1
            self.db.store_new_info([temperature,humidity,pressure],date,hh,mm)

        #print(temperature,humidity,pressure)
        return [temperature,humidity,pressure]




