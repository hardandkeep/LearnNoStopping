#while循环简介
'''
for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到条件不满足为止
'''
'''
#接下来的代码最好都理解透和熟记于心

current_nmber = 1
while current_nmber <= 5:
    print(current_nmber)
    current_nmber += 1     #当条件不满足时，执行步骤跳出循环，然后继续顺序执行
print(current_nmber)


#让用户选择何时退出：我们只需要利用while循环，设置一个退出值，当不是这个值时，程序继续运行，当是这个值时，程序退出

message = ''   #需要提供一个空字符串用以while条件的判断，否则无法判断
while message != 'esc':
    message = input('你可以输入esc用以退出程序：')
print("你已经成功退出程序！")


#使用标志：在要求很多条件都满足才继续运行的程序中，可定义一个变量额来判断整个程序的活动状态。
   #使用这种标志，你可以使程序在标志为False时停止运行，让标志位True时让程序继续活跃

active = True
while active:
    message = input('输入信息，我将返回给你，或者输入quit退出程序：')
    
    if message == 'quit':
        active = False
        print("你已经成功退出程序")
    else:
        print(message)
'''
'''
#使用break退出循环
 
 要立刻退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句

 break语句用于控制程序流程，可使用它来控制那些代码行将被执行，那些代码行不被执行，从而让程序按我的要求来执行代码
 '''
'''
#如， 改进上面的退出机制

while True:
    city = input('请输入你喜欢的城市名字，亦可以输入quit退出程序')
    
    if city == 'quit':
        print('你已经成功退出程序')
        break
    else:
        print(city)
'''

#在循环中使用continue：要返回到循环开头，并根据条件测试结果决定是否继续执行，可使用continue语句
   #它不像break语句那样不再执行余下的代码并退出整个循环，它只是
#例如用从一数到十，但只打印偶数的循环：

'''
current_number = 0
while current_number <10:
    current_number += 1
    current_numbers = current_number % 2
    if current_numbers == 0:
        print(current_number) 
这个是输出十以内包括十的偶数，接下来使用continue来输出偶数
'''
current_number = 0
while current_number <10:
    current_number += 1
    current_numbers = current_number % 2
    if current_numbers != 0:
        continue    
    '''
    在这边是，如果这个数的求余不等于0(即奇数)，那么执行continue语句并且忽略循环内的下方语句，
    回到开头继续执行，这样当数是偶数时，if的条件判断不通过，执行print语句输出偶数，
    就这样利用了continue语句过滤了所有奇数
    '''
    print(current_number)


#注意：要避免无限循环

'''
注意：在学习过程中我老是遇到那种比如一个列表的名字就直接拿来当作while循环的条件的
那不是错的，那是利用了条件测试，使用true和false，比如列表为空的时候表示为false，非空的时候表示true
这样，循环就可以持续下去
具体问题具体分析
'''        
