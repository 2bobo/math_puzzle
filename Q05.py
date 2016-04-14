import itertools

c = 0
d = [10, 50, 100, 500]
s = 1000
m = 15

for i in range(2, m + 1):
    r = list(itertools.combinations_with_replacement(d, i))
    for v in r:
        if sum(v) == s:
            print(v)
            c += 1
print(c)
