#进行识别古诗词网验证码尝试
from lxml import etree
import requests
from Yzm_Sb import Chaojiying_Client
from PIL import Image


#古诗词网登录界面网址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

#UA伪装
heards = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

#发起请求
page_text = requests.get(url=url,headers=heards).text

#创建一个etree对象
tree = etree.HTML(page_text)

#使用xpath对页面进行解析
img_yzm = tree.xpath('/html/body/form[1]/div[4]/div[4]/img/@src')[0]
yzm_jpg = 'https://so.gushiwen.cn/'+img_yzm

#再次请求验证码图片地址
yzm_text = requests.get(url=yzm_jpg,headers=heards).content

#保存二进制gif验证码图片
fp = open('yzm.gif','wb')
fp.write(yzm_text)
fp.close()

#gif转jpg格式是从网上copy的，要掌握
#打开gif格式的图片
im = Image.open(r'yzm.gif')
im = im.convert('RGB')
def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass
for i, frame in enumerate(iter_frames(im)):
    # 保存成jpg格式
    frame.save(r'yzm'+'.jpg',**frame.info)

#要对验证码进行识别需要调用超级鹰的类(注意需要把它们的那个代码复制到和这个文件同目录)

# 用户中心>>软件ID 生成一个替换 96001
chaojiying = Chaojiying_Client('1477792904', 'aini3333nian.', '915180')
# 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
im = open('yzm.jpg','rb').read()
# 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
print(chaojiying.PostPic(im, 1004))
