n = int(input("enter number1: "))
m = int(input("enter number2: "))
op = input("enter operator(+, -, *, /): ")

if op == "+":
    print(n + m)
elif op == "-":
    print(n - m)
elif op == "*":
    print(n * m)
elif op == "/":
    if m == 0:
        print("error")
    else:
        print(n / m)