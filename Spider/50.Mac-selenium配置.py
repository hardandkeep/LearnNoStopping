'''
1.python：pip3 install selenium

2.进入镜像网站:http://chromedriver.storage.googleapis.com/index.html选择对应的谷歌浏览器的驱动版本

3.Mac-m1选m1版本，Mac选mac版本，windows选win32版本，下载解压

4.Mac将ChromeDriver拷贝到/usr/local/bin下，windows复制到python的Scripts下或随意放，然后运行时指定

5.运行测试，Mac可能会有不识别不信任的问题：
    解决方法：cd /usr/local/bin/
            xattr -d com.apple.quarantine chromedriver
            信任即可
'''

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options

#实现无可视化界面的操作
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable--gpu')

#实现规避检测(要用的时候直接复制粘贴)
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=option)

driver.get("https://www.baidu.com")

