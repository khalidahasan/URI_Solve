a = int(input())
i = 1

while i <= a:
    i = i + 1
    b, c = input().split()
    b = int(b)
    c = int(c)
    if c == 0:
        print("divisao impossivel")
    else:
        print(b/c)