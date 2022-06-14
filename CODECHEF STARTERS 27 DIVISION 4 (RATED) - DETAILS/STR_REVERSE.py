for _ in range(int(input())):
    s=input()
    n=0
    for i  in range(0,len(s)):
        if s[i]!=s[-1-i]:
            n+=1
    print(n)
