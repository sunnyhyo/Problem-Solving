Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name='나이화'
>>> kor, eng, math =90,80,60
>>> total =kor+eng+math
>>> average=total/3
>>> print(name, '성적은','총점이', total, '평균이', average, '입니다.')
나이화 성적은 총점이 230 평균이 76.66666666666667 입니다.
>>> print("%s 성적은 총점이 %s 평균이 %s 입니다. " %(name, total, average))
나이화 성적은 총점이 230 평균이 76.66666666666667 입니다. 
>>> print("%s 성적은 총점이 %s 평균이 %0.2f 입니다. " %(name, total, average))
나이화 성적은 총점이 230 평균이 76.67 입니다. 
>>> print("%s는 상위 10%% 성적입니다"%name)
나이화는 상위 10% 성적입니다
>>> print("%s는 상위 10\% 성적입니다"%name)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("%s는 상위 10\% 성적입니다"%name)
TypeError: not enough arguments for format string
>>> print("%s는 상위 10% 성적입니다"%name)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("%s는 상위 10% 성적입니다"%name)
TypeError: not enough arguments for format string
>>> 
