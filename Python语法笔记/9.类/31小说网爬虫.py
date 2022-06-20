import requests
import re
import os
from threading import Thread


#通用爬虫--类来实现
class Spider(object):

    heards ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    def __init__(self,name,url,):
        '''爬虫的属性'''
        self.name = name
        self.url = url


    def attain_urls(self,content_url):
        '''爬虫的方法'''
        req = requests.get(url=content_url, headers=self.heards)
        res = req.text

        title_list = re.findall('<dd><a href=".*?">(.*?)</a></dd>', res, re.S)
        list_urls = re.findall("(\/\d+\/\d+\/\d+\.html)", res, re.S)

        print(title_list,list_urls)

        return title_list,list_urls


    def parse_data(self,url,File_path,title):
        '''解析数据'''
        pre_req = requests.get(url=url, headers=self.heards)
        pre_res = pre_req.text

        story = re.findall('<p>(.*?)</p>', pre_res, re.S)
        print(story)
        # 持久性存储
        filePath = File_path + "." + title + '.text'

        with open(filePath, 'w', encoding='utf-8') as fp:
            fp.write(story)


    def save_data(self):
        '''保存数据'''
        name = input("请输入小说名字:")
        content_url = input("请输入小说目录页面url:")

        File_path = './' + name + '/'
        if not os.path.exists(File_path):
            os.mkdir(File_path)

        title_list,list_urls = self.attain_urls(content_url)

        count = 0
        for url in list_urls:
            title = "try"

            url = self.url + content_url

            #self.parse_data(url,File_path,title)
            self.theading(url,File_path,title)

            count = count + 1


    def theading(self,url,File_path,title):
        '''多线程'''
        thead = Thread(target=self.parse_data,args=(url,File_path,title,))
        thead.setDaemon(True)
        thead.start()


if __name__ == "__main__":
    spider = Spider(name="31小说网爬虫",url="http://www.31xiaoshuo.com")
    spider.save_data()