jam = 0
tedad = 0
while True:
    nomreh = int(input("enter a number: "))
    if nomreh == 0:
        break
    else:
        if 0 <= nomreh <= 20:
            tedad += 1
            jam += nomreh
        else:
            print("ورودی نامعتبر")

avg = jam / tedad

if avg >= 10:
    if avg >= 18:
        print("عالی", avg)
    elif avg >= 16:
        print("خوب", avg)
    elif avg >= 14:
        print("متوسط", avg)
    else:
        print("لب مرز", avg)
else:
    print("افتاده", avg)