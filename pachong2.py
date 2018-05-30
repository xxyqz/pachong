import json
import requests
from requests.exceptions import RequestException
import re
import time
import random
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

for i in range(10):
    url = 'http://maoyan.com/board/4?offset=' + str(i)
    response = requests.get(url, headers=headers)
    time.sleep(1 + random.random())
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    for dd in soup.find_all(name='dd'):
        row = []
        for p in dd.find_all(name="p"):
            if p.string is not None:
                row.append(p.string.strip())

        with open('result2.txt', 'a', encoding='utf-8') as f:
            f.write(str(row) + '\n')
