import numpy as np
uk='GB_video_data_numbers.csv'
#delimiter取以。。为分割，dtype按什么方式解析，unpack转置
t=np.loadtxt(uk,delimiter=',',dtype="int64")
print(t)
print('\n')
#取行(第三行)
print(t[2])
print('\n')
#切片，连续的多行
print(t[2:])
print('\n')
#切片，不连续的多行(如2810行)
print(t[[2,8,10]])
print('\n')
#取列(第一列)
print(t[:,0])
print('\n')
#取连续列（3开始每一列）
print(t[:,2:])
print('\n')
#取不连续
print(t[:,[0,2]])
print('\n')
#取第三行第四列
print(t[2,3],type(t[2,3]))#注意数据类型变化
#取多行和多列（取第三行到第五行，第二列到第四列）
a=t[2:5,1:4]#注意前闭后开
print(a)
#取多个不相邻点((0,0),(2,1),(2,3))
b=t[[0,2,2],[0,1,3]]
print(b)










