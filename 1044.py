a, b = input().split()
a = int(a)
b = int(b)
if b > a:
    c = (b % a)
    if c == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif a > b:
    c = (a % b)
    if c == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
