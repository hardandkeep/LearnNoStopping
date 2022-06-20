#典型的ajax请求

import requests
import json

if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"

    param = {
        'type': '11',
        'interval_id': '100:90',
        'action':'',
        'start': '0',
        'limit': '20'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    req = requests.get(url=url,params=param,headers=headers)
    list_json = req.json()

    fp = open('./douban_spider.json','w',encoding='utf-8')
    #使用dump方法转换json对象
    json.dump(list_json,fp=fp,ensure_ascii=False)

    print('over!!!')
