n1 = int(input("enter a number: "))
op = input("enter operator: ")
n2 = int(input("enter another number: "))
result = 0
if op == "+":
    result = n1 + n2
    print(result)
elif op == "-":
    result = n1 - n2
    print(result)
elif op == "*":
    result = n1 * n2
    print(result)
elif op == "/":
    if n2 == 0:
        print("error")
    else:
        result = n1 / n2
        print(result)
while True:
    answer = input("do you want to continue? (y/n): ")
    if answer == "n":
        break
    else:
        op = input("enter operator: ")
        n3 = int(input("enter another number: "))
        if op == "+":
            result = result + n3
            print(result)
        elif op == "-":
            result = result - n3
            print(result)
        elif op == "*":
            result = result * n3
            print(result)
        elif op == "/":
            if n3 == 0:
                print("error")
                continue
            else:
                result = result / n3
                print(result)
                continue