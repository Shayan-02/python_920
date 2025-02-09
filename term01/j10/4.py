a = [1, 2, 2, 4, "ali", "reza", 5, True, 8]

print(a)
a.pop()
print(a)
a.pop(5)
print(a)
a.remove(5)
print(a)
print()
b = a.copy()
print(a, b, sep="\n")