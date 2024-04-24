import random

def generar_matriz_azar(n):
    # Generar una lista de números únicos dentro del rango [0, N^2)
    numeros_unicos = list(range(n * n))
    random.shuffle(numeros_unicos)

    matriz = [[0] * n for _ in range(n)]
    index = 0

    # Rellenar la matriz con los números únicos
    for i in range(n):
        for j in range(n):
            matriz[i][j] = numeros_unicos[index]
            index += 1

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print("\t".join(map(str, fila)))

# Tamaño de la matriz
n = 4  # Puedes cambiar este valor según tus necesidades

# Generar y mostrar la matriz
matriz = generar_matriz_azar(n)
imprimir_matriz(matriz)
