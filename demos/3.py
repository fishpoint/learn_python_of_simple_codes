# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list.

def yanghui():
    for n in range(1,11):      // 这里设置要输出的杨辉三角的行数
        SecondLine = []        // 用来存放下一行数据。需要在循环内清空
        for i in range(0,n):   // 一行的数据长度为n个。从0~n-1。
            if i==0 or i==n-1:
                SecondLine.append(1)  // 每行收尾两个数字设为1.用append
            else:
                SecondLine.append(PrimList[i-1]+PrimList[i])    // 非首末时，第二行的第n位为第一行的n-1位和第n位之和。
        yield(SecondLine)                       // 返回第二行
        PrimList=SecondLine                     // 让第二行数据成为下一轮的第一行。

for l in yanghui():
    print(l)


