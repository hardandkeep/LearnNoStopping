
'''
#文件的打开与关闭

#这会在这个文件目录下创建文件
#如果这个文件不存在就新建
#存在的话会覆盖

f = open('test.txt','w')
#这里面的w是'写'
#即：有w，r，wb，rb等等，w为写，r为读，wb为以二进制写入，rb为以二进制来读
#w，r一个也没写时，默认为r读
f.close()  #关闭文件
'''

'''
#文件的写入
f = open("test.txt","w")

f.write('hello world!')  #将字符串写入文件中

f.close()
'''
#y养成好习惯：有文件关闭的语句

#读取操作
'''
f = open("test.txt","w")

f.write('hello world!')  #将字符串写入文件中

f.close()


f = open("test.txt","r")  #只读模式

content = f.read(5)   #读前五个字节
print(content)

content = f.read(6)  #读从第五开始的后面六个
print(content)    
                  #这之中，要知道指针的概念，读几个就移动几个
f.close()
'''
'''
#更快的读取
f = open("test.txt","r")  #只读模式

content = f.readlines()
print(content)

f.close()
'''
'''
一行一行的读
f = open("test.txt","r")

content = f.readline()
print("1:%s"%content)

content = f.readline()
print("2:%s"%content)

f.close()
'''

'''
#重命名:需要引入os中的rename(需要修改的文件名，新的文件名)
import os

os.rename("test.txt","new_test.txt")
'''


fp = open("txt.csv", 'w')
fp.write(','.join(['我', '爱', '你']))
fp.close()

fp = open('txt.csv', 'r')
line = fp.readline()
print(line)
fp.close()


# os模块里面有对文件操作的很多方法......


# 注：别乱用代码删文件，妈蛋路径一写错，不小心把电脑系统里面的文件都删除了就尴尬了

