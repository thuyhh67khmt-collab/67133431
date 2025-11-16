# Nhập số cần kiểm tra
n = int(input("Nhập một số: "))

# Kiểm tra 3 điều kiện
if n % 2 == 0 and n > 10 and n % 3 == 0:
    print("Số thỏa mãn cả 3 điều kiện.")
else:
    print("Số KHÔNG thỏa mãn 3 điều kiện.")
