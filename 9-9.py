#Lab9-9 (list에 저장된 숫자들의 합)

list1 = [10, 20, 30]
list2 = ["100", "200", "300"]

#list1의 숫자들 합을 위한 변수 초기화
sum1 = 0
for item in list1:
    sum1 += item

#list2의 숫자들 합을 위한 변수 초기화
sum2 = 0
for item in list2:
    # list2 의 item은 문자열이므로 숫자로 변환 후 덧셈
    sum2 += int(item)

print("list1의 합은 %d 입니다." %sum1)
print("list2의 합은 %d 입니다." %sum2)

list1의 합은 60 입니다.
list2의 합은 600 입니다.
