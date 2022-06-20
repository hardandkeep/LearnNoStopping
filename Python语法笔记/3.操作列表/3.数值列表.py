#创建数值列表
    #列表非常适合存储数字的集合

#使用函数range()
for number in range(1,9):
    print(number)
    #从结果来看，该循环并不会输出数字9，因此假如要输出1到5，那么就要range(1,6)：
    #range()函数可以生成一系列的数字



#使用函数range()来创建数值列表
    #要构建数值列表，可以使用list()将range()的结果直接转换成为列表
    #直接将range()当作list()的参数
numbers = list(range(1,9))
print(numbers)
    #使用range()函数还可以指定步长，range(起始值，终点指，步长值)
even_numbers = list(range(1,9,2))
print(even_numbers)




#亦可以使用方法append()来创建数值列表
numbers = []
for value in range(1,9):
    number = value**2
    numbers.append(number)
#或者number.append(value**2)
print(numbers)



numbers = []
for number in range(1,10):
    numbers.append(number)
print(numbers)
#列表解析时




numbers = [numbers.append(number) for number in range(1,10)]
print(numbers)





numbers = []
for number in range(1,10):
    numbers.append(number)
print(numbers)