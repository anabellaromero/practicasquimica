
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


sumadiagonal = 0
for i in range(3):
    sumadiagonal += matriz[i][i]


print("Matriz:")
for fila in matriz:
    print(fila)

print("Suma de la diagonal:", sumadiagonal)
