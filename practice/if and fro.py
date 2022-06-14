import math
T=input("Number of test case \n")

i=1
while i <= int(T):
    n=input()
    j=0
    while j<int(n):
        if (j==0):
            print("3") 
        elif(j%2==0):
            print(j*2)
        elif(j%2!=0):
            print(j*j)
        j +=1
    i += 1

exit