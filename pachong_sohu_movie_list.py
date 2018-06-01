import requests
import time
from lxml import etree
import urllib

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
years = [{'year':'2018','para':'2018'}, {'year':'2017','para':'2017'}, {'year':'2016','para':'2016'}, {'year':'2015','para':'2015'}
    , {'year':'2014','para':'2014'}, {'year':'2013','para':'2013'}, {'year':'2012','para':'2012'}, {'year':'2011','para':'2011'}
    ,{'year':'2010','para':'2010'},{'year':'00年代','para':'11'},{'year':'90年代','para':'90'},{'year':'80年代','para':'80'},{'year':'更早','para':'1'}]

# movie_types =[{'type':'爱情片','para':'100'},{'type':'战争片','para':'101'},{'type':'喜剧片','para':'102'},{'type':'科幻片','para':'103'}
# ,{'type':'恐怖片','para':'104'},{'type':'动画片','para':'105'},{'type':'动作片','para':'106'},{'type':'风月片','para':'107'}
# ,{'type':'剧情片','para':'108'},{'type':'歌舞片','para':'108'},{'type':'纪录片','para':'110'},{'type':'魔幻片','para':'111'}
# ,{'type':'灾难片','para':'112'},{'type':'悬疑片','para':'113'},{'type':'传记片','para':'114'},{'type':'警匪片','para':'116'}
# ,{'type':'伦理片','para':'117'},{'type':'惊悚片','para':'118'},{'type':'谍战片','para':'119'},{'type':'历史片','para':'120'}
# ,{'type':'武侠片','para':'121'},{'type':'青春片','para':'122'},{'type':'文艺片','para':'123'},{'type':'犯罪片','para':'139'}
# ,{'type':'艺术片','para':'140'},{'type':'推理片','para':'141'},{'type':'侦探片','para':'142'},{'type':'间谍片','para':'143'}
# ,{'type':'戏曲片','para':'144'},{'type':'音乐片','para':'145'},{'type':'古装片','para':'146'},{'type':'探索片','para':'147'}
# ,{'type':'微电影','para':'135'}]
# countries=[{'country':'内地','para':'00'},{'country':'香港','para':'01'}
#     ,{'country':'台湾','para':'02'},{'country':'美国','para':'03'}
#     ,{'country':'日本','para':'04'},{'country':'韩国','para':'15'}
#     , {'country': '英国', 'para': '07'},{'country':'法国','para':'08'}
#     , {'country': '德国', 'para': '09'}, {'country': '意大利', 'para': '10'}
#     , {'country': '西班牙', 'para': '11'}, {'country': '俄罗斯', 'para': '12'}
#     , {'country': '加拿大', 'para': '13'}, {'country': '印度', 'para': '05'}
#     , {'country': '泰国', 'para': '06'}, {'country': '其他', 'para': '14'}]

for year in years:
    # for movie_type in movie_types:
    #     for country in countries:

            amount = 0
            page = 1

            while True:

                try:
                    url="https://so.tv.sohu.com/list_p11_p2_p3_p4"+year['para']+"_p5_p6_p73_p82_p91_p10"+str(page)+"_p11_p12_p130.html"
                    response = requests.get(url, headers=headers)
                    html = response.text
                    content = etree.HTML(html)
                    movie_names = content.xpath("/html/body/div[@class='wrap']/div[@class='sort-column area']/div[@class='column-bd cfix']/ul[@class='st-list cfix']//strong/a")
                    amount += len(movie_names)
                    page += 1

                    if len(movie_names) < 30 or page > 30:
                        break

                    time.sleep(1)
                except Exception:
                    print('Retry ' + year['year']+' '+'全部类型 全部国家' +' page '+str(page))

            result = "{},{},{},{},{}".format(year['year'], '全部类型','全部国家', url, str(amount))
            print(result)
            with open("list_sohu_movie.txt", 'a', encoding='utf-8') as f:
                f.write(result + '\n')
