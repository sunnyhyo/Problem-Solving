#실습4


import turtle

def play():
    t1.forward(2)
    t2.forward(2)
    if t1.distance(t2)<12:
        t1.write("Game Over", False, "center", ("",15) )
    else:
        screen.ontimer(play,10)

t1=turtle.Turtle()
t1.up()
t1.shape("turtle")
t1.goto(-300,0)
screen=t1.getscreen()

t2=turtle.Turtle()
t2.up()
t2.shape("turtle")
t2.goto(300,0)
t2.left(180)

screen.ontimer(play,10)
