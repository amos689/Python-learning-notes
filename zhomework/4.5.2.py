import numpy as np
import random as rd
a1=np.array([0]*10)
print(a1)
a1[4]=1
print(a1)
a2=np.array([[j for j in range(3)] for i in range(3)])
for i in range(3):
    for j in range(3):
        if i==0 or i==2 or j==0 or j==2:
            a2[i][j]=1
        else:
            a2[i][j]=0
print(a2)
a3=np.array([[rd.randint(1,1000) for i in range(10)] for j in range(10)])
print("max={},min={},mean={}".format(np.max(a3),np.min(a3),np.mean(a3)))
