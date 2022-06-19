import math


for _ in range(int(input())):
    N=int(input())
    if N%2==0:
        sequence=""
        for i in range(int(N/2)):
            if i%2!=0:
                sequence+="1"
            else:
                sequence+="0"
        for i in range(int(N/2),N):
            if i%2!=0:
                sequence+="0"
            else:
                sequence+="1"           
        print(sequence)
    else:
        sequence=""
        for i in range(int((N-1)/2)):
            if i%2!=0:
                sequence+="1"
            else:
                sequence+="0"
        if math.ceil(N/2)%2==0:
            sequence+="1"
        else:
            sequence+="0"
        for i in range(int((N+1)/2),N):
            if i%2==0:
                sequence+="0"
            else:
                sequence+="1"
        print(sequence) 