#########################################
#과제2-1
#에스터로이드 게임
#1585063 박효선
#########################################
####모듈호출
import turtle
import random
import time



#########################################
####스크린 위에 우주선, 소행성1, 소행성2를 그리기
#우주선 만들기
player=turtle.Turtle()      #player= 우주선(파랑색, 거북모양)
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen=player.getscreen()

#소행성 만들기
a1=turtle.Turtle()  #a1= 소행성1(빨간색, 동그라미)
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1_play_range =random.randint(-300,300)  #게임 플레이 범위
a1.goto(a1_play_range, a1_play_range)

a2=turtle.Turtle()  #a2= 소행성2(빨간색, 동그라미)
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2_play_range =random.randint(-300,300)  #게임 플레이 범위
a2.goto(a2_play_range, a2_play_range)




########################################
#### 함수정의

# turnLeft  함수 정의
#왼쪽으로 30도 회전
def turnLeft():  
    player.left(30)  

#turnRight 함수 정의
#오른쪽으로 30도 회전
def turnRight():  
    player.right(30) 

#속도조절 함수 정의
#속도는 기본2 에서 최대5 까지 높이기
speed =2
def speedUp():      
    global speed
    speed+=1
    if speed>5:     #속도 5를 넘으면 다시 속도 2
        speed=2

        

#play 함수 정의
#실제 게임의 이벤트
a1_moving=True  
a2_moving=True   

def play():      
    global a1_moving
    global a2_moving
    global a1_play_range
    global a2_play_range


    #우주선, 소행성1, 소행성2 움직임
    player.forward(speed)   
    if a1_moving == True: a1.forward(2)  #소행성1 움직이는 상태
    if a2_moving == True: a2.forward(2)  #소행성2 움직이는 상태


    #소행성이 범위 바깥으로 나가면
    #범위 내 임의의 지점으로 불러오기
    if a1.xcor()> 500 : a1.goto(a1_play_range, a1_play_range)
    if a2.xcor()> 500 : a2.goto(a2_play_range, a2_play_range)


    #우주선과 소행성이 충돌하면
    #소행성 검정색, 소행성 멈춤 plague
    if player.distance(a1) < 12:
        a1.color("black")  
        a1_moving=False                
    if player.distance(a2) < 12:
        a2.color("black")
        a2_moving=False


    #게임종료판단
    #게임종료o: 소행성1,2 모두 멈춤 상태
    if (a1_moving == False) and (a2_moving == False):
        time_end =time.time()                         #종료시점 측정
        play_time= time_end - time_start    #플레이타임 
        player.write("Game Over : %0.2f 초" %(play_time), False, "center", ("",15) ) 

    #게임종료x: play 함수 호출 
    else: screen.ontimer(play,10)
        

    
############################
#게임 실행하기

time_start =time.time()           #시작시점 측정
screen.ontimer(play,10)         #게임 시작: play 함수 호출 
screen.onkeypress(turnLeft,"Left")          #Left 키를 누르면 turnLeft 함수 호출
screen.onkeypress(turnRight,"Right")    #Right 키를 누르면 turnRight 함수 호출
screen.onkeypress(speedUp, "space")    #space 키를 누르면 speed 함수 호출
screen.listen()                                                  #거북이 그래픽 창이 키보드  입력을 받는다.
    



