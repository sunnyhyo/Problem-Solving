#콜백 함수

def drawit(x,y):            #매개변수 2개 
    t.penup()


s=turtle.Screen()                   #그림이 그려지는 화면을 얻음
s.onescreenclick(drawit)    #마우스 클릭 이벤트 처리 함수를 등록한다.

#이벤트가 발생했을때 , 함수를 불러옴
#정보가 변경되거나 이벤트가 발생했을 때,
#자신의 변경된 정보나 이벤트에 따른
#어떠한 처리를 할 수 있게 제공하는 함수를 콜백 함수(callback function)라고 부른다.
