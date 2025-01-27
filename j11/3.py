mosalas = input().split()
sums = 0
for _ in mosalas:
    if int(_) != 0:
        sums += int(_)
    else:
        break

if sums == 180:
    print("YES")
else:
    print("NO")