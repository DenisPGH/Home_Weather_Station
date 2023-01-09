import os

###############################################
#PATH_HOLIDAYS= '/home/raspi/Desktop/watch/Home_Weather_Station/Wetter/holdays_2023.csv'
# PATH_HOLIDAYS = 'holdays_2023.csv'
# PATH_DB = 'wetter_DB_1.csv'
# self.__path_DB='/home/raspi/Desktop/watch/Home_Weather_Station/Wetter/wetter_DB.csv'

PATH_HOLIDAYS= 'holdays_2023.csv' if os.getlogin()=='Owner' else '/home/raspi/Desktop/watch/Home_Weather_Station/Wetter/holdays_2023.csv'
PATH_DB ='wetter_DB_1.csv' if os.getlogin()=='Owner' else '/home/raspi/Desktop/watch/Home_Weather_Station/Wetter/wetter_DB.csv'

print(os.getlogin())