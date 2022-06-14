t=int(input())
i=1
list1=[]
list2=[]
list3=[]

while(i<=t):
    n=int(input())
    j=1
    while(j<=n):
        name,mark=list(map(str,input().split()))
        list1.append(name)
        list2.append(mark)
        j+=1
    max_value=max(list2)
    for p in range(0,n):
        if list2[p]==max_value:
            list3.append(list1[p])
            p+=1
    list3.sort()
    for s in list3:
        print(s,end="\n")
    list1.clear()
    list2.clear()
    list3.clear()   
    i+=1
