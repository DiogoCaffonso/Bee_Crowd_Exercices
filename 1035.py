A, B, C, D = map(int, input().split())
e = False
if A%2 == 0:
    e = True
if B > C and D > A and C+D>A+B and C>0 and D>0 and e:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")