'''这是我的第一个程序'''
#tempstr="82f" (向tempstr赋值82f)
# 命名规则：大小写字母，数字下划线，数字，中文等字符及其组合（大小写敏感，首字母不能是数字，不能与保留字相同）
# 保留字是编程语言基本单词，大小写敏感：if是保留字，IF是变量
#eval('print("Hello,world,Hello Amos.")')
'''
eval():脱下字符串的引号，表示本来含义
.format():将不同类型全部变成字符串类型
'''
temp = input("请输入需要转化的温度（摄氏温度后缀c/C，华氏温度后缀f/F）\n")
if temp[-1] in ['F', 'f']:
    c = (eval(temp[0:-1])-32)/1.8
    print("所对应的摄氏度为{:.2f}C".format(c))#此处冒号不能省略
elif temp[-1] in ['c', 'C']:
    f = eval(temp[0:-1])*1.8+32
    print("所对应的华氏度为{:.2f}F".format(f))
else:
    print("格式错误")
