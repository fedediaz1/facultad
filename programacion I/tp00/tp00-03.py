
"""
-----------------------------------------------------------------------------------------------
Título: tp00-03 -  ASIENTOS DE CONFERENCIA 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Escribir un programa básico de caja, donde se ingrese el precio total de la compra, luego se ingrese el monto con el cual
el cliente abona la compra, y finalmente informe con un mensaje si no es suficiente con lo que abonó o, caso contrario,
informe el vuelto que se le debe dar al cliente.
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

precioDeLaCompra = int(input('Ingresar el valor total de la compra: '))
monto = int(input('Ingresar el monto con el que abona el cliente: '))

if precioDeLaCompra > monto:
    print('no es suficiente la cantidad de dinero del cliente.')
else:
    vuelto = monto - precioDeLaCompra
    print('el vuelto es un total de: $',vuelto)