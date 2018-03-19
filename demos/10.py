# -*- coding: utf-8 -*-
'''
    文件的基本操作。
'''
__author__ = "YuDian"
import os
# dir=r'F:/for_python/novel1.txt'
# # os.path.exists(path)  判断路径是否存在
# if os.path.exists(dir):
#     print('dir exists')
# else:
#     print('print no exists')
# # os.path.isfile(path)     判断是否为文件
# if os.path.isfile(dir):
#     print("is file")
# else:
#     print('no file')
#
# # os.path.getsize(path)    获取文件大小
# size=os.path.getsize(dir)
# print(int(size/1024))
#

# os.path.walk(path)    遍历path,返回一个三元组(dirpath,dirnames,filenames)
n=1
for (root,dirs,files) in os.walk(r'F:\for_python'):
    # for filename in files:
    #     print('files:'+os.path.join(root,filename))
    # if n==1:
    #     print(dirs)
    #     n=n+1
    if n==1:
        print(files)
        print(dirs)
        n=n+1
    # print(dirs)
    # for dirc in dirs:
    #     print('dir:'+os.path.join(root,dirc))

print(1024**3/1024/1024/1024)