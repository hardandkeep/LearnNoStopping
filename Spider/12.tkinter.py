import tkinter as tk#后面多加的as可以用tk代替tkinter来写接下来的代码

window = tk.Tk()#创建主窗口
window.title('我是一个标题')#窗口的名字/标题
window.geometry('200x100')#窗口的长宽（里面的x就是英文字母x）

var = tk.StringVar()

#在windo里面在弄出一块标签，并传入所需要的参数
#不可变的文本-text
#可变的文本--textvariable，这不就是英语的翻译意思？
l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
l.pack()#放置这个Label---place()是精确位置的放置

def hit_me():
    on_hit = False
    if on_hit == False:
        on_hit=True
        var.set('you hit me')
    else:
        var.set('')

btn = tk.Button(window,text='hit me',width=15,height=2,command=hit_me)#command=函数名,只要在窗口一点击这个hit_me就会运行这个函数
btn.pack()

window.mainloop()#运行