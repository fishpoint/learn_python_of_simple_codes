# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    用multiprocessing模块的Process启动新进程的过程。区别p.pid()和os.getpid()的区别。p.name、p.is_alive()的作用和输出。
'''
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':  # 该句不能省，不然会报错。
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    print(os.getpid())
    print(p.is_alive())
    print(p.pid)  # p.pid 存储的是子进程的pid。而os.getpid则是程序运行处的当前进程的进程名。这里由于没启动，所以没添加进程。为None

    p.start()  # 执行完start()。子进程才创建好。
    print(os.getpid())
    print(p.name)  # 打印子进程名字
    print(p.is_alive())  # 在start()到join()这一段时间。子进程存在。start()前和join()后，子进程都不存在。但是子进程的pid还保留。
    print(p.pid)

    p.join()

    print(p.pid)
    print(p.is_alive())
    print(os.getpid())
    print('Child process end.')
