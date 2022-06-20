# coding utf-8

import os
import random
from time import sleep
from tkinter import *

import requests
from lxml import etree

def gainSongurl(artist,page,csrf):
    '''
    获取歌曲名称列表和歌曲地址字典
    :param artist: 作者
    :param page: 所需爬取的页数
    :return: 返回歌曲名称列表和歌曲地址字典
    '''
    url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?"

    params = {
        'key': artist,
        'pn': page,
        'rn': '30',
        'httpsStatus': '1',
        'reqId': 'ff64c670-5d64-11ec-b3ab-af362aed8567'
    }

    headers = {
        'user-agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random.randint(1000, 9999)}.{random.randint(100, 999)} Safari/537.36',
        'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
        'Cookie': '_ga=GA1.2.391452555.1639527875; _gid=GA1.2.248719171.1640241599; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1639544812,1639550600,1640241599,1640241611; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1640241611; kw_token={}'.format(csrf),
        'csrf': csrf,
    }

    res = requests.get(url=url,params=params,headers=headers)

    res = res.json()

    dataList = res['data']['list']

    songNameList = []
    songSongUrlDict = {}
    for d in dataList:
        try:
            songName = d['name']
            rid = d['rid']
            songUrl = "https://link.hhtjim.com/kw/{}.mp3".format(rid)
            songNameList.append(songName)
            songSongUrlDict[songName] = songUrl
            #print(songName)
            #print(songUrl)
        except Exception as result:
            print(result[:18])

    return songNameList,songSongUrlDict

def DownloadSong(songNameList,songSongUrlDict,arist):
    '''
    下载酷我音乐的歌曲
    :param songNameList: 歌曲名称列表
    :param songSongUrlDict: 歌曲名称对应的歌曲地址字典
    :param arist: 歌曲作者
    :return: 无
    '''

    print("正在下载{}的歌...预计下载{}首歌曲！".format(arist,30))

    if not os.path.exists('./{}'.format(arist)):
        os.mkdir('./{}'.format(arist))

    count = 1
    for name in songNameList:
        try:
            url = songSongUrlDict[name]
            print(url)
            res = requests.get(url).content

            print("正在下载第{}首歌曲：{}！".format(count,name))

            with open('./{}/{}.mp3'.format(arist,name),'wb') as fp:
                fp.write(res)

            count += 1

        except Exception as result:
            print(str(result)[:19])

        time = [1.8, 2.1, 2.5, 2.7, 3]
        #sleep(random.choice(time))

def gainCsrf():
    '''
    伪造csrf加密参数
    :return:
    '''
    e = 'abcdefghizklmnopqrstuvwxyz1234567890'
    eList = []
    for i in e.upper():
        eList.append(i)

    csrf = ''
    for i in range(11):
        csrf = csrf + random.choice(eList)

    return csrf


if __name__ == "__main__":

    while True:
        print("输入q可退出程序！")
    
        airist = input("请输入你要下载歌曲的作者：")

        print("请前往'https://www.kuwo.cn/search/list?key={}'选择爬取那一页！".format(airist))

        if airist == 'q':
            break

        page = input("请输入你要下载第几页：")

        if page == 'q':
            break

        #伪造csrf加密参数
        csrf = gainCsrf()

        #爬取歌曲名称和歌曲地址
        songNameList,songSongUrlDict = gainSongurl(airist,page,csrf)
        #下载歌曲
        DownloadSong(songNameList,songSongUrlDict,airist)

        sleep(5)


