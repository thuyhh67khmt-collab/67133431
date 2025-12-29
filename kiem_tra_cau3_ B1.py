n=int(input("Nhap so luong phan tu:"))
arr=[ ]

for i in range(n):
    x=int(input(f"Nhap phan tu thu {i+1}"))
    arr.append(x)
print("Cac phan tu chia het cho ca 2 va 3 la:")
for x in arr:
    if x % 6==0:
        print(x)