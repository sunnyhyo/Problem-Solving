# 재귀함수 사례

#factorial
#팩토리얼

def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)

f(2)
#2=2*1
f(3)
#6=3*2*1
f(4)
#24=4*3*2*1
