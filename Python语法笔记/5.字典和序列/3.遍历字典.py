#遍历字典：for key,value in 字典名.方法items():即可
human = {'man':'woman','new_man':'new_woman'}
for k,v in human.items():
    print(k,v)

   #遍历字典时需要用到方法items()

#遍历字典中的所有键：使用方法keys()
for k in human.keys():
    print(k)

   #遍历字典中的所有键时需要用到方法keys()

#按顺序来遍历字典中的所有键：使用方法sorted()去括起来字典名.方法()
for k in sorted(human.keys()):   #字母表顺序
    print(k)

#遍历字典中的所有值：使用方法values()
for v in human.values():
    print(v)

    #遍历字典中的所有值时需要用到方法values()