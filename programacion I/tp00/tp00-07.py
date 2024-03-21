

"""
-----------------------------------------------------------------------------------------------
Título: tp00-07 -  ASIENTOS DE CONFERENCIA 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Escribir un programa que, ingresado el precio de lista de un producto, muestre cuanto le costará al cliente según todas
las opciones de pago disponibles (si es en cuotas además del precio final debe mostrar el valor de cada cuota). Los
descuentos o recargos según las formas de pago son los siguientes:
En efectivo aplicar 10% de descuento
        Tarjeta 1 pago mantener el precio de lista
        Tarjeta 3 pagos recargar 5%
        Tarjeta 6 pagos recargar 10%
        Tarjeta 12 pagos recargar 15%
Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar si se ingresa un precio
de 0 pesos (en dicho caso debe terminar sin calcular nada). Se pide usar un tipo de bucle que evite tener que escribir el
input dos veces.
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
'''Escribir un programa que, ingresado el precio de lista de un producto, muestre cuanto le costará al cliente según todas
las opciones de pago disponibles (si es en cuotas además del precio final debe mostrar el valor de cada cuota). Los
descuentos o recargos según las formas de pago son los siguientes:
En efectivo aplicar 10% de descuento
        Tarjeta 1 pago mantener el precio de lista
        Tarjeta 3 pagos recargar 5%
        Tarjeta 6 pagos recargar 10%
        Tarjeta 12 pagos recargar 15%
Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar si se ingresa un precio
de 0 pesos (en dicho caso debe terminar sin calcular nada). Se pide usar un tipo de bucle que evite tener que escribir el
input dos veces.'''

precioDeLista = int(input('ingresar el precio de lista del producto: '))
total = 0 

while precioDeLista != 0:
    metodoDePago = input('si se paga en efectivo, escribir "efectivo", sino, escribir si se quiere pagar en 1, 3, 6 o 12 cuotas. tener en cuenta que las cuotas tienen interes: ')
    if metodoDePago == "efectivo":
        total = precioDeLista - (precioDeLista * 0.1)
        print('el total a pagar del primer producto es de:',total)
    elif metodoDePago != "efectivo":
        metodoDePago = int(metodoDePago)
        if metodoDePago == 1:
            total = precioDeLista
            print('el total a pagar del primer producto es de:',total)

        elif metodoDePago == 3:
            total = precioDeLista + (precioDeLista * 0.05)
            print('el total a pagar del primer producto es de:',total,'y debera pagar un total de:$',total/3,'por mes')

        elif metodoDePago == 6:
            total = precioDeLista + (precioDeLista * 0.1)
            print('el total a pagar del primer producto es de:',total,'y debera pagar un total de:$',total/6,'por mes')

        else:
            total = precioDeLista + (precioDeLista * 0.15)
            print('el total a pagar del primer producto es de:',total,'y debera pagar un total de:$',total/12,'por mes')


    precioDeLista = int(input('ingresar el precio de lista de otro producto'))

    