# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:25:20 2018

@author: HS
"""

#에스터로이드 게임

import turtle
import random

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



def turnLeft():  #왼쪽으로 30도 회전
    player.left(30)  

def turnRight():  #오른쪽으로 30도 회전
    player.right(30) 

stop= False
def moveStop():  #움직임을 멈춤
    global stop
    stop= True
    #UP키 한번 더 누르면 다시 작동하게 


speed =2
def speedUp():      #속도 높이는 함수
    global speed
    speed+=1
    if speed>5:     #최대 5까지
        speed=5
    
def goHome():       #소행성, 우주선을 초기 상태로 만들어 시작
    player.home()
    a1.home()
    a2.home()

def start():    #게임을 시작하는 함수
    global playing
    if playing == False:
        playing= True
        player.clear
        play() #메세지를 지웁니다

playing = True
def play():      #게임을 실제로 플레이 하는 함수
    global playing
    global stop
    
    if playing:
        screen.ontimer(play,10)
    
    if stop == False: 
        player.forward(speed)
    
    if a1.xcor()> 500 or a1.ycor()>500 :
        a1.goto(random.randint(-300,300),random.randint(-300,300))
    if a2.xcor()> 500 or a2.ycor()>500 : 
        a1.goto(random.randint(-300,300),random.randint(-300,300))
    
    if player.distance(a1) <12:
        a1.color("black")
    else: a1.forward(2)
    
    if player.distance(a2) <12:
        a2.color("black")
    else: a2.forward(2)
    
    if player.distance(a1) <12 and player.distance(a2) <12:
        playing = False
        player.write("Game Over", False, "center", ("",15))

    
    
screen.ontimer(play, 10)
screen.onkeypress(turnLeft,"Left")      #Left 키를 누르면 turnLeft 함수 호출
screen.onkeypress(turnRight,"Right")    #Right 키를 누르면 turnRight 함수 호출
screen.onkeypress(moveStop, "Up")       #UP 키를 누르면 moveStop 함수 호출
screen.onkeypress(goHome,"Down")        #Down 키를 누르면 goHome 함수 호출
screen.onkeypress(speedUp, "space")     #space 키를 누르면 speed 함수 호출

screen.listen()  #거북이 그래픽 창이 키보드  입력을 받는다.
    



