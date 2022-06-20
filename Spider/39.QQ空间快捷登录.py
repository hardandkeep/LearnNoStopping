from selenium import webdriver
import time

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://qzone.qq.com/')

time.sleep(2)

bro.switch_to.frame('login_frame')

button = bro.find_element_by_id('img_out_1477792904')
button.click()

time.sleep(2)

bro.maximize_window()

time.sleep(2)

bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(2)

bro.quit()
