# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    粗陋的代码检查，把自己写的代码放在前面，同时进行注释(用IDE自带的注释快捷键注释，也就是'# '.)可以忽视行里面的[]但是[ ]不行。就是只能是None行。
    由于我用pycharm写的话，前面会自动带上# -*- coding: utf-8 -*-   __author__ = "YuDian"  两行，所以我默认忽略这两行。
    若要自己用，要修改的地方在代码的注释中给出。
'''
import os
filename=input('哪个文件？：')
file=os.path.join('F:/python_codes/learn_python_of_simple_codes/demos/',filename)    # 将join中的路径换为自己的文件路径。
# print(file)
with open(file,'r') as f:
    AllLines=f.readlines()
for i in range(len(AllLines)):
    AllLines[i]=AllLines[i].replace('\n','')

FirstLines=[]
SecondLines=[]
times = 0
for i in range(2,len(AllLines)):         # 设定检查起始行。。    按照自己的情况修改range的始末。
    if AllLines[i] !='':
        if AllLines[i][0]=='#':
            times=times+1
            if AllLines[i].replace('#','')!='':
                FirstLines.append(AllLines[i])
        else:
            if(times>=3):
                SecondLines.append(AllLines[i])
            else:
                times=0

if len(FirstLines)!=len(SecondLines):
    print('行数都不对，前面的行数为：%s,而后面的行数为:%s'%(len(FirstLines),len(SecondLines)))
    raise(SystemExit)
flag=0

for i in range(len(FirstLines)):
    if(FirstLines[i].replace('#','').lstrip()==SecondLines[i].lstrip()):    # .lstrip()去掉开头的空格
        pass
    else:
        print(False)
        flag=1
        print(FirstLines[i].replace('#','').lstrip())
        print(SecondLines[i])
if flag==0:
    print('all right...还是有错？可能是缩减有问题。再检查缩进情况。')

    for i in range(len(FirstLines)):
        suo1st=len(FirstLines[i].replace('# ',''))-len(FirstLines[i].replace('#','').lstrip())
        suo2nd=len(SecondLines[i])-len(SecondLines[i].lstrip())
        if suo1st!=suo2nd:
            if(flag==0):
                print('find!有缩进错误~')
            flag=flag+1
            print(FirstLines[i])
            print('前面的缩进为%s个空格，后面的缩进为%s个空格。'%(suo1st,suo2nd))
if flag==0:
    print('缩减也没错...')

