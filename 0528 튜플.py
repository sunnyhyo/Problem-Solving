Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> #tuple  튜플
>>> 
>>> '''
튜플은 리스트와 비슷하나, 몇가지 내용이 다름

- 리스트: [   ], 그 값을 생성, 삭제 , 수정 가능
- 튜플 : (  ), 그 값을 변화시킬 수 없다!!! (가장 큰 차이점)

- 프로그램이 진행되는 동안 그 값이 항상 변하지 않기를 바란다면
  or 바뀔까 걱정하고 싶지 않다면 튜플을 사용
- 수시로 변화시켜야 할 경우는 리스트 사용
'''
'\n튜플은 리스트와 비슷하나, 몇가지 내용이 다름\n\n- 리스트: [   ], 그 값을 생성, 삭제 , 수정 가능\n- 튜플 : (  ), 그 값을 변화시킬 수 없다!!! (가장 큰 차이점)\n\n- 프로그램이 진행되는 동안 그 값이 항상 변하지 않기를 바란다면\n  or 바뀔까 걱정하고 싶지 않다면 튜플을 사용\n- 수시로 변화시켜야 할 경우는 리스트 사용\n'
>>> 
>>> 
>>> #생성
>>> 
>>> t1=()
>>> t2=(1,)   #단 한개의 요소만을 같는 튜플은 뒤에 콤마를 넣어야 함
>>> t3=(1,2,3)
>>> t4=1,2,3   #괄호를 생략해도 무반
>>> t5=(1,2,'a','b')
>>> 
>>> t1
()
>>> t2
(1,)
>>> t3
(1, 2, 3)
>>> t4
(1, 2, 3)
>>> t5
(1, 2, 'a', 'b')
>>> #여러가지 변수 타입 가능
>>> 
>>> 
>>> #인덱싱 슬라이싱
>>> 
>>> t1=(1,2,3,4)
>>> t1[0]
1
>>> t1[3]
4
>>> t1[1:]
(2, 3, 4)
>>> 
>>> # +, * 연산
>>> 
>>> t2=(3,4)
>>> t1+t2
(1, 2, 3, 4, 3, 4)
>>> 
>>> t3=(5,6)
>>> t3*3
(5, 6, 5, 6, 5, 6)
>>> 
>>> #튜플은 항목 변경이나 삭제가 안됨
>>> del(t1[0])
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    del(t1[0])
TypeError: 'tuple' object doesn't support item deletion
>>> t1[0]='c'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    t1[0]='c'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> t1
(1, 2, 3, 4)
>>> l1=t1[:]
>>> li
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    li
NameError: name 'li' is not defined
>>> l1
(1, 2, 3, 4)
>>> l1=[]
>>> l1.append(t1[:])
>>> l1
[(1, 2, 3, 4)]
>>> l1.append(t1[0])
>>> l1
[(1, 2, 3, 4), 1]
>>> 
>>> l1=[]
>>> l1.append(t1[0])
>>> l1
[1]
>>> l1.append(t1[1])
>>> l1
[1, 2]
>>> l1.append(t1[2])
>>> l1
[1, 2, 3]
>>> l1.append(t1[3])
>>> li
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    li
NameError: name 'li' is not defined
>>> 
>>> 
