for _ in range (0,int(input())):
    A,B,C,D=map(int,input().split(" "))
    if A>=B:
        B=B+C
        if A>=B:
            B=B+D
            if A>=B:
                print('N')
            elif A<B:
                print('S')
        elif A<B:
            A=A+D
            if A>=B:
                print('N')
            elif A<B:
                print('S')
    elif A<B:
        A=A+C
        if A>=B:
            B=B+D
            if A>=B:
                print('N')
            elif A<B:
                print('S')
        elif A<B:
            A=A+D
            if A>=B:
                print('N')
            elif A<B:
                print('S')