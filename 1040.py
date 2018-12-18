a, b, c, d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

e = (a * 2 + b * 3 + c * 4 + d) / 10
print('Media:', '%.1f' % e)

if e >= 7.0:
    print('Aluno aprovado.')
elif 6.9 >= e >= 5.0:
    print('Aluno em exame.')
    m = float(input())
    print('Nota do exame:', '%.1f' % m)
    if (m + e / 2) >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final:', '%.1f' % ((e + m) / 2))
else:
    print('Aluno reprovado.')
