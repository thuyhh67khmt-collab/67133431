def GTLN(a,b,c):
    maxx=a
    if maxx<b:
        maxx=b
    if maxx<c:
        maxx=c
    return maxx
def GTNN(a,b,c):
    minx=a
    if minx>b:
        minx=b
    if minx>c:
        minx=c
    return minx
a=int(input("Nhap so a:"))
b=int(input("Nhap so b:"))
c=int(input("Nhap so c:"))
max=GTLN(a,b,c)
print(f" So lon nhat la {max}")
min=GTNN(a,b,c)
print(f" So nho nhat la {min}")