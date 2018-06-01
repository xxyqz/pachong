import requests
import time
from lxml import etree
import urllib

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
#years = ['2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011','2010','2000','1990','1980','1970','1969']
years = ['2000']
# movie_types =[{'type': '古装'}, {'type': '武侠'}, {'type': '警匪'}, {'type': '军事'}, {'type': '神话'}, {'type': '科幻'}
#     , {'type': '悬疑'}, {'type': '历史'}, {'type': '儿童'}, {'type': '农村'}, {'type': '都市'}, {'type': '家庭'}
#     , {'type': '搞笑'}, {'type': '偶像'}, {'type': '言情'}, {'type': '时装'}, {'type': '优酷出品'}]
movie_types =[{'type': '都市'}, {'type': '言情'}, {'type': '时装'}]
countries=['中国','中国香港','中国台湾', '韩国', '日本', '美国', '英国', '泰国', '新加坡']
moneys = [{'type':'付费','para':'1'},{'type':'免费','para':'2'},{'type':'VIP','para':'3'}]

for year in years:
    for movie_type in movie_types:
        for country in countries:
            for money in moneys:

                amount = 0
                page = 1

                while True:

                    try:

                        url = "http://list.youku.com/category/show/c_97_g_"+urllib.parse.quote(movie_type['type'])+"_a_"+urllib.parse.quote(country)+"_r_"+year+"_u_1_pt_"+money['para']+"_d_1_p_"+str(page)+".html?spm=a2h1n.8251845.filterPanel.5!4~1~3!3~A"
                        response = requests.get(url, headers=headers)
                        html = response.text
                        content = etree.HTML(html)
                        movie_names = content.xpath("//div[@class='yk-pack pack-film']/ul[@class='info-list']/li[@class='title']/a")
                        amount += len(movie_names)
                        page += 1

                        if len(movie_names) < 30 or page > 30:
                            break

                        time.sleep(1)
                    except Exception:
                        print('Retry ' + year+' '+movie_type['type']+' ' +' page '+str(page))

                result = "{},{},{},{},{}".format(year, movie_type['type'],country+money['type'], url, str(amount))
                print(result)
                with open("list_youku_series.txt", 'a', encoding='utf-8') as f:
                    f.write(result + '\n')
