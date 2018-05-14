#함수의 호출 (2/3)
#함수정의
#전달받은 인자를 정의한 변수에 저장
def computeAverage(num1,num2):      #parameter
    result=(num1+num2)/2
    return result

#두 수에 대한 평균 구하는 프로그램
#전달인자, 인수, argument 2,6
val=computeAverage(2,6)         
print("평균 =",val)
