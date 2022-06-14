lst=[]
while input()!="done":
    y=x-1
    if type(y)==int():
        lst.append(x)
        x=input()
    else:
        print("Put any intigral value")
        x=input()
lst.sort()
print("Largest number is: ",lst[-1],"Smallest number is: ",lst[0])
