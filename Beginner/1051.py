n = float(input())
n_comeco = n
T1 = 0
T2 = 0
T3 = 0
if n > 4500:
    T3 = 0.28*(n - 4500)
    n = 4500
if n > 3000:
    T2 = 0.18*(n - 3000)
    n = 3000
if n > 2000:
    T1 = 0.08*(n - 2000)
    n = 2000
if n_comeco <= 2000:
    print("Isento")
else:
    s = "{:.2f}".format(T1 + T2 + T3)
    print(f"R$ {s}")