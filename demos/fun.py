# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
just for fun
'''


import os
var=62

if var<100:
    var=var+1
    with open(r'F:\python_codes\learn_python_of_simple_codes\demos\fun.py','r+') as f:
        flist=f.readlines()
        flist[8]='var=%s\n'%var
        with open(r'F:\python_codes\learn_python_of_simple_codes\demos\fun.py', 'w') as f:
            f.writelines(flist)
    print(var)
    os.system('python fun.py')

if var==100:
    var=0
    with open(r'F:\python_codes\learn_python_of_simple_codes\demos\fun.py','r+') as f:
        flist=f.readlines()
        flist[8]='var=%s\n'%var
        with open(r'F:\python_codes\learn_python_of_simple_codes\demos\fun.py', 'w') as f:
            f.writelines(flist)
    os.system('python fun.py')





