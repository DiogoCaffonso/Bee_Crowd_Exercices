Prod = [[1, 4], [2, 4.5], [3, 5], [4, 2], [5, 1.5]]
qual, quanto = map(int, input().split())
T = "{:.2f}".format(Prod[qual-1][1]*quanto)
print(f"Total: R$ {T}")