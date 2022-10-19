import numpy as np
a=np.random.randint(1,100,(2,3,4))
print(a,end='\n\n')
print(a.sum(axis=2))