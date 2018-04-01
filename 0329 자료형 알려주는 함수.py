Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #자료형 알려주는 함수
>>> type(10)
<class 'int'>
>>> type(10.0)
<class 'float'>
>>> type("hello")
<class 'str'>
>>> type(True)
<class 'bool'>
>>> # 참/거짓 자료형 : bool
>>> 
>>> a,b,c,d = 11,3.14, 'ewha', Flase
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a,b,c,d = 11,3.14, 'ewha', Flase
NameError: name 'Flase' is not defined
>>> a,b,c,d = 11,3.14, 'ewha', False
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
>>> type(d)
<class 'bool'>
>>> 
>>> type(3+3)
<class 'int'>
>>> #정수
>>> type(3+3.14)
<class 'float'>
>>> #실수
>>> type("="*3)
<class 'str'>
>>> #문자열
>>> type(4%2==0)
<class 'bool'>
>>> #참/거짓
