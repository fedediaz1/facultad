"""
-----------------------------------------------------------------------------------------------
Título: TP01-07 -  DÍA SIGUIENTE
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Escribir una función diaSiguiente() que reciba como parámetro una fecha cualquiera expresada por tres enteros
(correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes el día siguiente al dado. Utilizando
esta misma función, sin modificaciones ni agregados, desarrollar programas que permitan:
• Programa TP01-07A: Sumar N días a una fecha.
• Programa TP01-07B: Calcular la cantidad de días existentes entre dos fechas cualesquiera.

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
def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def diaSiguiente(dia, mes, anio):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if es_bisiesto(anio):
        dias_por_mes[2] = 29
    
    if dia < dias_por_mes[mes]:
        return dia + 1, mes, anio
    elif mes < 12:
        return 1, mes + 1, anio
    else:
        return 1, 1, anio + 1

def sumarNDias(dia, mes, anio, n):
    for _ in range(n):
        dia, mes, anio = diaSiguiente(dia, mes, anio)
    return dia, mes, anio
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
    


# Ejemplo de uso
dia, mes, anio = int(input('ingresar un dia del anio: ')), int(input('ingresar un mes del anio: ')), int(input('ingresar un anio: '))
n = int(input('ingresar una cantidad de dias para sumar'))
dia_siguiente, mes_siguiente, anio_siguiente = sumarNDias(dia, mes, anio, n)
print(f"La fecha después de sumar {n} días a {dia}/{mes}/{anio} es: {dia_siguiente}/{mes_siguiente}/{anio_siguiente}")
