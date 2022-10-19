# 试验一第一题
ls = [2]
for i in range(3, 101):
    flag = 1
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        ls.append(i)
for i in ls:
    print("*"*i)

# 试验一第二题
str1 = input("请输入字符串")
dic1 = {}
for i in str1:
    if i in dic1.keys():
        dic1[i] += 1
    else:
        dic1.update({i: 1})
for i, j in dic1.items():
    print("{}出现{}次".format(i, j))
