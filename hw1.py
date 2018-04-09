#1585063 박효선
#과제1

date=input("날짜:")
carnum=input("차량번호:")

end_date=int(date[4])
end_car=int(carnum[-1])


if 5==abs(end_car- end_date) or 0==abs(end_car-end_date):
    print("오늘 날짜 끝자리는 %s이므로 %s차량은 운행할 수 없습니다"
          %(end_date, carnum))
else:
    print("오늘 날짜 끝자리는 %s이므로 %s차량은 운행할 수 있습니다"
          %(end_date, carnum))
