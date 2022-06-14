for _ in range(int(input())):
    N=int(input())
    for r in range (1,N+1):
        for c in range (1,N+1):
            if c==r and c!=1 and c!=3:
                print('Q',end=(''))
            else:
                print('.',end=(''))
        print('\n')
        