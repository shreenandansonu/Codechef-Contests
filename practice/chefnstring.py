for _ in range(int(input())):
    s=list(input())
    j=0
    k=0
    for i in range(0,len(s)-1):
        if s[i]+s[i+1]=="xy" or s[i+1]+s[i]=="xy":
            j+=1
    for i in range(0,len(s)-2):
        if s[i]+s[i+1]+s[i+2]=="xyx" or s[i]+s[i+1]+s[i+2]=="yxy":
            k+=1
    print(j-k)