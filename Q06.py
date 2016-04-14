def collatz(n, f):
    if f == 1 or (n % 2) != 0:
        f = 0
        a = int((n * 3) + 1)
    elif (n % 2) == 0:
        a = int(n / 2)

    # print(a)
    if a == i:
        return 1
    elif a == 1:
        return 0
    else:
        t = collatz(a, f)
    return t


c = 0
for i in range(2, 10001, 2):
    r = collatz(i, 1)
    if r == 1:
        c += 1
print(c)
