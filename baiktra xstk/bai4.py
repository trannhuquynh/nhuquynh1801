a= int(input("nhập số nguyên dương a:"))
def tinhtong(a):
    b=0
    while (a>0):
        b = b + a%10
        a = int(a/10)
    return b
print(" Tổng các chữ số của ", a , "là" ,tinhtong(a))