n=int(input("양의 정수 입력:"))
i, sum=0,0

while(i<n):  #사용자가 입력한 수 보다 i 가 적은가?
    sum+=i   #누적합
    i+=1     #i에 1을 더함
    print(sum) 
