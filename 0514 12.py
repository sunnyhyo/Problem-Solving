#키워드 인수

def calc(x, y, z):
    return (x*1)+(y*2)+(z*3)

calc(y=1,x=3,z=4)
calc(y=2,x=1,z=3)
calc(x=2,z=1,y=3)
calc(x=2,y=1,z=3)
calc(2,1,3)


>>> calc(y=1,x=3,z=4)
17
>>> calc(y=2,x=1,z=3)
14
>>> calc(x=2,z=1,y=3)
11
>>> calc(x=2,y=1,z=3)
13
>>> calc(2,1,3)

13
