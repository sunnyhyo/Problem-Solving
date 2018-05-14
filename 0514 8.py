#지역변수: 함수 안에서 선언되는 변수 , 함수 안에서만 작동
#전역변수: 함수 외부에서 선언되는 변수 ,


a=1

def vartest(a):
    a=a+1

varest(a)
print(a)
