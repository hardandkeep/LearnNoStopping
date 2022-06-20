'''
记住函数定义之中形参可能包含多个，因此函数调用中也可能包含多个实参
向函数传递参数的方式很多，可使用'位置实参'，这要求实参的顺序与形参相同
也可以使用'关键字实参'，其中每个实参都由变量名和值组成
还可以使用'列表，字典'，下面依次介绍这几种方式
'''

#1.位置实参：其实就是按照顺序一一对应
def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print('\n I have a ' , animal_type , '!')
    print('My ' , animal_type , "'s name is " , pet_name.title() , '.')

describe_pet('hamster','harry')    #其中，hamster和harry分别对应储存在animal_type和pet_name中


#2.关键字实参：其实就是在调用的时候，直接指明形参1=实参1，形参2=实参2......
def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print('\n I have a ' , animal_type , '!')
    print('My ' , animal_type , "'s name is " , pet_name.title() , '.')

describe_pet(animal_type = 'hamster',pet_name = 'harry')


#3.默认值：其实就是在定义函数的时候就先给形参一个默认值，这样在调用函数的时候就算没有传递实参亦可以输出相应的返回值
def describe_pet(pet_name,animal_type = 'dog'):
    '''显示宠物信息'''
    print('\n I have a ' , animal_type , '!')
    print('My ' , animal_type , "'s name is " , pet_name.title() , '.')

describe_pet(pet_name = 'lixuexue')   #注意，刚刚我的pet_name是放在animal_type之后的，然后调用时报错了
                                      #所以，顺序也要注意，即有默认值的形参往后面放
                                      #即，在形参列表中必须先列出没有默认值的形参



