from math import sqrt
print('giải phương trình bậc 2')
a= float(input("nhập a: "))
b= float(input("nhập b: "))
c= float(input("nhập c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        if c == 0:
            print("phương trình có một nghiệm x = 0")
        else:
            print("phương trình có một nghiệm x= = -c/b")
else:
    delta = -b**2 - 4 * a * c
    if (delta < 0):
        print("phương trình vô nghiệm")
    if (delta == 0):
        print("phuông trình có nghiệm kép x= ", -b/(2*a))
    else:
        print("phương trình có 2 nghiệm phân biệt:")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))
