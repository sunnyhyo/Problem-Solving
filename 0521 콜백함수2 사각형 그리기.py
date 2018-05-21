import turtle

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawit(x, y):
    t.penup()   #꼬리 들고
    t.goto(x, y) #가고
    t.pendown() #꼬리 내리고
    t.begin_fill() #채울 준비 하고
    t.fillcolor("green")#색상준비
    square(50) #사각형그리고
    t.end_fill() #색상 채우기

# 거북이 한마리 준비.
t = turtle.Turtle()
# 그림이 그려지는 화면을 얻는다.
s = turtle.Screen()
# 마우스 클릭 이벤트 처리 함수를 등록한다.
s.onscreenclick(drawit)
