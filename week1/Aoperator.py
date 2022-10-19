'''
(a=10,b=21)
+	加 - 两个对象相加	a + b 输出结果 31
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
/	除 - x 除以 y	b / a 输出结果 2.1
%	取模 - 返回除法的余数	b % a 输出结果 1
**	幂 - 返回x的y次幂	a**b 为10的21次方
//	取整除 - 向下取接近商的整数	
>>> 9//2
4
>>> -9//2
-5
'''

'''
python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
'''
print(10 and 20)#体现了其惰性运算的特点
print(10 or 20)
print(not 10)
'''
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True
'''
#sort()是可变对象(字典、列表)的方法，无参数，无返回值，sort()会改变可变对象，因此无需返回值。
#sort()方法是可变对象独有的方法或者属性，而作为不可变对象如元组、字符串是不具有这些方法的，如果调用将会返回一个异常。
#sorted()是python的内置函数，并不是可变对象(列表、字典)的特有方法，sorted()函数需要一个参数(参数可以是列表、字典、元组、字符串)，
#无论传递什么参数，都将返回一个以列表为容器的返回值，如果是字典将返回键的列表。
#reverse()与sort的使用方式一样，而reversed()与sorted()的使用方式相同。
ls1=[1,5,6,3,7,4]
ls2=[1,5,6,3,7,4]
print(ls1.sort(),ls1)
print(sorted(ls2),ls2)