#question 12
n=eval(input("请输入个数："))
ls=[]
for i in range(n):
    ls.append(eval(input("请输入一个数字：")))
print(sum(ls),sum(ls)/n)