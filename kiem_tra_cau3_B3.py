n=int(input("Nhap vao so nguyen duong bat ki: "))
def is_armstrong(n):
    result = True
    if n < 0:
        result = False
    str_n = str(n)
    k = len(str_n)
    total = 0
    for digit in str_n:
        total += int(digit) ** k
    result = total == n
    return result
print(f"{n} la so Armstrong: {is_armstrong(n)}")