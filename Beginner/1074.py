n = int(input())
N = []
a = []
b = []
c = []
for i in range(n):
    nn = int(input())
    N.append(nn)
for i in N:
    if i%2 == 0:
        a.append("EVEN")
    else:
        a.append("ODD")
    if i > 0:
        b.append("POSITIVE")
        c.append(False)
    elif i < 0:
        b.append("NEGATIVE")
        c.append(False)
    else:
        b.append("NULL")
        c.append(True)
for i in N:
    if not c[N.index(i)]:
        print(f"{a[N.index(i)]} {b[N.index(i)]}")
    if c[N.index(i)]:
        print(b[N.index(i)])