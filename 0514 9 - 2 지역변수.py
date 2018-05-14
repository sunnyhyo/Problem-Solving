#지역변수
#매개변수는 무조건 지역변수!! : result, radius
#전역변수: r, area

#함수정의
def calculateArea (radius):  #radius 지역변수    
    result = 3.14 * radius**2   #
    return result   #반환 

#실행
r = float(input("원의 반지름: "))
area = calculateArea(r)  #함수를 area로 받았음
print(result)

#result 를 직접 사용할 수 있다고 생각했음.
#함수 안에서 만든 변수는 바깥에서  사용할 수 없음 .
#result 정의되지 않았다.
