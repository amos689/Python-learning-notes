'''lambda
def f(num):
    return num**2
等价于
f=lambda x: x**2

def g(x,y):
    return x+y
等价于
g=lambda x,y : x+y
'''
with open("price.csv",'r',encoding="UTF8") as f:
    ls=[]
    n=1
    for i in f:
        if n==1:
            n+=1
            continue
        else:
            a=tuple(i.split(","))
            ls.append(a)
print(ls)
ls.sort(key=lambda x:x[2],reverse=True)
print(ls)
print(max(ls,key=lambda x:x[2]))