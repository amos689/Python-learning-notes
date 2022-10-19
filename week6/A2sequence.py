# 序列是一个基类类型，包括字符串，元组和列表
# 序列，顾名思义，都有序号，都能完成切片操作
s="soma"
s1=s[::-1]
s=list(s)
s2=reversed(s)
s=''.join(s)
s2=''.join(s2)
print(s1+'\n'+s2+'\n'+str(type(s)))

'''
(1)、序列类型通用操作符

操作符及应用	描述
x in s	如果x是序列s的元素，返回True，否则返回False
x not in s	如果x是序列s的元素，返回False，否则返回True
s + t	连接两个序列s和t
s*n 或 n*s	将序列s复制n次
s[i]	索引，返回s中的第i个元素， i是序列的序号
s[i: j] 或 s[i: j: k]	切片，返回序列s中第i到j以k为步长的元素子序列

(2)、序列类型通用函数和方法
函数和方法	描述
len(s)	返回序列s的长度
min(s)	返回序列s的最小元素， s中元素需要可比较
max(s)	返回序列s的最大元素， s中元素需要可比较
s.index(x) 或
s.index(x, i, j)	返回序列s从i开始到j位置中第一次出现元素x的位置
s.count(x)	
返回序列s中出现x的总次数
'''
print(s.count('a'),s.index('a'),min(s))
print('a' in s,'b' not in s)