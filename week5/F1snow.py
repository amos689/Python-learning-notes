from turtle import*

setup(1000,600)
speed(10)

def dwsno(size,n):
    if n==0:
        fd(size)
    else:
        for angle in [0,60,-120,60]:
            left(angle)
            dwsno(size/3,n-1)

def dwcil():
    penup()
    goto(60,30)
    pendown()
    circle(70.7,360)
    
def main():
    penup()
    goto(-200,100)
    pendown()
    pensize(3)
    dwsno(400,3)
    right(120)
    dwsno(400,3)
    right(120)
    dwsno(400,3)
    dwcil()
    hideturtle()
    done()

main()