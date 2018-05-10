# 사각형 바깥 테두리를 굵게하기

import turtle

def drawSquare(length):
    t.begin_fill()
    t.pensize(3)
    t.fillcolor("green")  #도형 내부 채우기
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

t=turtle.Turtle()

t.up()
t.goto(-200,0)
t.down()
drawSquare(100)


t.up()
t.goto(0,0)
t.down()
drawSquare(100)


t.up()
t.goto(200,0)
t.down()
drawSquare(100)



