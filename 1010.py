c1, n1, p1 = map(float,input().split())
c2, n2, p2 = map(float,input().split())
X = "{:.2f}".format(n1*p1 + n2*p2)
print(f"VALOR A PAGAR: R$ {X}")