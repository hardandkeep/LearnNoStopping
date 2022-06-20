from time import sleep

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#设置账号密码
loginId = '17353756960'
loginPw = 'aini3333nian.'

# selenium检测 CDP-->Google 的Chrome Devtools-Protocol 来解决这个问题
options = webdriver.ChromeOptions()
#忽略证书警告
options.add_argument('ignore-certificate-errors')
#开启selenium实验性功能参数
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#防止被检测为自动化测试软件
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=options)
#设置cdp不会触发淘宝登陆滑块（没有这个设置就需要过阿里滑块）
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

#使用selenium打开网页
driver.get('https://login.taobao.com/member/login.jhtml?'
           'spm=a21bo.jianhua.201864-2.d1.5af911d9KtXPp5&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F')

#显式等待
wait = WebDriverWait(driver,10)
#定位并等待输入账号框元素出现
login_id = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="fm-login-id"]')))
#输入账号
if login_id:
    for i in loginId:
        login_id.send_keys(i)
        sleep(0.3)
#定位并等待输入密码框元素出现
login_pw = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="fm-login-password"]')))
#输入密码
if login_pw:
    for p in loginPw:
        login_pw.send_keys(p)
        sleep(0.3)

sleep(0.4)
#定位并等待登录按钮元素出现
enter = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="login-form"]/div[4]/button')))
if enter:
    enter.click()

sleep(3)
cookie = driver.get_cookies()
print(cookie)
sleep(15)
#关闭浏览器
driver.close()