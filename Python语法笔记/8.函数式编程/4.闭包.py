'''
闭包
在 Python 中，函数也是一个对象。因此，我们在定义函数时，可以再嵌套定义一个函数，并将该嵌套函数返回，比如：
'''
from math import pow

def make_pow(n):
    def inner_func(x):     # 嵌套定义了 inner_func
        return pow(x, n)   # 注意这里引用了外部函数的 n
    return inner_func      # 返回 inner_func
#上面的代码中，函数 make_pow 里面又定义了一个内部函数 inner_func，然后将该函数返回。因此，我们可以使用 make_pow 来生成另一个函数：

pow2 = make_pow(2)  # pow2 是一个函数，参数 2 是一个自由变量
print(pow2)
print(pow2(6))

#我们还注意到，内部函数 inner_func 引用了外部函数 make_pow 的自由变量 n，这也就意味着，当函数 make_pow 的生命周期结束之后，n 这个变量依然会保存在 inner_func 中，它被 inner_func 所引用。

del make_pow         # 删除 make_pow
#pow3 = make_pow(3) #无法调用

print(pow2(9))   # pow2 仍可正常调用，自由变量 2 仍保存在 pow2 中
#像上面这种情况，一个函数返回了一个内部函数，该内部函数引用了外部函数的相关参数和变量，我们把该返回的内部函数称为闭包（Closure）。

#在上面的例子中，inner_func 就是一个闭包，它引用了自由变量 n。


'''
闭包的作用

闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在。
闭包在运行时可以有多个实例，即使传入的参数相同。
'''

#pow_a = make_pow(2)
#pow_b = make_pow(2)
#pow_a == pow_b

#利用闭包，我们还可以模拟类的实例。
#这里构造一个类，用于求一个点到另一个点的距离：

from math import sqrt

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def get_distance(self, u, v):
        distance = sqrt((self.x - u) ** 2 + (self.y - v) ** 2)
        return distance

pt = Point(7, 2)        # 创建一个点
pt.get_distance(10, 6)  # 求到另一个点的距离

#用闭包来实现：

def point(x, y):
    def get_distance(u, v):
        return sqrt((x - u) ** 2 + (y - v) ** 2)

    return get_distance

pt = point(7, 2)
pt(10, 6)


'''
小结

闭包是携带自由变量的函数，即使创建闭包的外部函数的生命周期结束了，闭包所引用的自由变量仍会存在。
闭包在运行可以有多个实例。
尽量不要在闭包中引用循环变量，或者后续会发生变化的变量。
'''


def outer(a):
    print('--')
    def inner(b): #python会读取这个定义函数但不会执行
        print(a+b)
    return inner #需要把内层函数return给外层

out1 = outer('卷')
out2 = outer('废')
out1('王')
out2('物')














