import requests
from lxml import etree
from multiprocessing import pool
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
}
# 保存视频的id
contId = ""
# 保存视频的所有下载链接
urls = []


def init():
    # 获取首页的视频信息
    url = "https://www.pearvideo.com/category_5"
    # UA 伪装
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43"
    }
    res = requests.get(url=url, headers=headers).content
    tree = etree.HTML(res)

    # 获取视频标题以及详情信息的地址
    for li in tree.xpath("//ul[@id='listvideoListUl']/li"):
        # 视频的标题
        video_name = li.xpath(".//div[@class='vervideo-title']/text()")[0]
        # 视频的详情url
        video_url = "https://www.pearvideo.com/" + li.xpath(".//a[@class='vervideo-lilink actplay']/@href")[0]

        # 获取视频的id
        contId = video_url[::-1][:7][::-1]
        # 创建了一个session对象来保持会话
        session = requests.session()
        url = "https://www.pearvideo.com/videoStatus.jsp"
        headers = {
            # 这里需要视频详情界面的url
            "Referer": video_url,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
        }
        # 请求的Id参数
        param = {
            "contId": contId
        }

        # 获取视频伪装过的下载链接
        res = session.get(url=url, params=param, headers=headers).json()
        # 被伪装的下载地址
        down_url = res['videoInfo']['videos']['srcUrl']

        # 需要被替换的模式
        ex = "third/.*?/(.*?)-.*?"
        # 需要被替换的字符串
        need_replace = re.findall(ex, down_url)[0]
        # 替换后的字符串
        replaced = "cont-" + contId
        # 真实的下载地址
        down_url = down_url.replace(need_replace,replaced)

        # 将url和视频名称封装进url列表
        dic = {
            "name": contId + ".mp4",
            "url": down_url
        }
        urls.append(dic)

# 下载视频
def down(urls):
    url = urls['url']
    name = urls['name']
    print(name, "正在下载")
    resPage = requests.get(url=url, headers=headers)
    print(resPage.status_code)
    with open(name, 'wb') as fp:
        fp.write(resPage.content)
    print(name, "下载完成")


if __name__ == "__main__":
    init()
    mypool = pool.Pool(4)
    mypool.map(down, urls)



