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
        self.hour=TIME_DATE()
        self.hours=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        self.first_run = 0

    def acctual_temperature_outside(self):
        """
        with curl get the page from the wetter, only if 1:00 or 1:30 or 22:00 or 22:30 etc in half hour
        then parse to html
        with regex get the value


        :return: the temperatue in C
        """

        if self.hour.TIME()[1] ==00 or self.hour.TIME()[1]==30 or self.first_run==0: # 1:00, 2:00 etc
            self.first_run=1

            try:
                response = requests.get('https://www.accuweather.com/de/ch/bern/312122/current-weather/312122', headers=self.headers)
                html = soup(response.text, 'html.parser')
                temp = html.select('body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.card-content > div.current-weather > div.current-weather-info > div > div')
                found = re.finditer(self.pattern, str(temp[0]))
                for each in found:
                    self.current_temperature = each.group('temp')
                    self.last_temperature=self.current_temperature
            except:
                self.last_temperature = self.current_temperature
                return self.last_temperature
        else:
            #self.last_temperature = self.current_temperature
            return self.last_temperature

        return self.current_temperature


# if __name__ == "__main__":
#     pass
    # k=Outside()
    # print(k.acctual_temperature_outside())