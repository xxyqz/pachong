import requests
import time
from lxml import etree
import urllib

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
#years = ['2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011','2010','2000','1990','1980','1970','1969']
years = ['2000','1990']
# movie_types =[{'type': '武侠'}, {'type': '警匪'}, {'type': '犯罪'}, {'type': '科幻'}, {'type': '战争'}, {'type': '恐怖'}
#     , {'type': '惊悚'}, {'type': '恐怖'}, {'type': '纪录片'}, {'type': '西部'}, {'type': '戏曲'}, {'type': '歌舞'}
#     , {'type': '奇幻'}, {'type': '冒险'}, {'type': '悬疑'}, {'type': '历史'}, {'type': '动作'}, {'type': '传记'}
#     , {'type': '动画'}, {'type': '儿童'}, {'type': '喜剧'}, {'type': '爱情'}, {'type': '剧情'}, {'type': '运动'}
#     , {'type': '短片'}, {'type': '优酷出品'}]
movie_types=[{'type': '动作'},{'type': '爱情'},{'type': '剧情'}]
#moneys=[{'type':'全部','para':'0'}]
moneys = [{'type':'付费','para':'1'},{'type':'免费','para':'2'},{'type':'VIP','para':'3'}]
countries=['中国','中国香港','中国台湾', '韩国', '日本', '美国', '法国', '英国', '德国', '意大利', '加拿大', '印度', '俄罗斯', '泰国', '其他']

for year in years:
    for movie_type in movie_types:
        for country in countries:

            amount = 0
            page = 1

            while True:

                try:

                    url = "http://list.youku.com/category/show/c_96_g_"+urllib.parse.quote(movie_type['type'])+"_a_"+urllib.parse.quote(country)+"_r_"+year+"_u_1_s_1_d_1_p_"+str(page)+".html?spm=a2h1n.8251845.0.0"
                    response = requests.get(url, headers=headers)
                    html = response.text
                    content = etree.HTML(html)
                    movie_names = content.xpath("//li[@class='title']/a/text()")
                    amount += len(movie_names)
                    page += 1

                    if len(movie_names) < 30 or page > 30:
                        break

                    time.sleep(1)
                except Exception:
                    print('Retry ' + year+' '+movie_type['type']+' ' +' page '+str(page))

            result = "{},{},{},{},{}".format(year, movie_type['type'],country, url, str(amount))
            print(result)
            with open("list_youku_movie.txt", 'a', encoding='utf-8') as f:
                f.write(result + '\n')
