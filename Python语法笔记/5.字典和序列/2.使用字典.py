#1.访问字典中的值：print(字典名['键名'])
human = {'man':'woman'}
print(human['man'])

#2.添加键-值对：直接语句 字典名['键名'] = 值名 即可添加到字典中键-值对
human = {}
human['man'] = 'woman'
print(human)

#3.修改字典中的值：只需指定字典名，用方括号括起的键以及与该键相关联的新值即可
human = {'man':'woman'}
human['man'] = 'new_woman'
print(human)

#4.删除键-值对：直接语句，del 字典名['键名']即可
del human['man']
print(human)

#5.由类似对象组成的字典 