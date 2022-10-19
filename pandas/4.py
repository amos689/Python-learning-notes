import pandas as pd
text=pd.read_excel(r"E:\\learning notes\\C_learing\\pyexperiment\\pandas\\fruit.xlsx")
'''基础篇'''
print(text,end="\n\n")
#查看前五行的Fruit和Sale的信息
print(text[["Fruit","Sale"]][:5],end='\n\n')    #先按要求选择再取前五
print(text[:5][["Fruit","Sale"]],end='\n\n')    #先取前五再按要求选择
print(text.loc[:,["Fruit","Sale"]][:5],end='\n\n')
#求销量总和
print(text.loc[:,["Sale"]].sum(),end="\n\n")
print(text["Sale"].sum())
#求葡萄出现次数
print(text.loc[:,["Fruit"]].isin(["Grape"]).sum(),end="\n\n")
print(text["Fruit"].isin(["Grape"]).sum(),end='\n\n')
#果然，我猜的没错:)
print(text[:5][[True,True,False,True,False]],end='\n\n')
#验证这两个的返回值不同，不能混淆
print(text["Fruit"].isin(["Grape"]),type(text["Fruit"].isin(["Grape"])),end='\n\n')#<class 'pandas.core.series.Series'>
print(text.loc[:,["Fruit"]].isin(["Grape"]),type(text.loc[:,["Fruit"]].isin(["Grape"])),end="\n\n")#<class 'pandas.core.frame.DataFrame'>
#求grape的销量和
print(text[text["Fruit"].isin(["Grape"])]["Sale"].sum(),end='\n\n')
#求单次交易在范围内的记录
print(text["Sale"].between(15,100),end='\n\n')
print(text[text["Sale"].between(15,100)],end='\n\n')

'''提高篇'''
print("提高篇",end="\n\n")
#查看交易额统计信息
print(text["Sale"].describe(),end='\n\n')
#查看交易额中值
print(text["Sale"].median(),end='\n\n')
#查看交易额最小的三条记录
print(text.nsmallest(3,"Sale"),end='\n\n')
#查看交易额最大的三条记录
print(text.nlargest(3,"Sale"),end='\n\n')
#最大的交易额
print(text["Sale"].max(),end='\n\n')
#最小的交易额
print(text["Sale"].min(),end='\n\n')
#第一个最大交易额下标和详细信息
index1=text["Sale"].idxmax()
print(index1)
print(text.loc[index1,["Date","Sale"]],end='\n\n')
#按交易额降序(这里是false)按时间升序(这里是true)
print(text.sort_values(by=["Sale","Date"],ascending=[False,True])[:15],end='\n\n')
#分组
print(text.groupby(by="Fruit")["Sale"].sum())
#md，不学了