a, b, c = 10, 20, 30

# green = fruits[0]
# yellow = fruits[1]
# red = fruits[2]

fruits = ("apple", "banana", "cherry", "orange", "kiwi")
green, *yellow, red = fruits
print(green, yellow, red)