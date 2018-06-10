#Lab9-ex4
#parameter 두개, return 값이 있는 함수 정의 및 함수 호출 연습

#getSum 함수 정의
#시작값고 종료값을 파라미터로 받아 시작값부터 종료값 까지의 숫자를 더해
#그 결과를 반환하는 함수 작성
def getSum(start, stop):
    #start 부터 stop 까지의 값을 더하고 그 결과를 반환
    sum=0   #누적할 변수 초기화

    #종료값까지 더해야 하므로 stop+1 미만까지 반복
    while start <= stop:
        sum+=start
        start+=1
    #for n in range(start, stop+1):
    #    sum+=n
    return sum

#1~10까지의 합을 구해서 그 결과를 출력 (getSum 함수 호출)
# getSum 함수 호출, 시작값으로 1 종료값으로 10 전달
# getSum 호출 후 반환 받은 값을 result 에 저장
result = getSum(1,10)
print(result)
