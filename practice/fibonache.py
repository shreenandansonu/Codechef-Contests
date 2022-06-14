for _ in range(int(input())):
    fib=1
    n=int(input())
    for x in range(1,n+1):
        fib+=fib
    print(fib)