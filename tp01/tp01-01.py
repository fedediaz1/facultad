
"""
-----------------------------------------------------------------------------------------------
Título: TP01-01 - MAYOR ENTRE TRES NÚMEROS
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor
estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje
informativo si éste no existe.

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
def mayorNum (a,b,c):
    mayor = -1
    if a > b:
        if a > c:
            mayor = a
    elif b > a:
        if b > c:
            mayor = b
    elif c > a:
        if c > b:
            mayor = c
    return mayor
    

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

a = int(input('ingresar el primer numero: '))
b = int(input('ingresar el segundo numero: '))
c = int(input('ingresar el tercer numero: '))


resultado = mayorNum(a,b,c)

if resultado != -1:
    print('el mayor numero es:',resultado)
else:
    print('no hay mayor estricto')