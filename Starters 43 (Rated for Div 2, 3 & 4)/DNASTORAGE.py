for _ in range(int(input())):
    N=int(input())
    S=str(input())
    M=[]
    for i in range(0,N,2):
        if S[i]+S[i+1]=="00":
            M.append("A")
        elif S[i]+S[i+1]=="01":
            M.append("T")
        elif S[i]+S[i+1]=="10":
            M.append("C")
        else:
            M.append("G")
    for y in M:
        print(y,end="")






#        print(S[i])
#        if int(S[i])==0:
#            if int(S[i+1])==0:
#                N.append("A")
#            else:
#                N.append("T")
#        else:
#            if int(S[i+1])==0:
#                N.append("C")
#            else:
#                N.append("G")