Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x+=y
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x+=y
NameError: name 'x' is not defined
>>> x=1000
>>> x
1000
>>> 1
1
>>> x+=2
>>> x
1002
>>> x-=1000
>>> x
2
>>> x**=2
>>> x
4
>>> x%=2
>>> x
0
>>> 
>>> #복합연산자
>>> total=0
>>> kor=90
>>> eng=80
>>> math=80
>>> total+=kor
>>> total
90
>>> total+=eng
>>> total
170
>>> total+=math
>>> totla
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    totla
NameError: name 'totla' is not defined
>>> total
250
>>> 
>>> #money
>>> money=2450
>>> coin500s=money//500
>>> money, coin500s
(2450, 4)
>>> money%=500
>>> coin100s=money//100
>>> money, coin100s
(450, 4)
>>> money%=100
>>> coin50s=money//50
>>> monwy,coin50s
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    monwy,coin50s
NameError: name 'monwy' is not defined
>>> money,coin50s
(50, 1)
>>> 
>>> #관계연산자
>>> x=10
>>> y=12
>>> x.12
SyntaxError: invalid syntax
>>> x>12
False
>>> x<y
True
>>> x==y
False
>>> x!=y
True
>>> x>y
False
>>> x>=y
False
>>> x<=y
True
>>> 10.
10.0
>>> 10>10
False
>>> 10<10
False
>>> #비교해서 결과를 알려줌 (TRUE, FALSE)
>>> 10==10
True
>>> 10=10
SyntaxError: can't assign to literal
>>> 10!=10
False
>>> 10>=10
True
>>> 10<=10
True
>>> x='a'
>>> y='A'
>>> z="a"
>>> x>y
True
>>> x<y
False
>>> x==y
False
>>> x!=y
True
>>> x==z
True
>>> #문자비교
>>> #소문자>대문자
>>> 
>>> #두 개의 문자 사이에도 대소관계가 있음
>>> # 컴퓨터 자체는 문자를 코드형식으로 mapping
>>> #그 코드를 비교
>>> 
