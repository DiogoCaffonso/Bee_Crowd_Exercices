x = int(input())
y = int(input())
s = 0
if x > y:
    m = y
    M = x
else:
    M = y
    m = x
m+=1
while m < M:
    if m%2 != 0:
        s+=m
    m+=1
print(s)