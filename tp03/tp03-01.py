"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def cargaMatriz(fil, col):
    matriz = []
    for f in range(fil):
        fila = []
        for c in range(col):
            relleno = random.randint(0, 99)
            fila.append(relleno)
        matriz.append(fila)
    return matriz

def ordenarMatriz(_matriz):
    _matriz = [sorted(fila) for fila in _matriz]
    return _matriz

def intercambiarFilas(_matriz, fila1, fila2):
    _matriz[fila1], _matriz[fila2] = _matriz[fila2], _matriz[fila1]
    return _matriz

def intercambiarCol(_matriz, col1, col2):
    _matriz[col1], _matriz[col2] = _matriz[col2], _matriz[col1]
    return _matriz

def trasponer_matriz(matriz):
    n = len(matriz)  # Obtenemos el tamaño de la matriz (suponemos que es cuadrada)
    for i in range(n):
        for j in range(i+1, n):  # Iteramos solo sobre la mitad superior de la matriz
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]  # Intercambiamos los elementos
    return matriz

def calcularPromedio(_matriz, fil):
    suma = sum(_matriz[fil])
    promedio = suma / len(_matriz[fil])
    return promedio    

def porcentaje_impares(matriz, columna):
    # Verificar que la matriz sea cuadrada
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            raise ValueError("La matriz no es cuadrada")

    # Verificar que la columna sea válida
    if columna < 0 or columna >= n:
        raise ValueError("La columna especificada está fuera de rango")

    # Contar elementos impares en la columna
    impares = 0
    for fila in matriz:
        if fila[columna] % 2 != 0:
            impares += 1

    # Calcular porcentaje de elementos impares
    porcentaje = (impares / n) * 100
    return porcentaje


def es_simetrica(matriz):
    # Verificar que la matriz sea cuadrada
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False

    # Verificar si la matriz es igual a su traspuesta
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def es_simetrica_diagonal_secundaria(matriz):
    # Verificar que la matriz sea cuadrada
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False

    # Verificar si la matriz es igual a su traspuesta reflejada horizontalmente
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - 1 - j][n - 1 - i]:
                return False
    return True
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#----------------------------------------------------------------------------------------------


#-------------------------------------------------
# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] cargar matriz")
        print("[2] ordenar matriz")
        print("[3] intercambiar dos filas")
        print("[4] intercambiar dos columnas")
        print("[5] trasponer matriz")
        print("[6] calcular promedio de fila")
        print("[7] porcentaje de elm impares de una columna")
        print("[8] simetria con diagonal principal")
        print("[9] simetria con diagonal secundaria")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3","4",'5','6','7','8','9'): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == "0": # Opción salir del programa
        exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    elif opcion == "1":   # Opción 1
        filasUsuario = int(input('ingresar la cantidad de filas: '))
        columnasUsuario = int(input('ingresar la cantidad de columnas: '))
        matrizResultante = cargaMatriz(filasUsuario,columnasUsuario)
        for fila in matrizResultante: print(fila)

    elif opcion == "2":   # Opción 2
        matrizOrdenada = ordenarMatriz(matrizResultante[::])
        print('matriz original:')
        for fila in matrizResultante: print(fila)
        print('matriz resultante:')
        for fila in matrizOrdenada:print(fila)

    elif opcion == "3":   # Opción 3
        filaIntercambiar1 = int(input('ingresar la primera fila a intercambiar: '))
        filaIntercambiar2 = int(input('ingresar la segunda fila a intercambiar: '))
        filasIntercambiadas = intercambiarFilas(matrizResultante[::], filaIntercambiar1,filaIntercambiar2)
        print('matriz original:')
        for fila in matrizResultante: print(fila)
        print('matriz resultante:')

        for fila in filasIntercambiadas: print(fila)

    elif opcion == "4":   # Opción 4
        colIntercambiar1 = int(input('ingresar la primera columna a intercambiar: '))
        colIntercambiar2 = int(input('ingresar la segunda columna a intercambiar: '))
        columnasIntercambiadas = intercambiarCol(matrizResultante[::], colIntercambiar1, colIntercambiar2)
        print('matriz original:')
        for fila in matrizResultante: print(fila)
        print('matriz resultante:')
        for fila in columnasIntercambiadas: print(fila)
    elif opcion == "5":   # Opción 5
        trasponerMatriz = trasponer_matriz(matrizResultante[::])
        print('matriz original:')
        for fila in matrizResultante: print(fila)
        print('matriz resultante:')
        for fila in trasponerMatriz: print(fila)
    elif opcion == "6":   # Opción 6
        filaDelPromedio = int(input('ingresar la fila: '))
        promedio = calcularPromedio(matrizResultante,filaDelPromedio)
        for fila in matrizResultante: print(fila)
        print('matriz resultante:')
        print(promedio)
    elif opcion == "7":   # Opción 7
        columna = int(input('ingresar una columna '))
        porcentaje = porcentaje_impares(matrizResultante[::],columna)
        print('el porcentaje de valores impares en la columna',columna,'es de:',porcentaje)
    elif opcion == "8":   # Opción 8
        if es_simetrica(matrizResultante[::]):
            print('la matriz es simetrica.')
        else:
            print('no es simetrica.')
    elif opcion == "9":   # Opción 9
        if es_simetrica_diagonal_secundaria(matrizResultante[::]):
            print('la matriz es simetrica.')
        else:
            print('no es simetrica.')     

    print()
    input("Presione ENTER para volver al menú.")