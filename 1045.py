a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
d = [a, b, c]
d.sort()

if d[2] >= d[1] + d[0]:
    print('NAO FORMA TRIANGULO')
elif (d[2] * d[2]) == (d[1] * d[1]) + (d[0] * d[0]):
    print('TRIANGULO RETANGULO')
elif (d[2] * d[2]) > (d[1] * d[1]) + (d[0] * d[0]):
    print('TRIANGULO OBTUSANGULO')
elif (d[2] * d[2]) < (d[1] * d[1]) + (d[0] * d[0]):
    print('TRIANGULO ACUTANGULO')
if d[2] == d[1] == d[0]:
    print('TRIANGULO EQUILATERO')
elif d[2] == d[1] or d[1] == d[0] or d[2] == d[0]:
    print('TRIANGULO ISOSCELES')
