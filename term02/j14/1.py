lst = []
while True:
    n = int(input())
    if n == 0:
        break
    lst.append(n)

for _ in lst[::-1]:
    print(_)