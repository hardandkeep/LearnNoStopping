#复制列表
#要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引([:])，这样就可以复制整个列表

#例如，假设有一个列表，其中包含你最喜欢的四种食品，而你还想创建另外一个列表，在其中包含了一位朋友喜欢的所有食品。
    #不过你喜欢的食品，这位朋友都喜欢，因此你可以创建这个列表：
my_foods = ['noodles','meat','soup']
friend_foods = my_foods[:]

#从这句来看，复制列表其实就是，新建一个列表，然后在等号右边写上：要负责列表的名字[:]
    #其中，方括号里面是你要复制的范围




    