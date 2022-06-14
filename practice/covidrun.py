t=int(input())
list=[]
for i in range(t):
    list.clear()
    n,k,x,y=map(int,input().split())
    if (x>y) and (x>0):
        for j in range(round(n/k)):
            x-=j*k
            if (x==y):
                list.append("YES")
            else:
                list.append("NO")
    if (x<y) and (x<n):
        for j in range(round(n/k)):
            x+=j*k
            if (x==y):
                list.append("YES")
            else:
                list.append("NO")
    if "YES" in list:
        print("YES")
    else:
        print("NO")