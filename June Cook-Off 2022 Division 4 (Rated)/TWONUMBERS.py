
for _ in range(int(input())):
    N=int(input())
    if N%2!=0:
        y=(N//2)+1
        print(int((N-y)*y-1))
    else:
        if (N/2)%2==0:
            x=(N/2)+1
            print(int((N-x)*x-1))
        else:
            x=(N/2)+2
            print(int((N-x)*x-1))

