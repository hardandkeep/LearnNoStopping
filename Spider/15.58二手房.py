'''
import requests
from lxml import etree
#/html/body/div/div/div/section/section[3]/section[1]/div

url = 'https://www.58.com/ershoufang/'

heards = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
}

page_text = requests.get(url=url,headers=heards).text

tree = etree.HTML(page_text)

tr_list = tree.xpath('/html/body/div[7]/div[1]/table/tbody/tr')

for tr in tr_list:
    detail_room = tr.xpath('./td[2]/a/@herf|./td[2]/a/br')
    value_room = tr.xpath('./td[3]/b)
    size_room = tr.xpath('./td[4]/tr')
'''
