from selenium import webdriver
from time import sleep
#实行无可视化界面(谷歌的无头浏览器一直在更新，selenium自带的phantomjs已经停止更新，但是phantomjs不需要在自带一个浏览器啊，做成exe的时候多方便)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

#实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable--gpu')

#实现规避检测(要用的时候直接复制粘贴)
option = ChromeOptions()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
option.add_experimental_option('excludeSwitches',['enable-automation'])
#如何实现让selenium#规避被检测的风险
bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options,options=option)


#无可视化界面(无头浏览器) phantomJs
bro.get('https//www.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()