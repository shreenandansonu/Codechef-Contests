t=input("\n")
i=1
while i <= int(t):
    n = int(input())
    for line in range(n,0,-1):
        for star in range(0,line):
            if (star+1)%5==0:
                print("#", end=" ")
            else:
                print("*", end=" ")
        print("\n")
    i+=1