import csv
import time
import datetime

class HELPER():
    def __init__(self):
        self.__path_DB='/home/raspi/Desktop/watch/Home_Weather_Station/Wetter/wetter_DB.csv'
    def return_DB(self):
        return self.__path_DB

class TIME_DATE():
    def __init__(self):
        pass
    def DATE(self):
        date_ = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
        return date_
    def TIME(self):
        hh = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[0]
        mm = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[1]
        ss = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[2]
        return [hh,mm,ss]



class DataBaseWetter:
    def __init__(self):
        self.path_store_wetter= 'Wetter'
        self.name_DB= HELPER().return_DB()
        self.name_DB='/home/raspi/Desktop/watch/Home_Weather_Station/Wetter/wetter_DB.csv'
        #self.date=TIME_DATE()

    def store_new_info(self,values:list,date,hh,mm):
        """

        :param values: array [temp,humm,pressure]
        :param time_: actual time
        :return: nothing
        """
        temp=values[0]
        humm=values[1]
        pressure=values[2]
        with open(f'{self.name_DB}', mode='a', newline='') as csv_write:  # w,a
            file = csv.writer(csv_write, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # [2023-01-01,HH,MM,Temperature,Humidity,Pressure]
            #file.writerow([self.date.DATE(),self.date.TIME()[0],self.date.TIME()[1],temp,humm,pressure])
            file.writerow([date,hh,mm,temp,humm,pressure])


    def return_info_db(self):
        """

        :return: values from the DB with the values of temp, humm, pressure
        """
        with open(f'{self.name_DB}', mode='r', newline='') as csv_read:  # w,a
            print(csv_read.readlines())






