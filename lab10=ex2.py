#lab10-ex2

import turtle

#사각형 그리는 drawSquare() 함수 정의
#매개변수,인자(parameter): 사각형 한 변의 길이

def drawSquare(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


#사각형 그리는 프로그램

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

