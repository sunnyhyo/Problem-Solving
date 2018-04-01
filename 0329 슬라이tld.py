Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Users/user/Desktop/0329 인덱싱, 슬라이스.py ==============
>>> a = "Life is too short, You need Python"
>>> a[0]
'L'
>>> a[3]
'e'
>>> a[-1]
'n'
>>> b=a[0]+a[1]+a[2]+a[3]
>>> b
'Life'
>>> a[0:4]
'Life'
>>> a[5:7]
'is'
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
>>> #전체 출력
>>> 
>>> a="20010331Rainy"
>>> date=a[:8]
>>> weather=a[8:]
>>> date
'20010331'
>>> weather
'Rainy'
>>> year=a[:4]
>>> day=a[4:8]
>>> year
'2001'
>>> day
'0331'
>>> #슬라이싱
