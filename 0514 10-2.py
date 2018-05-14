#함수 안에서 전역 변수 변경(3/3)


def calculateArea (radius):
    global area  #global을 사용하여 전역 변수에 값을 저장한다고 알려야 한다. 
    area = 3.14 * radius**2 # 전역변수 area에 계산값을 저장하려고 했다!
    #새로운 전역변수  area 생성되었음
    return  #리턴하지 않고 내려옴

area = 0  # ?? 여기서 왜 0 이 무시되었는지? 
r = float(input("원의 반지름: "))
calculateArea(r)
print(area)


#원의 반지름: 10
#314.0
