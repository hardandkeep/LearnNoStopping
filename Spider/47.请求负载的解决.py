import json
import requests

url = 'https://www.pzds.com/api/public/goods/ys/listAccount'
headers = {
    'Cookie': 'UM_distinctid=17bdea56a57289-05863ab5e3b83c-2343360-1fa400-17bdea56a5857e; CNZZDATA1279695818=1975124089-1631517705-|1631517705',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Referer':'https://www.pzds.com/goodsList?gameCode=YS&linkClick=131',
    'Origin':'https://www.pzds.com'
}

#将请求负载中的都复制，然后剔除一些无效的(null的)
data = {
    "action": {
    "goodsType": "ACCOUNT",
    "gameCode": "YS",
    },
    "sort": "onStandTime",
    "order": "desc",
    "page": 1,
    "pageSize": 20,
    "gameCode": "YS"
}

#观察请求头那需要什么类型的参数--例如这里就是json传入
resp = requests.post(url=url, headers=headers, json=data,timeout=None)
print(resp.text)