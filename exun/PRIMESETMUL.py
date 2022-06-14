num=[1]
for _ in range (int(input())):
    n,m=map(int,input().split(' '))
    lst=list[map(int,input().split(' '))]
    for x in range(2,m):
        y=x
        for a in lst:
            if y%a==0:
                y=y/a
                if y==1:
                    num.append(x)