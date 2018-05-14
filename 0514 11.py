
def greet(name, msg="별일없죠?"):  #디폴트 인수 defualt argument , 맨 마지막에 위치시킴
    print("안녕 ", name + ', ' + msg)

greet("영희", "숙제 했어요?" )
greet("영희")



def sayMyself(name, age, korean=True ):  #한국에 사는 것이 디폴트 값
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)

    if korean:
        print("서울에 삽니다.")
    else:
        print("외국에 삽니다.")

sayMyself("나이화", 21)
print()
sayMyself("김한국", 22, False)

    
