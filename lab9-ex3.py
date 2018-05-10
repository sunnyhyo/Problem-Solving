#입력이 있는 경우, 반환 값이 있는 경우

def caculateArea(radius):
    area=3.14*radius**2
    return area



#>>> val=caculateArea(5.0)
#>>> print(val)
#78.51


inradius=float(input("반지름을 입력하시오: "))
val=caculateArea(inradius)
print(val)

#반지름을 입력하시오: 6
#113.04
