#외부 이미지 사용
import turtle
import random
import time

screen=turtle.Screen()
image1="C:\\Users\\user\\Downloads\\rabbit.gif"
image2="C:\\Users\\user\\Downloads\\turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()    # 첫 번째 거북이를 생성한다.
t1.shape(image1)
t1.pensize(5)           # 팬의 두께를 5로 한다.
t1.penup()              # 펜을 든다.
t1.goto(-300, 0)        # (-300, 0) 위치로 간다.

t2 = turtle.Turtle()    # 두 번째 거북이를 생성한다.
t2.shape(image2)
t2.pensize(5)           # 팬의 두께를 5로 한다.
t2.penup()              # 펜을 든다.
t2.goto(-300, -200)     # (-300, -200) 위치로 간다.


t1.pendown()
t2.pendown()
t1.speed(1)
t1.speed(1)

start=time.time()

for i in range(30):
    d1=random.randint(1,50)
    t1.forward(d1)
    d2=random.randint(1,50)
    t2.forward(d2)

end=time.time()
et=end-start
print("달리기 시간: %0.2f" %et)
