start = int(input("enter start: "))
end = int(input("enter end: "))

for yechizi in range(start, end+1):
    if yechizi % 5 == 0:
        print(yechizi, end=" ")