import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

fp = open("每日蔬菜价格详情.csv",'w',encoding="utf-8")
writer = csv.writer(fp)

def Down_load_onepage(url,headers):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    req = requests.get(url=url,headers=headers,proxies={'https':'115.208.91.103:12488'}).text
    tree = etree.HTML(req)
    #这里千万要注意，我在chrome开发者工具中直接复制的完整xpath路径里面有tbody，但是源代码当中是没有的，这个tbody是开发者工具自动加的
    #所以，xpath路径应该以网页源代码的为准，不能加xtboby，不然会出现列表中无这个元素的错误---估计以前很多时候提取不到也是因为这种原因，开发者工具会自己解析源代码
    #一切以网页源代码为准，因为我们利用解析工具解析的是网页源代码
    tr_list = tree.xpath("/html/body/div[2]/div[4]/div[1]/table/tr")[1:] #用索引来指定输出第二行以及第二行后的元素
    for tr in tr_list:
        data = tr.xpath("./td//text()")
        #对输出的数据进行简单的处理，剔除掉//和\
        #用生成器
        #data = (item.replace("\\","").replace("/","") for item in data)
        #print(list(data))
        writer.writerow(data)



if __name__ == "__main__":
    #url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    #for i in range(1,200):
        #效率极其低下
        url = f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml"
        Down_load_onepage(url,headers)
    '''
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            t.sumbit(Down_load_onepage, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")

