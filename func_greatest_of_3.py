def func_greatest_of_3_no(a,b,c):
    if (a>b and a>c):
        print("A is a greatest number")
    elif (b>a and b>c):
        print("B is a greatest number")
    elif (c>b and c>a):
        print("C is a greatest number")


a = int(input("enter 1st num : "))
b = int(input("enter 2nd num : "))
c = int(input("enter 3rd num : "))

func_greatest_of_3_no(a,b,c)