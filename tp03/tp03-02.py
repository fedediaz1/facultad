"""
-----------------------------------------------------------------------------------------------
Título: TP - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:


Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def matriz_A():
    fil = 4
    col = 4
    relleno = 0
    matriz = []
    for f in range(fil):
        matriz.append([relleno] * col)

    val = 1
    for i in range(len(matriz)):
        matriz[i][i] += val
        val += 2
    return matriz

def matriz_B():
    fil = 4
    col = 4
    relleno = 0
    matriz = []
    for f in range(fil):
        matriz.append([relleno] * col)

    val = 1
    fila = fil - 1  # Comenzamos desde la última fila
    for i in range(col):
        matriz[fila][i] += val
        val *= 3
        fila -= 1  # Movemos hacia arriba en la siguiente iteración
        if fila < 0:
            break  # Salir si alcanzamos la primera fila
    return matriz

def matriz_C():
    matriz = []
    for i in range(4):
        fila = []
        for j in range(4):
            fila.append(max(0, min(i + 1, 4 - j)))
        matriz.append(fila)
    return matriz

def matriz_D():
    matriz = []
    valor = 8
    for i in range(n):
        fila = [valor] * n
        matriz.append(fila)
        valor //= 2
    return matriz

def matriz_E(n):
    matriz = []
    valor = 1
    for i in range(n):
        fila = []
        for j in range(n):
            if (i + j) % 2 == 0:
                fila.append(0)
            else:
                fila.append(valor)
                valor += 1
        matriz.append(fila)
    return matriz

def matriz_F(n):
    matriz = []
    valor = 0
    for i in range(n):
        fila = []
        for j in range(n):
            if i >= j:
                fila.append(valor)
                valor += 1
            else:
                fila.append(n * n - valor)
                valor += 1
        matriz.append(fila)
    return matriz

def matriz_G(n):
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    inicio_fila = 0
    fin_fila = n - 1
    inicio_columna = 0
    fin_columna = n - 1

    while inicio_fila <= fin_fila and inicio_columna <= fin_columna:
        # Llenar la fila superior
        for j in range(inicio_columna, fin_columna + 1):
            matriz[inicio_fila][j] = valor
            valor += 1
        inicio_fila += 1

        # Llenar la columna derecha
        for i in range(inicio_fila, fin_fila + 1):
            matriz[i][fin_columna] = valor
            valor += 1
        fin_columna -= 1

        # Llenar la fila inferior
        if inicio_fila <= fin_fila:
            for j in range(fin_columna, inicio_columna - 1, -1):
                matriz[fin_fila][j] = valor
                valor += 1
            fin_fila -= 1

        # Llenar la columna izquierda
        if inicio_columna <= fin_columna:
            for i in range(fin_fila, inicio_fila - 1, -1):
                matriz[i][inicio_columna] = valor
                valor += 1
            inicio_columna += 1

    return matriz

def matriz_H(matriz):
    matriz = [[0 for _ in range(4)] for _ in range(4)]

    matriz[0][0] = 1
    limite = 2
    sumador = 2
    x = 0

    while True:
        fila = 0
        columna = limite
        while fila < limite - 1:

            while columna > 0:

                matriz[fila][columna - 1] = sumador
                sumador += 1
                columna -= 1
                fila += 1
            columna += 1

        limite += 1

        if matriz[0][len(matriz[0]) - 1] != 0:

            while True:
                fila2 = x + 1

                for columna in range(len(matriz[0]) - 1, x, -1):
                    matriz[fila2][columna] = sumador
                    sumador += 1
                    fila2 += 1

                x += 1

                if matriz[len(matriz) - 1][len(matriz[0]) - 1] != 0:
                    break
            break

    return matriz

def matriz_I(n):
    matriz = [[0] * n for _ in range(n)]

    valor = 1
    i = 0
    j = 0
    direccion = 1

    while valor <= n * n:
        matriz[i][j] = valor
        valor += 1

        if direccion == 1:
            if i == 0 or j == n - 1:
                direccion = -1
                if j == n - 1:
                    i += 1
                else:
                    j += 1
            elif matriz[i - 1][j + 1] == 0:
                i -= 1
                j += 1
            else:
                direccion = -1
                i += 1
        else:
            if i == n - 1 or j == 0:
                direccion = 1
                if i == n - 1:
                    j += 1
                else:
                    i += 1
            elif matriz[i + 1][j - 1] == 0:
                i += 1
                j -= 1
            else:
                direccion = 1
                j += 1

    return matriz

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

n = 4
matrizA = matriz_A()
matrizB = matriz_B()
matrizC = matriz_C()
matrizD = matriz_D()
matrizE = matriz_E(n)
matrizF = matriz_F(n)
matrizG = matriz_G(n)
matrizH = matriz_H(n)
matrizI = matriz_I(n)


for fila in matrizA: print(fila)
print()
for fila in matrizB: print(fila)
print()
for fila in matrizC: print(fila)
print()
for fila in matrizD: print(fila)
print()
for fila in matrizE: print(fila)
print()
for fila in matrizF: print(fila)
print()
for fila in matrizG: print(fila)
print()
for fila in matrizH: print(fila)
print()
for fila in matrizI: print(fila)