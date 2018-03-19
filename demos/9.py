# -*- coding: utf-8 -*-
__author__ = "YuDian"

'''
    python的多重继承。主要检验一下多重继承的继承顺序。下面代码和解析：https://kevinguo.me/2018/01/19/python-topological-sorting/
'''
class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2(A,B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)           # python支持多重继承，在解析父类的__init__时，定义解析顺序的是子类的__mro__属性，内容为一个存储要解析类顺序的元组。
    d=D()
    d.foo()
    d.bar()
