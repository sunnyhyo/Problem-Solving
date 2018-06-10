#Lab9-4  n! 계산 함수 (사용자가 종료할 때까지 반복)
#factorial 함수 정의 작성
#factorial 함수 계산할 n을 파라미터로 받는다.
#n! 계산한 결과 반환
def factorial(n):
    result = 1

    for i in range(1, n+1):
        result += i

    return result

#팩토리얼 계산할 값을 사용자에게 입력 받아
#팩토리얼을 계산하는 factorial 함수 호출
#사용자가 음의 정수 입력하면 양의 정수 입력하라는 메세지 출력
#사용자가 0을 입력하면 팩토리얼 계산 종료
while True:
    print()
    num = int(input("팩토리얼 구할 정수를 입력(0은 종료): "))

    if num == 0:
        print("프로그램을 종료합니다.")
        break
    elif num < 0:
        print("양의 정수를 입력하세요.")
        continue

    result = factorail(num)
    print("%d!은 %d입니다" %(num, result))
