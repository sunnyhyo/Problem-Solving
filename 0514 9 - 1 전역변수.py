#지역변수
#매개변수는 무조건 지역변수!! result
#전역변수 : r, area


#함수정의
def calculateArea ():  #radius 지역변수    
    result = 3.14 * r**2   # 바깥에서 만든 r 변수를 함수 내에서 사용 
    return result   #반환 

#실행
r = float(input("원의 반지름: "))   #전역변수로  r 이라는 변수생성
area = calculateArea()
print(area)
