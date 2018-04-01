#lab4-3

name=input("이름을 입력하시오.: ")
num=input("주민등록번호를 입력하시오.: ")

year=1900+int(num[:2])
month=num[2:4]
day=num[4:6]

sex=num[-7]

if sex=='1':
    gender='남성'
else:
    gender='여성'


print("%s 고객의 생년월일은 \n %s년 %s월 %s일 입니다."%(name,year,month,day))
print("%s 고객은 %s입니다"%(name, gender))
