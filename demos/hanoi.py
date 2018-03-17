__author__="YuDian"

def move(n,a,b,c):
    if n==1:
        print("move %s——>%s"%(a,c))
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
n=input("想移动多少层的：")
move(3,'a','b','c')