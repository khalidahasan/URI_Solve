a = int(input())

for i in range(a):
    b, c, d = input().split()
    b = float(b)
    c = float(c)
    d = float(d)
    e = (((b * 2) + (c * 3) + (d * 5)) / 10)
    print('%.1f' % e)