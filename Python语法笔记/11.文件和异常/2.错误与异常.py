# 为了防止在程序运行当中，程序报错引发中断(崩溃)，引入错误与异常检查

# 例如我们去读一个不存在的文件
'''
print("--test--1--")

f = open("123.txt","r")

print("--test--2--")
'''
# 你会发现，这个到第七行程序崩溃，后面的print无法执行


# 此时用try
'''
try：
    print("--test--1--")

    f = open("123.txt","r")

    print("--test--2--")

except IOError:   #文件没找到属于IO异常（输入输出异常）
    pass        #捕获异常后，执行的代码
                #发生的错误需要与你去防止崩溃写的异常类型相对应
'''


'''
#当有两个异常的时候
try：
    print("--test--1--")
    f = open("123.txt","r")
    print("--test--2--")

    print(num)
except (NameError,IOError):   #将可能产生的异常类型，都放到这个小括号中
    pass
'''

'''
#获取信息描述
try：
    print("--test--1--")
    f = open("123.txt","r")
    print("--test--2--")

    print(num)
except (NameError,IOError) as result:  #result也可以换成别的
    print("产生异常了") 
    print(result)
'''


#简单粗暴型直接捕获所有的异常------这个最舒服的-------
try:
    pass
except Exception as result:
    pass


try:
    pass

except:
    pass

finally:
    pass

#try的嵌套