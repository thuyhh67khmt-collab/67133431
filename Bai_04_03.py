# Nhập nhiệt độ và loại
temp = float(input("Nhập nhiệt độ: "))
loai = input("Nhập loại (C/F/K): ").upper()

if loai == "C":
    f = temp * 9/5 + 32
    k = temp + 273.15
    print(f"{temp:.2f} °C = {f:.2f} °F = {k:.2f} K")
elif loai == "F":
    c = (temp - 32) * 5/9
    k = c + 273.15
    print(f"{temp:.2f} °F = {c:.2f} °C = {k:.2f} K")
elif loai == "K":
    c = temp - 273.15
    f = c * 9/5 + 32
    print(f"{temp:.2f} K = {c:.2f} °C = {f:.2f} °F")
else:
    print("Loại nhiệt độ không hợp lệ!")
