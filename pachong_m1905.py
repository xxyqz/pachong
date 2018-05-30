import json
import requests
from requests.exceptions import RequestException
import re
import time
import random
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

year = 2018

while True:
    if year < 2011:
        break
    page = 1
    while True:
        url="http://www.1905.com/mdb/film/list/country-China/year-"+str(year)+"/o0d0p"+str(page)+".html"
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:

                html = response.text
                content = etree.HTML(html)

                movie_names = content.xpath("//ul[@class='inqList pt18']//div[@class='text']/p[1]/a/text()")
                star_nodes = content.xpath("//ul[@class='inqList pt18']//div")
                stars = list()
                for star_node in star_nodes:
                    stars.append("/".join(star_node.xpath(".//p[@class='zy'][1]/a/text()")))

                if len(movie_names) == 0:
                    break

                for i in range(len(movie_names)):
                    row = "{},{},{}".format(str(year), movie_names[i], stars[i])
                    print(row)
                    with open("result_m1905.txt", 'a', encoding='utf-8') as f:
                        f.write(str(row) + '\n')

                page += 1
                time.sleep(1)

            else:
                print(response)

        except RequestException:
            print(RequestException)

    year -= 1
