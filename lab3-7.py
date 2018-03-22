#lab3-7
money=int(input('투입한 돈: '))
price=int(input('물건값: '))

charge=money-price
c500= int(charge/500)
c100= (charge-500*c500)/100

print('500원 동전의 개수: %d'%c500)
print('100원 동전의 개수: %d'%c100)
