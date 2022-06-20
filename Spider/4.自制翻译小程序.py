#自制翻译小程序
    #总结：reques和urllib中的data和parms是可以添加参数的（参数会附加在url后面）
    #    文件的持久化存储---利用变量
    #    阿贾克斯(ajks)的初步了解以及应用
    #想程序一直运行加个while循环，想给查询的单词或者词语排序，加个for循环
#翻译句子功能尚未实现
import tkinter
from tkinter import *
import requests
import json
#for i in range(1,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):

window = tkinter.Tk()

window.title("你红哥翻译小程序")

entry = Entry(window)
entry.pack()

#word = entry.get()

def attain_trans():
    #1.指定url
    post_url = "https://fanyi.baidu.com/sug"
    #2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    word = entry.get()

    #3.post请求参数处理(同处理get时的parms一致)
    data = {
        "kw":word
    }
    req = requests.post(url=post_url,data=data,headers=headers)

    #5.获取响应数据:json()方法返回的是obj(当确认响应数据是json类型时，才可以使用json()方法返回数据)
    dic_obj = req.json()
    try:
        trans_word = dic_obj["data"][0]["v"]
        var.set(trans_word)
    except:
        var.set("翻译失败")

button = Button(window,text="翻译",command=attain_trans)
button.pack()

var = StringVar()
label = Label(window,textvariable=var,background='yellow',width=50)
label.pack()

window.mainloop()