t=int(input("\n"))
i=1
while i<=t:
    n=int(input("\n"))
    while n>0:
        j=1
        while j<=n:
            if j%5==0:
                print("#", end="")
            else:
                print("*", end="")
            j+=1    
        print("")
        n-=1
    i+=1