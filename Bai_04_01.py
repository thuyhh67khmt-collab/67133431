# Nhập số điện tiêu thụ
so_dien = int(input("Nhập số điện tiêu thụ (kWh): "))

tien = 0
if so_dien <= 50:
    tien = so_dien * 1678
elif so_dien <= 100:
    tien = 50 * 1678 + (so_dien - 50) * 1734
elif so_dien <= 200:
    tien = 50 * 1678 + 50 * 1734 + (so_dien - 100) * 2014
elif so_dien <= 350:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (so_dien - 200) * 2536
else:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 150 * 2536 + (so_dien - 350) * 2927

print(f"Tổng tiền điện: {tien:,} VND")
