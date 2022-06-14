item_name=[]
item_quantity=[]

Operation_list=[]
operated_name_list=[]
operated_quantity_list=[]

N=int(input())

for i in range(N):
    name,quantity=list(map(str,input().split()))
    item_name.append(name)
    item_quantity.append(quantity)

Opr=int(input())

for i in range(Opr):
    Operation,operated_name,operated_quantity=list(map(str,input().split()))
    
    Operation_list.append(Operation)
    operated_name_list.append(operated_name)
    operated_quantity_list.append(operated_quantity)

for i in range(Opr):
    if Operation_list[i]=="Delete" or Operation_list[i]=="delete" or Operation_list[i]=="DELETE":
        
        for j in range(N):
            
            if operated_name[i]==item_name[j]:
                
                if operated_quantity<=item_quantity[j]:
                    item_quantity=item_quantity-operated_quantity
                    print("Deleted "+operated_quantity[i]+" items from "+operated_name)
                    break
                elif j==N:
                    print("Cannot delete "+operated_quantity[i]+" items from "+operated_name)
            
            else:
                continue

    elif Operation_list[i]=="Add" or Operation_list[i]=="add" or Operation_list[i]=="ADD":

        for j in range(N):
            
            if operated_name[i]==item_name[j]:
                item_quantity[j]+=operated_quantity
                print("Added "+operated_quantity[i]+" items in "+operated_name)
                N=N+1
                break

            elif j==N:
                item_name.append(operated_name[i])
                item_quantity.append(operated_quantity[i])
                print("Added "+operated_quantity[i]+" items in "+operated_name)
                N=N+1
                break

Total=0
for i in range(N):
    Total+=item_quantity[i]

print("Total item is",Total)