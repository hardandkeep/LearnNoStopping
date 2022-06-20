#有时候我们最开始并不知道函数需要接受多少个实参，好在python允许函数从调用语句中收集任意数量的实参
   #例如看一个制作披萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少中配料
   #下面的函数只有一个形参*toppings，但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中

#传递任意数量的实参的关键是：*形参

def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print(toppings)

make_pizza('pppppp')
make_pizza('pppppp','aaaaaaa','bbbbbbb')
'''
解释：形参名*toppings中的星号让python创建了一个名为toppings的空元组，并将其收到的所有值都封装到这个元组中
函数体内的print语句通过生产输出来证明python能够处理使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形
它以类似的方式处理不同的调用，注意：python将实参封装到一个元组中，即便函数只收到一个值也是如此

将实参封装到元组中，日常生活中有了解过整体代换，应该亦是如此吧！
'''

#将print替换为循环:使出来的值正常点

def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('-',topping)

make_pizza('pppppp')
make_pizza('pppppp','aaaaaaa','bbbbbbb')








#结合使用位置实参和任意数量实参
'''
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中

例如，如果前面的函数还需要一个表示披萨尺寸的实参，必然将该形参放在形参*topping的前面
'''

def make_pizza(size,*toppings):
    '''概述要制作的披萨'''
    print('\nMaking a ', str(size),'-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ',topping)

make_pizza(16, 'pppppp')
make_pizza(12,'aaaaaaa','ppppppp')







#使用任意数量的关键字实参
'''
有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息
在这种情况下，可将函数编写成能够接受任意数量的键-对值——————调用语句提供了多少就接受多少
一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息
在下面的示例中，函数build_profile()接受名和姓，同时还接受任意数量的关键字实参
'''

def build_profile(first,last, **user_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)