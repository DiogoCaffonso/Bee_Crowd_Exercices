A, B, C = map(float,input().split())
pi = 3.14159
Tri = "{:.3f}".format(A*C/2)
Cir = "{:.3f}".format(pi*pow(C, 2))
Tra = "{:.3f}".format((A+B)*C/2)
Qua = "{:.3f}".format(pow(B, 2))
Ret = "{:.3f}".format(A*B)
print(f"TRIANGULO: {Tri}\nCIRCULO: {Cir}\nTRAPEZIO: {Tra}\nQUADRADO: {Qua}\nRETANGULO: {Ret}")