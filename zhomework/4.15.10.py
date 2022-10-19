#question 10
n=eval(input("请输入克数："))
sum=0
p=input("是否加急：Y是，N否")
if p=="Y":
    sum+=5
if n<=1000:
    sum+=8
else:
    sum+=8
    n1=n-1000
    a=int(n1/500)
    b=n1%500
    if b!=0:
        a+=1
    sum+=4*a
print("{}元".format(sum))
        