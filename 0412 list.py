Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #list 자료형
>>> 
>>> n=[2,3,5,7]
>>> len(n)
4
>>> n[0]
2
>>> n[1]
3
>>> n[2]
5
>>> n[3]
7
>>> 
>>> color=["blue","red","yellow"]
>>> len(color)
3
>>> 
>>> color[0]
'blue'
>>> color[1]
'red'
>>> color[2]
'yellow'
>>> 
>>> 
>>> for i in range(len(color)):
	print(color[i])  

	
blue  #color[0] 0번째 아이템 
red   #color[1] 1번째 아이템
yellow  #color[2] 2번째 아이템
>>> 
>>> for i in range(0,4):  #범위 밖의 아이템은 오류
	print(color[i])

	
blue
red
yellow
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    print(color[i])
IndexError: list index out of range
>>>
>>> #len()  문자열 이 포함된 개수, 키워드의 개수, list 에 포함된 item의 개수
>>> 
>>> len("HELLO")
5
>>> len(color)
3
>>> 
