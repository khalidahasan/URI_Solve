a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
s = a + b + c
s = int(s)

if 0 <= s < 24:
    print(s)
elif s >= 24:
    print(s - 24)
elif s < 0:
    print(24 + s)