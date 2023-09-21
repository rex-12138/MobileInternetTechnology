
import ssl

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
title = re.findall('<div class="title fs18">(.*?)</div>', html)
address = re.findall('<p>地址：(.*?)</p>',html)
postcode = re.findall('<p>邮编：(.*?)</p>',html)
tele = re.findall('<p>电话：(.*?)</p>',html)
for i in range(len(title)):
    print('校区名称：',title[i])
    print('地址：',address[i])
    print('邮编：',postcode[i])
    print('电话：',tele[i])
    print('------------------------')


# <div class="title fs18">雁栖湖校区</div>
#<p>地址：北京市怀柔区雁栖湖东路1号</p>
#<p>邮编：101408</p>
#p>电话：010-69671108</p>

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
