#多线程
    #为什么使用多线程?
        #--->进程是分配资源的最小单位，一旦创建一个进程就会分配一定的资源
        #线程是程序执行的最小单位,实际上进程只负责分配资源，而利用这些资源执行程序的是线程，也就是说进程是线程的容器,
          #一个进程中最少有一个线程来负责执行程序,同时线程自己不拥有系统资源，只需要一点儿在运行中必不可少的资源,
          #但它可与同属一个进程的其他线程共享进程所拥有的全部资源,就像通过QQ软件(一个进程)打开两个窗口(两个线程)跟两个人聊天一样,
          #实现多任务的同时也节省了资源

#多线程的作用:
'''
例如:
def func1():
    print("任务1")

def func2():
    print("任务2")

func1()
func2()

当运行程序之后，在进程中默认会有一个线程用来执行程序,这个线程称之为主线程
主线程会按照顺序去先执行func1,在执行func2

而多线程:在进程中创建一个新的线程，这个线程称之为子线程
此时,主线程执行func1，子线程执行func2    (它们是同时执行)
'''


#多线程完成多任务
    #线程的创建步骤
'''
    1.导入线程模块:import threading
    2.通过现场类创建线程对象:线程对象 = threading.Thread(target=任务名)
        参数:
        #target执行的目标任务，这里指的是函数名
        #name进程名，一般不用设置
        #group进程组，目前只能使用None
    3.启动线程执行任务:线程对象.start()
'''
import threading
import time

def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(1)
#跳舞
def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(1)
    res = "我"
    return res

if __name__ == "__main__":

    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()




# 线程执行带有参数的进程
# args:以元组的方式给执行任务传参(只能有一个元组，按顺序传参)
'''
    import threading
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

        sing_thread = threading.Thread(target=sing,args=(3,))
        dance_thread = threading.Thread(target=dance,args=(3,))

        sing_thread.start()
        dance_thread.start()
'''
# kwargs:以字典方式给执行任务传参(在传入参数的时候只需要key值与形参一样，不需要按顺序)
'''
    import threading
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

        sing_thread = threading.Thread(target=sing,kwargs={"num":3})
        dance_thread = threading.Thread(target=dance,kwargs={"num":3})

        sing_thread.start()
        dance_thread.start()
'''


#主线程和子线程的结束顺序:主线程会等待所有子线程执行结束之后才会结束
    #设置为主线程关闭,子进程会自动销毁---子进程守护模式
'''
设置守护主线程:
------法一:在每个子线程对象创建的后面,再写上,子线程对象.daemon = True 那么这个子线程就会守护主线程
------法二:在子线程启动之前,写上,子线程对象.thread.setDaemon(True)
------在主线程直接退出的时候，子线程如果还在运行，那么直接销毁
'''


#线程之间的执行是无序的



