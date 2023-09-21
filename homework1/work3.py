import requests
from bs4 import BeautifulSoup
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
}
for page in range(1, 7):
    r = requests.get(f'http://cpc.people.com.cn/GB/87228/index{page}.html', headers=headers);
    r.encoding = 'gb2312';
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find("div", class_ = "p2j_con02 clearfix g-w1200")
    items = title.find_all('li')
    for item in items:
        a_tag = item.find('a')
        print(item.get_text())
        print(a_tag['href'])
        print('------------------------')




