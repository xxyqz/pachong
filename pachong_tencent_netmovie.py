import json
import requests
from requests.exceptions import RequestException
import re
import time
import random
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

years = [{"year":'2018','para':'4330'},{'year':'2017','para':'4331'},{'year':'2016','para':'4332'},{'year':'2015','para':'4333'},{'year':'2014-2010','para':'4334'}]

for year in years:
    page = 1
    while True:
        url = "http://v.qq.com/x/list/movie?iyear="+year['para']+"&format=2&offset="+str((page-1)*30)
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:

                html = response.text
                content = etree.HTML(html)

                movie_names = content.xpath("//strong[@class='figure_title']/a/text()")
                stars = content.xpath("//div[@class='figure_desc']/a[1]/text()")

                if len(movie_names) == 0:
                    break

                for i in range(len(movie_names)):
                    row = "{},{},{}".format(year['year'], movie_names[i], stars[i])
                    print(row)
                    with open("result_tencent_netmovie.txt", 'a', encoding='utf-8') as f:
                        f.write(str(row) + '\n')

                page += 1
                time.sleep(1)

            else:
                print(response)

        except RequestException:
            print(RequestException)


