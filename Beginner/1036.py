a, b, c = map(float, input().split())
Δ = b**2 - 4*a*c
if Δ < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = "{:.5f}".format((-b + pow(Δ, 0.5))/(2*a))
    x2 = "{:.5f}".format((-b - pow(Δ, 0.5))/(2*a))
    print(f"R1 = {x1}")
    print(f"R2 = {x2}")