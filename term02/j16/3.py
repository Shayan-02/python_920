def mosalas(lst):
    for _ in lst:
        if _ == 0:
            return "No"
    else:
        if sum(lst) == 180:
            return "Yes"
        else:
            return "No"


a = [int(i) for i in input().split()]
print(mosalas(a))