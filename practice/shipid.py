for _ in range(int(input())):
    list=[["b", "BattleShip"],["c", "Cruiser"],["d", "Destroyer"],["f", "Frigate"]]
    l=input()
    for i in range(len(list)):
        if l.lower()==list[i][0]:
            print(list[i][1])