import math
def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt (( ((x1-x2)**2)+((y1-y2)**2) ))
    return print("Distance: "+str("{0:.2f}".format(distance)))
test_cases = int(input())
i=1
while i <= int(test_cases):
    p=input().split()
    x1, y1, x2, y2=list(map(float,p))
    compute_distance(x1, y1, x2, y2)
    i+=1

    