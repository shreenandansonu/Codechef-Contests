for _ in range (int(input())):
    x,y,z=map(int,input().split(" "))
    t=(x*5)+(y*10)
    n=t//z
    print(n)