#lab10-ex3


import turtle


#사각형 그리는 drawSquare() 함수 정의
#매개변수(parameter): 사각형 한 변의 길이
def drawSquare(length):
    t.begin_fill()          
    t.pensize(3)            #도형 윤곽선 굵기
    t.fillcolor("green")    #도형 내부 채우기
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()



#좌표 이동하는 movePoint() 함수 정의
#매개변수: x좌표, y좌표
def movePoint(x,y):
    t.up()
    t.goto(x,y)
    t.down()


#사각형 그리는 프로그램
t=turtle.Turtle()
t.shape("turtle")

#좌표 이동 위해 movwPoint() 함수를 호출한다

movePoint(-200,60)
drawSquare(100)


movePoint(0,388)
drawSquare(100)

movePoint(200,-50)
drawSquare(100)
