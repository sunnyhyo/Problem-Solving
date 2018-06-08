#재귀함수2

def descending(n):
    if n==1:
        print(n)
    else:
        print(n)        #출력
        descending(n-1) #호출

descending(10)

#출력을 먼저 함
print()


def ascending(n):
    if n==10:
        print(n)
    else:
        print(n)
        ascending(n+1)
ascending(1)

print()

        
def ascending(n):
    if n==1:
        print(n)
    else:
        ascending(n-1)  #호출
        print(n)        #출력
        
ascending(10)
        
