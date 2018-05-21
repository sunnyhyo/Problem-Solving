def calculateArea(radius):
    result=3.14*radius**2
    return result

r=float(input("원의 반지름: "))
area=calculateArea(r)
print(result) #오류- 지역변수를 바깥에서 print()못함
print(area) #314.0
