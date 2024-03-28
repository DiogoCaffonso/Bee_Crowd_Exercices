d = float(input())
m1 = 0
m5 = 0
m10 = 0
m25 = 0
m50 = 0
m100 = 0
n2 = 0
n5 = 0
n10 = 0
n20 = 0
n50 = 0
n100 = 0
while d - 100 >= 0:
    n100+=1
    d = d - 100
while d - 50 >= 0:
    n50+=1
    d = d - 50
while d - 20 >= 0:
    n20+=1
    d = d - 20
while d - 10 >= 0:
    n10+=1
    d = d - 10
while d - 5 >= 0:
    n5+=1
    d = d - 5
while d - 2 >= 0:
    n2+=1
    d = d - 2
while d - 1 >= 0:
    m100+=1
    d = d - 1
while d - 0.5 >= 0:
    m50+=1
    d = d - 0.5
while d - 0.25 >= 0:
    m25+=1
    d = d - 0.25
while d - 0.1 >= 0:
    m10+=1
    d = d - 0.1
while d - 0.05 >= 0:
    m5+=1
    d = d - 0.05
d = float("{:.2f}".format(d))
while d - 0.01 >= 0:
    m1+=1
    d = float("{:.2f}".format(d - 0.01))
print("NOTAS:")
print(f"{n100} nota(s) de R$ 100.00")
print(f"{n50} nota(s) de R$ 50.00")
print(f"{n20} nota(s) de R$ 20.00")
print(f"{n10} nota(s) de R$ 10.00")
print(f"{n5} nota(s) de R$ 5.00")
print(f"{n2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{m100} moeda(s) de R$ 1.00")
print(f"{m50} moeda(s) de R$ 0.50")
print(f"{m25} moeda(s) de R$ 0.25")
print(f"{m10} moeda(s) de R$ 0.10")
print(f"{m5} moeda(s) de R$ 0.05")
print(f"{m1} moeda(s) de R$ 0.01")