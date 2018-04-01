Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #특수문자
>>> #이스케이프 문자
>>> # \ 백슬래시 기호와 함께 문자 조합해서 특수한 목적으로 사용
'
>>> 
>>> print("동해물과 \n백두산이\n마르고 닳도록")
동해물과 
백두산이
마르고 닳도록
>>> print("""동해물과
백두산이
마르고 닳도록""")
동해물과
백두산이
마르고 닳도록
>>> 
>>> print('''동해물과
백두산이
마르고 닳도록''')
동해물과
백두산이
마르고 닳도록
>>> 
>>> food = "Python's favorite food is perl”
SyntaxError: EOL while scanning string literal
>>> food = "Python's favorite food is perl"
>>> 
>>> print(food)
Python's favorite food is perl
>>> 
>>> food = 'Python\'s  favorite food is perl'
>>> print(food)
Python's  favorite food is perl
>>> 
>>> say = '"Python is very easy." he says.'
>>> print(say)
"Python is very easy." he says.
>>> 
>>> say="\"Python is very easy.\" he says."
>>> print(say)
"Python is very easy." he says.
>>> 
>>> print('이름\t학번\t성적')
이름	학번	성적
>>> print('\\ \\ \\ \\ \\\')
	  
SyntaxError: EOL while scanning string literal
>>> print('\\ \\ \\ \\ \\')
	  
\ \ \ \ \
>>> print('\\ \\ \\ \\ \\\'')
	  
\ \ \ \ \'
>>> 
	  
>>> multiline="""Life is too short
You need python"""
	  
>>> print(multiline)
	  
Life is too short
You need python
>>> 
	  
>>> multiline='''Life is too short
You need python'''
	  
>>> print(multiline)
	  
Life is too short
You need python
>>> 
	  
>>> multiline='Life is too short\nYou need python'
	  
>>> print(multiline)
	  
Life is too short
You need python
>>> 
