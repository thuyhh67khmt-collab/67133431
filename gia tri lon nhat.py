def GTLN(a,b,c):
    maxx=a
    if maxx<b:
        maxx=b
    if maxx<c:
        maxx=c
    return maxx
a,b,c=map (int,input("Nhập a,b,c:").split())
a=GTLN (a,b,c)
print (a)

