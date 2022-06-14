for _ in range(int(input())):
    A,B=map(int,input().split(" "))
    C=B-A
    if C%3==0 or C%3==1:
        print("YES")
    else:
        print("NO")