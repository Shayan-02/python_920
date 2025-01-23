lst = []
a = "hello world"
invalid = ["e", "o", "i", "a", "u"]
for _ in a:
    if _ not in invalid:
        lst.append(_)

print(lst)