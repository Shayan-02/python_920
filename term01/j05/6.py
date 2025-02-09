c = 10

for اصغر in range(5):
    num = int(input("enter an number: "))
    if c == num:
        print("برنده شدید")
        break
    else:
        if c < num:
            print("بزرگتر انتخاب کردید")
        else:
            print("کوچکتر انتخاب کردید")
else:
    print("باختی")
