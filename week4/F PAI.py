from random import*
from time import*
dirt=100000000
hits=0.0
start=perf_counter()
for i in range(dirt):
    x,y=random(),random()
    dis=pow(x**2+y**2,0.5)
    if dis<=1.0:
        hits+=1
pai=4*(hits/dirt)
print("pai={:.5f}".format(pai))
print("excuting time:{:.5f}s".format(perf_counter()-start))