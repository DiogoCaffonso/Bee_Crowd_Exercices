n = int(input())
t = True
DDD = [61, 71, 11, 21, 32, 19, 27, 31]
Destination = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
for i in range(len(DDD)):
    if n == DDD[i]:
        print(Destination[i])
        t = False
if t:
    print("DDD nao cadastrado")