#question 15
import random
x=[random.randint(1,100) for i in range(20)]
print("排序前：",x)
a=sorted(x[0::2])
''' del x[0:20:2]
for i in range(20):
    if i%2==0:
        x.insert(i,a[i//2])
print("排序后：",x) '''
x[0:20:2]=a
print("排序后：",x)
    