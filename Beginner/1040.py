N1, N2, N3, N4 = map(float, input().split())
A = "{:.1f}".format((2*N1 + 3*N2 + 4*N3 + N4)/10)
print(f"Media: {A}")
A = float(A)
if A >= 7:
    print("Aluno aprovado.")
elif A < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    E = "{:.1f}".format(float(input()))
    print(f"Nota do exame: {E}")
    E = float(E)
    M = (A+E)/2
    if M >= 5:
        M = "{:.1f}".format(M)
        print(f"Aluno aprovado.\nMedia final: {M}")
    else:
        M = "{:.1f}".format(M)
        print(f"Aluno reprovado.\nMedia final: {M}")