import numpy as np

print(type(np.identity(3)))
a=np.diag([1,2,3,4])
print(a,type(a))
b=np.matrix([[1,2,3],[4,5,6]])
print(b,type(b))
c=np.array([2,1,5,4,6,3])
print(c.sort(),c)
print(np.round(np.cos(c),2))
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c.T)