'''
关于库函数声明
import 模块：导入一个模块；注：相当于导入的是一个文件夹，是个相对路径。

from…import：导入了一个模块中的一个函数；注：相当于导入的是一个文件夹中的文件，是个绝对路径。

from…import *：是把一个模块中所有函数都导入进来，
注：相当于：相当于导入的是一个文件夹中所有文件，所有函数都是绝对路径，不用再采用"<库名>.<函数名>(变量名)"格式了
'''
import turtle
turtle.setup(650,350,200,200)
'''
该函数各参数关系如图所示，其具体定义为：turtle.setup（width,height,startx,starty）
作用：设置主窗体的大小和位置。
width：窗口宽度，如果值是整数，表示像素值；如果值是小数，表示窗口宽度与屏幕的比例。
height：窗口高度，如果值是整数，表示像素值；如果值是小数，表示窗口高度与屏幕的比例。
startx：窗口左侧与屏幕左侧的像素距离，如果值是None，窗口位于屏幕水平中央。
starty：窗口顶部与屏幕顶部的像素距离，如果值是None，窗口位于屏幕垂直中央。
'''
turtle.penup()  #松开画笔，让海龟飞行。
turtle.fd(-250)     #沿当前直线运行
turtle.pendown()    #落下海龟，开始画图
turtle.pensize(25)
turtle.pencolor("cyan")
turtle.seth(-40)    #由圆心角定理，想海龟走直线，先转（80/2）°，改变海龟行进的方向（海龟前进的方向默认为零度）
for i in range(4):
    turtle.circle(40,80)    #以海龟左侧为正方向，40像素为半径，转80°
    turtle.circle(-40,80)   #以海龟左侧为正方向，-40像素为半径，转80°
turtle.circle(40,80/2)  #将龟头(???)摆正
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()