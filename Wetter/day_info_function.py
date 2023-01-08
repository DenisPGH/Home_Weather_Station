import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
from database_function import TIME_DATE


class Ortodox:
    def __init__(self):
        self.headers = {
    'authority': 'www.google-analytics.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'content-length': '0',
    'content-type': 'text/plain',
    'origin': 'https://bgcal.com',
    'referer': 'https://bgcal.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
        self.params={
    'v': '1',
    '_v': 'j98',
    'a': '527144005',
    't': 'pageview',
    '_s': '1',
    'dl': 'https://bgcal.com/%D0%BF%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B8/2023',
    'ul': 'en-us',
    'de': 'UTF-8',
    'dt': 'Празници през 2023 година | BGCAL - почивни дни, празници, именни дни, официални празници',
    'sd': '24-bit',
    'sr': '1280x720',
    'vp': '567x609',
    'je': '0',
    '_u': 'AACAAEABAAAAACAAI~',
    'jid': '',
    'gjid': '',
    'cid': '706217715.1673171320',
    'tid': 'UA-60785317-1',
    '_gid': '658702250.1673171320',
    '_slc': '1',
    'z': '598198186',
}
        self.date=TIME_DATE()
        self.today="Fest"
        self.werbung=[6,9]
        self.day = 'day'
        self.holi = 'holi'
        self.date_day_info = {}  # {date: [{day:'P', holi:'absved'} , {}] , }
        self.counter = 0
        self.LINK_CSV_HOLIDAYS= 'holdays_2023.csv'
        self.colums=['month','date','inforamtion']


    def current_day_ortodox(self):
        """
        :return: string with the information for current day
        """
        month=int(self.date.DATE().split("-")[1])
        day = int(self.date.DATE().split("-")[2])

        data= pd.read_csv(self.LINK_CSV_HOLIDAYS,sep='|',names=self.colums,header=None)
        result=data.loc[(data['month'] == month) & (data['date'] == day)]['inforamtion'].values.tolist()
        if result:
            return result[0]
        else:
            return ''

    def create_csv_file__holidays(self):
        """
        create csv file with the month| day | information
        :return:
        """
        try:
            response = requests.post('https://bgcal.com/%D0%BF%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B8/2023', params=self.params, headers=self.headers)
            html = soup(response.text, 'html.parser')
            with open(f'{self.LINK_CSV_HOLIDAYS}', mode='w', encoding='utf-8', newline='') as csv_write:
                for a in range(5, 19):
                    if a not in self.werbung:
                        self.counter+=1
                        info = html.select(f'body > div.container > div:nth-child({a})> div > div > div.list-group > div')
                        self.date_day_info[self.counter] = []
                        for b in info:
                            holiday = b.select('h4')[0].text.split(':')[1].strip().split('-')[0]
                            date = b.select('h4')[0].text.split(':')[0].split(" ")[0].strip()
                            file = csv.writer(csv_write, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            file.writerow([self.counter, date, holiday])



        except:
            pass




# if __name__ == "__main__":
#
#     k=Ortodox()
#     #print(k.create_csv_file__holidays())
#     print(k.current_day_ortodox())