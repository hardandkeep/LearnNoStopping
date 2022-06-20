# 首先需要安装requests库pip install request并import
import requests

# 简单的请求
res = requests.get(url='https://www.baidu.com')
print(res.status_code)