# 先随机生成一个含有10个大小写和长度均不固定的单个字母列表的列表Words。
# 然后用reduce函数将该列表变为一个含有10个大小写和长度不固定的字符串NewWords。
# 然后用map函数将NewWords变为一个首字母大写，其他字母小写的列表NewName.
import random
from functools import reduce
def word2sentence(word1,word2):   #  word2sentence函数用来将两个字符组成一个字符串。用在reduce里面可以将多个单字字符组成字符串。
    NewWord=word1+word2
    return NewWord

def name(name):          #  name函数先将字符串变为全部小写.lower()。再将全部小写的字符串变为首字母大写.capitalize()
    name=name.lower().capitalize()
    return name

Words=[]                   # Words 用来存放随机生成的所有的单个字符。共有10组，每组长度在[2,5]
for i in range(1,11):
    word=[]                #  word用来存放10组中每一组的所有字符。
    for s in range(1,random.randint(3,6)):       # 这一句用来表明word的长度在[2,5]个之间
        t=random.randint(1,2)         #  t用来决定是大写还是小写字母
        if t==1:
            word.append(chr(random.randint(65,90)))         # t 为 1时，生成大写字母
        elif t==2:
            word.append(chr(random.randint(97,122)))        # t 为 2时，生成小写字母
    Words.append(word)
    #   第一步完成
    NewWords=[]
for a in range(0,len(Words)):
    NewWords.append(reduce(word2sentence,Words[a]))
print(NewWords)
# 第二步完成
NewName=list(map(name,NewWords))
print(NewName)
# 第三步完成

