i = 2
while i <= 200:
    if i == 100:
        i += 2
        continue
    elif i == 150:
        break
    else:
        print(i, end="\t")
        i += 2