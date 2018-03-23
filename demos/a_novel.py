# -*- coding: utf-8 -*-
__author__ = "YuDian"

from multiprocessing import Pool  # Pool用来创建进程池
import os, time
from urllib import request  # 访问网页
from bs4 import BeautifulSoup  # 第三方库，能更好的对HTML进行解析

'''
    基本思路：1.从一个盗版小说网站上得到一些小说的名字和对应的链接；
             2.选定一本小说名，通过对应的链接得到小说的所有章节链接；
             3.通过所有所有的章节链接通过对每个章节的网页进行分析，得到小说正文。分别存在不同的文档中（使用多进程）
             4.将文档按顺序拼接，得到最终文档，删除中间文档。
'''


def download(head, filename, ProNum, start, end, PageLinks):  # 向函数传入请求头、文件名、进程序号、始末章节、章节链表
    print(os.getpid())  # 打印该进程id
    for page in range(start, end + 1):
        PageUrl = PageLinks[page]
        PageReq = request.Request(PageUrl, headers=head)
        response = request.urlopen(PageReq)
        PageHtml = BeautifulSoup(response, 'lxml')

        title = PageHtml.find('div', class_='entry-single').h1.string  # 分析得到小说标题
        print(title, 'is downloading...')
        print(os.getpid())
        if page == start:
            f = open(filename + str(ProNum) + '.txt', 'w')  # 小说名+进程序号作为文件名
            f.write('\n' + title + '\n')
        else:
            f = open(filename + str(ProNum) + '.txt', 'a')
            f.write('\n' + title + '\n')
        text = PageHtml.find('div', id='booktext').children
        for i in text:
            if (i.find('div') == -1):
                if len(i) > 1:
                    newstr = str(i).replace('\n', '').replace('\xa0', ' ').replace('\ue810', '').replace('\ue420',
                                                                                                         '').replace(
                        '\ue2f0', '').replace('\ue0df', '')  # 根据输出的情况手动将不能编码的字符进行转换
                    try:  # 保证在遇到不能打印的字符时，程序能进行运行。
                        f.write(newstr)
                    except Exception as e:
                        print(e)

# 第一步：从网站上得到所有的小说名字和对应链接

if __name__ == '__main__':
    AllLinks = {}  # AllLinks用来存放小说名称和对应链接
    url = r'http://www.kushubao.com/xiaoshuodaquan/3.html'  # 网站网址
    HeadUrl = r'http://www.kushubao.com'  # 因为从网址上爬到的小说链接只有后面的/xxxx所以要自己补全URL。
    head = {}  # 以浏览器的方式进行访问
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers=head)
    response = request.urlopen(req)  # 返回的response通过response.read().decode('uth-8')就可以输出网页的HTML
    html = BeautifulSoup(response, 'lxml')  # 将response变为BeautifulSoup能处理的对象
    novellist = html.find(class_='novellist')  # 定位到小说名和对应链接在的地方
    novels = novellist.find_all('a')  # 得到所有的小说名和链接在的HTML语句，.find_all()方法得到的是一个list
    for novel in novels:
        AllLinks[novel.string] = str(HeadUrl + novel.get('href'))

    # 第一步到这里结束。此时所有的小说名和对应的完整链接都存放在名为AllLinks的字典中。
    #
    # 第二步：通过指定小说名，从AllLinks中得到该小说的对应链接，然后下载所有的小说章节。

    name = '神灵契约'  # 指定的小说名称
    NovelUrl = AllLinks[name]
    NovelReq = request.Request(NovelUrl, headers=head)
    PageLinks = []  # 列表，用来存放所有的小说章节链接。
    # 不用字典的理由：因为元素在字典里面是无序排列的，在第三步要按顺序从低章到高章下载。所以直接用了一个list。反正章节名可以在没章里面搞到。
    response = request.urlopen(NovelReq)
    html = BeautifulSoup(response, 'lxml')  # html 中放的就是有每章的名字和链接的BeautifulSoup对象。可以用html.pretty()进行查看
    LinkTag = html.find('div', id='xslist')
    PageList = LinkTag.find_all('a')
    for page in PageList:
        PageLinks.append(NovelUrl + page.get('href'))

    # 自此，第二步结束，得到的章节链接仿真了PageLinks的链表中。

    # 第三步，多并程下载小说内容

    ProcessNumber = 11  # 要开的进程数
    p = Pool()  # 创建进程池。由于参数缺省，默认为运行电脑的核数
    StartTime = time.time()  # 开始时间
    StartPage = 0
    for process in range(ProcessNumber):  # 用来创建进程
        if (process < ProcessNumber - 1):
            EndPage = int(len(PageLinks) / ProcessNumber * (process + 1) - 1)
        else:
            EndPage = len(PageLinks) - 1
        #         得到每个进程下载起始章节。
        print('进程序号：', process + 1, '始末章节：%s--->%s' % (StartPage, EndPage))
        p.apply_async(download, args=(head, name, process, StartPage, EndPage, PageLinks))
        StartPage = EndPage + 1
    p.close()  # close和join要放到for循环外。
    p.join()
    EndTime = time.time()
    print('Total run time=%.3f' % (EndTime - StartTime))

    # 第三步结束。（download传入的参量太多了。)

    # 第4步：将所有分开的章节整合到一起，并删除临时章节。

    wr = open(name + '.txt', 'w')  # 最后存放的文件名
    for i in range(ProcessNumber):
        re = open(name + str(i) + '.txt', 'r')
        lines = re.readlines()
        wr.writelines(lines)
        re.close()
    wr.close()
    # 文件合并完毕
    for i in range(ProcessNumber):
        try:
            os.remove(name + str(i) + '.txt')  # 移除文件
        except Exception as e:
            print('文件：', name + str(i) + '.txt', '无法删除')
