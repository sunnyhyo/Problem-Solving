#0315 lab2-1

print('*'*30)
name= input('학생 이름은? ')
a= int(input('국어 점수는? '))
b= int(input('영어 점수는? '))
c= int(input('수학 점수는? '))
print()
print()
print('='*30)
print( name, '총점과 평균입니다. ')
print('총점 = ', a+b+c, '점')
print('평균 = ', (a+b+c)/3, '점')


# print('총점 = ', a+b+c+ '점')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
