"""
-----------------------------------------------------------------------------------------------
Título: TP02-05 - ELEMENTOS ELIMINADOS

Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:

Eliminar de una lista de números enteros aquellos valores que se encuentren en una segunda lista. Imprimir la lista
original, la lista de valores a eliminar y la lista resultante. La función deben modificar la lista original sin crear una copia
modificada.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def eliminarElementos():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista2 = [2, 3, 6, 7, 11, 13, 14, 13, 15, 16, 17, 18]
    print(lista)
    print(lista2)
    i = 0
    while i < len(lista):
        j = 0
        while j < len(lista2):
            if lista[i] == lista2[j]:
                lista.pop(i)

            j += 1
        i += 1
    print(lista)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------


eliminarElementos()