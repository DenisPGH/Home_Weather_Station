from database_function import TIME_DATE
from paths import USER, USER_CLIENT
from sqlite_db__function import SQLiteSensor

if USER==USER_CLIENT:
    from gpiozero import CPUTemperature


class MonitoringCPU:
    def __init__(self):
        self.__temperature_cpu=50.00
        self.db=SQLiteSensor()
        self.td = TIME_DATE()
        self.mm_old = ""
        self.first_run=0
    def temperature_CPU(self):
        """
        :return: the actual value of the temperature cpu
        """
        date=self.td.date()
        mm = self.td.TIME()[1]
        if USER == USER_CLIENT:
            cpu=CPUTemperature()
            temperature = cpu.temperature
        else:
            temperature = 50.346

        self.__temperature_cpu=int(temperature)

        if mm == "00" or mm == "15" or mm == "30" or mm == "45":
            self.first_run = 1
            if mm != self.mm_old:  # or hh != self.hh_old:
                self.db.add_to_table_cpu(date,str(int(temperature)))
                self.mm_old = mm
        return self.__temperature_cpu