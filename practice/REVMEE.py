N=int(input())
lst=list(map(int,input().split(" ")))
for _ in (lst[::-1]):
    print(_ ,end=" ")