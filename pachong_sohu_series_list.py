import requests
import time
from lxml import etree
import urllib

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
years = [{'year':'2018','para':'2018'}, {'year':'2017','para':'2017'}, {'year':'2016','para':'2016'}, {'year':'2015','para':'2015'}
    , {'year':'2014','para':'2014'}, {'year':'2013','para':'2013'}, {'year':'2012','para':'2012'}, {'year':'2011','para':'2011'}
    ,{'year':'2010','para':'2010'},{'year':'00年代','para':'11'},{'year':'90年代','para':'90'},{'year':'80年代','para':'80'},{'year':'更早','para':'1'}]

movie_types =[{'type':'偶像剧','para':'100'}
    ,{'type':'家庭剧','para':'101'}
    ,{'type':'历史剧','para':'102'}
    ,{'type':'年代剧','para':'103'}
    , {'type': '言情剧', 'para': '104'}
    , {'type': '武侠剧', 'para': '105'}
    , {'type': '古装剧', 'para': '106'}
    , {'type': '都市剧', 'para': '107'}
    , {'type':'农村剧','para':'108'}
    , {'type': '军旅剧', 'para': '109'}
    , {'type': '刑侦剧', 'para': '110'}
    , {'type': '喜剧', 'para': '100'}
    , {'type': '悬疑剧', 'para': '100'}
    , {'type': '情景剧', 'para': '100'}
    , {'type': '传记剧', 'para': '100'}
    , {'type': '科幻剧', 'para': '100'}
    , {'type': '动画片', 'para': '100'}
    , {'type': '动作剧', 'para': '100'}
    , {'type': '真人秀', 'para': '100'}
    , {'type': '栏目剧', 'para': '100'}
    , {'type': '谍战剧', 'para': '100'}
    , {'type': '伦理剧', 'para': '100'}
    , {'type': '战争剧', 'para': '100'}
    , {'type': '神话剧', 'para': '100'}
    , {'type': '惊悚剧', 'para': '100'}
    , {'type': '剧情片', 'para': '100'}
    , {'type': '商战剧', 'para': '100'}
    , {'type': '警匪剧', 'para': '100'}
    , {'type': '玄幻剧', 'para': '100'}]
countries=[{'country':'内地','para':'00'},{'country':'香港','para':'01'}
    ,{'country':'台湾','para':'02'},{'country':'美国','para':'03'}
    ,{'country':'日本','para':'04'},{'country':'韩国','para':'15'}
    , {'country': '英国', 'para': '07'}, {'country': '泰国', 'para': '06'}, {'country': '其他', 'para': '14'}]

for year in years:
    for movie_type in movie_types:
        for country in countries:

            amount = 0
            page = 1

            while True:

                try:
                    url="https://so.tv.sohu.com/list_p1101_p2101"+movie_type['para']+"_p310"+country['para']+"_p4"+year['para']+"_p5_p6_p73_p82_p91_p10"+str(page)+"_p11_p12_p130.html"
                    response = requests.get(url, headers=headers)
                    html = response.text
                    content = etree.HTML(html)
                    movie_names = content.xpath("/html/body/div[@class='wrap']/div[@class='sort-column area']/div[@class='column-bd cfix']/ul[@class='st-list cfix']//strong/a/text()")
                    amount += len(movie_names)
                    page += 1

                    if len(movie_names) < 30 or page > 30:
                        break

                    time.sleep(1)
                except Exception:
                    print('Retry ' + year['year']+' '+movie_type['type']+' '+country['country'] +' page '+str(page))

            result = "{},{},{},{},{}".format(year['year'], movie_type['type'],country['country'], url, str(amount))
            print(result)
            with open("list_sohu_series.txt", 'a', encoding='utf-8') as f:
                f.write(result + '\n')
