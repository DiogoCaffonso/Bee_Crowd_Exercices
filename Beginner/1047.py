sh, sm, fh, fm = map(int, input().split())
x = 0
y = 0
if sh == fh and fm == sm:
    x+=24
elif sh == fh and fm != sm:
    if sm < fm:
        y = fm - sm
    else:
        x+=23
        fm+=60
        y = fm - sm
elif sh < fh:
    x = fh - sh
    if sm <= fm:
        y = fm - sm
    elif fm < sm:
        fm+=60
        y = fm - sm
        x-=1
else:
    fh+=24
    x = fh - sh
    if sm <= fm:
        y = fm - sm
    elif fm < sm:
        fm+=60
        y = fm - sm
        x-=1
print(f"O JOGO DUROU {x} HORA(S) E {y} MINUTO(S)")