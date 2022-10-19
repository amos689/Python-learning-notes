#question 15
import random
x=[random.randint(1,100) for i in range(20)]
print("排序前：",x)
a=sorted(x[0::2])
b=(x[1::2])
c=[]
for i in a[:]:
    c.append(i)
    a.remove(i)
    for j in b:
        c.append(j)
        b.remove(j)
        break
print("排序后：",c)
