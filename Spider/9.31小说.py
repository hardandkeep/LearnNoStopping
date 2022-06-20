#2021.4.2日下午，自己分析了31小说这个网站，实现了爬取
#表明这个网站里面的小说我均可爬取下来,改一下url和即可
#到后面学习异步，并向，多线程爬取
#使用了os库，利用os库来实现和系统的交互---创建了一个文件夹

import requests
import json
import re
import os
import tkinter
from threading import Thread

def download_story():

    name = input("请输入小说名字:")
    File_path = './' + name + '/'
    if not os.path.exists(File_path):
        os.mkdir(File_path)

    heards = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    url = url_entry.get()
    req = requests.get(url=url,headers=heards)

    res = req.text

    title = re.findall('<dd><a href=".*?">(.*?)</a></dd>',res,re.S)

    list_req = re.findall("(\/\d+\/\d+\/\d+\.html)", res, re.S)

    all_page_list = []

    count = 0
    for i in list_req:
        pre_url = 'http://www.31xiaoshuo.com'+i

        pre_req = requests.get(url=pre_url,headers=heards)

        pre_res = pre_req.text

        zjdl_text_list = re.findall('<p>(.*?)</p>',pre_res,re.S)

        #持久性存储
        filePath = File_path + str(count+1)+"."+title[count]+'.text'
        count = count + 1
        #print(zjdl_text_list)
        with open(filePath,'w',encoding='utf-8') as f:
            for message in zjdl_text_list:
                f.write(message)
    print('下载完成')

def theading():
    thead_1 = Thread(target=download_story)
    thead_1.setDaemon(True)
    thead_1.start()


window = tkinter.Tk()
window.title("你红哥牌下载器")
window.geometry('300x150')
label_1 = tkinter.Label(text="31小说下载器")
label_1.pack()
label_2 = tkinter.Label(text='在浏览器打开http://www.31xiaoshuo.com/')
label_2.pack()
label_3 = tkinter.Label(text='点击你想下载的小说，跳转到该小说页面')
label_3.pack()
url_label = tkinter.Label(text='在输入框输入你复制的小说目录页面网页链接:')
url_label.pack()
url_entry = tkinter.Entry()
url_entry.pack()
button_1 = tkinter.Button(text='立刻下载',command=theading)
button_1.pack()
window.mainloop()
