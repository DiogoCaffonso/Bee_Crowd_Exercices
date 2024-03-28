a = 0
m = 0
d = int(input())
while d >= 365:
    a+=1
    d-=365
while d >= 30:
    m+=1
    d-=30
print(f"{a} ano(s)\n{m} mes(es)\n{d} dia(s)")