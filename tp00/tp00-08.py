"""
-----------------------------------------------------------------------------------------------
Título: TP00-08 - AUTONOMÍA DE VEHÍCULO
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Realizar un programa que solicite la carga de las temperaturas de todos los días de enero y al finalizar devuelva la
temperatura promedio, máxima y mínima del mes.

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
...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
temperaturaDelDia = 0
suma = 0
for i in range(32):
    temperaturaMaxima = 0
    temperaturaDelDia = int(input('Ingrese la temperatura del día:'))
    temperaturaMinima = temperaturaDelDia
    suma += temperaturaDelDia
    if temperaturaDelDia > temperaturaMaxima:
        temperaturaMaxima = temperaturaDelDia
    if temperaturaDelDia < temperaturaMinima:
        temperaturaMinima = temperaturaDelDia

print('La temperatura máxima es de:', temperaturaMaxima)
print('La temperatura mínima es de:', temperaturaMinima)
print('El promedio de temperatura de los 10 días es de:', suma / 31)
