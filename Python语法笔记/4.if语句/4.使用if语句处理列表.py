#使用if语句处理列表

#检查特殊元素：利用if语句来处理一些特殊情况
cars = ['lanbogini','xuefulan','baoma']
'''
for car in cars:
    print('I superly like this',car)
'''

for car in cars:
    if car == 'baoma':
        print('this',car,'is not good!')
    else:
        print('I superly like this',car)





#确定列表不是空的

cars = []

if cars:
    for car in cars:
        print('your garage has a ',car)
    print('I will take a car to find you')
else:
    print('the garage has not a car ')
    #在这边，直接拿列表来当条件，如果列表为空则为false，列表不为空则为true




#使用多个列表

car_faculty_available = ['lanbogini','xuefulan','baoma','daben','maikailun','wulinhongguang']
car_faculty_requested = ['lanbogini','xuefulan','qice','qiche','wudi']

for car_requested in car_faculty_requested:
    if car_requested in car_faculty_available:
        print('this',car_requested,'can sell for you')
    else:
        print('sorry,now,we do not have it,we can hurry to produce this',car_requested)