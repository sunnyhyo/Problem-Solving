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
a1=turtle.Turtle()  #소행성1
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300,300),random.randint(-300,300))

a2=turtle.Turtle()  #소행성2
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300,300),random.randint(-300,300))


#이벤트 처리하기

def turnleft():
    player.left(30)  #왼쪽으로 30도 회전한다

def turnright():
    player.right(30) #오른쪽으로 30도 회전한다

def b():
    player.home()
    a1.home()
    a2.home()

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(turnright,"Up")
screen.onkeypress(b,"Down")
screen.listen()  #거북이 그래픽 창이 키보드  입력을 받는다.


#이동하기
def play():  #2 픽셀 전
    player.forward(3)
    a1.forward(2)
    a2.forward(2)
    screen.ontimer(play,10) #10초가 지나면 자동으로 호출 

screen.ontimer(play,10)




#stop up key  누르면 stop 함수 호출
변수 하나를 global 로 , moving =False
if moving 호출
if not moving 호출 안함

#격추여부 변수
forward 할지 말지 결정
#격추 여부를 확인
우주선의 중심에서 소행선 사이의 거리가 12 미만이면 격추된 것으로 간주
#두 소행선이 모두 격추되면 game over라고 화면에 출력
start time end time
#space 키르 누르면 우주선의 속도가 빨라진다
#소행선이 화면 바깥으로 나갔는지 체크
-500,500안에 있는지 없는지 
