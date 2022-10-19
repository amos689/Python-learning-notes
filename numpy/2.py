import numpy as np
#shape返回的是一个元组，所以reshape时也要输入元组
#一维
t1=np.arange(12)
print(t1,t1.shape)
#二维
t2=np.array([[1,2,3],[4,5,6]])
print(t2,t2.shape)
#三维
t3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3,t3.shape)
#更改形状
t4=np.array([i for i in range(24)])
t4=t4.reshape((4,6))
print(t4,t4.shape)

t5=np.arange(24).reshape(2,3,4)#2,3,4分别代表块，行，列
print(t5,t5.shape)
#展开成一维
print(t5.flatten())
#数组与数字的计算（广播机制）
print(t5+2)
print(t5*2)
print(t5/0)#nan==0/0,inf==num/0
#矩阵相加减，必须行/列相同（必须有一个维度相同）
t6=np.arange(100,124).reshape(4,6)
print(t6+t4)
t7=np.array([0,1,2,3,4,5])
print(t4-t7)#第一列做差
t8=np.arange(4).reshape(4,1)
print(t8,'\n',t4-t8)#第一列做差




