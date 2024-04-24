"""
-----------------------------------------------------------------------------------------------
Título: TP02-01 - MES NÚMERO A TEXTO
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Escribir una función que reciba un número de mes y devuelva una cadena con el nombre del mes.
Probar la función desde un programa principal con un input para la entrada del número de mes, luego la llamada a la
función con dicho número como argumento, y finalmente un print de lo que la función devuelve.


Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def devolverNombreDelMes(numDelMes):
    mes = ''
    if numDelMes == 1:
        mes = 'enero'
    elif numDelMes == 2:
        mes = 'febreo'
    elif numDelMes == 3:
        mes = 'marzo'
    elif numDelMes == 4:
        mes = 'abril'
    elif numDelMes == 5:
        mes = 'mayo'
    elif numDelMes == 6:
        mes = 'junio'
    elif numDelMes == 7:
        mes = 'julio'
    elif numDelMes == 8:
        mes = 'agosto'
    elif numDelMes == 9:
        mes = 'septiembre'
    elif numDelMes == 10:
        mes = 'octubre'
    elif numDelMes == 11:
        mes = 'noviembre'
    else:
        mes = 'diciembre'
    return mes
    


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

numeroDelMes = int(input('ingresar un numero de mes'))

resultado = devolverNombreDelMes(numeroDelMes)

print(resultado)
