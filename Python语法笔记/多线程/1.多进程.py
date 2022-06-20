#多任务介绍
    #多任务是指在同一时间内执行多个任务
        #例如:电脑在下载文件的时候同时下载多个文件，又比如同时打开很多软件......

    #并发:在一段时间内交替去执行多个任务
        #例如：对于单核cpu处理多任务，操作系统轮流让各个人物交替执行

    #并行:在一段时间内真正的同时一起执行多个任务
        #对于多核cpu处理多任务，操作系统会给cpu的每个内核安排一个执行的任务，多个内核是真正的一起同时执行多个任务


#进程介绍
    #进程是资源分配的最小单位，它是操作系统进行资源分配和调度运行的基本单位，通俗理解:一个正在运行的程序就是一个进程，例如正在运行的qq，微信等，它们都是一个个的进程

def func1():
    print("1")

def func2():
    print("2")

#func1()
#func2()
'''
上述程序在运行之后,程序会默认创建一个进程，这个默认创建的进程我们称之为主进程(先执行func1，在执行func2)

而使用多进程则是:程序运行后又创建了一个进程，这个新创建的进程我们称之为子进程(主进程执行func1，子进程执行func2)
这样就达到了同时执行func1和func2了
'''

#多进程完成多任务
    #进程的创建步骤:
'''
1.导入进程包:
import multiprocessing

2.通过进程类创建进程对象:
进程对象=multiprocessing.Process(target=任务名)
    参数:
        #target执行的目标任务，这里指的是函数名
        #name进程名，一般不用设置
        #group进程组，目前只能使用None
3.启动进程执行任务:
进程对象.start()
'''
#例如:
'''
import multiprocessing
import time
#唱歌
def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(1)
#跳舞
def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(1)

if __name__ == "__main__": #没用这个语句就报错了，以后记得使用

    sing_processing = multiprocessing.Process(target=sing)
    dance_processing = multiprocessing.Process(target=dance)

    sing_processing.start()
    dance_processing.start()
'''

#进程执行带有参数的进程
    #args:以元组的方式给执行任务传参(只能有一个元组，按顺序传参)
'''
    import multiprocessing
    import time
    #唱歌
    def sing(num):
        for i in range(num):
            print("唱歌...")
            time.sleep(1)
    #跳舞
    def dance(num):
        for i in range(num):
            print("跳舞...")
            time.sleep(1)
    
    if __name__ == "__main__": #没用这个语句就报错了，以后记得使用--->这个是主进程入口==主程序入口
    
        sing_processing = multiprocessing.Process(target=sing,args=(3,))
        dance_processing = multiprocessing.Process(target=dance,args=(3,))
    
        sing_processing.start()
        dance_processing.start()
'''
    #kwargs:以字典方式给执行任务传参(在传入参数的时候只需要key值与形参一样，不需要按顺序)
'''
    import multiprocessing
    import time
    #唱歌
    def sing(num):
        for i in range(num):
            print("唱歌...")
            time.sleep(1)
    #跳舞
    def dance(num):
        for i in range(num):
            print("跳舞...")
            time.sleep(1)

    if __name__ == "__main__": #没用这个语句就报错了，以后记得使用

        sing_processing = multiprocessing.Process(target=sing,kwargs={"num":3})
        dance_processing = multiprocessing.Process(target=dance,kwargs={"num":3})

        sing_processing.start()
        dance_processing.start()
'''


#获取进程编号
    #第一种获取进程编号的方法:
        #获取当前进程编号:
            #os.getpid()

    #第二种获取进程编号的方法:
        #获取当前父进程的编号:
            #os.getppid()


import multiprocessing
import time
import os

# 唱歌
def sing(num):
    print("获取当前唱歌进程的编号:",os.getpid())
    print("获取当前唱歌主进程的编号:", os.getppid())
    for i in range(num):
        print("唱歌...")
        time.sleep(1)


# 跳舞
def dance(num):
    print("获取当前跳舞进程的编号:", os.getpid())
    print("获取当前跳舞主进程的编号:", os.getppid())
    for i in range(num):
        print("跳舞...")
        time.sleep(1)

#主进程
if __name__ == "__main__":  # 没用这个语句就报错了，以后记得使用
    print("主进程的pid:",os.getpid())
    #创建子进程对象并指定执行的任务名
    sing_processing = multiprocessing.Process(target=sing, args=(3,))
    dance_processing = multiprocessing.Process(target=dance, args=(3,))

    #启动子进程并执行任务
    sing_processing.start()
    dance_processing.start()


#进程的注意点
'''
主进程会等待所有子进程执行结束再结束:想想QQ
------因此,在创建多任务的时候一定要有主进程,然后在创建多个子进程

设置守护主进程:
------在每个子进程对象创建的后面,再写上,子进程对象.daemon = True 那么这个子进程就会守护主进程  
------在主进程直接退出的时候，子进程如果还在运行，那么直接销毁
'''


#实例:高并发的文件copy器