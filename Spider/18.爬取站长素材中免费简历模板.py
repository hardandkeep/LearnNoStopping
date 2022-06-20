
#已经使用selenium+requests实现

import requests
from lxml import etree
import time
import re
#因为之前那个网址已经被改了，所以这个就拿来做一个获取图片的示范


url = 'https://scpic.chinaz.net/files/pic/jianli/201902/hwbg28/1.jpg'

#UA伪装
heards = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

r = requests.get(url=url,headers=heards).content


#在获取了图像链接之后直接对该图像链接发起请求，拿到其二进制数据，存入jpg文件中即可看到其图像


#视频的原理其实差不多，但是要更复杂
#但是python第三方库提供了一个库，可以传入该视频链接，这个库会自动解析然后下载该视频

fp = open('jianli.jpg','wb')
fp.write(r)
fp.close()



