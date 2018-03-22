# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    尝试用多进程下载一部小说。
        第一步：实现单进程的小说下载。
'''

# 第一步：获取所有的小说名字和连接。

from bs4 import BeautifulSoup
from urllib import request



def download(page,filename,number):
    title=page.find('div',class_='entry-single').h1.string
    print(title,'is downloading...')
    if number==1:
        f=open(filename+'.txt','w')
        f.write('\n'+title+'\n')
    else:
        f=open(filename+'.txt','a')
        f.write('\n'+title+'\n')
    text=page.find('div',id='booktext').children
    for i in text:
        # print(i.find('div'))
        if(i.find('div')==-1):
            if len(i)>1:
                newstr=str(i).replace('\n', '').replace('\xa0', ' ').replace('\ue810','').replace('\ue420','').replace('\ue2f0','')
                try:
                    f.write(newstr)
                except Exception as e:
                    print(e)

# 23~28是凑出来的。。。。。。





if __name__ == '__main__':
    AllLinks = {}
    url = r'http://www.kushubao.com/xiaoshuodaquan/3.html'
    HeadUrl = r'http://www.kushubao.com'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = BeautifulSoup(response, 'lxml')
    novellist = html.find(class_='novellist')
    novels = novellist.find_all('a')
    for novel in novels:
        AllLinks[novel.string] = str(HeadUrl + novel.get('href'))
    # for k,v in AllLinks.items():
    #     print(k,v)

# 到这里，得到的小说名称和该小说对应的连接存放在AllLinks字典中。
# --------------------------------------------------------------------------------------
# 第二步：得到指定小说的所有章节目录和章节对应连接。

    name='护花风水师'
    NovelUrl=AllLinks[name]
    NovelReq=request.Request(NovelUrl, headers=head)
    PageLinks=[]
    response=request.urlopen(NovelReq)
    html=BeautifulSoup(response,'lxml')
    LinkTag=html.find('div',id='xslist')
    # print(LinkTag)
    PageList=LinkTag.find_all('a')
    for page in PageList:
        PageLinks.append(NovelUrl+page.get('href'))
    # for page in PageLinks:
    #     print(page)

# 到这一部分，得到了选定的小说对应的没章的连接。这里只有连接。章节名在具体章节中获得。

# 第三部分：从每章下载文本
    i=0
    for SingleLink in PageLinks:
        PageUrl=SingleLink
        i=i+1
        PageReq = request.Request(PageUrl, headers=head)
        response=request.urlopen(PageReq)
        PageHtml=BeautifulSoup(response,'lxml')
        download(PageHtml,name,i)
