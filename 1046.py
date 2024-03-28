st, et = map(int, input().split())
x = 0
if st == et:
    x+=24
elif st < et:
    x = et - st
else:
    et+=24
    x = et - st
print(f"O JOGO DUROU {x} HORA(S)")