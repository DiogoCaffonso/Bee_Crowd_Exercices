N = -1
I = -1
for i in range(100):
    x = int(input())
    if N < x:
        N = x
        I = i+1
print(f"{N}\n{I}")