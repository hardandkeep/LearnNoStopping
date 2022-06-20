import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
}

response = requests.get("https://www.imooc.com/course/list?page=1",headers=headers).text

tree = etree.HTML(response)

content = tree.xpath('//*[@id="main"]/div[3]/div[1]/a[1]/p[1]/text()')[0]

print(content)

#等有充分时间的时候，函数式编程爬取全站