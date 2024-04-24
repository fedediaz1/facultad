
"""
-----------------------------------------------------------------------------------------------
Título: tp00-04 -  ASIENTOS DE CONFERENCIA 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Un banco necesita establecer los nuevos límites de crédito de sus tarjetas. Las de tipo 1 aumentarán un 25%; las de tipo
2 aumentarán un 35%; las de tipo 3 aumentarán un 40%, y las de cualquier otro tipo aumentarán un 50%. Desarrollar un
algoritmo para calcular el nuevo límite según el límite actual y el tipo de tarjeta del cliente.
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

limiteActual = int(input('Ingreasr el limite actual: '))
tipoDeTargetaDelCliente = int(input('ingresar si el tipo de targeta del cliente: '))

if tipoDeTargetaDelCliente == 1:
    limiteActual = limiteActual + (limiteActual * 0.25)
elif tipoDeTargetaDelCliente == 2:
    limiteActual = limiteActual + (limiteActual * 0.35)
elif tipoDeTargetaDelCliente == 3:
    limiteActual = limiteActual + (limiteActual * 0.40)
else:
    limiteActual = limiteActual + (limiteActual * 0.5)

    
print('el limite acutal es de:',limiteActual)