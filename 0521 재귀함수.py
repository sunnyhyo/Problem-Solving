#재귀함수
#자기 자신을 다시 호출하는 형태의 함수를 재귀함수(Recursion Function)

def recursive(a):
    print("call me")
    if a ==0:               #a==0인경우 종류. 호출 그만함
        return
    recursive(a-1)  #a-1 자기 자신을 다시 호출

recursive(2)
#call me            a=2
#call me            a=1
#call me            a=0
