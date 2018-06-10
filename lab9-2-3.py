#Lab9-2(2) (별표 출력 함수2)
#별표 사각형을 출력하는 rectangle 함수 정의 작성
#한 라인에 찍을 별표 개수, 그것을 몇 라인 찍을 지 개수를 파라미터로 받게 한다.
#반환할 것은 없음

def rectangle(n, m):
    #한 라인을 별표로 찍는 코드 작성
    line = "* "* n

    #m 라인만큼 출력
    for i in range(m):
        print(line)

#사용자에게 한 변의 길이와 높이를 정수로 입력받아
#사각형을 출력하는 rectangle 함수 호출
width =int(input("한 변의 길이 입력: "))
height = int(input("높이 입력: "))
rectangle(width, height)

한 변의 길이 입력: 4
높이 입력: 5
* * * * 
* * * * 
* * * * 
* * * * 
* * * *
