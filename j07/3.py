sums, l = 0, 0
while True:
    num = int(input("enter a number: "))
    if num == 0:
        break
    if 0 <= num <= 20: 
        sums += num
        l += 1
print(f"average: {sums/l}")