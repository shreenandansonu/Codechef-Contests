for _ in range(int(input())):
    M=int(input())
    S=str(input())
    N=""
    for i in range(0,M,2):
        if int(S[i])==0:
            if int(S[i+1])==0:
                N+="A"
            else:
                N+="T"
        else:
            if int(S[i+1])==0:
                N+="C"
            else:
                N+="G"
    print(N)