f = input()
s = input()
t = input()
fst = [["vertebrado"], ["ave", "mamifero"], ["carnivoro", "onivoro", "onivoro", "herbivoro"], ["aguia", "pomba", "homem", "vaca"]]
scd = [["invertebrado"], ["inseto", "anelideo"], ["hematofago", "herbivoro", "hematofago", "onivoro"], ["pulga", "lagarta", "sanguessuga", "minhoca"]]
conjunto = [fst, scd]
if f == conjunto[0][0][0]:
    i = 0
    if s == conjunto[0][1][0]:
        if t == conjunto[0][2][0]:
            k = 0
        else:
            k = 1
    else:
        if t == conjunto[0][2][2]:
            k = 2
        else:
            k = 3
else:
    i = 1
    if s == conjunto[1][1][0]:
        if t == conjunto[1][2][0]:
            k = 0
        else:
            k = 1
    else:
        if t == conjunto[1][2][2]:
            k = 2
        else:
            k = 3
print(conjunto[i][3][k])