def cutter(n, m, r):
    a = 0
    t = []
    for nn in n:
        if a != m and nn != 1:
            t.append(int(nn / 2))
            t.append(int(nn / 2) + int(nn % 2))
            a += 1
        elif a == m and nn != 1:
            t.append(nn)
        else:
            t.append(nn)
        t.sort(reverse=True)
    if max(t) != 1:
        r = cutter(t, m, r)

    return r + 1


r = 0

n = 8
m = 3
print("n=8,m=3")
print(cutter([n], m, r))

n = 20
m = 3
print("n=20,m=3")
print(cutter([n], m, r))

n = 100
m = 5
print("n=100,m=5")
print(cutter([n], m, r))
