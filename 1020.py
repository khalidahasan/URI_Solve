a = int(input())

b = a / 365
b = int(b)
c = a % 365
c = int(c)
d = c / 30
d = int(d)
e = c % 30

print(b, 'ano(s)')
print(d, 'mes(es)')
print(e, 'dia(s)')
