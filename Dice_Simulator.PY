import random

print("Welcome to Dice Simulator")
a = "b"
while a == "b":
    r = random.randint(1,6)
    if r == 1:
        print(["....."])
        print(["     "])
        print(["  o  "])
        print(["     "])
        print(["....."])

    if r == 2:
        print(["....."])
        print(["  o  "])
        print(["     "])
        print(["  o  "])
        print(["....."])

    if r == 3:
        print(["....."])
        print(["     "])
        print([" o o "])
        print(["  o  "])
        print(["....."])

    if r == 4:
        print(["....."])
        print([" o o "])
        print(["     "])
        print([" o o "])
        print(["....."])

    if r == 5:
        print(["....."])
        print([" o o "])
        print(["  o  "])
        print([" o o "])
        print(["....."])

    if r == 6:
        print(["....."])
        print([" o o "])
        print([" o o "])
        print([" o o "])
        print(["....."])

    a = input("Press b to roll again : ")    


