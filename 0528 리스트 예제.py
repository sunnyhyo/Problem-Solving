# 예제1
import random

animals = [‘cat’, ‘dog’, ‘tiger’, ‘rabbit’, ‘turtle’]
alreadyfeed = []
count = 0

if ‘cow’ not in animals:
    animals.append(‘cow’)

while True:
    animal = random.choice(animals)
    if animal in alreadyfeed: continue      #만약 리스트 안에 있다면, contine 다시 올라가서 animal choice
    
    print(“feed”, animal)
    alreadyfeed.append(animal)  #먹인 동물들은 리스트에 추가한 뒤
    count += 1    #count 하나를 올린다
    if count == len(animals) : break  #만약 동물 수와 먹인 동물들 수가 같으면  logic stop



# 예제2
animals = [‘cat’, ‘dog’, ‘tiger’, ‘rabbit’, ‘turtle’]

while True:
    animal = animals.pop()  #마지막에 있는 동물 POP 하고 먹인다. 리스트에서 삭제
    print(“feed”, animal)  #먹인 동물들 print, 반복
    if len(animals) == 0: break  #list에 남아있는 동물이 0이면 break
