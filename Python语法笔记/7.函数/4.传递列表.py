'''
你会经常发现，向函数传递列表很有用，这种列表包含的可能是名字，数字或是更复杂的对象（如字典）
将列表传递给函数后，函数就能直接访问其内容
下面使用函数来提高处理列表的效率

假如有一个用户列表，我们要问候其中的每位客户。下面的示例将一个名字列表传递给一个名为greet_users()的函数
这个函数问候列表中的每个人
'''

#传递列表：实际上就是把列表当作实参传递
def greet_users(names):
    '''向列表中的每位用户都发出简单的问候'''
    for name in names:
        masg = 'Hello,' + name.title() + '!'
        print(masg)
usernames = ['ligouxue','lixuelian','lixuehong']
greet_users(usernames)     #效率的确挺高


#在函数中修改列表：在列表传递给函数后，函数就可以对其进行修改，在函数中对这个列表所作出的人和修改都是永久性的
    #例如，来看一家为用户提交的设计制作3D打印模型的公司，将需要打印的设计存储在一个列表中，打印后移动到另一个列表中
   #不使用函数时：
  #首先创建一个列表，其中包含一些需要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
  #模拟打印每个设计，直到其中没有未打印的设计为止
  #打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
      
    #模拟根据设计制作3D打印模型的过程
    print('Printing model:' , current_design)
    completed_models.append(current_design)
  #显示打印好的所有模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model)


#为重新组织起这些代码，我们可以编写两个函数，每个函数都做一件具体的工作
def print_models(unprinted_designs,completed_models):
    '''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟根据设计制作3D打印模型的过程
        print('Printing models:',current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


#禁止函数修改列表：看数129——————————上面的也看书127


