'''
map 函数的使用形式如下：
map(function, sequence)
解释：对 sequence 中的 item 依次执行 function(item)，并将结果组成一个 List返回
'''

def square(x):
    return x * x

r = map(square, [1,2,3,4])
print(r)

r = map(lambda x: x*x, [1,2,3,4])
print(r)

r = map(str, [1,2,3,4])
print(r)

r = map(int, ['1','2','3','4'])
print(r)


def double(x):
    return 2 * x

def triple(x):
    return 3 * x

def square(x):
    return x * x

funcs = [double, triple, square]  # 列表元素是函数对象

# 相当于 [double(4), triple(4), square(4)]
value = list(map(lambda f: f(4), funcs))

print(value)


'''
reduce 函数的使用形式如下：

reduce(function, sequence[, initial])
解释：先将 sequence 的前两个 item 传给 function，
即 function(item1, item2)，函数的返回值和 sequence 的下一个 item 
再传给 function，即 function(function(item1, item2), item3)，
如此迭代，直到 sequence 没有元素，如果有 initial，则作为初始值调用。
'''

#reduce不知道为什么无法用


'''
filter

filter 函数用于过滤元素，它的使用形式如下：

filter(function, sequnce)
解释：将 function 依次作用于 sequnce 的每个 item，
即 function(item)，将返回值为 True 的 item 
组成一个 List/String/Tuple (取决于 sequnce 的类型，
python3 统一返回迭代器) 返回。
'''

even_num = list(filter(lambda x: x % 2 == 0, [0,1,2,3,4]))
print(even_num)

r = list(filter(lambda x: x >= 2, [1,2,3,4]))
print(r)


#sorted(*args, **kwargs):
'''最基础的就是传入一个列表,而后按ascii大小来排序,想反序使用reverse=True'''
'''但是sorted()亦可以根据自己写的或其他特定函数进行按需排序'''
'''例如传入一个绝对值函数参数,先将列表a中的元素绝对值之后在进行排序,而后在返回排序完之后的列表(元素还都是原来的哦!)'''
a = [1,2,4,3,-10,-50,49,22]
k = sorted(a,key=abs)
print(k)










