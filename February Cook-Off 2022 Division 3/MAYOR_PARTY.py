for _ in range (int(input())):
    Pa,Pb,Pc=map(int,input().split(' '))
    if Pb>(Pa+Pc):
        print(Pb)
    else:
        print(Pa+Pc)