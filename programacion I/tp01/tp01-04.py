"""
-----------------------------------------------------------------------------------------------
Título: TP01-04 - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:

Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que
debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero
recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que
se minimice la cantidad de billetes. Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10. Emitir
un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $3170 y se abona con $5000, el
vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200, 1 billete de $100 y 3 billetes de $10.

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
def calcular_vuelto(compra, dinero_recibido):
    vuelto = dinero_recibido - compra
    
    if vuelto < 0:
        print("Error: El dinero recibido es insuficiente.")
        return
    
    billete5000 = vuelto // 5000
    vuelto %= 5000
    
    billete1000 = vuelto // 1000
    vuelto %= 1000
    
    billete500 = vuelto // 500
    vuelto %= 500
    
    billete200 = vuelto // 200
    vuelto %= 200
    
    billete100 = vuelto // 100
    vuelto %= 100
    
    billete50 = vuelto // 50
    vuelto %= 50
    
    billete10 = vuelto // 10
    
    print("El vuelto a entregar es:")
    if billete5000 > 0:
        print(billete5000,'billetes de 5.000')
    if billete1000 > 0:
        print(billete1000,'billetes de 1.000')
    if billete500 > 0:
        print(billete500,'billetes de 500')
    if billete200 > 0:
        print(billete200,'billetes de 200')
    if billete100 > 0:
        print(billete100,'billetes de 100')
    if billete50 > 0:
        print(billete50,'billetes de 50')
    if billete10 > 0:
        print(billete10,'billetes de 10')




#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

calcular_vuelto(compra, dinero_recibido)