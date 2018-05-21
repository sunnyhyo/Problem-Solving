def calculateArea (radius):
    global area             #함수 바깥에서 생성된 전역변수를 수정하고 싶을때 signal 은 global
    area = 3.14 * radius**2
    return


area = 0
r = float(input("원의 반지름: "))
calculateArea(r)
print(area)
