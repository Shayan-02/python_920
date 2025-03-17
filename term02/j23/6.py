from functools import reduce

a = [5, 8, 10, 20, 50, 100]

total = reduce((lambda x, y: x*y), a)
print(total)
