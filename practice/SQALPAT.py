n=int(input())
for x in range(1,n+1):
    if x%2!=0:
        print(str(5*(x-1)+1) +" "+ str(5*(x-1)+2) +" "+ str(5*(x-1)+3) +" "+ str(5*(x-1)+4) +" "+ str(5*(x-1)+5))
    elif x%2==0:
        print(str(5*(x-1)+5) +" "+ str(5*(x-1)+4) +" "+ str(5*(x-1)+3) +" "+ str(5*(x-1)+2) +" "+ str(5*(x-1)+1))