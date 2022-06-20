#you-get的基本使用

'''
pip install you-get

在命令行时:
    下载单个视频:you-get url ---该命令会直接将视频下载到命令行输出的文件夹

    批量下载:you-get --playlist url ---批量下载的同时也会将视频里的弹幕也给下载下来
        如果想开启弹幕，可以下载Danmu2Ass工具，将弹幕格式转换成ass格式，即可

    暂停和继续:Ctrl+c,此时会在命令行中输出的文件中存在一个.download的缓存文件
             在命令行里面重新输入刚刚的那个命令，它会对该文件夹进行检测，如果有缓存的.download文件，它就会继续从这里开始下载

    查看视频参数:you-get -i url ---......

    指定清晰度下载:当我们拿到视频的参数详情后，我们可以选择我们想要下载的视频格式
                 命令如下:you-get ----format=flv360/720/1080... url

    指定下载路径:you-get -o 路径 url

用python下载:使用sys库(操作命令行的)
    import sys
    from you_get import common as you_get
    url = ""
    sys.argv=['you-get','-i',url]
    you_get.main()
'''

import sys
from  you_get import common as you_get

'''
#下载单集
url = "https://www.bilibili.com/bangumi/play/ss31778?from_spmid=666.24.0.0"
#偿试了好几次发现，他会默认下载在我这个py文件所在的目录,于是我想在这个目录里面的新垣结衣文件夹里存,即,./新垣结衣

sys.argv=["you-get""-o","./通灵妃",url]
you_get.main()
'''
#下载多集
url = "https://www.bilibili.com/bangumi/play/ss33624?from_spmid=666.24.0.0"
#偿试了好几次发现，他会默认下载在我这个py文件所在的目录,于是我想在这个目录里面的新垣结衣文件夹里存,即,./新垣结衣

sys.argv=["you-get","--playlist","-o","./红楼梦",url]
you_get.main()




