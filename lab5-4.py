#lab5-4

a=int(input("첫 번째 수를 입력하시오: "))
b=int(input("두 번째 수를 입력하시오: "))
c=int(input("세 번째 수를 입력하시오: "))

print("입력하신 값 %s,%s,%s 중 가장 큰 수는 "%(a,b,c), end="")

if a>=b:
    if a>=c:
        print("%s입니다" %a)
    else:
        print("%s입니다" %c)
else:
    if b>=c:
        print("%s입니다" %b)
    else:
        print("%s입니다" %c)
                  
