#lab11-ex2
#전역변수 와 지역변수 구별하기


pi= 3.141595653589793

def area_of_circle(radius):
    #원의 반지름을 입력바아 넓이를 반환한다.
    area=radius+radius*pi
    return area

def volumn_of_cylinder(radius, height):
    """원기둥의 반지름과 놆이를 입력받아 부피를 반환한다"""
    top_area=area_of_circle(radius)
    volumn=top_area*height
    return volumn

result=volumn_of_cylinder(5,10)
print(result)


