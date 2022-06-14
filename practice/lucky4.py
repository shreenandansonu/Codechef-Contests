t=int(input())
for i in range (0,t,1):
    x=input()
    m=0
    for j in range(0,len(x),1):
        if x[j]==str(4):
            m+=1
    print(m)