def test1():
    print("hello world 1")


def test2():
    a = 10
    return "hello world 2"

a = test1()
print(test2())
b = test2() * 2
print(b)

def test3(a, b):
    return a + b

print(test3(1, 2)*2)

def test4(a, b):
    print(a + b)

test4(1, 2)