num = int(input("enter a number: "))

if num % 15 == 0:
    print("fizbuz")
elif num % 5 == 0:
    print("buz")
elif num % 3 == 0:
    print("fiz")
else:
    print(num)