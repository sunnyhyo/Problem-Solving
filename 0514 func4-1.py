#함수정의 연습(4/4)
#함수정의

def hello():
    result= "Hello!"
    return result

def hello():
    return "Hello!"

def repeat(n):
    result = 'Ha' *n
    return result

def repeat(n):
    return 'Ha' *n

#반환값이 있을 것임
def maxList(lst):
    maxVal=lst[0]
    for n in lst:
        if maxVal < n:  #크지 않다면
            maxVal = n  # n 바꿔치기

    return maxVal








    
