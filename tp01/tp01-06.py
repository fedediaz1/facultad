"""
-----------------------------------------------------------------------------------------------
Título: TP01-06 -  CONCATENAR BÁSICO

Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva el número que resulte de
concatenar ambos valores. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades
de Python no vistas en clase, ni tampoco concatenar strings mediante la conversión de número a cadena.
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
def concatenar(num1, num2):
    lista = []
    lista.append(num1)
    lista.append(num2)
    return lista


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

num1 = int(input('ingresar un numero: '))
num2 = int(input('ingresar otro numero: '))

resultado = concatenar(num1,num2)

for i in range(len(concatenar(num1,num2))):
    print (concatenar(num1,num2)[i],end="")