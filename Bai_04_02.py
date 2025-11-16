# Nhập thông tin học sinh
ten = input("Nhập tên học sinh: ")
diem_toan = float(input("Điểm Toán: "))
diem_ly = float(input("Điểm Lý: "))
diem_hoa = float(input("Điểm Hóa: "))

# Tính điểm trung bình
dtb = (diem_toan + diem_ly + diem_hoa) / 3

# Xếp loại
if dtb >= 8:
    xeploai = "Giỏi"
elif dtb >= 6.5:
    xeploai = "Khá"
elif dtb >= 5:
    xeploai = "Trung bình"
else:
    xeploai = "Yếu"

# Xuất kết quả
print("\n=== KẾT QUẢ HỌC SINH ===")
print(f"Tên học sinh: {ten}")
print(f"Điểm Toán: {diem_toan:.2f}")
print(f"Điểm Lý: {diem_ly:.2f}")
print(f"Điểm Hóa: {diem_hoa:.2f}")
print(f"Điểm trung bình: {dtb:.2f}")
print(f"Xếp loại: {xeploai}")
