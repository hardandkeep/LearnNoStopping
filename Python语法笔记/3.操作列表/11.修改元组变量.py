#虽然不能修改元组的元素，但可以给存储元组的变量赋值，因此如果要修改前述矩形的长宽，可以从新定义整个元组
dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)