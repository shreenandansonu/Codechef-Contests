t=int(input()) #test case
i=1
while (i<=t):
    n=int(input()) #no of initial elements
    item=[]
    quant=[]
    j=1
    while(j<=n):
        im,qt=list(map(str,input().split()))
        item.append(im)
        quant.append(qt)
        j+=1
    m=int(input())#no of opperations
    k=1
    while(k<=m):
        oprn,nim,nqt=list(map(str,input().split()))
        if oprn =="ADD":
            if nim in item:
                id1=item.index(nim)
                quant[id1]=int(quant[id1])+int(nqt)
                print("UPDATED Item "+ item[id1])
            else:
                item.append(nim)
                quant.append(nqt)
                print("ADDED Item "+nim)
        elif oprn =="DELETE":
            if nim in item :
                id2=item.index(nim)
                if int(nqt)<int(quant[id2]):
                    quant[id2]=int(quant[id2])-int(nqt)
                    print("DELETED Item "+nim)
                else:
                    print("item "+nim+ " could not be DELETED")
            else:
                print("Item " +nim+ " does not exist")
        k+=1
    j=0
    total=0
    while(j<=len(quant)-1):
        total+=int(quant[j])
        j+=1
    print("Total Items in Inventory: " + str(total))
    item.clear()
    quant.clear()
    i+=1
