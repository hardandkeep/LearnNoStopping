cars = ['terl','cannoable','redline','specialized']
print(cars)




#使用del语句来删除列表中的元素:需要知道所需删除的元素在列表中的位置------(最简单最普遍的一种删除元素的方法)
#如果知道所需删除元素的位置,使用del语句
del cars[0]    #会删除列表中的第一个元素
print(cars)




#使用方法.pop()删除列表末尾的元素-----(写循环的时候经常使用)
poped_cars = cars.pop()    #列表中的最后一个元素被删除,但是删除的元素被赋予给了poped_cars
print(poped_cars)          #输出被删除的最后一个元素
print(cars)                #输出被删除最后一个元素之后的列表
#其中,第一第二句话等于print(car.pop()),既会删除最后一个元素,又会输出被删除的元素

    #利用pop()来弹出列表中任何位置的元素
car = cars.pop(0)
print("I hate a car,that is "+ car +"!")




#使用方法.remove()来根据值来删除元素------(最直观的一种删除元素的方法)
cars.remove('cannoable')
print(cars)




#使用方法.clear()删除列表里的所有元素，相当于 del a[:]


