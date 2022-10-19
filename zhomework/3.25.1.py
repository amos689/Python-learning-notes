#实验三第一题
with open("test.csv",'w',encoding="UTF8") as fc:
    ls1=['城市:,','环比,','同比,','定基','\n']
    ls2=['北京:,','101.5,','120.7,','121.4','\n']
    ls3=['上海:,','101.2,','127.3,','127.8','\n']
    ls4=['广州:,','102.0,','140.9,','145.5','\n']
    ls5=["深圳:,","102.0,","140.9,","145.5",'\n']
    ls6=["沈阳:,","100.1,","101.4,","101.6",'\n']
    ls7=[ls1,ls2,ls3,ls4,ls5,ls6]
    for i in ls7:
        fc.writelines(i)
with open("test.csv",'r',encoding="UTF8") as fc:
    for i in fc.readlines():
        print(i,end='')
