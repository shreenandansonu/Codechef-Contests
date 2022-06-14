import math
def compute_distance(x1,y1,x2,y2):
    xdistance=(x1-x2)**2
    ydistance=(y1-y2)**2
    distance= xdistance+ydistance
    eucDistance=math.sqrt(distance)
    return print("Distance: (:.2f}".format(eucDistance))
t=int(input())
while(t>0):
    x1,y1,x2,y2=map(int, input().split())
    compute_distance(x1,y1,x2,y2)
    t=t-1
