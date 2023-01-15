import copy

import requests
from bs4 import BeautifulSoup as soup
import re
#
# headers = {
#     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#     'Referer': 'https://www.accuweather.com/',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# response = requests.get('https://www.accuweather.com/de/ch/bern/312122/current-weather/312122', headers=headers)
#
#
# html=soup(response.text,'html.parser')
# temp=html.select('body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.card-content > div.current-weather > div.current-weather-info > div > div')
# #print(temp[0]) # body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.card-content > div.current-weather > div.current-weather-info > div > div
#
# pattern=r"(?P<temp>([0-9]+))"
#
# found=re.finditer(pattern,str(temp[0]))
# current_temperature=0
# for each in found:
#     current_temperature=each.group('temp')
#
# print(current_temperature)
from database_function import TIME_DATE
from sqlite_db__function import SQLiteSensor


class Outside:
    def __init__(self):
        self.headers = {
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'Referer': 'https://www.accuweather.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}
        self.current_temperature=0
        self.pattern=r"(?P<temp>([0-9]+))"
        self.current_temperature=0
        self.last_temperature=0
        self.time_=TIME_DATE()
        self.hours=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        self.first_run = 0
        self.current_status="no info"
        self.current_pressure_outside=0
        self.searched_units_pressure='0'
        self.db=SQLiteSensor()
        self.mm_old=''

    def acctual_temperature_outside(self):
        """
        with curl get the page from the wetter, only if 1:00 or 1:30 or 22:00 or 22:30 etc in half hour
        then parse to html
        with regex get the value


        :return: the temperatue in C, status, luftdruck in hPa
        """
        mm=self.time_.TIME()[1]

        if  mm== "00" or mm== "15" or mm == "30" or mm == "45": # 1:00, 2:00 etc
            self.first_run=1
            try:
                response = requests.get('https://www.accuweather.com/de/ch/bern/312122/current-weather/312122', headers=self.headers)
                html = soup(response.text, 'html.parser')
                temp = html.select('body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.card-content > div.current-weather > div.current-weather-info > div > div')
                status_wetter = html.select('body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.card-content > div.current-weather > div.phrase')
                #presure_outside=html.select("body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.current-weather-details.no-realfeel-phrase.odd > div:nth-child(8)")
                self.current_status=status_wetter[0].text
                self.current_temperature = temp[0].text.split("C")[0]
                #print('start')
                for child in range(5,13):
                    if self.searched_units_pressure.isdigit() and 900 <= int(self.searched_units_pressure) <= 1100:
                        self.current_pressure_outside=self.searched_units_pressure
                        break
                    presure_outside = html.select(
                        f"body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.current-weather-details.no-realfeel-phrase.odd > div:nth-child({child})")
                    self.searched_units_pressure = presure_outside[0].text.split(" ")[1]

                self.last_temperature=self.current_temperature
            except:
                self.last_temperature = self.current_temperature
                return self.last_temperature,self.current_status,self.current_pressure_outside
            #self.last_temperature = self.current_temperature
            return self.last_temperature,self.current_status,self.current_pressure_outside
        if mm != self.mm_old:
            self.db.add_to_table_outside(self.time_.date(),str(self.current_temperature))
            self.mm_old = mm
        return self.current_temperature ,self.current_status,self.current_pressure_outside


if __name__ == "__main__":
    pass
    # k=Outside()
    # print(k.acctual_temperature_outside())