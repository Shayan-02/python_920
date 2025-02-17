def ali(lst):
    for _ in lst[::-1]:
        print(_)


lst = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        lst.append(a)

ali(lst)
