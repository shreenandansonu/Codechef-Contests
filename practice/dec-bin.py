def convert( x ):
    if x == 0:
        return 0
    else:
        return (x % 2 + 10 *
                convert(int(x // 2)))

t=int(input())
i=1
while (i<=t):
    x = int(input())
    print(convert(x))
    i+=1