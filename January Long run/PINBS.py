for _ in range (int(input())):
    no=[]
    S=str(input())
    prime_numbers=['10','11','101','111','1011','1101','10001','10011','10111','11101']
    for x in prime_numbers:
        if len(S)>len(x):
            b=S.find(x)
            if b>=0:
                print('YES')
                no.append('YES')
                break
            else:
                no.append('NO')                  
        else:
            break
    if 'YES' not in no:
           print('NO')