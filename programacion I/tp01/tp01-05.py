"""
-----------------------------------------------------------------------------------------------
Título: TP01-05 - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Escribir dos funciones separadas que reciban un número natural y devuelvan verdadero o falso según el número sea de
alguna de las siguientes categorías:
Función oblongo(): Informa si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener
multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.
Función triangular(): Informa si un número es triangular. Un número se define como triangular si puede expresarse
como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número
triangular porque se obtiene sumando 1+2+3+4.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def oblongo(a):
    for i in range(a):
        if i * (i+1) == a:
            return True

def triangular(b):
    suma = 0
    for i in range(b):
        suma += i
        if suma == b:
            return True




#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

a = int(input('ingresar un numero: '))

if oblongo(a) == True:
    print('el numero',a,'es oblongo')
else:
    print('el numero',a,'no es oblongo')

b = int(input('ingresar otro numero: '))

if triangular(b) == True:
    print('el numero',b,'es triangular')
else:
    print('el numero',b,'no es triangular')