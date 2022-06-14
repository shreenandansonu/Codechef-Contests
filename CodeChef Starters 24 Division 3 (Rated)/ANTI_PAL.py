for _ in range (int(input())):
    N=int(input())
    S=input()
    if N/2==0:
        anti_pal=[None]*N
        for s in S:
            i=0
            while i<=N:
                if anti_pal[N-i]!=s:
                    anti_pal[i]=s
                    i+=1
                    continue
        if None in anti_pal:
            print('NOd')
        else:
            print('YES')
    else:
        print('NO')