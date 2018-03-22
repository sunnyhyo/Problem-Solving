#lab3-8
name=input('이름: ')
kor=int(input('국어점수: '))
eng=int(input('영어점수: '))
math=int(input('수학점수: '))

tot= kor+eng+math
mean= float(tot/3)

print('총점: %d'%tot)
print('평균: %0.2f'%mean)
