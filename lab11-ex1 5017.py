#lab11-ex1
#전역변수 지역변수

seconds_per_minute=60  #전역변수

def minutes_to_seconds(minutes): #지역변수 
    seconds = minutes *seconds_per_minute   #외부에 있는 값을 가져옴
    return seconds #지역변수
    #seconds는 함수 내부에서 만들어져서 지역변수  return

a= minutes_to_seconds(3)
#print(seconds)  #지역변수이기 때문에 함수 밖에서 읽는 오류 발생
print(a)
