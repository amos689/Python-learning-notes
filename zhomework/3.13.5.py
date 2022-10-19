a=eval(input("请输入以','为分隔的自然数列表:"))
ans=1
for i in a:
    ans*=i
print(ans)