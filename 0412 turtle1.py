#정오각형 그리기 프로그램

import turtle as t

n=5                     #오각형을 그림
t.color("purple")       
t.begin_fill()          #색칠할 영역을 시작함
for x in range(n):      #n 번 반복
    t.forward(50)       #거북이 50만큼 앞으로 이동
    t.left(360/n)       #거북이 360/n만큼 왼쪽으로 회전
t.end_fill()            #색칠할 영역을 마무리
