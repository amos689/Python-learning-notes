'''
通过不同方法完成num的阶乘（或其倍数的运算）
'''
# 定义常规函数
def c1(num):
    c=1
    for i in range(1,num+1):
        c*=i
    return c
# 定义可选参数函数(n可赋值可不赋值，不赋值默认n=1)
def c2(num,n=1):
    c=1
    for i in range(1,num+1):
        c*=i
    return c//n,c,n
# 定义可变参数函数(*n可给变量可不给变量)
def c3(num,*n):
    c=1
    for i in range(1,num+1):
        c*=i
    for j in n:
        c*=j
    return c
# 定义lambda函数
f=lambda x,y:x+y
a=eval(input())
print(c1(a))
print(c2(a,2))
print(int(c3(a,2,0.5,5,0.2)))
print(f(a,a))

'''
用lambda函数和sort函数实现排序(实现按照长度递增)
list.sort()函数
函数原型：list.sort(key = None, reverse = False)
参数解析：
key参数（元素的属性）按照属性进行排序：
一般来说格式为 key = 函数名，这个函数在我们编写的时候只存在一个参数，这个参数取自列表中

reverse参数（正序还是逆序）：
reverse = True 降序排序，reverse = False 升序排序，默认升序排序
'''
lst=['Apple', 'Grape', 'Orange', 'Pear', 'Cheery', 'Bluebrrey', 'Dew']
lst.sort(key=lambda st:len(st),reverse=False)
print(lst)