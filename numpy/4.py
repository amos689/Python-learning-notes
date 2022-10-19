import numpy as np

t1=np.array([[0,1,2,3,4,5],[6,7,8,9,10,11]])
t2=np.array([[12,13,14,15,16,17],[18,19,20,21,22,23]])
#拼接
#水平拼接
print(np.hstack((t1,t2)))#注意括号，要两层
t=np.vstack((t1,t2))
print('\n')
#竖直拼接
print(np.vstack((t1,t2)))
print('\n')
print(t)
print('\n')
#行列交换
#行交换
t[[1,2],:]=t[[2,1],:]
print(t)
print('\n')
#列交换
t[:,[0,2]]=t[:,[2,0]]
print(t)
print('\n')
