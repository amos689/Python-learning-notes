# question 4
ls=eval(input("请输入由三个元素组成的列表"))
sum=0
for i in range(ls[0],ls[1]+1):
    if i%ls[2]==0:
        sum+=i
print(sum)