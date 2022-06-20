import requests
import random


ip = requests.get("http://www.zdopen.com/ShortProxy/GetIP/?api=202111042241254911&akey=84e58a925bded778&timespan=5&type=3")

ip_list = ip.json()['data']['proxy_list']
ipList = []
for ip in ip_list:
    i = str(ip['ip']) + ':' + str(ip['port'])
    ipList.append(i)

print(ipList)

url = 'https://www.baidu.com'

heards = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

#注意：还要加上端口
proxies = {
    "http": random.choice(ipList)
}

page_text = requests.get(url=url,headers=heards,proxies=proxies).text
page_text.encode().decode('utf-8')
print(page_text)


'''
proxies = {
    "http": 'ip:port'
}
requests.get(url=url,proxies=proxies)
'''


















