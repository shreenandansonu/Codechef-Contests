for _ in range(int(input())):
    X,Y,A=map(int,input().split(" "))
    if X<=A & A<Y:
        print("YES")
    else:
        print("NO")