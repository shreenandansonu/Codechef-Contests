t=int(input())
j=1
while j<=t:
    Str=str(input())
    string_to_list = (Str.split())
    i=0
    while(i<=len(string_to_list)):
            length=len(string_to_list[i])
            if(string_to_list[i][0]=="@"):
                length=length-1
            if(i==len(string_to_list)):
                print(length,end="")
            else:
                print(length,end=",")
            print("\n")
            i+=1
    j+=1