def reverse(x):
    return x [::-1]

T=input("Number of test case \n")

i=1
while i <= int(T):
    str=input("Enter the string\n")
    if str==reverse(str):
         print("It is a palindrome \n")
    else:
         print("It is not a palindrome\n")
    print(i)
    i += 1

exit