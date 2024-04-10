"""
-----------------------------------------------------------------------------------------------
Título: TP02-03 - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento
imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar
de dos dígitos.

b. Calcular y devolver el producto de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la
función lo recibe como parámetro. No utilizar listas auxiliares.

d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa
es [50, 17, 91, 17, 50].

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
def cargarListaConNumerosAlAzar():
    lista = []
    cantidadDeNumeros = random.randint(10,99)
    for _ in range(cantidadDeNumeros):
        lista.append(random.randint(1000,9999))
    return lista

def productoDeElementosEnListas(lista):
    total = 1
    for i in range(len(lista)):
        total *= lista[i]
    return total

def eliminarUnNumero(num):
    i = len(listaAleatoria) - 1
    while i >= 0:
        if listaAleatoria[i] == num:
            listaAleatoria.remove(listaAleatoria[i])
        i -= 1

def esCapicua(lista):
    lista2 = lista[::-1]
    if lista2 == lista:
        return True
        
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

#cargar la lista de numeros aleatorios y luego calcular el producto de sus elementos
listaAleatoria = cargarListaConNumerosAlAzar()
total = productoDeElementosEnListas(listaAleatoria)

#mostrar la lista y mostrar el total del producto de sus elementos
print(listaAleatoria)
print(total)


#pedirle al usuario que ingrese un numero para eliminar de la lista
numeroAEliminar = int(input('ingresar un numero para eliminar de la lista: '))
eliminarUnNumero(numeroAEliminar) #llamar a la funcion


#mostrar la lista
print(listaAleatoria)


#definir si es capicua
if esCapicua(listaAleatoria):
    print('la lista es capicua')
else:
    print('no es capicua')