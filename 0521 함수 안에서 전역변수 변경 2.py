def calculateArea (radius):
    area = 3.14 * radius**2 # 전역변수 area에 계산값을 저장하려고 했다!
    #여기서 새로운 지역변수 area 가 생성됨
    return


area = 0
r = float(input("원의 반지름: "))
calculateArea(r)
print(area)  #전역변수 area 출
