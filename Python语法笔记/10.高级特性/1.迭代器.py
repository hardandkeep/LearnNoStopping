#迭代器(Iterator)

'''
对于一个可迭代对象，我们可以使用iter()来将其变成迭代器
'''
exL = [1,2,3,4,5] #可迭代对象
ex = iter(exL) #将其转换为迭代器
print(next(ex))
print(next(ex))
print(next(ex))
print(next(ex))




'''
迭代和可迭代

可以使用for 循环进行迭代的对象，就是可迭代对象，它的定义如下：

含有__iter__()方法或__getitem__()方法的对象称之为可迭代对象。
使用isinstance()进行判断是否可迭代：

>> > from collections import Iterable

>> > isinstance((), Iterable)  # 元组
True
>> > isinstance([], Iterable)  # 列表
True
>> > isinstance({}, Iterable)  # 字典
True
>> > isinstance('abc', Iterable)  # 字符串
True
>> > isinstance(100, Iterable)  # 数字
False
可见，我们熟知的字典（dict）、元组（tuple）、集合（set）和字符串对象都是可迭代的。
'''

'''
迭代器

现在，让我们看看什么是迭代器（Iterator）。上文说过， ** 迭代器是指遵循迭代器协议（iterator
protocol）的对象。 ** 从这句话我们可以知道，迭代器是一个对象，但比较特别，它需要遵循迭代器协议，那什么是迭代器协议呢？

** *迭代器协议（iteratorprotocol） ** *是指要实现对象的__iter()__和next()方法（注意：Python3要实现__next__()方法），
其中，__iter()__方法返回迭代器对象本身，next()方法返回容器的下一个元素，在没有后续元素时抛出StopIteration异常。
接下来讲讲迭代器的例子，有什么常见的迭代器呢？列表是迭代器吗？字典是迭代器吗？我们使用
isinstance()来判断是否是迭代器
>> > from collections import Iterator
>> >
>> > isinstance((), Iterator)
False
>> > isinstance([], Iterator)
False
>> > isinstance({}, Iterator)
False
>> > isinstance('', Iterator)
False
>> > isinstance(123, Iterator)
False

斐波那契数列迭代器

现在，让我们来自定义一个迭代器：斐波那契（Fibonacci）数列迭代器。
根据迭代器的定义，我们需要实现__iter()__和next()方法（在Python3中是__next__()方法）。先看代码：
# -*- coding: utf-8 -*-
from collections import Iterator

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 返回迭代器对象本身
    def __iter__(self):
        return self

    # 返回容器下一个元素
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


def main():
    fib = Fib()  # fib 是一个迭代器
    print('isinstance(fib, Iterator): ', isinstance(fib, Iterator))

    for i in fib:
        if i > 10:
            break
        print(i)

if __name__ == '__main__':
    main()
    
在上面的代码中，我们定义了一个Fib类，用于生成Fibonacci数列。
在类的实现中，我们定义了__iter__方法，它返回对象本身，这个方法会在遍历时被Python内置的iter()函数调用，返回一个迭代器。
类中的next()方法用于返回容器的下一个元素，
当使用for 循环进行遍历的时候，就会使用 Python 内置的 next() 函数调用对象的 next 方法（在 Python3 中是 __next__ 方法）对迭代器进行遍历。

运行上面的代码，可得到如下结果：

isinstance(fib, Iterator): True
1
1
2
3
5
8
'''

'''
小结:

元组、列表、字典和字符串对象是可迭代的，但不是迭代器，
不过我们可以通过iter()函数获得一个迭代器对象
Python的for 循环实质上是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的；
自定义迭代器需要实现对象的__iter()__和next()方法（注意：Python3要实现__next__()方法），
其中，__iter()__方法返回迭代器对象本身，next()方法返回容器的下一个元素，在没有后续元素时抛出StopIteration异常。
'''