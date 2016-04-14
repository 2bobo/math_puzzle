n = 101
c = n * [True]
i = 2

for a in range(2, n):
    for i in range(a - 1, n, a):
        c[i] = not (c[i])

c.pop(-1)

# 答え合わせ
for b in range(len(c)):
    if c[b]:
        print(b + 1)
