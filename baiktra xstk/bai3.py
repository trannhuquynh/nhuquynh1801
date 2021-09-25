a= int(input("nhập số cần tính giai thừa:"))
def giaithua(a):
    if(a<0):
        int(input("nhập lại a là số nguyên dương:"))
    if a==0:
        return 1
    return a* giaithua(a-1)
print("Giai thừa của ", a ,"là", giaithua(a))