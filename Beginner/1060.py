a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = [a, b, c, d, e, f]
j = 0
for i in x:
    if i > 0:
        j+=1
print(f"{j} valores positivos")