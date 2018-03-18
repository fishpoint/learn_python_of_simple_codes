# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    元素为class的list_包含二维list生成
'''


class Data(object):
    def __init__(self, datas):
        self.datas = datas

    def printdata(self):
        print(self.datas)

# dic = {'姓名': '', '年龄': 0}


library = [[chr(b + 65), b] for b in range(26)]
print(library)
lst = []
for info in library:
    dic = {'姓名': '', '年龄': 0}
    dic['姓名'] = info[0]
    dic['年龄'] = info[1]
    lst.append(Data(dic))
for p in lst:
    p.printdata()
