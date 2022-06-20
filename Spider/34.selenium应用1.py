#就拿昨天晚上气死我的这个站长简历模板的这个网站开刀，爬爆它
from selenium import webdriver
from lxml import etree
import requests
import time
import os

#实例化一个浏览器对象
bro = webdriver.Chrome(executable_path = './chromedriver.exe')

#用get方法打开一个指定的url
bro.get('https://sc.chinaz.com/jianli/daxuesheng.html')

#获取当前浏览器页面的源码数据
page_text = bro.page_source

#用xpath解析数据
tree = etree.HTML(page_text)
detail_url = tree.xpath('/html/body/div[5]/div[2]/div/div/div/a/@href')

time.sleep(2)
bro.quit()

#将获取的页面模板链接拼接并获取模板
moban_url_list=[]
moban_img_list=[]
heards = {
'Referer': 'https://sc.chinaz.com/jianli/190306274410.htm',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'
}
for i in detail_url:
    moban_url = 'https:'+i
    moban_url_list.append(moban_url)
print(moban_url_list)

if not os.path.exists('./站长简历集'):
    os.mkdir('./站长简历集/')

k = 0

for j in moban_url_list:
    k += 1
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get(j)
    # 尝试了多次之后在这个位置让脚本停了两秒，这次成功获取到了想要的标签，得出结论，那个图片链接，是最后渲染出来了，直接瞬间打开的时候还没有渲染完，没拿到渲染完之后的网页源代码
    #建议使用显示等待
    time.sleep(2)
    moban_text = bro.page_source
    print(moban_text)
    n_tree = etree.HTML(moban_text)
    moban_img = n_tree.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[2]/span/img/@src')[0]
    moban_img_url = "https:"+moban_img
    moban_content = requests.get(moban_img_url).content
    print(moban_content)
    fp = open("./站长简历集/"+str(k)+".模板图片.jpg", "wb")
    fp.write(moban_content)
    fp.close()
    bro.quit()

















'''
    moban_text = requests.get(url=moban_url,headers=heards).text
    n_tree = etree.HTML(moban_text)
    moban_img = n_tree.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[2]/span/img')
    moban_img_list.append(moban_img)
'''




