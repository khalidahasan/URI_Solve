a = int(input())

b = a / 60
c = a % 60
b = int(b)
d = b / 60
d = int(d)
e = b % 60

print('%d:%d:%d' % (d, e, c))
