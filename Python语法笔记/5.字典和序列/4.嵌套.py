#有时候需要将一系列字典储存在列表中，或者将列表作为值存在字典中，这称为嵌套
#我们可以在列表中嵌套字典，可以在字典中嵌套字典，亦可以在字典中嵌套字典
#第二局其实就是，字典可以作为列表的元素，而列表亦可以作为字典的值，甚至字典可以作为另一个字典的值

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]   #它们都是一个个变量，不需要加单(双)引号
for alien in aliens:
    print(alien)


#自动创建
#创建一个用于储存外星人的列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'solw'}
    aliens.append(new_alien)

#显示前五个外星人
for new_alien in aliens[:5]:
    print(new_alien)
print('...')

#外星人总数
print("total is ",str(len(aliens)))








#创建一个用于储存外星人的列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'solw'}
    aliens.append(new_alien)

#修改前三个外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'middle'

#显示前五个外星人
for new_alien in aliens[:5]:
    print(new_alien)
print('...')

#外星人总数
print("total is ",str(len(aliens)))



#创建一个用于储存外星人的列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'solw'}
    aliens.append(new_alien)

#修改前三个外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'middle'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

#显示前五个外星人
for new_alien in aliens[:5]:
    print(new_alien)
print('...')

#外星人总数
print("total is ",str(len(aliens)))





#在字典中储存列表：有时候需要将列表存储在字典中，而不是将字典存储在列表
'''
例如，你如何描述顾客点的披萨呢？
如果使用列表，只能存储要添加的披萨配料，但如果使用字典，就不仅可在其中包含配料列表了，还可以包含其他有关披萨的描述

在下面的示例中，存储了披萨的两方面的信息：外皮类型和配料列表
其中的配料列表是一个与键toppings相关联的值
要访问该列表，我们使用字典名和键toppings，就像访问字典中的其他值一样
这将返回一个列表，而不是单个值
'''
#存储所点的披萨信息
pizza = {'crust':'thick','toppings':['mushrooms','extra cheese'],}

#概述所点的披萨
print('you ordered a ' + pizza['crust'] + '-crust pizza' + 'withh the follwing toppings:')

for topping in pizza['toppings']:
    print('\t',topping)



#在字典中存储字典


