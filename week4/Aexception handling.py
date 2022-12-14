'''
异常处理
捕捉异常可以使用try/except语句。
try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
如果你不想在异常发生时结束你的程序，只需在try里捕获它。

语法：
以下为简单的try....except...else的语法：
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
finally:
    <语句>        #程序一定执行
    try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，
try子句先执行，接下来会发生什么依赖于执行时是否出现异常。
    如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，
控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
    如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，
或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
    如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
'''
import time as t
st=t.perf_counter()
try:
    guess=eval(input())
except SyntaxError:
    print("wrong input,exit(1)")
except NameError:
    print("wrong input,exit(2)")
else:
    try:
        print(guess**2)
    except TypeError:
        print("wrong input,exit(3)")
finally:
    end=t.perf_counter()
    print("{:-^30.6f}".format(end-st))
'''
Python常见异常类型大概分为以下类：

    1.AssertionError：当assert断言条件为假的时候抛出的异常

    2.AttributeError：当访问的对象属性不存在的时候抛出的异常

    3.IndexError：超出对象索引的范围时抛出的异常

    4.KeyError：在字典中查找一个不存在的key抛出的异常

    5.NameError：访问一个不存在的变量时抛出的异常

    6.OSError：操作系统产生的异常

    7.SyntaxError：语法错误时会抛出此异常

    8.TypeError：类型错误，通常是不通类型之间的操作会出现此异常

    9.ZeroDivisionError：进行数学运算时除数为0时会出现此异常
'''