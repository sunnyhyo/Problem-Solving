#디폴트 인수

def greet(name, msg="별일없죠?"):
     #디폴트 인수는 맨 마지막에 위치시킨다
    #def greet(msg=“별일 없죠?”, name): 불가능
    print("안녕 ", name + ', ' + msg)


greet("영희", "숙제 했어요? ")
#안녕 영희, 숙제 했어요?
greet("영희")
#안녕 영희 , 별일 없죠?
