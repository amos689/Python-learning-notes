import pandas as pd
text=pd.read_excel("E:\\learning notes\\C_learing\\pyexperiment\\pandas\\fruit.xlsx")
print(text[:10])
print(text[2:8])
print(len(text))
print(text['Sale'].sum())
print(text['Sale'].describe())
for i in ['Grape','Banana','Peach','Pear']:
    print(text[text.Fruit==i]['Sale'].sum())
data=dict()
for i in text['Fruit']:
    data[i]=text.groupby(by='Date')['Sale'].sum()
print(data)
dic={}
for i in text.iterrows():
    if i[1][1] not in dic.keys():
        dic.update({i[1][1]:i[1][2]})
    elif i[1][1] in dic.keys():
        dic[i[1][1]]+=i[1][2]
print(dic)
