'''
2022 1 13 接单汽车之家的评论采集单子，遇到字体反爬，特此记录一下

最开始遇到，是发现爬出来的评论中有很多 "一个口字型里面有个问号"，随后问了群里的兄弟，得知是字体反爬
其中一个兄弟告诉我对大部分的网站来说可以去测试ua，找到那个刚好就是可以得到不会字体加密的ua，对写题网站不适应
于是乎我就边那大把大把的ua进行测试，边自己再去找另外一种方法，字体映射

大致思路可以参考这两篇文章:
    https://zhuanlan.zhihu.com/p/32087297
    https://blog.csdn.net/zwq912318834/article/details/80268149

大致思路:
    分析也页面的时候如果页面的中的字体是正常的而源代码或开发者工具中字里面夹杂这一些奇怪的字符，那很有可能就是字体反爬
    此时，在源代码或开发者工具中搜索 font-face，在其中查找有没有ttf文件，找到后用 fontcreator软件打开它，查看其详细的字体排布

    def parseDetail(html):
        #解析286x30评论的详情页面
        tree = etree.HTML(html)

        # 匹配ttf font
        font_url = re.findall("url\(\\'(.*?)'\)", html,re.M)[2]
        font_url = 'https:' + font_url
        print(font_url)
        cont = requests.get(url=font_url).content
        with open('01.ttf','wb') as fp:
            fp.write(cont)

        world = TTFont('./01.ttf')
        uni_list = world['cmap'].tables[0].ttFont.getGlyphOrder()
        unicode_list = [eval(r"u'\u" + uni[3:] + "'") for uni in uni_list[1:]]
        word_list = ['四', '空', '孩', '着', '过', '冷', '启', '响', '小', '当', '右', '五', '矮', '三', '光', '身', '六', '中', '灯', '公', '盘', '里', '内', '了', '机', '排', '来', '左', '多', '短', '无', '得', '级', '味', '养', '长', '二', '问', '外', '有', '十', '加', '坏', '耗', '自', '比', '很', '硬', '油', '坐', '低', '地', '手', '路', '好', '真', '和', '泥', '远', '开', '电', '控', '八', '音', '不', '实', '少', '动', '副', '门', '软', '只', '的', '大', '是', '保', '量', '下', '七', '高', '皮', '上', '雨', '九', '一', '性', '呢', '更', '档', '近']

        time = tree.xpath('/html/body/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/b/text()')[0].strip()
        discuss_list = tree.xpath('/html/body/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[4]//text()')
        discuss = ''
        for dis in discuss_list:
            discuss = discuss + dis.strip()

        for i in range(len(unicode_list)):
            discuss = discuss.replace(unicode_list [i], word_list[i])
        print(discuss)

        return time,discuss

    其实就是在爬取每一页的文字的同时将ttf文件的链接爬取，然后请求存储为01.ttf，然后利用fonTools进行解析和得到编码列表
    再将其与我们自己照着那个软件打开ttf文件时的文字进行映射，最后将文字中乱码的文字进行替换即可
'''

'''
字体反爬:
编码改变字体不变破解思路:
    在做爬虫的时候如果在前端页面遇到在一堆文字中间夹杂着一些奇怪的字符，
    那么大概率是遇到了字体反爬，如果我们不对中间夹杂着的字符进行还原就会导致爬取的文本失去了原本该有的价值，
    那么一般解决字体发爬的思路是啥样的呢？
    1.遇到字体反爬，到源代码中搜索关键字"font-face"确定有字体文件(以ttf结尾)
    2.将以ttf结尾的链接进行下载并本地保存，通过fontcreator进行打开
    3.多下载几个字体文件进行对比，看是只有几个字被编码还是编码不同字体不变还是都变
    4.如果是某几个字被编码，那么我们手动的将这几个被编码的字每次replace替换即可
    5.如果是编码不同字体不变，那么只需将每个字对应的编码进行手动列出，在每次请求时一并下载相应的字体文件并获取其中的编码列表
    6.如果是编码不同字体也不同，那么就需要在每次请求时，获取字体文件并获取其中每个字的xy坐标
'''