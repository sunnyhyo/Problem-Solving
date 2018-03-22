Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var1=2424
>>> var1=24
>>> var2=2+5**2
>>> var1
24
>>> var2
27
>>> var5='이화여대'
>>> var6='18'
>>> var6
'18'
>>> print(var6)
18
>>> #var6 18이 어떤 문자형인지 나타냄
>>> #print(var6)  내용만 나타냄
>>> 
>>> number
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> number=5
>>> numbrt
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    numbrt
NameError: name 'numbrt' is not defined
>>> number
5
>>> number1 =number2+2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    number1 =number2+2
NameError: name 'number2' is not defined
>>> #변수는 사용되기 전에 = 연산자를 이용해 값을 할당해야 함
>>> 
>>> #문자열 -> 숫자
>>> t= input('정수를 입력하시오')
정수를 입력하시오5
>>> t
'5'
>>> # '' 문자열로서 5
>>> t*3
'555'
>>> # 문자열 * 3 : 문자열 3번 반복
>>> x=input(t)
5
>>> x
''
>>> x*3
''
>>> x=input(t)
5
>>> x
''
>>> t=5
>>> x=input(t)
5
>>> x
''
>>> # ????
>>> 
>>> x=int()
>>> x=int(5)
>>> x
5
>>> # 문자열 x 를 숫자로 변환 int()
>>> 
>>> # 숫자 -> 문자열
>>> print('나는 현재' )
나는 현재
>>> print('나는 현재' + 21 + '살이다')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print('나는 현재' + 21 + '살이다')
TypeError: must be str, not int
>>> # 문자열과 숫자를 합칠 수 없다
>>> 
>>> # 숫자 + 숫자 : 연산
>>> # 문자 + 문자 : 문자열 붙여줌
>>> # 문자 + 숫자 : 불가능
>>> 
>>> print('나는 현재' + str)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print('나는 현재' + str)
TypeError: must be str, not type
>>> print('나는 현재' + str(21) + '살이다.')
나는 현재21살이다.
>>> print('원주율은 ' + str(3.14)+'입니다.')
원주율은 3.14입니다.
>>> 
>>> kor=90
>>> print('국어: '+str(kor)+'점')
국어: 90점
>>> 
>>> #변수명 규칙알기
>>> 
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> #파이썬에서 사용하고 있는 예약어
>>> len(keyword.kwlist)
33
>>> #키워드 총 33개
>>> 
>>> len('Hello')
5
>>> #문자열의 길이 알려줌
>>> #소수점 이하 출력할 자릿수 지정
>>> pi=3.14159265358979323846
>>> print('둘째자리까지 출력: %0.2f' %pi)
둘째자리까지 출력: 3.14
>>> # %f 실수를 출력하라
>>> # %0.2f 소수점 아래 두번째 자리까지 출력해라
>>> # %pi 그 실수는 뒤에 있는 pi
>>> print('%0.2f' %pi)
3.14
>>> val=10/3
>>> print('넷째 자리까지 출력: %0.4f' %val)
넷째 자리까지 출력: 3.3333
>>> print('셋째 자리까지 출력: %0.3f' %(10/3))
셋째 자리까지 출력: 3.333
>>> print('셋째 자리까지 출력: %0.3f' %val)
셋째 자리까지 출력: 3.333
>>> 
