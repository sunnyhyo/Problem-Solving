#lab5-7

a=int(input("첫 번째 과목을 입력하시오: "))
b=int(input("두 번째 과목을 입력하시오: "))
c=int(input("세 번째 과목을 입력하시오: "))

mean=(a+b+c)/3

if a>=60 and b>=60 and c>=60:
    print("자격증 합격")
else:
    if mean>=70:
        print("자격증 합격")
    else:
        print("자격증 불합격")
