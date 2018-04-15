#turtle4
import turtle


oh=[20,30,40]
for i in range(len(oh)):
    turtle.left(oh[i-1])
    for k in range(4):
        turtle.forward(50)
        turtle.left(90)

