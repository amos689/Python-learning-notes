a=eval(input("请输入以','为分隔的自然数列表:"))
b=eval(input("请输入以','为分隔的自然数列表(与第一个等长):"))
ans=sum(i*j for i,j in zip(a,b))
print(ans)