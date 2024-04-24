"""
-----------------------------------------------------------------------------------------------
Título: TP02-04 -  ELEMENTOS AL CUADRADO

Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado.
Luego se solicita imprimir los últimos 10 valores de la lista

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def calcularCuadrados():
    n = int(input('ingresar un numero: '))
    lista = []
    for i in range(1, n+1):
        lista.append(i**2)
    
    if len(lista) >= 10:
        print(lista[-1], lista[-2], lista[-3], lista[-4], lista[-5], lista[-6], lista[-7], lista[-8], lista[-9], lista[-10])
    else:
        print(lista[::-1])


    return lista

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

calcularCuadrados()