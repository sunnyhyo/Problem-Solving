#lab11-ex3
#전역변수와 지역변수

times=0    #count 함수가 실행된 횟수

def count():
    #이 함수가 실행된 횟수를 화면에 출력한다.
    global times #times 는 전역변수다 . 사용하고 변경까지 하고 싶을때
    times=times+1
    print(times)

count()
count()
