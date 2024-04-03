a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
x = [a, b, c, d, e]
j = 0
for i in x:
    if abs(i%2) == 0:
        j+=1
print(f"{j} valores pares")