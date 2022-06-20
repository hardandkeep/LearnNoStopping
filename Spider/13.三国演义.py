import requests
from bs4 import BeautifulSoup
import re
import os

#这里是用正则实现了三国演义小说的爬取

heards = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
if not os.path.exists('./三国演艺/'):
    os.mkdir('./三国演艺/')
for i in range(1,121):
    url = 'http://mathfunc.com/book/sanguoyanyi/'+str(i)+'.html'
    res = requests.get(url=url,headers=heards).text
    sanguoyanyi_text = re.findall('<p>(.*?)</p>',res,re.S)
    text_page = './三国演艺/'+str(i)+'.三国演艺'
    for passage in sanguoyanyi_text:
        fp = open(text_page,'w',encoding='utf_8')
        fp.write(passage)


#这边用bs4来解析这个web、










