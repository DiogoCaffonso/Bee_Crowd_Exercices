d = int(input())
print(d)
n1 = 0
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
    n1+=1
    d = d - 1
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")