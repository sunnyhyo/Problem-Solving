#예제 2
# 함수 정의 (원의 면적 구하는 함수)
def calculate_area (radius):
    area = 3.14 * radius**2
    return area

# 본 프로그램
n = float(input("숫자 입력: "))
c_area = calculate_area(n)

print(c_area)
