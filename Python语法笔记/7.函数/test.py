class Turtle:

    def __init__(self, color, leg, weight):
      '''属性'''
      self.color = color
      self.leg = leg
      self.weight = weight

    '''方法'''
    def Tcolor(self):
        print("我的颜色是{}".format(self.color))


    def Tleg(self):
        print("我有{}条腿".format(self.leg))


    def Tweight(self):
        print("我有{}斤".format(self.weight))


whiteTurtle = Turtle("白色", "四", "三十")
whiteTurtle.Tcolor()
whiteTurtle.Tleg()
whiteTurtle.Tweight()

