import math
T=input("Number of test case \n")
i=1
while i <= int(T):
    list=[]
    for j in range(4):
        p=float(input())
        list.append(p)
        j+=1
    distance = math.sqrt (( ((list[0]-list[2])**2)+((list[1]-list[3])**2) ))
    print("Distance: " + str(distance))
         
    i += 1
