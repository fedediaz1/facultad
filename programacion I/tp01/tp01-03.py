"""
-----------------------------------------------------------------------------------------------
Título: TP01-03 - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que
dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita
desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el
total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.
                            Cantidad de viajes              Valor de 1 pasaje
                            --------------------------------------------------------------------------
                            |1 a 20                         Averiguar en internet el valor actualizado|
                            |21 a 30                        20% de descuento                          |
                            |31 a 40                        30% de descuento                          |
                            |41 o más                       40% de descuento                          |
                            ---------------------------------------------------------------------------
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
def tarifas(viajes):
    precio = 125
    if viajes > 0 and viajes <= 20:
        precio = precio * viajes
    elif viajes > 20 and viajes <= 30:
        precio *= 0.8 * viajes
    elif viajes > 30 and viajes <= 40:
        precio *= 0.7 * viajes
    else:
        precio *= 0.6 * viajes
    return precio

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
        
viajes = int(input('ingresar la cantidad de viajes ralizados en el mes: '))

resultado = tarifas(viajes)

print('el valor total de los viajes realizados es de: $',resultado)

