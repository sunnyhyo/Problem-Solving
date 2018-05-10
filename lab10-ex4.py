#lab10-ex4

import turtle


#사각형 그리는 drawSquare() 함수 정의
#매개변수(parameter): 사각형 한 변의 길이
def drawSquare(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


#좌표 이동하는 movePoint() 함수 정의
#매개변수: x좌표, y좌표
def movePoint(x,y):
    t.up()
    t.goto(x,y)
    t.down()

#좌표 이동하고 사각형 그리는 drawlt() 함수 정의
#매개변수(parameter): x좌표, y좌표
def drawlt(x,y):
    movePoint(x,y)
    drawSquare(100)


#마우스 클릭하는 곳에 사각형 그리기

t=turtle.Turtle()
t.shape("turtle")
s=turtle.Screen()

#마우스 클릭하면 drawlt()함수를 호출한다.
s.onscreenclick(drawlt)
