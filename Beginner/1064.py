a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = [a, b, c, d, e, f]
y = []
for i in x:
    if i > 0:
        y.append(i)
print(f"{len(y)} valores positivos\n{(sum(y)/len(y)):.1f}")