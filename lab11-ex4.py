#lab11-ex4

times=0  #전역변수 

def count(times):  #지역변수 
    #이 함수가 실행된 횟수를 화면에 출력한다.
    times=times+1  #지역변수 =전역변수 +1
    print(times)   #지역변수 
    return times   #지역변수 


print(times)        #전역변수 
times=count(times)  #count(지역변수)
times=count(times)



#0
#1
#2
