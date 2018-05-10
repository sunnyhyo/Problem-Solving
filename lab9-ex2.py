#입력 있는 경우 , 반환 값은 없는 경우

def printAddress(name):
    print("서울특별시 서대문구 이화여대길")
    print("호크마 교양 대학")
    print(name)


#>>> printAddress("나이화")
#서울특별시 서대문구 이화여대길
#호크마 교양 대학
#나이화



#사용자에게 이름을 입력받음
inname=input("이름을 입력하시오")
#입력받은 이름을 printAddress 함수를 호출하며 전달
printAddress(inname)


#이름을 입력하시오나이화
#서울특별시 서대문구 이화여대길
#호크마 교양 대학
#나이화
