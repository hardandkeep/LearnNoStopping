#每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试.
#根据条件测试的值为True还是False来决定是否执行if语句中的代码。
#如果条件测试的值为True，Python就执行紧跟在if语句后面的代码，如果为False，则忽略

#  1.检查是否相等
car = 'lanbogini'
car == 'lanbogini'
   #一个等号为赋值，两个等号为判断是否相等
car = 'xuefulan'
car == 'lanbogini'
   #当然，想看到结果为True还是False要print()函数

#  2.
car = 'Lanbogini'
car == 'lanbogini'

car = 'Lanbogini'
car.lower()  == 'lanbogini'

#  3.检查是否不相等：使用惊叹号和等号组合
car = 'lanbogini'
car != 'xuefulan'

#  4.比较数字
age = 1
age == 1
   # > < >= <=
age = int(input("请输入你的年龄："))
if age>= 18:
    print('you are a big boy!')
else:
    print('you are too small!')





#  5.检查多个条件：and or not
age_0 = 22
age_1 = 18
age_0 >= 0 and age_1 >=21
   #结果为false
age_1 = 22
age_0 >= 21 and age_1 >= 21
   #结果为true
   #也可以写成(age_0 >= 21 and (age_1 >= 21))

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 > 21
   #结果为true
age_0 = 18 
age_0 >= 21 or age_1 >=21
   #结果为false





#   6.检查特定值是否包含在列表中
cars = ['lanbogini','maikailun','baoma','xuefulan']
print('lanbogini' in cars) 
print('jjjjjj' in cars)
   #利用这种语法格式即可检查列表中是否存在我们想要的元素

#   7.检查特定值是否不包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
   print(user.title() + ',you can post a respone if you wish.')

#   8.布尔表达式
'''
随着你对编程的了解越来越深入，将遇到术语布尔表达式，它不过是条件测试的别名
与条件表达式不一样的是，布尔表达式的结果要么为true要么为false

布尔表达式通常用来记录条件，如游戏是否在运行，或用户是否可以编辑网站的特定内容
在跟踪程序状态或程序中的重要的条件方面，布尔值提供了一中高效的方式
'''
game_active = True
can_edit = False
