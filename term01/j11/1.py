mosalas = []

for _ in range(1, 4):
    a = int(input(f"enter number{_}: "))
    mosalas.append(a)
sums = 0

for _ in range(3):
    if mosalas[_] != 0:
        sums += mosalas[_]
if sums == 180:
    print("YES")
else:
    print("NO")