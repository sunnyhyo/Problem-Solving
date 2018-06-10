# Lab9-5 (도형 그리기)

import turtle as t

#다각형을 그리기 함수 정의 작성
#파라미터로 받은 n각형을 그리는 함수
def drawPolagon(n):
    t.clear()
    for i in range(n):
        t.forward(100)
        t.right(360/n)

#별 그리기 함수 정의 작성
def drawStar():
    t.clear()
    for i in range(5):
        t.forward(100)
        t.right(144)

#메뉴 출력하는 함수 정의 작성
def showMenu():
    print("******* 메뉴 *******")
    print("1. 삼각형 그리기")
    print("2. 사각형 그리기")
    print("3. 오각형 그리기")
    print("4. 별 그리기")
    print("0. 종료")
    print("*****************")

#본 프로그램
while True:
    showMenu() #메뉴 출력하는 함수 호출
    menu = int(input("번호 입력:  "))  #원하는 도형 그릴 번호 선택

    if menu == 0: break
    elif menu < 0 or menu >4 : continue
    elif menu ==1: drawPloygon(3)
    elif menu ==2: drawPloygon(4)
    elif menu ==3: drawPloygon(5)
    elif menu ==4: drawStar()
