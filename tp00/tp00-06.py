

"""
-----------------------------------------------------------------------------------------------
Título: tp00-06 -  ASIENTOS DE CONFERENCIA 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Realizar un programa donde se vayan ingresando las calificaciones de los alumnos de un curso. Luego de ingresar la
calificación del último alumno, se ingresará un -1 para terminar la carga. El programa informará entonces la calificación
promedio del curso.
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

notaDelAlumno = int(input('ingresar la nota del primer alumno: '))
suma = 0
cantidad = 0

while notaDelAlumno != -1:
    suma += notaDelAlumno
    notaDelAlumno = int(input('ingresar la siguiente nota del siguiente alumno: '))
    cantidad += 1

print('el promedio de notas es de: ', suma/cantidad)