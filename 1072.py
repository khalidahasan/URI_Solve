a = int(input())
d = 0
e = 0

for i in range(a):
    c = int(input())
    if 10 <= c <= 20:
        d += 1
    else:
        e += 1
print(d, "in")
print(e, "out")