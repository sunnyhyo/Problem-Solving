#if 3
#lab5-ex1


score=input("점수입력:")
score=int(score)
if score>90:
    print("합격!!! - 장학금 100%")
elif score>80:
    print("합격!!! - 장학금 50%")
elif score>70:
    print("합격!!! - 장학금 없음")
else:
    print("불합격;;;")
