#lab10-ex1

#다음을 30번 반복수행
# [1, 100] 사이의 난수를 발생하여 변수 lengt에 저장한다.
#• 거북이를 length 만큼 움직인다.
#• [-180, 180] 사이의 난수를 발생하여 변수 angle에 저장한다.
#• 거북이를 angle 만큼 회전시킨다


import turtle
import random
t=turtle.Turtle()
t.shape("turtle")

for i in range(30):
    length = random.randint(1,100)
    t.forward(length)
    angle=random.randint(-180,180)
    t.right(angle)
