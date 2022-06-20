import time
from selenium.webdriver.chrome.options import Options
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
try:
    #无头浏览器操作
    opt = Options()
    opt.add_argument('--headless')
    #warnings.filterwarnings("ignore",message=".*PhantomJS has been deprecated.*",category=UserWarning)
    #bro = webdriver.PhantomJS(executable_path='phantomjs.exe')
    bro = webdriver.Chrome(executable_path='chromedriver.exe',options=opt)

    bro.get('http://10.255.0.19/')

    id_input = bro.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/form/input[3]')
    id_input.send_keys('2020304023')

    mima_input = bro.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/form/input[4]')
    mima_input.send_keys('304023')
    #在封装之前确定是那个运行商网络
    dx_button = bro.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/select/option[3]')
    dx_button.click()
    #yd_button = bro.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/select/option[5]')
    #yd_button.click()
    #lt_button = bro.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/select/option[4]')
    #lt_button.click()
    #这里原本出现了一个错误
    dl_button = bro.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/form/input[2]')
    bro.execute_script("arguments[0].click();", dl_button)
    print('校园网登录完成...')
    bro.quit()
except Exception:
    print('你可能已经登录过了！')
    time.sleep(2)
    bro.quit()
'''
'''
今天用selenium尝试做网页测试的时候遇到一个错误：

selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <button onclick="kwdGoSearch($('#kwdselectid').val());">...</button> is not clickable at point (660, 229). Other element would receive the click: <div id="work_position_click_center_right" class="con">...</div>
  (Session info: chrome=80.0.3987.149)
1
2
原因：
应该是元素定位相互覆盖。
解决办法：
将：

driver.find_element_by_css_selector('.ush button').click()
1
改为：

element1 = driver.find_element_by_css_selector('.ush button')
driver.execute_script("arguments[0].click();", element1)
'''

if EC.presence_of_element_located(By.ID,'id'):
    pass

