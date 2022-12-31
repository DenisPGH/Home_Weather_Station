import csv
import time
import datetime
class DataBaseWetter:
    def __init__(self):
        self.time_= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.path_store_wetter= 'Wetter'
        self.name_DB= 'wetter_DB'
    def store_new_info(self,values:list,time_):
        """

        :param values: array [temp,humm,pressure]
        :param time_: actual time
        :return: nothing
        """
        temp=values[0]
        humm=values[1]
        pressure=values[2]
        with open(f'{self.name_DB}.csv', mode='w', newline='') as csv_write:  # w,a
            file = csv.writer(csv_write, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file.writerow([time_,temp,humm,pressure])


    def return_info_db(self):
        """

        :return: values from the DB with the values of temp, humm, pressure
        """
        with open(f'{self.name_DB}.csv', mode='r', newline='') as csv_read:  # w,a
            print(csv_read.readlines())






