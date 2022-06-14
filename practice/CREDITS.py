for _ in range (int(input())):
    X=int(input())
    if X>65:
        print('Overload')
    elif X<35:
        print('Underload')
    else:
        print('Normal')