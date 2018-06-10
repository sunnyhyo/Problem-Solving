#Lab9-10 (문자열 내의 개별 문자)

school = "이화여자대학교 공과대학"
subjects = ["국어", "영아", "수학", "물리"]

#문자열 슬라이싱과 인덱싱 연산
shortSchool = school[ :3] + school[4] + school[-5: ]
#subject에서 앞 글자만 모아 저장할 변수 초기화
shortSubjects = ""

#subjects 아이템을 반복해서 과목명을 가져온다
for i in range(len(subjects)):
    shortSubjects += (subjects[i])[0] #각 과목의 앞 글자 추출
    #과목 뒤에 쉼표 작성, 마지막 과목 뒤에는 쉼표를 붙이지 않음
    if i < len(subjects)-1 :
         shortSubjects += ",  "

#결과 출력
print(shortSchool)
print(shortSubjects)    

이화여대 공과대학
국,  영,  수,  물
