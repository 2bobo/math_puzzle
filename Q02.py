import re

ope = ["+", "-", "*", ""]

for n in range(1000, 10000):
    n_list = list(str(n))
    for a in ope:
        for b in ope:
            for c in ope:
                if a or b or c:
                    t = re.split('([\+\-\*\/])', "".join([n_list[0], a, n_list[1], b, n_list[2], c, n_list[3]]))
                    d = ""
                    for v in t:
                        if v.isdigit():
                            d += str(int(v))
                        else:
                            d += v
                    r_list = list(str(eval(d)))
                    if r_list == n_list[::-1]:
                        print(d)
                        print("".join(n_list) + "=" + "".join(r_list))
                        print("---")
