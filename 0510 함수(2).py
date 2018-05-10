Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> random.random()
0.9326020188190144
>>> random.randint(1,6)
4
>>> random.randint(0,100)
71
>>> random.randint(-100m50)
SyntaxError: invalid syntax
>>> random.randint(-100,50)
24
>>> #이상, 이하의 정수를 리턴
>>> random.random()
0.5147962954294074
>>> #이상, 미만의 실수를 리턴
>>> 
>>> random.randrange(100)
6
>>> random.randrange(1,10)
6
>>> random.randrange(1,10,2)
1
>>> #이상, 미만의 정수를 리턴
>>> #1부터 2씩 증가한 수 중 10 미만의 정수를 리턴
>>> #1,3,5,7,9 중 임의의 수 리턴
>>> 
>>> random.choice([1,2,3,4,5,6])
3
>>> #sequence 자료형에서 하나를 임의로 선택하여 리턴
>>> color=random.choice(["black","green","yellow","red"])
>>> color
'yellow'
>>> #sequence 자료형은 여러가지 자료가 묶여있는 형태
>>> #black, green, yellow, red 중 하나를 임의로 선택하여 color에 저장
>>> 
>>> #1이상 100이하의 난수를 발생하시오
>>> random.randint(1,100)
33
>>> random.randrange(1,101)
93
>>> #난수를 이용하여 주사위를 던지시오
>>> random.randint(1,6)
5
>>> random.randrange(1,7)
1
>>> #0~100 사이의 2의 배수 중 난수를 발생하시오
>>> random.randrange(0,101,2)
40
>>> 
