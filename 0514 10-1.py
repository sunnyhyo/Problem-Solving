#함수 안에서 전역 변수 변경(2/3)


def calculateArea (radius):
    area = 3.14 * radius**2 # 전역변수 area에 계산값을 저장하려고 했다!
    #새로운 지역변수 area 생성되었음
    return  #리턴하지 않고 내려옴

area = 0  #전역변수 area =0  로 새롭게 정의 되었음
r = float(input("원의 반지름: "))
calculateArea(r)
print(area)
