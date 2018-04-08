#lab5-5

name = input("이름을 입력하시오: ")
score=int(input("점수를 입력하시오: "))

if score<=100:
    if score>=90:
        grade="A"
    else:
        if score>=80:
            grade="B"
        elif score>=70:
            grade="C"
        elif score>=60:
            grade="D"
        else:
            grade="F"


print("""이름 \t점수 \t학점
%s\t%s\t%s""" %(name,score,grade))
