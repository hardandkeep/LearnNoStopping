import requests
from lxml import etree
import os

file_path = './学习资料/'
if not os.path.exists(file_path):
    os.mkdir(file_path)
heards = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

for i in range(1,175):
    url = 'https://pic.netbian.com/4kmeinv/index_'+str(i)+'.html'

    #返回页面数据
    page_text = requests.get(url=url,headers=heards).text

    #创建一个xpath对象
    tree = etree.HTML(page_text)

    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')

    for li in li_list:
        img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        file_name = file_path+img_name

        #这个细节没想起来，着重复习
        #利用拼接起的的完整图片网址，对这个网址发起请求并获得二进制数据保存至本地便于提取
        img_data = requests.get(url=img_src,headers=heards).content
        fp = open(file_name, 'wb')
        fp.write(img_data)
        print('正在下载中...')

print("下载全部完成")




