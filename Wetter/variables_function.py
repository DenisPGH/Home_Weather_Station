import datetime


class Variables:
    def __init__(self):
        self.PASSWORD = '1234'
        self.TRIES_ENTER_PASSWORD=0
        self.MAX_ENTERS_PASSWORD=3
        self.TIME_RESTART='07:05' #"HH:MM"
        self.IS_REBOOT=False
        self.DEGREE_SIGN=u'\N{DEGREE SIGN}'
        self.MAX_TEMPERATURE_CPU=65    # degrees



        self.password=''
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

        self.FS_VALUE_X_WETTER_STATUS = 360
        self.FS_VALUE_Y_WETTER_STATUS = 175
        self.FS_SIZE_VALUE_WETTER_STATUS = 16

        self.FS_VALUE_X_PRESSURE_OUTSIDE = 600
        self.FS_VALUE_Y_PRESSURE_OUTSIDE = 230
        self.FS_SIZE_VALUE_PRESSURE_OUTSIDE = 20

        self.FS_VALUE_X_CPU_TEMP = 65
        self.FS_VALUE_Y_CPU_TEMP = 200
        self.FS_SIZE_VALUE_CPU_TEMP = 65

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

        self.SS_TABLE_X_LABEL_CHART = 370
        self.SS_TABLE_Y_LABEL_CHART = 430
        # units
        self.FS_SIZE_UNITS = 40
        self.FS_SIZE_UNITS_hPa = 20
        self.FS_LEVEL_UNITS = 370
        self.FS_UNITS_X_TEMP = 170
        self.FS_UNITS_X_HUM = 470
        self.FS_UNITS_X_PRESS = 735
        self.FS_UNITS_X_TEMP_OUTSIDE = 470
        self.FS_UNITS_Y_TEMP_OUTSIDE = 220

        self.FS_UNITS_X_PRESSURE_OUTSIDE = 735
        self.FS_UNITS_Y_PRESSURE_OUTSIDE = 250

        self.FS_UNITS_X_CPU_TEMP = 170
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

        self.SS_LEVEL_BUTTONS=420
        self.FS_BUTTON_X_BACK = 0
        self.FS_BUTTON_Y_BACK = self.SS_LEVEL_BUTTONS

        self.FS_BUTTON_X_ONE_DAY = 100
        self.FS_BUTTON_Y_ONE_DAY= self.SS_LEVEL_BUTTONS

        self.FS_BUTTON_X_7_DAY = 230
        self.FS_BUTTON_Y_7_DAY = self.SS_LEVEL_BUTTONS

        self.FS_BUTTON_X_HISTORY_TEMP_OUTSIDE = 360
        self.FS_BUTTON_Y_HISTORY_TEMP_OUTSIDE = 285
        self.FS_HISTORY_TEMP_OUTSIDE_SIZE = 13

        self.FS_BUTTON_X_HISTORY_CPU_TEMP = 70
        self.FS_BUTTON_Y_HISTORY_CPU_TEMP = 285
        self.FS_HISTORY_HISTORY_CPU_SIZE = 13

        #####################################
        self.factor_keyboard_x_axis=60
        self.LS_KEYBOARD_X=170+self.factor_keyboard_x_axis
        self.LS_KEYBOARD_Y=120
        self.LS_SIZE_BUTTONS=60
        self.LS_SIZE_FONT_BUTTONS=30

        self.LS_TABLE_ENTER_X = 170+self.factor_keyboard_x_axis
        self.LS_TABLE_ENTER_Y = 50
        self.LS_TABLE_ENTER_SIZE = 20



        self.LS_ENTER_FIELD_X = 330+self.factor_keyboard_x_axis
        self.LS_ENTER_FIELD_Y = 55
        self.LS_ENTER_FONT = 20

        self.LS_ENTER_BUTTON_X = 280+self.factor_keyboard_x_axis
        self.LS_ENTER_BUTTON_Y = 350

        self.LS_CLEAR_BUTTON_X = 470 + self.factor_keyboard_x_axis
        self.LS_CLEAR_BUTTON_Y = 50

        self.LS_WRONG_PASSWORD_X = 170 + self.factor_keyboard_x_axis
        self.LS_WRONG_PASSWORD_Y = 20
        self.LS_WRONG_PASSWORD_FONT = 12
        self.LS_WRONG_PASSWORD_COLOR = 'Red'
        self.LS_WRONG_PASSWORD_STRING=f"Wrong password! You have {self.MAX_ENTERS_PASSWORD-self.TRIES_ENTER_PASSWORD} more times."
        ####### strings ###############
        self.STRING_DEGREES = f" {self.DEGREE_SIGN}C"
        self.STRING_TABLE_TEMP_IN = "Temperature Inside :"
        self.STRING_TABLE_TEMP_OUT = "Temperature Outside :"
        self.STRING_TABLE_HUM_IN = "Humidity Inside:"
        self.STRING_TABLE_PRESS_IN = "Pressure Inside:"
        self.STRING_TABLE_PRESS_OUT = "Pressure Outside :"
        self.STRING_TABLE_CPU = "Temperature CPU :"
        self.STRING_BUTTON_HISTORY_TEMP = "History Temperature"
        self.STRING_BUTTON_HISTORY_TEMP_OUT = "History Outside"
        self.STRING_BUTTON_HISTORY_HUM = "History Humidity"
        self.STRING_BUTTON_HISTORY_PRESS = "History Pressure"
        self.STRING_BUTTON_HISTORY_CPU = "History CPU"
        self.STRING_BUTTON_HISTORY_ONE_DAY = "One day"
        self.STRING_BUTTON_HISTORY_7_DAYS = "7 days"
        self.STRING_NO_NAMEDAY =f"Денислав Петров"
        self.STRING_SHUTDOWN ="Bye-Bye"
        self.STRING_BUTTON_BACK ="BACK"
        ######  indexes  #######################
        self.INDEX_TEMP_INSIDE=1
        self.INDEX_HUM=2
        self.INDEX_PRESS_INSIDE=3
        self.INDEX_TIME=4
        self.INDEX_TEMP_OUTSIDE=5
        self.INDEX_STATUS_OUTSIDE=6
        self.INDEX_PRESS_OUTSIDE=7
        self.INDEX_CPU_TEMP=8
        self.INDEX_WRONG_PASSWORD_STRING=9
        self.INDEX_NAMEDAY=10
        self.INDEX_VIDEO_STATUS=11




        #############################
        #############################
        self.DICTIONARY_DE_to_BG={'Schneefall': 'Снеговалеж',
                                  'Leichter Schneefall': 'Лек снеговалеж',
                                  'Stark bewölkt': 'Силно заоблачено',
                                  'Teilweise bewölkt': 'Отчасти заоблачено',
                                  'Wolkig': 'Облачно',
                                  'Vielfach klar': 'Предимно ясно',
                                  'Klar': 'Ясно',
                                  'Sonnig': "Слънчево",
                                  'Eisnebel': 'Мъгла и лед',
                                  'Überwiegend sonnig': 'Предимно слънчево',
                                  'Teils sonnig': 'Отчасти слънчево',
                                  }



