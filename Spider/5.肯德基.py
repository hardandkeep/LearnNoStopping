import requests
import json
import time
'''
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
'''

for i in range(1,9):
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }
    data = {
        'cname':'',
        'pid':'' ,
        'keyword': '北京',
        'pageIndex': i,
        'pageSize': '10'
        }
    
    req = requests.post(url=url,headers=headers,data=data)
    time.sleep(2)
    
    dict_json = req.json()
    
    fp = open('./kfc.json','w',encoding='utf-8')
    json.dumps(dict_json,fp=fp,ensure_ascii=False)
    
    print('over!!!')