def lon(i):
    c=0
    while i>=1:
        i=i/10
        c +=1
    return c

ls=[]
a=eval(input("请输入以','为分隔的自然数列表:"))
for i in a:
    ls.append(lon(i))
print(ls)