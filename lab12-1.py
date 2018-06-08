#실습1

import turtle

def play():
    t.forward(2)
    screen.ontimer(play, 10)

t=turtle.Turtle()
t.up()


screen=t.getscreen()
screen.ontimer(play,10)


import turtle

stop=False

def moveStop():
    global stop
    stop=True

def play():
    t.forward(2)
    if stop ==False:
        screen.ontimer(play, 10)

t=turtle.Turtle()
t.up()

screen = t.getscreen()
screen.ontimer(play,10)
screen.onkeypress(moveStop, "Up")
screen.listen()
