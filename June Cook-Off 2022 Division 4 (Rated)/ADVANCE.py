for _ in range (int(input())):
    X,Y= map(int, input().split(" "))
    if Y> X+200 or Y<X:
        print("NO")
    else:
        print("YES")