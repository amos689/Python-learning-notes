import pandas as pd
import numpy as np
#DataFrame 二维的Series容器(竖着叫index，横着叫column)
t1=pd.DataFrame(np.arange(12).reshape(3,4))
print(t1,end='\n\n')
#行索引，表明不同行，横向索引，axis=0,index
#列索引，表明不同列，纵向索引，axis=1,columns
t2=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(t2,end="\n\n")
#传入字典(两种方式)
d1={"name":["xiaoming","xiaohong"],"age":[20,32],"tel":[10086,10010]}
t3=pd.DataFrame(d1)
print(t3,end='\n\n')
d2=[{"name":"xiaohong","age":32,"tel":10010},{"name":"xiaogang","tel":10000},{"name":"xiaowang","age":22}]
t3=pd.DataFrame(d2)
print(t3,end='\n\n')
# t4=pd.DataFrame(pd.read_excel("E:\\learning notes\\C_learing\\pyexperiment\\pandas\\fruit.xlsx"))
# print(t4)



