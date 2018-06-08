#실습3

import turtle

speed=2

def speedUp():
    global speed
    speed +=1

def play():
    t.forward(speed)
    screen.ontimer(play,10)

t=turtle.Turtle()
t.up()
t.goto(-500,0)

screen = t.getscreen()
screen.ontimer(play,10)
screen.onkeypress(speedUp, "space")
screen.listen()
