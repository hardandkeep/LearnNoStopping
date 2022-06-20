#使用方法sort()对列表进行永久性排序

cars = ['bmw','aud','toy','sub']
cars.sort()    #这会使列表按照字母表中顺序进行排序
print(cars) 
    #向括号中传递reverse=True参数
cars.sort(reverse=True)    #这会使列表按照字母表中的相反顺序进行排序
print(cars)

print(help(cars.sort))


#使用函数sorted()对列表进行暂时性排序

cars = ['bmw','aud','toy','sub']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))    #暂时性排列是sorted(将列表放到里面)
                       #永久性排列是 列表.sort()或传递参数



#运用方法.reverse()倒着打印列表

cars = ['bmw','aud','toy','sub']
print(cars)
cars.reverse()    #这句语句会反转列表,而不是按照字母表的顺序进行反转,切记
print(cars)




#运用函数len()确定列表的长度
cars = ['bmw','aud','toy','sub']
print(len(cars))



#list.copy()返回列表的浅拷贝。相当于 a[:]


#list.index(x,start,end)
'''
返回列表中第一个值为 x 的元素的零基索引。未找到指定元素时，触发 ValueError 异常
可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数
'''












