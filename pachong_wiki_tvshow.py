import json
import requests
from requests.exceptions import RequestException
import re
import time
import random
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
years=[2018,2017,2016,2015,2014,2013,2012,2011]

for year in years:

    url = "https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%E7%94%B5%E8%A7%86%E5%89%A7%E5%88%97%E8%A1%A8_%28"+str(year)+"%E5%B9%B4%29"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:

            html = response.text
            content = etree.HTML(html)
            selector = etree.HTML(html)

            if year >= 2013:

                tv_show_names = content.xpath("//table[@class='wikitable'][1]//td[1]")+content.xpath("//table[@class='wikitable'][3]//td[1]")
                net_tv_show_names = selector.xpath("//table[@class='wikitable'][2]//td[1]")

                for tv_show_name in tv_show_names:
                    row_tv_show = "{},{},{}".format(str(year), 'tv_show', tv_show_name.xpath('string(.)'))
                    print(row_tv_show)
                    with open("result_wiki_tv_shows.txt", 'a', encoding='utf-8') as f:
                        f.write(str(row_tv_show) + '\n')

                for net_tv_show_name in net_tv_show_names:
                    row_net_tv_show = "{},{},{}".format(str(year),'net_tv_show', net_tv_show_name.xpath('string(.)'))
                    print(row_net_tv_show)
                    with open("result_wiki_tv_shows.txt", 'a', encoding='utf-8') as f:
                        f.write(str(row_net_tv_show) + '\n')
            else:
                tv_show_names = content.xpath("//table[@class='wikitable'][1]//td[1]")+content.xpath("//table[@class='wikitable'][2]//td[1]")

                for tv_show_name in tv_show_names:
                    row_tv_show = "{},{},{}".format(str(year), 'tv_show', tv_show_name.xpath('string(.)'))
                    print(row_tv_show)
                    with open("result_wiki_tv_shows.txt", 'a', encoding='utf-8') as f:
                        f.write(str(row_tv_show) + '\n')

            time.sleep(1)

        else:
            print(response)

    except RequestException:
        print(RequestException)

