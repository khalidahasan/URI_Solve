a = []
for i in range(6):
    n = float(input())
    a.append(float(n))

l = 0
for j in range(6):
    if a[j] > 0:
        l += 1
print(l, "valores positivos")
