#########################################
#과제2-2 
#Tic-Tac-Toe 게임
#1585063 박효선
#########################################
####모듈 호출
import time



#########################################
####함수 정의


#보드 그리는 drawBoard 함수 정의
board=[" "," "," "," "," "," "," "," "," "] 

def drawBoard():    
    print("  %c   |  %c  |   %c   " % (board[0],board[1],board[2]))    
    print("___|___|___")    
    print("  %c   |  %c  |   %c   " % (board[3],board[4],board[5]))    
    print("___|___|___")    
    print("  %c   |  %c  |   %c   " % (board[6],board[7],board[8]))    
    print("___|___|___")  



#게임의 종료를 확인하는 checkFinish 함수 정의
#게임종료:   승리조건, 무승부조건 만족하면 True 반환
#게임계속:   승리, 무승부 모두 아니면 False 반환 
def checkFinish():
    #승리조건1 : 가로빙고 체크
    #승자를 알기 위해 printWinner 함수로 pos 전달
    if   (board[0] == board[1] and board[1]== board[2] and board[0]!= ' '):
        printWinner(0)
        return True
    elif   (board[3] == board[4] and board[4] == board[5] and board[3]!= ' '):
        printWinner(3)
        return True
    elif   (board[6] == board[7] and board[7] == board[8] and board[6]!=' '):
        printWinner(6)
        return True
    
    #승리조건2 : 세로빙고 체크
    #승자를 알기 위해 printWinner 함수로 pos 전달
    elif   (board[0] == board[3] and board[3] == board[6]and board[0]!=' '):
        printWinner(0)
        return True
    elif   (board[1] == board[4] and board[4]== board[7] and board[1]!=' '):
        printWinner(1)
        return True
    elif   (board[2] == board[5] and board[5]== board[8] and board[2]!=' '):
        printWinner(2)
        return True

    #승리조건3: 대각선 빙고 체크
    #승자를 알기 위해 printWinner 함수로 pos 전달
    elif   (board[0] == board[4] and board[4]== board[8] and board[4]!=' '):
        printWinner(4)
        return True
    elif   (board[2] == board[4] and board[4]== board[6] and board[4]!=' '):
        printWinner(4)
        return True

    #무승부 조건
    elif  (board[0]!=' ' and board[1]!=' ' and board[2]!=' '
           and board[3]!=' ' and board[4]!=' ' and board[5]!=' '
           and board[6]!=' '  and board[7]!=' ' and board[8]!=' '):
        print("무승부")
        return True

    #승리, 무승부 모두 아니면 False 
    else:   return False


#승자 출력 printWinner 함수 정의
#checkWin 함수에서 승자의 pos를 전달받음
#승자가 누구인지 출력
def printWinner(pos):
    if board[pos]=="x":
        print("선수 1 승리!!")
    else:
        print("선수 2 승리!!")



#########################################
####실제 게임 실행
#게임 준비
print("Tic-Tac-Toe 게임 (만든사람 : 박효선)")    
print("선수1 [X] --- 선수2 [O]")    
print()    
print()    
print("준비 중입니다...")    
time.sleep(1)
drawBoard()     #빈 보드 그리기
print()

#########################################
#게임시작
#선수1, 선수2 번갈아 가면서  o, x 를 체크하기
player=1      
while True:        

    #차례
    if(player % 2 != 0):        #홀수번째 차례: 선수1 (x체크)
        print("선수 1 차례")    
        Mark = 'x'   
    else:    
        print("선수 2 차례")    #짝수번째 차례: 선수2 (o체크)
        Mark = 'o'

    #사용자가 위치를 선택, 사용자의 위치선택값을 받음
    choose= int(input("마크하기를 원하는 위치(1-9)를 선택하세요 : "))
    idx =choose-1



    #선택한 board가  빈공간이면 마크한다
    if board[idx]!=' ':   continue
    board[idx] =Mark


    #마크한 보드를 그린다
    drawBoard()
    print()
    print()


    #게임이 종료되었는지 확인
    finish=checkFinish()
    if finish== True:   break
    #게임이 종료되면 끝

    #게임이 종료되지 않았다면 계속 플레이
    player+=1    #선수 교체



