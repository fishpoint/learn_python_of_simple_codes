'''
        设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''
import time,functools

def metric(text=''):     # 可以给装饰器输入文本，默认为 。
    def decorator(func):  # 装饰器本体，输入函数
        @functools.wraps(func)    #将__name__更正为func.__name__.不然会是wrapper
        def wrapper(*args,**wk):
            BeginTime=time.time()
            func(*args,**wk)     #  (*args,**wk)可以匹配具有任何输入的函数。 这里让程序运行.好得出运行时间
            EndTime=time.time()
            print('%s %s : running time %.4f secod' %(text,func.__name__,EndTime-BeginTime))
            return func(*args,**wk)
        return wrapper
    return decorator
# 测试
@metric('works')             #     等价于:fast=metric('works')(fast)
def fast(x, y):
    time.sleep(0.012)
    return x + y;

@metric('another works')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')