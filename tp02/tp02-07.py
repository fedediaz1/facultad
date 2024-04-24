"""
-----------------------------------------------------------------------------------------------
Título: TP02-06 -  VERIFICAR ORDEN DE ELEMENTOS

Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:

Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente
o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def verificar(lista):
    return lista == sorted(lista)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

lista = [1,2,3,4,5,6]

resultado = verificar(lista)

print(resultado)
