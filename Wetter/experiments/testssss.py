from collections import OrderedDict

import requests
from bs4 import BeautifulSoup as soup

cookies = {
    'PHPSESSID': '30a13e9fe318463819b122352e1ce5c0',
}

headers = {
    'authority': 'bg-patriarshia.bg',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=30a13e9fe318463819b122352e1ce5c0',
    'referer': 'https://bg-patriarshia.bg/calendar/2023-1',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
month=1
response = requests.get(f'https://bg-patriarshia.bg/calendar/2023-{month}', cookies=cookies, headers=headers)
#print(response.text)
html = soup(response.text, 'html.parser')
temp = html.select("body > div.blog-area.section-padding-100 > div > div > div.col-12.col-lg-8.page-content")

day='day'
info='info'
date_day_info={} # {date:{day:'P',info:'absved'}
for a in temp[0].select('tr'):
    res=list(a.select('td'))
    if len(res) == 3:
        date=res[0].text
        day_week=res[1].text
        info_for_day=res[2].text

        date_day_info[date]={}
        date_day_info[date][day]=day_week
        date_day_info[date][info]=info_for_day

print(date_day_info)
for k,v in date_day_info.items():
    print(v[info])



