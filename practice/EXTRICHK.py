lst=list(map(int,input().split(" ")))
lst.sort()
a,b,c=lst[0],lst[1],lst[2]
if (a+b>c):
    if a==b==c:
        print(1)
    elif a==b or b==c or c==a:
        print(2)
    else:
        print(3)
else:
    print(-1)