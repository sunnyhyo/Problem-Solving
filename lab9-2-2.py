#lab9-2  (별표 사각형 함수 출력 함수)
#별표 사각형을 출력하는 rectangle 함수 정의 작성
#한 변의 길이를 파라미터로 받게 한다.
#반환할 것은 없음
def rectangle(n):
    #한 라인을 별표를 찍는 코드 작성
    i=0
    while i < n:
        print("*"*n)  
        i+=1
    #for I in range(n):
     #   print(line)
#사용자한테 한 변의 길이를 정수로 입력받아 
#사각형을 출력하는 rectangle 함수 호출
width=int(input("한 변의 길이 입력: "))
rectangle(width)
