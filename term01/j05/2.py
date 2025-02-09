riazi = int(input("Enter a number: "))
phisic = int(input("Enter a number: "))

miangin = (riazi + phisic) / 2

if 0 <= riazi <= 20: # if 0 <= riazi <= 20 and 0 <= phisic <= 20:
    if 0 <= phisic <= 20:
        if miangin >= 10:
            if miangin >= 18:
                print("عالی")
            elif miangin >= 16:
                print("خوب")
            elif miangin >= 14:
                print("متوسط")
        else:
            print("افتاده")
else:
    print("ورودی نامعتبر")