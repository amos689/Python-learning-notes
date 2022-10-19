'''
函数语法
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
# 字符串倒置方法1
'''
语法：  'sep'.join(seq)
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
'''
str1 = 'amos'
lst = list(str1)
lst.reverse()
str2 = ''.join(lst)
print(str2)
print(type(str2))
# 字符串倒置方法2
'''
append()函数
描述：在列表ls最后(末尾)添加一个元素object
语法：ls.append(object) -> None 无返回值
'''
str_3 = 'phoenix'
i = len(str_3) - 1
str_list = []
while(i >= 0):
    str_list.append(str_3[i])
    i = i - 1
print(''.join(str_list))

# *附加挑战：生成二维数组
#(1.)
a=[]
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(i)
for i in range(5):
    print(a[i])
#(2.)
a=[[0]*5 for i in range(2)]
a[1][2]=1
print(type(a),a)
    
# break与continue的应用（同C语言）
st='python'
while st!='':
    for c in st:
        if c=='t':
            break
        print(c,end='')
    st=st[:-1]
    if st in ['p']:
        break
print()

# for/while+else（如果不是break退出的for或者while，都将执行else）

