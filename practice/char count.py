for t in range(int(input())):
    string_to_list = (str(input()).split( ))
    for i in range (0,len(string_to_list)):
        length=len(string_to_list[i])
        if(string_to_list[i][0]=="@"):
            length=length-1
        if(i==(len(string_to_list)-1)):
            print(length,end="")
        else:
            print(length,end=",")
    print("\n")