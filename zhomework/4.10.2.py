# 试验二第一题
import random as rd
name = ["root"]
passwd = {"passwd": "123456"}
for i in range(3):
    inp1 = input("请输入账号")
    if inp1 in name:
        inp2 = input("请输入密码")
        if inp2 == passwd["passwd"]:
            print("登录成功")
            break
        if inp2 != passwd["passwd"]:
            print("密码错误,你还有{}次机会".format(2-i))
    else:
        print("账号错误,你还有{}次机会".format(2-i))
    if i == 2:
        print("三次错误，程序退出！")
        exit()
print("请选择你要完成的任务:")
print("******************************")
print("1 计算1到100的和")
print("2 输出1到100的偶数")
inp3 = eval(input())
if inp3 == 1:
    sum = 0
    for i in range(1, 101, 1):
        sum += i
    print(sum)
elif inp3 == 2:
    ls = []
    for i in range(1, 101, 1):
        if i % 2 == 0:
            ls.append(i)
    print(ls)
else:
    print("非法输入，程序结束")

# 实验二第二题
num = [rd.randint(1, 100) for i in range(20)]
a = sorted(num[:10])
b = sorted(num[10:], reverse=True)
print(a+b)

# 实验二第三题
x = eval(input("请输入一个数字"))
if x < 0:
    print(0)
elif 0 <= x < 5:
    print(x)
elif 5 <= x < 10:
    print(x*3-5)
elif 10 <= x < 20:
    print(x*0.5-2)
else:
    print(0)

# 实验二第四题


def move(n, a, b, c):
    if(n == 1):
        print(a, "->", c)
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)


n = eval(input("请输入汉诺塔层数"))
move(n, "a", "b", "c")
