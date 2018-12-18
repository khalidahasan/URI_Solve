while True:
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

    f = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        f = int(input())
        if f == 1 or f == 2:
            break
    if f == 2:
        break
