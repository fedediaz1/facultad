

"""
-----------------------------------------------------------------------------------------------
Título: tp00-05 -  ASIENTOS DE CONFERENCIA 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
En un mercado los clientes pueden comprar sólo una unidad de cada producto. Realizar un programa que pida uno por
uno los precios de los productos comprados por el cliente, y que al ingresar un precio igual a cero muestre el total que
debe abonar por la compra y la cantidad de productos comprados.
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
precio = int(input('ingresar el precio del producto seleccionado: '))
totaDeLaCompra = 0

while precio != 0:
    totaDeLaCompra += precio
    precio = int(input('ingresar valor del siguiente producto: '))

print('el total a pagar es de:', totaDeLaCompra)


