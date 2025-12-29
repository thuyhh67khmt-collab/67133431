n=int(input("Nhap so luong phan tu:"))
arr=[ ]
for i in range(n):
    x=int(input(f"Nhap phan tu thu{i+1}"))
    arr.append(x)
tong=0
for x in arr:
     if x % 2==0 or x % 3==0:
        tong+=0
print("Tong cac phan tu chia het cho 2 hoac 3 laf :", tong)


