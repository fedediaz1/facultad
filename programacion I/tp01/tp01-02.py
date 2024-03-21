"""
-----------------------------------------------------------------------------------------------
Título: TP01-02 - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Desarrollar una función que reciba tres números enteros positivos correspondientes al día, mes y año de una fecha, y
verifique si corresponden a una fecha válida. Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años
bisiestos. La función debe devolver True o False según la fecha sea correcta o no. Realizar también un programa para
verificar el comportamiento de la función.

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
def mesDiaAno (dia,mes,ano):
    if dia > 31 or mes == 12 or ano <= 0:
        return False
    elif mes == 2 and ano % 4 == 0:
        if dia <= 29:
            return True
        else:
            return False
    elif mes == 2 and ano % 4 != 0:
        if dia <= 28:
            return True
        else:
            return False
    elif dia <= 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and ano > 0:
        return True
    elif dia <= 30 and mes == 2 or mes == 4 or mes == 5 or mes == 9 or mes == 11 and ano > 0:
        return True



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
    
dia = int(input('ingresar un dia del ano: '))
mes = int(input('ingresar un mes del ano: '))
ano = int(input('ingresar un ano: '))

if mesDiaAno(dia,mes,ano) == True:
    print('el',dia,'-',mes,'-',ano,'es valido')
else:
    print('el',dia,'-',mes,'-',ano,'es invalido')