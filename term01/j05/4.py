a, b, c = 10, 30, 20

if a < b and b < c:
    print(f"{a} < {b} < {c}")
elif a < c or b < c:
    print("pass1")
if b < c or c > a:
    print("pass2")