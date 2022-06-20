import json
from time import sleep
import random
import requests


def getMblogid(pagenum,headers):
    '''携带cookie获取播主页面接口中的mblogid'''
    url = 'https://weibo.com/ajax/statuses/mymblog?uid=1924585171&page={}&feature=0'.format(pagenum)
    session = requests.Session()
    res = session.get(url,headers=headers)
    print(res.text)
    jsonData = res.json()
    dataList = jsonData['data']['list']
    idList = []
    for data in dataList:
        isLongText = str(data['isLongText'])
        if isLongText == 'True' or isLongText == 'true':
            mblogid = data['mblogid']
            idList.append(mblogid)
            print(mblogid)

    return idList

def longText(mblogid,headers):
    url = 'https://weibo.com/ajax/statuses/longtext?id={}'.format(mblogid)
    session = requests.Session()
    res = session.get(url,headers=headers)
    jsonData = res.json()
    longTextContent = jsonData['data']['longTextContent']
    print(longTextContent)
    with open('blog.txt','a',encoding='utf-8') as fp:
        fp.write(longTextContent)


if __name__ == '__main__':

    cookie = 'SINAGLOBAL=942725036976.8325.1633678388598; ULV=1633678388604:1:1:1:942725036976.8325.1633678388598:; SCF=Ar8ASZOOHgkN03WdGrdvx285GJDhF8hcLWEH6jCAzKVL9IsB51Kq3_efYQbwWZyFG5R2Ru9KBkww5y1f1_zhRt4.; XSRF-TOKEN=i7NcA_Axgur0h8m8q_1c3cZk; SUB=_2A25MrpI-DeRhGeFL6FsW8CzEzDyIHXVv3YT2rDV8PUNbmtAKLRTTkW9NQgqoVwnGle4gAHAlkidkITv640Flt3NM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W57h5B7f8wpvmYbj7mAUWyr5JpX5KzhUgL.FoMfe0.NehzRS052dJLoIX8-i--fiKLFiKL8i--fiKnRi-z7i--fiKysi-2Xi--Xi-iFi-20i--Ri-2NiKnpi--ciKL2iKy8i--NiK.4i-i2H5tt; ALF=1670125038; SSOLoginState=1638589038; WBPSESS=izT1azHHfvHDh_VXumHQ-3zmWTx8561_Wr392hFEv0X04gX9k4RVtGjksbjzTLyodn7E7rMCVHc2QHNKGxEmvuhmxItTyEhPC2RNltJhdyyXCrcdpnXBkBSMq4H3ZsHxKkWPBSD7XTRzhkbovA4LEg=='

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'referer': 'https://weibo.com/u/1924585171',
        'Cookie': cookie,
    }

    count = 1
    while True:

        idList = getMblogid(count,headers)
        count += 1
        for id in idList:
            longText(id,headers)
            randtime = [1,1.5,2,2.5]
            sleep(random.choice(randtime))
        sleep(1)



