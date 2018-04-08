#lab5-3


year=int(input("연도를 입력하시오.:"))

if (year>=1900) and (year<=2020):
    if (year%4==0) and (year%100!=0) or (year%400==0):
        print("입력하신 %s년은 \n윤년입니다."%year)
else:
    print('"1900~2020"년 사이의 \n연도를 입력하세요.')
