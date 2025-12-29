a=int(input("Nhap so a:"))
b=int(input("Nhap so b:"))

if a==0 and b==0:
    print("Phuong trinh vo so nghiem")
elif a==0 and b!=0:
    print("Phuong trinh vo so nghiem")
else:
    x= -b/a
    print("Phuong trinh có nghiem x=",x)