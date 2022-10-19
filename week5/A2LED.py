from turtle import*
from time import*
'''
write(arg,move=false,align='left',font=('arial',8,'normal'))
在当前乌龟位置写入文本。

arg--信息，将写入Turtle绘画屏幕。

move（可选）：在默认情况下，move为false。如果move为true，则笔将移动到右下角。

align（可选）：可取值是left即左、center即中、right即右之一，是字符串格式。

font（可选）：字体三元组（fontname、fontsize、fonttype），fontname即字体名称，fontsize即字体大小，
fonttype即字体类型如：normal、bold、italic。
'''
speed(10)
def drawGap(): #绘制数码管间隔
    penup()
    fd(5)
def drawLine(draw):   #绘制单段数码管
    pensize(6)
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup()
    fd(20)
def drawDate(date):
    pencolor("red")
    for i in date:
        if i == '-':
            write('年',font=("Arial", 26, "normal"))
            pencolor("green")
            fd(40)
        elif i == '=':
            write('月',font=("Arial", 26, "normal"))
            pencolor("blue")
            fd(40)
        elif i == '+':
            write('日',font=("Arial", 26, "normal"))
        else:
            drawDigit(eval(i))
def main():
    setup(800, 350, 200, 200)
    penup()
    fd(-350)
    pensize(5)
#    drawDate('2018-10=10+')
    drawDate(strftime('%Y-%m=%d+',gmtime()))
    hideturtle()
    done()
main()