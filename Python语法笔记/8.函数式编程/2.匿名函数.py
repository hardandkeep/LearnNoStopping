'''使用关键字lambda来创建一个匿名函数---没有名字的函数'''
'''它的形式：lambda 参数: 表达式'''

#例如下面这两个函数是等效的
def double(x):
    return 2 * x

lambda x: 2 * x

#调用匿名函数
print((lambda x: 2 * x )(8))

#它可以赋值给另一个变量
fuc = lambda x: 2 * x
print(fuc(8))

'''
lambda 函数一般适用于创建一些临时性的，小巧的函数。
比如上面的 double 函数，我们当然可以使用 def 来定义，
但使用 lambda 来创建会显得很简洁，尤其是在高阶函数的使用中。
'''
def func(g,arr):
    return [g(x) for x in arr]

lst = func(lambda x: x + 1, [1,2,3,4])

print(lst)

'''
小结：
匿名函数本质上是一个函数，没有函数名称，因此使用匿名函数不用担心函数名冲突；
匿名函数一般适用于创建一些临时性的，小巧的函数；
'''