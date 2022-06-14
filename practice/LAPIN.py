for _ in range(int(input())):
    S=input()
    left,right=0,(len(S)-1)
    while left<=right:
        if S[left]!=S[right]:
            print('NO')
            break
        else:
            left+=1
            right-=1