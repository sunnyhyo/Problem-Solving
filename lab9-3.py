def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

n=int(input("팩토리얼을 구할 정수를 입력: "))
num=factorial(n)

print("%d!은 %d입니다."%(n,num))
