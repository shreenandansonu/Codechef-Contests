for _ in range(int(input())):
    P,Q=map(int,input().split(" "))
    if (P+Q)%4==0 or (P+Q)%4==1 :
        print("ALICE")
    else:
        print("BOB")