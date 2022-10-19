import pandas as pd
t1=pd.Series([1,2,31,12,3,4])
#第一列是索引(键)，第二列是数(值)(带标签的数)
print(t1,type(t1),end="\n\n")
t2=pd.Series([1,23,42,2,1],index=list("abcde"))
print(t2,end="\n\n")
dict1={"name":"xiaohong","age":38,"tel":10086}
t3=pd.Series(dict1)
print(t3,end="\n\n")
print(t3["age"],t3[1],end="\n\n")#索引和位置都可以
#一下三种方法一样
print(t3[:3],end="\n\n")
print(t3[[0,1,2]],end="\n\n")
print(t3[["name","age","tel"]],end="\n\n")
#bool索引，搜索value中跟bool比关系的数
print(t1[t1>10],end="\n\n")
#series也分索引(index)和值(value),均为可迭代的
print(t3.index)
for i in t3.values:
    print(i,end="\n\n")

#读取文件
df=pd.read_excel("E:\\learning notes\\C_learing\\pyexperiment\\pandas\\fruit.xlsx")
print(df)






