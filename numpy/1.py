import numpy as np
import random as rd
t1=np.array([1,2,3])
print(t1)
print(type(t1),end="\n\n")
t2=np.array(range(10))
print(t2,end="\n\n")
t3=np.arange(12)
print(t3,end="\n\n")
t4=np.arange(4,10,2)
print(t4)
print(t4.dtype,end="\n\n")
t5=np.array(range(1,4),dtype=float)
print(t5,t5.dtype,end="\n\n")
t6=np.array([1,1,0,1,0,1,0,0],dtype=bool)
print(t6,t6.dtype,end="\n\n")
t7=t6.astype("int64")
print(t7,t7.dtype,end="\n\n")

#不要忘了加[]
t8=np.array([rd.random() for i in range(10)])
t8=np.round(t8,2)
print(t8,t8.dtype,end="\n\n")
