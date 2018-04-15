#원을 반복해서 그리는 프로그램

import turtle as t

n=50
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):   #n번 반복
    t.circle(80)     #현재 위치에서 반지름이 80인 원을 그림
    t.left(360/n)    #360/n만큼 거북이를 왼쪽으로 회전
 
