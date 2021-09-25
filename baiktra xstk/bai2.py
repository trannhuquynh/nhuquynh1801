Q=[1,1,2,3,5,6,15,21,34]
Q1=[1,3,5,4,7,88,66,59,40,54]
print("list Q", Q)
print("list Q1", Q1)
Q2= list(set (Q) & set (Q1))
print("Các phần tử trùng nhau trong 2 mảng là:",Q2)
Q3= list(set (Q) & set (Q2))
print("Các phần tử không trùng nhau của list Q và list Q1 là:",Q3)
Q4= list(set (Q1) & set (Q2))
print("Các phần tử không trùng nhau của list Q1 và list Q2 là:",Q4)

