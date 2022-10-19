sum=0
a=eval(input("请输入以','为分隔的自然数列表:"))
for i in a:
    sum+=i
avg=sum/len(a)
print("平均数是：{:.3f}".format(avg))