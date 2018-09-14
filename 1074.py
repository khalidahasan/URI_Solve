a = int(input())
i = 1

while i <= a:
    i = i + 1
    b = input()
    b = int(b)
    if b == 0:
        print("NULL")
    elif b % 2 == 0:
        if b < 0:
            print("EVEN NEGATIVE")
        else:
            print("EVEN POSITIVE")
    elif b % 2 == 1:
        if b < 0:
            print("ODD NEGATIVE")
        else:
            print("ODD POSITIVE")