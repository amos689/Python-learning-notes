#question 8
num=eval(input("请输入一个数字"))
flag=1
if num<=1:
    flag=0
for i in range(2,num):
    if(num%i==0):
        flag=0
        break
if flag==1:
    print("YES")
else:
    print("NO")