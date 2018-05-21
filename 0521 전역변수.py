def calculateArea():
    result=3.14*r**2  #r 은 전역변수. 바깥에서 지정된 수를 입력받음
    return result

r=float(input("원의 반지름: "))
area=calculateArea()
print(area)
