vazn = int(input("vazn e khod ra vared konid: "))
ghad = float(input("ghad e khod ra vared konid: "))

bmi = vazn / (ghad * ghad)

if bmi < 18:
    print("boro ghaza bokhor chag shi")
elif 18 <= bmi and bmi <= 25:
    print("hamin okeye")
else:
    print("enghad ghaza nakhor chag shodi")
