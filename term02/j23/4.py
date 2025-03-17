lst2 = ["1", "2", "3"]
lst3 = []
for _ in lst2:
    lst3.append(int(_))
print(lst3)


lst = ["1", "2", "3"]
print(list(map(int, lst)))
