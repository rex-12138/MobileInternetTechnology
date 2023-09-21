import ssl
from lxml import etree
import requests
import re

ssl._create_default_https_context = ssl._create_unverified_context
from urllib import request
url = 'https://www.ucas.ac.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
req = request.Request(url=url, headers=headers, method='GET')
response = request.urlopen(req)
html = response.read().decode('utf-8')
tree = etree.HTML(html)
rows = tree.xpath('/html/body/header[@class="header"]/div[@class="full_menu"]/nav[@class="nav full_nav"]/ul/li')[1:]
for row in rows:
    print(row.xpath('./a/text()')[0])
    lines = row.xpath('./div[@class="subNav2"]/dl[@class="subNavList2"]/dd')
    for line in lines:

        print("  ",line.xpath('./a/text()')[0])
