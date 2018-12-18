a = int(input())
d = 0
e = 0
f = 0
g = 0
d = int(d)
e = int(e)
f = int(f)
g = int(g)
x = 0
y = 0
z = 0
x = int(x)
y = int(y)
z = int(z)


for i in range(a):
    b, c = input().split()
    b = int(b)
    c = str(c)

    if c == 'C':
        d += b
    elif c == 'R':
        e += b
    elif c == 'S':
        f += b

g = (d + e + f)
x = (d * 100 / g)
y = (e * 100 / g)
z = (f * 100 / g)

print('Total:', g, 'cobaias')
print("Total de coelhos:", d)
print("Total de ratos:", e)
print("Total de sapos:", f)
print("Percentual de coelhos:", '%.2f' % x, '%')
print("Percentual de ratos:", '%.2f' % y, '%')
print("Percentual de sapos:", '%.2f' % z, '%')