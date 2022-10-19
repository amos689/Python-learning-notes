import pandas as pd

t1=pd.DataFrame(pd.read_excel("E:\\learning notes\\C_learing\\pyexperiment\\pandas\\fruit.xlsx"))
#b 显示前十行，第2:8行
print(t1.head(10),end="\n\n")
print(t1.loc[1:8],end="\n\n")
#c 查询有多少行
print(t1.index.size,end="\n\n")
#d 计算总销量
sale1=0
for i in t1["Sale"]:
    sale1+=i
print(sale1,end="\n\n")
#e 查询销量统计信息
# dic1={"Grape":0,"Banana":0,"Peach":0,"Pear":0}
# for i in t1.iterrows():
#     if i[1][1] in dic1.keys():
#         dic1[i[1][1]]+=i[1][2]
# print(dic1,end="\n\n")
#f 循环遍历["Grape","Banana","Peach","Pear"]每个水果总销量
ls1=["Grape","Banana","Peach","Pear"]
dic2={}
for i in t1.iterrows():
    if i[1][1] in ls1 and i[1][1] in dic2.keys():
        dic2[i[1][1]]+=i[1][2]
    elif i[1][1] in ls1 and i[1][1] not in dic2.keys():
        dic2.update({i[1][1]:i[1][2]})
print(dic2)
#g1 按截止日期计算水果总销量
dic3={}
for i in t1.iterrows():
    if i[1][0] not in dic3.keys():
        dic3.update({i[1][0]:i[1][2]})
    elif i[1][0] in dic3.keys():
        dic3[i[1][0]]+=i[1][2]
print(dic3)
#g2 按水果种类计算水果总销售量
dic4={}
for i in t1.iterrows():
    if i[1][1] not in dic4.keys():
        dic4.update({i[1][1]:i[1][2]})
    elif i[1][1] in dic4.keys():
        dic4[i[1][1]]+=i[1][2]
print(dic4)











