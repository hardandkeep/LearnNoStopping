from selenium import webdriver
import time
#导入动作链对应的类
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在与iframe标签制作的则必须通过如下操作在进行定位

#切换浏览器标签定位的作用域
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

#动作链
action = ActionChains(bro)
#点击长安指定的标签
action.click_and_hold(div)

for i in range(5):
    #perform()立刻执行动作链操作
    action.move_by_offset(17,0).perform()#move_by_offset(x,y)x,y坐标轴
    time.sleep(0.3)

#释放动作链
action.release()

bro.quit()
