from database_function import DataBaseWetter, TIME_DATE

# uncomment here
from paths import USER,USER_CLIENT
#import copy
from sqlite_db__function import SQLiteSensor


mode=2 # 1=bme280 git, 2= pip install RPi.bme280

if mode==1:
    if USER == USER_CLIENT:
        try:
            from smbus2 import SMBus
        except ImportError:
            from smbus import SMBus
        from bme280 import BME280


    class Sensor:
        def __init__(self):
            if USER == USER_CLIENT:
                self.bus = SMBus(1)  # buss
                self.bme280 = BME280(i2c_dev=self.bus)
            self.db = DataBaseWetter()
            self.db_sql = SQLiteSensor()
            self.td = TIME_DATE()
            self.first_run = 0
            self.hh_old = ""
            self.mm_old = ""

        def reading(self):
            """
            get the values from the sensor and return it in array [temp,humm,pressure]
            :return:
            """
            # uncomment here
            date = self.td.date()
            hh = self.td.TIME()[0]
            mm = self.td.TIME()[1]
            if USER == USER_CLIENT:
                # print('a')
                temperature = int(self.bme280.get_temperature())
                humidity = int(self.bme280.get_humidity())
                pressure = int(self.bme280.get_pressure())

                # temperature=copy.copy(t)
                # humidity=copy.copy(h)
                # pressure=copy.copy(p)
            else:
                temperature = 3
                humidity = 99
                pressure = 1100

            if mm == "00" or mm == "30":  # 1:00, 2:00, 3:00 etc
                self.first_run = 1
                if mm != self.mm_old:  # or hh != self.hh_old:
                    self.db.store_new_info([temperature, humidity, pressure], date, hh, mm)
                    self.db_sql.store_new_info__into__table(date, hh, mm, temperature, humidity, pressure)
                    self.mm_old = mm

            # print(temperature,humidity,pressure)
            return [temperature, humidity, pressure]






elif mode==2 :
    if USER == USER_CLIENT:
        import smbus2
        import bme280

    class Sensor:
        def __init__(self):
            if USER == USER_CLIENT:
                self.port = 1
                self.address = 0x76
                self.bus = smbus2.SMBus(self.port)
                self.calibration_params = bme280.load_calibration_params(self.bus, self.address)

            self.db = DataBaseWetter()
            self.db_sql = SQLiteSensor()
            self.td = TIME_DATE()
            self.first_run = 0
            self.hh_old = ""
            self.mm_old = ""

        def reading(self):
            """
            get the values from the sensor and return it in array [temp,humm,pressure]
            :return:
            """
            # uncomment here
            date = self.td.date()
            hh = self.td.TIME()[0]
            mm = self.td.TIME()[1]
            if USER == USER_CLIENT:

                data = bme280.sample(self.bus, self.address, self.calibration_params)
                temperature= int(data.temperature)
                humidity = int(data.humidity)
                pressure = int(data.pressure)
                #debug
                print(temperature,humidity,pressure)
            else:
                temperature = 3
                humidity = 99
                pressure = 1100

            if mm == "00" or mm == "30":  # 1:00, 2:00, 3:00 etc
                self.first_run = 1
                if mm != self.mm_old:  # or hh != self.hh_old:
                    self.db.store_new_info([temperature, humidity, pressure], date, hh, mm)
                    self.db_sql.store_new_info__into__table(date, hh, mm, temperature, humidity, pressure)
                    self.mm_old = mm

            # print(temperature,humidity,pressure)
            return [temperature, humidity, pressure]





