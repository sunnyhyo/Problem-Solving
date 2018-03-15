# 0315 lab2-2

total=int(input('인출 금액(1천 단위 이상으로): '))
print()
print('='*20)

print('인출 내역:')
a= total//50000
b= (total-(a*50000))//10000
c= (total-(a*50000+b*10000))//5000
d= (total-(a*50000+b*10000+c*5000))//1000

print( '5만원- %d장'  %a)
print( '1만원- %d장'  %b)
print( '5천원- %d장'  %c)
print( '1천원- %d장'  %d)
