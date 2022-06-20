#访问qq空间
import time
from Yzm_Sb import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

id_mima_btn = bro.find_element_by_id('switcher_plogin')
id_mima_btn.click()

input_u = bro.find_element_by_id('u')
input_u.send_keys('1477792904')
time.sleep(2)
input_p = bro.find_element_by_id('p')
input_p.send_keys('aini10000nian.')
time.sleep(2)
login_ = bro.find_element_by_id('login_button')
login_.click()

