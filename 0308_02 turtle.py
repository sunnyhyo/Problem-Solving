Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t= turtle.Pen()
>>> 
>>> t.forward(100)
>>> 
>>> #화살표는 방향성이 있음
>>> #화살표의 방향 바꾸기
>>> 
>>> t.right(90)
>>> t.forward(100)
>>> t.right(90)
>>> t.fw(100)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.fw(100)
AttributeError: 'Turtle' object has no attribute 'fw'
>>> t.fd(100)
>>> t.right(90)
>>> t.forward(100)
>>> 
=============================== RESTART: Shell ===============================
>>> # 육각형 그리기
>>> 
>>> import turtle
>>> t= turtle.Pen()
>>> t.forward(100)
>>> t.right(60)
>>> t.forward(100)
>>> t.right(60)
>>> t.forward(100)
>>> t.right(60)
>>> t.forward(100)
>>> t.right(60)
>>> t.forward(100)
>>> t.right(60)
>>> t.forward(100)
>>> 
