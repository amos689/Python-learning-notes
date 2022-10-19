#实验三第二题
import numpy as np
import random as rd

ls1=np.arange(5,33,3)
print(ls1,end='\n\n')

ls2=np.array([rd.randint(1,100) for i in range(9)]).reshape(3,3)
for i in range(3):
    for j in range(3):
        if i==0 or j==0 or i==2 or j==2:
            ls2[i][j]=0
        else:
            ls2[i][j]=1
print(ls2,end='\n\n')

ls3=np.array([[rd.randint(1,10) for i in range(2)] for j in range(3)]).reshape(2,3)
print(ls3,end='\n\n')

ls4=np.array([[rd.uniform(5,10) for i in range(3)]for j in range(5)]).round(2)
print(ls4,end='\n\n')

a=np.array([1,2,3,4,5])
b=np.array([4,5,6,7,8])
dis=np.sqrt(np.sum(np.square(a-b)))
print("{:.3f}".format(float(dis)),end='\n\n')