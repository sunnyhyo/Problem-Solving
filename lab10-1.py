
import turtle
import random

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

def randomLength():
    length= random.randint(50,100)
    return length

def x_coordinate():
    x= random.randint(-300,300)
    return x

def y_coordinate():
    y= random.randint(-200,200)
    return y


t=turtle.Turtle()
t.shape("turtle")

movePoint(x_coordinate,y_coordinate)
drawSquare(randomLength)


#movePoint(x,y)
#drawSquare(length)
