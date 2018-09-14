A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

tri = .5 * A * C
cir = 3.14159 * C * C
trap = (A + B) / 2 * C
squ = B * B
rec = A * B
print('TRIANGULO: %.3f' % tri)
print('CIRCULO: %.3f' % cir)
print('TRAPEZIO: %.3f' % trap)
print('QUADRADO: %.3f' % squ)
print('RETANGULO: %.3f' % rec)
