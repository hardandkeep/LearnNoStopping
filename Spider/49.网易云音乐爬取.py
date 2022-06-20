# Coding on 20211212
import os
from time import sleep
import requests
from lxml import etree


def spiderSongId():
    '''获得网易云音乐的歌单歌曲id'''
    #网易云音乐歌单url
    url = "https://music.163.com/playlist?id=4932445865"
    #发起请求
    res = requests.get(url,headers=headers).text
    #解析页面
    tree = etree.HTML(res)
    songName = tree.xpath('//ul[@class="f-hide"]/li/a/text()')
    songhref = tree.xpath('//ul[@class="f-hide"]/li/a/@href')
    songId = []
    for i in songhref:
        id = i.strip('/song?id=')
        songId.append(id)

    return songName,songId


def gainSongUrl(songId):
    '''利用外链将id拼接为歌曲网址'''
    songIdList = []
    for id in songId:
        songid = "https://link.hhtjim.com/163/{}.mp3".format(id)
        songIdList.append(songid)

    return songIdList


def DownloadSong(songName,songUrlList):
    '''将拼接好的外链歌曲地址进行下载'''
    try:
        for name,url in zip(songName,songUrlList):
            res = requests.get(url,headers=headers).content
            with open("./songFold/{}.mp3".format(name),'wb') as fp:
                fp.write(res)

    except Exception as result:
        print(result)


if __name__ == "__main__":
    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    }
    #获得歌曲名称和歌曲id
    songName,songId = spiderSongId()
    #利用外链来获得歌曲地址
    songUrlList = gainSongUrl(songId)
    #创建一个文件夹
    if not os.path.exists('./songFold'):
        os.mkdir('./songFold')
    #下载歌曲
    DownloadSong(songName,songUrlList)



