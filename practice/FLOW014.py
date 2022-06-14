for  _ in range (int(input())):
    hardness,carbon,strenght = map(float, input().split())
    if((hardness>50) and (carbon<0.7) and (strenght>5600)):
        print("10")
    elif((hardness>50) and (carbon<0.7)):
        print("9")
    elif((carbon<0.7) and (strenght>5600)):
        print("8")
    elif((hardness>50) and (strenght>5600)):
        print("7")
    elif((hardness>50) or (carbon<0.7) or (strenght>5600)):
        print("6")
    else:
        print("5")