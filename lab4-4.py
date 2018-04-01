#lab4-4

name=input("파일 이름을 입력하시오.: ")

ext=name[-4]

if ext=='.':
    oh=name[-3:]
else:
    oh=name[-2:]

print("입력한 파일의 확장자는 \n%s입니다."%oh)
