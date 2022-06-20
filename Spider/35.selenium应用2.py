#自动打开淘宝和输入
from selenium import webdriver
import time
#实例化一个浏览器对象
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
#指定浏览器打开特定的url
bro.get('https://www.taobao.com/')

#标签定位(find一类的方法)
search_input = bro.find_element_by_id('q')
#标签交互
search_input.send_keys('iphone')

#滚动操作记得学习
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')

#定位搜索标签
btn = bro.find_element_by_css_selector('.btn-search')
#点击
btn.click()


#打开另外一个页面
bro.get('https://www.baidu.com')
time.sleep(2)
#回退页面
bro.back()
time.sleep(2)
#前进页面
bro.forward()

time.sleep(5)
bro.quit()


