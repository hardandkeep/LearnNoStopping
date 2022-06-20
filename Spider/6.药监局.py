import requests
import json

for p in range(6):

    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"

    pre_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

    data = {
        'on': 'true',
        'page': p,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }

    req = requests.post(url=url,headers=headers,data=data)
    dict_id = req.json()

    #获取id
    i = 0
    list_data = []
    list_id = dict_id["list"]
    id_s = []
    for value in list_id:
        id_ = value["ID"]
        id_s.append(id_)

        #利用获取的id进行添加参数进行爬取数据

        data = {
            'id': id_s[i]
        }
        i = i + 1
        respose = requests.post(url=pre_url,headers=headers,data=data)

    #持久化存储
        dic_json = respose.json()
        list_data.append(dic_json)
print(list_data)


