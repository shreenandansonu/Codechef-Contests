def lapindrome(stri,stri_len):
    front_stri=stri[(0,stri_len/2,1)]
    end_stri=stri[(-stri_len/2,-1,-1)]
    if front_stri==end_stri:
        print("YES")
    else:
        print("NO")

for _ in range (0,int(input())):
    stri=input()
    stri_len=len(stri)
    if stri_len/2!=0:
        stri_len=stri_len-1
    elif stri_len/2!=0:
        stri_len=stri_len
    lapindrome(stri,stri_len)