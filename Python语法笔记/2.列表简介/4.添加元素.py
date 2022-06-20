cars = ['terl','cannoable','redline','specialized']
print(cars)



#使用方法.append()将其添加到列表的最后面
cars.append('lambogini')
print(cars)


#使用方法.extend(iterable)来拓展列表
#用可迭代对象的元素扩展列表。相当于 a[len(a):] = iterable 。
list1 = [1,2,3]
list2 = [4,5,6]
#list1.extend(list2) == list1[len(list1):] = list2
#得list1 = [1, 2, 3, 4, 5, 6]



#使用方法insert()可以在列表任何地方插入元素
cars.insert(0,'maikailun')    #此时迈凯伦会被插入到第一个,因为0就是指第一
print(cars)
cars.insert(1,'dier')    #此时第二会被插入到第二个,因为1指的是第二
print(cars)




my_family = ["father",'mother','first sister','second sister','the smallest boy']
my_family.append("dead dog")
print(my_family)

my_family.insert(6,"dead dog")
print(my_family)