# -*- coding: utf-8 -*-
__author__ = "YuDian"
import os
var=0

if var==0:
    var=var+1
    with open(r'F:\python_codes\learn_python_of_simple_codes\demos\setup_auto.py','r+') as f:
        flist=f.readlines()
        flist[3]='var=%s\n'%var
        with open(r'F:\python_codes\learn_python_of_simple_codes\demos\setup_auto.py', 'w') as f:
            f.writelines(flist)
if var==2:
    from distutils.core import setup
    import os
    import py2exe
    setup(console=['setup_auto.py'])

if var==1:
    var=var+1
    name=input('which function you want to pack?')
    with open(r'F:\python_codes\learn_python_of_simple_codes\demos\setup_auto.py','r+') as f:
        flist=f.readlines()
        flist[3]='var=%s\n'%var
        flist[16]="    setup(console=['%s'])\n"%name
        with open(r'F:\python_codes\learn_python_of_simple_codes\demos\setup_auto.py', 'w') as f:
            f.writelines(flist)
    os.system('python setup_auto.py py2exe')
    var=0
    with open(r'F:\python_codes\learn_python_of_simple_codes\demos\setup_auto.py','r+') as f:
        flist=f.readlines()
        flist[3]='var=%s\n'%var
        with open(r'F:\python_codes\learn_python_of_simple_codes\demos\setup_auto.py', 'w') as f:
            f.writelines(flist)




