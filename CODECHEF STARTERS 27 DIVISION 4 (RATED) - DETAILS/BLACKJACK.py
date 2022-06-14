for _ in range (int(input())):
    A,B=map(int,input().split(' '))
    C=21-(A+B)
    if C<=10:
        print(C)
    else:
        print(-1)