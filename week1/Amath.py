#选择函数
a,b,c=5,8,2
print(max(a,b,c),min(a,b,c))
'''
ps:max和min还支持key参数指定排序规则，既可以是函数，也可以是lambda表达式
'''
print(max(a,b,c,key=lambda a:1/a))
ar=[5,4,2,8,10]
#排序函数
print(sorted(ar)) #可对元组，字典，集合，列表进行排序并返回一个*列表
'''
ps:
    1.sorted函数有reverse参数指定是升序（False）还是降序（True），默认为升序
    2.sorted依然有key参数
'''
#翻转函数
from random import shuffle
data=list(range(20))
print(data)
shuffle(data)
print(data)
data=list(reversed(data))
print(data)
print(max(data))
'''
ps:reversed函数只能返回一个迭代器对象的内存地址，且对reversed(a)这个返回值只能操作一次
一个列表a：
a=[1,2,3,4,5,6,7]
一个对象b：
b=reversed(a)
输出：
print(b)
<list_reverseiterator object at 0x000001652144E940>      显示为一个迭代器对象的内存地址
print(list(b))
[7, 6, 5, 4, 3, 2, 1] 
当再次输出对象b时：
print(list(b))
[]     显示为空列表！
由此可知：reversed（）返回的是一个迭代器对象，只能进行一次循环遍历。显示一次所包含的值！
'''