correct = 10

num = int(input("enter your choice: "))

if num < correct:
    print("too low")
elif num > correct:
    print("too high")
elif num == correct:
    print("correct")