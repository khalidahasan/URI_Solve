a, b = input().split()

a = float(a)
b = float(b)

if a > 0 and b > 0:
    print('Q1')
elif a < 0 < b:
    print('Q2')
elif a < 0 and b < 0:
    print('Q3')
elif a > 0 and b < 0:
    print('Q4')
elif a == 0 and b != 0:
    print('Eixo Y')
elif b == 0 and a != 0:
    print('Eixo X')
else:
    print('Origem')
