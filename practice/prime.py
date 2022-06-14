for _ in range(int(input())):
    n=int(input())
    list=[]
    for i in range(2,n):
        list.append(n%i)
    if 0 in list or n==1:
        print("no")
    else:
        print("yes")