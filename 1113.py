b = int()
c = int()

while True:
    b, c = input().split()
    b = int(b)
    c = int(c)

    if b > c:
        print("Decrescente")
    elif b < c:
        print("Crescente")
    else:
        exit()
