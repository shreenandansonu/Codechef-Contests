def per_arr(val):
    res = []
    
    if(val%2 == 0):
        pivot = val//2
        for i in range(val):
            if(i%2 == 0):
                res.append(pivot-((i+1)//2))
            else:
                res.append(pivot+((i+1)//2))
    else:
        pivot = (val//2)+1
        for i in range(val):
            if(i%2 == 0):
                res.append(pivot+((i+1)//2))
            else:
                res.append(pivot-((i+1)//2))
    return reversed(res)

N = int(input())
for _ in range(N):
    val = int(input())
    print(*per_arr(val))
        