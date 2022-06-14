for _ in range(int(input())):
    N=int(input())
    S=str(input())
    if len(S)==N:
        index_code=S.find('code')
        index_chef=S.find('chef')
        if index_code<index_chef:
            print('AC')
        else:
            print('WA')
    else:
        print('WA')