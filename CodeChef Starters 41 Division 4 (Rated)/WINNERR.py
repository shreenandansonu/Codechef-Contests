for _ in range (int(input())):
    pa,pb,qa,qb=map(int,input().split(" "))
    p=[pa,pb]
    p.sort()
    P=p[1]
    q=[qa,qb]
    q.sort()
    Q=q[1]
    if Q>P:
        print("P")
    elif Q<P:
        print("Q")
    else:
        print("TIE")