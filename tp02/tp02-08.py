"""
-----------------------------------------------------------------------------------------------
Título: TP02-07 -  LISTA NORMALIZADA
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:

Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir que todos sus
elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar
también un programa que permita verificar el comportamiento de la función. Por ejemplo, normalizar([1, 1, 2]) debe
devolver [0.25, 0.25, 0.50].

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def normalizarLista(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista[i]/sum(lista))
    return lista2


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

lista = [1,1,3,5,7,3]

result = normalizarLista(lista)

print(result)