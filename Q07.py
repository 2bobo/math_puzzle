from datetime import *

dt = datetime(1964, 10, 10)
a = 0
while dt != datetime(2020, 7, 20):
    idt = int(dt.strftime("%Y%m%d"))
    ldt = list(bin(idt))
    del ldt[:2]
    ldt.reverse()
    rdt = "".join(ldt)
    rdt = int(rdt, 2)
    if idt == rdt:
        print(dt.strftime("%Y/%m/%d"))
        print(str(idt) + ":" + str(rdt))
        a += 1
    dt = dt + timedelta(days=1)

print(a)
