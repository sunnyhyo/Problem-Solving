#Lab9-ex3
#parameter 한개 있고 return 값이 있는 함수 정의 및 호출
#입력이 있는 경우, 반환 값이 있는 경우

#caculateArea 함수 정의
#반지름을 입력받아 원의 면적을 구해 이를 return(반환)
def caculateArea(radius):
    area=3.14*radius**2
    return area

>>> val=caculateArea(5.0)
>>> print(val)
78.51

#사용자에게 반지름 입력받아 
inradius=float(input("반지름을 입력하시오: "))
#원의 넓이 구하는 함수 호출(입력받은 값 전달)
#calculateArea에게 면적을 반환받아 area에 저장
area=caculateArea(inradius)

# area 에 있는 값 출력
print("반지름이 %0.2f인 원의 area")

반지름을 입력하시오: 6
113.04
