'''
列表类型操作函数和方法

函数或方法	描述
ls[i] = x	        替换列表ls第i元素为x
ls[i: j: k] = lt	用列表lt替换ls切片后所对应元素子列表
del ls[i]	        删除列表ls中第i元素
del ls[i: j: k]	    删除列表ls中第i到第j以k为步长的元素
ls += lt	        更新列表ls，将列表lt元素增加到列表ls中
ls *= n	            更新列表ls，其元素重复n次

函数或方法	描述
ls.append(x)	在列表ls最后增加一个元素x
ls.clear()	    删除列表ls中所有元素
ls.copy()	    生成一个新列表，赋值ls中所有元素
ls.insert(i,x)	在列表ls的第i(从零数)位置增加元素x
ls.pop(i)	    将列表ls中第i位置元素取出并删除该元素
ls.remove(x)	将列表ls中出现的第一个元素x删除
ls.reverse()	将列表ls中的元素反转
ls.sort()       将ls中元素按首字母ASCII码排序
'''

# 创建一个list
lst=[]
print(lst)
# 给list输入5个变量
lst+=[1,2,3,4,5]
print(lst)
# 把第三个变量更改为6
lst[2]=6
print(lst)
# 在第三个变量的位置加上一个7
lst.insert(2,7)
print(lst)
# 删掉第二个数据
lst.remove(lst[1])
print(lst)
# 删掉第2-5个数据
del lst[1:4]
print(lst)
# 判断0在不在list内
print(0 in lst)
# 在list内增加0
lst.append(0)
print(lst)
# 返回0在list中的索引
print(lst.index(0))
# 返回list的长度
print(len(lst))
# 返回list中最大的
print(max(lst))
# 清除list
lst.clear()
print(lst)