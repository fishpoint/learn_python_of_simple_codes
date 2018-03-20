# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    利用上次写的dirs_size.py。将最后的list(SortedAllSize)进行pickle和unpickle.
    
    pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
    或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
'''


import pickle,time

if __name__=='__main__':
    import dirs_size
    f=open('save_pickle.txt','wb')
    pickle.dump(dirs_size.SortedAllSize,f)
    f.close()
    time.sleep(1)
    f=open('save_pickle.txt','rb')
    for i in pickle.load(f):
        print(i.name)
# for i in new:
#     print(i)





