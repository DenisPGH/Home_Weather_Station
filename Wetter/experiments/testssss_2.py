import requests
from bs4 import BeautifulSoup as soup
headers = {
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

params = {
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

response = requests.post('https://bgcal.com/%D0%BF%D1%80%D0%B0%D0%B7%D0%BD%D0%B8%D1%86%D0%B8/2023', params=params, headers=headers)
html = soup(response.text, 'html.parser')


werbung=[6,9]


day='day'
holi='holi'
date_day_info={} # {date: [{day:'P', holi:'absved'} , {}] , }
counter=0
for a in range(5,19):
    if a not in werbung:
        info = html.select(f'body > div.container > div:nth-child({a})> div > div > div.list-group > div')
        date_day_info[counter] = []
        for b in info:
            month=b.select('h4')[0].text.split(':')[0].split(" ")[1].strip()
            holiday=b.select('h4')[0].text.split(':')[1].strip().split('-')[0]
            date=b.select('h4')[0].text.split(':')[0].split(" ")[0].strip()
            current_day_fest={}
            current_day_fest[day]=date
            current_day_fest[holi]=holiday
            date_day_info[counter].append(current_day_fest)


print(date_day_info)



