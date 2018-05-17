#거북이 경주 게임

import turtle


t1=turtle.Turtle()  #첫번째 거북이
t2=turtle.Turtle()  #두번째 거북이


t1.penup()
t1.goto(-300,0)

t2.penup()
t2.goto(-300,-100)


t1.color("pink")
t1.shape("turtle")
t1.shapesize(2)
t1.pensize(5)

t2.color("blue")
t2.shape("turtle")
t2.shapesize(3)
t2.pensize(5)


import random
t1.pendown()
t2.pendown()

#달기기
for i in range(30):         #30번 반복한다
    d1=random.randint(1,50) #1부터 50 사이의 난수를 발생한다
    t1.forward(d1)          #난수만큼 이동한다
    d2=random.randint(1,50)
    t2.forward(d2)












