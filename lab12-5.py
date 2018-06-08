#실습5

import turtle
def play():
    t.forward(2)
    if t.xcor() > 500 : t.goto(0,0)
    screen.ontimer(play, 10)

t = turtle.Turtle()
t.shape("turtle")
t.up()
screen = t.getscreen()

screen.ontimer(play, 10)

