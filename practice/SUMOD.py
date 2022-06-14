t=int(input())
i=1
while(i<=t):
    n=input()
    j=1
    total=0
    while (j<=len(n)):
        total=total+int(n[j-1])
        j+=1
    print(total)
    i+=1
