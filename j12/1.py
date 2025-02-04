lst = [1, "ali", "rezaee", 25, True]
lst[1] = "reza"

t1 = (1, "ali", 3)

l1 = list(t1)
l1[1] = "reza"
t1 = tuple(l1)

print(t1)