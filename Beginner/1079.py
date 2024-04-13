N = int(input())
X = []
Y = []
Z = []
for i in range(N):
    x, y, z = map(float, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)
for i in range(N):
    print(f"{((X[i]*2 + Y[i]*3 + Z[i]*5)/10):.1f}")