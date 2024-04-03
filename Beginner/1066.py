a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
x = [a, b, c, d, e]
even = 0
odd = 0
pos = 0
neg = 0
for i in x:
    if i%2 == 0:
        even+=1
    else:
        odd+=1
    if i > 0:
        pos+=1
    elif i < 0:
        neg +=1
print(f"{even} valor(es) par(es)\n{odd} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)")