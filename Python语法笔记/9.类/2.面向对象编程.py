#self是什么?
#self是当一个对象的方法被调用的时候,对象会将自身作为第一个参数传给self参数(调用的时候是看不见self),python就知道是那个对象在调用方法了
'''例如下例'''

class Ball:
    def setName(self,name):
        self.name = name

    def kick(self):
        print("我是%s,该死的,谁踢我"%self.name)

a = Ball()
a.setName("球A")
b = Ball()
b.setName("球B")
c = Ball()
c.setName("球C")

a.kick()
b.kick()
c.kick()
'''
运行会发现同样是调用kick方法,但是对象全都不一样
这是因为当实例化了a并且设置名字之后,调用a.kick()方法的时候,
a对象本身会传入到kick括号中去,只是因为这个参数(self)是隐藏的而已
此时在对应前面的self是什么?进行理解
'''

#Python魔法方法:__init__(self),它会在创建对象(初始化)的时候自动被调用
#即,实例化类的时候是可以传入参数的,而传入的参数就会到__init__(self,parms1,parms2,..)方法的参数中
'''例如对上面的Ball对象进行改进'''

class Ball:
    def __init__(self,name):
        self.name = name

    def kick(self):
        print("我是%s,该死的,谁踢我"%self.name)

a = Ball("球A")
b = Ball("球B")
c = Ball("球C")
a.kick()
b.kick()
c.kick()
'''
这里就是直接在创建类的时候传入name参数,
而传入的name参数会传入到init方法中进行赋值操作,
记住,实例化类的时候__init__(self)会自动运行,进行初始化的属性操作,
'''

#公有和私有:默认时类的属性和方法是公有的,但有时需要私有...
#默认公有时可以从外部直接访问,但是私有时从外部无法访问(python这边是隐藏了而已,其实还是可以从外部访问的)
'''例如下例'''

class Person:
    name = "李学红"

p = Person()
print(p.name)

class Person:
    __name = "李学红"

    def get_name(self):
        return self.__name
p = Person()
#p.__name 运行这句时会报错:AttributeError: 'Person' object has no attribute '__name'
#此时只能从类内部访问,你可以在类里面写个getname方法
print(p.get_name())
#但是其实python只是把名字给改了而已,把__name改成了_Person__name,即"_类名__隐藏名"

print(p._Person__name) #即可访问

