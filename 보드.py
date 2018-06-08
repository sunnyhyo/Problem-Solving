
import time

board=[" "," "," "," "," "," "," "," "," "]


def drawBoard():    
    print("  %c   |   %c   |   %c   " % (board[0],board[1],board[2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[3],board[4],board[5]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[6],board[7],board[8]))    
    print("___|___|___")  

def printWinner(pos):
    if board[pos]=="x":
        print("선수 1 승리")
    else:
        print("선수 2 승리")


def checkWin():
    if   (board[0] == board[1] and board[1]== board[2] and board[0]!= ' '):
        printWinner(0)
        return True
    elif   (board[3] == board[4] and board[4] == board[5] and board[3]!= ' '):
        printWinner(3)
        return True
    elif   (board[6] == board[7] and board[7] == board[8] and board[6]!=' '):
        printWinner(6)
        return True
    elif   (board[0] == board[3] and board[3] == board[6]and board[0]!=' '):
        printWinner(0)
        return True
    elif   (board[1] == board[4] and board[4]== board[7] and board[1]!=' '):
        printWinner(1)
        return True
    elif   (board[2] == board[5] and board[5]== board[8] and board[2]!=' '):
        printWinner(2)
        return True
    elif   (board[0] == board[4] and board[4]== board[8] and board[4]!=' '):
        printWinner(4)
        return True
    elif   (board[2] == board[4] and board[4]== board[6] and board[4]!=' '):
        printWinner(4)
        return True
    elif  (board[0]!=' ' and board[1]!=' ' and board[2]!=' '
           and board[3]!=' ' and board[4]!=' ' and board[5]!=' '
           and board[6]!=' '  and board[7]!=' ' and board[8]!=' '):
        print("무승부")
        return True
    else:
        return False


player=1
print("Tic-Tac-Toe 게임 (만든사람 : 박효선)")    
print("선수1 [X] --- 선수2 [O]")    
print()    
print()    
print("준비 중입니다...")    
time.sleep(1)
drawBoard()

while True:        
    if(player % 2 != 0):    
        print("선수 1 차례")    
        Mark = 'x'   
    else:    
        print("선수 2 차례")    
        Mark = 'o'    
    position = int(input("마크하기를 원하는 위치(1-9)를 선택하세요 : "))
    idx =int(position)-1
    if board[idx]!=' ':
        continue
    board[idx] =Mark
    drawBoard()
    finish=checkWin()
    if finish== True:
        break
    player+=1    




        
