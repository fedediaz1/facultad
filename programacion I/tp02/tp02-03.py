"""
-----------------------------------------------------------------------------------------------
Título: TP02-03 - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:

Escribir funciones para:

a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa a través del teclado.

b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no
debe modificar la lista.

c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin
importar el orden.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from random import randint

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def cargarLista():
    lista = []
    n = int(input('ingresar un numero: '))
    for _ in range(n):
        lista.append(randint(1,100))
    return lista

def elementoRepetido(lista):
    for i in range(len(lista)):
        if lista[i] in lista:
            return True
    return False
def eliminarUnNumero(num):
    i = len(listaAleatoria) - 1
    while i >= 0:
        if listaAleatoria[i] == num:
            listaAleatoria.remove(listaAleatoria[i])
        i -= 1
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

listaAleatoria = cargarLista()

print(listaAleatoria)


if elementoRepetido(listaAleatoria):
    print('tiene algun/algunos elemento repetido')
else:
    print('no se repte ninguno')

print(listaAleatoria)