# random是使用随机数的python标准库函数
'''
seed()、random()
seed()函数用来初始化随机数种子，默认值为当前系统时间。
随机数种子多为一个整数，而且相同的种子所生成的随机数序列也相同。
random()函数用来生成一个[0, 1]之间的随机小数。

randint()
randint(a, b)(a<=b) 生成一个[a, b]之间的整数。

getrandbits()
getrandbits(n) 生成一个n比特长度(指对应二进制最大长度有几位)的随机整数。

randrange()
randrange(a, b, s)三个参数，前两个确定范围，最后一个确定步长。生成一个[a, b)之间的以s为步数的随机整数。

uniform()
uniform(a, b)生成一个[a, b]间的随机小数。

choice()， shuffle()
choice(s)从序列类型中随机返回一个元素。
shuffle(s)将序列类型中的元素随机排列，返回打乱后的序列(*必须以list形式填入函数)。

sample()
sample(s, k)
从序列类型中随机选择k个元素，返回这k个元素组成的列表*。
'''
import random as rad
str1='fuck'
print(rad.choice(str1)) #返回fuck中随机的字符
print(type(str1))
str2=list(str1)         #将str1的list形式传递给str2
print(str2)
rad.shuffle(str2)       #打乱
print(str2)
print(type(str2))
str2=''.join(str2)      #将str2恢复到字符串
print(str2)
print(type(str2))
print(rad.sample(str2,2))
print(type(str2))