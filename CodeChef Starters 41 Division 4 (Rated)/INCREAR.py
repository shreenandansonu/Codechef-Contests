import math
for _ in range(int(input())):
    x,y=map(int,input().split(" "))
    if x>y:
        z=x-y
        if z%2==0:
            print(int(z/2))
        else:
            print(int(math.ceil(z/2)+1))
    elif x<y:
        print(y-x)
    else:
        print(0)