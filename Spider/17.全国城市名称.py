import requests
from lxml import etree
import pymongo
import csv


def spider(url,heards):
    '''爬取中国全部城市名称'''
    #解析网页
    page_text = requests.get(url=url,headers=heards).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li')  # xpath提取元素

    city_list = []
    city_dict_list = []
    i = 1
    for li in li_list:
        city_dict = {}
        city_name = li.xpath('./a/text()')[0]
        city_list.append(city_name)
        city_dict['第{}个城市'.format(str(i))] = city_name
        city_dict_list.append(city_dict)
        i = i + 1

    return city_list,city_dict_list,len(city_list)


def txtSave(city_list):
    '''存储为txt格式文件'''
    fp = open('全国城市名称.txt', 'w', encoding='utf-8')
    i = 1
    for city in city_list:
        fp.write(str(i) + ":" + str(city) + '\n')
        i = i + 1


def csvSave(city_list):
    '''存储为csv表格文件'''
    with open('全国城市名称.csv','w',errors='') as fp:
        writer = csv.writer(fp)
        writer.writerows(city_list)



def mongoSave(city_dict_list):
    '''存储在mongodb数据库中'''
    client = pymongo.MongoClient(host='localhost', port=27017)
    collection = client['China']['City']
    collection.insert_many(city_dict_list)


if __name__ == "__main__":
    # api网址
    url = 'https://www.aqistudy.cn/historydata/'
    # 伪装头
    heards = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64)'
    }
    print("运行爬虫:")
    city_list,city_dict_list,length = spider(url,heards)
    print("存储为txt文件:")
    txtSave(city_list)
    print("存储为csv文件:")
    csvSave(city_list)
    print("存储在数据库中:")
    mongoSave(city_dict_list)
    print("全部存储完毕")
    print("全国城市数量为:{}".format(length))

