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

    def acctual_temperature_outside(self):
        """
        with curl get the page from the wetter
        then parse to html
        with regex get the value


        :return: the temperatue in C
        """
        try:
            response = requests.get('https://www.accuweather.com/de/ch/bern/312122/current-weather/312122', headers=self.headers)
            html = soup(response.text, 'html.parser')
            temp = html.select('body > div > div.two-column-page-content > div.page-column-1 > div.page-content.content-module > div.current-weather-card.card-module.content-module > div.card-content > div.current-weather > div.current-weather-info > div > div')
            found = re.finditer(self.pattern, str(temp[0]))
            for each in found:
                self.current_temperature = each.group('temp')
        except:
            return self.current_temperature

        return self.current_temperature


if __name__ == "__main__":
    pass
    # k=Outside()
    # print(k.acctual_temperature_outside())