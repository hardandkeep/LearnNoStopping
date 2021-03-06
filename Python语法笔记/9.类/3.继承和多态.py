#继承和多态

#在面向对象编程中，当我们已经创建了一个类，而又想再创建一个与之相似的类，比如添加几个方法，或者修改原来的方法，这时我们不必从头开始，可以从原来的类派生出一个新的类，我们把原来的类称为父类或基类，而派生出的类称为子类，子类继承了父类的所有数据和方法。

#让我们看一个简单的例子，首先我们定义一个Animal类：

class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


#现在，我们想创建一个Dog类，比如：

class Dog(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('WangWang.., I am %s. ' % self.name)


#可以看到，Dog类和Animal类几乎是一样的，只是greet方法不一样，我们完全没必要创建一个新的类，而是从Animal类派生出一个新的类：

class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s. ' % self.name)


#Dog类是从Animal类继承而来的，Dog类自动获得了Animal类的所有数据和方法，而且还可以对父类的方法进行修改，我们看看使用：

animal = Animal('animal')  # 创建 animal 实例
animal.greet()

dog = Dog('dog')  # 创建 dog 实例
dog.greet()

#我们还可以对Dog类添加新的方法：

class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s. ' % self.name)

    def run(self):
        print('I am running.I am running')


dog = Dog('dog')
dog.greet()
dog.run()

#多态:
#多态的概念其实不难理解，它是指对不同类型的变量进行相同的操作，它会根据对象（或类）类型的不同而表现出不同的行为。
#事实上，我们经常用到多态的性质，比如：

print(1 + 2)
print('a' + 'b')

#可以看到，我们对两个整数进行 + 操作，会返回它们的和，对两个字符进行相同的 + 操作，会返回拼接后的字符串。也就是说，不同类型的对象对同一消息会作出不同的响应。

#再看看类的例子：

class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s.' % self.name)


class Cat(Animal):
    def greet(self):
        print('MiaoMiao.., I am %s' % self.name)


def hello(animal):
    animal.greet()


dog = Dog('dog')
hello(dog)

cat = Cat('cat')
hello(cat)

#可以看到，cat和dog是两个不同的对象，对它们调用greet方法，它们会自动调用实际类型的greet方法，作出不同的响应。这就是多态的魅力。

'''
小结:
继承可以拿到父类的所有数据和方法，子类可以重写父类的方法，也可以新增自己特有的方法。
有了继承，才有了多态，不同类的对象对同一消息会作出不同的相应。
'''