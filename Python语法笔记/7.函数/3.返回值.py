'''
函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值
函数返回的值被称为返回值
在函数中，可使用return语句将值返回到调用函数的代码行
返回值能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序
'''

#1.返回简单值:注意，返回的值需要有个变量来接收
def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

my_sister = get_formatted_name('li','xuexue')
print(my_sister)
    #但是这引发了一个问题，并不是所有的人姓名都是两个字，或者是三个字





#2.让实参变成可选的：关键是——空字符串 + if语句
def get_formatted_name(first_name,middle_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

my_sister = get_formatted_name('li','xue','lian')
print(my_sister)
     #当向返回的名字只有两个字时，要如何做呢？---其实只需给要选择是否输出的那个形参来个空字符串
def get_formatted_name(first_name,last_name,middle_name = ''):
    '''返回整洁的姓名'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

my_sister = get_formatted_name('li','xue')    #这边仍需要注意的是，赋予空字符串的那个形参要放到最后
print(my_sister)
                                              #注意这边的条件测试，python将空字符串解读为False，非空解读为True

#3.返回字典：函数可以返回任何类型的值，包括列表和字典等较复杂的数据结构
def build_person(first_name,last_name):
    '''返回一个字典，其中包含了有关一个人的信息'''
    person = {'first':first_name,'last':last_name}
    return person

my_sister = build_person('li','xue')
print(my_sister)
'''
解释：函数build_person()接受名和姓，并将这些值封装到字典中，存储first_name的值时使用的键为'first'
而储存last_name的值时用的是键'last'
最后返回表示人的整个字典，打印这个返回的值，此时原来的两项文本信息存储在了字典之中
'''

#4.结合使用函数和while循环：记住，现在学的和之前学的都可以任意搭配使用
def get_formatted_name(first_name,last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

#这是一个无限循环！——————无限循环可以让程序持续运行，非常有用
while True:
    print('\nPlease tell me your name:')
    print("\nif you want to quit the program please input 'quit'")
    f_name = input('First name:')
    if f_name == 'quit':
        break
    l_name = input('Last name:')
    if l_name == 'quit':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print('\nhello, ' + formatted_name + "!")