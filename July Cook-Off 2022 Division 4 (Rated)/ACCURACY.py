for _ in range(int(input())):
    X=int(input())
    y=X%3
    if y!=0:
        print(3-y)
    else:
        print(0)