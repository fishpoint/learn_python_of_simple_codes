# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    用filter筛选指定数目的回文数。    
'''
def palindrome(n):
    return str(n) == str(n)[::-1]

def num():
    n=100000
    while True:
        n=n+1
        yield n

def find_num():
    it=num()
    while True:
        nu=filter(palindrome,it)
        yield next(nu)

n=0
for s in find_num():
    print(s)
    n=n+1
    if n==50:
        break
