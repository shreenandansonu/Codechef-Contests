import math
T=input("Number of test case \n")
i=1
while i <= int(T):
    p=input().split()
    my_map=list(map(int,p))
    distance = math.sqrt (( ((my_map[0]-my_map[2])**2)+((my_map[1]-my_map[3])**2) ))
    print("Distance: " + str(distance))
         
    i += 1
