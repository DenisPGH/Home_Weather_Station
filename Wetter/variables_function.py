import datetime


class Variables:
    def __init__(self):
        self.fg_buttons = 'White'
        self.bg_buttons = "Black"
        self.size_buttons = 17
        self.font_buttons = 'Areil'
        self.value_unit = {'temperature': "C", 'pressure': 'hPa', 'humidity': "%"}
        self.interval_refresh_page = 10000  # 4000
        self.width = 700
        self.height = 700
        self.value = 0
        self.VIDEO_ON = False
        self.VIDEO_TEXT = 'Video'
        self.FG = 'White'
        self.VIDEO_BG = 'Green'
        self.VIDEO_SIZE_FONT = 10
        self.VIDEO_TEXT_FG = 'White'
        self.VIDEO_STOPPED_STRING = 'Stopped!'
        self.VIDEO_ON_STRING = 'Recording...'
        self.VIDEO_MODUS = self.VIDEO_STOPPED_STRING

        # self.dinamic_value_function = {1: self.sensor.reading()[0],
        #                                2: self.sensor.reading()[1],
        #                                3: self.sensor.reading()[2],
        #                                4: datetime.datetime.today().strftime('%d-%m-%Y    %H:%M'),
        #                                5: self.outside.acctual_temperature_outside()[0],
        #                                6: self.outside.acctual_temperature_outside()[1],
        #                                7: self.outside.acctual_temperature_outside()[2],
        #
        #                                }
        ####
        # values
        self.FS_VALUE_SIZE = 65
        self.FS_LEVEL_VALUES = 350
        self.FS_VALUE_X_TEMP = 65
        self.FS_VALUE_X_HUM = 355
        self.FS_VALUE_X_PRESS = 600
        self.FS_VALUE_X_TEMP_OUTSIDE = 360
        self.FS_VALUE_Y_TEMP_OUTSIDE = 200
        self.FS_VALUE_X_TIME = 0
        self.FS_VALUE_Y_TIME = 0
        self.FS_SIZE_VALUE_TIME = 50

        self.FS_VALUE_X_NAMEDAY = 20
        self.FS_VALUE_Y_NAMEDAY = 100
        self.FS_SIZE_VALUE_NAMEDAY = 20

        self.FS_VALUE_X_VIDEO_MODE = 600
        self.FS_VALUE_Y_VIDEO_MODE = 100
        self.FS_SIZE_VALUE_VIDEO_MODE = 12

        self.FS_VALUE_X_WETTER_STATUS = 380
        self.FS_VALUE_Y_WETTER_STATUS = 175
        self.FS_SIZE_VALUE_WETTER_STATUS = 16

        self.FS_VALUE_X_PRESSURE_OUTSIDE = 600
        self.FS_VALUE_Y_PRESSURE_OUTSIDE = 230
        self.FS_SIZE_VALUE_PRESSURE_OUTSIDE = 20

        self.FS_VALUE_X_CPU_TEMP = 60
        self.FS_VALUE_Y_CPU_TEMP = 200
        self.FS_SIZE_VALUE_CPU_TEMP = 40

        self.FS_VIDEO_BUTTON_X = 500
        self.FS_VIDEO_BUTTON_Y = 100
        # table
        self.FS_LEVEL_TABLES = 320
        self.FS_TABLE_X_TEMP = 60
        self.FS_TABLE_X_HUM = 350
        self.FS_TABLE_X_PRESS = 600
        self.FS_TABLE_X_TEMP_OUTSIDE = 345
        self.FS_TABLE_Y_TEMP_OUTSIDE = 150
        self.FS_TABLE_X_PRESS_OUTSIDE = 600
        self.FS_TABLE_Y_PRESS_OUTSIDE = 200

        self.FS_TABLE_X_CPU_TEMP = 60
        self.FS_TABLE_Y_CPU_TEMP = 150
        # units
        self.FS_SIZE_UNITS = 20
        self.FS_LEVEL_UNITS = 370
        self.FS_UNITS_X_TEMP = 170
        self.FS_UNITS_X_HUM = 470
        self.FS_UNITS_X_PRESS = 735
        self.FS_UNITS_X_TEMP_OUTSIDE = 490
        self.FS_UNITS_Y_TEMP_OUTSIDE = 240

        self.FS_UNITS_X_PRESSURE_OUTSIDE = 735
        self.FS_UNITS_Y_PRESSURE_OUTSIDE = 250

        self.FS_UNITS_X_CPU_TEMP = 190
        self.FS_UNITS_Y_CPU_TEMP = 220
        # buttons
        self.FS_LEVEL_BUTTONS = 440
        self.FS_BUTTON_X_HISTORY_TEMP = 30
        self.FS_BUTTON_X_HISTORY_HUM = 320
        self.FS_BUTTON_X_HISTORY_PRESS = 570
        self.FS_BUTTON_X_BREAK = 750
        self.FS_BUTTON_Y_BREAK = 0

        self.FS_BUTTON_X_SHUTDOWN = 740
        self.FS_BUTTON_Y_SHUTDOWN = 60
        self.FS_SHUTDOWN_SIZE = 13

        self.FS_BUTTON_X_HISTORY_TEMP_OUTSIDE = 360
        self.FS_BUTTON_Y_HISTORY_TEMP_OUTSIDE = 285
        self.FS_HISTORY_TEMP_OUTSIDE_SIZE = 13

        self.FS_BUTTON_X_HISTORY_CPU_TEMP = 70
        self.FS_BUTTON_Y_HISTORY_CPU_TEMP = 285
        self.FS_HISTORY_HISTORY_CPU_SIZE = 13


################
        # self.fg_buttons = 'White'
        # self.bg_buttons = "Black"
        # self.size_buttons = 17
        # self.font_buttons = 'Areil'
        # self.value_unit = {'temperature': "C", 'pressure': 'hPa', 'humidity': "%"}
        # self.interval_refresh_page = 10000  # 4000
        # self.history=History()
        # self.width = 700
        # self.height = 700
        # self.value = 0
        ###################
        # self.VIDEO_ON=False
        # self.VIDEO_TEXT = 'Video'
        # self.FG = 'White'
        # self.VIDEO_BG = 'Green'
        # self.VIDEO_SIZE_FONT = 10
        # self.VIDEO_TEXT_FG='White'
        # self.VIDEO_STOPPED_STRING='Stopped!'
        # self.VIDEO_ON_STRING='Recording...'
        # self.VIDEO_MODUS=self.VIDEO_STOPPED_STRING
        #
        # self.dinamic_value_function={1: self.sensor.reading()[0],
        #                              2: self.sensor.reading()[1],
        #                              3: self.sensor.reading()[2],
        #                              4: datetime.datetime.today().strftime('%d-%m-%Y    %H:%M'),
        #                              5: self.outside.acctual_temperature_outside()[0],
        #                              6: self.outside.acctual_temperature_outside()[1],
        #                              7: self.outside.acctual_temperature_outside()[2],
        #
        #                              }
        # ####
        # #values
        # self.FS_VALUE_SIZE=65
        # self.FS_LEVEL_VALUES=350
        # self.FS_VALUE_X_TEMP = 65
        # self.FS_VALUE_X_HUM = 355
        # self.FS_VALUE_X_PRESS = 600
        # self.FS_VALUE_X_TEMP_OUTSIDE = 380
        # self.FS_VALUE_Y_TEMP_OUTSIDE = 200
        # self.FS_VALUE_X_TIME = 0
        # self.FS_VALUE_Y_TIME = 0
        # self.FS_SIZE_VALUE_TIME = 50
        #
        #
        # self.FS_VALUE_X_NAMEDAY = 20
        # self.FS_VALUE_Y_NAMEDAY = 100
        # self.FS_SIZE_VALUE_NAMEDAY = 20
        #
        # self.FS_VALUE_X_VIDEO_MODE = 600
        # self.FS_VALUE_Y_VIDEO_MODE = 100
        # self.FS_SIZE_VALUE_VIDEO_MODE = 12
        #
        # self.FS_VALUE_X_WETTER_STATUS = 380
        # self.FS_VALUE_Y_WETTER_STATUS = 175
        # self.FS_SIZE_VALUE_WETTER_STATUS = 16
        #
        # self.FS_VALUE_X_PRESSURE_OUTSIDE = 600
        # self.FS_VALUE_Y_PRESSURE_OUTSIDE = 230
        # self.FS_SIZE_VALUE_PRESSURE_OUTSIDE = 20
        #
        #
        # self.FS_VIDEO_BUTTON_X=500
        # self.FS_VIDEO_BUTTON_Y=100
        # # table
        # self.FS_LEVEL_TABLES = 320
        # self.FS_TABLE_X_TEMP=60
        # self.FS_TABLE_X_HUM=350
        # self.FS_TABLE_X_PRESS=600
        # self.FS_TABLE_X_TEMP_OUTSIDE=345
        # self.FS_TABLE_Y_TEMP_OUTSIDE=150
        # self.FS_TABLE_X_PRESS_OUTSIDE=600
        # self.FS_TABLE_Y_PRESS_OUTSIDE=200
        # #units
        # self.FS_SIZE_UNITS=20
        # self.FS_LEVEL_UNITS = 370
        # self.FS_UNITS_X_TEMP = 170
        # self.FS_UNITS_X_HUM = 470
        # self.FS_UNITS_X_PRESS = 735
        # self.FS_UNITS_X_TEMP_OUTSIDE = 470
        # self.FS_UNITS_Y_TEMP_OUTSIDE = 240
        #
        # self.FS_UNITS_X_PRESSURE_OUTSIDE = 735
        # self.FS_UNITS_Y_PRESSURE_OUTSIDE = 250
        # #buttons
        # self.FS_LEVEL_BUTTONS = 440
        # self.FS_BUTTON_X_HISTORY_TEMP = 30
        # self.FS_BUTTON_X_HISTORY_HUM = 320
        # self.FS_BUTTON_X_HISTORY_PRESS = 570
        # self.FS_BUTTON_X_BREAK = 750
        # self.FS_BUTTON_Y_BREAK = 0
        #
        # self.FS_BUTTON_X_SHUTDOWN = 740
        # self.FS_BUTTON_Y_SHUTDOWN = 60
        # self.FS_SHUTDOWN_SIZE=13
