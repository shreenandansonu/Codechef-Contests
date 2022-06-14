def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
for _ in range(int(input())):
    s=input()
    if reverse(s)==s:
        print("wins")
    else:
        print("loses")