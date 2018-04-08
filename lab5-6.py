#lab5-6

n_pencil=int(input("연필 개수 입력: "))
n_pen=int(input("볼펜 개수 입력: "))

p_pencil=1000
p_pen=2000

tot= n_pencil*p_pencil + n_pen*p_pen
#print(tot)

if tot >10000:
    tot=tot*0.9
    print("10%% 할인되었습니다. \n지불할 돈: %s원" %tot) #% 문자 자체를 쓰기 위해 %%
else:
    print( "\n지불할 돈: %s원" %tot)
