s = float(input())
r = 0
ns = 0
if s >= 0 and s <= 400:
    r = 0.15*s
    ns = "{:.2f}".format(s + r)
    r = "{:.2f}".format(r)
    s = "{:.2f}".format(s)
    print(f"Novo salario: {ns}\nReajuste ganho: {r}\nEm percentual: 15 %")
elif s > 400 and s <= 800:
    r = 0.12*s
    ns = "{:.2f}".format(s + r)
    r = "{:.2f}".format(r)
    s = "{:.2f}".format(s)
    print(f"Novo salario: {ns}\nReajuste ganho: {r}\nEm percentual: 12 %")
elif s > 800 and s <= 1200:
    r = 0.1*s
    ns = "{:.2f}".format(s + r)
    r = "{:.2f}".format(r)
    s = "{:.2f}".format(s)
    print(f"Novo salario: {ns}\nReajuste ganho: {r}\nEm percentual: 10 %")
elif s > 1200 and s <= 2000:
    r = 0.07*s
    ns = "{:.2f}".format(s + r)
    r = "{:.2f}".format(r)
    s = "{:.2f}".format(s)
    print(f"Novo salario: {ns}\nReajuste ganho: {r}\nEm percentual: 7 %")
else:
    r = 0.04*s
    ns = "{:.2f}".format(s + r)
    r = "{:.2f}".format(r)
    s = "{:.2f}".format(s)
    print(f"Novo salario: {ns}\nReajuste ganho: {r}\nEm percentual: 4 %")