n = 22

n1 = n % 10
n2 = n // 10

n3 = str(n1) + str(n2)

if int(n) == int(n3):
    print("مغلوب")
else:
    print("غیر مغلوب")
