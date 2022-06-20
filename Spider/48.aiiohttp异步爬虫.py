'''
python在3.4版本中将asyncio引入内置模块，即支持了异步操作，在3.5版本后引入async/await关键字简化了异步操作。aiohttp是基于asyncio的一个异步http框架，可以基于此框架编写异步爬虫。
关于asyncio需要提前明确几个概念：

event_loop事件循环：协程函数必须注册到事件循环中，由事件循环运行。
coroutine协程：本质是一个函数，但是需要由async指定为协程函数。
task任务：coroutine本质是函数，需要将其封装为任务，任务可以包含各种状态。
future：较低层的可等待（awaitable）对象，表示异步操作的最终结果。当一个Future对象被等待的时候协程会一直等待，直到Future运行完毕。Future是Task的父类，它和task没有本质区别。
学习异步前强烈建立看一下asyncio的基本概念和核心架构，推荐看：http://www.360doc.com/content/19/0123/07/58006001_810729573.shtml
也可以看一下这个博客理解协程的各种操作https://www.jianshu.com/p/50384d0d3940

关于aiohttp，做爬虫最重要的是ClientSession对象，由这个对象进行请求发送。aiohttp的中文文档：https://hubertroy.gitbooks.io/aiohttp-chinese-documentation/content/

开始编写爬虫（以豆瓣电影top250为例）
先编写解析模块，这里用pyquery模块进行解析。
pyquery 是类似jQuery 的python实现。pyquery是基于lxml（c编写）模块，所以要比纯python编写的Beautifulsoup解析速度快。
'''
from pyquery import PyQuery as pq

def parse(resp_html):
    doc = pq(resp_html)
    for li in doc('div.article ol li').items():
        title = li('div > div.info > div.hd > a > span:nth-child(1)').text()  # 电影标题
        score = li('span.rating_num').text()  # 评分
        print(title, score)

#编写协程函数
import asyncio
import aiohttp
# 协程函数
async def crawl(url):
    async with aiohttp.ClientSession() as session:  # ClinetSession对象
        # 发送get请求，里面可以像requests.get()一样传递headers或者proxy等，详情可查看文档
        async with session.get(url) as resp:
            parse(await resp.text())

url = 'https://movie.douban.com/top250/'
loop = asyncio.get_event_loop()   # 获取事件循环
loop.run_until_complete(crawl(url))   # 执行


#多url请求
url = 'https://movie.douban.com/top250/?start={}'
# tasks = [asyncio.ensure_future(crawl(url.format(i))) for i in range(0, 250, 25)]
tasks = []
for i in range(0, 250, 25):
    # ensure_future()创建任务，3.7版本可以使用asyncio.create_task()创建
    task = asyncio.ensure_future(crawl(url.format(i)))
    tasks.append(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))  # 将task添加到事件循环
#异步请求非常快，可以限制连接池容量。linux打开文件的最大数默认是1024，windows默认是509，
#如果异步操作文件的数量超过最大值会引起报错ValueError: too many file descriptors in select()
#可以用asyncio.Semaphore(100)限制并发数量。

async def crawl(url):
    # async with asyncio.Semaphore(30):  # 限制并发数量
    conn = aiohttp.TCPConnector(limit=30)   # 限制连接池数量，limit=0表示不限制，默认为100
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as resp:
            return parse(await resp.text())
#或者用协程嵌套
async def main():
    url = 'https://movie.douban.com/top250/?start={}'
    tasks = [asyncio.ensure_future(crawl(url.format(i))) for i in range(0, 250, 25)]
    await asyncio.wait(tasks)   # await asyncio.gather(*tasks)也可以

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#如果嵌套的协程函数有return返回值
async def main():
    url = 'https://movie.douban.com/top250/?start={}'
    tasks = [asyncio.ensure_future(crawl(url.format(i))) for i in range(0, 250, 25)]
    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print(task.result())
    # 或者
    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#完整代码
import asyncio
import aiohttp, async_timeout
from pyquery import PyQuery as pq


def parse(resp_html):
    res = []
    doc = pq(resp_html)
    for li in doc('div.article ol li').items():
        title = li('div > div.info > div.hd > a > span:nth-child(1)').text()
        score = li('span.rating_num').text()
        res.append({'title': title, 'score': score})
    return res

async def crawl(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return parse(await resp.text())   # 有返回值

async def main():
    url = 'https://movie.douban.com/top250/?start={}'
    tasks = [asyncio.ensure_future(crawl(url.format(i))) for i in range(0, 250, 25)]
    await asyncio.wait(tasks)
    results = await asyncio.gather(*tasks)   # 获取返回值
    for result in results:
        print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

