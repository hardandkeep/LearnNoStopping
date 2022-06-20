"""
为了以后实现剪辑电影之类的
特地实现Bilibili电影爬虫，将电影下载到电脑上

1.随便打开一个电影网页，随后定位到其原文档html包，找到相关cid，id，session等
2.找到playurl包，定位到视频url，测试返回响应
3.输入电影网址，得到相关参数，携带相关参数请求playurl包，得到电影url
4.进行多线程下载视频与音频至文件夹
5.利用ffmepg将视频与音频进行合并
"""

import requests
from lxml import etree
import json
import os
from threading import Thread
from moviepy import *
#from moviepy.editor import *


class BiliMovieSpider:
    def __init__(self, url, head):
        self.doc_url = url
        self.header = head

        self.movie_name = None
        self.movie_video_url = None
        self.movie_audio_url = None

        self.session = requests.Session()

    def request_parse(self):
        doc_res = self.session.get(url=self.doc_url, headers=self.header)
        if doc_res.status_code == 200:
            doc_html = doc_res.text
            tree = etree.HTML(doc_html)
            script = tree.xpath("//script/text()")[5]
            txt = script.replace('window.__INITIAL_STATE__=', '')
            txt = txt.replace(";(function(){var s;(s=document.currentScript||document.scripts"
                              "[document.scripts.length-1]).parentNode.removeChild(s);}());", '')
            txt_dict = json.loads(txt)
            self.movie_name = txt_dict["h1Title"]
            txt_dict = txt_dict["mediaInfo"]["episodes"][0]
            avid = txt_dict['aid']
            cid = txt_dict['cid']
            ep_id = txt_dict['id']

            print("解析doc页成功")
        else:
            print(doc_res.status_code)
            return

        params = {
            "avid": avid,
            "cid": cid,
            "qn": "0",
            "fnver": "0",
            "fnval": "4048",
            "fourk": "1",
            "ep_id": ep_id,
            "session": "3e85eee79f9307e7182201006170e87f"
        }

        play_url = "https://api.bilibili.com/pgc/player/web/playurl?"
        play_res = self.session.get(url=play_url, params=params, headers=self.header)
        if play_res.status_code == 200:
            play_data = play_res.json()
            # 均为最佳画质
            self.movie_video_url = play_data["result"]["dash"]["video"][0]["backupUrl"][1]
            self.movie_audio_url = play_data["result"]["dash"]["audio"][0]["backupUrl"][1]

            print("解析电影URL成功")
        else:
            print(play_res.status_code)
            return

    def download_video(self):
        print("正在下载{}视频".format(self.movie_name))

        try:
            down_video = self.session.get(url=self.movie_video_url, headers=self.header)
            filepath = "./Bilibili电影/"
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            with open(filepath+self.movie_name+".mp4", 'wb') as fp:
                fp.write(down_video.content)
        except Exception as result:
            print("下载{}视频失败，请稍后再试...".format(self.movie_name))
            return

        print("{}视频下载完成".format(self.movie_name))

    def download_audio(self):
        print("正在下载{}音频".format(self.movie_name))

        try:
            down_audio = self.session.get(url=self.movie_audio_url, headers=self.header)
            filepath = "./Bilibili电影/"
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            with open(filepath + self.movie_name + ".mp3", 'wb') as fp:
                fp.write(down_audio.content)
        except Exception as result:
            print("下载{}音频失败，请稍后再试...".format(self.movie_name))
            return

        print("{}音频下载完成".format(self.movie_name))

    def merge_video_audio(self):
        video = VideoFileClip("./Bilibili电影/{}.mp4".format(self.movie_name))   # 读入视频
        audio = AudioFileClip("./Bilibili电影/{}.mp3".format(self.movie_name))   # 读入音频
        video = video.set_audio(audio)   # 将音轨合成到视频中
        video.write_videofile("./Bilibili电影/合并完成")

    def thread_func(self):
        thread_v = Thread(target=self.download_video)
        thread_a = Thread(target=self.download_audio)
        thread_v.start()
        thread_a.start()

    def main(self):
        self.request_parse()
        self.thread_func()


if __name__ == "__main__":
    doc_url = "https://www.bilibili.com/bangumi/play/ss28585?theme=movie&from_spmid=666.7.operation.2"

    head = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "cookie": "_uuid=A0DA2EF6-958E-05CE-27CC-D41DB442C4DF57477infoc; buvid3=E88BF123-D5E9-44DA-87D1-8FA7AA3C403A167622infoc; b_nut=1635686757; sid=7uta5613; rpdid=|(umY~RYumkk0J'uYJYlkJR~~; video_page_version=v_old_home; b_ut=5; i-wanna-go-back=2; CURRENT_BLACKGAP=0; blackside_state=0; fingerprint3=ebea23a94af415a4483638b094435578; fingerprint_s=cda93cc959d72e037a734bc34ee111de; innersign=0; buvid4=22BA184F-08D5-1238-A607-33FD507F182387537-022041122-TvW4JFlOmLtLWy7ozHf4rVEhBbOIBgMwEtRpdh8dDdGNWTxlVzgGTQ%3D%3D; CURRENT_QUALITY=0; fingerprint=eeec0734326de2cbb347169c0c5468cc; buvid_fp_plain=undefined; DedeUserID=471487676; DedeUserID__ckMd5=bd1ee62109bb3bad; SESSDATA=83073f0f%2C1665238748%2Caf616*41; bili_jct=f25208b74d111adfba91a069d2209dcf; buvid_fp=eeec0734326de2cbb347169c0c5468cc; CURRENT_FNVAL=4048; PVID=3; b_lsid=B7739CB1_1801B6C35F0",
        "pragma": "no-cache",
        "referer": "https://www.bilibili.com/movie/",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    }

    spider = BiliMovieSpider(doc_url, head)
    spider.main()


