a, b = input().split()
a = int(a)
b = int(b)
if a == 1:
    c = 4.00 * b
elif a == 2:
    c = 4.50 * b
elif a == 3:
    c = 5.00 * b
elif a == 4:
    c = 2.00 * b
elif a == 5:
    c = 1.50 * b
else:
    c = 0 * b
print('Total: R$', '%.2f' % c)
