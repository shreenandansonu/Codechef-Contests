L=int(input())
B=int(input())
A=L*B
P=2*(L+B)
if A>P:
    print('Area')
    print(A)
elif A<P :
    print('Peri')
    print(P)
else:
    print('Eq')
    print(P)