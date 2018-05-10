def getGrade(score):
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    print("성적은",grade, "입니다")

score=int(input("점수 입력: "))
getGrade(score)
#print("성적은 %s 입니다"%getGrade)
