x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())
Xsq = (x2 - x1)**2
Ysq = (y2 - y1)**2
D = "{:.4f}".format(pow(Xsq + Ysq, 0.5))
print(D)