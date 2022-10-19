#1.range函数的试用
'''
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))
'''
'''
函数语法
range(start, stop[, step])(**左闭右开)
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
#2.对python不可改变字符串的修改
s=input()
t=""
print("{}".format(len(s)))
for c in s:
    t+=c
print("{}".format(t))
'''
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z': 
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
    elif 'A' <= c <= 'Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
    else:
        t += c
print(t)
'''
'''
str1 = "我是字符串数据类型"
# 将字符串类型转换成列表类型
list1 = list(str1)
print(list1)
list1[0] = "它"  # 将列表中的第一个数据修改为它
str1 = "".join(list1)   # 将列表转换成字符串类型
print(str1)
运行结果：
['我', '是', '字', '符', '串', '数', '据', '类', '型']
它是字符串数据类型
'''