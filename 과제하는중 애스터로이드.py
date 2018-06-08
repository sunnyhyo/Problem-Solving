# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 22:37:09 2018

@author: HS
"""

#에스터로이드 게임

import turtle
import random

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

def turnLeft():  #왼쪽으로 30도 회전
    player.left(30)  

def turnRight():  #오른쪽으로 30도 회전
    player.right(30) 

stop= False
a1_stop=False
a2_stop=False
def moveStop():  #움직임을 멈춤
    global stop
    global t1_stop
    global t2_stop
    stop= True
    a1_stop= True
    a2_stop= True

def goHome():       #소행성, 우주선을 초기 상태로 만들어 시작
    player.home()
    a1.home()
    a2.home()

speed =2
def speedUp():      #속도 높이는 함수
    global speed
    speed+=1
    #최대 5까지

#이동하기
def play():  
    player.forward(speed)
    if stop == False: 
        screen.ontimer(play,10) #10초가 지나면 자동으로 호출 
    if a1_stop ==False:
        a1.forward(2)
    if a2_stop==False:
        a2.forward(2)
    if player.distance(a1)<12:
        a1.write("Game Over", False, "center", ("",15))
        a1.color("black")
    if player.distance(a2)<12:
        a2.write("Game Over", False, "center", ("",15))
        a2.color("black")
    else: screen.ontimer(play, 10)
    if a1.xcor()> 500 : a1.goto(random.randint(-300,300),random.randint(-300,300))
    if a1.xcor()> 500 : a1.goto(random.randint(-300,300),random.randint(-300,300))
    else: screen.ontimer(play, 10)




screen.onkeypress(turnLeft,"Left")      #Left 키를 누르면 turnLeft 함수 호출
screen.onkeypress(turnRight,"Right")    #Right 키를 누르면 turnRight 함수 호출
screen.onkeypress(moveStop, "Up")       #UP 키를 누르면 moveStop 함수 호출
screen.onkeypress(goHome,"Down")        #Down 키를 누르면 goHome 함수 호출
screen.onkeypress(speedUp, "space")     #space 키를 누르면 speed 함수 호출

screen.listen()  #거북이 그래픽 창이 키보드  입력을 받는다.


