#使用方法来修改字符串的大小写
#方法出现在这个变量的后面

#方法有:.title().upper().lower()

#让python对变量执行方法title()指定的操作.每个方法后面都跟着一对括号

#这是因为方法通常需要额外的信息来完成其工作.这种信息是在括号内提供的.函数title()不需要额外的信息,因此是空的
name = "ada lovelace"
print(name.title())    #首字母大写
print(name.upper())    #全部字母大写
print(name.lower())    #全部字母小写
