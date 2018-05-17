#에스터로이드 게임

import turtle
import random
import math

#우주선 만들기

player=turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen=player.getscreen()

#소행성 만들기

a1=turtle.Turtle()
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300,300),random.randint(-300,300))

a2=turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300,300),random.randint(-300,300))


#이벤트 처리하기

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def b():
    player.home()
    a1.home()
    a2.home()

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(turnright,"Up")
screen.onkeypress(b,"Down")
screen.listen()

#이동하기

def play():
    player.forward(3)
    a1.forward(2)
    a2.forward(2)
    screen.ontimer(play,10) #10초가 지나면 자동으로 호출 

screen.ontimer(play,10)

