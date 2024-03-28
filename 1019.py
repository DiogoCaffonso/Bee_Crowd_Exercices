h = 0
m = 0
s = int(input())
while s >= 60:
    m+=1
    s-=60
while m >= 60:
    h+=1
    m-=60
print(f"{h}:{m}:{s}")