# 用递归完成汉诺塔

from time import perf_counter
start=perf_counter()
t=0
def hanoi(num,st,mid,to):
    global t
    if num==1:
        print("{}:{}->{}".format(1,st,to))
        t+=1
    else:
        hanoi(num-1,st,to,mid)
        print("{}:{}->{}".format(num,st,to))
        t+=1
        hanoi(num-1,mid,st,to)
        
num=eval(input())
hanoi(num,'A','B','C')
print('汉诺塔完成，公用{}步，程序运行{:.2f}秒'.format(t,(perf_counter()-start)))