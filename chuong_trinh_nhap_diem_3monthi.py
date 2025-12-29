toan=int(input("Nhap diem mon Toan"))
ly=int(input("Nhap diem mon Ly"))
hoa=int(input("Nhap diem mon Hoa"))
tongdiem3mon= toan+ ly + hoa
if tongdiem3mon >= 15  and toan >= 5 and ly >= 5 and hoa >= 5 :
    print("hoc deu cac mon va dau")
elif tongdiem3mon >= 15 and toan >=4 and ly >= 4 and hoa >=4 :
    print("dau")
else:
    print("hoc chua deu cac mon")