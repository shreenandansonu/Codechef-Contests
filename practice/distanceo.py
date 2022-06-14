import math as a
def compute_distance (x1,y1,x2,y2):
    xd=(x1-x2)**2
    yd=(y1-y2)**2
    td=a.sqrt(xd+yd)
    return print("Distance: "+str(round(td, 2)))
t=int(input())
while(t>0):
    x1,y1,x2,y2=map(int,input().split())
    compute_distance(x1,y1,x2,y2)
    t-=1
