A, B, C = map(float, input().split())
if A+B==C or A+C==B or B+C==A:
    area = (A+B)*C/2
    print(f"Area = {area}")
else:
    per = A+B+C
    print(f"Perimetro = {per}")