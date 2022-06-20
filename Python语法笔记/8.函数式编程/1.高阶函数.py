'''一个函数接收另一个函数作为参数，这种函数称之为高阶函数'''

'''
函数可被变量进行指定(例如:f=abs()),指向函数的变量可做为参数传入函数,此变量传入的函数便是高级函数
由此,函数可做为参数传入函数,注意:abs和abs(),前者是指向函数本身,后者则是调用此函数
python提供了四个内置的高级函数:map(),filter(),sorted()
'''
#map(func, *iterables):
'''其中func为函数名作为参数,iterables为可迭代对象,*表示可传入多个此参数'''
'''此函数可根据自己定制的函数去处理单个或多个可迭代对象中的元素'''

'''例如'''
def sum(x,y):
    return x+y

a = [1,2,3]
b = [-1,-2,-3]

s = map(sum,a,b)
print(list(s))


#filter(function or None, iterable):
'''func和iterable见上述,filter()根据func的具体情况来过滤掉可迭代对象中的元素'''
'''True为不过滤,False为过滤 '''
a = [0,1,' ']
def rem(i):
    if i != ' ':
        return True

d = filter(rem,a)
print(list(d))

def sum(x,y):
    return x+y

a = [1,2,3]
b = [-1,-2,-3]
print(sum(a,b))







