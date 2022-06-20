'''
#整数
three = 1+2
print(1+2)
print(three)

print(3-2)
print(2*3)
print(3/2)

print(3**2)
print(3**3)
print(10**6)

#浮点数:python将带有小数点的数字都称为浮点数
print(0.1+0.1)
print(0.2+0.2)
print(2*0.1)
print(2*0.2)
#结果包含的小数位数可能是不确定的
print(0.1+0.2)
print(3*0.1)
#通过上面的输出会发现,有两个算出来不准,有多余的小数,所有的语言都存在这种问题
#在后面会解决此问题

#使用函数str()避免类型错误(即字符串和数字的区别要做好)
age = 23
#message = 'Happy' + age + 'rd birthday!'
#把上一行的#去掉就会出现类型错误,message中包含的是字符串,而age=23是数字,为int类型的整数变量
message = 'Happy ' + str(age) + 'rd birthday!'
#此时str()将age = 23 转换成了字符串类型
print(message)


print('-_-'*8)


age = input("what your age is :")
print(age)

age = int(input("what your age is :"))
if age >= 18:
    print("you are a rope man")
else:
    print("you are too young")
'''
numbers = list(range(1,9))
print(numbers)