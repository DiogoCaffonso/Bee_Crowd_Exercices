n = int(input())
x = []
d = 0
f = 0
while n != 0:
    x.append(int(input()))
    n-=1
for i in x:
    if i >= 10 and i <= 20:
        d+=1
    else:
        f+=1
print(f"{d} in\n{f} out")