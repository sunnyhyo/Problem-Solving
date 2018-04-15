import turtle as t


colors=["yello","red","greed","purple","blue"]

for i in range(len(colors)):
    t.up()
    t.goto((-300+(i*100)),0)
    t.down()

    t.width(3*i)
    t.color(colors[i])
    t.circle(10)
    
