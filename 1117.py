c = 0
d = 0
while True:
    b = float(input())
    if 0.0 <= b <= 10.0:
        c += b
        d += 1
        if d == 2:
            break
    else:
        print("nota invalida")

e = c / 2
print("media =", "%.2f" % e)
