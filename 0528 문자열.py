Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> #파이썬 자료형
>>> 
>>> #문자열(string)
>>> 
>>> food="Python's favorite food is perl"
>>> print(food)
Python's favorite food is perl
>>> 
>>> food='Python\'s favorite food is perl'
>>> print(food)
Python's favorite food is perl
>>> 
>>> say ='"Python is easy," he says,'
>>> print(say)
"Python is easy," he says,
>>> 
>>> say='"Python is very easy." he says.'
>>> print(say)
"Python is very easy." he says.
>>> 
>>> say="\"Python is very easy.\" he says."
>>> print(say)
"Python is very easy." he says.
>>> 
>>> lines = "Life is too short\nYou need python"
>>> print(lines)
Life is too short
You need python
>>> 
>>> lines="""Life is too short
You need python
"""
>>> print(lines)
Life is too short
You need python

>>> 
>>> #문자열 연산, 인덱싱
>>> #문자열 연산
>>> 
>>> head ='Pyhon'
>>> tail='is fun!'
>>> head + tail
'Pyhonis fun!'
>>> 
>>> a='python'
>>> a*2
'pythonpython'
>>> 
>>> a="Life is too short, You need Python"
>>> a[0]
'L'
>>> a[-1]
'n'
>>> b=a[0] + a[1] + a[2] + a[3]
>>> b
'Life'
>>> 
>>> a[12:17]
'short'
>>> a[19:-7]
'You need'
>>> a[19:]
'You need Python'
>>> a[:17]
'Life is too short'
>>> a[:]
'Life is too short, You need Python'
>>> 
>>> a[3]='p'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a[3]='p'
TypeError: 'str' object does not support item assignment
>>> 
>>> #문자열 특징 immutable
>>> 
>>> 
>>> #문자열 포맷팅(Formatting)
>>> 
>>> #숫자, 문자열 바로 대입
>>> str1="I eat %d apples. "%3
>>> str1
'I eat 3 apples. '
>>> 
>>> str2= "I eat %d apples." %"five"
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    str2= "I eat %d apples." %"five"
TypeError: %d format: a number is required, not str
>>> str2= "I eat %d apples."  % 'five'
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    str2= "I eat %d apples."  % 'five'
TypeError: %d format: a number is required, not str
>>>  #??
>>> 
>>> #변수로 대입
>>> number =3
>>> str3= "I eat %d apples."%number
>>> print(str3)
I eat 3 apples.
>>> 
>>> #두 개 이상의 값을 치환
>>> number =10
>>> 
>>> day ="three"
>>> str3=" I ate %d apples. do I was sick for %s days." %(number, day)
>>> print(str3)
 I ate 10 apples. do I was sick for three days.
>>> 
>>> #포맷 코드
>>> 
>>> #%s 포맷 코드는 어떤 형태로든 변환이 가능
>>> "I have %s apples." %3
'I have 3 apples.'
>>> "rate is %s" %3.234
'rate is 3.234'
>>> 
>>> #포맷팅 연산자 %d, %s 와 리터럴 %를 같이 쓸때는 %%
>>> #혼용시 오류가남
>>> 
>>> "Error is 5%"
'Error is 5%'
>>> 
>>> "Error is %d%." %98
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    "Error is %d%." %98
ValueError: incomplete format
>>> 
>>> "Error is %d%%." %98
'Error is 98%.'
>>> 
>>> #정렬과 공백
>>> "%10s" %"hi"
'        hi'
>>> "%-10s"%"hi"
'hi        '
>>> str2= "I eat %s apples." %"five"
>>> str2
'I eat five apples.'
>>> str2= "I eat %s apples." % 'five'
>>> str2
'I eat five apples.'
>>> 
>>> 
>>> 
>>> "%10s" %"hi"
'        hi'
>>> #10개 자리를 확보한 수 오른쪽 정렬
>>> 
>>> "%-10s"%"hi"
'hi        '
>>> 10개 자리를 확보한 후 왼쪽 정렬
SyntaxError: invalid syntax
>>> #남은 공백의 갯수 8 칸
>>> 
>>> #정렬과 공백
>>> 
>>> "%0.4f"%3.412145
'3.4121'
>>> #소수 이하 4자리까지 표시
>>> 
>>> "%10.4f" %3.412145
'    3.4121'
>>> #10개 자리를 확보하고 소수 리하 4자리까지 표시(오른쪽으로 정렬)
>>> 
>>> "%-10.4f" %3.412145
'3.4121    '
>>> #10개 자리를 확보하고 소수 이하 4자리까지 표시(왼쪽으로 정렬)
>>> #공백은 4자리
>>> #3.4121 6자리
>>> 
>>> 
>>> #문자열 관련 함수들
>>> 
>>> a='hi'
>>> a.upper()
'HI'
>>> 
>>> a='HI'
>>> a.lower()
'hi'
>>> #upper() : 소문자 -> 대문자
>>> #lower() : 대문자 -> 소문자
>>> 
>>> a='hobby'
>>> a.count('b')
2
>>> #count() : 문자 개수 세기
>>> #hobby 에서 b 문자의 개수는 2개
>>> 
>>> a= "Python is best choice"
>>> a.find('b')
10
>>> #find() : 위치 알려주기
>>> #문자열 중 'b'가 처음으로 나온 위치를 반환.
>>> #만약 찾는 문자의 문자열이 존재하지 않는다면 -1 반환
>>> 
>>> a.find('k')
-1
>>> 
>>> a="Life is too short"
>>> a.index('t')
8
>>> #index() : 위치 알려주기
>>> #문자열 중 't'가 처음으로 나온 위치를 반환.
>>> #만약 찾는 문자나 문자열이 존재하지 않는다면 에러를 발생 (find 와 차이)
>>> 
>>> a.index('k')
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.index('k')
ValueError: substring not found
>>> 
>>> a="       hi     '
SyntaxError: EOL while scanning string literal
>>> a="       hi     "
>>> a.strip()
'hi'
>>> #strip() : 양쪽 공백 지우기
>>> 
>>> mystr="{0} apples. {1}days."
>>> mystr.format(10,'three')
'10 apples. threedays.'
>>> 
>>> "{0<10}".format('hi')
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    "{0<10}".format('hi')
KeyError: '0<10'
>>> "{0:<10}".format('hi')
'hi        '
>>> 
>>> y=3.421234342
>>> "0:0.4f".format(y)
'0:0.4f'
>>> "{0:0.4f}".format(y)
'3.4212'
>>> 
>>> #문자열 포맷팅
>>> #값 치환
>>> #정렬 (오른쪽, 왼쪽, 양쪽)
>>> #공백을 특정 문자로 채루기
>>> #실수 포맷팅 등
>>> 
>>> a=','
>>> a.join('abcd')
'a,b,c,d'
>>> 
>>> #join(0 문자열 삽입
>>> 
>>> a= "Life id too short"
>>> a.replace("Life", "Your leg")
'Your leg id too short'
>>> 
>>> a.replace("id", "is")
'Life is too short'
>>> 
>>> 
>>> #replace() 문자열 바꾸기
>>> #replace(바뀌게 될 문자열, 바꿀 문자열)
>>> 
>>> a="Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> 
>>> #split() : 문자열 나누기
>>> #구분자로 해서 나눈 문자열들은 리스트에 하나씩 들어가게 된다
>>> 
>>> a="a:b:c:d"
>>> a.split(":")
['a', 'b', 'c', 'd']
>>> 
>>> #1) a.split() 처럼 괄호안에 아무런 값도 넣어주지 않으면 공백을 구분자로 문자열을 나누어 중다
>>> #2) a.split(':') 처럼 괄호 안에 특정한 값이 있을 경우에는 괄호안의 값을 구분자로 해서 문자열을 나누어 준다
>>> 
>>> a
'a:b:c:d'
>>> a.split()
['a:b:c:d']
>>> a.split(':')
['a', 'b', 'c', 'd']
>>> 
>>> 
>>> 
>>> 
