#0315  input


hello=input()
print(hello)


hello=input("인사말 입력: ")  #프롬프트 문자열 
print(hello)

home=input()
print(home)

home=input("고향은? ")
print(home)

#input 으로 들어온 값은 무조건 문자열
# 즉, 숫자를 입력해도 문자열로 들어옴
# 따라서 숫자 연산을 하고 싶으면 숫자로 변환하는 것이 필요


myAge=input("my age? ")
yourAge=input("your Age? ")
print(myAge)
print(yourAge)
print(myAge+yourAge)
