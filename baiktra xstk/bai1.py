Q1 = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
print("Q1: ", Q1)
print("Q2: ")
for i in range(0, 15):
    if(Q1[i] < 30):
        Q2 = Q1[i]
        print(Q2, end=", ")
print("Nhập a: ")
a = input("")
print("Những số nhỏ hơn a là: ")
for i in range(0, 15):
    if(Q1[i] < int(a)):
        Q3 = Q1[i]
        print(Q3, end=", ")