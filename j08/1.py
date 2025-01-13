dorost = 10

# for _ in range(5, 0, -1):
#     adad = int(input(f"enter a number (you have {_} chances): "))
#     if adad == dorost:
#         print("javab e dorost")
#         break
#     elif adad < dorost:
#         print("bozorgtar entekhab kon")
#     elif adad > dorost:
#         print("koochektar entekhab kon")
# else:
#     print("bakhti")

i = 5
while i:
    adad = int(input(f"enter a number (you have {i} chances): "))
    if adad == dorost:
        print("javab e dorost")
        break
    elif adad < dorost:
        print("bozorgtar entekhab kon")
        i -= 1
    elif adad > dorost:
        print("koochektar entekhab kon")
        i -= 1
else:
    print("bakhti")