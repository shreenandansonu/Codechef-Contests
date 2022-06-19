for _ in range(int(input())):
    a, b, n = map(int, input().split())
    bx = bin(a^b)[2:]
    bn = bin(n)[2:]
    if a==b:
        print(0)
    elif len(bx) > len(bn):
        print(-1)
    elif a^b >= n:
        print(2)
    else:
        print(1)