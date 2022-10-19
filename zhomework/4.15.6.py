#question 6
dic={}
ls=[]
while True:
    str1=input("请输入单词：")
    if str1=="exit":
        break
    else:
        ls.append(str1)
for i in ls:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic.update({i:1})
for i,j in dic.items():
    print("{} {}".format(j,i))