# question 1
str1 = input("请输入字符串")
dic1 = {}
for i in str1:
    if i in dic1.keys():
        dic1[i] += 1
    else:
        dic1.update({i: 1})
for i, j in dic1.items():
    print("{}出现{}次".format(i, j))