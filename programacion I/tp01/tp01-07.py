"""
-----------------------------------------------------------------------------------------------
Título: TP01-07 - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Escribir una función diaSiguiente() que reciba como parámetro una fecha cualquiera expresada por tres enteros
(correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes el día siguiente al dado. Utilizando
esta misma función, sin modificaciones ni agregados, desarrollar programas que permitan:
• Programa TP01-07A: Sumar N días a una fecha.
• Programa TP01-07B: Calcular la cantidad de días existentes entre dos fechas cualesquiera.

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
def diaSiguiente():
    dia = int(input('ingresar un dia del anio: '))
    mes = int(input('ingresar un mes del anio: '))
    anio = int(input('ingresar un anio: '))
    dia +=  1
    print(dia,mes,anio)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
    
diaSiguiente()