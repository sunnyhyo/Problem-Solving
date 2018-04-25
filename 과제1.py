#1585063 박효선
#과제1


#변수입력
date=input("날짜를 입력하세요: ")           #날짜 입력- 형식이 정해졌기 때문에 따로 지정하지 않음
carnum=input("차량번호를 입력하세요: ")     #차량번호 입력


#변수정의
end_date=int(date[4])                       #날짜 끝번호- mm/dd/yyyy 중 4번째 문자열
end_car=int(carnum[-1])                     #차량번호 끝번호


#운행여부 판단
if 5==abs(end_car- end_date) or 0==abs(end_car-end_date):   #절대값 함수 abs()
    print("오늘 날짜 끝자리는 %s이므로 %s차량은 운행할 수 없습니다"
          %(end_date, carnum))
else:
    print("오늘 날짜 끝자리는 %s이므로 %s차량은 운행할 수 있습니다"
          %(end_date, carnum))




