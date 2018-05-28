Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> #Dictionary 딕셔너리 자료형
>>> 
>>> #딕셔너리(dictionary)도 리스트와 같이 값을 저장하는 방법이다. 하지만 딕셔너리에는 값(value)과 관련된 키(key)를 함께 저장한다.
>>> 
>>> 
>>> #딕셔너리에 데이터 저장
>>> 
>>> phone_book={}
>>> phone_book['홍길동'] = '010-1234-5678'
>>> print(phone_book)
{'홍길동': '010-1234-5678'}
>>> #홍길동이라는 key 에 전화번호 value 저장
>>> 
>>> phone_book = {"홍길동": "010-1234-5678"}
>>> #한번에 {key:value}
>>> phone_book["강감찬"] = "010-1234-5679"
>>> phone_book["이순신"] = "010-1234-5680"
>>> print(phone_book)
{'홍길동': '010-1234-5678', '강감찬': '010-1234-5679', '이순신': '010-1234-5680'}
>>> #key  값은 유일해야함
>>> #중복입력하면 마지막에 입력한 key : value 값으로 저장된다
>>> 
>>> 
>>> #딕셔너리 검색
>>> print(phone_book['강감찬'])
010-1234-5679
>>> #키를 가지고 값을 검색
>>> 
>>> phone_book.keys()
dict_keys(['홍길동', '강감찬', '이순신'])
>>> #모든 키들을 검색
>>> 
>>> phone_book.values()
dict_values(['010-1234-5678', '010-1234-5679', '010-1234-5680'])
>>> #모든 값들을 검색
>>> 
>>> #딕셔너리의 순서는 상관없음
>>> 
>>> 
>>> #예제
>>> for key in phone_book.keys():
	print(key, phone_book[key])

	
홍길동 010-1234-5678
강감찬 010-1234-5679
이순신 010-1234-5680
>>> #딕셔너리 항목 방문, key, value 출력
>>> 
>>> for key in sorted(phone_book.keys()):
	print(key, phone_book[key])

	
강감찬 010-1234-5679
이순신 010-1234-5680
홍길동 010-1234-5678
>>> #파이썬 내장함수 sortes: 리스트, 딕셔너리 키 등을 인수로 주면 정렬한 결과를 반환
>>> 
