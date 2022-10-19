'''
所有字符串函数均可对字符串进行操作(不只限于对变量名操作)
'''
# (1/4)变大小写、变字符、排序
str1 = "Amos_Phoenix"
a = 12
print(type(a), end="\n\n")
a = str(a)  # 将a转化为字符串类型
print(str1.lower(), str1.upper(), str1, end="\n\n")  # 全部变大/小写
str1=str1.lower()
print(str1, end="\n\n")
print(type(a), end="\n\n")

# (2/4)替换和居中
str2 = "Bmos_Phoenix"
print(str2.replace('B', 'A')+'\n'+str1.center(26, ' '), end="\n\n")
# str2.replace('老串','新串')
# str1.center(总格数,'填充符')

# (3/4)增添/删除字符
str3 = '= python= '
print(str3.join('MYPY')+'\n'+str3.strip(' =np'), end="\n\n")
# str.strip('两头要删除的字符，不能删str中间')
# str.join('在输入字符串中间每个元素中间加上str字符串')
#***'(间隔符)'.join(母串)
'''
原方法释义中操作的是可迭代对象，不是专指序列，广义上可迭代对象的例子包括所有序列类型
(例如 list、str 和 tuple)以及某些非序列类型例如 dict、文件对象
以及定义了 __iter__() 方法或是实现了 Sequence 语义的 __getitem__() 方法的任意自定义类对象。
另外，如果可迭代对象中只能存在 string 元素，否则会报 TypeError 异常。
'''

# (4/4)字符转编码/编码转字符
for i in range(12):
    c = chr(9800+i)
    print(c, ord(c))

'''
字符串切片：
split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表(list)
***分割后分割标志字符将被删去
语法
str.split(str="", num=string.count(str)).
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等，他会把中间连续的空字符一并替换。
num -- 分割次数。默认为 -1, 即分隔所有,如果参数 num 有指定值，则分隔 num+1 个子字符串。
返回值
返回分割后的字符串列表。
'''
str4 = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str4.split(), end="\n\n")        # 以空字符为分隔符，包含 \n
print(str4.split(' ', 1 ), end="\n\n")  # 以空格为分隔符，分一次，分隔成两个

#注意：str函数对于元组，列表，集合类函数进行处理时不会脱去其身上带有的括号或者逗号
lst=[1,1,5,6,3]
lst=str(lst)
print(lst,type(lst), end="\n\n")
print(list(lst), end="\n\n")