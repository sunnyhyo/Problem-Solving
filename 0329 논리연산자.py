Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.


#논리연산자
# and
# or 
# not 피연산자 1개

>>> x=True
>>> y=False
>>> x and y
False
>>> 
>>> x or y
True
>>> 
>>> not x
False
>>> 
>>> not y
True
>>> 
>>> x=20
>>> y=15
>>> (x%2)==0   #x를 2로 나누었을때 몫이 0인가? 
True
>>> (y%2)==0   #y를 2로 나누었을때 몫이 0인가? 
False
>>> not((x%2)==0)
False
>>> 
>>> (x%2)==0 and (y%2)==0
False
>>> 
>>> (x%2)==0 or (y%2)==0
True
