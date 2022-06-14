# cook your dish here
x, y = [float,input().split()]
if (x%5 != 0) or (x > y - 0.50):
    print(y)
else:
    bal = y - x - 0.50
    print("{:.2f}".format(bal))