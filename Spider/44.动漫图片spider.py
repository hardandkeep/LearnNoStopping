import requests
from lxml import etree
import os


def save(i,jpg_pic):
    print('正在下载第', i+1, '个动漫图片')
    with open('./动漫图片/' + str(i+1) + '.jpg', 'wb') as fp:
        fp.write(jpg_pic)


def spider(page,i):
    url = 'https://anime-pictures.net/pictures/view_posts/' + str(page) + '?lang=zh_CN'
    res = requests.get(url=url, headers=heards).text
    tree = etree.HTML(res)
    #定位图片地址列表
    span_list = tree.xpath('//*[@id="posts"]/div[2]/span')
    #对图片地址元素列表里面的每一个元素进行定位与请求
    for span in span_list:
        try:
            #定位到含有图片的网址
            href = span.xpath('./a/@href')[0]
            #拼接为一个完整的含有图片的网址
            pic_url = 'https://anime-pictures.net' + href
            #对此含有图片的网址进行请求
            detail_res = requests.get(url=pic_url, headers=heards).text
            detail_tree = etree.HTML(detail_res)
            #定位到目标图片地址
            src = detail_tree.xpath('//*[@id="big_preview"]/@src')[0]
            #拼接出图片地址
            src_url = 'https:' + src
            #对图片地址进行请求得到二进制数据
            jpg_pic = requests.get(url=src_url, headers=heards).content
            #将图片进行保存
            save(i,jpg_pic)
            # 计数器
            i = i + 1

        except Exception as result:
            print(result)
    return i



if __name__ == "__main__":

    # UA伪装
    heards = {
        'referer': 'https://anime-pictures.net/?lang=zh_CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    #新建一个文件夹用来保存图片
    if not os.path.exists('./动漫图片/'):
        os.mkdir('./动漫图片/')

    i = 0
    for page in range(0,10): #自己设置爬取页数
        #进行爬取与保存
        i = spider(page=page,i=i)
