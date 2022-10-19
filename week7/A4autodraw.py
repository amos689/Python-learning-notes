#第一个表示前进距离，第二个表示左右(1右2左)转向，第三个表示转向角度，最后三个表示rgb三通道值
from turtle import *
f=open("E:\learning notes\C_learing\pyexperiment\week7\A4.txt","r",encoding="UTF-8")
setup(800,600)
pensize(5)
speed(10)
title("auto_draw")
drw=[]
for i in f:
    i=i.replace("\n","")
    drw.append(list(map(eval,i.split(","))))
f.close()
for i in range(len(drw)):
    pencolor(drw[i][3],drw[i][4],drw[i][5])
    fd(drw[i][0])
    if drw[i][1]:
        right(drw[i][2])
    else:
        left(drw[i][2])
hideturtle()
done()