# 通过key来排序
def sorted_dict_key(dicts):
    items = dicts.items()
    items_li = [[key, value] for key, value in items]
    items_li.sort()
    return items_li


dict_exp1 = {3: 'www', 2: 'ttt', 5: 'yyy'}
sorted_dict = sorted_dict_key(dict_exp1)
print(sorted_dict)


# sort只能对列表排序，sorted是对任何可迭代对象
sort_li = [(key, dict_exp1[key]) for key in sorted(dict_exp1)]
print(sort_li)


# 通过value来排序
def sorted_dict_value(dicts):
    items = dicts.items()
    items_li = [[value, key] for key, value in items]
    items_li.sort()
    return items_li


dict_exp2 = {'www': 3, 'ttt': 2, 'yyy': 5}
sorted_dict = sorted_dict_value(dict_exp2)
print(sorted_dict)


# sort只能对列表排序，sorted是对任何可迭代对象
sort_li = [(dict_exp2[key], key) for key in sorted(dict_exp2)]
print(sort_li)
