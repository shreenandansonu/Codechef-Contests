for _ in range (int(input())):
    A,B=map(int,input().split(" "))
    C=A+B
    if C%2==0:
        print("YES")
    else:
        print("NO")