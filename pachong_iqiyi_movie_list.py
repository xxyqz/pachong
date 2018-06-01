import json
import requests
from requests.exceptions import RequestException
import re
import time
import random
from lxml import etree
import os


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
years = ['2018', '2017', '2016', '2011_2015', '2000_2010', '1990_1999', '1980_1989', '1964_1979']
movie_types =[{'type': '喜剧', 'para': '8'}
    , {'type': '悲剧', 'para': '13'}
    , {'type': '爱情', 'para': '6'}
    , {'type': '动作', 'para': '11'}
    , {'type': '枪战', 'para': '131'}
    , {'type': '犯罪', 'para': '291'}
    , {'type': '惊悚', 'para': '128'}
    , {'type': '恐怖', 'para': '10'}
    , {'type': '悬疑', 'para': '289'}
    , {'type': '动画', 'para': '12'}
    , {'type': '家庭', 'para': '27356'}
    , {'type': '奇幻', 'para': '1284'}
    , {'type': '魔幻', 'para': '129'}
    , {'type': '科幻', 'para': '9'}
    , {'type': '战争', 'para': '7'}
    , {'type': '青春', 'para': '130'}]
moneys = [{'type': '免费', 'para': '0'}, {'type': '付费', 'para': '2'}]

for year in years:

    for movie_type in movie_types:

        for money in moneys:
            amount = 0
            page = 1

            while True:

                try:
                    url = "http://list.iqiyi.com/www/1/-" + movie_type['para'] + "---------" + money['para'] + "-" + year + "--4-" + str(page) + "-1-iqiyi--.html"
                    response = requests.get(url, headers=headers)
                    html = response.text
                    content = etree.HTML(html)
                    movie_names = content.xpath("//p[@class='site-piclist_info_title  movie-tit ']/a/@title")
                    # movie_names = content.xpath("//p[@class='site-piclist_info_title movie-tit']/a/text()")
                    amount += len(movie_names)
                    page += 1

                    if len(movie_names) < 30 or page > 30:
                        break

                    time.sleep(1)
                except Exception:
                    print('Retry ' + year+' '+movie_type['type']+' ' + money['type']+' page '+str(page))

            result = "{},{},{},{},{}".format(year, movie_type['type'], money['type'], url, str(amount))
            print(result)
            with open("list_iqiyi_movie.txt", 'a', encoding='utf-8') as f:
                f.write(result + '\n')
