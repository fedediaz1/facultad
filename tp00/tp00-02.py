"""
-----------------------------------------------------------------------------------------------
Título: tp00-02 -  ASIENTOS DE CONFERENCIA 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Realizar un programa que permita ingresar la cantidad de inscriptos a una conferencia y la cantidad de asientos
disponibles en el auditorio. Se debe indicar si alcanzan los asientos. Si los asientos no alcanzan, indicar cuantos faltan para
que todos los inscriptos puedan sentarse. 
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

cantidadDePersonas = int(input('ingresar la cantidad de personas que van a asistir a la conferencia: '))
cantidadDeAsientos = int(input('Ingresar la cantidad de asientos disponibles en el auditorio: '))

if cantidadDeAsientos >= cantidadDePersonas:
    print('los',cantidadDeAsientos,'asientos, alcanzan para las',cantidadDePersonas,'personas,')
else:
    asientosFaltantes = cantidadDePersonas - cantidadDeAsientos
    print('faltarian un total de:',asientosFaltantes,'asientos')
    
