for _ in range(0,int(input())):
    basic_salary=int(input())
    if basic_salary <1500:
        print("{0:.2f}".format(basic_salary+ 0.1*basic_salary+0.9*basic_salary))
    else:
        print("{0:.2f}".format(basic_salary+500+0.98*basic_salary))