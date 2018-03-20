# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    v1.0:   2018/3/19 21:39
        完成对指定的文件夹(TopDir)内部的文件和目录进行排序。文件和目录混合排序。可选择从小到大或者是从大到小。
    v1.2:  2018/3/19
        添加对files和dirs的分开显示排序结果。将排序结果放在本地磁盘中。
'''

import os

N = 1


class dirc(object):  # dirc类用来表示文件的大小和类型(kb,mb,gb)
    def __init__(self, name, size, sizetype, ctype=0):
        self.name = name  # name存放名字
        self.size = size  # size存放更换过的大小
        self.sizetype = sizetype  # sizetype存放类型
        self.ctype = ctype  # file or dir
        self.realtype = self.int2str(self.sizetype)  # 类型的真实意义 b,kb,mb,gb
        self.realctype = self.ctype2real(self.ctype)

    def int2str(self, sizetype):
        if self.sizetype == 1:
            return 'Byte'
        elif self.sizetype == 2:
            return 'KB'
        elif self.sizetype == 3:
            return 'MB'
        elif self.sizetype == 4:
            return 'GB'

    def ctype2real(self, ctype):
        if ctype == 1:
            return 'Dir'
        elif ctype == 0:
            return 'File'

    def printlog(self):
        self.logges = self.realctype + ':' + self.name + '       ' + str(self.size) + self.realtype
        print(self.logges)


AllSize = []  # AllSize用来存放所有的dirc类


def single_dir_size(dirname):  # 程序的功能是对传入的文件夹计算大小的单位
    size = GetDirSize(dirname)  # 调用GetDirSize函数，得到原始大小
    BeautifulSize, sizetype = beautiful_size(size)  # 调用beautiful_size函数，得到变换后的大小和单位
    return BeautifulSize, sizetype


def GetDirSize(dirname):  # 得到dirfile的大小。dirname是文件夹名
    TotalSize = 0
    for (DownRoot, DownDirs, DownFiles) in os.walk(dirname):
        for file in DownFiles:
            TotalSize = TotalSize + os.path.getsize(os.path.join(DownRoot, file))
    return TotalSize


def beautiful_size(size):  # 对size进行单位转换
    sizeflag = 1
    global N
    while size > 1024:
        size = size / 1024
        sizeflag = sizeflag + 1  # sizeflag:1  byte       2: kb    3:mb    4:gb
    print('running...' + str(N))
    N = N + 1
    return size, sizeflag


def all_sort(list, SortType=1, spearate=0):
    # SortType:1   AllSize[0]:min     SortType:0  AllSize[0]:max
    # speratate:1  file和dir一块排序     0 ： 分开排序
    # 不能用可变参量*name传入list。不然在函数内会变成tuple

    # 用冒泡排序法对List进行排序
    for n in range(0, len(AllSize) - 1):
        for i in range(0, len(AllSize) - 1 - n):
            RivalLow = AllSize[i]
            RivalHigh = AllSize[i + 1]
            c = RivalLow.size * 1024 ** (RivalLow.sizetype - 1)
            d = RivalHigh.size * 1024 ** (RivalHigh.sizetype - 1)
            if RivalLow.size * 1024 ** (RivalLow.sizetype - 1) > RivalHigh.size * 1024 ** (RivalHigh.sizetype - 1):
                AllSize[i], AllSize[i + 1] = RivalHigh, RivalLow
    NewSize = AllSize
    if not spearate:
        NewSize = []
        for n in AllSize:
            if n.ctype == 0:
                NewSize.append(n)
        for n in AllSize:
            if n.ctype == 1:
                NewSize.append(n)

    if SortType == 1:  # 选择排序方法：默认从小到大
        return NewSize  # 1 从小到大
    elif SortType == 0:
        return NewSize[::-1]  # 0  从大到小


n = 1  # 得到TopDor下一层的文件夹名
TopDir = r'D:/'  # TopDir 指向最高层的文件夹
TopDir = input('where you want to sort?:')
if TopDir == '':
    TopDir = 'F:\python_codes\learn_python_of_simple_codes\demos'
SizeWay = 0
SizeWay = int(input('choose a way to sort(1:bigger;0:smaller):'))
spearate = 0
spearate = int(input('choose sort files and dirs total or depart(1:total;0:depart)'))
for (root, dirs, files) in os.walk(TopDir):
    if n == 1:
        FirstName = dirs  # FirstName下存放的是TopDir下第一层的文件夹名（只有名字，不是全路径）
        FirstFiles = files
        n = n + 1
        for FileName in FirstFiles:
            FileFullName = os.path.join(root, FileName)
            FileSize = os.path.getsize(FileFullName)
            FileSize, FileSizeType = beautiful_size(FileSize)
            AllSize.append(dirc(name=FileFullName, size=round(FileSize, 3), sizetype=FileSizeType, ctype=0))

        for name in FirstName:
            DirAllName = os.path.join(root, name)  # 得到文件夹的完整路径
            DirSize, DirSizeType = single_dir_size(DirAllName)  # 得到文件大小和单位
            AllSize.append(
                dirc(name=DirAllName, size=round(DirSize, 3), sizetype=DirSizeType, ctype=1))  # 将信息组成class放到List中。
            # round(size,n)  将传入的数据size保留n位小数。
        # for i in AllSize:
        #     print(i.name,'__',i.size,'__',i.realtype)
        # print(type(AllSize))
        SortedAllSize = all_sort(AllSize, SortType=SizeWay, spearate=spearate)
        if not os.path.exists(os.path.join(r'F:/', 'save_size')):
            os.mkdir(os.path.join(r'F:/', 'save_size'))
        with open(r'F:/save_size/save_sort.txt', 'w') as f:
            f.write('')
        for i in SortedAllSize:
            i.printlog()
            with open(r'F:/save_size/save_sort.txt', 'a') as f:
                f.write(i.logges + '\n')
    else:
        break
input()
