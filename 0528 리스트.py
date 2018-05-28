Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #리스트
>>> 
>>> heroes=[]
>>> heroes.append("아이언맨")
>>> heroes
['아이언맨']
>>> heroes.append("닥터스트레인지")
>>> print(heroes)
['아이언맨', '닥터스트레인지']
>>> 
>>> a=[]
>>> b=['a','b']
>>> c=[1,2,3]
>>> 
>>> #a,b,c 각각은 리스트 객체
>>> c.append(4)
>>> c
[1, 2, 3, 4]
>>> #모든 대상은 객체 - 객체지향적 언어
>>> # . 으로 객체, 함수 연결
>>> 
>>> letters=['A','B','C','D','E','F']
>>> print(letters[0])
A
>>> print(letters[1)]
SyntaxError: invalid syntax
>>> print(letters[1])
B
>>> letters[2]
'C'
>>> print(letters[2])
C
>>> 
>>> print(letters[2:5])
['C', 'D', 'E']
>>> #인덱싱, 슬라이싱 가능
>>> 
>>> print(letters[:3])
['A', 'B', 'C']
>>> print(letters[:])
['A', 'B', 'C', 'D', 'E', 'F']
>>> heroes=['아이언맨','토르','헐크','스칼렛 위치']
>>> heroes[1]
'토르'
>>> heroes[1]='닥터 스트레인지'
>>> #인덱스를 이용하여 수정한다
>>> heroes[1]
'닥터 스트레인지'
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치']
>>> 
>>> #특정 항목의 인덱스 찾기
>>> 
>>> print(heroes.index('헐크'))
2
>>> 
>>> #리스트의 복사
>>> 
>>> a=[1,2,3,4,5]
>>> b=a
>>> print(a)
[1, 2, 3, 4, 5]
>>> print(b)
[1, 2, 3, 4, 5]
>>> b[1]=30
>>> print(a)
[1, 30, 3, 4, 5]
>>> print(b)
[1, 30, 3, 4, 5]
>>> # a is assigned in b
>>> # dependent
>>> 
>>> a=[1,2,3,4,5]
>>> b=[:]  #리스트에 항목들을 복사
SyntaxError: invalid syntax
>>> b=a[:]  #리스트에 항목들을 복사
>>> print(a)
[1, 2, 3, 4, 5]
>>> print(b)
[1, 2, 3, 4, 5]
>>> b[1]=30
>>> print(a)
[1, 2, 3, 4, 5]
>>> print(b)
[1, 30, 3, 4, 5]
>>> # independent
>>> 
>>> 
>>> #특정 위치에 항목 삽입
>>> heroes
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치']
>>> heroes.append('스파이더맨')
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']
>>> 
>>> heroes.insert(1, '배트맨')
>>> print(heroes)
['아이언맨', '배트맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']
>>> #1번 인덱스의  아이템으로 삽입
>>> 
>>> #파이썬 내장함수 len(리스트) : 리스트의 항목 반환
>>> len(heroes)
6
>>> 
>>> 
>>> #항목 삭제
>>> heroes=['아이언맨','토르','헐크','스칼렛 위치']
>>> heroes.remove('스칼렛우치')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    heroes.remove('스칼렛우치')
ValueError: list.remove(x): x not in list
>>> heroes.remove('스칼렛 위치')
>>> print(heroes)
['아이언맨', '토르', '헐크']
>>> heroes
['아이언맨', '토르', '헐크']
>>> 
>>> 
>>> #파이썬 내장 함수 del(리스트[n]) : 리스트의 특정 위치에 있는 항목 삭제
>>> heroes=['아이언맨','토르','헐크','스칼렛 위치']
>>> del(heroes[0])  #0번 인덱스 항목 삭제
>>> print(heroes)
['토르', '헐크', '스칼렛 위치']
>>> 
>>> 
>>> #항목이 리스트 안에 있는지 체크
>>> if '슈퍼맨' in heroes:
	heroes.remove('슈퍼맨')

	
>>> heroes
['토르', '헐크', '스칼렛 위치']
>>> 
>>> if '슈퍼맨' in heroes:
	heroes.append('슈퍼맨')

	
>>> heroes
['토르', '헐크', '스칼렛 위치']
>>> 
>>> if '슈퍼맨' not in heroes:
	heroes.append('슈퍼맨')

	
>>> heroes
['토르', '헐크', '스칼렛 위치', '슈퍼맨']
>>> 
>>> 
>>> #pop() : 리스트의 마지막 항목 꺼내옴
>>> heroes=['아이언맨','토르','헐크','스칼렛 위치']
>>> last_hero = heroes.pop()
>>> print(last_hero)
스칼렛 위치
>>> 
>>> 
>>> #리스트 방문/정렬
>>> #리스트 방문 : 리스트의 항목을 차례로 읽어볼 수 있음
>>> heroes=['아이언맨','토르','헐크','스칼렛 위치']
>>> for hero in heroes:
	print(hero)

	
아이언맨
토르
헐크
스칼렛 위치
>>> 
>>> #알파벳 순서대로 sorting
>>> heroes=['아이언맨','토르','헐크','스칼렛 위치']
>>> heroes.sort()    #list의 항목을 정렬
>>> print(heroes)
['스칼렛 위치', '아이언맨', '토르', '헐크']
>>> 
>>> 
