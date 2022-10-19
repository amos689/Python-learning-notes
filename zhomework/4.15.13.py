#question 13
str1=input("请输入一个字符串")
ls=[]
str1=' '.join(str1.split())
ls=str1.split(" ")
dic={}
for i in ls:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic.update({i:1})
print(dic)
        