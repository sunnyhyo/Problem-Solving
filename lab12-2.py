#실습2


import turtle

def moveStop():
    global t1_stop
    t1_stop=True

def play():
    if t1_stop==False:
        t1.forward(2)
    t2.forward(2)
    screen.ontimer(play,10)

t1=turtle.Turtle()
t1.up()
t1.goto(-300,0)
screen=t1.getscreen()

t2=turtle.Turtle()
t2.up()
t2.goto(-300,100)
screen=t2.getscreen()

t1_stop=False

screen.ontimer(play,10)
screen.onkeypress(moveStop, "Up")
screen.listen()
