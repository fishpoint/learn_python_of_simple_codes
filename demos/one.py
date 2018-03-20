# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    与two.py联结，用来理解if __name__=='__main__'的意思。
'''
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print(__name__)
    print("one.py is being imported into another module")