#디폴트 함수 

def sayMyself( name, age, korean=True ):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)

    if korean:
        print("서울에 삽니다.")
    else:
        print("외국에 삽니다.")


sayMyself("나이화", 21)
print() #띄움줄

sayMyself("김한국", 22, False)
