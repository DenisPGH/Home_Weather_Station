import datetime
import os
from cpu_monitoring_function import MonitoringCPU
from day_info_function import Ortodox
from paths import USER, USER_CLIENT
from sensor_function import Sensor
from variables_function import Variables
from wetter_outside_function import Outside


class Switch_helper_test(Variables):
    def __init__(self):
        super().__init__()
        self.sensor = Sensor()
        self.outside = Outside()
        self.cpu_raspi = MonitoringCPU()
        self.orthodox = Ortodox()
    def searched_index(self, index):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(index), lambda: default)()

    def case_1(self):
        return self.sensor.reading()[0]

    def case_2(self):
        return self.sensor.reading()[1]

    def case_3(self):
        return self.sensor.reading()[2]

    def case_4(self):
        time=datetime.datetime.today().strftime('%H:%M  %d-%m-%Y')
        ### restat here ##############################################
        hh, mm = time.split("  ")[0].split(":")
        if f"{hh}:{mm}" == self.TIME_RESTART and USER == USER_CLIENT and self.IS_REBOOT == False:
            print('Reboot')
            self.IS_REBOOT = True
            os.system('sudo reboot')
        return time

    def case_5(self):
        return self.outside.acctual_temperature_outside()[0]

    def case_6(self):
        word = self.outside.acctual_temperature_outside()[1]
        if word in self.DICTIONARY_DE_to_BG.keys():
            to_return = self.DICTIONARY_DE_to_BG[word]
        else:
            to_return = self.outside.acctual_temperature_outside()[1]
        return to_return

    def case_7(self):
        return self.outside.acctual_temperature_outside()[2]

    def case_8(self):
        return self.cpu_raspi.temperature_CPU()

    def case_9(self):
        return  f"Wrong password! You have {self.MAX_ENTERS_PASSWORD - self.TRIES_ENTER_PASSWORD} more times."

    def case_10(self):
        text_ = self.orthodox.current_day_ortodox()
        if text_ != "":
            to_return = f"Днес:  {text_}"
        else:
            to_return = self.STRING_NO_NAMEDAY

        return to_return

    def case_11(self):
        self.value = self.VIDEO_MODUS
        self.VIDEO_BG = 'Red' if self.VIDEO_ON == True else 'Green'
        self.VIDEO_TEXT = 'Stop video' if self.VIDEO_ON == True else 'Play video'




