a = float(input())
b = int(a)

c = b / 100
c = int(c)
d = b % 100
e = d / 50
e = int(e)
f = d % 50
g = f / 20
g = int(g)
h = f % 20
i = h / 10
i = int(i)
j = h % 10
k = j / 5
k = int(k)
l = j % 5
m = l / 2
m = int(m)
n = l % 2

o = (a - b) * 100
p = o / 50
p = int(p)
q = o % 50
r = q / 25
r = int(r)
s = q % 25
t = s / 10
t = int(t)
u = s % 10
v = u / 5
v = int(v)
w = u % 5
w = int(w)

print('NOTAS:')
print(c, 'nota(s) de R$ 100.00')
print(e, 'nota(s) de R$ 50.00')
print(g, 'nota(s) de R$ 20.00')
print(i, 'nota(s) de R$ 10.00')
print(k, 'nota(s) de R$ 5.00')
print(m, 'nota(s) de R$ 2.00')
print('MOEDAS:')
print(n, 'moeda(s) de R$ 1.00')
print(p, 'moeda(s) de R$ 0.50')
print(r, 'moeda(s) de R$ 0.25')
print(t, 'moeda(s) de R$ 0.10')
print(v, 'moeda(s) de R$ 0.05')
print(w, 'moeda(s) de R$ 0.01')
