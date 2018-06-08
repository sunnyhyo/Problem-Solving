#에스터로이드 게임

import turtle
import random
import time


#우주선 만들기
player=turtle.Turtle()      #우주선(파랑색, 거북모양)
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen=player.getscreen()

#소행성 만들기
a1=turtle.Turtle()  #소행성1(빨간색, 동그라미)
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300,300),random.randint(-300,300))

a2=turtle.Turtle()  #소행성2(빨간색, 동그라미)
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300,300),random.randint(-300,300))


#함수들

def turnLeft():  #왼쪽으로 30도 회전
    player.left(30)  

def turnRight():  #오른쪽으로 30도 회전
    player.right(30) 




speed =2
def speedUp():      #속도 높이는 함수
    global speed
    speed+=1
    if speed>5:     #최대 5까지
        speed=2

def start():    #게임을 시작하는 함수
    global playing
    if playing == False:
        playing= True
        player.clear
        play() #메세지를 지웁니다

a1_stop=False
a2_stop=False
def play():      #게임을 실제로 플레이 하는 함수
    global a1_stop
    global a2_stop
    
    player.forward(speed)
    if a1_stop == False: a1.forward(2)
    if a2_stop == False: a2.forward(2)

    
    if a1.xcor()> 500 :
        a1.goto(random.randint(-300,300),random.randint(-300,300))
    if a2.xcor()> 500 : 
        a1.goto(random.randint(-300,300),random.randint(-300,300))
    
    if player.distance(a1) <12:
        a1.color("black")
        a1_stop=True
    
    if player.distance(a2) <12:
        a2.color("black")
        a2_stop=True

    if (a1_stop == True) and (a2_stop==True):
        time_end =time.time()
        player.write("Game Over : %0.2f 초" %(time_end - time_start), False, "center", ("",15) )
    
    else:
        screen.ontimer(play,10)
        

    

#게임실행
time_start =time.time()
screen.ontimer(play,10)
screen.onkeypress(turnLeft,"Left")      #Left 키를 누르면 turnLeft 함수 호출
screen.onkeypress(turnRight,"Right")    #Right 키를 누르면 turnRight 함수 호출
screen.onkeypress(speedUp, "space")     #space 키를 누르면 speed 함수 호출
screen.listen()  #거북이 그래픽 창이 키보드  입력을 받는다.
    



