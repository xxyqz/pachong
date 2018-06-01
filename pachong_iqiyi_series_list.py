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
movie_types =[{'type': '自制', 'para': '11992'}
    , {'type': '古装', 'para': '24'}
    , {'type': '言情', 'para': '20'}
    , {'type': '武侠', 'para': '23'}
    , {'type': '偶像', 'para': '30'}
    , {'type': '家庭', 'para': '1654'}
    , {'type': '青春', 'para': '1653'}
    , {'type': '都市', 'para': '24064'}
    , {'type': '喜剧', 'para': '135'}
    , {'type': '战争', 'para': '27916'}
    , {'type': '军旅', 'para': '1655'}
    , {'type': '谍战', 'para': '290'}
    , {'type': '悬疑', 'para': '32'}
    , {'type': '罪案', 'para': '149'}
    , {'type': '穿越', 'para': '148'}
    , {'type': '宫廷', 'para': '139'}
    , {'type': '历史', 'para': '21'}
    , {'type': '神话', 'para': '145'}
    , {'type': '科幻', 'para': '34'}
    , {'type': '年代', 'para': '27'}
    , {'type': '农村', 'para': '29'}
    , {'type': '商战', 'para': '140'}
    , {'type': '剧情', 'para': '24063'}
    , {'type': '奇幻', 'para': '27881'}
    , {'type': '网剧', 'para': '24065'}]
moneys = [{'type': '免费', 'para': '0'}, {'type': '付费', 'para': '2'}]


for year in years:

    for movie_type in movie_types:

        for money in moneys:
            amount = 0
            page = 1

            while True:

                try:
                    url = "http://list.iqiyi.com/www/2/-" + movie_type['para'] + "---------" + money['para'] + "-" + year + "--4-" + str(page) + "-1-iqiyi--.html"
                    response = requests.get(url, headers=headers)
                    html = response.text
                    content = etree.HTML(html)
                    movie_names = content.xpath("//p[@class='site-piclist_info_title ']/a/@title")
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
            with open("list_iqiyi_series.txt", 'a', encoding='utf-8') as f:
                f.write(result + '\n')
