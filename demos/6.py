'''
    使用埃氏筛法和filter函数计算素数
'''


def _odd_iter():  # 产生从1开始的奇数
    n = 1
    while True:
        n = n + 2
        yield n


def _not_disvisible(n):  # 筛选函数，n为当前第一个数。该函数返回一个函数，用做filter的筛选函数
    return lambda x: x % n > 0    # 若后面的数能被第一个数整除，则return 0.否则return 1.保留


# 上面的函数也能写成：
        # def _not_disvisible(n):
        #     def f(x):
        #         return x % n
        #     return f


def primes():
    yield 2
    it = _odd_iter()   # 初始序列
    while True:
        n = next(it)     # 返回序列的第一个数
        yield n
        it = filter(_not_disvisible(n), it)


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
