lst=list(map(int,input().split(" ")))
lst.sort()
for _ in range(lst[0],lst[1]+1):
    if _%2!=0:
        print(_, end=" ")